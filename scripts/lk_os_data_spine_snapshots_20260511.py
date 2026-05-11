#!/usr/bin/env python3
"""LK OS Data Spine read-only source snapshots.

Scope: verify freshness/count/status for Shopify, Tiny, GA4, paid sources and Klaviyo.
No writes to Shopify, Tiny, GA4, Meta, Metricool, Google Ads, Klaviyo, Supabase or production DBs.
Secrets are fetched in-process from Doppler and never printed.
Private raw-ish output goes outside Git under /opt/data/hermes_bruno_ingest/local_sql/ with chmod 600.
Public report is sanitized and contains only counts/statuses/non-PII operational facts.
"""
from __future__ import annotations

import base64
import json
import os
import pathlib
import subprocess
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOPPLER_TOKEN_FILE = pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_data_spine_snapshots')
PUBLIC_JSON = ROOT / 'reports/lk-os-data-spine-snapshot-2026-05-11.json'
PUBLIC_MD = ROOT / 'reports/lk-os-data-spine-snapshot-2026-05-11.md'
REVISION_KLAVIYO = '2025-10-15'
META_ACCOUNT_FALLBACK = 'act_1242062509867163'


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def today_sp() -> tuple[str, str]:
    # Good enough for closed-window freshness checks; avoids pulling same-day partials as final truth.
    today = datetime.now(timezone.utc).date()
    end = today.isoformat()
    start = (today - timedelta(days=7)).isoformat()
    yesterday = (today - timedelta(days=1)).isoformat()
    return start, yesterday if yesterday >= start else end


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
    for k, v in (headers or {}).items():
        req.add_header(k, v)
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


def safe_max(values: list[str | None]) -> str | None:
    vals = [v for v in values if v]
    return max(vals) if vals else None


def mask_money_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out = []
    for r in rows:
        out.append({k: r.get(k) for k in ['id', 'name', 'created_at', 'updated_at', 'processed_at', 'financial_status', 'fulfillment_status', 'total_price', 'currency', 'source_name']})
    return out


def shopify_snapshot(secrets: dict[str, str]) -> dict[str, Any]:
    store = (secrets.get('SHOPIFY_STORE_URL') or '').strip().replace('https://', '').replace('http://', '').strip('/')
    token = secrets.get('SHOPIFY_ACCESS_TOKEN') or ''
    if not store or not token:
        return {'source': 'Shopify', 'fact_label': 'fact_shopify', 'ok': False, 'status': 'missing_credentials'}
    headers = {'X-Shopify-Access-Token': token, 'Accept': 'application/json'}
    base = f'https://{store}/admin/api/2024-01'
    start, end = today_sp()
    products_count = http_json(f'{base}/products/count.json', headers=headers)
    orders_count = http_json(f'{base}/orders/count.json?' + urllib.parse.urlencode({'status': 'any', 'created_at_min': start, 'created_at_max': end}), headers=headers)
    products = http_json(f'{base}/products.json?' + urllib.parse.urlencode({'limit': 10, 'fields': 'id,title,handle,status,updated_at,published_at,variants'}), headers=headers)
    orders = http_json(f'{base}/orders.json?' + urllib.parse.urlencode({'status': 'any', 'limit': 10, 'order': 'updated_at desc', 'fields': 'id,name,created_at,updated_at,processed_at,total_price,currency,financial_status,fulfillment_status,source_name,line_items'}), headers=headers)
    prod_rows = (products.get('body') or {}).get('products') or [] if products.get('ok') else []
    order_rows = (orders.get('body') or {}).get('orders') or [] if orders.get('ok') else []
    variant_count_sample = sum(len(p.get('variants') or []) for p in prod_rows)
    return {
        'source': 'Shopify',
        'fact_label': 'fact_shopify',
        'ok': bool(products_count.get('ok') and orders_count.get('ok') and products.get('ok') and orders.get('ok')),
        'api_statuses': {'products_count': products_count.get('status'), 'orders_7d_count': orders_count.get('status'), 'products_sample': products.get('status'), 'orders_sample': orders.get('status')},
        'product_count': (products_count.get('body') or {}).get('count'),
        'orders_7d_count': (orders_count.get('body') or {}).get('count'),
        'products_sample_count': len(prod_rows),
        'variants_in_product_sample': variant_count_sample,
        'orders_sample_count': len(order_rows),
        'freshness': {'max_product_updated_at_sample': safe_max([p.get('updated_at') for p in prod_rows]), 'max_order_updated_at_sample': safe_max([o.get('updated_at') for o in order_rows])},
        'sample_orders_no_customer_pii': mask_money_rows(order_rows[:5]),
    }


