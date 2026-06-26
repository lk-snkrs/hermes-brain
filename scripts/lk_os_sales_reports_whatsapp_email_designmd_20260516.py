#!/usr/bin/env python3
# Auto-remediation contract (sensitive/productive review):
# Safe autonomous action here is limited to local comment/docs updates and
# sanitized read-only classification. Do not execute, send, mutate production,
# change credentials, or call external write APIs unless a scoped approval packet
# names target, risk, rollback/readback, and verification. Never print secret
# values; keep values_printed=false.
"""LK OS sales reports: WhatsApp + DesignMD HTML previews.

Read-only generator for Lucas-approved sales reports. Fetches Shopify orders only,
keeps customer PII out, writes local JSON/WhatsApp/HTML artifacts, and prints a
sanitized WhatsApp message suitable for approval-gated delivery.
"""
from __future__ import annotations

import argparse
import base64
import html
import json
import os
import pathlib
import re
import subprocess
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from typing import Any
from zoneinfo import ZoneInfo

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUTDIR = ROOT / 'reports' / 'lk-sales-reports'
DOPPLER_TOKEN_FILE = pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
SP_TZ = ZoneInfo('America/Sao_Paulo')

SECRET_PATTERNS = [
    re.compile(r'shp(at|ca|ss)_[A-Za-z0-9_\-]{20,}'),
    re.compile(r'dp\.st\.[A-Za-z0-9_\-]{20,}'),
    re.compile(r'gh[pousr]_[A-Za-z0-9_]{30,}'),
    re.compile(r'-----BEGIN [A-Z ]*PRIVATE KEY-----'),
    re.compile(r'(?i)(access_token|appsecret_proof|client_secret|token|key|secret|password)=([^&\s]+)'),
]
BRANDS = [
    'Onitsuka Tiger', 'New Balance', 'Nike', 'Jordan', 'Air Jordan', 'Adidas', 'adidas',
    'Represent', 'Asics', 'Mizuno', 'Puma', 'Salomon', 'UGG', 'Birkenstock', 'Crocs',
    'Fear of God', 'Essentials', 'Polo Ralph Lauren', 'Ralph Lauren', 'Vans', 'Converse', 'Oakley', 'Hoka', 'Corteiz'
]


def scrub(text: str) -> str:
    for pat in SECRET_PATTERNS:
        if pat.pattern.startswith('(?i)'):
            text = pat.sub(lambda m: f'{m.group(1)}=[REDACTED]', text)
        else:
            text = pat.sub('[REDACTED]', text)
    return text


def brl(value: float | int | None) -> str:
    if value is None:
        return 'n/d'
    return 'R$ ' + f'{float(value):,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


def as_float(value: Any) -> float:
    try:
        return float(value or 0)
    except Exception:
        return 0.0


def load_secrets() -> dict[str, str]:
    token = DOPPLER_TOKEN_FILE.read_text().strip()
    req = urllib.request.Request('https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json')
    req.add_header('Authorization', 'Basic ' + base64.b64encode((token + ':').encode()).decode())
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)


def http_json(url: str, *, headers: dict[str, str], timeout: int = 90, method: str = 'GET', body: dict[str, Any] | None = None) -> dict[str, Any]:
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode(errors='replace')
            return {'ok': True, 'status': resp.status, 'body': json.loads(raw) if raw else {}, 'headers': dict(resp.headers)}
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode(errors='replace')
        try:
            body = json.loads(raw) if raw else {}
        except Exception:
            body = {'raw': raw[:500]}
        return {'ok': False, 'status': exc.code, 'body': body}
    except Exception as exc:
        return {'ok': False, 'status': None, 'error': type(exc).__name__, 'message': str(exc)[:300]}


def classify_order_channel(order: dict[str, Any]) -> str:
    source = (order.get('source_name') or '').lower()
    tags = (order.get('tags') or '').lower()
    if source in {'pos', 'shopify_pos'} or 'pos' in tags or 'loja física' in tags or 'loja fisica' in tags:
        return 'loja'
    return 'online'


def extract_brand(title: str) -> str:
    tl = title.lower()
    # prefer multi-word before generic Jordan/Nike
    for brand in sorted(BRANDS, key=len, reverse=True):
        if brand.lower() in tl:
            return 'adidas' if brand == 'adidas' else brand
    # fallback: remove common category words and use first meaningful token
    cleaned = re.sub(r'^(t[eê]nis|chinelo|slide|moletom|camiseta|bon[eé]|jaqueta)\s+', '', title, flags=re.I).strip()
    return cleaned.split()[0] if cleaned else 'n/d'


def classify_sale_mix(title: str, item: dict[str, Any] | None = None) -> str:
    """Coarse commercial mix: tênis vs roupa vs outros.

    Shopify line_items in this report do not reliably include product_type, so
    classify from title/name first and keep ambiguous non-shoe items as outros
    instead of inflating roupa.
    """
    item = item or {}
    text = ' '.join(str(x or '') for x in [title, item.get('name'), item.get('variant_title'), item.get('vendor')]).lower()
    if re.search(r'\b(t[eê]nis|tenis|sneaker|shoe|sapato|chinelo|slide|sand[aá]lia|birkenstock|crocs|air force|dunk|jordan|samba|gazelle|campus|9060|204l|mexico 66|gel-|xt-6|speedcat)\b', text):
        return 'Tênis'
    if re.search(r'\b(camiseta|camisa|tee|t-shirt|cal[cç]a|pants|bermuda|shorts|jaqueta|jacket|moletom|hoodie|blusa|polo|sweatshirt)\b', text):
        return 'Roupa'
    return 'Outros'


def order_seller_hint(order: dict[str, Any]) -> str:
    # LK POS writes the human seller into order tags as "Vendedor: Nome".
    # Prefer this explicit tag over internal Shopify staff/user IDs.
    tags = str(order.get('tags') or '')
    for tag in [t.strip() for t in tags.split(',') if t.strip()]:
        m = re.match(r'(?i)^vendedor\s*:\s*(.+)$', tag)
        if m:
            seller = re.sub(r'\s+', ' ', m.group(1)).strip()
            if seller and not seller.isdigit():
                return seller[:80]

    note_attrs = order.get('note_attributes') or []
    for item in note_attrs:
        name = str(item.get('name') or '').lower()
        if any(k in name for k in ['seller', 'vendedor', 'staff', 'atendente']):
            val = str(item.get('value') or '').strip()
            if val and not val.isdigit():
                return val[:80]
    if any(order.get(key) for key in ('staff_member_id', 'user_id')):
        return 'needs_mapping_pos_staff_id'
    return 'needs_data'


def next_link(headers: dict[str, Any]) -> str | None:
    link = headers.get('Link') or headers.get('link') or ''
    for part in str(link).split(','):
        if 'rel="next"' in part:
            m = re.search(r'<([^>]+)>', part)
            if m:
                return m.group(1)
    return None


def b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b'=').decode()


