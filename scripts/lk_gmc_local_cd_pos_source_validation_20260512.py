#!/usr/bin/env python3
"""Read-only POS/source validation for LK GMC local C/D residual rows.

Consumes the 63 residual local C/D rows that have no Shopify-live exact SKU and
no Tiny exact codigo, then validates by Shopify live product title and current
Merchant local replacement presence. This is an investigation/approval-packet
prep only: no Merchant, Shopify, Tiny, POS, feed, DB, campaign or external writes.
"""
from __future__ import annotations

import csv
import importlib.util
import json
import os
import pathlib
import re
import unicodedata
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / 'scripts/lk_gmc_catalog_duplication_audit_20260512.py'
INPUT_CSV = ROOT / 'reports/lk-gmc-2026-05-12-local-cd-residual-tiny-probe.csv'
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_reconciliation')
ROLLBACK_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
RUN_STAMP = '2026-05-12-local-cd-pos-source-validation'
PRIVATE_CSV = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}.csv'
ROLLBACK_JSON = ROLLBACK_DIR / f'lk-gmc-{RUN_STAMP}-rollback-snapshot.json'
OUT_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
OUT_CSV = ROOT / f'reports/lk-gmc-{RUN_STAMP}.csv'
OUT_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
CONTROL = ROOT / 'areas/lk/projetos/lk-os-implementation-control.md'
INDEX = ROOT / 'empresa/rotinas/_index.md'

