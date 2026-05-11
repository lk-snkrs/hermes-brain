#!/usr/bin/env python3
"""LK OS Weekly CEO Review, read-only.

Generates a weekly executive review from Shopify-confirmed sales, GA4 behavior,
Meta/Metricool platform signals and Tiny stock checks for the week's sold SKUs.
No sends, cron, campaigns, product/price/stock/customer edits, supplier contact,
DB writes or external actions. Secrets are fetched in-process from Doppler and
never printed.
"""
from __future__ import annotations

import base64
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
DOPPLER_TOKEN_FILE = pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_data_spine_snapshots')
PUBLIC_JSON = ROOT / 'reports/lk-os-weekly-ceo-review-2026-05-04_2026-05-10.json'
PUBLIC_MD = ROOT / 'reports/lk-os-weekly-ceo-review-2026-05-04_2026-05-10.md'
TELEGRAM_PREVIEW_JSON = ROOT / 'reports/lk-os-weekly-ceo-review-telegram-preview-2026-05-04_2026-05-10.json'
TELEGRAM_PREVIEW_MD = ROOT / 'reports/lk-os-weekly-ceo-review-telegram-preview-2026-05-04_2026-05-10.md'
OFFICIAL_DEPOSIT = 'LK | CONTROLE ESTOQUE'
SP_TZ = ZoneInfo('America/Sao_Paulo')
META_ACCOUNT_FALLBACK = 'act_1242062509867163'


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def closed_week_window() -> dict[str, str]:
    today_sp = datetime.now(SP_TZ).date()
    end_day = today_sp - timedelta(days=1)
    start_day = end_day - timedelta(days=6)
    start_dt = datetime(start_day.year, start_day.month, start_day.day, 0, 0, 0, tzinfo=SP_TZ)
    end_dt = datetime(end_day.year, end_day.month, end_day.day, 23, 59, 59, tzinfo=SP_TZ)
    return {
        'start_date': start_day.isoformat(),
        'end_date': end_day.isoformat(),
        'start_iso': start_dt.isoformat(),
        'end_iso': end_dt.isoformat(),
        'label': 'last_7_closed_days_brt',
    }


def brl(value: float | int | None) -> str:
    if value is None:
        return 'n/d'
    return 'R$ ' + f'{float(value):,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


def pct(value: float | int | None) -> str:
    if value is None:
        return 'n/d'
    return f'{float(value):.2%}'


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


def http_json(url: str, *, method: str = 'GET', headers: dict[str, str] | None = None, body: Any = None, timeout: int = 90) -> dict[str, Any]:
    data = None if body is None else json.dumps(body, ensure_ascii=False).encode()
    req = urllib.request.Request(url, data=data, method=method)
    for key, value in (headers or {}).items():
        req.add_header(key, value)
    if data is not None and not req.has_header('Content-Type'):
        req.add_header('Content-Type', 'application/json')
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode(errors='replace')
            return {'ok': True, 'status': resp.status, 'body': json.loads(raw) if raw else {}}
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode(errors='replace')
        try:
            parsed = json.loads(raw) if raw else {}
        except Exception:
            parsed = {'raw': raw[:500]}
        return {'ok': False, 'status': exc.code, 'body': parsed}
    except Exception as exc:
        return {'ok': False, 'status': None, 'error': type(exc).__name__, 'message': str(exc)[:300]}


def normalize_sku(value: str | None) -> str:
    return re.sub(r'[^A-Z0-9]', '', (value or '').upper())


def classify_order_channel(order: dict[str, Any]) -> str:
    source = (order.get('source_name') or '').lower()
    tags = (order.get('tags') or '').lower()
    if source in {'pos', 'shopify_pos'} or 'pos' in tags or 'loja física' in tags or 'loja fisica' in tags:
        return 'loja_fisica_or_pos'
    return 'online_or_unknown'


