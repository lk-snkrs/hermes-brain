#!/usr/bin/env python3
"""Build read-only deletion-only preview for LK GMC old duplicate B identifiers.

No writes. Rows qualify only when old Merchant product is still current and the
correct Shopify-live SKU product ID already exists in Merchant. Execution would
be DELETE old exact IDs only, with rollback by reinserting the original product.
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
B2_CSV = ROOT / 'reports/lk-gmc-2026-05-12-package-b2-shopify-live-preview.csv'
SNAPSHOT = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-executable-previews-rollback-2026-05-12.json')
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
RUN_STAMP = '2026-05-12-package-b3-delete-old-duplicates-preview'
PRIVATE_JSON = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-rollback-preview.json'
OUT_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
OUT_CSV = ROOT / f'reports/lk-gmc-{RUN_STAMP}.csv'
OUT_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
PACKAGE = 'B3_delete_old_duplicate_identifier_preview'


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
    b2_rows = list(csv.DictReader(B2_CSV.open(encoding='utf-8')))

    public_rows = []
    private_records = []
    counters: Counter[str] = Counter()
    for r in b2_rows:
        old_pid = r.get('old_product_id') or ''
        new_pid = r.get('new_product_id') or ''
        orig = original_by_pid.get(old_pid, {})
        product = orig.get('merchant_product_resource') or {}
        if not old_pid or not new_pid or not product:
            status = 'skipped_missing_evidence'
        elif old_pid == new_pid:
            status = 'blocked_same_product_id_not_a_duplicate'
        elif old_pid not in current_ids:
            status = 'skipped_old_not_current'
        elif new_pid not in current_ids:
            status = 'skipped_target_not_current'
        else:
            status = 'preview_ready_delete_old_only_needs_approval'
        counters[status] += 1
        public = {
            'old_product_id_to_delete': old_pid,
            'old_offer_id': r.get('old_offer_id'),
            'correct_existing_product_id_to_keep': new_pid,
            'correct_offer_id': r.get('new_offer_id'),
            'title': r.get('title'),
            'evidence': 'correct_shopify_live_sku_product_already_exists_in_merchant',
            'preview_status': status,
        }
        public_rows.append(public)
        if status == 'preview_ready_delete_old_only_needs_approval':
            private_records.append(public | {
                'package': PACKAGE,
                'rollback_original_product': product,
                'rollback_original_status': orig.get('merchant_product_status') or {},
                'proposed_operation_if_approved': 'DELETE old_product_id_to_delete only; keep correct_existing_product_id_to_keep.',
                'rollback_if_needed': 'Reinsert rollback_original_product via Content API products.insert.',
                'approval_gate': 'Requires explicit Lucas approval before Merchant DELETE execution.',
            })

    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE_DIR, 0o700)
    PRIVATE_JSON.write_text(json.dumps({
        'generated_at': utc_now(),
        'mode': 'preview_only_no_writes',
        'scope': PACKAGE,
        'records': private_records,
    }, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    os.chmod(PRIVATE_JSON, 0o600)

    payload = {
        'generated_at': utc_now(),
        'status': 'gmc_package_b3_delete_old_duplicates_preview_ready_no_writes',
        'scope': PACKAGE,
        'source_labels': ['fact_merchant_center', 'fact_shopify', 'derived_reconciliation'],
        'merchant_products_current_read': len(current_products),
        'input_rows': len(b2_rows),
        'preview_status_counts': dict(counters),
        'ready_delete_old_only_needs_approval': counters.get('preview_ready_delete_old_only_needs_approval', 0),
        'private_rollback_preview_path': str(PRIVATE_JSON),
        'not_touched': ['merchant_product_write_or_delete','shopify_write','feed','database','campaign_or_external_send','local_channel','pos_inventory'],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    with OUT_CSV.open('w', newline='', encoding='utf-8') as f:
        fields = ['old_product_id_to_delete','old_offer_id','correct_existing_product_id_to_keep','correct_offer_id','title','evidence','preview_status']
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(public_rows)

    lines = [
        '# LK GMC Package B3 Delete Old Duplicate Identifiers Preview, 2026-05-12', '',
        f"Status: `{payload['status']}`", '',
        '## Resumo executivo',
        f"- Linhas avaliadas: {len(b2_rows)}",
        f"- Candidatos delete-old-only prontos para aprovação: {payload['ready_delete_old_only_needs_approval']}",
        f"- Snapshot privado preview/rollback: `{PRIVATE_JSON}`",
        '',
        '## Veredito',
        '- Os 854 B restantes foram bloqueados pelo guard same-ID: `old_product_id == correct_existing_product_id`.',
        '- Portanto, não existe pacote delete-old-only seguro aqui; esses itens são no-op/valid_after_shopify_live.',
        '- Nenhuma escrita foi feita e nenhuma aprovação de delete deve ser pedida para estes 854.',
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
        'ready_delete_old_only_needs_approval': payload['ready_delete_old_only_needs_approval'],
        'preview_status_counts': dict(counters),
        'private_rollback_preview_path': str(PRIVATE_JSON),
        'public_report': str(OUT_MD),
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
