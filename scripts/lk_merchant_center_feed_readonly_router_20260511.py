#!/usr/bin/env python3
"""LK Merchant Center feed read-only router.

Reads Google Merchant Center product statuses via Doppler-sourced Google credentials
in-process only. It produces a feed/PDP diagnostic queue for LK OS Phase 6 without
changing Merchant Center, Shopify, feed, theme, Search Console, or public content.
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
from collections import Counter, defaultdict
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOPPLER_TOKEN_FILE = pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
OUT_JSON = ROOT / 'reports/lk-merchant-center-feed-readonly-router-2026-05-11.json'
OUT_MD = ROOT / 'reports/lk-merchant-center-feed-readonly-router-2026-05-11.md'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/merchant-center-feed-readonly-router-2026-05-11.md'
GSC_REPORT = ROOT / 'reports/lk-search-console-readonly-router-2026-05-11.json'

CONTENT_SCOPE = 'https://www.googleapis.com/auth/content'
MAX_PRODUCTS = 5000


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
    missing = [k for k in ['client_email', 'private_key', 'token_uri'] if not sa.get(k)]
    if missing:
        raise RuntimeError('service_account_missing_' + '_'.join(missing))
    return sa


def sign_jwt_with_openssl(sa: dict[str, Any]) -> str:
    now = int(time.time())
    claim = {
        'iss': sa['client_email'],
        'scope': CONTENT_SCOPE,
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
        proc = subprocess.run(['openssl', 'dgst', '-sha256', '-sign', key_path], input=signing_input.encode(), capture_output=True, check=True)
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
        return json.loads(r.read().decode())['access_token']


def get_json(url: str, token: str) -> dict[str, Any]:
    req = urllib.request.Request(url)
    req.add_header('Authorization', 'Bearer ' + token)
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        text = e.read().decode(errors='replace')
        try:
            body = json.loads(text)
        except Exception:
            body = {'raw': text[:500]}
        raise RuntimeError(f'merchant_api_failed_{e.code}: {json.dumps(body)[:400]}') from e


def fetch_product_statuses(token: str, merchant_id: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    page_token = None
    while len(rows) < MAX_PRODUCTS:
        qs = {'maxResults': '250'}
        if page_token:
            qs['pageToken'] = page_token
        url = f"https://shoppingcontent.googleapis.com/content/v2.1/{merchant_id}/productstatuses?" + urllib.parse.urlencode(qs)
        data = get_json(url, token)
        resources = data.get('resources') or []
        rows.extend(resources)
        page_token = data.get('nextPageToken')
        if not page_token or not resources:
            break
    return rows[:MAX_PRODUCTS]


def load_gsc_priority_pages() -> dict[str, dict[str, Any]]:
    if not GSC_REPORT.exists():
        return {}
    data = json.loads(GSC_REPORT.read_text())
    out: dict[str, dict[str, Any]] = {}
    for opp in data.get('opportunities', []):
        page = opp.get('page')
        if page and page not in out:
            out[page] = {
                'query': opp.get('query'),
                'priority': opp.get('priority'),
                'impressions': opp.get('impressions'),
                'ctr_percent': opp.get('ctr_percent'),
                'position': opp.get('position'),
                'source_label': 'fact_gsc',
            }
    return out


def destination_summary(status: dict[str, Any]) -> tuple[list[str], list[str], list[str]]:
    approved, disapproved, pending = [], [], []
    for dest in status.get('destinationStatuses') or []:
        name = dest.get('destination') or dest.get('destinationName') or 'unknown'
        stat = (dest.get('status') or '').lower()
        if stat == 'approved':
            approved.append(name)
        elif stat in {'disapproved', 'excluded'}:
            disapproved.append(name)
        else:
            pending.append(f'{name}:{stat or "unknown"}')
    return approved, disapproved, pending


def classify_product(status: dict[str, Any], gsc_by_page: dict[str, dict[str, Any]]) -> dict[str, Any]:
    issues = status.get('itemLevelIssues') or []
    approved, disapproved, pending = destination_summary(status)
    link = status.get('link') or ''
    gsc = gsc_by_page.get(link)
    if disapproved or issues:
        priority = 'P1'
        action = 'feed_issue_fix_preview'
        reason = 'produto com issue/reprovação em Merchant Center'
    elif gsc:
        priority = 'P2'
        action = 'gsc_feed_pdp_alignment_preview'
        reason = 'PDP/collection tem oportunidade GSC e feed aprovado deve ser mantido alinhado'
    elif pending:
        priority = 'P2'
        action = 'merchant_pending_status_monitor'
        reason = 'status Merchant pendente/não aprovado em pelo menos um destino'
    else:
        priority = 'P3'
        action = 'monitor'
        reason = 'sem issue Merchant e sem cruzamento GSC prioritário nesta janela'
    issue_codes = [i.get('code') or i.get('attributeName') or 'unknown_issue' for i in issues]
    issue_details = []
    for i in issues[:5]:
        issue_details.append({
            'code': i.get('code'),
            'attribute': i.get('attributeName'),
            'description': i.get('description'),
            'detail': i.get('detail'),
            'servability': i.get('servability'),
            'resolution': i.get('resolution'),
        })
    return {
        'priority': priority,
        'recommended_action': action,
        'reason': reason,
        'product_id': status.get('productId'),
        'title': status.get('title'),
        'link': link,
        'approved_destinations': approved,
        'disapproved_destinations': disapproved,
        'pending_destinations': pending,
        'item_issue_count': len(issues),
        'item_issue_codes': issue_codes,
        'item_issue_details': issue_details,
        'gsc_context': gsc,
        'approval_status': 'read_only_preview',
        'write_allowed_now': False,
        'source_label': 'fact_merchant_center',
    }


def build_payload(statuses: list[dict[str, Any]], merchant_id_present: bool) -> dict[str, Any]:
    gsc_by_page = load_gsc_priority_pages()
    rows = [classify_product(s, gsc_by_page) for s in statuses]
    queue = [r for r in rows if r['priority'] in {'P1', 'P2'}]
    priority_order = {'P1': 0, 'P2': 1, 'P3': 2}
    queue.sort(key=lambda r: (priority_order.get(r['priority'], 9), -r['item_issue_count'], r.get('title') or ''))

    dest_counter = Counter()
    issue_counter = Counter()
    for r in rows:
        if r['disapproved_destinations']:
            dest_counter.update('disapproved:' + d for d in r['disapproved_destinations'])
        if r['pending_destinations']:
            dest_counter.update('pending:' + d for d in r['pending_destinations'])
        issue_counter.update(r['item_issue_codes'])

    issue_groups: dict[tuple[str, str], dict[str, Any]] = {}
    for r in queue:
        code_key = ', '.join(sorted(set(r['item_issue_codes']))[:6]) or 'no_item_issue_code'
        dest_key = ', '.join(sorted(r['disapproved_destinations'])) or 'no_disapproved_destination'
        key = (code_key, dest_key)
        if key not in issue_groups:
            issue_groups[key] = {
                'priority': r['priority'],
                'issue_codes': code_key,
                'disapproved_destinations': dest_key,
                'count': 0,
                'sample_product_ids': [],
                'sample_links': [],
                'recommended_action': r['recommended_action'],
                'approval_status': 'read_only_preview',
                'write_allowed_now': False,
                'source_label': 'fact_merchant_center',
            }
        issue_groups[key]['count'] += 1
        if len(issue_groups[key]['sample_product_ids']) < 8:
            issue_groups[key]['sample_product_ids'].append(r.get('product_id'))
        if r.get('link') and len(issue_groups[key]['sample_links']) < 3:
            issue_groups[key]['sample_links'].append(r['link'])
    grouped = sorted(issue_groups.values(), key=lambda g: (-g['count'], g['issue_codes']))

    summary = {
        'merchant_center_id_present': merchant_id_present,
        'product_statuses_read': len(statuses),
        'queue_items': len(queue),
        'p1_items': sum(1 for r in queue if r['priority'] == 'P1'),
        'p2_items': sum(1 for r in queue if r['priority'] == 'P2'),
        'products_with_item_issues': sum(1 for r in rows if r['item_issue_count'] > 0),
        'products_with_disapproved_destination': sum(1 for r in rows if r['disapproved_destinations']),
        'products_crossing_gsc_priority': sum(1 for r in rows if r['gsc_context']),
        'issue_groups': len(grouped),
        'writes_allowed_now': 0,
    }
    return {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'LK Merchant Center feed read-only router',
        'summary': summary,
        'issue_groups': grouped[:30],
        'queue': queue[:80],
        'top_issue_codes': [{'issue': k, 'count': v} for k, v in issue_counter.most_common(20)],
        'destination_status_counts': [{'status': k, 'count': v} for k, v in dest_counter.most_common(20)],
        'guardrails': [
            'Merchant Center status is fact_merchant_center for feed health; Shopify remains source for product data and commerce state.',
            'Feed, Shopify, PDP, image, title/meta, Merchant Center and Google admin changes require preview and Lucas approval.',
            'This step uses GET/list endpoints only and does not call insert/update/delete/custombatch or supplemental feed mutations.',
            'No customer PII is used or exported.',
        ],
        'not_performed': [
            'merchant_center_write', 'feed_update', 'supplemental_feed_update', 'product_insert',
            'product_delete', 'shopify_write', 'theme_write', 'gsc_admin_change', 'indexing_api_submit',
            'content_publish', 'campaign_or_customer_send', 'cron_creation'
        ],
    }


def markdown(payload: dict[str, Any]) -> str:
    s = payload['summary']
    lines = [
        '# LK Merchant Center Feed Read-only Router, 2026-05-11',
        '',
        f"Generated at: `{payload['generated_at']}`",
        '',
        '## Veredito',
        '',
        'Merchant Center entrou na Fase 6 como fonte `fact_merchant_center`: status de feed, destinos, issues de item e cruzamento com GSC agora viram fila de diagnóstico, sem write em feed, Shopify ou Google.',
        '',
        '## Snapshot',
        '',
        f"- Merchant Center ID presente no Doppler: {s['merchant_center_id_present']}",
        f"- Produtos/status lidos: {s['product_statuses_read']}",
        f"- Itens roteados na fila: {s['queue_items']}",
        f"- P1: {s['p1_items']}",
        f"- P2: {s['p2_items']}",
        f"- Produtos com issue de item: {s['products_with_item_issues']}",
        f"- Produtos com destino reprovado: {s['products_with_disapproved_destination']}",
        f"- Produtos cruzando oportunidade GSC: {s['products_crossing_gsc_priority']}",
        f"- Writes liberados agora: {s['writes_allowed_now']}",
        '',
        '## Top grupos de problema',
        '',
    ]
    if payload.get('issue_groups'):
        for i, group in enumerate(payload['issue_groups'][:12], 1):
            lines.extend([
                f"### {i}. {group['priority']} · {group['recommended_action']} · {group['count']} itens",
                f"- Issue codes: {group['issue_codes']}",
                f"- Destinos reprovados: {group['disapproved_destinations']}",
                f"- Amostras de produto: {', '.join([x for x in group['sample_product_ids'] if x][:5])}",
                f"- Status: `{group['approval_status']}`",
                '',
            ])
    else:
        lines.append('- Nenhum grupo P1/P2 encontrado nesta leitura; manter monitoramento e cruzar com próxima fila GSC/Shopify.')
        lines.append('')
    lines.extend(['## Amostras de fila individual', ''])
    if payload['queue']:
        for i, item in enumerate(payload['queue'][:8], 1):
            lines.extend([
                f"### {i}. {item['priority']} · {item['recommended_action']}",
                f"- Produto: {item.get('title') or '(sem título)'}",
                f"- Link: {item.get('link') or '(sem link)'}",
                f"- Issues: {item['item_issue_count']} · {', '.join(item['item_issue_codes'][:5]) if item['item_issue_codes'] else 'nenhuma'}",
                f"- Destinos reprovados: {', '.join(item['disapproved_destinations']) if item['disapproved_destinations'] else 'nenhum'}",
                f"- Destinos pendentes: {', '.join(item['pending_destinations']) if item['pending_destinations'] else 'nenhum'}",
                f"- Motivo: {item['reason']}",
                f"- Status: `{item['approval_status']}`",
                '',
            ])
            if item.get('gsc_context'):
                g = item['gsc_context']
                lines.extend([
                    f"  - Cruzamento GSC: `{g.get('query')}`, {g.get('impressions')} impressões, CTR {g.get('ctr_percent')}%, posição {g.get('position')}",
                    '',
                ])
    else:
        lines.append('- Nenhum item P1/P2 encontrado nesta leitura; manter monitoramento e cruzar com próxima fila GSC/Shopify.')
        lines.append('')
    lines.extend(['## Top issue codes', ''])
    if payload['top_issue_codes']:
        for x in payload['top_issue_codes'][:15]:
            lines.append(f"- {x['issue']}: {x['count']}")
    else:
        lines.append('- Nenhum issue code retornado no recorte lido.')
    lines.extend(['', '## Guardrails', ''])
    for g in payload['guardrails']:
        lines.append(f'- {g}')
    lines.extend(['', '## O que não foi feito', ''])
    for n in payload['not_performed']:
        lines.append(f'- {n}')
    return '\n'.join(lines) + '\n'


def main() -> None:
    secrets = load_doppler()
    merchant_id = secrets.get('MERCHANT_CENTER_ID_LK')
    if not merchant_id:
        payload = {
            'generated_at': datetime.now(timezone.utc).isoformat(),
            'scope': 'LK Merchant Center feed read-only router',
            'summary': {
                'merchant_center_id_present': False,
                'product_statuses_read': 0,
                'queue_items': 0,
                'p1_items': 0,
                'p2_items': 0,
                'products_with_item_issues': 0,
                'products_with_disapproved_destination': 0,
                'products_crossing_gsc_priority': 0,
                'writes_allowed_now': 0,
            },
            'queue': [],
            'top_issue_codes': [],
            'destination_status_counts': [],
            'guardrails': ['Merchant Center ID missing; do not invent feed issues.'],
            'not_performed': ['merchant_center_write', 'feed_update', 'shopify_write', 'cron_creation'],
        }
    else:
        token = access_token(parse_service_account(secrets))
        statuses = fetch_product_statuses(token, merchant_id)
        payload = build_payload(statuses, merchant_id_present=True)
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    text = markdown(payload)
    OUT_MD.write_text(text, encoding='utf-8')
    BRAIN_DOC.write_text(text, encoding='utf-8')
    print(json.dumps({'ok': True, 'summary': payload['summary']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
