#!/usr/bin/env python3
"""LK OS sales reports: WhatsApp + DesignMD HTML previews.

Read-only generator for Lucas-approved sales reports. Fetches Shopify orders only,
keeps customer PII out, writes local JSON/WhatsApp/HTML artifacts, and prints a
sanitized WhatsApp message suitable for approval-gated delivery.
"""
from __future__ import annotations

import base64
import html
import json
import pathlib
import re
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
    'Fear of God', 'Essentials', 'Vans', 'Converse', 'Oakley', 'Hoka', 'Corteiz'
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


def http_json(url: str, *, headers: dict[str, str], timeout: int = 90) -> dict[str, Any]:
    req = urllib.request.Request(url, headers=headers, method='GET')
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


def order_seller_hint(order: dict[str, Any]) -> str:
    # Shopify REST POS can vary by app/version. Do not expose raw staff/user IDs
    # as "vendedor" in a sales group; report seller only when an explicit human
    # label exists in note attributes. Internal IDs require a mapping step.
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


def fetch_orders(secrets: dict[str, str], start_iso: str, end_iso: str) -> dict[str, Any]:
    store = (secrets.get('SHOPIFY_STORE_URL') or '').strip().replace('https://', '').replace('http://', '').strip('/')
    token = secrets.get('SHOPIFY_ACCESS_TOKEN') or ''
    if not store or not token:
        return {'ok': False, 'status': 'missing_shopify_credentials', 'orders': []}
    headers = {'X-Shopify-Access-Token': token, 'Accept': 'application/json'}
    base = f'https://{store}/admin/api/2024-01'
    fields = ','.join([
        'id','name','created_at','processed_at','total_price','currency','financial_status','fulfillment_status',
        'source_name','landing_site','referring_site','tags','line_items','discount_codes','note_attributes','location_id','user_id','staff_member_id'
    ])
    params = {
        'status': 'any',
        'limit': 250,
        'created_at_min': start_iso,
        'created_at_max': end_iso,
        'fields': fields,
        'order': 'created_at asc',
    }
    res = http_json(f'{base}/orders.json?' + urllib.parse.urlencode(params), headers=headers)
    return {'ok': bool(res.get('ok')), 'status': res.get('status'), 'orders': (res.get('body') or {}).get('orders') or []}


def summarize_orders(orders: list[dict[str, Any]]) -> dict[str, Any]:
    revenue = sum(as_float(o.get('total_price')) for o in orders)
    channels = defaultdict(lambda: {'orders': 0, 'revenue': 0.0})
    product_rows = {}
    brand_counter: Counter[str] = Counter()
    brand_revenue: Counter[str] = Counter()
    seller_counter: Counter[str] = Counter()
    seller_revenue: Counter[str] = Counter()
    source_counter: Counter[str] = Counter()
    no_sku = 0
    for order in orders:
        ch = classify_order_channel(order)
        rv = as_float(order.get('total_price'))
        channels[ch]['orders'] += 1
        channels[ch]['revenue'] += rv
        source_counter[order.get('source_name') or 'unknown'] += 1
        if ch == 'loja':
            seller = order_seller_hint(order)
            seller_counter[seller] += 1
            seller_revenue[seller] += rv
        for item in order.get('line_items') or []:
            title = item.get('title') or item.get('name') or 'Produto sem título'
            sku = (item.get('sku') or '').strip() or 'sem_sku'
            if sku == 'sem_sku':
                no_sku += 1
            variant = item.get('variant_title') or 'sem tamanho informado'
            qty = int(as_float(item.get('quantity')))
            line = as_float(item.get('price')) * qty
            brand = extract_brand(title)
            brand_counter[brand] += qty
            brand_revenue[brand] += line
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
        'seller_orders': seller_counter.most_common(10),
        'seller_revenue': [(k, round(v, 2)) for k, v in seller_revenue.most_common(10)],
        'source_names': source_counter.most_common(8),
        'no_sku_line_items': no_sku,
    }


