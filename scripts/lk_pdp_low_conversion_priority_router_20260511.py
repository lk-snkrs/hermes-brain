#!/usr/bin/env python3
"""LK PDP/page low-conversion priority router, read-only.

Combines GA4 landing-page conversion facts with the previously materialized
Search Console and Merchant Center read-only routers. Produces a prioritized
SEO/CRO queue for PDPs, collections and homepage with no Shopify, theme,
Merchant, GSC, feed, content, or campaign writes.
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
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOPPLER_TOKEN_FILE = pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
GSC_REPORT = ROOT / 'reports/lk-search-console-readonly-router-2026-05-11.json'
MERCHANT_REPORT = ROOT / 'reports/lk-merchant-center-feed-readonly-router-2026-05-11.json'
OUT_JSON = ROOT / 'reports/lk-pdp-low-conversion-priority-router-2026-05-11.json'
OUT_MD = ROOT / 'reports/lk-pdp-low-conversion-priority-router-2026-05-11.md'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/pdp-low-conversion-priority-router-2026-05-11.md'
PROPERTY_ID = '348553567'
BASE_URL = 'https://lksneakers.com.br'


def b64url(raw: bytes) -> str:
    return base64.urlsafe_b64encode(raw).decode().rstrip('=')


def load_doppler() -> dict[str, str]:
    token = os.environ.get('DOPPLER_TOKEN') or DOPPLER_TOKEN_FILE.read_text().strip()
    req = urllib.request.Request('https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json')
    req.add_header('Authorization', 'Basic ' + base64.b64encode((token + ':').encode()).decode())
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def parse_service_account(secrets: dict[str, str]) -> dict[str, Any]:
    raw = secrets.get('GOOGLE_SERVICE_ACCOUNT_JSON') or secrets.get('GA4_LK_N8N_ZIPPER_SERVICE_ACCOUNT') or secrets.get('GA4_LK_SERVICE_ACCOUNT')
    if not raw:
        raise RuntimeError('missing_google_service_account_secret')
    try:
        sa = json.loads(raw)
    except json.JSONDecodeError:
        sa = json.loads(base64.b64decode(raw).decode())
    for key in ['client_email', 'private_key', 'token_uri']:
        if not sa.get(key):
            raise RuntimeError(f'service_account_missing_{key}')
    return sa


def sign_jwt_with_openssl(sa: dict[str, Any], scope: str) -> str:
    now = int(time.time())
    header = {'alg': 'RS256', 'typ': 'JWT'}
    claim = {
        'iss': sa['client_email'],
        'scope': scope,
        'aud': sa.get('token_uri') or 'https://oauth2.googleapis.com/token',
        'iat': now,
        'exp': now + 3600,
    }
    signing_input = b64url(json.dumps(header, separators=(',', ':')).encode()) + '.' + b64url(json.dumps(claim, separators=(',', ':')).encode())
    with tempfile.NamedTemporaryFile('w', delete=False) as key_file:
        key_file.write(sa['private_key'])
        key_path = key_file.name
    try:
        proc = subprocess.run(['openssl', 'dgst', '-sha256', '-sign', key_path], input=signing_input.encode(), capture_output=True, check=True)
    finally:
        pathlib.Path(key_path).unlink(missing_ok=True)
    return signing_input + '.' + b64url(proc.stdout)


def access_token(sa: dict[str, Any], scope: str) -> str:
    body = urllib.parse.urlencode({
        'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer',
        'assertion': sign_jwt_with_openssl(sa, scope),
    }).encode()
    req = urllib.request.Request(sa.get('token_uri') or 'https://oauth2.googleapis.com/token', data=body, method='POST')
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())['access_token']


def ga4_run_report(token: str, start_date: str, end_date: str) -> list[dict[str, Any]]:
    payload = {
        'dateRanges': [{'startDate': start_date, 'endDate': end_date}],
        'dimensions': [{'name': 'landingPagePlusQueryString'}],
        'metrics': [
            {'name': 'sessions'},
            {'name': 'totalUsers'},
            {'name': 'screenPageViews'},
            {'name': 'ecommercePurchases'},
            {'name': 'purchaseRevenue'},
        ],
        'limit': 5000,
        'orderBys': [{'metric': {'metricName': 'sessions'}, 'desc': True}],
    }
    req = urllib.request.Request(
        f'https://analyticsdata.googleapis.com/v1beta/properties/{PROPERTY_ID}:runReport',
        data=json.dumps(payload).encode(), method='POST')
    req.add_header('Authorization', 'Bearer ' + token)
    req.add_header('Content-Type', 'application/json')
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            data = json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f'ga4_run_report_failed_{e.code}: {e.read().decode(errors="replace")[:400]}') from e
    rows = []
    for row in data.get('rows') or []:
        path = row['dimensionValues'][0]['value']
        mv = [m['value'] for m in row['metricValues']]
        sessions = int(float(mv[0] or 0))
        users = int(float(mv[1] or 0))
        views = int(float(mv[2] or 0))
        purchases = int(float(mv[3] or 0))
        revenue = float(mv[4] or 0)
        if path == '(not set)' or not path.startswith('/'):
            continue
        clean_path = path.split('?')[0]
        rows.append({
            'path': clean_path,
            'url': BASE_URL + clean_path,
            'sessions': sessions,
            'total_users': users,
            'screen_page_views': views,
            'ecommerce_purchases': purchases,
            'purchase_revenue': round(revenue, 2),
            'landing_purchase_rate_percent': round((purchases / sessions) * 100, 2) if sessions else 0.0,
            'source_label': 'fact_ga4',
        })
    return rows


def page_type(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    path = parsed.path
    if path == '/':
        return 'homepage'
    if path.startswith('/products/'):
        return 'pdp'
    if path.startswith('/collections/'):
        return 'collection'
    return 'other'


def load_gsc_context() -> dict[str, dict[str, Any]]:
    if not GSC_REPORT.exists():
        return {}
    data = json.loads(GSC_REPORT.read_text())
    out: dict[str, dict[str, Any]] = {}
    for page in data.get('top_pages', []):
        out[page['page']] = page
    for opp in data.get('opportunities', []):
        current = out.setdefault(opp['page'], {
            'page': opp['page'], 'clicks': 0, 'impressions': 0, 'ctr_percent': 0, 'position': None, 'source_label': 'fact_gsc'
        })
        current.setdefault('queries', [])
        current['queries'].append({
            'query': opp.get('query'), 'impressions': opp.get('impressions'), 'ctr_percent': opp.get('ctr_percent'), 'position': opp.get('position'), 'priority': opp.get('priority')
        })
    return out


def load_merchant_context() -> dict[str, dict[str, Any]]:
    if not MERCHANT_REPORT.exists():
        return {}
    data = json.loads(MERCHANT_REPORT.read_text())
    out: dict[str, dict[str, Any]] = {}
    for item in data.get('queue', []):
        link = item.get('link')
        if link:
            out[link.split('?')[0]] = {
                'priority': item.get('priority'),
                'item_issue_count': item.get('item_issue_count'),
                'item_issue_codes': sorted(set(item.get('item_issue_codes') or []))[:8],
                'disapproved_destinations': item.get('disapproved_destinations') or [],
                'source_label': 'fact_merchant_center',
            }
    return out


def classify(row: dict[str, Any], gsc: dict[str, Any] | None, merchant: dict[str, Any] | None) -> dict[str, Any]:
    sessions = row['sessions']
    purchases = row['ecommerce_purchases']
    cvr = row['landing_purchase_rate_percent']
    ptype = page_type(row['url'])
    impressions = int((gsc or {}).get('impressions') or 0)
    ctr = float((gsc or {}).get('ctr_percent') or 0)
    merchant_issues = int((merchant or {}).get('item_issue_count') or 0)

    score = 0
    reasons: list[str] = []
    if sessions >= 250:
        score += 30; reasons.append('alto tráfego GA4')
    elif sessions >= 100:
        score += 18; reasons.append('tráfego médio GA4')
    if purchases == 0 and sessions >= 100:
        score += 30; reasons.append('zero compras atribuídas à landing page')
    elif cvr < 0.35 and sessions >= 100:
        score += 22; reasons.append('conversão de landing baixa')
    elif cvr < 0.8 and sessions >= 100:
        score += 12; reasons.append('conversão abaixo do esperado')
    if impressions >= 10000 and ctr < 1.0:
        score += 25; reasons.append('muita impressão GSC com CTR baixo')
    elif impressions >= 5000 and ctr < 2.0:
        score += 15; reasons.append('oportunidade orgânica GSC')
    if merchant_issues:
        score += 18; reasons.append('issue Merchant no produto/feed')
    if ptype == 'pdp':
        score += 8; reasons.append('PDP diretamente acionável')
    elif ptype == 'collection':
        score += 5; reasons.append('collection comercial relevante')

    if score >= 60:
        priority = 'P1'
    elif score >= 38:
        priority = 'P2'
    else:
        priority = 'P3'

    actions = []
    if impressions and ctr < 1.5:
        actions.append('title_meta_ctr_preview')
    if purchases == 0 or cvr < 0.5:
        actions.append('pdp_cro_above_fold_preview')
    if merchant_issues:
        actions.append('merchant_feed_issue_preview')
    if not actions:
        actions.append('monitor')

    return {
        **row,
        'page_type': ptype,
        'priority': priority,
        'score': score,
        'reason': '; '.join(reasons) if reasons else 'monitoramento sem bloqueio crítico',
        'recommended_actions': actions,
        'gsc_context': gsc,
        'merchant_context': merchant,
        'approval_status': 'read_only_preview',
        'write_allowed_now': False,
        'source_labels': ['fact_ga4'] + (['fact_gsc'] if gsc else []) + (['fact_merchant_center'] if merchant else []),
    }


def build_payload(ga4_rows: list[dict[str, Any]], gsc_by_url: dict[str, dict[str, Any]], merchant_by_url: dict[str, dict[str, Any]], start_date: str, end_date: str) -> dict[str, Any]:
    candidates = []
    for row in ga4_rows:
        if page_type(row['url']) not in {'pdp', 'collection', 'homepage'}:
            continue
        if row['sessions'] < 80:
            continue
        candidates.append(classify(row, gsc_by_url.get(row['url']), merchant_by_url.get(row['url'])))
    candidates.sort(key=lambda x: (x['priority'], -x['score'], -x['sessions'], x['url']))
    queue = [c for c in candidates if c['priority'] in {'P1', 'P2'}]
    summary = {
        'ga4_rows_read': len(ga4_rows),
        'candidate_pages': len(candidates),
        'queue_items': len(queue),
        'p1_items': sum(1 for x in queue if x['priority'] == 'P1'),
        'p2_items': sum(1 for x in queue if x['priority'] == 'P2'),
        'pdp_items': sum(1 for x in queue if x['page_type'] == 'pdp'),
        'collection_items': sum(1 for x in queue if x['page_type'] == 'collection'),
        'homepage_items': sum(1 for x in queue if x['page_type'] == 'homepage'),
        'zero_purchase_items': sum(1 for x in queue if x['ecommerce_purchases'] == 0),
        'gsc_joined_items': sum(1 for x in queue if x['gsc_context']),
        'merchant_joined_items': sum(1 for x in queue if x['merchant_context']),
        'writes_allowed_now': 0,
    }
    return {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'LK PDP/collection low-conversion priority router',
        'window': {'start_date': start_date, 'end_date': end_date},
        'summary': summary,
        'queue': queue[:80],
        'guardrails': [
            'GA4 landing-page metrics are fact_ga4; GSC metrics are fact_gsc; Merchant feed statuses are fact_merchant_center.',
            'Landing-page purchase rate is directional CRO triage, not a full attribution model.',
            'Any Shopify SEO field, PDP content, image, theme, feed, Merchant or Google change requires preview and Lucas approval.',
            'No customer PII is used or exported.',
        ],
        'not_performed': [
            'shopify_write', 'theme_write', 'pdp_content_update', 'seo_field_update', 'merchant_center_write',
            'feed_update', 'gsc_admin_change', 'indexing_api_submit', 'content_publish', 'campaign_or_customer_send', 'cron_creation'
        ],
    }


def markdown(payload: dict[str, Any]) -> str:
    s = payload['summary']
    lines = [
        '# LK PDP Low-conversion Priority Router, 2026-05-11',
        '',
        f"Generated at: `{payload['generated_at']}`",
        '',
        '## Veredito',
        '',
        'A Fase 6 agora cruza demanda orgânica e conversão: GA4 identifica páginas com tráfego e baixa compra, GSC adiciona impressão/CTR, Merchant adiciona risco de feed. A saída é fila de preview, sem writes.',
        '',
        '## Snapshot',
        '',
        f"- Janela: {payload['window']['start_date']} a {payload['window']['end_date']}",
        f"- Linhas GA4 lidas: {s['ga4_rows_read']}",
        f"- Páginas candidatas: {s['candidate_pages']}",
        f"- Itens na fila: {s['queue_items']}",
        f"- P1: {s['p1_items']}",
        f"- P2: {s['p2_items']}",
        f"- PDPs: {s['pdp_items']}",
        f"- Collections: {s['collection_items']}",
        f"- Homepage: {s['homepage_items']}",
        f"- Itens com zero compra atribuída: {s['zero_purchase_items']}",
        f"- Itens cruzados com GSC: {s['gsc_joined_items']}",
        f"- Itens cruzados com Merchant: {s['merchant_joined_items']}",
        f"- Writes liberados agora: {s['writes_allowed_now']}",
        '',
        '## Top fila',
        '',
    ]
    for i, item in enumerate(payload['queue'][:20], 1):
        lines.extend([
            f"### {i}. {item['priority']} · {item['page_type']} · score {item['score']}",
            f"- URL: {item['url']}",
            f"- GA4: {item['sessions']} sessões, {item['ecommerce_purchases']} compras, CVR landing {item['landing_purchase_rate_percent']}%, receita R$ {item['purchase_revenue']}",
            f"- Ações preview: {', '.join(item['recommended_actions'])}",
            f"- Motivo: {item['reason']}",
            f"- Fontes: {', '.join(item['source_labels'])}",
            f"- Status: `{item['approval_status']}`",
            '',
        ])
        if item.get('gsc_context'):
            g = item['gsc_context']
            lines.append(f"  - GSC: {g.get('impressions')} impressões, CTR {g.get('ctr_percent')}%, posição {g.get('position')}")
            if g.get('queries'):
                topq = g['queries'][0]
                lines.append(f"  - Query destaque: `{topq.get('query')}`, {topq.get('impressions')} impressões, CTR {topq.get('ctr_percent')}%")
            lines.append('')
        if item.get('merchant_context'):
            m = item['merchant_context']
            lines.append(f"  - Merchant: {m.get('item_issue_count')} issues, códigos {', '.join(m.get('item_issue_codes') or [])}")
            lines.append('')
    lines.extend(['## Guardrails', ''])
    for g in payload['guardrails']:
        lines.append(f'- {g}')
    lines.extend(['', '## O que não foi feito', ''])
    for n in payload['not_performed']:
        lines.append(f'- {n}')
    return '\n'.join(lines) + '\n'


def main() -> None:
    gsc_data = json.loads(GSC_REPORT.read_text())
    start_date = gsc_data['window']['start_date']
    end_date = gsc_data['window']['end_date']
    token = access_token(parse_service_account(load_doppler()), 'https://www.googleapis.com/auth/analytics.readonly')
    ga4_rows = ga4_run_report(token, start_date, end_date)
    payload = build_payload(ga4_rows, load_gsc_context(), load_merchant_context(), start_date, end_date)
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    text = markdown(payload)
    OUT_MD.write_text(text, encoding='utf-8')
    BRAIN_DOC.write_text(text, encoding='utf-8')
    print(json.dumps({'ok': True, 'summary': payload['summary']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
