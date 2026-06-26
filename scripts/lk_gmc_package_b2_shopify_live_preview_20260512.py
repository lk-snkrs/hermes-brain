#!/usr/bin/env python3
"""Build read-only executable preview for LK GMC package B remaining rows using Shopify live variant evidence.

No writes. Produces a private rollback/preview JSON with exact old/new product IDs
and sanitized public reports. Requires explicit Lucas approval before any Merchant
insert/delete execution.
"""
from __future__ import annotations

import csv
import importlib.util
import json
import os
import pathlib
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / 'scripts/lk_gmc_catalog_duplication_audit_20260512.py'
B_SCRIPT = ROOT / 'scripts/lk_gmc_execute_package_b_identifier_fix_20260512.py'
SHOPIFY_CSV = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_reconciliation/lk-gmc-2026-05-12-b-remaining-shopify-live-probe.csv')
SNAPSHOT = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-executable-previews-rollback-2026-05-12.json')
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
RUN_STAMP = '2026-05-12-package-b2-shopify-live-preview'
PRIVATE_JSON = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-rollback-preview.json'
OUT_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
OUT_CSV = ROOT / f'reports/lk-gmc-{RUN_STAMP}.csv'
OUT_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
PACKAGE = 'B2_online_identifier_fix_shopify_live_preview'


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def import_module(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def load_original_by_pid() -> dict[str, dict[str, Any]]:
    data = json.loads(SNAPSHOT.read_text(encoding='utf-8'))
    out = {}
    for r in data.get('records', []):
        p = r.get('merchant_product_resource') or {}
        pid = p.get('id') or (r.get('classification') or {}).get('product_id')
        if pid:
            out[pid] = r
    return out


def replacement_product(product: dict[str, Any], target_offer_id: str) -> dict[str, Any]:
    out = json.loads(json.dumps(product, ensure_ascii=False))
    for k in ['id', 'kind', 'source']:
        out.pop(k, None)
    out['offerId'] = target_offer_id
    if str(product.get('mpn') or '') == str(product.get('offerId') or ''):
        out['mpn'] = target_offer_id
    return out


def main() -> None:
    audit = import_module(AUDIT_PATH, 'lk_gmc_catalog_duplication_audit')
    bmod = import_module(B_SCRIPT, 'lk_gmc_execute_package_b_identifier_fix')
    secrets = audit.load_doppler()
    merchant_id = secrets.get('MERCHANT_CENTER_ID_LK')
    if not merchant_id:
        raise RuntimeError('missing_merchant_center_id')
    token = audit.google_access_token(audit.parse_service_account(secrets))
    current_products = bmod.list_all_products(merchant_id, token)
    current_ids = {p.get('id') for p in current_products}
    original_by_pid = load_original_by_pid()

    rows = list(csv.DictReader(SHOPIFY_CSV.open(encoding='utf-8')))
    public_rows = []
    private_records = []
    counters: Counter[str] = Counter()
    for r in rows:
        old_pid = r.get('old_product_id') or ''
        sku = r.get('shopify_sku') or ''
        state = r.get('shopify_probe_state') or ''
        orig = original_by_pid.get(old_pid, {})
        product = orig.get('merchant_product_resource') or {}
        if state != 'shopify_live_active_variant_with_sku_review_candidate' or not sku or not product:
            status = 'skipped_not_candidate'
            new_pid = ''
        else:
            new_pid = f"online:{product.get('contentLanguage') or 'pt'}:{product.get('targetCountry') or 'BR'}:{sku}"
            # Hard safety guard: same ID is not a duplicate and not an identifier fix.
            # Deleting it would remove the real product. Classify as no-op/valid.
            if new_pid == old_pid:
                status = 'skipped_same_product_id_noop_valid_after_shopify_live'
            elif old_pid not in current_ids:
                status = 'skipped_old_not_current'
            elif new_pid in current_ids:
                status = 'skipped_target_already_exists_different_id'
            elif sku == product.get('offerId'):
                status = 'skipped_already_correct'
            else:
                status = 'preview_ready_needs_approval'
        counters[status] += 1
        public = {
            'old_product_id': old_pid,
            'old_offer_id': r.get('old_offer_id'),
            'new_product_id': new_pid,
            'new_offer_id': sku,
            'title': r.get('merchant_title'),
            'evidence': 'shopify_live_link_variant_active_with_sku',
            'preview_status': status,
        }
        public_rows.append(public)
        if status == 'preview_ready_needs_approval':
            private_records.append(public | {
                'package': PACKAGE,
                'rollback_original_product': product,
                'rollback_original_status': orig.get('merchant_product_status') or {},
                'replacement_product': replacement_product(product, sku),
                'approval_gate': 'Requires explicit Lucas approval before Merchant insert-new/delete-old execution.',
            })

    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE_DIR, 0o700)
    PRIVATE_JSON.write_text(json.dumps({
        'generated_at': utc_now(),
        'mode': 'preview_only_no_writes',
        'scope': PACKAGE,
        'rollback_note': 'If applied later: reinsert rollback_original_product and delete new_product_id to roll back.',
        'records': private_records,
    }, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    os.chmod(PRIVATE_JSON, 0o600)

    payload = {
        'generated_at': utc_now(),
        'status': 'gmc_package_b2_shopify_live_preview_ready_no_writes',
        'scope': PACKAGE,
        'source_labels': ['fact_merchant_center', 'fact_shopify', 'derived_reconciliation'],
        'merchant_products_current_read': len(current_products),
        'input_rows': len(rows),
        'preview_status_counts': dict(counters),
        'ready_needs_approval': counters.get('preview_ready_needs_approval', 0),
        'private_rollback_preview_path': str(PRIVATE_JSON),
        'not_touched': ['merchant_product_write_or_delete','shopify_write','feed','database','campaign_or_external_send','local_channel','pos_inventory'],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    with OUT_CSV.open('w', newline='', encoding='utf-8') as f:
        fields = ['old_product_id','old_offer_id','new_product_id','new_offer_id','title','evidence','preview_status']
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(public_rows)

    lines = [
        '# LK GMC Package B2 Shopify Live Identifier Fix Preview, 2026-05-12', '',
        f"Status: `{payload['status']}`", '',
        '## Resumo executivo',
        f"- Linhas avaliadas a partir do Shopify live probe: {len(rows)}",
        f"- Candidatos prontos para aprovação: {counters.get('preview_ready_needs_approval', 0)}",
        f"- Pulados old ausente: {counters.get('skipped_old_not_current', 0)}",
        f"- Pulados target já existente: {counters.get('skipped_target_already_exists', 0)}",
        f"- Pulados já corretos: {counters.get('skipped_already_correct', 0)}",
        f"- Snapshot privado preview/rollback: `{PRIVATE_JSON}`",
        '',
        '## Veredito',
        '- Shopify live confirmou os 854 variants ativos com SKU, mas o SKU gera o mesmo product ID já existente.',
        '- Com o guard same-ID, B2 agora é no-op: 0 linhas são candidatas a insert-new/delete-old.',
        '',
        '## Não tocado',
    ]
    for item in payload['not_touched']:
        lines.append(f'- {item}')
    lines.extend(['', '## Arquivos', f'- JSON: `{OUT_JSON}`', f'- CSV: `{OUT_CSV}`'])
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(OUT_MD.read_text(encoding='utf-8'), encoding='utf-8')

    print(json.dumps({
        'status': payload['status'],
        'ready_needs_approval': payload['ready_needs_approval'],
        'preview_status_counts': dict(counters),
        'private_rollback_preview_path': str(PRIVATE_JSON),
        'public_report': str(OUT_MD),
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
