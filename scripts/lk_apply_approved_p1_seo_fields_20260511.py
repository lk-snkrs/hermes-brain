#!/usr/bin/env python3
"""Apply approved LK P1 SEO title/meta fields to Shopify.

Approval source: Lucas said "Aprovada as melhorias, seguir" after the P1 SEO/CRO approval packets.
Scope applied here is deliberately narrow: SEO title/meta fields for the 8 approved
product/collection packets. Visible CRO recommendations, H1/body/layout/theme,
homepage/admin scope, Merchant, GSC, feed, campaign and customer sends remain blocked.

The script:
- reads approved packets from reports/lk-p1-seo-cro-approval-packets-2026-05-11.json;
- fetches Shopify credentials from Doppler in-process only;
- backs up current live SEO fields;
- applies productUpdate/collectionUpdate GraphQL mutations;
- re-queries live objects and verifies exact target values;
- writes JSON + Markdown audit/rollback artifacts.
"""
from __future__ import annotations

import base64
import json
import os
import pathlib
import re
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOPPLER_TOKEN_FILE = pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
SOURCE = ROOT / 'reports/lk-p1-seo-cro-approval-packets-2026-05-11.json'
OUT_JSON = ROOT / 'reports/lk-approved-p1-seo-fields-execution-2026-05-11.json'
OUT_MD = ROOT / 'reports/lk-approved-p1-seo-fields-execution-2026-05-11.md'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/approved-p1-seo-fields-execution-2026-05-11.md'
API_VERSION = '2024-01'


def doppler_secrets(names: list[str]) -> dict[str, str]:
    token = os.environ.get('DOPPLER_TOKEN')
    if not token:
        token = DOPPLER_TOKEN_FILE.read_text().strip()
    req = urllib.request.Request('https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json')
    req.add_header('Authorization', 'Basic ' + base64.b64encode((token + ':').encode()).decode())
    with urllib.request.urlopen(req, timeout=30) as r:
        all_secrets = json.loads(r.read().decode())
    out = {name: all_secrets.get(name) for name in names}
    missing = [k for k, v in out.items() if not v]
    if missing:
        raise RuntimeError('missing required secret names: ' + ', '.join(missing))
    return out  # type: ignore[return-value]


def normalize_store(store: str) -> str:
    store = store.strip().replace('https://', '').replace('http://', '').strip('/')
    return store


def gql(store: str, token: str, query: str, variables: dict[str, Any]) -> dict[str, Any]:
    url = f'https://{store}/admin/api/{API_VERSION}/graphql.json'
    body = json.dumps({'query': query, 'variables': variables}).encode()
    req = urllib.request.Request(url, data=body, method='POST')
    req.add_header('X-Shopify-Access-Token', token)
    req.add_header('Content-Type', 'application/json')
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            payload = json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        text = e.read().decode(errors='replace')[:500]
        raise RuntimeError(f'shopify_http_error_{e.code}: {text}') from e
    if payload.get('errors'):
        raise RuntimeError('shopify_graphql_errors: ' + json.dumps(payload['errors'], ensure_ascii=False)[:800])
    return payload


def handle_from_url(url: str) -> str:
    return url.rstrip('/').split('/')[-1]


PRODUCT_QUERY = '''
query ProductByHandle($handle: String!) {
  productByHandle(handle: $handle) {
    id
    handle
    title
    seo { title description }
  }
}
'''

COLLECTION_QUERY = '''
query CollectionByHandle($handle: String!) {
  collectionByHandle(handle: $handle) {
    id
    handle
    title
    descriptionHtml
    seo { title description }
  }
}
'''

PRODUCT_UPDATE = '''
mutation ProductSeoUpdate($input: ProductInput!) {
  productUpdate(input: $input) {
    product { id handle title seo { title description } }
    userErrors { field message }
  }
}
'''

COLLECTION_UPDATE = '''
mutation CollectionSeoUpdate($input: CollectionInput!) {
  collectionUpdate(input: $input) {
    collection { id handle title seo { title description } }
    userErrors { field message }
  }
}
'''


def query_target(store: str, token: str, page_type: str, handle: str) -> dict[str, Any] | None:
    if page_type == 'pdp':
        data = gql(store, token, PRODUCT_QUERY, {'handle': handle})['data']['productByHandle']
    elif page_type == 'collection':
        data = gql(store, token, COLLECTION_QUERY, {'handle': handle})['data']['collectionByHandle']
    else:
        return None
    return data


def update_target(store: str, token: str, page_type: str, gid: str, title: str, description: str) -> dict[str, Any]:
    if page_type == 'pdp':
        payload = gql(store, token, PRODUCT_UPDATE, {'input': {'id': gid, 'seo': {'title': title, 'description': description}}})
        node = payload['data']['productUpdate']['product']
        errors = payload['data']['productUpdate']['userErrors']
    elif page_type == 'collection':
        payload = gql(store, token, COLLECTION_UPDATE, {'input': {'id': gid, 'seo': {'title': title, 'description': description}}})
        node = payload['data']['collectionUpdate']['collection']
        errors = payload['data']['collectionUpdate']['userErrors']
    else:
        return {'node': None, 'userErrors': [{'message': f'unsupported page_type {page_type}'}]}
    return {'node': node, 'userErrors': errors}


