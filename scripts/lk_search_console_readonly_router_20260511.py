#!/usr/bin/env python3
"""LK Search Console read-only router.

Fetches Google Search Console Search Analytics for LK using Doppler-sourced
service-account credentials in-process only. Produces a sanitized opportunity
queue: queries, pages, CTR, position and recommended SEO/CRO action. No writes,
no Indexing API calls, no Merchant Center changes, no Shopify changes.
"""
from __future__ import annotations

import base64
import hashlib
import json
import os
import pathlib
import subprocess
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOPPLER_TOKEN_FILE = pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
OUT_JSON = ROOT / 'reports/lk-search-console-readonly-router-2026-05-11.json'
OUT_MD = ROOT / 'reports/lk-search-console-readonly-router-2026-05-11.md'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/search-console-readonly-router-2026-05-11.md'

SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']


def b64url(raw: bytes) -> str:
    return base64.urlsafe_b64encode(raw).decode().rstrip('=')


def http_json(url: str, method: str = 'GET', headers: dict[str, str] | None = None, payload: Any | None = None) -> tuple[int, Any]:
    data = None if payload is None else json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, method=method)
    for k, v in (headers or {}).items():
        req.add_header(k, v)
    if data is not None:
        req.add_header('Content-Type', 'application/json')
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            text = r.read().decode()
            return r.status, json.loads(text) if text else {}
    except urllib.error.HTTPError as e:
        text = e.read().decode(errors='replace')
        try:
            body = json.loads(text)
        except Exception:
            body = {'raw': text[:500]}
        return e.code, body


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
        # Some stores use base64 encoded JSON.
        sa = json.loads(base64.b64decode(raw).decode())
    needed = ['client_email', 'private_key', 'token_uri']
    missing = [k for k in needed if not sa.get(k)]
    if missing:
        raise RuntimeError('service_account_missing_' + '_'.join(missing))
    return sa


def sign_jwt_with_openssl(sa: dict[str, Any]) -> str:
    now = int(time.time())
    claim = {
        'iss': sa['client_email'],
        'scope': ' '.join(SCOPES),
        'aud': sa.get('token_uri') or 'https://oauth2.googleapis.com/token',
        'iat': now,
        'exp': now + 3600,
    }
    header = {'alg': 'RS256', 'typ': 'JWT'}
    signing_input = b64url(json.dumps(header, separators=(',', ':')).encode()) + '.' + b64url(json.dumps(claim, separators=(',', ':')).encode())
    with tempfile.NamedTemporaryFile('w', delete=False) as key_file:
        key_file.write(sa['private_key'])
        key_path = key_file.name
    try:
        proc = subprocess.run(
            ['openssl', 'dgst', '-sha256', '-sign', key_path],
            input=signing_input.encode(),
            capture_output=True,
            check=True,
        )
    finally:
        pathlib.Path(key_path).unlink(missing_ok=True)
    return signing_input + '.' + b64url(proc.stdout)


def access_token(sa: dict[str, Any]) -> str:
    assertion = sign_jwt_with_openssl(sa)
    body = urllib.parse.urlencode({
        'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer',
        'assertion': assertion,
    }).encode()
    req = urllib.request.Request(sa.get('token_uri') or 'https://oauth2.googleapis.com/token', data=body, method='POST')
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    with urllib.request.urlopen(req, timeout=60) as r:
        token = json.loads(r.read().decode())
    return token['access_token']


def query_gsc(token: str, site_url: str, start: str, end: str, dimensions: list[str], row_limit: int = 25000) -> dict[str, Any]:
    encoded = urllib.parse.quote(site_url, safe='')
    url = f'https://searchconsole.googleapis.com/webmasters/v3/sites/{encoded}/searchAnalytics/query'
    payload = {
        'startDate': start,
        'endDate': end,
        'dimensions': dimensions,
        'rowLimit': row_limit,
        'searchType': 'web',
        'dataState': 'final',
    }
    status, body = http_json(url, method='POST', headers={'Authorization': 'Bearer ' + token}, payload=payload)
    if status >= 400:
        raise RuntimeError(f'gsc_query_failed_{status}: {json.dumps(body)[:300]}')
    return body


def classify(row: dict[str, Any]) -> dict[str, Any]:
    clicks = row.get('clicks', 0)
    impressions = row.get('impressions', 0)
    ctr = row.get('ctr', 0.0)
    pos = row.get('position', 0.0)
    if impressions >= 500 and pos <= 12 and ctr < 0.03:
        action = 'title_meta_ctr_preview'
        priority = 'P1'
        reason = 'impressões altas, posição próxima da primeira página e CTR baixo'
    elif impressions >= 300 and 4 <= pos <= 15:
        action = 'content_onpage_boost_preview'
        priority = 'P1'
        reason = 'posição 4–15 com volume suficiente para ganho por on-page/conteúdo'
    elif impressions >= 100 and clicks == 0:
        action = 'serp_copy_or_intent_check'
        priority = 'P2'
        reason = 'impressões sem clique, provável desalinhamento de título/meta/intenção'
    elif clicks >= 10 and pos > 10:
        action = 'supporting_content_or_internal_links'
        priority = 'P2'
        reason = 'já recebe cliques apesar de posição baixa, merece reforço'
    else:
        action = 'monitor'
        priority = 'P3'
        reason = 'sem alavanca clara nesta janela'
    return {'priority': priority, 'recommended_action': action, 'reason': reason}