QUERY = '''query ProductsByTitle($q: String!) {
  products(first: 10, query: $q) {
    edges {
      node {
        id
        legacyResourceId
        title
        handle
        status
        vendor
        productType
        variants(first: 100) {
          edges {
            node { id legacyResourceId sku title barcode inventoryQuantity }
          }
        }
      }
    }
  }
}'''


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def import_audit():
    spec = importlib.util.spec_from_file_location('audit', AUDIT_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def shop_host(raw: str) -> str:
    return (raw or '').strip().replace('https://', '').replace('http://', '').strip('/')


def norm_text(s: str | None) -> str:
    raw = unicodedata.normalize('NFKD', s or '').encode('ascii', 'ignore').decode('ascii')
    return re.sub(r'\s+', ' ', re.sub(r'[^a-zA-Z0-9]+', ' ', raw).strip().lower())


def gql_products(host: str, token: str, title: str) -> list[dict[str, Any]]:
    q = 'title:"' + title.replace('\\', '\\\\').replace('"', '\\"') + '"'
    req = urllib.request.Request(f'https://{host}/admin/api/2024-01/graphql.json', data=json.dumps({'query': QUERY, 'variables': {'q': q}}).encode('utf-8'), method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-Shopify-Access-Token', token)
    with urllib.request.urlopen(req, timeout=120) as r:
        data = json.loads(r.read().decode())
    if data.get('errors'):
        raise RuntimeError(json.dumps(data['errors'])[:1000])
    return [edge['node'] for edge in data.get('data', {}).get('products', {}).get('edges', [])]


def public_row(row: dict[str, Any]) -> dict[str, Any]:
    return {
        'package': row['package'],
        'decision_state': row['decision_state'],
        'product_id': row['product_id'],
        'old_offer_id': row['offer_id'],
        'old_normalized_sku': row['normalized_sku'],
        'merchant_title': row['merchant_title'],
        'shopify_title_match_status': row['shopify_title_match_status'],
        'shopify_product_title': row['shopify_product_title'],
        'shopify_product_handle': row['shopify_product_handle'],
        'shopify_current_skus_sample': ';'.join(row['shopify_current_skus'][:12]),
        'shopify_total_inventory_quantity': row['shopify_total_inventory_quantity'],
        'replacement_local_product_ids_sample': ';'.join(row['replacement_local_product_ids'][:12]),
        'replacement_local_present_count': row['replacement_local_present_count'],
        'merchant_destination_problem': row['merchant_destination_problem'],
        'merchant_item_issue_count': row['merchant_item_issue_count'],
        'recommended_next_action': row['recommended_next_action'],
    }


def main() -> None:
    residual = list(csv.DictReader(INPUT_CSV.open(encoding='utf-8')))
    audit = import_audit()
    secrets = audit.load_doppler()
    merchant_id = secrets.get('MERCHANT_CENTER_ID_LK')
    host = shop_host(secrets.get('SHOPIFY_STORE_URL') or '')
    shopify_token = secrets.get('SHOPIFY_ACCESS_TOKEN') or ''
    if not merchant_id or not host or not shopify_token:
        raise RuntimeError('missing_required_credentials')

    content_token = audit.google_access_token(audit.parse_service_account(secrets))
    products = audit.list_all('products', merchant_id, content_token)
    statuses = audit.list_all('productstatuses', merchant_id, content_token)
    product_by_id = {p.get('id'): p for p in products}
    status_by_id = {s.get('productId'): s for s in statuses}
    local_ids_by_offer = {p.get('offerId'): p.get('id') for p in products if p.get('channel') == 'local'}

    titles = sorted({r.get('merchant_title') or '' for r in residual if r.get('merchant_title')})
    shopify_by_title: dict[str, list[dict[str, Any]]] = {t: gql_products(host, shopify_token, t) for t in titles}

    out_rows: list[dict[str, Any]] = []
    for row in residual:
        title = row.get('merchant_title') or ''
        old_sku = row.get('normalized_sku') or ''
        old_pid = row.get('product_id') or ''
        matches = shopify_by_title.get(title, [])
        exact_title_matches = [p for p in matches if norm_text(p.get('title')) == norm_text(title)]
        active_exact = [p for p in exact_title_matches if p.get('status') == 'ACTIVE']
        chosen = active_exact[0] if active_exact else (exact_title_matches[0] if exact_title_matches else (matches[0] if matches else {}))
        variants = [(e.get('node') or {}) for e in ((chosen.get('variants') or {}).get('edges') or [])]
        current_skus = [str(v.get('sku') or '') for v in variants if v.get('sku')]
        replacement_local_ids = []
        for sku in current_skus:
            pid = local_ids_by_offer.get('LIA_' + sku)
            if pid and pid != old_pid and pid not in replacement_local_ids:
                replacement_local_ids.append(pid)
        total_inv = sum(int(v.get('inventoryQuantity') or 0) for v in variants if isinstance(v.get('inventoryQuantity'), int))
        st = status_by_id.get(old_pid) or {}
        has_dest_problem = any((d.get('status') or '') not in {'approved', 'pending'} for d in st.get('destinationStatuses') or [])
        issue_count = len(st.get('itemLevelIssues') or [])

        if active_exact and old_sku not in current_skus and replacement_local_ids:
            decision = 'old_lia_sku_replaced_by_active_shopify_product_with_replacement_local_present'
            action = 'eligible for residual approval packet as exact old local ID cleanup candidate after rollback snapshot; product/source has active replacement local rows'
        elif active_exact and old_sku not in current_skus:
            decision = 'old_lia_sku_not_current_but_active_product_exists_no_replacement_local_seen'
            action = 'do not delete yet; inspect source/POS app because active product exists but local replacement rows were not found'
        elif active_exact and old_sku in current_skus:
            decision = 'unexpected_current_sku_found_by_title_preserve'
            action = 'preserve; conflicts with earlier exact-SKU probe and needs classifier debugging'
        elif chosen:
            decision = 'shopify_title_found_not_active_or_not_exact_manual_review'
            action = 'manual review before any local cleanup; do not execute from this packet'
        else:
            decision = 'no_shopify_title_match_no_tiny_code_residual_cleanup_candidate_after_rollback'
            action = 'eligible for strict residual approval packet after rollback snapshot; no live Shopify/Tiny/source evidence found'

        out_rows.append({
            'package': row.get('package') or '',
            'product_id': old_pid,
            'offer_id': row.get('offer_id') or '',
            'normalized_sku': old_sku,
            'merchant_title': title,
            'decision_state': decision,
            'shopify_title_match_status': chosen.get('status') or '',
            'shopify_product_title': chosen.get('title') or '',
            'shopify_product_handle': chosen.get('handle') or '',
            'shopify_product_legacy_id': chosen.get('legacyResourceId') or '',
            'shopify_current_skus': current_skus,
            'shopify_total_inventory_quantity': total_inv,
            'replacement_local_product_ids': replacement_local_ids,
            'replacement_local_present_count': len(replacement_local_ids),
            'merchant_destination_problem': has_dest_problem,
            'merchant_item_issue_count': issue_count,
            'recommended_next_action': action,
        })

    counts = Counter(r['decision_state'] for r in out_rows)
    by_package: dict[str, Counter] = defaultdict(Counter)
    for r in out_rows:
        by_package[r['package']][r['decision_state']] += 1
    approval_candidates = [r for r in out_rows if r['decision_state'] in {
        'old_lia_sku_replaced_by_active_shopify_product_with_replacement_local_present',
        'no_shopify_title_match_no_tiny_code_residual_cleanup_candidate_after_rollback',
    }]
    blocked_review = [r for r in out_rows if r not in approval_candidates]

    PRIVATE_DIR.mkdir(parents=True, exist_ok=True); os.chmod(PRIVATE_DIR, 0o700)
    ROLLBACK_DIR.mkdir(parents=True, exist_ok=True); os.chmod(ROLLBACK_DIR, 0o700)
    fields = list(public_row(out_rows[0]).keys()) if out_rows else []
    for path in (PRIVATE_CSV, OUT_CSV):
        with path.open('w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            for r in out_rows:
                w.writerow(public_row(r))
    os.chmod(PRIVATE_CSV, 0o600)

    rollback_payload = {
        'generated_at': utc_now(),
        'scope': 'Private rollback/source snapshot for local C/D POS/source validation residual rows; no writes executed',
        'records': [
            {
                'product_id': r['product_id'],
                'merchant_product_resource': product_by_id.get(r['product_id']) or {},
                'merchant_product_status': status_by_id.get(r['product_id']) or {},
                'decision_state': r['decision_state'],
                'recommended_next_action': r['recommended_next_action'],
            }
            for r in out_rows
        ],
    }
    ROLLBACK_JSON.write_text(json.dumps(rollback_payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    os.chmod(ROLLBACK_JSON, 0o600)

    payload = {
        'generated_at': utc_now(),
        'status': 'gmc_local_cd_pos_source_validation_readonly',
        'scope': 'Read-only POS/source validation for 63 local C/D residual rows using Shopify live title/product and Merchant local replacement presence',
        'source_labels': ['fact_merchant_center', 'fact_shopify', 'fact_tiny_stock', 'derived_reconciliation', 'manual_approval_required'],
        'summary': {
            'input_residual_rows': len(residual),
            'unique_titles_checked_shopify_live': len(titles),
            'decision_state_counts': dict(counts),
            'decision_state_counts_by_package': {pkg: dict(cnt) for pkg, cnt in by_package.items()},
            'approval_candidate_rows_after_source_validation': len(approval_candidates),
            'blocked_manual_review_rows': len(blocked_review),
            'private_rollback_snapshot_path': str(ROLLBACK_JSON),
            'merchant_writes': 0,
            'shopify_writes': 0,
            'tiny_writes': 0,
            'pos_or_local_inventory_writes': 0,
            'database_writes': 0,
            'external_sends': 0,
        },
        'interpretation': {
            'recommended_policy': 'Do not execute automatically. This creates a smaller residual approval packet; execution would require Lucas approval for exact local product IDs and rollback plan.',
            'replacement_logic': 'If old LIA SKU is not current in active Shopify product and replacement LIA rows for current SKUs are already present, old local IDs are likely stale source remnants rather than active inventory.',
        },
        'samples': {
            'approval_candidates': [public_row(r) for r in approval_candidates[:25]],
            'blocked_manual_review': [public_row(r) for r in blocked_review[:25]],
        },
        'public_csv': str(OUT_CSV),
        'private_csv': str(PRIVATE_CSV),
        'not_performed': ['merchant_product_delete','merchant_product_update','content_api_custombatch','feed_update','shopify_write','tiny_write','database_write','local_inventory_disable','pos_inventory_write','campaign_or_external_send'],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    lines = [
        '# LK GMC Local C/D POS/Source Validation, 2026-05-12', '',
        f"Status: `{payload['status']}`", '',
        '## Resumo executivo',
        f"- Residuais locais avaliados: {len(residual)}",
        f"- Títulos únicos checados no Shopify live: {len(titles)}",
        f"- Estados: {dict(counts)}",
        f"- Candidatos para approval packet residual: {len(approval_candidates)}",
        f"- Bloqueados para revisão manual: {len(blocked_review)}",
        '- Merchant/Shopify/Tiny/POS/DB writes: 0', '',
        '## Veredito',
        '- O bloco POS/source reduziu a investigação a um pacote residual exato, mas não executa nada.',
        '- Candidatos só podem virar delete/update após aprovação explícita, por product ID exato, com rollback privado.',
        f"- Snapshot privado de rollback: `{ROLLBACK_JSON}`", '',
        '## Arquivos',
        f"- JSON público: `{OUT_JSON}`",
        f"- CSV público: `{OUT_CSV}`",
        f"- CSV privado/auditoria chmod 600: `{PRIVATE_CSV}`", '',
        '## Não executado',
    ]
    for item in payload['not_performed']:
        lines.append(f'- {item}')
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(OUT_MD.read_text(encoding='utf-8'), encoding='utf-8')

    if CONTROL.exists():
        marker = '### 2026-05-12 — GMC local C/D POS/source validation'
        text = CONTROL.read_text(encoding='utf-8')
        block = (
            f"\n{marker}\n\n"
            f"- Status: POS/source validation read-only concluída para {len(residual)} residuais locais.\n"
            f"- Estados: {dict(counts)}.\n"
            f"- Approval candidates residuais: {len(approval_candidates)}; bloqueados revisão: {len(blocked_review)}.\n"
            f"- Snapshot privado rollback/source salvo; nenhum write executado.\n"
        )
        if marker not in text:
            CONTROL.write_text(text.rstrip() + block + '\n', encoding='utf-8')
    if INDEX.exists():
        text = INDEX.read_text(encoding='utf-8')
        line = '| LK GMC Local C/D POS Source Validation 2026-05-12 | `areas/lk/rotinas/gmc-2026-05-12-local-cd-pos-source-validation.md` | Validação read-only POS/source dos 63 residuais locais C/D por Shopify live title/current SKUs e presença de replacement local, com rollback privado e sem writes |'
        if line not in text:
            INDEX.write_text(text.rstrip() + '\n' + line + '\n', encoding='utf-8')

    print(json.dumps({'status': payload['status'], 'summary': payload['summary'], 'public_report': str(OUT_MD)}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