def google_access_token_from_service_account(sa: dict[str, Any], scope: str) -> str:
    now = int(time.time())
    header = {'alg': 'RS256', 'typ': 'JWT'}
    claim = {'iss': sa['client_email'], 'scope': scope, 'aud': 'https://oauth2.googleapis.com/token', 'iat': now, 'exp': now + 3600}
    signing_input = (b64url(json.dumps(header, separators=(',', ':')).encode()) + '.' + b64url(json.dumps(claim, separators=(',', ':')).encode())).encode()
    key_path = None
    try:
        with tempfile.NamedTemporaryFile('w', delete=False) as f:
            key_path = f.name
            f.write(sa['private_key'])
        os.chmod(key_path, 0o600)
        proc = subprocess.run(['openssl', 'dgst', '-sha256', '-sign', key_path], input=signing_input, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    finally:
        if key_path:
            try:
                os.remove(key_path)
            except FileNotFoundError:
                pass
    assertion = signing_input.decode() + '.' + b64url(proc.stdout)
    data = urllib.parse.urlencode({'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer', 'assertion': assertion}).encode()
    req = urllib.request.Request('https://oauth2.googleapis.com/token', data=data, method='POST')
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    with urllib.request.urlopen(req, timeout=60) as resp:
        payload = json.load(resp)
    return payload['access_token']


def ga4_run_report(secrets: dict[str, str], start_date: str, end_date: str, *, limit: int = 1000) -> dict[str, Any]:
    sa_raw = secrets.get('GA4_LK_SERVICE_ACCOUNT') or secrets.get('GOOGLE_SERVICE_ACCOUNT_JSON')
    prop = secrets.get('GOOGLE_ANALYTICS_PROPERTY_ID') or secrets.get('GA4_LK_PROPERTY_ID') or secrets.get('GA4_PROPERTY_ID')
    if not sa_raw or not prop:
        return {'ok': False, 'status': 'missing_ga4_credentials', 'rows': []}
    try:
        token = google_access_token_from_service_account(json.loads(sa_raw), 'https://www.googleapis.com/auth/analytics.readonly')
        url = f'https://analyticsdata.googleapis.com/v1beta/properties/{prop}:runReport'
        body = {
            'dateRanges': [{'startDate': start_date, 'endDate': end_date}],
            'dimensions': [{'name': 'pagePath'}, {'name': 'pageTitle'}],
            'metrics': [{'name': 'screenPageViews'}, {'name': 'sessions'}, {'name': 'activeUsers'}],
            'limit': limit,
            'orderBys': [{'metric': {'metricName': 'screenPageViews'}, 'desc': True}],
        }
        res = http_json(url, method='POST', headers={'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}, body=body, timeout=90)
        rows = []
        for row in (res.get('body') or {}).get('rows') or []:
            dims = row.get('dimensionValues') or []
            mets = row.get('metricValues') or []
            rows.append({
                'path': dims[0].get('value') if len(dims) > 0 else '',
                'title': dims[1].get('value') if len(dims) > 1 else '',
                'views': int(as_float(mets[0].get('value') if len(mets) > 0 else 0)),
                'sessions': int(as_float(mets[1].get('value') if len(mets) > 1 else 0)),
                'users': int(as_float(mets[2].get('value') if len(mets) > 2 else 0)),
            })
        return {'ok': bool(res.get('ok')), 'status': res.get('status'), 'date_range': {'start': start_date, 'end': end_date}, 'rows': rows}
    except Exception as exc:
        return {'ok': False, 'status': 'exception', 'error': type(exc).__name__, 'message': str(exc)[:300], 'rows': []}


def page_label(path: str, title: str) -> str:
    if title and title != '(not set)':
        cleaned = re.sub(r'\s+[|–-]\s+LK Sneakers.*$', '', title).strip()
        cleaned = re.sub(r'\s+por\s+R\$\s+[\d\.,]+.*$', '', cleaned, flags=re.I).strip()
        return cleaned[:90]
    slug = path.strip('/').split('/')[-1].replace('-', ' ')
    return slug.title() if slug else path


def ga4_site_interest(secrets: dict[str, str], end_date: datetime) -> dict[str, Any]:
    current_start = (end_date.date() - timedelta(days=6)).isoformat()
    current_end = end_date.date().isoformat()
    previous_start = (end_date.date() - timedelta(days=13)).isoformat()
    previous_end = (end_date.date() - timedelta(days=7)).isoformat()
    current = ga4_run_report(secrets, current_start, current_end)
    previous = ga4_run_report(secrets, previous_start, previous_end)
    rows = current.get('rows') or []
    previous_rows = previous.get('rows') or []
    prev_by_path = {r.get('path'): r for r in previous_rows}
    current_totals = {
        'views': sum(int(r.get('views') or 0) for r in rows),
        'sessions': sum(int(r.get('sessions') or 0) for r in rows),
        'users': sum(int(r.get('users') or 0) for r in rows),
    }
    previous_totals = {
        'views': sum(int(r.get('views') or 0) for r in previous_rows),
        'sessions': sum(int(r.get('sessions') or 0) for r in previous_rows),
        'users': sum(int(r.get('users') or 0) for r in previous_rows),
    }
    collections = [r for r in rows if '/collections/' in r.get('path', '')][:3]
    products = [r for r in rows if '/products/' in r.get('path', '')][:3]
    rising = []
    for r in rows:
        if '/products/' not in r.get('path', ''):
            continue
        prev = prev_by_path.get(r.get('path'), {'views': 0})
        lift = int(r.get('views') or 0) - int(prev.get('views') or 0)
        if int(r.get('views') or 0) >= 10 and lift >= 5 and int(prev.get('views') or 0) <= max(20, int(r.get('views') or 0) * 0.7):
            rising.append({**r, 'previous_views': int(prev.get('views') or 0), 'lift': lift})
    rising = sorted(rising, key=lambda x: (x['lift'], x['views']), reverse=True)[:3]
    return {
        'ok': current.get('ok') and previous.get('ok'),
        'current_status': current.get('status'),
        'previous_status': previous.get('status'),
        'current_range': {'start': current_start, 'end': current_end},
        'previous_range': {'start': previous_start, 'end': previous_end},
        'current_totals': current_totals,
        'previous_totals': previous_totals,
        'top_collections_7d': collections,
        'top_products_7d': products,
        'rising_products': rising,
        'note': 'GA4 mede visitação/interesse; Shopify continua fonte oficial de pedidos/receita.',
    }


def fetch_orders(secrets: dict[str, str], start_iso: str, end_iso: str) -> dict[str, Any]:
    store = (secrets.get('SHOPIFY_STORE_URL') or '').strip().replace('https://', '').replace('http://', '').strip('/')
    token = secrets.get('SHOPIFY_ACCESS_TOKEN') or ''
    if not store or not token:
        return {'ok': False, 'status': 'missing_shopify_credentials', 'orders': [], 'pagination_complete': False}
    headers = {'X-Shopify-Access-Token': token, 'Accept': 'application/json'}
    base = f'https://{store}/admin/api/2024-01'
    fields = ','.join([
        'id','name','created_at','processed_at','cancelled_at','closed_at','total_price','currency','financial_status','fulfillment_status',
        'source_name','landing_site','referring_site','tags','line_items','discount_codes','note_attributes','location_id','user_id','staff_member_id','customer'
    ])
    params = {
        'status': 'any',
        'limit': 250,
        'created_at_min': start_iso,
        'created_at_max': end_iso,
        'fields': fields,
        'order': 'created_at asc',
    }
    url = f'{base}/orders.json?' + urllib.parse.urlencode(params)
    orders: list[dict[str, Any]] = []
    statuses: list[Any] = []
    pagination_complete = False
    for _ in range(20):
        res = http_json(url, headers=headers)
        statuses.append(res.get('status'))
        if not res.get('ok'):
            return {'ok': False, 'status': res.get('status'), 'orders': orders, 'pagination_complete': pagination_complete}
        orders.extend((res.get('body') or {}).get('orders') or [])
        nxt = next_link(res.get('headers') or {})
        if not nxt:
            pagination_complete = True
            break
        url = nxt
    return {'ok': True, 'status': statuses[-1] if statuses else None, 'orders': orders, 'orders_fetched': len(orders), 'pagination_complete': pagination_complete}


def is_reportable_order(order: dict[str, Any]) -> bool:
    if order.get('cancelled_at'):
        return False
    status = str(order.get('financial_status') or '').lower()
    return status not in {'voided', 'refunded'}


def summarize_orders(orders: list[dict[str, Any]]) -> dict[str, Any]:
    revenue = sum(as_float(o.get('total_price')) for o in orders)
    channels = defaultdict(lambda: {'orders': 0, 'revenue': 0.0})
    product_rows = {}
    brand_counter: Counter[str] = Counter()
    brand_revenue: Counter[str] = Counter()
    sale_mix_qty: Counter[str] = Counter()
    sale_mix_revenue = defaultdict(float)
    seller_counter: Counter[str] = Counter()
    seller_revenue: Counter[str] = Counter()
    store_known_customers = 0
    store_repeat_customer_orders = 0
    store_first_customer_orders = 0
    store_missing_customer_orders = 0
    source_counter: Counter[str] = Counter()
    financial_counter: Counter[str] = Counter()
    cancelled_count = 0
    no_sku = 0
    suspicious_sku = 0
    for order in orders:
        ch = classify_order_channel(order)
        rv = as_float(order.get('total_price'))
        channels[ch]['orders'] += 1
        channels[ch]['revenue'] += rv
        source_counter[order.get('source_name') or 'unknown'] += 1
        financial_counter[order.get('financial_status') or 'unknown'] += 1
        if order.get('cancelled_at'):
            cancelled_count += 1
        if ch == 'loja':
            seller = order_seller_hint(order)
            seller_counter[seller] += 1
            seller_revenue[seller] += rv
            customer = order.get('customer') or {}
            if customer:
                store_known_customers += 1
                if int(as_float(customer.get('orders_count'))) > 1:
                    store_repeat_customer_orders += 1
                else:
                    store_first_customer_orders += 1
            else:
                store_missing_customer_orders += 1
        line_items = order.get('line_items') or []
        line_subtotal = sum(as_float(item.get('price')) * int(as_float(item.get('quantity'))) for item in line_items)
        allocation_factor = (rv / line_subtotal) if line_subtotal > 0 else 1.0
        for item in line_items:
            title = item.get('title') or item.get('name') or 'Produto sem título'
            sku = (item.get('sku') or '').strip() or 'sem_sku'
            if sku == 'sem_sku':
                no_sku += 1
            elif sku.isdigit() and len(sku) >= 10:
                suspicious_sku += 1
            variant = item.get('variant_title') or 'sem tamanho informado'
            qty = int(as_float(item.get('quantity')))
            line = as_float(item.get('price')) * qty * allocation_factor
            brand = extract_brand(title)
            brand_counter[brand] += qty
            brand_revenue[brand] += line
            sale_family = classify_sale_mix(title, item)
            sale_mix_qty[sale_family] += qty
            sale_mix_revenue[sale_family] += line
            key = (title, sku, variant)
            row = product_rows.setdefault(key, {'product_title': title, 'sku': sku, 'size_or_variant': variant, 'quantity': 0, 'line_revenue_estimate': 0.0, 'channels': Counter()})
            row['quantity'] += qty
            row['line_revenue_estimate'] += line
            row['channels'][ch] += qty
    top_products = sorted(product_rows.values(), key=lambda x: (x['quantity'], x['line_revenue_estimate']), reverse=True)[:10]
    for row in top_products:
        row['line_revenue_estimate'] = round(row['line_revenue_estimate'], 2)
        row['channels'] = dict(row['channels'])
    return {
        'orders_count': len(orders),
        'revenue_total': round(revenue, 2),
        'average_order_value': round(revenue / len(orders), 2) if orders else 0,
        'channels': {k: {'orders': v['orders'], 'revenue': round(v['revenue'], 2)} for k, v in channels.items()},
        'top_products': top_products,
        'top_brands_by_qty': brand_counter.most_common(8),
        'top_brands_by_revenue': [(k, round(v, 2)) for k, v in brand_revenue.most_common(8)],
        'sale_mix_by_qty': sale_mix_qty.most_common(),
        'sale_mix_by_revenue': [(k, round(v, 2)) for k, v in sorted(sale_mix_revenue.items(), key=lambda kv: kv[1], reverse=True)],
        'seller_orders': seller_counter.most_common(10),
        'seller_revenue': [(k, round(v, 2)) for k, v in seller_revenue.most_common(10)],
        'store_repeat_customers': {
            'known_customer_orders': store_known_customers,
            'repeat_customer_orders': store_repeat_customer_orders,
            'first_customer_orders': store_first_customer_orders,
            'missing_customer_orders': store_missing_customer_orders,
            'repeat_rate_known_percent': round((store_repeat_customer_orders / store_known_customers) * 100, 1) if store_known_customers else None,
        },
        'source_names': source_counter.most_common(8),
        'financial_statuses': financial_counter.most_common(8),
        'cancelled_orders': cancelled_count,
        'no_sku_line_items': no_sku,
        'suspicious_sku_line_items': suspicious_sku,
    }


def window_defs(now: datetime) -> dict[str, dict[str, Any]]:
    today = now.date()
    yesterday = today - timedelta(days=1)
    two_days_ago = today - timedelta(days=2)
    def dt(day, h, m, s):
        return datetime(day.year, day.month, day.day, h, m, s, tzinfo=SP_TZ)
    def month_start(day):
        return datetime(day.year, day.month, 1, 0, 0, 0, tzinfo=SP_TZ)
    def previous_month_same_endpoint(endpoint: datetime) -> datetime:
        year = endpoint.year
        month = endpoint.month - 1
        if month == 0:
            year -= 1
            month = 12
        next_month = month + 1
        next_year = year
        if next_month == 13:
            next_month = 1
            next_year += 1
        last_day_prev_month = (datetime(next_year, next_month, 1, tzinfo=SP_TZ) - timedelta(days=1)).day
        day = min(endpoint.day, last_day_prev_month)
        return datetime(year, month, day, endpoint.hour, endpoint.minute, endpoint.second, tzinfo=SP_TZ)
    same_time_end = dt(yesterday, now.hour, now.minute, now.second)
    current_month_start = month_start(today)
    previous_month_end = previous_month_same_endpoint(now)
    previous_month_start = datetime(previous_month_end.year, previous_month_end.month, 1, 0, 0, 0, tzinfo=SP_TZ)
    return {
        'current_month_to_date': {
            'label': f'Mês atual — {current_month_start.strftime("%d/%m")} a {now.strftime("%d/%m %H:%M")}',
            'start': current_month_start,
            'end': now,
            'kind': 'month_to_date',
        },
        'previous_month_same_to_date': {
            'label': f'Mês anterior até o mesmo dia — {previous_month_start.strftime("%d/%m")} a {previous_month_end.strftime("%d/%m %H:%M")}',
            'start': previous_month_start,
            'end': previous_month_end,
            'kind': 'previous_month_to_date',
        },
        'two_days_ago_closed': {
            'label': f'Anteontem fechado — {two_days_ago.strftime("%d/%m")}',
            'start': dt(two_days_ago, 0, 0, 0),
            'end': dt(two_days_ago, 23, 59, 59),
            'kind': 'previous_baseline',
        },
        'morning_yesterday': {
            'label': f'Ontem fechado — {yesterday.strftime("%d/%m")}',
            'start': dt(yesterday, 0, 0, 0),
            'end': dt(yesterday, 23, 59, 59),
            'kind': 'morning',
        },
        'yesterday_same_time': {
            'label': f'Ontem até {now.strftime("%H:%M")} — {yesterday.strftime("%d/%m")}',
            'start': dt(yesterday, 0, 0, 0),
            'end': same_time_end,
            'kind': 'baseline_same_time',
        },
        'pulse_16h': {
            'label': f'Hoje parcial — {today.strftime("%d/%m")} até {now.strftime("%H:%M")}',
            'start': dt(today, 0, 0, 0),
            'end': now,
            'kind': 'pulse',
        },
        'store_1930': {
            'label': f'Loja física — {today.strftime("%d/%m")} até {now.strftime("%H:%M")} (parcial)' if now.hour < 19 or (now.hour == 19 and now.minute < 30) else f'Fechamento loja — {today.strftime("%d/%m")} até 19:30',
            'start': dt(today, 0, 0, 0),
            'end': min(now, dt(today, 19, 30, 0)),
            'kind': 'store',
        },
    }


def pct(part: float | int, total: float | int) -> str:
    total_f = float(total or 0)
    if total_f <= 0:
        return '0%'
    return f'{(float(part or 0) / total_f) * 100:.0f}%'.replace('.', ',')


def top_product_text(summary: dict[str, Any], *, limit: int = 2, numbered: bool = True) -> list[str]:
    products = summary.get('top_products') or []
    lines = []
    for idx, product in enumerate(products[:limit], 1):
        title = product.get('product_title', 'Produto n/d')
        variant = product.get('size_or_variant') or 'sem tamanho'
        qty = product.get('quantity', 0)
        prefix = f'{idx}. ' if numbered else ''
        lines.append(f'{prefix}{title} · {variant} · qtd {qty}')
    return lines or ['n/d']


def top_brand_text(summary: dict[str, Any], *, limit: int = 3) -> str:
    brands = summary.get('top_brands_by_qty') or []
    return ' · '.join(f'{name} ({qty})' for name, qty in brands[:limit]) if brands else 'n/d'


def sale_mix_text(summary: dict[str, Any]) -> str:
    mix_qty = dict(summary.get('sale_mix_by_qty') or [])
    mix_rev = dict(summary.get('sale_mix_by_revenue') or [])
    total_qty = sum(int(v or 0) for v in mix_qty.values())
    total_rev = sum(float(v or 0) for v in mix_rev.values())
    parts = []
    for label in ['Tênis', 'Roupa', 'Outros']:
        qty = int(mix_qty.get(label) or 0)
        rev = float(mix_rev.get(label) or 0)
        if qty or rev:
            parts.append(f'{label}: {qty} un. · {brl(rev)} · {pct(rev, total_rev)}')
    return ' | '.join(parts) if parts else 'n/d'


def brand_share_text(summary: dict[str, Any], *, limit: int = 8) -> str:
    raw_brands = summary.get('top_brands_by_revenue') or []
    known = {b.lower(): ('Adidas' if b.lower() == 'adidas' else b) for b in BRANDS}
    grouped = defaultdict(float)
    for name, value in raw_brands:
        label = known.get(str(name).lower(), 'Outras marcas')
        grouped[label] += float(value or 0)
    brands = sorted(grouped.items(), key=lambda kv: kv[1], reverse=True)
    total = float(summary.get('revenue_total') or 0)
    if total <= 0:
        total = sum(float(value or 0) for _, value in brands)
    parts = []
    for name, value in brands[:limit]:
        parts.append(f'{name}: {pct(value, total)} ({brl(value)})')
    return ' | '.join(parts) if parts else 'n/d'


def delta_percent_value(current: float | int, baseline: float | int) -> float | None:
    baseline_value = float(baseline or 0)
    if baseline_value == 0:
        return None
    return ((float(current or 0) - baseline_value) / baseline_value) * 100


def signed_int_delta(current: int | float, baseline: int | float) -> str:
    delta = int(current or 0) - int(baseline or 0)
    sign = '+' if delta >= 0 else ''
    return f'{sign}{delta}'


def channel_performance_lines(current: dict[str, Any], baseline: dict[str, Any], *, label: str) -> list[str]:
    """Split loja física vs site/e-commerce with absolute and percentage deltas.

    Lucas corrected that the COO read needs to know whether an overall fall is
    coming from the store or from the site. These lines must therefore show the
    channel revenue, order count and variation for each side, not only the total.
    """
    cur_ch = current.get('channels') or {}
    base_ch = baseline.get('channels') or {}
    loja = cur_ch.get('loja', {'orders': 0, 'revenue': 0})
    online = cur_ch.get('online', {'orders': 0, 'revenue': 0})
    loja_base = base_ch.get('loja', {'orders': 0, 'revenue': 0})
    online_base = base_ch.get('online', {'orders': 0, 'revenue': 0})
    loja_delta_pct = delta_percent_value(loja.get('revenue'), loja_base.get('revenue'))
    online_delta_pct = delta_percent_value(online.get('revenue'), online_base.get('revenue'))
    diagnosis = 'pressão equilibrada entre loja e site'
    if loja_delta_pct is not None and online_delta_pct is not None:
        if loja_delta_pct >= -3 and online_delta_pct < -8:
            diagnosis = 'loja sustentada; gargalo principal no site/e-commerce'
        elif online_delta_pct <= loja_delta_pct - 5:
            diagnosis = 'queda concentrada no site/e-commerce; foco em tráfego, conversão e páginas de maior interesse'
        elif loja_delta_pct <= online_delta_pct - 5:
            diagnosis = 'queda mais concentrada na loja física; foco em vitrine, abordagem e fluxo POS'
    return [
        f"• Loja física ({label}): {brl(loja.get('revenue'))} · {loja.get('orders', 0)} vendas · variação {delta_text(loja.get('revenue'), loja_base.get('revenue'))} · vendas {signed_int_delta(loja.get('orders', 0), loja_base.get('orders', 0))}",
        f"• Site/e-commerce ({label}): {brl(online.get('revenue'))} · {online.get('orders', 0)} vendas · variação {delta_text(online.get('revenue'), online_base.get('revenue'))} · vendas {signed_int_delta(online.get('orders', 0), online_base.get('orders', 0))}",
        f"• Diagnóstico canal: {diagnosis}.",
    ]


def count_delta_text(current: float | int, baseline: float | int) -> str:
    current_value = float(current or 0)
    baseline_value = float(baseline or 0)
    delta = current_value - baseline_value
    sign = '+' if delta >= 0 else ''
    pct_label = 'n/d'
    if baseline_value:
        pct_delta = (delta / baseline_value) * 100
        pct_sign = '+' if pct_delta >= 0 else ''
        pct_label = f'{pct_sign}{pct_delta:.1f}%'.replace('.', ',')
    return f'{sign}{int(delta)} ({pct_label})'


def ga4_performance_line(ga4: dict[str, Any]) -> str:
    current = ga4.get('current_totals') or {}
    previous = ga4.get('previous_totals') or {}
    if not current:
        return '• Performance site GA4: n/d'
    return (
        f"• Performance site GA4 7d: {int(current.get('sessions') or 0)} sessões "
        f"({count_delta_text(current.get('sessions'), previous.get('sessions'))}) · "
        f"{int(current.get('views') or 0)} views ({count_delta_text(current.get('views'), previous.get('views'))})"
    )


def month_performance_lines(payload: dict[str, Any]) -> list[str]:
    month = payload['reports'].get('current_month_to_date', {}).get('summary', {})
    previous = payload['reports'].get('previous_month_same_to_date', {}).get('summary', {})
    if not month:
        return ['• n/d']
    delta = delta_text(month.get('revenue_total'), previous.get('revenue_total')) if previous else 'n/d'
    lines = [
        f"• Mês atual: {brl(month.get('revenue_total'))} · {month.get('orders_count', 0)} vendas · ticket {brl(month.get('average_order_value'))}",
        f"• Mês anterior até o mesmo dia: {brl(previous.get('revenue_total'))} · {previous.get('orders_count', 0)} vendas · variação {delta}",
        *channel_performance_lines(month, previous, label='mês contra mês'),
        f"• Mix mês: {sale_mix_text(month)}",
        f"• Share marcas mês: {brand_share_text(month)}",
        '• Vendedores no mês: ' + seller_summary(month),
    ]
    return lines


def month_store_performance_lines(payload: dict[str, Any]) -> list[str]:
    """Store/POS-only monthly context for the 19h30 report.

    The 19h30 close must not drift into online/e-commerce reporting. The
    generator still computes full-month summaries for the 09h/16h reports, but
    store-close visible copy uses the POS-filtered monthly summary stored on
    each monthly report row.
    """
    month = (payload['reports'].get('current_month_to_date', {}) or {}).get('store_only_summary', {})
    previous = (payload['reports'].get('previous_month_same_to_date', {}) or {}).get('store_only_summary', {})
    if not month:
        return ['• n/d']
    delta = delta_text(month.get('revenue_total'), previous.get('revenue_total')) if previous else 'n/d'
    lines = [
        f"• Loja no mês: {brl(month.get('revenue_total'))} · {month.get('orders_count', 0)} vendas · ticket {brl(month.get('average_order_value'))}",
        f"• Loja no mês anterior até o mesmo dia: {brl(previous.get('revenue_total'))} · {previous.get('orders_count', 0)} vendas · variação {delta}",
        f"• Mix loja no mês: {sale_mix_text(month)}",
        f"• Share marcas loja no mês: {brand_share_text(month)}",
        '• Vendedores POS no mês: ' + seller_summary(month),
    ]
    return lines


def channel_summary(summary: dict[str, Any]) -> str:
    ch = summary.get('channels') or {}
    online = ch.get('online', {'orders': 0, 'revenue': 0})
    loja = ch.get('loja', {'orders': 0, 'revenue': 0})
    total = summary.get('revenue_total') or 0
    return (
        f"Online {brl(online.get('revenue'))} ({online.get('orders', 0)} vendas · {pct(online.get('revenue'), total)})\n"
        f"Loja {brl(loja.get('revenue'))} ({loja.get('orders', 0)} vendas · {pct(loja.get('revenue'), total)})"
    )


def seller_summary(summary: dict[str, Any]) -> str:
    sellers = summary.get('seller_revenue') or []
    if sellers and not (len(sellers) == 1 and sellers[0][0] in {'needs_data', 'needs_mapping_pos_staff_id'}):
        return '; '.join([f'{name}: {brl(val)}' for name, val in sellers[:3]])
    if sellers and sellers[0][0] == 'needs_mapping_pos_staff_id':
        return 'aguardando mapeamento dos vendedores do POS'
    return 'dado ainda não disponível com segurança no Shopify/POS'


def seller_performance_lines(summary: dict[str, Any], *, limit: int = 5) -> list[str]:
    sellers = summary.get('seller_revenue') or []
    seller_orders = dict(summary.get('seller_orders') or [])
    lines = []
    for name, value in sellers[:limit]:
        if name in {'needs_data', 'needs_mapping_pos_staff_id'}:
            continue
        orders = int(seller_orders.get(name, 0) or 0)
        ticket = (float(value or 0) / orders) if orders else 0
        lines.append(f'• {name}: {brl(value)} · {orders} venda(s) · ticket {brl(ticket)}')
    return lines or ['• dado de vendedor ainda não disponível com segurança no POS']


def delta_text(current: float | int, baseline: float | int) -> str:
    """Return financial delta plus percentage vs baseline.

    Example: -R$ 145.154,97 (-19,7%). Lucas corrected that
    LK reports must show both the absolute financial variation and
    the percentage variation in month/day comparison blocks.
    """
    current_value = float(current or 0)
    baseline_value = float(baseline or 0)
    delta = current_value - baseline_value
    sign = '+' if delta >= 0 else '-'
    pct_label = 'n/d'
    if baseline_value:
        pct_delta = (delta / baseline_value) * 100
        pct_sign = '+' if pct_delta >= 0 else ''
        pct_label = f'{pct_sign}{pct_delta:.1f}%'.replace('.', ',')
    return f'{sign}{brl(abs(delta))} ({pct_label})'


def quality_notes(payload: dict[str, Any]) -> list[str]:
    notes = []
    for key, report in payload.get('reports', {}).items():
        if not report.get('shopify_ok'):
            notes.append('dados Shopify incompletos; não usar como fechamento')
        if not report.get('pagination_complete', True):
            notes.append('paginação Shopify incompleta; leitura pode estar truncada')
    pulse = payload['reports']['pulse_16h']['summary']
    sku_empty = pulse.get('no_sku_line_items') or 0
    sku_suspicious = pulse.get('suspicious_sku_line_items') or 0
    if sku_empty:
        notes.append(f'{sku_empty} produto(s) vendidos com SKU vazio')
    if sku_suspicious:
        notes.append(f'{sku_suspicious} SKU(s) suspeito(s) para revisar')
    excluded = payload['reports']['pulse_16h'].get('orders_excluded') or 0
    if excluded:
        notes.append(f'{excluded} pedido(s) cancelado(s)/estornado(s) excluído(s) do cálculo')
    # de-duplicate while preserving order
    return list(dict.fromkeys(notes))


def section_lines(key: str, data: dict[str, Any]) -> list[str]:
    s = data['summary']
    lines = [
        f"*{data['label']}*",
        f"Receita: {brl(s['revenue_total'])}",
        f"Vendas: {s['orders_count']} · ticket médio {brl(s['average_order_value'])}",
    ]
    if key == 'store_1930':
        repeat = s.get('store_repeat_customers') or {}
        known = repeat.get('known_customer_orders') or 0
        repeat_orders = repeat.get('repeat_customer_orders') or 0
        repeat_rate = repeat.get('repeat_rate_known_percent')
        repeat_label = f'{repeat_rate:.1f}%'.replace('.', ',') if repeat_rate is not None else 'n/d'
        lines.append(f"Mix: {top_brand_text(s)}")
        lines.append(f"Tênis vs roupa: {sale_mix_text(s)}")
        lines.append(f"Vendedores: {seller_summary(s)}")
        lines.append(f"Recompra identificada: {repeat_orders} em {known} cliente(s) identificados · {repeat_label}")
        lines.append('Produto destaque: ' + top_product_text(s, limit=1, numbered=False)[0])
    else:
        lines.append('Canais:\n' + channel_summary(s))
        lines.append(f"Mix por unidades: {top_brand_text(s)}")
        lines.append(f"Tênis vs roupa: {sale_mix_text(s)}")
        lines.append('Produtos destaque:\n' + '\n'.join(top_product_text(s, limit=2)))
    if s.get('no_sku_line_items'):
        lines.append(f"Atenção de cadastro: {s['no_sku_line_items']} produto(s) vendidos com SKU vazio")
    return lines


def conclusion_lines(payload: dict[str, Any]) -> list[str]:
    yesterday = payload['reports']['morning_yesterday']['summary']
    same_time = payload['reports']['yesterday_same_time']['summary']
    pulse = payload['reports']['pulse_16h']['summary']
    store = payload['reports']['store_1930']['summary']
    same_hour_delta = delta_text(pulse.get('revenue_total'), same_time.get('revenue_total'))
    full_day_gap = delta_text(pulse.get('revenue_total'), yesterday.get('revenue_total'))
    return [
        '*Leitura COO*',
        f'• Hoje parcial vs ontem no mesmo horário: {same_hour_delta}.',
        f'• Hoje parcial vs ontem fechado: {full_day_gap} — referência, não fechamento.',
        f'• Loja está puxando o dia: {pct(store.get("revenue_total"), pulse.get("revenue_total"))} do vendido até agora.',
    ]


def action_lines(payload: dict[str, Any]) -> list[str]:
    pulse = payload['reports']['pulse_16h']['summary']
    actions = ['Time de loja: reforçar abordagem nos modelos/marcas do mix forte.']
    if pulse.get('no_sku_line_items') or pulse.get('suspicious_sku_line_items'):
        actions.append('Retaguarda: ajustar SKUs pendentes para preservar leitura de mix.')
    actions.append('Próximo check: fechamento loja 19h30.')
    return ['*Ações até o fechamento*'] + [f'• {a}' for a in actions]


def make_whatsapp_financial_pulse_16h(payload: dict[str, Any]) -> str:
    """Report 1/3: 16h financial pulse only.

    Does not include POS seller ranking, store deep-dive, or data-quality/SKU work.
    Those belong to the other scheduled reports.
    """
    reports = payload['reports']
    pulse = reports['pulse_16h']['summary']
    same_time = reports['yesterday_same_time']['summary']
    delta = float(pulse.get('revenue_total') or 0) - float(same_time.get('revenue_total') or 0)
    delta_label = delta_text(pulse.get('revenue_total'), same_time.get('revenue_total'))
    trend = 'acima' if delta >= 0 else 'abaixo'
    recovery_line = (
        f'Manter ritmo e proteger ticket médio; hoje está {delta_label} vs ontem no mesmo horário.'
        if delta >= 0
        else f'Recuperar {brl(abs(delta))} até o fechamento para igualar o ritmo de ontem.'
    )
    pulse_channels = pulse.get('channels') or {}
    same_channels = same_time.get('channels') or {}
    loja = pulse_channels.get('loja', {'orders': 0, 'revenue': 0})
    online = pulse_channels.get('online', {'orders': 0, 'revenue': 0})
    loja_yesterday = same_channels.get('loja', {'orders': 0, 'revenue': 0})
    online_yesterday = same_channels.get('online', {'orders': 0, 'revenue': 0})
    leading_channel = 'loja física' if float(loja.get('revenue') or 0) >= float(online.get('revenue') or 0) else 'e-commerce'
    lines = [
        '🟡 *LK OS · Pulso financeiro — 16h*',
        f"_{payload['generated_at_brt']}_",
        '_Fonte: Shopify · vendas registradas até agora · sem dados de cliente_',
        '',
        '*Placar até agora*',
        f"• Receita total: {brl(pulse['revenue_total'])}",
        f"• Vendas: {pulse['orders_count']} · ticket médio {brl(pulse['average_order_value'])}",
        f"• Ontem no mesmo horário: {brl(same_time['revenue_total'])} · {same_time['orders_count']} vendas",
        f"• Ritmo total: {delta_label} vs ontem no mesmo horário",
        f"• Tênis vs roupa hoje: {sale_mix_text(pulse)}",
        f"• Vendedores hoje: {seller_summary(pulse)}",
        '',
        '*Performance do mês*',
        *month_performance_lines(payload),
        '',
        '*Por canal até 16h*',
        f"• Loja física: {brl(loja.get('revenue'))} · {loja.get('orders', 0)} vendas · {pct(loja.get('revenue'), pulse.get('revenue_total'))}",
        f"• E-commerce: {brl(online.get('revenue'))} · {online.get('orders', 0)} vendas · {pct(online.get('revenue'), pulse.get('revenue_total'))}",
        f"• Loja vs ontem 16h: {delta_text(loja.get('revenue'), loja_yesterday.get('revenue'))} · vendas {signed_int_delta(loja.get('orders', 0), loja_yesterday.get('orders', 0))}",
        f"• Site/e-commerce vs ontem 16h: {delta_text(online.get('revenue'), online_yesterday.get('revenue'))} · vendas {signed_int_delta(online.get('orders', 0), online_yesterday.get('orders', 0))}",
        '',
        '*Leitura COO*',
        f'• O dia está {trend} de ontem no mesmo horário.',
        f'• Canal que mais está puxando: {leading_channel}.',
        f'• Mix que mais está puxando: {top_brand_text(pulse)}.',
        '',
        '*Ação até o fechamento*',
        f'• {recovery_line}',
        '• Usar o mix que já girou como argumento de venda agora.',
        '',
        '*Mix em destaque*',
    ]
    for name, qty in (pulse.get('top_brands_by_qty') or [])[:3]:
        lines.append(f'• {name}: {qty} un.')
    lines += [
        '',
        '*Próximo check*',
        '19h30 — fechamento da loja/dia.',
        '',
        '_Obs.: pedidos cancelados/estornados ficam fora do cálculo._',
    ]
    return scrub('\n'.join(lines).strip())


def ga4_item_lines(items: list[dict[str, Any]], *, rising: bool = False) -> list[str]:
    lines = []
    for item in items[:3]:
        label = page_label(item.get('path', ''), item.get('title', ''))
        if rising:
            lines.append(f"• {label}: {item.get('views', 0)} views · +{item.get('lift', 0)} vs 7 dias anteriores")
        else:
            lines.append(f"• {label}: {item.get('views', 0)} views")
    return lines or ['• n/d']


def make_whatsapp_previous_day_09h(payload: dict[str, Any]) -> str:
    """Report 2/3: 09h previous-day closed report."""
    reports = payload['reports']
    yesterday_report = reports['morning_yesterday']
    yesterday = yesterday_report['summary']
    baseline = reports.get('two_days_ago_closed', {}).get('summary', {})
    channels = yesterday.get('channels') or {}
    loja = channels.get('loja', {'orders': 0, 'revenue': 0})
    online = channels.get('online', {'orders': 0, 'revenue': 0})
    baseline_delta = delta_text(yesterday.get('revenue_total'), baseline.get('revenue_total')) if baseline else 'n/d'
    leading_channel = 'loja física' if float(loja.get('revenue') or 0) >= float(online.get('revenue') or 0) else 'e-commerce'
    lines = [
        '🟡 *LK OS · Reporte 09h — dia anterior*',
        f"_{payload['generated_at_brt']}_",
        f"_Referência: {yesterday_report['label'].replace('Ontem fechado — ', '')} · Shopify · sem dados de cliente_",
        '',
        '*Fechamento de ontem*',
        f"• Receita total: {brl(yesterday['revenue_total'])}",
        f"• Vendas: {yesterday['orders_count']} · ticket médio {brl(yesterday['average_order_value'])}",
        f"• Variação vs anteontem: {baseline_delta}",
        f"• Tênis vs roupa ontem: {sale_mix_text(yesterday)}",
        f"• Vendedores ontem: {seller_summary(yesterday)}",
        '',
        '*Performance do mês*',
        *month_performance_lines(payload),
        '',
        '*Por canal*',
        f"• Loja física: {brl(loja.get('revenue'))} · {loja.get('orders', 0)} vendas · {pct(loja.get('revenue'), yesterday.get('revenue_total'))}",
        f"• E-commerce: {brl(online.get('revenue'))} · {online.get('orders', 0)} vendas · {pct(online.get('revenue'), yesterday.get('revenue_total'))}",
        *channel_performance_lines(yesterday, baseline, label='vs anteontem'),
        '',
        '*Leitura COO*',
        f'• Canal que mais sustentou o dia: {leading_channel}.',
        f'• Mix principal: {top_brand_text(yesterday)}.',
        '• O 09h não deve prometer correção de um dia para o outro; ele orienta movimentos maiores da semana.',
        '',
        '*Movimentos para a semana*',
        '• Conversão: revisar páginas/coleções com visita alta e compra baixa antes de mexer em campanha.',
        '• Aquisição: usar os produtos em alta de visitação como sinal para mídia, conteúdo e vitrine.',
        '• Fidelidade: transformar o mix vencedor em régua de recompra/VIP, não apenas ação pontual do dia.',
        '',
        '*Produtos que mais apareceram*',
    ]
    lines += [f'• {line.lstrip("1234567890. ")}' for line in top_product_text(yesterday, limit=3, numbered=True)]
    ga4 = payload.get('ga4_site_interest') or {}
    if ga4.get('ok'):
        lines += [
            '',
            '*Interesse no site — últimos 7 dias*',
            ga4_performance_line(ga4),
            'Coleções mais visitadas:',
            *ga4_item_lines(ga4.get('top_collections_7d') or []),
            'Produtos mais visitados:',
            *ga4_item_lines(ga4.get('top_products_7d') or []),
            'Produtos começando a subir:',
            *ga4_item_lines(ga4.get('rising_products') or [], rising=True),
        ]
    else:
        lines += ['', '*Interesse no site — últimos 7 dias*', '• GA4 indisponível neste preview; manter como bloco obrigatório quando a API responder.']
    excluded = reports['morning_yesterday'].get('orders_excluded') or 0
    if excluded:
        lines += ['', f'_Obs.: {excluded} pedido(s) cancelado(s)/estornado(s) fora do cálculo._']
    return scrub('\n'.join(lines).strip())


def make_whatsapp_store_close_1930(payload: dict[str, Any]) -> str:
    """Report 3/3: 19h30 store/day close readout.

    Keep the WhatsApp message as an operational readout. Strategic decisions or
    next steps must be suggested separately to Lucas via Telegram.
    """
    reports = payload['reports']
    store = reports['store_1930']['summary']
    seller_lines = seller_performance_lines(store)
    month_seller_lines = seller_performance_lines((reports.get('current_month_to_date', {}) or {}).get('store_only_summary', {}))
    repeat = store.get('store_repeat_customers') or {}
    repeat_known = repeat.get('known_customer_orders') or 0
    repeat_count = repeat.get('repeat_customer_orders') or 0
    repeat_rate = repeat.get('repeat_rate_known_percent')
    repeat_text = f"{repeat_count} recompra(s) em {repeat_known} cliente(s) identificados" if repeat_known else 'dado de cliente não disponível com segurança'
    if repeat_rate is not None:
        repeat_text += f" · {str(repeat_rate).replace('.', ',')}%"
    lines = [
        '🟡 *LK OS · Fechamento 19h30 — loja física*',
        f"_{payload['generated_at_brt']}_",
        '_Fonte: Shopify POS · vendas registradas · sem dados de cliente_',
        '',
        '*Fechamento da loja*',
        f"• Receita loja: {brl(store['revenue_total'])}",
        f"• Vendas loja: {store['orders_count']} · ticket médio {brl(store['average_order_value'])}",
        f"• Mix loja: {top_brand_text(store)}",
        f"• Tênis vs roupa loja: {sale_mix_text(store)}",
        f"• Recompra identificada: {repeat_text}",
        '',
        '*Vendedores POS — hoje*',
    ]
    lines += seller_lines
    lines += [
        '',
        '*Performance do mês*',
        *month_store_performance_lines(payload),
        '',
        '*Vendedores POS — mês*',
    ]
    lines += month_seller_lines
    lines += [
        '',
        '*Produtos destaque da loja*',
    ]
    lines += [f'• {line.lstrip("1234567890. ")}' for line in top_product_text(store, limit=3, numbered=True)]
    lines += [
        '',
        '*Leitura COO*',
        f'• Loja fechou com ticket médio de {brl(store.get("average_order_value"))}.',
        f'• O mix da loja ficou concentrado em {top_brand_text(store)}.',
        '• Decisões estratégicas e próximos passos vão separadas para Lucas via Telegram.',
    ]
    excluded = reports['pulse_16h'].get('orders_excluded') or 0
    if excluded:
        lines += ['', f'_Obs.: {excluded} pedido(s) cancelado(s)/estornado(s) fora do cálculo._']
    return scrub('\n'.join(lines).strip())


def make_whatsapp(payload: dict[str, Any]) -> str:
    reports = payload['reports']
    yesterday = reports['morning_yesterday']['summary']
    same_time = reports['yesterday_same_time']['summary']
    pulse = reports['pulse_16h']['summary']
    notes = quality_notes(payload)
    lines = [
        '🟡 *LK OS · Vendas*',
        f"_{payload['generated_at_brt']}_",
        '_Fonte: vendas registradas · sem dados de cliente_',
        '',
        '*Resumo do dia*',
        f"• Hoje parcial: {brl(pulse['revenue_total'])} · {pulse['orders_count']} vendas · ticket médio {brl(pulse['average_order_value'])}",
        f"• Ontem mesmo horário: {brl(same_time['revenue_total'])} · {same_time['orders_count']} vendas · {delta_text(pulse['revenue_total'], same_time['revenue_total'])}",
        f"• Ontem fechado: {brl(yesterday['revenue_total'])} · {yesterday['orders_count']} vendas",
        '• Mix em destaque: ' + top_brand_text(pulse),
        '',
    ]
    lines += conclusion_lines(payload)
    lines += ['', *action_lines(payload), '', '━━━━━━━━━━━━━━']
    for key in ['pulse_16h', 'store_1930', 'morning_yesterday']:
        lines += section_lines(key, reports[key])
        lines += ['', '━━━━━━━━━━━━━━']
    if notes:
        lines += ['', '*Qualidade dos dados*']
        lines += [f'• {note}' for note in notes[:4]]
    lines += [
        '',
        '_Vendedor por tag POS. Estoque/margem exigem validação Tiny._',
    ]
    return scrub('\n'.join(lines).strip())


def make_html(payload: dict[str, Any]) -> str:
    """LK newsletter-standard HTML companion for the selected report."""
    report_type = payload.get('report_type') or 'all'
    key_map = {
        'pulse-finance-16h': ['pulse_16h'],
        'previous-day-09h': ['morning_yesterday'],
        'store-close-1930': ['store_1930'],
        'all': ['morning_yesterday', 'pulse_16h', 'store_1930'],
    }
    selected_keys = key_map.get(report_type, key_map['all'])
    title_map = {
        'pulse-finance-16h': ('Pulso financeiro', '16h'),
        'previous-day-09h': ('Dia anterior', '09h'),
        'store-close-1930': ('Fechamento', 'loja física'),
        'all': ('LK OS', 'vendas'),
    }
    subtitle_map = {
        'pulse-finance-16h': 'Leitura objetiva do ritmo do dia, com separação entre loja física e e-commerce.',
        'previous-day-09h': 'Fechamento do dia anterior para leitura semanal de conversão, aquisição e fidelidade.',
        'store-close-1930': 'Leitura exclusiva da loja física: vendedores, mix e recompra identificada no POS.',
        'all': 'Três leituras separadas, cada uma no seu horário e no seu escopo.',
    }
    title_a, title_b = title_map.get(report_type, title_map['all'])

    def metric(label: str, value: str, note: str = '') -> str:
        return f'''<td class="metric" width="33.33%">
          <div class="metric-label">{html.escape(label)}</div>
          <div class="metric-value">{html.escape(value)}</div>
          <div class="metric-note">{html.escape(note)}</div>
        </td>'''

    def products_html(summary: dict[str, Any]) -> str:
        products = summary.get('top_products') or []
        items = []
        for product in products[:3]:
            title = product.get('product_title') or 'Produto'
            variant = product.get('size_or_variant') or 'tamanho n/d'
            qty = product.get('quantity') or 0
            items.append(f'<li><span>{html.escape(title)}</span><small>{html.escape(str(variant))} · qtd {html.escape(str(qty))}</small></li>')
        return ''.join(items) or '<li><span>Sem produto destaque</span><small>n/d</small></li>'

    def sellers_html(summary: dict[str, Any]) -> str:
        sellers = summary.get('seller_revenue') or []
        seller_orders = dict(summary.get('seller_orders') or [])
        rows = []
        for name, value in sellers[:5]:
            orders = seller_orders.get(name, 0)
            avg = (float(value or 0) / orders) if orders else 0
            rows.append(f'''<tr>
              <td>{html.escape(str(name))}</td>
              <td align="right">{html.escape(brl(value))}</td>
              <td align="right">{html.escape(str(orders))}</td>
              <td align="right">{html.escape(brl(avg))}</td>
            </tr>''')
        return ''.join(rows) or '<tr><td colspan="4">Sem vendedor identificado com segurança.</td></tr>'

    def ga4_list_html(items: list[dict[str, Any]], *, rising: bool = False) -> str:
        rows = []
        for item in items[:3]:
            label = page_label(item.get('path', ''), item.get('title', ''))
            views = int(item.get('views') or 0)
            if rising:
                lift = int(item.get('lift') or 0)
                note = f'{views} views · +{lift} vs 7 dias anteriores'
            else:
                note = f'{views} views'
            rows.append(f'<li><span>{html.escape(label)}</span><small>{html.escape(note)}</small></li>')
        return ''.join(rows) or '<li><span>Sem dado suficiente</span><small>n/d</small></li>'

    def ga4_interest_html() -> str:
        ga4 = payload.get('ga4_site_interest') or {}
        if report_type != 'previous-day-09h':
            return ''
        if not ga4.get('ok'):
            status = ga4.get('current_status') or ga4.get('status') or 'indisponível'
            return f'''
    <section class="report ga4-report">
      <div class="eyebrow">GOOGLE ANALYTICS · SITE INTEREST</div>
      <h2>Interesse no site — últimos 7 dias</h2>
      <div class="panel soft"><p>GA4 indisponível neste envio ({html.escape(str(status))}). Shopify continua sendo a fonte oficial de pedidos e receita.</p></div>
    </section>'''
        current_totals = ga4.get('current_totals') or {}
        previous_totals = ga4.get('previous_totals') or {}
        return f'''
    <section class="report ga4-report">
      <div class="eyebrow">GOOGLE ANALYTICS · SITE PERFORMANCE</div>
      <h2>Performance e interesse no site — últimos 7 dias</h2>
      <table role="presentation" class="metric-row"><tr>
        {metric('Sessões GA4', str(int(current_totals.get('sessions') or 0)), count_delta_text(current_totals.get('sessions'), previous_totals.get('sessions')))}
        {metric('Views GA4', str(int(current_totals.get('views') or 0)), count_delta_text(current_totals.get('views'), previous_totals.get('views')))}
        {metric('Usuários GA4', str(int(current_totals.get('users') or 0)), count_delta_text(current_totals.get('users'), previous_totals.get('users')))}
      </tr></table>
      <div class="panel soft">
        <div class="panel-kicker">COLEÇÕES MAIS VISITADAS</div>
        <ul class="product-list">{ga4_list_html(ga4.get('top_collections_7d') or [])}</ul>
      </div>
      <div class="panel soft">
        <div class="panel-kicker">PRODUTOS MAIS VISITADOS</div>
        <ul class="product-list">{ga4_list_html(ga4.get('top_products_7d') or [])}</ul>
      </div>
      <div class="panel dark">
        <div class="panel-kicker">PRODUTOS COMEÇANDO A SUBIR</div>
        <ul class="product-list dark-list">{ga4_list_html(ga4.get('rising_products') or [], rising=True)}</ul>
      </div>
      <div class="metric-note">GA4 mede visitação/interesse; Shopify continua fonte oficial de pedidos e receita.</div>
    </section>'''

    def monthly_html() -> str:
        month = payload['reports'].get('current_month_to_date', {}).get('summary', {})
        previous = payload['reports'].get('previous_month_same_to_date', {}).get('summary', {})
        delta = delta_text(month.get('revenue_total'), previous.get('revenue_total')) if month and previous else 'n/d'
        month_channels = month.get('channels') or {}
        prev_channels = previous.get('channels') or {}
        loja = month_channels.get('loja', {'orders': 0, 'revenue': 0})
        online = month_channels.get('online', {'orders': 0, 'revenue': 0})
        loja_prev = prev_channels.get('loja', {'orders': 0, 'revenue': 0})
        online_prev = prev_channels.get('online', {'orders': 0, 'revenue': 0})
        channel_lines = '<br>'.join(html.escape(line.lstrip('• ')) for line in channel_performance_lines(month, previous, label='mês contra mês'))
        return f'''
    <section class="report month-report">
      <div class="eyebrow">PERFORMANCE DO MÊS</div>
      <h2>Mês contra mês, até o dia</h2>
      <table role="presentation" class="metric-row"><tr>
        {metric('Mês atual', brl(month.get('revenue_total')), f"{month.get('orders_count', 0)} vendas")}
        {metric('Mês anterior', brl(previous.get('revenue_total')), f"{previous.get('orders_count', 0)} vendas")}
        {metric('Variação', delta, 'mesmo dia e horário')}
      </tr></table>
      <table role="presentation" class="metric-row"><tr>
        {metric('Loja física mês', brl(loja.get('revenue')), f"{delta_text(loja.get('revenue'), loja_prev.get('revenue'))} · vendas {signed_int_delta(loja.get('orders', 0), loja_prev.get('orders', 0))}")}
        {metric('Site/e-commerce mês', brl(online.get('revenue')), f"{delta_text(online.get('revenue'), online_prev.get('revenue'))} · vendas {signed_int_delta(online.get('orders', 0), online_prev.get('orders', 0))}")}
        {metric('Diagnóstico canal', 'loja vs site', 'identificar onde caiu para priorizar foco')}
      </tr></table>
      <div class="panel soft"><p>{channel_lines}</p></div>
      <div class="panel soft">
        <div class="panel-kicker">MIX DO MÊS · TÊNIS VS ROUPA</div>
        <p>{html.escape(sale_mix_text(month))}</p>
      </div>
      <div class="panel soft">
        <div class="panel-kicker">SHARE DE MARCAS · MÊS</div>
        <p>{html.escape(brand_share_text(month))}</p>
      </div>
      <div class="panel dark">
        <div class="panel-kicker">VENDEDORES POS · MÊS</div>
        <table class="seller-table" role="presentation">
          <tr><th align="left">Vendedor</th><th align="right">Receita</th><th align="right">Vendas</th><th align="right">Ticket</th></tr>
          {sellers_html(month)}
        </table>
      </div>
    </section>'''

    def store_monthly_html() -> str:
        month = (payload['reports'].get('current_month_to_date', {}) or {}).get('store_only_summary', {})
        previous = (payload['reports'].get('previous_month_same_to_date', {}) or {}).get('store_only_summary', {})
        delta = delta_text(month.get('revenue_total'), previous.get('revenue_total')) if month and previous else 'n/d'
        return f'''
    <section class="report month-report">
      <div class="eyebrow">LOJA FÍSICA · MÊS</div>
      <h2>Loja física no mês, até o dia</h2>
      <table role="presentation" class="metric-row"><tr>
        {metric('Loja no mês', brl(month.get('revenue_total')), f"{month.get('orders_count', 0)} vendas")}
        {metric('Mês anterior', brl(previous.get('revenue_total')), f"{previous.get('orders_count', 0)} vendas")}
        {metric('Variação loja', delta, 'mesmo dia e horário')}
      </tr></table>
      <div class="panel soft">
        <div class="panel-kicker">MIX DA LOJA · MÊS</div>
        <p>{html.escape(sale_mix_text(month))}</p>
      </div>
      <div class="panel soft">
        <div class="panel-kicker">SHARE DE MARCAS · LOJA</div>
        <p>{html.escape(brand_share_text(month))}</p>
      </div>
      <div class="panel dark">
        <div class="panel-kicker">VENDEDORES POS · MÊS</div>
        <table class="seller-table" role="presentation">
          <tr><th align="left">Vendedor</th><th align="right">Receita</th><th align="right">Vendas</th><th align="right">Ticket</th></tr>
          {sellers_html(month)}
        </table>
      </div>
    </section>'''

    def report_card(key: str) -> str:
        report = payload['reports'][key]
        s = report['summary']
        title = html.escape(report['label'])
        revenue = brl(s.get('revenue_total'))
        orders = str(s.get('orders_count') or 0)
        avg = brl(s.get('average_order_value'))
        brands = top_brand_text(s)
        if key == 'store_1930':
            repeat = s.get('store_repeat_customers') or {}
            known = repeat.get('known_customer_orders') or 0
            repeat_orders = repeat.get('repeat_customer_orders') or 0
            repeat_rate = repeat.get('repeat_rate_known_percent')
            repeat_label = f'{repeat_rate:.1f}%'.replace('.', ',') if repeat_rate is not None else 'n/d'
            return f'''
    <section class="report">
      <div class="eyebrow">LOJA FÍSICA · POS</div>
      <h2>{title}</h2>
      <table role="presentation" class="metric-row"><tr>
        {metric('Receita loja', revenue, 'vendas POS válidas')}
        {metric('Vendas', orders, f'ticket médio {avg}')}
        {metric('Recompra', repeat_label, f'{repeat_orders} em {known} clientes')}
      </tr></table>
      <div class="split">
        <div class="panel soft">
          <div class="panel-kicker">MIX DA LOJA</div>
          <p>{html.escape(brands)}</p>
          <p><strong>Tênis vs roupa:</strong> {html.escape(sale_mix_text(s))}</p>
          <ul class="product-list">{products_html(s)}</ul>
        </div>
        <div class="panel dark">
          <div class="panel-kicker">VENDEDORES POS</div>
          <table class="seller-table" role="presentation">
            <tr><th align="left">Vendedor</th><th align="right">Receita</th><th align="right">Vendas</th><th align="right">Ticket</th></tr>
            {sellers_html(s)}
          </table>
        </div>
      </div>
    </section>'''
        ch = s.get('channels') or {}
        loja = ch.get('loja', {'orders': 0, 'revenue': 0})
        online = ch.get('online', {'orders': 0, 'revenue': 0})
        return f'''
    <section class="report">
      <div class="eyebrow">{html.escape(str(report.get('kind') or 'report')).upper()}</div>
      <h2>{title}</h2>
      <table role="presentation" class="metric-row"><tr>
        {metric('Receita total', revenue, f'{orders} vendas')}
        {metric('Loja física', brl(loja.get('revenue')), f"{loja.get('orders', 0)} vendas")}
        {metric('E-commerce', brl(online.get('revenue')), f"{online.get('orders', 0)} vendas")}
      </tr></table>
      <div class="panel soft">
        <div class="panel-kicker">MIX E PRODUTOS</div>
        <p>{html.escape(brands)}</p>
        <p><strong>Tênis vs roupa:</strong> {html.escape(sale_mix_text(s))}</p>
        <ul class="product-list">{products_html(s)}</ul>
      </div>
      <div class="panel dark">
        <div class="panel-kicker">VENDEDORES POS · PERÍODO</div>
        <table class="seller-table" role="presentation">
          <tr><th align="left">Vendedor</th><th align="right">Receita</th><th align="right">Vendas</th><th align="right">Ticket</th></tr>
          {sellers_html(s)}
        </table>
      </div>
    </section>'''

    # Daily/period read comes first; month-to-date context comes after it.
    # For the 09h report, include GA4 site-interest context in the email too,
    # not only in the WhatsApp text.
    monthly_block = store_monthly_html() if report_type == 'store-close-1930' else monthly_html()
    cards = ''.join(report_card(key) for key in selected_keys) + monthly_block + ga4_interest_html()
    return scrub(f'''<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>LK OS · Reports de venda</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400&family=Inter:wght@300;400;500;600&display=swap');
    * {{ box-sizing:border-box; }}
    body {{ margin:0; background:#FFFFFF; color:#111111; font-family:Inter, Arial, Helvetica, sans-serif; }}
    .frame {{ max-width:600px; margin:0 auto; background:#FFFFFF; }}
    .header {{ background:#050505; height:150px; display:flex; align-items:center; justify-content:center; text-align:center; }}
    .header img {{ display:block; width:78px; height:auto; }}
    .topline {{ background:#F8F5F1; padding:27px 20px 20px; text-align:center; border-bottom:1px solid #E5D7C9; }}
    .topline span {{ display:inline-block; font-size:11px; letter-spacing:6px; text-transform:uppercase; color:#8A6F5B; font-weight:400; }}
    .hero {{ background:#F2ECE4; padding:58px 42px 50px; text-align:center; border-bottom:1px solid #E5D7C9; position:relative; overflow:hidden; }}
    .hero:before {{ content:""; position:absolute; top:0; left:50%; transform:translateX(-50%); width:118px; height:5px; background:#B08A67; border-radius:0 0 999px 999px; }}
    .kicker {{ display:inline-block; font-size:10px; letter-spacing:6px; text-transform:uppercase; color:#8A6F5B; margin-bottom:24px; background:#FFFFFF; border:1px solid #E5D7C9; border-radius:999px; padding:11px 16px 10px 22px; }}
    h1 {{ margin:0; font-family:'Playfair Display', Georgia, 'Times New Roman', serif; font-weight:400; font-size:49px; line-height:.96; letter-spacing:-1.2px; }}
    h1 .warm {{ color:#B08A67; }}
    h1 em {{ color:#777777; font-style:italic; font-weight:400; }}
    .rule {{ width:38px; height:1px; background:#CDB49C; margin:25px auto 28px; }}
    .hero p {{ color:#6F6963; font-size:16px; line-height:1.85; margin:0 auto; max-width:430px; }}
    .report {{ padding:46px 44px 50px; border-bottom:1px solid #EEEEEE; background:#FFFFFF; }}
    .eyebrow, .panel-kicker {{ color:#9F9891; font-size:9px; letter-spacing:5px; text-transform:uppercase; margin-bottom:16px; font-weight:300; }}
    h2 {{ font-family:'Playfair Display', Georgia, 'Times New Roman', serif; font-size:34px; line-height:1.08; font-weight:400; margin:0 0 24px; color:#111111; }}
    .metric-row {{ width:100%; border-collapse:collapse; margin:0 0 28px; }}
    .metric {{ background:#F8F5F1; border:1px solid #E5D7C9; padding:22px 14px 20px; text-align:center; vertical-align:top; }}
    .metric-label {{ font-size:9px; letter-spacing:3px; color:#8A6F5B; text-transform:uppercase; margin-bottom:10px; }}
    .metric-value {{ font-family:'Playfair Display', Georgia, serif; font-size:24px; line-height:1.05; color:#111111; white-space:nowrap; }}
    .metric-note {{ color:#777777; font-size:11px; line-height:1.5; margin-top:9px; }}
    .split {{ display:block; }}
    .panel {{ padding:30px 32px 32px; margin-top:18px; }}
    .panel.soft {{ background:#EEE8E0; }}
    .panel.dark {{ background:#050505; color:#F8F8F8; }}
    .panel p {{ color:#6F6963; font-size:15px; line-height:1.8; margin:0 0 18px; }}
    .panel.dark .panel-kicker {{ color:#B5B0A8; }}
    .panel.dark .product-list li {{ border-top:1px solid rgba(255,255,255,.12); }}
    .panel.dark .product-list span {{ color:#F8F8F8; }}
    .panel.dark .product-list small {{ color:#B5B0A8; }}
    .product-list {{ list-style:none; margin:0; padding:0; }}
    .product-list li {{ padding:14px 0; border-top:1px solid rgba(17,17,17,.08); }}
    .product-list span {{ display:block; font-family:'Playfair Display', Georgia, serif; font-size:20px; line-height:1.18; color:#111111; }}
    .product-list small {{ display:block; margin-top:6px; font-size:11px; letter-spacing:2px; text-transform:uppercase; color:#8A6F5B; }}
    .seller-table {{ width:100%; border-collapse:collapse; color:#F8F8F8; font-size:12px; }}
    .seller-table th {{ color:#8A8A8A; font-size:9px; letter-spacing:2px; text-transform:uppercase; font-weight:400; padding:0 0 12px; }}
    .seller-table td {{ border-top:1px solid rgba(255,255,255,.12); padding:13px 0; color:#EDEBE8; }}
    .manifesto {{ background:#050505; color:#FFFFFF; margin:0; padding:58px 44px 50px; text-align:center; }}
    .manifesto p {{ font-family:'Playfair Display', Georgia, 'Times New Roman', serif; font-weight:400; font-style:italic; font-size:25px; line-height:1.45; margin:0 0 20px; color:#F8F8F8; }}
    .manifesto .sig {{ font-size:9px; letter-spacing:4px; text-transform:uppercase; color:#8A8A8A; }}
    .footer {{ background:#050505; padding:48px 44px 44px; text-align:center; color:#8A8A8A; }}
    .footer-logo {{ display:inline-block; margin-bottom:22px; width:66px; height:auto; }}
    .footer-slogan {{ font-family:'Playfair Display', Georgia, 'Times New Roman', serif; font-style:italic; font-size:15px; color:#B5B0A8; letter-spacing:.8px; line-height:1.45; margin-bottom:26px; }}
    .footer-rule {{ width:32px; height:1px; background:rgba(255,255,255,.14); margin:0 auto 22px; }}
    .address {{ font-size:11px; font-weight:300; line-height:1.9; color:#8A8A8A; }}
    @media (max-width:620px) {{
      .frame {{ max-width:100%; }}
      .hero {{ padding:54px 34px 44px; }}
      h1 {{ font-size:43px; }}
      .hero p {{ font-size:15px; }}
      .report {{ padding:40px 28px 44px; }}
      h2 {{ font-size:30px; }}
      .metric {{ display:block; width:100%; margin-bottom:10px; }}
      .panel {{ padding:28px 26px 30px; }}
    }}
  </style>
</head>
<body>
  <div style="display:none;max-height:0;overflow:hidden;opacity:0;color:transparent;line-height:1px;font-size:1px;">{html.escape(make_email_meta(payload)['preheader'])}</div>
  <main class="frame">
    <header class="header"><img alt="LK Sneakers" src="https://lksneakers.com.br/cdn/shop/files/LOGO-LK-BRANCO_885e01ed-68da-4988-b5a2-4ff4a10e238b.png?v=1763660281"></header>
    <section class="topline"><span>LK OS · REPORT OPERACIONAL</span></section>
    <section class="hero">
      <div class="kicker">{html.escape(payload['generated_at_brt'])}</div>
      <h1><span class="warm">{html.escape(title_a)}</span><br><em>{html.escape(title_b)}.</em></h1>
      <div class="rule"></div>
      <p>{html.escape(subtitle_map.get(report_type, subtitle_map['all']))}</p>
    </section>
    {cards}
    <section class="manifesto"><p>"O que é raro, merece ser acompanhado com precisão."</p><div class="sig">LK Sneakers</div></section>
    <footer class="footer">
      <img class="footer-logo" alt="LK Sneakers" src="https://lksneakers.com.br/cdn/shop/files/LOGO-LK-BRANCO_885e01ed-68da-4988-b5a2-4ff4a10e238b.png?v=1763660281">
      <div class="footer-slogan">O que é raro,<br>merece ser encontrado</div>
      <div class="footer-rule"></div>
      <div class="address">LK Sneakers · Rua Melo Alves, 344 · Jardins, São Paulo</div>
    </footer>
  </main>
</body>
</html>''')


def make_email_meta(payload: dict[str, Any]) -> dict[str, str]:
    """Subject/preheader package for the LK report email companion.

    These are internal/Lucas preview fields only. External sending remains
    approval-gated outside this generator.
    """
    report_type = payload.get('report_type') or 'all'
    reports = payload.get('reports') or {}
    generated = payload.get('generated_at_brt', '')
    if report_type == 'previous-day-09h':
        day_label = (reports.get('morning_yesterday') or {}).get('label', 'dia anterior').replace('Ontem fechado — ', '')
        summary = (reports.get('morning_yesterday') or {}).get('summary', {})
        subject = f'LK OS · Fechamento de ontem — {day_label}'
        preheader = f"Dia anterior: {brl(summary.get('revenue_total'))}, {summary.get('orders_count', 0)} vendas, mix, vendedores e leitura mês contra mês."
        headline = 'Fechamento de ontem para orientar semana, mix e conversão.'
    elif report_type == 'pulse-finance-16h':
        summary = (reports.get('pulse_16h') or {}).get('summary', {})
        subject = 'LK OS · Pulso financeiro 16h — ritmo do dia'
        preheader = f"Parcial 16h: {brl(summary.get('revenue_total'))}, {summary.get('orders_count', 0)} vendas, canais, mix e share mensal de marcas."
        headline = 'Pulso do dia para ajustar ritmo antes do fechamento.'
    elif report_type == 'store-close-1930':
        summary = (reports.get('store_1930') or {}).get('summary', {})
        subject = 'LK OS · Fechamento loja física — 19h30'
        preheader = f"Loja física: {brl(summary.get('revenue_total'))}, {summary.get('orders_count', 0)} vendas, vendedores POS, mix e mês."
        headline = 'Fechamento da loja física com vendedores, mix e mês.'
    else:
        summary = (reports.get('pulse_16h') or {}).get('summary', {})
        subject = f'LK OS · Reports de vendas — {generated[:10]}'
        preheader = f"Resumo operacional: {brl(summary.get('revenue_total'))}, canais, mix, vendedores e contexto mensal."
        headline = 'Resumo operacional consolidado.'
    return {
        'subject': subject,
        'preheader': preheader,
        'headline': headline,
        'generated_at_brt': generated,
        'report_type': str(report_type),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description='Generate LK OS sales reports.')
    parser.add_argument('--report', choices=['all', 'pulse-finance-16h', 'previous-day-09h', 'store-close-1930'], default='all')
    args = parser.parse_args()
    now = datetime.now(SP_TZ)
    if args.report == 'pulse-finance-16h':
        # Report 1 is the fixed 16h financial pulse. If previewed later in
        # the day, anchor the window to 16:00 instead of mixing in 19h30 data.
        report_cutoff = datetime(now.year, now.month, now.day, 16, 0, 0, tzinfo=SP_TZ)
        if now >= report_cutoff:
            now = report_cutoff
    elif args.report == 'previous-day-09h':
        # Report 2 is the fixed 09h previous-day close read. Anchor previews
        # to 09:00 so the artifact name and copy match the scheduled report.
        report_cutoff = datetime(now.year, now.month, now.day, 9, 0, 0, tzinfo=SP_TZ)
        if now >= report_cutoff:
            now = report_cutoff
    elif args.report == 'store-close-1930':
        # Report 3 is the fixed 19h30 store/day close read.
        report_cutoff = datetime(now.year, now.month, now.day, 19, 30, 0, tzinfo=SP_TZ)
        if now >= report_cutoff:
            now = report_cutoff
    secrets = load_secrets()
    reports = {}
    for key, win in window_defs(now).items():
        result = fetch_orders(secrets, win['start'].isoformat(), win['end'].isoformat())
        raw_orders = result.get('orders') or []
        excluded_orders = [o for o in raw_orders if not is_reportable_order(o)]
        orders = [o for o in raw_orders if is_reportable_order(o)]
        if key == 'store_1930':
            orders = [o for o in orders if classify_order_channel(o) == 'loja']
        reports[key] = {
            'kind': win['kind'],
            'label': win['label'],
            'window': {'start': win['start'].isoformat(), 'end': win['end'].isoformat()},
            'shopify_ok': result.get('ok'),
            'shopify_status': result.get('status'),
            'orders_fetched': result.get('orders_fetched', len(raw_orders)),
            'orders_excluded': len(excluded_orders),
            'excluded_financial_statuses': Counter([str(o.get('financial_status') or 'unknown') for o in excluded_orders]).most_common(8),
            'pagination_complete': result.get('pagination_complete'),
            'summary': summarize_orders(orders),
            'store_only_summary': summarize_orders([o for o in orders if classify_order_channel(o) == 'loja']),
        }
    payload = {
        'generated_at_utc': datetime.now(timezone.utc).isoformat(),
        'generated_at_brt': now.strftime('%d/%m/%Y %H:%M BRT'),
        'report_type': args.report,
        'scope': 'LK OS sales reports: today_partial, yesterday_same_time_baseline, store_current_or_1930, yesterday_closed',
        'reports': reports,
        'ga4_site_interest': ga4_site_interest(secrets, now) if args.report == 'previous-day-09h' else None,
        'guardrails': ['read_only_shopify', 'no_customer_pii', 'no_shopify_tiny_write', 'whatsapp_send_requires_current_approval'],
    }
    OUTDIR.mkdir(parents=True, exist_ok=True)
    stamp = now.strftime('%Y%m%dT%H%M%S%z')
    report_slug = args.report
    json_path = OUTDIR / f'lk-sales-reports-{report_slug}-{stamp}.json'
    wa_path = OUTDIR / f'lk-sales-reports-whatsapp-{report_slug}-{stamp}.txt'
    html_path = OUTDIR / f'lk-sales-reports-email-designmd-{report_slug}-{stamp}.html'
    email_meta_path = OUTDIR / f'lk-sales-reports-email-meta-{report_slug}-{stamp}.json'
    if args.report == 'pulse-finance-16h':
        msg = make_whatsapp_financial_pulse_16h(payload)
    elif args.report == 'previous-day-09h':
        msg = make_whatsapp_previous_day_09h(payload)
    elif args.report == 'store-close-1930':
        msg = make_whatsapp_store_close_1930(payload)
    else:
        msg = make_whatsapp(payload)
    email_meta = make_email_meta(payload)
    html_doc = make_html(payload)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')
    wa_path.write_text(msg, encoding='utf-8')
    html_path.write_text(html_doc, encoding='utf-8')
    email_meta_path.write_text(json.dumps(email_meta, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'json': str(json_path), 'whatsapp': str(wa_path), 'html': str(html_path), 'email_meta': str(email_meta_path), 'email': email_meta, 'message': msg}, ensure_ascii=False))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