def shopify_week(secrets: dict[str, str], window: dict[str, str]) -> dict[str, Any]:
    store = (secrets.get('SHOPIFY_STORE_URL') or '').strip().replace('https://', '').replace('http://', '').strip('/')
    token = secrets.get('SHOPIFY_ACCESS_TOKEN') or ''
    if not store or not token:
        return {'source': 'Shopify', 'fact_label': 'fact_shopify', 'ok': False, 'status': 'missing_credentials'}
    headers = {'X-Shopify-Access-Token': token, 'Accept': 'application/json'}
    base = f'https://{store}/admin/api/2024-01'
    params = {
        'status': 'any',
        'limit': 250,
        'created_at_min': window['start_iso'],
        'created_at_max': window['end_iso'],
        'fields': 'id,name,created_at,total_price,currency,financial_status,fulfillment_status,source_name,landing_site,referring_site,tags,line_items,discount_codes',
        'order': 'created_at asc',
    }
    res = http_json(f'{base}/orders.json?' + urllib.parse.urlencode(params), headers=headers, timeout=90)
    orders = (res.get('body') or {}).get('orders') or [] if res.get('ok') else []
    gross = sum(as_float(o.get('total_price')) for o in orders)
    channels: dict[str, dict[str, Any]] = defaultdict(lambda: {'orders': 0, 'revenue': 0.0})
    sources: dict[str, dict[str, Any]] = defaultdict(lambda: {'orders': 0, 'revenue': 0.0})
    daily: dict[str, dict[str, Any]] = defaultdict(lambda: {'orders': 0, 'revenue': 0.0})
    product_rows: dict[tuple[str, str, str], dict[str, Any]] = {}
    sku_counter: Counter[str] = Counter()
    landing_counter: Counter[str] = Counter()
    ref_counter: Counter[str] = Counter()
    discount_counter: Counter[str] = Counter()
    no_sku_lines = 0
    for order in orders:
        revenue = as_float(order.get('total_price'))
        day = str(order.get('created_at') or '')[:10] or 'unknown'
        channel = classify_order_channel(order)
        source = order.get('source_name') or 'unknown'
        daily[day]['orders'] += 1
        daily[day]['revenue'] += revenue
        channels[channel]['orders'] += 1
        channels[channel]['revenue'] += revenue
        sources[source]['orders'] += 1
        sources[source]['revenue'] += revenue
        if order.get('landing_site'):
            landing_counter[str(order.get('landing_site'))[:120]] += 1
        if order.get('referring_site'):
            ref_counter[str(order.get('referring_site'))[:120]] += 1
        for dc in order.get('discount_codes') or []:
            code = dc.get('code')
            if code:
                discount_counter[code] += 1
        for item in order.get('line_items') or []:
            sku = (item.get('sku') or '').strip()
            title = item.get('title') or item.get('name') or 'Produto sem título'
            variant = item.get('variant_title') or 'sem tamanho informado'
            qty = int(as_float(item.get('quantity')))
            revenue_line = as_float(item.get('price')) * qty
            if not sku:
                no_sku_lines += 1
            else:
                sku_counter[sku] += qty
            key = (title, sku or 'sem_sku', variant)
            row = product_rows.setdefault(key, {'product_title': title, 'sku': sku or 'sem_sku', 'size_or_variant': variant, 'quantity': 0, 'line_revenue_estimate': 0.0, 'source_label': 'fact_shopify'})
            row['quantity'] += qty
            row['line_revenue_estimate'] += revenue_line
    top_products = sorted(product_rows.values(), key=lambda x: (x['quantity'], x['line_revenue_estimate']), reverse=True)[:20]
    for row in top_products:
        row['line_revenue_estimate'] = round(row['line_revenue_estimate'], 2)
    return {
        'source': 'Shopify',
        'fact_label': 'fact_shopify',
        'ok': bool(res.get('ok')),
        'api_status': res.get('status'),
        'date_range': {'start': window['start_iso'], 'end': window['end_iso']},
        'orders_count': len(orders),
        'revenue_total': round(gross, 2),
        'average_order_value': round(gross / len(orders), 2) if orders else 0,
        'daily': {k: {'orders': v['orders'], 'revenue': round(v['revenue'], 2)} for k, v in sorted(daily.items())},
        'channels': {k: {'orders': v['orders'], 'revenue': round(v['revenue'], 2)} for k, v in channels.items()},
        'source_names': {k: {'orders': v['orders'], 'revenue': round(v['revenue'], 2)} for k, v in sorted(sources.items(), key=lambda item: item[1]['revenue'], reverse=True)},
        'top_products': top_products,
        'top_skus': sku_counter.most_common(15),
        'discount_codes_count': sum(discount_counter.values()),
        'landing_site_sample': landing_counter.most_common(10),
        'referring_site_sample': ref_counter.most_common(10),
        'no_sku_line_items': no_sku_lines,
        'pii_minimization': 'Order customer fields not requested from Shopify.',
    }


def b64url(raw: bytes) -> str:
    return base64.urlsafe_b64encode(raw).decode().rstrip('=')


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
    data = urllib.parse.urlencode({'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer', 'assertion': signing_input.decode() + '.' + b64url(proc.stdout)}).encode()
    req = urllib.request.Request('https://oauth2.googleapis.com/token', data=data, method='POST')
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)['access_token']