def window_defs(now: datetime) -> dict[str, dict[str, Any]]:
    today = now.date()
    yesterday = today - timedelta(days=1)
    def dt(day, h, m, s):
        return datetime(day.year, day.month, day.day, h, m, s, tzinfo=SP_TZ)
    return {
        'morning_yesterday': {
            'label': f'Vendas de ontem — {yesterday.strftime("%d/%m")}',
            'start': dt(yesterday, 0, 0, 0),
            'end': dt(yesterday, 23, 59, 59),
            'kind': 'morning',
        },
        'pulse_16h': {
            'label': f'Pulso comercial — {today.strftime("%d/%m")} até {now.strftime("%H:%M")}',
            'start': dt(today, 0, 0, 0),
            'end': now,
            'kind': 'pulse',
        },
        'store_1930': {
            'label': f'Loja física — {today.strftime("%d/%m")} até {now.strftime("%H:%M")} (parcial antes de 19h30)' if now.hour < 19 or (now.hour == 19 and now.minute < 30) else f'Fechamento loja — {today.strftime("%d/%m")} até 19:30',
            'start': dt(today, 0, 0, 0),
            'end': min(now, dt(today, 19, 30, 0)),
            'kind': 'store',
        },
    }


def section_lines(key: str, data: dict[str, Any]) -> list[str]:
    s = data['summary']
    ch = s.get('channels') or {}
    online = ch.get('online', {'orders': 0, 'revenue': 0})
    loja = ch.get('loja', {'orders': 0, 'revenue': 0})
    top = (s.get('top_products') or [{}])[0]
    brand_qty = (s.get('top_brands_by_qty') or [('n/d', 0)])[0]
    lines = [
        f"*{data['label']}*",
        f"Total: {brl(s['revenue_total'])} em {s['orders_count']} vendas · TM {brl(s['average_order_value'])}",
    ]
    if key == 'store_1930':
        lines.append(f"Loja: {brl(loja.get('revenue'))} em {loja.get('orders', 0)} vendas")
        sellers = s.get('seller_revenue') or []
        if sellers and not (len(sellers) == 1 and sellers[0][0] in {'needs_data', 'needs_mapping_pos_staff_id'}):
            seller_text = '; '.join([f"{name}: {brl(val)}" for name, val in sellers[:3]])
        elif sellers and sellers[0][0] == 'needs_mapping_pos_staff_id':
            seller_text = 'needs_mapping: Shopify POS retornou ID interno, ainda sem nome do vendedor'
        else:
            seller_text = 'needs_data: campo vendedor ainda não confirmado no POS/Shopify'
        lines.append(f"Vendedores: {seller_text}")
    else:
        lines.append(f"Online: {brl(online.get('revenue'))} ({online.get('orders', 0)}) · Loja: {brl(loja.get('revenue'))} ({loja.get('orders', 0)})")
    if top:
        lines.append(f"Produto destaque: {top.get('product_title', 'n/d')} · {top.get('size_or_variant', 'n/d')} · qtd {top.get('quantity', 0)}")
    lines.append(f"Marca destaque: {brand_qty[0]} · qtd {brand_qty[1]}")
    if s.get('no_sku_line_items'):
        lines.append(f"Atenção: {s['no_sku_line_items']} item(ns) sem SKU")
    return lines


def make_whatsapp(payload: dict[str, Any]) -> str:
    lines = [
        '🟡 *LK OS · Reports de venda*',
        f"Gerado em {payload['generated_at_brt']} · fonte: Shopify read-only",
        '',
    ]
    for key in ['morning_yesterday', 'pulse_16h', 'store_1930']:
        lines += section_lines(key, payload['reports'][key])
        lines.append('')
    lines += [
        '*Notas*',
        '• E-commerce e loja/POS separados quando a fonte identifica POS.',
        '• Report 19h30 foi gerado como parcial se ainda antes de 19h30.',
        '• Campo vendedor: só será mostrado quando a fonte POS expuser dado confiável.',
        '• Sem dados de cliente, sem alteração em Shopify/Tiny/campanhas.',
    ]
    return scrub('\n'.join(lines).strip())


