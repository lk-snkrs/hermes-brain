#!/usr/bin/env python3
"""LK OS Daily Sales Brief, read-only.

Generates a sanitized internal Daily Sales Brief using Shopify-confirmed sales,
GA4 channel behavior, and Tiny ERP stock checks for sold SKUs.

No writes, sends, campaigns, cron changes, product/price/stock edits, DB writes,
or external actions. Secrets are fetched in-process from Doppler and never printed.
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
PUBLIC_JSON = ROOT / 'reports/lk-os-daily-sales-brief-2026-05-10.json'
PUBLIC_MD = ROOT / 'reports/lk-os-daily-sales-brief-2026-05-10.md'
OFFICIAL_DEPOSIT = 'LK | CONTROLE ESTOQUE'
SP_TZ = ZoneInfo('America/Sao_Paulo')


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def closed_business_day() -> tuple[str, str, str, str]:
    """Return closed day in Sao Paulo timezone as date, start_iso, end_iso, label."""
    today_sp = datetime.now(SP_TZ).date()
    day = today_sp - timedelta(days=1)
    start = datetime(day.year, day.month, day.day, 0, 0, 0, tzinfo=SP_TZ)
    end = datetime(day.year, day.month, day.day, 23, 59, 59, tzinfo=SP_TZ)
    return day.isoformat(), start.isoformat(), end.isoformat(), 'last_closed_day_brt'


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
    req = urllib.request.Request(
        'https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json'
    )
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
            return {'ok': True, 'status': resp.status, 'body': json.loads(raw) if raw else {}, 'headers': dict(resp.headers)}
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


def shopify_orders(secrets: dict[str, str], start_iso: str, end_iso: str) -> dict[str, Any]:
    store = (secrets.get('SHOPIFY_STORE_URL') or '').strip().replace('https://', '').replace('http://', '').strip('/')
    token = secrets.get('SHOPIFY_ACCESS_TOKEN') or ''
    if not store or not token:
        return {'source': 'Shopify', 'fact_label': 'fact_shopify', 'ok': False, 'status': 'missing_credentials'}
    headers = {'X-Shopify-Access-Token': token, 'Accept': 'application/json'}
    base = f'https://{store}/admin/api/2024-01'
    params = {
        'status': 'any',
        'limit': 250,
        'created_at_min': start_iso,
        'created_at_max': end_iso,
        'fields': 'id,name,created_at,processed_at,updated_at,total_price,currency,financial_status,fulfillment_status,source_name,landing_site,referring_site,tags,line_items,discount_codes',
        'order': 'created_at asc',
    }
    res = http_json(f'{base}/orders.json?' + urllib.parse.urlencode(params), headers=headers, timeout=90)
    orders = (res.get('body') or {}).get('orders') or [] if res.get('ok') else []

    gross = sum(as_float(o.get('total_price')) for o in orders)
    channels: dict[str, dict[str, Any]] = defaultdict(lambda: {'orders': 0, 'revenue': 0.0})
    sources: dict[str, dict[str, Any]] = defaultdict(lambda: {'orders': 0, 'revenue': 0.0})
    product_rows: dict[tuple[str, str, str], dict[str, Any]] = {}
    sku_counter: Counter[str] = Counter()
    no_sku_lines = 0
    landing_counter: Counter[str] = Counter()
    ref_counter: Counter[str] = Counter()

    for order in orders:
        revenue = as_float(order.get('total_price'))
        channel = classify_order_channel(order)
        source = order.get('source_name') or 'unknown'
        channels[channel]['orders'] += 1
        channels[channel]['revenue'] += revenue
        sources[source]['orders'] += 1
        sources[source]['revenue'] += revenue
        if order.get('landing_site'):
            landing_counter[str(order.get('landing_site'))[:120]] += 1
        if order.get('referring_site'):
            ref_counter[str(order.get('referring_site'))[:120]] += 1
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
            row = product_rows.setdefault(key, {
                'product_title': title,
                'sku': sku or 'sem_sku',
                'size_or_variant': variant,
                'quantity': 0,
                'line_revenue_estimate': 0.0,
                'source_label': 'fact_shopify',
                'channels': Counter(),
            })
            row['quantity'] += qty
            row['line_revenue_estimate'] += revenue_line
            row['channels'][source] += qty

    top_products = sorted(product_rows.values(), key=lambda x: (x['quantity'], x['line_revenue_estimate']), reverse=True)[:15]
    for row in top_products:
        row['channels'] = dict(row['channels'].most_common(5))
        row['line_revenue_estimate'] = round(row['line_revenue_estimate'], 2)

    return {
        'source': 'Shopify',
        'fact_label': 'fact_shopify',
        'ok': bool(res.get('ok')),
        'api_status': res.get('status'),
        'date_range': {'start': start_iso, 'end': end_iso},
        'orders_count': len(orders),
        'revenue_total': round(gross, 2),
        'average_order_value': round(gross / len(orders), 2) if orders else 0,
        'channels': {k: {'orders': v['orders'], 'revenue': round(v['revenue'], 2)} for k, v in channels.items()},
        'source_names': {k: {'orders': v['orders'], 'revenue': round(v['revenue'], 2)} for k, v in sorted(sources.items(), key=lambda item: item[1]['revenue'], reverse=True)},
        'top_products': top_products,
        'top_skus': sku_counter.most_common(12),
        'no_sku_line_items': no_sku_lines,
        'landing_site_sample': landing_counter.most_common(5),
        'referring_site_sample': ref_counter.most_common(5),
        'raw_order_count_private': len(orders),
    }


def tiny_call(token: str, method: str, params: dict[str, Any]) -> dict[str, Any]:
    started = time.perf_counter()
    data = urllib.parse.urlencode({**params, 'token': token, 'formato': 'json'}).encode()
    req = urllib.request.Request(f'https://api.tiny.com.br/api2/{method}.php', data=data, method='POST')
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            body = json.load(resp)
            retorno = (body or {}).get('retorno') or {}
            return {'ok': True, 'status': resp.status, 'tiny_status': retorno.get('status'), 'body': body, 'latency_ms': int((time.perf_counter() - started) * 1000)}
    except urllib.error.HTTPError as exc:
        return {'ok': False, 'status': exc.code, 'tiny_status': None, 'message': exc.read().decode(errors='replace')[:300], 'latency_ms': int((time.perf_counter() - started) * 1000)}
    except Exception as exc:
        return {'ok': False, 'status': None, 'tiny_status': None, 'error': type(exc).__name__, 'message': str(exc)[:300], 'latency_ms': int((time.perf_counter() - started) * 1000)}


def tiny_stock_for_sold_skus(secrets: dict[str, str], top_products: list[dict[str, Any]]) -> dict[str, Any]:
    token = secrets.get('TINY_API_TOKEN') or ''
    if not token:
        return {'source': 'Tiny', 'fact_label': 'fact_tiny_stock', 'ok': False, 'status': 'missing_credentials'}
    checks = []
    seen: set[str] = set()
    for product in top_products:
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
            codigo = p.get('codigo') or ''
            candidates.append({'id': str(p.get('id') or ''), 'codigo': codigo, 'nome': p.get('nome'), 'exact_norm_sku': normalize_sku(codigo) == normalize_sku(sku)})
        exact = next((c for c in candidates if c['exact_norm_sku'] and c['id']), None)
        chosen = exact or (candidates[0] if len(candidates) == 1 else None)
        stock = None
        official = None
        if chosen:
            time.sleep(1.25)
            st = tiny_call(token, 'produto.obter.estoque', {'id': chosen['id']})
            prod = (((st.get('body') or {}).get('retorno') or {}).get('produto') or {}) if st.get('body') else {}
            for dep_item in prod.get('depositos') or []:
                dep = dep_item.get('deposito') or {}
                if dep.get('nome') == OFFICIAL_DEPOSIT:
                    saldo_raw = dep.get('saldo')
                    try:
                        saldo = float(str(saldo_raw).replace(',', '.'))
                    except Exception:
                        saldo = None
                    official = {
                        'deposit': OFFICIAL_DEPOSIT,
                        'saldo': saldo,
                        'saldo_raw_present': saldo_raw is not None,
                        'desconsiderar': dep.get('desconsiderar'),
                    }
            stock = {
                'http_status': st.get('status'),
                'tiny_status': st.get('tiny_status'),
                'latency_ms': st.get('latency_ms'),
            }
        sold_qty = int(product.get('quantity') or 0)
        saldo = official.get('saldo') if official else None
        risk = 'unknown'
        if saldo is not None:
            if saldo <= 0:
                risk = 'ruptura'
            elif saldo <= sold_qty:
                risk = 'baixo_estoque_vs_venda_do_dia'
            else:
                risk = 'ok_amostra'
        checks.append({
            'source_label': 'fact_tiny_stock',
            'product_title': product.get('product_title'),
            'sku': sku,
            'size_or_variant': product.get('size_or_variant'),
            'sold_qty_fact_shopify': sold_qty,
            'search_status': search.get('tiny_status'),
            'candidate_count': len(candidates),
            'chosen_tiny_id': chosen.get('id') if chosen else None,
            'chosen_match_quality': 'exact_norm_sku' if exact else ('single_candidate' if chosen else 'no_safe_candidate'),
            'official_deposit': official,
            'stock_call': stock,
            'stock_risk': risk,
        })
    return {
        'source': 'Tiny',
        'fact_label': 'fact_tiny_stock',
        'ok': True,
        'deposit': OFFICIAL_DEPOSIT,
        'checks_count': len(checks),
        'risk_counts': dict(Counter(c['stock_risk'] for c in checks)),
        'critical_or_unknown': [c for c in checks if c['stock_risk'] in {'ruptura', 'baixo_estoque_vs_venda_do_dia', 'unknown'}][:12],
        'checks': checks,
        'scope_note': 'Read-only. Estoque consultado só para SKUs vendidos no dia, não auditoria completa de catálogo.',
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
    assertion = signing_input.decode() + '.' + b64url(proc.stdout)
    data = urllib.parse.urlencode({'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer', 'assertion': assertion}).encode()
    req = urllib.request.Request('https://oauth2.googleapis.com/token', data=data, method='POST')
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    with urllib.request.urlopen(req, timeout=60) as resp:
        payload = json.load(resp)
    return payload['access_token']


def ga4_channels(secrets: dict[str, str], date: str) -> dict[str, Any]:
    sa_raw = secrets.get('GA4_LK_SERVICE_ACCOUNT') or secrets.get('GOOGLE_SERVICE_ACCOUNT_JSON')
    prop = secrets.get('GOOGLE_ANALYTICS_PROPERTY_ID') or secrets.get('GA4_LK_PROPERTY_ID') or secrets.get('GA4_PROPERTY_ID')
    if not sa_raw or not prop:
        return {'source': 'GA4', 'fact_label': 'fact_ga4', 'ok': False, 'status': 'missing_credentials'}
    try:
        token = google_access_token_from_service_account(json.loads(sa_raw), 'https://www.googleapis.com/auth/analytics.readonly')
        url = f'https://analyticsdata.googleapis.com/v1beta/properties/{prop}:runReport'
        body = {
            'dateRanges': [{'startDate': date, 'endDate': date}],
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
        totals = {
            'sessions': sum(r['sessions'] for r in rows),
            'transactions': sum(r['transactions'] for r in rows),
            'totalRevenue': round(sum(r['totalRevenue'] for r in rows), 2),
        }
        return {'source': 'GA4', 'fact_label': 'fact_ga4', 'ok': bool(res.get('ok')), 'api_status': res.get('status'), 'date_range': {'start': date, 'end': date}, 'totals': totals, 'top_channels': rows[:10], 'note': 'GA4 mede tráfego/canal/funil; Shopify permanece fonte oficial de pedido/receita.'}
    except Exception as exc:
        return {'source': 'GA4', 'fact_label': 'fact_ga4', 'ok': False, 'status': 'exception', 'error': type(exc).__name__, 'message': str(exc)[:300]}


def build_recommendations(shopify: dict[str, Any], tiny: dict[str, Any], ga4: dict[str, Any]) -> list[dict[str, Any]]:
    recs = []
    critical = tiny.get('critical_or_unknown') or []
    rupture = [c for c in critical if c.get('stock_risk') == 'ruptura']
    low = [c for c in critical if c.get('stock_risk') == 'baixo_estoque_vs_venda_do_dia']
    unknown = [c for c in critical if c.get('stock_risk') == 'unknown']
    if rupture:
        recs.append({'priority': 'P0', 'source_label': 'derived_reconciliation', 'action': 'Preparar preview de reposição/sourcing para SKUs vendidos com saldo zero no Tiny.', 'why': f'{len(rupture)} SKU(s) vendidos aparecem em ruptura no depósito oficial.', 'approval_required': 'Sim, antes de fornecedor/compra/Notion.'})
    if low:
        recs.append({'priority': 'P1', 'source_label': 'derived_reconciliation', 'action': 'Revisar cobertura dos SKUs com saldo menor ou igual à venda do dia.', 'why': f'{len(low)} SKU(s) com venda do dia encostando no saldo oficial.', 'approval_required': 'Sim, se virar compra, preço ou contato.'})
    if unknown:
        recs.append({'priority': 'P1', 'source_label': 'derived_reconciliation', 'action': 'Resolver mapeamento Shopify SKU ↔ Tiny antes de campanha ou reposição automática.', 'why': f'{len(unknown)} SKU(s) vendido(s) sem candidato Tiny seguro ou sem saldo legível.', 'approval_required': 'Sim, se exigir correção de cadastro.'})
    if shopify.get('orders_count', 0) == 0:
        recs.append({'priority': 'P1', 'source_label': 'fact_shopify', 'action': 'Investigar tráfego/conversão antes de qualquer campanha nova.', 'why': 'Shopify não retornou pedidos para o dia fechado.', 'approval_required': 'Não para análise; sim para campanha.'})
    ga4_sessions = ((ga4.get('totals') or {}).get('sessions') or 0) if ga4.get('ok') else 0
    if ga4_sessions and shopify.get('orders_count'):
        conv = shopify['orders_count'] / ga4_sessions
        if conv < 0.002:
            recs.append({'priority': 'P2', 'source_label': 'derived_reconciliation', 'action': 'Separar páginas/canais de alto tráfego e baixa compra para CRO.', 'why': f'Conversão aproximada Shopify pedidos / GA4 sessões em {conv:.2%}.', 'approval_required': 'Não para diagnóstico; sim para PDP/tema/preço.'})
    if not recs:
        recs.append({'priority': 'P2', 'source_label': 'derived_reconciliation', 'action': 'Sem alerta crítico; próximo passo é enriquecer o briefing com margem, canal pago e recompra.', 'why': 'Pedidos, GA4 e Tiny não apontaram bloqueio crítico na amostra.', 'approval_required': 'Não para análise.'})
    return recs[:6]


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


def write_outputs(report: dict[str, Any]) -> None:
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE_DIR, 0o700)
    private_path = PRIVATE_DIR / f"lk_os_daily_sales_brief_{report['business_date'].replace('-', '')}_{datetime.now(timezone.utc).strftime('%H%M%SZ')}.json"
    private_path.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    os.chmod(private_path, 0o600)

    public = sanitize_for_public(report)
    PUBLIC_JSON.write_text(json.dumps(public, ensure_ascii=False, indent=2))

    shop = public['sources']['shopify']
    tiny = public['sources']['tiny_stock']
    ga4 = public['sources']['ga4']
    channels = shop.get('channels') or {}
    online = channels.get('online_or_unknown') or {'orders': 0, 'revenue': 0}
    pos = channels.get('loja_fisica_or_pos') or {'orders': 0, 'revenue': 0}
    ga4_totals = ga4.get('totals') or {}
    approx_conv = None
    if ga4.get('ok') and ga4_totals.get('sessions'):
        approx_conv = shop.get('orders_count', 0) / ga4_totals['sessions']

    lines = [
        f"# LK OS Daily Sales Brief — {public['business_date']}",
        '',
        f"Gerado em: `{public.get('generated_at')}`.",
        f"Janela: `{public['date_range']['start']}` a `{public['date_range']['end']}`.",
        f"Arquivo privado auditável, fora do Git: `{private_path}`.",
        '',
        '## 1. Resumo executivo',
        '',
        f"Ontem a LK vendeu **{brl(shop.get('revenue_total'))}** em **{shop.get('orders_count')} pedidos**. Fonte: `fact_shopify`.",
        f"Online/indefinido: **{brl(online.get('revenue'))} / {online.get('orders')} pedidos**. Loja física/POS detectado: **{brl(pos.get('revenue'))} / {pos.get('orders')} pedidos**.",
        f"GA4: **{int(ga4_totals.get('sessions') or 0)} sessões**, **{int(ga4_totals.get('transactions') or 0)} transações GA4**, receita GA4 **{brl(ga4_totals.get('totalRevenue') or 0)}**. Fonte: `fact_ga4`, não receita oficial.",
        f"Conversão aproximada pedidos Shopify / sessões GA4: **{approx_conv:.2%}**." if approx_conv is not None else 'Conversão aproximada: `n/d`, GA4 indisponível ou sem sessões.',
        f"Tiny: **{tiny.get('risk_counts', {})}** nos SKUs vendidos checados. Fonte: `fact_tiny_stock`.",
        '',
        '## 2. Vendas Shopify',
        '',
        f"- Receita total: `{brl(shop.get('revenue_total'))}`",
        f"- Pedidos: `{shop.get('orders_count')}`",
        f"- Ticket médio: `{brl(shop.get('average_order_value'))}`",
        f"- Linhas sem SKU: `{shop.get('no_sku_line_items')}`",
        '- Source/canal:',
    ]
    for source, row in list((shop.get('source_names') or {}).items())[:8]:
        lines.append(f"  - `{source}`: {row.get('orders')} pedidos, {brl(row.get('revenue'))}")
    lines += ['', '## 3. Conversão e CRO', '']
    for row in ga4.get('top_channels') or []:
        lines.append(f"- `{row.get('channel')}`: {int(row.get('sessions') or 0)} sessões, {int(row.get('transactions') or 0)} transações, conversão GA4 {float(row.get('sessionConversionRate') or 0):.2%}.")
    if not (ga4.get('top_channels') or []):
        lines.append('- GA4 não retornou canais para a janela.')
    lines += ['', '## 4. Produtos/modelos/tamanhos vendidos', '']
    for row in shop.get('top_products') or []:
        lines.append(f"- **{row.get('product_title')}**, SKU `{row.get('sku')}`, tamanho `{row.get('size_or_variant')}`: {row.get('quantity')} un., receita estimada de linhas {brl(row.get('line_revenue_estimate'))}. Fonte: `fact_shopify`.")
    lines += ['', '## 5. Centro de Inteligência de Stock', '']
    for row in tiny.get('critical_or_unknown') or []:
        dep = row.get('official_deposit') or {}
        saldo = dep.get('saldo')
        lines.append(f"- **{row.get('product_title')}**, SKU `{row.get('sku')}`, tamanho `{row.get('size_or_variant')}`: vendido {row.get('sold_qty_fact_shopify')} un.; saldo Tiny `{saldo if saldo is not None else 'n/d'}`; risco `{row.get('stock_risk')}`; match `{row.get('chosen_match_quality')}`.")
    if not (tiny.get('critical_or_unknown') or []):
        lines.append('- Sem ruptura/baixo estoque/mapeamento desconhecido na amostra de SKUs vendidos.')
    lines += ['', '## 6. Pago, influencers e conteúdo', '']
    for item, count in shop.get('landing_site_sample') or []:
        lines.append(f"- Landing Shopify observada: `{item}` em {count} pedido(s). Fonte: `fact_shopify`.")
    for item, count in shop.get('referring_site_sample') or []:
        lines.append(f"- Referrer Shopify observado: `{item}` em {count} pedido(s). Fonte: `fact_shopify`.")
    if not (shop.get('landing_site_sample') or shop.get('referring_site_sample')):
        lines.append('- Sem landing/referrer suficiente no Shopify para atribuição segura por campanha neste briefing.')
    lines += ['', '## 7. Recomendações e aprovações pendentes', '']
    for rec in public.get('recommendations') or []:
        lines.append(f"- [{rec.get('priority')}] {rec.get('action')} Motivo: {rec.get('why')} Aprovação: {rec.get('approval_required')}. Fonte: `{rec.get('source_label')}`.")
    lines += [
        '',
        '## 8. Limites da leitura',
        '',
        '- Shopify é fonte oficial de pedidos/receita; GA4 é tráfego/canal/funil.',
        '- Tiny foi checado apenas para SKUs vendidos no dia; não é auditoria completa de estoque por catálogo.',
        '- Atribuição paga/influencer não foi promovida a fato sem ponte segura por UTM/referrer/cupom/ad_id.',
        '',
        '## 9. O que este script não fez',
        '',
        '- Não enviou WhatsApp, Klaviyo, e-mail, campanha ou mensagem externa.',
        '- Não alterou Shopify, Tiny, Supabase, Meta, Google, Metricool, Klaviyo, Notion, n8n, estoque, preço, produto, cliente ou banco de produção.',
        '- Não criou cron e não acionou fornecedor/compra.',
    ]
    PUBLIC_MD.write_text('\n'.join(lines) + '\n')


def main() -> None:
    date, start_iso, end_iso, label = closed_business_day()
    secrets = load_secrets()
    shop = shopify_orders(secrets, start_iso, end_iso)
    tiny = tiny_stock_for_sold_skus(secrets, shop.get('top_products') or []) if shop.get('ok') else {'source': 'Tiny', 'fact_label': 'fact_tiny_stock', 'ok': False, 'status': 'shopify_unavailable'}
    ga4 = ga4_channels(secrets, date)
    report = {
        'generated_at': now_utc(),
        'business_date': date,
        'window_policy': label,
        'date_range': {'start': start_iso, 'end': end_iso},
        'scope': 'LK OS Daily Sales Brief read-only: Shopify sales + GA4 channels + Tiny stock checks for sold SKUs',
        'sources': {'shopify': shop, 'tiny_stock': tiny, 'ga4': ga4},
        'recommendations': build_recommendations(shop, tiny, ga4),
        'not_performed': ['external_send', 'campaign', 'cron', 'shopify_write', 'tiny_write', 'stock_or_price_change', 'customer_contact', 'supplier_contact', 'production_db_write'],
        'private_notes': 'Raw response intentionally minimized; order customer fields were not requested from Shopify.',
    }
    write_outputs(report)
    print(json.dumps({'business_date': date, 'shopify_orders': shop.get('orders_count'), 'shopify_revenue': shop.get('revenue_total'), 'tiny_risks': tiny.get('risk_counts'), 'ga4_sessions': ((ga4.get('totals') or {}).get('sessions') if ga4.get('ok') else None), 'public_json': str(PUBLIC_JSON), 'public_md': str(PUBLIC_MD)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