def tiny_call(token: str, method: str, params: dict[str, Any]) -> dict[str, Any]:
    time.sleep(1.25)
    data = urllib.parse.urlencode({**params, 'token': token, 'formato': 'json'}).encode()
    req = urllib.request.Request(f'https://api.tiny.com.br/api2/{method}.php', data=data, method='POST')
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            return {'ok': True, 'status': resp.status, 'body': json.load(resp)}
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode(errors='replace')
        return {'ok': False, 'status': exc.code, 'body': {'raw': raw[:500]}}
    except Exception as exc:
        return {'ok': False, 'status': None, 'error': type(exc).__name__, 'message': str(exc)[:300]}


def tiny_snapshot(secrets: dict[str, str]) -> dict[str, Any]:
    token = secrets.get('TINY_API_TOKEN') or ''
    if not token:
        return {'source': 'Tiny', 'fact_label': 'fact_tiny_stock', 'ok': False, 'status': 'missing_credentials'}
    searches = []
    product_ids: list[str] = []
    for q in ['Nike', 'Adidas', 'New Balance', 'Asics', 'Onitsuka']:
        res = tiny_call(token, 'produtos.pesquisa', {'pesquisa': q, 'pagina': 1})
        retorno = (res.get('body') or {}).get('retorno') or {}
        rows = retorno.get('produtos') or []
        searches.append({'query': q, 'http_status': res.get('status'), 'tiny_status': retorno.get('status'), 'count_sample': len(rows)})
        for item in rows[:2]:
            pid = str(((item or {}).get('produto') or {}).get('id') or '')
            if pid and pid not in product_ids:
                product_ids.append(pid)
    stock_checks = []
    official_deposit_seen = 0
    for pid in product_ids[:6]:
        st = tiny_call(token, 'produto.obter.estoque', {'id': pid})
        p = (((st.get('body') or {}).get('retorno') or {}).get('produto') or {})
        deposits = []
        for d in p.get('depositos') or []:
            dep = d.get('deposito') or {}
            nome = dep.get('nome')
            if nome == 'LK | CONTROLE ESTOQUE':
                official_deposit_seen += 1
            deposits.append({'nome': nome, 'has_saldo': dep.get('saldo') is not None, 'desconsiderar': dep.get('desconsiderar')})
        stock_checks.append({'http_status': st.get('status'), 'tiny_status': ((st.get('body') or {}).get('retorno') or {}).get('status'), 'tiny_id': str(p.get('id') or pid), 'codigo_present': bool(p.get('codigo')), 'depositos': deposits})
    return {
        'source': 'Tiny',
        'fact_label': 'fact_tiny_stock',
        'ok': any(s['tiny_status'] == 'OK' for s in searches) and bool(stock_checks),
        'scope_note': 'Amostra read-only por buscas de marcas; estoque oficial deve usar depósito LK | CONTROLE ESTOQUE.',
        'searches': searches,
        'stock_checks_sample_count': len(stock_checks),
        'official_deposit_seen_in_sample': official_deposit_seen,
        'stock_checks': stock_checks,
    }


def b64url(raw: bytes) -> str:
    return base64.urlsafe_b64encode(raw).decode().rstrip('=')


def google_access_token_from_service_account(sa: dict[str, Any], scope: str) -> str:
    """Create a Google OAuth token without third-party Python packages.

    The private key is written to a chmod 600 temp file only for openssl signing,
    then deleted immediately. No key material is printed or committed.
    """
    now = int(time.time())
    header = {'alg': 'RS256', 'typ': 'JWT'}
    claim = {
        'iss': sa['client_email'],
        'scope': scope,
        'aud': 'https://oauth2.googleapis.com/token',
        'iat': now,
        'exp': now + 3600,
    }
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