def make_html(payload: dict[str, Any]) -> str:
    cards = []
    for key in ['morning_yesterday', 'pulse_16h', 'store_1930']:
        report = payload['reports'][key]
        lines = section_lines(key, report)
        lis = ''.join(f'<li style="margin:0 0 10px 0;">{html.escape(line.replace("*", ""))}</li>' for line in lines[1:])
        cards.append(f'''
        <tr><td style="padding:28px 32px;background:#FFFFFF;border:1px solid #E8E6E2;">
          <div style="font-family:DM Sans,Arial,sans-serif;font-size:10px;letter-spacing:.22em;text-transform:uppercase;color:#8A8580;margin-bottom:12px;">{html.escape(report['kind'])}</div>
          <h2 style="font-family:Georgia,serif;font-size:28px;font-weight:400;line-height:1.05;margin:0 0 18px;color:#0A0A0A;">{html.escape(report['label'])}</h2>
          <ul style="font-family:DM Sans,Arial,sans-serif;font-size:14px;line-height:1.6;color:#1A1A1A;padding-left:18px;margin:0;">{lis}</ul>
        </td></tr><tr><td style="height:18px"></td></tr>''')
    return scrub(f'''<!doctype html><html><body style="margin:0;padding:0;background:#F0ECE8;">
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" bgcolor="#F0ECE8"><tr><td align="center" style="padding:28px 12px;">
<table role="presentation" width="640" cellspacing="0" cellpadding="0" style="max-width:640px;width:100%;">
<tr><td bgcolor="#0A0A0A" style="padding:30px 40px;text-align:center;color:#FFFFFF;font-family:DM Sans,Arial,sans-serif;font-size:18px;letter-spacing:.18em;">LK SNEAKERS</td></tr>
<tr><td bgcolor="#1A1A1A" style="padding:12px 40px;text-align:center;color:#E8D8C4;font-family:DM Sans,Arial,sans-serif;font-size:10px;letter-spacing:.22em;text-transform:uppercase;">Reports de venda · LK OS</td></tr>
<tr><td style="padding:44px 32px 24px;background:#FDF9F5;text-align:center;">
<h1 style="font-family:Georgia,serif;font-size:42px;font-weight:400;line-height:1;margin:0 0 14px;color:#0A0A0A;">Vendas com curadoria e clareza operacional</h1>
<p style="font-family:DM Sans,Arial,sans-serif;font-size:14px;line-height:1.7;color:#8A8580;margin:0;">Gerado em {html.escape(payload['generated_at_brt'])}. Fonte primária: Shopify Admin read-only. Sem PII de cliente.</p>
</td></tr>
<tr><td style="height:22px"></td></tr>
{''.join(cards)}
<tr><td bgcolor="#0A0A0A" style="padding:22px 32px;color:#E8D8C4;font-family:DM Sans,Arial,sans-serif;font-size:11px;line-height:1.6;">Separação online/loja depende de source_name/tags POS. Vendedor permanece needs_data até campo confiável ser validado.</td></tr>
</table></td></tr></table></body></html>''')


def main() -> int:
    now = datetime.now(SP_TZ)
    secrets = load_secrets()
    reports = {}
    for key, win in window_defs(now).items():
        result = fetch_orders(secrets, win['start'].isoformat(), win['end'].isoformat())
        orders = result.get('orders') or []
        if key == 'store_1930':
            orders = [o for o in orders if classify_order_channel(o) == 'loja']
        reports[key] = {
            'kind': win['kind'],
            'label': win['label'],
            'window': {'start': win['start'].isoformat(), 'end': win['end'].isoformat()},
            'shopify_ok': result.get('ok'),
            'shopify_status': result.get('status'),
            'summary': summarize_orders(orders),
        }
    payload = {
        'generated_at_utc': datetime.now(timezone.utc).isoformat(),
        'generated_at_brt': now.strftime('%d/%m/%Y %H:%M BRT'),
        'scope': 'LK OS sales reports: morning_yesterday, pulse_16h/current, store_1930/current_or_partial',
        'reports': reports,
        'guardrails': ['read_only_shopify', 'no_customer_pii', 'no_shopify_tiny_write', 'whatsapp_send_requires_current_approval'],
    }
    OUTDIR.mkdir(parents=True, exist_ok=True)
    stamp = now.strftime('%Y%m%dT%H%M%S%z')
    json_path = OUTDIR / f'lk-sales-reports-{stamp}.json'
    wa_path = OUTDIR / f'lk-sales-reports-whatsapp-{stamp}.txt'
    html_path = OUTDIR / f'lk-sales-reports-email-designmd-{stamp}.html'
    msg = make_whatsapp(payload)
    html_doc = make_html(payload)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')
    wa_path.write_text(msg, encoding='utf-8')
    html_path.write_text(html_doc, encoding='utf-8')
    print(json.dumps({'json': str(json_path), 'whatsapp': str(wa_path), 'html': str(html_path), 'message': msg}, ensure_ascii=False))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