def build_router(gsc_rows: list[dict[str, Any]], page_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    opportunities = []
    for row in gsc_rows:
        keys = row.get('keys') or []
        if len(keys) < 2:
            continue
        query, page = keys[0], keys[1]
        cls = classify(row)
        if cls['priority'] == 'P3':
            continue
        # queries are GSC aggregate search terms, not customer PII, but avoid very long/raw weird strings.
        if len(query) > 120:
            query_display = query[:117] + '...'
        else:
            query_display = query
        opportunities.append({
            'priority': cls['priority'],
            'query': query_display,
            'page': page,
            'clicks': row.get('clicks', 0),
            'impressions': row.get('impressions', 0),
            'ctr_percent': round((row.get('ctr', 0.0) or 0.0) * 100, 2),
            'position': round(row.get('position', 0.0) or 0.0, 1),
            'recommended_action': cls['recommended_action'],
            'reason': cls['reason'],
            'approval_status': 'read_only_preview',
            'write_allowed_now': False,
            'source_label': 'fact_gsc',
        })
    opportunities.sort(key=lambda x: (x['priority'], -x['impressions'], x['position']))
    return opportunities[:40]


def summarize_pages(page_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    pages = []
    for row in page_rows[:30]:
        page = (row.get('keys') or [''])[0]
        pages.append({
            'page': page,
            'clicks': row.get('clicks', 0),
            'impressions': row.get('impressions', 0),
            'ctr_percent': round((row.get('ctr', 0.0) or 0.0) * 100, 2),
            'position': round(row.get('position', 0.0) or 0.0, 1),
            'source_label': 'fact_gsc',
        })
    return pages


def markdown(payload: dict[str, Any]) -> str:
    s = payload['summary']
    lines = [
        '# LK Search Console Read-only Router, 2026-05-11',
        '',
        f"Generated at: `{payload['generated_at']}`",
        '',
        '## Veredito',
        '',
        'Search Console entrou na Fase 6 como fonte `fact_gsc`: queries, páginas, CTR, posição e oportunidades agora viram fila de melhoria, sem write em Shopify, Merchant Center ou Google.',
        '',
        '## Janela e fonte',
        '',
        f"- Property: `{payload['property']}`",
        f"- Janela: `{payload['window']['start_date']}` a `{payload['window']['end_date']}`",
        f"- Linhas query/página recebidas: {s['query_page_rows']}",
        f"- Páginas agregadas recebidas: {s['page_rows']}",
        f"- Oportunidades roteadas: {s['opportunities']}",
        f"- Writes liberados agora: {s['writes_allowed_now']}",
        '',
        '## Top oportunidades',
        '',
    ]
    for i, o in enumerate(payload['opportunities'][:12], 1):
        lines.extend([
            f"### {i}. {o['priority']} · {o['recommended_action']}",
            f"- Query: `{o['query']}`",
            f"- Página: {o['page']}",
            f"- Clicks/impressões: {o['clicks']} / {o['impressions']}",
            f"- CTR/posição: {o['ctr_percent']}% / {o['position']}",
            f"- Motivo: {o['reason']}",
            f"- Status: `{o['approval_status']}`",
            '',
        ])
    lines.extend(['## Top páginas por impressões', ''])
    for p in payload['top_pages'][:10]:
        lines.append(f"- {p['page']}: {p['clicks']} clicks, {p['impressions']} impressões, CTR {p['ctr_percent']}%, posição {p['position']}")
    lines.extend(['', '## Guardrails', ''])
    for g in payload['guardrails']:
        lines.append(f'- {g}')
    lines.extend(['', '## O que não foi feito', ''])
    for n in payload['not_performed']:
        lines.append(f'- {n}')
    return '\n'.join(lines) + '\n'


def main() -> None:
    generated_at = datetime.now(timezone.utc).isoformat()
    today = date.today()
    end = today - timedelta(days=3)
    start = end - timedelta(days=27)
    secrets = load_doppler()
    property_url = secrets.get('GSC_SITE_URL') or 'sc-domain:lksneakers.com.br'
    sa = parse_service_account(secrets)
    token = access_token(sa)
    query_page = query_gsc(token, property_url, start.isoformat(), end.isoformat(), ['query', 'page'])
    page = query_gsc(token, property_url, start.isoformat(), end.isoformat(), ['page'])
    rows = query_page.get('rows') or []
    page_rows = page.get('rows') or []
    opportunities = build_router(rows, page_rows)
    payload = {
        'generated_at': generated_at,
        'scope': 'LK Search Console read-only opportunity router',
        'property': property_url,
        'window': {'start_date': start.isoformat(), 'end_date': end.isoformat(), 'data_state': 'final'},
        'summary': {
            'query_page_rows': len(rows),
            'page_rows': len(page_rows),
            'opportunities': len(opportunities),
            'p1_opportunities': sum(1 for o in opportunities if o['priority'] == 'P1'),
            'p2_opportunities': sum(1 for o in opportunities if o['priority'] == 'P2'),
            'writes_allowed_now': 0,
        },
        'opportunities': opportunities,
        'top_pages': summarize_pages(page_rows),
        'guardrails': [
            'GSC is fact_gsc for search demand; Shopify remains source for products/orders.',
            'Title/meta/PDP changes require preview and Lucas approval before Shopify writes.',
            'No Indexing API, Merchant Center, Shopify, theme or feed writes in this step.',
            'No customer PII is used or exported.',
        ],
        'not_performed': [
            'shopify_write', 'theme_write', 'merchant_center_write', 'gsc_admin_change',
            'indexing_api_submit', 'content_publish', 'campaign_or_customer_send', 'cron_creation'
        ],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    text = markdown(payload)
    OUT_MD.write_text(text, encoding='utf-8')
    BRAIN_DOC.write_text(text.replace('# LK Search Console Read-only Router, 2026-05-11', '# LK Search Console Read-only Router, 2026-05-11'), encoding='utf-8')
    print(json.dumps({'ok': True, 'summary': payload['summary'], 'property': property_url}, ensure_ascii=False))


if __name__ == '__main__':
    main()