def run() -> dict[str, Any]:
    src = json.loads(SOURCE.read_text())
    secrets = doppler_secrets(['SHOPIFY_STORE_URL', 'SHOPIFY_ACCESS_TOKEN'])
    store = normalize_store(secrets['SHOPIFY_STORE_URL'])
    token = secrets['SHOPIFY_ACCESS_TOKEN']
    records = []
    for p in src['packets']:
        handle = handle_from_url(p['url'])
        target_title = p['proposed_title']
        target_desc = p['proposed_meta']
        record: dict[str, Any] = {
            'rank': p['rank'],
            'url': p['url'],
            'page_type': p['page_type'],
            'handle': handle,
            'target': {'seo_title': target_title, 'seo_description': target_desc},
            'approved_scope': 'seo_title_meta_only',
            'write_allowed_by_user_approval': True,
            'visible_changes_applied': False,
        }
        try:
            before = query_target(store, token, p['page_type'], handle)
            if not before:
                record.update({'status': 'skipped', 'reason': 'target_not_found', 'verified_live': False})
                records.append(record)
                continue
            record['shopify_id'] = before['id']
            record['backup'] = {
                'title': before.get('title'),
                'seo_title': (before.get('seo') or {}).get('title'),
                'seo_description': (before.get('seo') or {}).get('description'),
            }
            changed = record['backup']['seo_title'] != target_title or record['backup']['seo_description'] != target_desc
            mutation = update_target(store, token, p['page_type'], before['id'], target_title, target_desc)
            if mutation.get('userErrors'):
                record.update({'status': 'failed', 'reason': 'user_errors', 'userErrors': mutation['userErrors'], 'verified_live': False})
                records.append(record)
                continue
            time.sleep(0.25)
            after = query_target(store, token, p['page_type'], handle)
            after_seo = (after or {}).get('seo') or {}
            verified = after_seo.get('title') == target_title and after_seo.get('description') == target_desc
            record.update({
                'status': 'executed_verified' if verified else 'executed_not_verified',
                'changed_from_backup': changed,
                'after': {
                    'title': (after or {}).get('title'),
                    'seo_title': after_seo.get('title'),
                    'seo_description': after_seo.get('description'),
                },
                'verified_live': verified,
            })
        except Exception as e:
            record.update({'status': 'failed', 'reason': type(e).__name__, 'message': str(e)[:500], 'verified_live': False})
        records.append(record)
    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'approved LK P1 Shopify SEO title/meta execution',
        'approval_text': 'Lucas: Aprovada as melhorias, seguir',
        'source': str(SOURCE.relative_to(ROOT)),
        'summary': {
            'packets_in_source': len(src['packets']),
            'attempted': len(records),
            'executed_verified': sum(1 for r in records if r['status'] == 'executed_verified'),
            'failed': sum(1 for r in records if r['status'] == 'failed'),
            'skipped': sum(1 for r in records if r['status'] == 'skipped'),
            'visible_changes_applied': 0,
            'non_seo_writes': 0,
        },
        'records': records,
        'rollback_instructions': [
            'Use each record.backup.seo_title and record.backup.seo_description with the same productUpdate/collectionUpdate mutation to restore previous SEO fields.',
            'Rollback should be limited to records with status executed_verified or executed_not_verified.',
            'Do not touch H1/body/theme/price/stock/SKU/images/campaigns during rollback.',
        ],
        'not_performed': [
            'visible_h1_update', 'pdp_body_update', 'collection_description_update', 'theme_or_liquid_write',
            'price_update', 'stock_update', 'sku_update', 'variant_update', 'image_update',
            'merchant_center_write', 'feed_update', 'gsc_admin_change', 'indexing_api_submit',
            'content_publish', 'campaign_or_customer_send', 'cron_creation'
        ],
    }
    return payload


def md(payload: dict[str, Any]) -> str:
    s = payload['summary']
    lines = [
        '# LK Approved P1 SEO Fields Execution, 2026-05-11', '',
        f"Generated at: `{payload['generated_at']}`", '',
        '## Veredito', '',
        'Apliquei somente os SEO fields aprovados, title/meta, nos 8 pacotes P1. Mudanças visíveis de CRO continuam apenas como preview.', '',
        '## Snapshot', '',
        f"- Pacotes na origem: {s['packets_in_source']}",
        f"- Tentativas: {s['attempted']}",
        f"- Executados e verificados live: {s['executed_verified']}",
        f"- Falhas: {s['failed']}",
        f"- Pulados: {s['skipped']}",
        f"- Mudanças visíveis aplicadas: {s['visible_changes_applied']}",
        f"- Writes não-SEO: {s['non_seo_writes']}", '',
        '## Registros', '',
    ]
    for r in payload['records']:
        lines.extend([
            f"### {r['rank']}. {r['page_type']} · {r['handle']}", '',
            f"- URL: {r['url']}",
            f"- Status: `{r['status']}`",
            f"- Verificado live: {r.get('verified_live')}",
            f"- Title SEO aplicado: {r['target']['seo_title']}",
            f"- Meta SEO aplicada: {r['target']['seo_description']}",
            f"- Backup title SEO anterior: {r.get('backup', {}).get('seo_title')}",
            f"- Backup meta SEO anterior: {r.get('backup', {}).get('seo_description')}",
            ''
        ])
        if r['status'] == 'failed':
            lines.extend([f"- Motivo: {r.get('reason')}: {r.get('message') or r.get('userErrors')}", ''])
    lines.extend(['## Rollback', ''])
    for item in payload['rollback_instructions']:
        lines.append(f'- {item}')
    lines.extend(['', '## O que não foi feito', ''])
    for n in payload['not_performed']:
        lines.append(f'- {n}')
    return '\n'.join(lines) + '\n'


def main() -> None:
    payload = run()
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    text = md(payload)
    OUT_MD.write_text(text, encoding='utf-8')
    BRAIN_DOC.write_text(text, encoding='utf-8')
    print(json.dumps({'ok': payload['summary']['failed'] == 0, 'summary': payload['summary']}, ensure_ascii=False))
    if payload['summary']['failed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