def ga4_snapshot(secrets: dict[str, str]) -> dict[str, Any]:
    sa_raw = secrets.get('GA4_LK_SERVICE_ACCOUNT') or secrets.get('GOOGLE_SERVICE_ACCOUNT_JSON')
    prop = secrets.get('GOOGLE_ANALYTICS_PROPERTY_ID') or secrets.get('GA4_LK_PROPERTY_ID') or secrets.get('GA4_PROPERTY_ID')
    if not sa_raw or not prop:
        return {'source': 'GA4', 'fact_label': 'fact_ga4', 'ok': False, 'status': 'missing_credentials'}
    start, end = today_sp()
    try:
        token = None
        try:
            from google.auth.transport.requests import Request as GoogleAuthRequest
            from google.oauth2 import service_account
            creds = service_account.Credentials.from_service_account_info(json.loads(sa_raw), scopes=['https://www.googleapis.com/auth/analytics.readonly'])
            creds.refresh(GoogleAuthRequest())
            token = creds.token
        except Exception:
            token = google_access_token_from_service_account(json.loads(sa_raw), 'https://www.googleapis.com/auth/analytics.readonly')
        url = f'https://analyticsdata.googleapis.com/v1beta/properties/{prop}:runReport'
        body = {
            'dateRanges': [{'startDate': start, 'endDate': end}],
            'dimensions': [{'name': 'sessionDefaultChannelGroup'}],
            'metrics': [{'name': m} for m in ['sessions', 'totalUsers', 'transactions', 'totalRevenue', 'sessionConversionRate']],
            'limit': 20,
            'orderBys': [{'metric': {'metricName': 'sessions'}, 'desc': True}],
        }
        res = http_json(url, method='POST', headers={'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}, body=body)
        rows = []
        for row in (res.get('body') or {}).get('rows') or []:
            label = row['dimensionValues'][0]['value']
            metrics = {name: float(m.get('value') or 0) for name, m in zip(['sessions', 'totalUsers', 'transactions', 'totalRevenue', 'sessionConversionRate'], row.get('metricValues') or [])}
            rows.append({'channel': label, **metrics})
        return {'source': 'GA4', 'fact_label': 'fact_ga4', 'ok': bool(res.get('ok')), 'api_status': res.get('status'), 'date_range': {'start': start, 'end': end}, 'row_count': len(rows), 'top_channels': rows[:10]}
    except Exception as exc:
        return {'source': 'GA4', 'fact_label': 'fact_ga4', 'ok': False, 'status': 'exception', 'error': type(exc).__name__, 'message': str(exc)[:300]}


def meta_snapshot(secrets: dict[str, str]) -> dict[str, Any]:
    token = secrets.get('META_ACCESS_TOKEN') or ''
    account = secrets.get('META_ADS_ACCOUNT_ID') or secrets.get('META_AD_ACCOUNT_ID') or META_ACCOUNT_FALLBACK
    if not token:
        return {'source': 'Meta Ads', 'fact_label': 'platform_signal', 'ok': False, 'status': 'missing_credentials'}
    acct = account if str(account).startswith('act_') else f'act_{account}'
    qs = urllib.parse.urlencode({'access_token': token, 'date_preset': 'last_7d', 'fields': 'spend,impressions,clicks,actions,action_values', 'level': 'account'})
    res = http_json(f'https://graph.facebook.com/v20.0/{acct}/insights?{qs}', timeout=90)
    rows = (res.get('body') or {}).get('data') or [] if res.get('ok') else []
    row = rows[0] if rows else {}
    purchase_keys = ['offsite_conversion.fb_pixel_purchase', 'omni_purchase', 'purchase']
    def action_val(items: list[dict[str, Any]]) -> tuple[float, str | None]:
        vals = {i.get('action_type'): float(i.get('value') or 0) for i in items or []}
        for k in purchase_keys:
            if k in vals:
                return vals[k], k
        return 0.0, None
    purchases, purchase_key = action_val(row.get('actions') or [])
    purchase_value, value_key = action_val(row.get('action_values') or [])
    return {'source': 'Meta Ads', 'fact_label': 'platform_signal', 'ok': bool(res.get('ok')), 'api_status': res.get('status'), 'account_checked': acct, 'date_preset': 'last_7d', 'rows': len(rows), 'spend': float(row.get('spend') or 0), 'impressions': int(float(row.get('impressions') or 0)), 'clicks': int(float(row.get('clicks') or 0)), 'purchase_actions': purchases, 'purchase_action_key': purchase_key, 'purchase_value': purchase_value, 'purchase_value_key': value_key, 'note': 'Meta é diagnóstico de plataforma, não receita operacional final.'}


def metricool_snapshot(secrets: dict[str, str]) -> dict[str, Any]:
    token = secrets.get('METRICOOL_API_TOKEN') or secrets.get('METRICOOL_USER_TOKEN') or ''
    user_id = secrets.get('METRICOOL_USER_ID') or '4792967'
    blog_id = secrets.get('METRICOOL_BLOG_ID') or secrets.get('METRICOOL_LK_BRAND_ID') or '6217010'
    if not token:
        return {'source': 'Metricool Google Ads', 'fact_label': 'platform_signal', 'ok': False, 'status': 'missing_metricool_token', 'user_id_present': bool(user_id), 'blog_id': blog_id}
    start, end = today_sp()
    base_q = {'userId': user_id, 'blogId': blog_id, 'userToken': token}
    prof = http_json('https://app.metricool.com/api/admin/simpleProfiles?' + urllib.parse.urlencode(base_q), timeout=60)
    from_iso = start + 'T00:00:00'
    to_iso = end + 'T23:59:59'
    ad_q = {**base_q, 'from': from_iso, 'to': to_iso, 'timezone': 'America/Sao_Paulo', 'providers[]': 'adwords'}
    ads = http_json('https://app.metricool.com/api/v2/advertising/campaigns?' + urllib.parse.urlencode(ad_q), timeout=90)
    body = ads.get('body') if isinstance(ads.get('body'), dict) else {}
    rows = body.get('data') or body.get('campaigns') or body.get('items') or []
    if isinstance(rows, dict):
        rows = list(rows.values())
    brand_facts = []
    for item in (prof.get('body') or []) if isinstance(prof.get('body'), list) else []:
        if str(item.get('id') or item.get('blogId') or '') == str(blog_id):
            brand_facts.append({'label': item.get('label') or item.get('name'), 'id': item.get('id') or item.get('blogId'), 'timezone': item.get('timezone')})
    return {'source': 'Metricool Google Ads', 'fact_label': 'platform_signal', 'ok': bool(prof.get('ok') and ads.get('ok')), 'profile_status': prof.get('status'), 'ads_status': ads.get('status'), 'blog_id': blog_id, 'brand_facts': brand_facts[:3], 'date_range': {'start': start, 'end': end}, 'google_ads_rows': len(rows) if isinstance(rows, list) else None, 'note': 'Metricool/Google Ads é custo e diagnóstico de plataforma, não receita final.'}


def klaviyo_snapshot(secrets: dict[str, str]) -> dict[str, Any]:
    token = secrets.get('KLAVIYO_API_KEY') or ''
    if not token:
        return {'source': 'Klaviyo', 'fact_label': 'platform_signal', 'ok': False, 'status': 'missing_credentials'}
    headers = {'Authorization': f'Klaviyo-API-Key {token}', 'Accept': 'application/json', 'revision': REVISION_KLAVIYO}
    lists = http_json('https://a.klaviyo.com/api/lists/?page[size]=10', headers=headers, timeout=60)
    campaigns = http_json('https://a.klaviyo.com/api/campaigns/?' + urllib.parse.urlencode({'filter': "equals(messages.channel,'email')", 'page[size]': '10'}), headers=headers, timeout=60)
    list_rows = (lists.get('body') or {}).get('data') or [] if lists.get('ok') else []
    camp_rows = (campaigns.get('body') or {}).get('data') or [] if campaigns.get('ok') else []
    safe_campaigns = []
    for c in camp_rows[:10]:
        attrs = c.get('attributes') or {}
        safe_campaigns.append({'id': c.get('id'), 'name': attrs.get('name'), 'status': attrs.get('status'), 'created_at': attrs.get('created_at'), 'updated_at': attrs.get('updated_at'), 'send_time': attrs.get('send_time')})
    return {'source': 'Klaviyo', 'fact_label': 'platform_signal', 'ok': bool(lists.get('ok') and campaigns.get('ok')), 'api_statuses': {'lists': lists.get('status'), 'campaigns': campaigns.get('status')}, 'lists_sample_count': len(list_rows), 'campaigns_sample_count': len(camp_rows), 'campaigns_sample': safe_campaigns, 'note': 'Read-only; não cria, agenda nem envia campanha.'}


def sanitize_for_public(snapshot: dict[str, Any]) -> dict[str, Any]:
    # Current collectors already avoid PII/secrets. This is a final guardrail for obvious secret-like keys if APIs change.
    blocked = {'access_token', 'token', 'api_key', 'authorization', 'email', 'phone', 'first_name', 'last_name', 'customer'}
    def scrub(v: Any) -> Any:
        if isinstance(v, dict):
            return {k: ('[REDACTED]' if any(b in k.lower() for b in blocked) else scrub(val)) for k, val in v.items()}
        if isinstance(v, list):
            return [scrub(x) for x in v]
        return v
    return scrub(snapshot)


def write_outputs(summary: dict[str, Any]) -> None:
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE_DIR, 0o700)
    private_path = PRIVATE_DIR / f"lk_os_data_spine_snapshot_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
    private_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2))
    os.chmod(private_path, 0o600)
    public = sanitize_for_public(summary)
    PUBLIC_JSON.write_text(json.dumps(public, ensure_ascii=False, indent=2))
    lines = [
        '# LK OS Data Spine — snapshot read-only 2026-05-11',
        '',
        f"Gerado em: `{summary['generated_at']}`.",
        '',
        'Escopo: snapshot operacional read-only de frescor/contagem/status. Não executa writes, envios, campanhas, alterações de estoque, alterações de preço ou banco de produção.',
        '',
        f"Arquivo privado auditável, fora do Git: `{private_path}`.",
        '',
        '## Resultado por fonte',
        '',
    ]
    for item in public['sources']:
        lines += [
            f"### {item['source']}",
            '',
            f"- Status: `{'OK' if item.get('ok') else 'ATENÇÃO'}`",
            f"- Rótulo: `{item.get('fact_label')}`",
        ]
        for k in ['product_count', 'orders_7d_count', 'products_sample_count', 'orders_sample_count', 'stock_checks_sample_count', 'official_deposit_seen_in_sample', 'row_count', 'rows', 'google_ads_rows', 'lists_sample_count', 'campaigns_sample_count']:
            if k in item:
                lines.append(f"- {k}: `{item.get(k)}`")
        if item.get('freshness'):
            lines.append(f"- Freshness: `{json.dumps(item.get('freshness'), ensure_ascii=False)}`")
        if item.get('date_range'):
            lines.append(f"- Janela: `{item['date_range'].get('start')}` a `{item['date_range'].get('end')}`")
        if item.get('status'):
            lines.append(f"- Observação/status: `{item.get('status')}`")
        if item.get('note'):
            lines.append(f"- Nota: {item.get('note')}")
        lines.append('')
    ok_count = sum(1 for s in public['sources'] if s.get('ok'))
    lines += [
        '## Leitura executiva',
        '',
        f"- Fontes OK: `{ok_count}/{len(public['sources'])}`.",
        '- Shopify continua sendo `fact_shopify` para pedidos, vendas, catálogo e SKU canônico.',
        '- Tiny continua sendo `fact_tiny_stock`; o depósito oficial é `LK | CONTROLE ESTOQUE`.',
        '- GA4 é `fact_ga4` para tráfego/canal/funil, não receita final.',
        '- Meta, Google/Metricool e Klaviyo entram como `platform_signal` até reconciliação com Shopify/GA4.',
        '',
        '## O que este script não fez',
        '',
        '- Não enviou e-mail, WhatsApp ou campanha.',
        '- Não alterou Shopify, Tiny, Klaviyo, Meta, Google, Metricool, Supabase, Notion, n8n ou banco de produção.',
        '- Não exportou PII para o repositório.',
    ]
    PUBLIC_MD.write_text('\n'.join(lines) + '\n')


def main() -> None:
    started = now_utc()
    secrets = load_secrets()
    collectors = [shopify_snapshot, tiny_snapshot, ga4_snapshot, meta_snapshot, metricool_snapshot, klaviyo_snapshot]
    sources = []
    for fn in collectors:
        try:
            sources.append(fn(secrets))
        except Exception as exc:
            sources.append({'source': fn.__name__.replace('_snapshot', ''), 'fact_label': 'unknown', 'ok': False, 'status': 'collector_exception', 'error': type(exc).__name__, 'message': str(exc)[:300]})
    summary = {
        'generated_at': started,
        'finished_at': now_utc(),
        'scope': 'LK OS Data Spine read-only source freshness/count/status snapshots',
        'sources': sources,
    }
    write_outputs(summary)
    print(json.dumps({'ok_sources': sum(1 for s in sources if s.get('ok')), 'total_sources': len(sources), 'public_json': str(PUBLIC_JSON), 'public_md': str(PUBLIC_MD)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