def ga4_week(secrets: dict[str, str], window: dict[str, str]) -> dict[str, Any]:
    sa_raw = secrets.get('GA4_LK_SERVICE_ACCOUNT') or secrets.get('GOOGLE_SERVICE_ACCOUNT_JSON')
    prop = secrets.get('GOOGLE_ANALYTICS_PROPERTY_ID') or secrets.get('GA4_LK_PROPERTY_ID') or secrets.get('GA4_PROPERTY_ID')
    if not sa_raw or not prop:
        return {'source': 'GA4', 'fact_label': 'fact_ga4', 'ok': False, 'status': 'missing_credentials'}
    try:
        token = google_access_token_from_service_account(json.loads(sa_raw), 'https://www.googleapis.com/auth/analytics.readonly')
        url = f'https://analyticsdata.googleapis.com/v1beta/properties/{prop}:runReport'
        body = {
            'dateRanges': [{'startDate': window['start_date'], 'endDate': window['end_date']}],
            'dimensions': [{'name': 'sessionDefaultChannelGroup'}],
            'metrics': [{'name': m} for m in ['sessions', 'totalUsers', 'transactions', 'totalRevenue', 'sessionConversionRate']],
            'limit': 20,
            'orderBys': [{'metric': {'metricName': 'sessions'}, 'desc': True}],
        }
        res = http_json(url, method='POST', headers={'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}, body=body, timeout=90)
        rows = []
        for row in (res.get('body') or {}).get('rows') or []:
            label = row['dimensionValues'][0]['value']
            metrics = {name: as_float(m.get('value')) for name, m in zip(['sessions', 'totalUsers', 'transactions', 'totalRevenue', 'sessionConversionRate'], row.get('metricValues') or [])}
            rows.append({'channel': label, **metrics})
        totals = {'sessions': sum(r['sessions'] for r in rows), 'transactions': sum(r['transactions'] for r in rows), 'totalRevenue': round(sum(r['totalRevenue'] for r in rows), 2)}
        return {'source': 'GA4', 'fact_label': 'fact_ga4', 'ok': bool(res.get('ok')), 'api_status': res.get('status'), 'date_range': {'start': window['start_date'], 'end': window['end_date']}, 'totals': totals, 'top_channels': rows[:10], 'note': 'GA4 mede tráfego/canal/funil; Shopify é receita oficial.'}
    except Exception as exc:
        return {'source': 'GA4', 'fact_label': 'fact_ga4', 'ok': False, 'status': 'exception', 'error': type(exc).__name__, 'message': str(exc)[:300]}


def meta_week(secrets: dict[str, str], window: dict[str, str]) -> dict[str, Any]:
    token = secrets.get('META_ACCESS_TOKEN') or ''
    account = secrets.get('META_ADS_ACCOUNT_ID') or secrets.get('META_AD_ACCOUNT_ID') or META_ACCOUNT_FALLBACK
    if not token:
        return {'source': 'Meta Ads', 'fact_label': 'platform_signal', 'ok': False, 'status': 'missing_credentials'}
    acct = account if str(account).startswith('act_') else f'act_{account}'
    time_range = json.dumps({'since': window['start_date'], 'until': window['end_date']})
    qs = urllib.parse.urlencode({'access_token': token, 'time_range': time_range, 'fields': 'spend,impressions,clicks,actions,action_values', 'level': 'account'})
    res = http_json(f'https://graph.facebook.com/v20.0/{acct}/insights?{qs}', timeout=90)
    rows = (res.get('body') or {}).get('data') or [] if res.get('ok') else []
    row = rows[0] if rows else {}
    keys = ['offsite_conversion.fb_pixel_purchase', 'omni_purchase', 'purchase']
    def action_val(items: list[dict[str, Any]]) -> tuple[float, str | None]:
        vals = {i.get('action_type'): as_float(i.get('value')) for i in items or []}
        for key in keys:
            if key in vals:
                return vals[key], key
        return 0.0, None
    purchases, purchase_key = action_val(row.get('actions') or [])
    purchase_value, value_key = action_val(row.get('action_values') or [])
    spend = as_float(row.get('spend'))
    return {'source': 'Meta Ads', 'fact_label': 'platform_signal', 'ok': bool(res.get('ok')), 'api_status': res.get('status'), 'account_checked': acct, 'date_range': {'start': window['start_date'], 'end': window['end_date']}, 'rows': len(rows), 'spend': round(spend, 2), 'impressions': int(as_float(row.get('impressions'))), 'clicks': int(as_float(row.get('clicks'))), 'purchase_actions': purchases, 'purchase_action_key': purchase_key, 'purchase_value': round(purchase_value, 2), 'purchase_value_key': value_key, 'platform_roas': round(purchase_value / spend, 2) if spend else None, 'note': 'Meta é platform_signal, não receita final.'}


def metricool_week(secrets: dict[str, str], window: dict[str, str]) -> dict[str, Any]:
    token = secrets.get('METRICOOL_API_TOKEN') or secrets.get('METRICOOL_USER_TOKEN') or ''
    user_id = secrets.get('METRICOOL_USER_ID') or '4792967'
    blog_id = secrets.get('METRICOOL_BLOG_ID') or secrets.get('METRICOOL_LK_BRAND_ID') or '6217010'
    if not token:
        return {'source': 'Metricool Google Ads', 'fact_label': 'platform_signal', 'ok': False, 'status': 'missing_metricool_token', 'blog_id': blog_id}
    base_q = {'userId': user_id, 'blogId': blog_id, 'userToken': token}
    prof = http_json('https://app.metricool.com/api/admin/simpleProfiles?' + urllib.parse.urlencode(base_q), timeout=60)
    ad_q = {**base_q, 'from': window['start_date'] + 'T00:00:00', 'to': window['end_date'] + 'T23:59:59', 'timezone': 'America/Sao_Paulo', 'providers[]': 'adwords'}
    ads = http_json('https://app.metricool.com/api/v2/advertising/campaigns?' + urllib.parse.urlencode(ad_q), timeout=90)
    body = ads.get('body') if isinstance(ads.get('body'), dict) else {}
    rows = body.get('data') or body.get('campaigns') or body.get('items') or []
    if isinstance(rows, dict):
        rows = list(rows.values())
    brand_facts = []
    for item in (prof.get('body') or []) if isinstance(prof.get('body'), list) else []:
        if str(item.get('id') or item.get('blogId') or '') == str(blog_id):
            brand_facts.append({'label': item.get('label') or item.get('name'), 'id': item.get('id') or item.get('blogId'), 'timezone': item.get('timezone')})
    return {'source': 'Metricool Google Ads', 'fact_label': 'platform_signal', 'ok': bool(prof.get('ok') and ads.get('ok')), 'profile_status': prof.get('status'), 'ads_status': ads.get('status'), 'blog_id': blog_id, 'brand_facts': brand_facts[:3], 'date_range': {'start': window['start_date'], 'end': window['end_date']}, 'google_ads_rows': len(rows) if isinstance(rows, list) else None, 'note': 'Metricool/Google Ads é platform_signal, não receita final.'}


def tiny_call(token: str, method: str, params: dict[str, Any]) -> dict[str, Any]:
    started = time.perf_counter()
    data = urllib.parse.urlencode({**params, 'token': token, 'formato': 'json'}).encode()
    req = urllib.request.Request(f'https://api.tiny.com.br/api2/{method}.php', data=data, method='POST')
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            body = json.load(resp)
            return {'ok': True, 'status': resp.status, 'tiny_status': ((body or {}).get('retorno') or {}).get('status'), 'body': body, 'latency_ms': int((time.perf_counter() - started) * 1000)}
    except Exception as exc:
        return {'ok': False, 'status': None, 'tiny_status': None, 'error': type(exc).__name__, 'message': str(exc)[:300], 'latency_ms': int((time.perf_counter() - started) * 1000)}


def tiny_stock_for_sold_skus(secrets: dict[str, str], top_products: list[dict[str, Any]]) -> dict[str, Any]:
    token = secrets.get('TINY_API_TOKEN') or ''
    if not token:
        return {'source': 'Tiny', 'fact_label': 'fact_tiny_stock', 'ok': False, 'status': 'missing_credentials'}
    checks = []
    seen: set[str] = set()
    for product in top_products[:15]:
        sku = product.get('sku') or ''
        if not sku or sku == 'sem_sku' or sku in seen:
            continue
        seen.add(sku)
        time.sleep(1.25)
        search = tiny_call(token, 'produtos.pesquisa', {'pesquisa': sku, 'pagina': 1})
        rows = (((search.get('body') or {}).get('retorno') or {}).get('produtos') or []) if search.get('body') else []
        candidates = []
        for item in rows[:10]:
            p = (item or {}).get('produto') or {}
            candidates.append({'id': str(p.get('id') or ''), 'codigo': p.get('codigo') or '', 'nome': p.get('nome'), 'exact_norm_sku': normalize_sku(p.get('codigo') or '') == normalize_sku(sku)})
        exact = next((c for c in candidates if c['exact_norm_sku'] and c['id']), None)
        chosen = exact or (candidates[0] if len(candidates) == 1 else None)
        official = None
        if chosen:
            time.sleep(1.25)
            st = tiny_call(token, 'produto.obter.estoque', {'id': chosen['id']})
            prod = (((st.get('body') or {}).get('retorno') or {}).get('produto') or {}) if st.get('body') else {}
            for dep_item in prod.get('depositos') or []:
                dep = dep_item.get('deposito') or {}
                if dep.get('nome') == OFFICIAL_DEPOSIT:
                    try:
                        saldo = float(str(dep.get('saldo')).replace(',', '.')) if dep.get('saldo') is not None else None
                    except Exception:
                        saldo = None
                    official = {'deposit': OFFICIAL_DEPOSIT, 'saldo': saldo, 'saldo_raw_present': dep.get('saldo') is not None}
        sold_qty = int(product.get('quantity') or 0)
        saldo = official.get('saldo') if official else None
        risk = 'unknown'
        if saldo is not None:
            if saldo <= 0:
                risk = 'ruptura'
            elif saldo <= sold_qty:
                risk = 'baixo_estoque_vs_venda_da_semana'
            else:
                risk = 'ok_amostra'
        checks.append({'source_label': 'fact_tiny_stock', 'product_title': product.get('product_title'), 'sku': sku, 'size_or_variant': product.get('size_or_variant'), 'sold_qty_fact_shopify': sold_qty, 'candidate_count': len(candidates), 'chosen_tiny_id': chosen.get('id') if chosen else None, 'chosen_match_quality': 'exact_norm_sku' if exact else ('single_candidate' if chosen else 'no_safe_candidate'), 'official_deposit': official, 'stock_risk': risk})
    return {'source': 'Tiny', 'fact_label': 'fact_tiny_stock', 'ok': True, 'deposit': OFFICIAL_DEPOSIT, 'checks_count': len(checks), 'risk_counts': dict(Counter(c['stock_risk'] for c in checks)), 'critical_or_unknown': [c for c in checks if c['stock_risk'] in {'ruptura', 'baixo_estoque_vs_venda_da_semana', 'unknown'}][:12], 'checks': checks, 'scope_note': 'Read-only. Estoque consultado só para SKUs vendidos na semana, não auditoria completa de catálogo.'}


def build_recommendations(shopify: dict[str, Any], ga4: dict[str, Any], tiny: dict[str, Any], meta: dict[str, Any], metricool: dict[str, Any]) -> list[dict[str, Any]]:
    recs = []
    if not shopify.get('ok') or not ga4.get('ok') or not tiny.get('ok'):
        recs.append({'priority': 'P0', 'source_label': 'derived_reconciliation', 'action': 'Resolver falha de fonte antes de usar o review para decisão.', 'why': 'Shopify, GA4 e Tiny são fontes base do review semanal.', 'approval_required': 'Não para diagnóstico; sim para credenciais/infra.'})
    risk_counts = tiny.get('risk_counts') or {}
    rupture_count = int(risk_counts.get('ruptura') or 0)
    low_count = int(risk_counts.get('baixo_estoque_vs_venda_da_semana') or 0)
    unknown_count = int(risk_counts.get('unknown') or 0)
    if rupture_count:
        recs.append({'priority': 'P0', 'source_label': 'derived_reconciliation', 'action': 'Preparar fila de sourcing/reposição para SKUs vendidos na semana com saldo zero no Tiny.', 'why': f'{rupture_count} SKU(s) vendidos aparecem em ruptura no depósito oficial.', 'approval_required': 'Sim, antes de compra/fornecedor/Notion.'})
    if low_count:
        recs.append({'priority': 'P1', 'source_label': 'derived_reconciliation', 'action': 'Revisar cobertura dos SKUs com venda semanal encostando no saldo oficial.', 'why': f'{low_count} SKU(s) têm saldo menor ou igual à venda da semana.', 'approval_required': 'Sim, se virar compra, preço ou contato.'})
    if unknown_count:
        recs.append({'priority': 'P1', 'source_label': 'derived_reconciliation', 'action': 'Priorizar saneamento SKU Shopify ↔ Tiny antes de escalar mídia dos produtos vendidos.', 'why': f'{unknown_count} SKU(s) vendidos sem candidato Tiny seguro ou sem saldo legível.', 'approval_required': 'Sim, se exigir write em cadastro.'})
    sessions = ((ga4.get('totals') or {}).get('sessions') or 0) if ga4.get('ok') else 0
    orders = shopify.get('orders_count') or 0
    if sessions and orders:
        conv = orders / sessions
        if conv < 0.003:
            recs.append({'priority': 'P1', 'source_label': 'derived_reconciliation', 'action': 'Investigar CRO semanal por canal de alto tráfego e baixa compra.', 'why': f'Conversão aproximada Shopify pedidos / GA4 sessões em {conv:.2%}.', 'approval_required': 'Não para diagnóstico; sim para PDP/tema/preço.'})
    if meta.get('ok') and meta.get('spend') and shopify.get('revenue_total'):
        spend_share = meta['spend'] / shopify['revenue_total']
        recs.append({'priority': 'P2', 'source_label': 'derived_reconciliation', 'action': 'Usar Meta como sinal de mídia e reconciliar campanhas com landing/referrer/cupom antes de falar em ROAS real.', 'why': f'Gasto Meta sinalizado equivale a {spend_share:.1%} da receita Shopify semanal, sem prova SKU por campanha ainda.', 'approval_required': 'Não para análise; sim para campanha.'})
    if not metricool.get('ok'):
        recs.append({'priority': 'P2', 'source_label': 'platform_signal', 'action': 'Revisar conexão Metricool/Google Ads se o Weekly Review exigir mídia Google completa.', 'why': 'Metricool/Google Ads não retornou OK nesta execução.', 'approval_required': 'Não para diagnóstico; sim para mexer em credencial/configuração.'})
    return recs[:7]


def sanitize_for_public(report: dict[str, Any]) -> dict[str, Any]:
    blocked = {'email', 'phone', 'customer', 'address', 'token', 'api_key', 'authorization', 'first_name', 'last_name', 'cpf', 'cnpj'}
    def scrub(value: Any) -> Any:
        if isinstance(value, dict):
            return {key: ('[REDACTED]' if any(b in key.lower() for b in blocked) else scrub(val)) for key, val in value.items()}
        if isinstance(value, list):
            return [scrub(item) for item in value]
        return value
    public = scrub(report)
    public.pop('private_notes', None)
    return public


def build_telegram_preview(public: dict[str, Any], *, explicit_request: bool = False) -> dict[str, Any]:
    shop = public['sources']['shopify']
    ga4 = public['sources']['ga4']
    tiny = public['sources']['tiny_stock']
    meta = public['sources']['meta_ads']
    metricool = public['sources']['metricool_google_ads']
    recs = public.get('recommendations') or []
    priorities = {r.get('priority') for r in recs}
    api_failure = not (shop.get('ok') and ga4.get('ok') and tiny.get('ok'))
    has_p0_p1 = bool({'P0', 'P1'} & priorities)
    would_notify = bool(explicit_request or api_failure or has_p0_p1)
    trigger = 'explicit_request' if explicit_request else ('api_failure' if api_failure else ('p0_p1_anomaly' if has_p0_p1 else 'silent_no_anomaly'))
    sessions = int(((ga4.get('totals') or {}).get('sessions') or 0))
    orders = int(shop.get('orders_count') or 0)
    conv = orders / sessions if sessions else None
    lines = [
        f"**LK OS Weekly CEO Review, {public['week']['start_date']} a {public['week']['end_date']}**",
        f"Preview interno, não enviado automaticamente. Gatilho: `{trigger}`." if would_notify else 'Silêncio recomendado: sem P0/P1, sem falha de fonte e sem pedido explícito.',
        '',
        f"• Shopify: **{brl(shop.get('revenue_total'))}** em **{orders} pedidos**. Fonte: `fact_shopify`.",
        f"• GA4: **{sessions} sessões**, **{int(((ga4.get('totals') or {}).get('transactions') or 0))} transações GA4**. Fonte: `fact_ga4`, não receita oficial.",
        f"• Conversão aproximada: **{pct(conv)}** pedidos Shopify / sessões GA4.",
        f"• Tiny: ruptura `{(tiny.get('risk_counts') or {}).get('ruptura', 0)}`, baixo estoque `{(tiny.get('risk_counts') or {}).get('baixo_estoque_vs_venda_da_semana', 0)}`, unknown `{(tiny.get('risk_counts') or {}).get('unknown', 0)}`. Fonte: `fact_tiny_stock`.",
        f"• Meta: gasto sinalizado **{brl(meta.get('spend') or 0)}**, ROAS plataforma `{meta.get('platform_roas') if meta.get('platform_roas') is not None else 'n/d'}`. Fonte: `platform_signal`.",
        f"• Metricool/Google Ads: linhas `{metricool.get('google_ads_rows')}`, status `{metricool.get('ads_status') or metricool.get('status')}`. Fonte: `platform_signal`.",
        '',
        '**Prioridades**',
    ]
    for rec in [r for r in recs if r.get('priority') in {'P0', 'P1'}][:4]:
        lines.append(f"• [{rec.get('priority')}] {rec.get('action')} Motivo: {rec.get('why')} Fonte: `{rec.get('source_label')}`.")
    if not any(r.get('priority') in {'P0', 'P1'} for r in recs):
        lines.append('• Nenhum P0/P1. Manter silêncio e arquivar review no Brain.')
    lines += ['', '**Guardrail**', '• Preview interno. Não enviou Telegram automático, cron, Klaviyo, WhatsApp, campanha, fornecedor, compra ou alteração em Shopify/Tiny/banco.']
    return {'generated_at': now_utc(), 'week': public['week'], 'channel': 'telegram_preview_only', 'would_notify': would_notify, 'silence_policy': {'mode': 'silent_unless_p0_p1_api_failure_or_explicit_request', 'trigger': trigger, 'p0_count': sum(1 for r in recs if r.get('priority') == 'P0'), 'p1_count': sum(1 for r in recs if r.get('priority') == 'P1'), 'api_failure': api_failure, 'explicit_request': explicit_request}, 'source_labels': ['fact_shopify', 'fact_ga4', 'fact_tiny_stock', 'platform_signal', 'derived_reconciliation'], 'message_markdown': '\n'.join(lines), 'not_performed': ['telegram_send', 'cron', 'external_send', 'campaign', 'shopify_write', 'tiny_write', 'supplier_contact', 'production_db_write']}


def write_outputs(report: dict[str, Any]) -> None:
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE_DIR, 0o700)
    private_path = PRIVATE_DIR / f"lk_os_weekly_ceo_review_{report['week']['start_date'].replace('-', '')}_{report['week']['end_date'].replace('-', '')}_{datetime.now(timezone.utc).strftime('%H%M%SZ')}.json"
    private_path.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    os.chmod(private_path, 0o600)
    public = sanitize_for_public(report)
    PUBLIC_JSON.write_text(json.dumps(public, ensure_ascii=False, indent=2))
    telegram = build_telegram_preview(public)
    TELEGRAM_PREVIEW_JSON.write_text(json.dumps(telegram, ensure_ascii=False, indent=2))
    TELEGRAM_PREVIEW_MD.write_text(telegram['message_markdown'] + '\n')

    shop = public['sources']['shopify']
    ga4 = public['sources']['ga4']
    tiny = public['sources']['tiny_stock']
    meta = public['sources']['meta_ads']
    metricool = public['sources']['metricool_google_ads']
    sessions = int(((ga4.get('totals') or {}).get('sessions') or 0))
    orders = int(shop.get('orders_count') or 0)
    conv = orders / sessions if sessions else None
    lines = [
        f"# LK OS Weekly CEO Review — {public['week']['start_date']} a {public['week']['end_date']}",
        '',
        f"Gerado em: `{public.get('generated_at')}`.",
        f"Política de janela: `{public['week']['label']}`.",
        f"Arquivo privado auditável, fora do Git: `{private_path}`.",
        '',
        '## 1. Resumo CEO',
        '',
        f"- Shopify: **{brl(shop.get('revenue_total'))}** em **{orders} pedidos**, ticket médio **{brl(shop.get('average_order_value'))}**. Fonte: `fact_shopify`.",
        f"- GA4: **{sessions} sessões**, **{int(((ga4.get('totals') or {}).get('transactions') or 0))} transações GA4**, receita GA4 **{brl(((ga4.get('totals') or {}).get('totalRevenue') or 0))}**. Fonte: `fact_ga4`, não receita oficial.",
        f"- Conversão aproximada Shopify pedidos / GA4 sessões: **{pct(conv)}**.",
        f"- Tiny nos SKUs vendidos: **{tiny.get('risk_counts', {})}**. Fonte: `fact_tiny_stock`.",
        f"- Meta Ads: gasto **{brl(meta.get('spend') or 0)}**, compras plataforma `{meta.get('purchase_actions')}`, valor plataforma **{brl(meta.get('purchase_value') or 0)}**, ROAS plataforma `{meta.get('platform_roas') if meta.get('platform_roas') is not None else 'n/d'}`. Fonte: `platform_signal`.",
        f"- Metricool/Google Ads: linhas `{metricool.get('google_ads_rows')}`, status `{metricool.get('ads_status') or metricool.get('status')}`. Fonte: `platform_signal`.",
        '',
        '## 2. Vendas por dia',
        '',
    ]
    for day, row in (shop.get('daily') or {}).items():
        lines.append(f"- `{day}`: {row.get('orders')} pedidos, {brl(row.get('revenue'))}.")
    lines += ['', '## 3. Canais GA4', '']
    for row in ga4.get('top_channels') or []:
        lines.append(f"- `{row.get('channel')}`: {int(row.get('sessions') or 0)} sessões, {int(row.get('transactions') or 0)} transações, conversão GA4 {pct(row.get('sessionConversionRate') or 0)}.")
    lines += ['', '## 4. Produtos e estoque crítico', '']
    for row in tiny.get('critical_or_unknown') or []:
        dep = row.get('official_deposit') or {}
        saldo = dep.get('saldo')
        lines.append(f"- **{row.get('product_title')}**, SKU `{row.get('sku')}`, tamanho `{row.get('size_or_variant')}`: vendido {row.get('sold_qty_fact_shopify')} un.; saldo Tiny `{saldo if saldo is not None else 'n/d'}`; risco `{row.get('stock_risk')}`; match `{row.get('chosen_match_quality')}`.")
    if not (tiny.get('critical_or_unknown') or []):
        lines.append('- Sem ruptura/baixo estoque/mapeamento desconhecido na amostra de SKUs vendidos.')
    lines += ['', '## 5. Mídia e atribuição, ainda como sinal', '']
    lines.append('- Meta/Metricool entram como `platform_signal`: úteis para diagnóstico de gasto, alcance e campanha, mas não substituem Shopify como venda real.')
    for item, count in shop.get('landing_site_sample') or []:
        lines.append(f"- Landing Shopify observada: `{item}` em {count} pedido(s). Fonte: `fact_shopify`.")
    for item, count in shop.get('referring_site_sample') or []:
        lines.append(f"- Referrer Shopify observado: `{item}` em {count} pedido(s). Fonte: `fact_shopify`.")
    lines += ['', '## 6. Prioridades e aprovações', '']
    for rec in public.get('recommendations') or []:
        lines.append(f"- [{rec.get('priority')}] {rec.get('action')} Motivo: {rec.get('why')} Aprovação: {rec.get('approval_required')}. Fonte: `{rec.get('source_label')}`.")
    lines += ['', '## 7. O que este script não fez', '']
    for item in public.get('not_performed') or []:
        lines.append(f"- `{item}`")
    lines += ['', '## 8. Limitações', '', '- Semana read-only de 7 dias fechados, sem margem/CMV ainda.', '- CRM/RFM e SEO entram como próximos módulos de profundidade, não foram recalculados neste script.', '- Nenhum ROAS operacional foi declarado sem reconciliação por pedido/SKU/campanha.']
    PUBLIC_MD.write_text('\n'.join(lines) + '\n')


def main() -> None:
    window = closed_week_window()
    secrets = load_secrets()
    shop = shopify_week(secrets, window)
    ga4 = ga4_week(secrets, window)
    tiny = tiny_stock_for_sold_skus(secrets, shop.get('top_products') or []) if shop.get('ok') else {'source': 'Tiny', 'fact_label': 'fact_tiny_stock', 'ok': False, 'status': 'shopify_unavailable'}
    meta = meta_week(secrets, window)
    metricool = metricool_week(secrets, window)
    report = {'generated_at': now_utc(), 'week': window, 'scope': 'LK OS Weekly CEO Review read-only: Shopify + GA4 + Tiny + Meta/Metricool platform signals', 'sources': {'shopify': shop, 'ga4': ga4, 'tiny_stock': tiny, 'meta_ads': meta, 'metricool_google_ads': metricool}, 'recommendations': build_recommendations(shop, ga4, tiny, meta, metricool), 'not_performed': ['telegram_send', 'cron', 'external_send', 'campaign', 'shopify_write', 'tiny_write', 'stock_or_price_change', 'customer_contact', 'supplier_contact', 'production_db_write'], 'private_notes': 'PII minimized; order customer fields were not requested.'}
    write_outputs(report)
    print(json.dumps({'week': {'start': window['start_date'], 'end': window['end_date']}, 'shopify_orders': shop.get('orders_count'), 'shopify_revenue': shop.get('revenue_total'), 'ga4_sessions': ((ga4.get('totals') or {}).get('sessions') if ga4.get('ok') else None), 'tiny_risks': tiny.get('risk_counts'), 'meta_spend': meta.get('spend'), 'metricool_google_ads_rows': metricool.get('google_ads_rows'), 'public_json': str(PUBLIC_JSON), 'public_md': str(PUBLIC_MD), 'telegram_preview_md': str(TELEGRAM_PREVIEW_MD)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
