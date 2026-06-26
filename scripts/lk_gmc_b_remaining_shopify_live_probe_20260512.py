#!/usr/bin/env python3
"""Read-only Shopify live probe for LK GMC B rows whose link variant was missing in local Data Spine.

No writes. Uses Shopify Admin GraphQL query only to check whether Merchant link
variant IDs still exist in Shopify and have active-product SKUs.
"""
from __future__ import annotations

import csv
import importlib.util
import json
import os
import pathlib
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / 'scripts/lk_gmc_catalog_duplication_audit_20260512.py'
RECON_CSV = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_reconciliation/lk-gmc-2026-05-12-post-ab-b-remaining-reconciliation-review.csv')
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_reconciliation')
RUN_STAMP = '2026-05-12-b-remaining-shopify-live-probe'
PRIVATE_CSV = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}.csv'
OUT_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
OUT_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'

QUERY = '''query VariantNodes($ids: [ID!]!) {
  nodes(ids: $ids) {
    __typename
    ... on ProductVariant {
      id
      legacyResourceId
      sku
      title
      product { id legacyResourceId title handle status }
    }
  }
}'''


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def import_audit():
    spec = importlib.util.spec_from_file_location('lk_gmc_catalog_duplication_audit', AUDIT_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def shop_host(raw: str) -> str:
    host = (raw or '').strip().replace('https://', '').replace('http://', '').strip('/')
    return host


def gql(host: str, token: str, variables: dict[str, Any]) -> dict[str, Any]:
    url = f'https://{host}/admin/api/2024-01/graphql.json'
    body = json.dumps({'query': QUERY, 'variables': variables}).encode('utf-8')
    req = urllib.request.Request(url, data=body, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-Shopify-Access-Token', token)
    with urllib.request.urlopen(req, timeout=120) as r:
        data = json.loads(r.read().decode())
    if data.get('errors'):
        raise RuntimeError(json.dumps(data['errors'])[:1000])
    return data


def chunks(xs: list[str], n: int) -> list[list[str]]:
    return [xs[i:i+n] for i in range(0, len(xs), n)]


def main() -> None:
    audit = import_audit()
    secrets = audit.load_doppler()
    host = shop_host(secrets.get('SHOPIFY_STORE_URL') or '')
    token = secrets.get('SHOPIFY_ACCESS_TOKEN') or ''
    if not host or not token:
        raise RuntimeError('missing_shopify_secret')

    rows = list(csv.DictReader(RECON_CSV.open(encoding='utf-8')))
    target = [r for r in rows if r.get('state_after_ab') == 'old_present_no_strict_target' and r.get('variant_from_link')]
    unique_variants = sorted({r['variant_from_link'] for r in target if r.get('variant_from_link')})

    found_by_legacy: dict[str, dict[str, Any]] = {}
    for batch in chunks(unique_variants, 100):
        ids = [f'gid://shopify/ProductVariant/{x}' for x in batch]
        data = gql(host, token, {'ids': ids})
        for requested, node in zip(batch, data.get('data', {}).get('nodes', [])):
            if node:
                found_by_legacy[requested] = node

    out_rows = []
    for r in target:
        vid = r.get('variant_from_link') or ''
        node = found_by_legacy.get(vid)
        if not node:
            state = 'shopify_variant_not_found_live'
            sku = ''
            product_status = ''
            product_title = ''
        else:
            sku = node.get('sku') or ''
            product = node.get('product') or {}
            product_status = product.get('status') or ''
            product_title = product.get('title') or ''
            if product_status == 'ACTIVE' and sku:
                state = 'shopify_live_active_variant_with_sku_review_candidate'
            elif product_status == 'ACTIVE' and not sku:
                state = 'shopify_live_active_variant_without_sku'
            else:
                state = 'shopify_live_variant_product_not_active'
        out_rows.append({
            'old_product_id': r.get('old_product_id'),
            'old_offer_id': r.get('old_offer_id'),
            'merchant_title': r.get('title'),
            'variant_from_link': vid,
            'shopify_probe_state': state,
            'shopify_sku': sku,
            'shopify_product_status': product_status,
            'shopify_product_title': product_title,
        })

    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE_DIR, 0o700)
    fields = ['old_product_id','old_offer_id','merchant_title','variant_from_link','shopify_probe_state','shopify_sku','shopify_product_status','shopify_product_title']
    with PRIVATE_CSV.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(out_rows)
    os.chmod(PRIVATE_CSV, 0o600)

    counts = Counter(r['shopify_probe_state'] for r in out_rows)
    candidate_rows = [r for r in out_rows if r['shopify_probe_state'] == 'shopify_live_active_variant_with_sku_review_candidate']
    payload = {
        'generated_at': utc_now(),
        'status': 'gmc_b_remaining_shopify_live_probe_readonly',
        'scope': 'Read-only Shopify live variant probe for package B remaining rows',
        'source_labels': ['fact_shopify', 'fact_merchant_center', 'derived_reconciliation'],
        'input_rows_with_link_variant': len(target),
        'unique_variant_ids_queried': len(unique_variants),
        'state_counts': dict(counts),
        'review_candidate_count': len(candidate_rows),
        'private_csv': str(PRIVATE_CSV),
        'not_touched': ['merchant_product_write_or_delete','shopify_write','feed','database','campaign_or_external_send','local_channel','pos_inventory'],
        'interpretation': 'Shopify live active variant with SKU is stronger evidence, but still needs a write-preview package with exact old/new product IDs and rollback before any Merchant identifier change.'
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    lines = [
        '# LK GMC B Remaining Shopify Live Probe, 2026-05-12', '',
        f"Status: `{payload['status']}`", '',
        '## Resumo executivo',
        f"- Linhas B restantes com variant no link: {len(target)}",
        f"- Variant IDs únicos consultados no Shopify live: {len(unique_variants)}",
        f"- Review candidates com variant ativo + SKU no Shopify live: {len(candidate_rows)}",
        '',
        '## Estados encontrados',
    ]
    for k, v in counts.most_common():
        lines.append(f'- {k}: {v}')
    lines.extend([
        '',
        '## Veredito',
        '- A causa provável dos 840 `link_variant_not_found_active` é drift/defasagem do Data Spine local contra Shopify live, não necessariamente ausência real no Shopify.',
        '- Estes candidatos ainda não foram escritos no Merchant. O próximo passo seguro é montar um novo pacote preview com old/new product IDs exatos e rollback.',
        f'- CSV privado: `{PRIVATE_CSV}`',
        '',
        '## Não tocado',
    ])
    for item in payload['not_touched']:
        lines.append(f'- {item}')
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(OUT_MD.read_text(encoding='utf-8'), encoding='utf-8')
    print(json.dumps({
        'status': payload['status'],
        'state_counts': dict(counts),
        'review_candidate_count': len(candidate_rows),
        'private_csv': str(PRIVATE_CSV),
        'public_report': str(OUT_MD),
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
