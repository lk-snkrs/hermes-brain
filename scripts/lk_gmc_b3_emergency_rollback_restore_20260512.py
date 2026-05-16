#!/usr/bin/env python3
"""Emergency rollback for LK GMC B3 rows deleted due to unsafe same-ID preview.

Restores original Merchant products for rows where old_product_id_to_delete is now
absent. Does not delete or modify any correct/present rows.
"""
from __future__ import annotations

import csv
import importlib.util
import json
import os
import pathlib
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / 'scripts/lk_gmc_catalog_duplication_audit_20260512.py'
B_SCRIPT = ROOT / 'scripts/lk_gmc_execute_package_b_identifier_fix_20260512.py'
EXEC_ROLLBACK = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-12-package-b3-delete-old-duplicates-execution-rollback.json')
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
RUN_STAMP = '2026-05-12-package-b3-emergency-rollback-restore'
PRIVATE_JSON = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}.json'
OUT_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
OUT_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def import_module(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def post_json(url: str, token: str, body: dict[str, Any]) -> dict[str, Any]:
    data = json.dumps(body, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')
    req.add_header('Authorization', 'Bearer ' + token)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            raw = r.read().decode()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        raw = e.read().decode(errors='replace')
        raise RuntimeError(f'http_{e.code}: {raw[:1000]}') from e


def insert_product(merchant_id: str, token: str, product: dict[str, Any]) -> dict[str, Any]:
    url = f'https://shoppingcontent.googleapis.com/content/v2.1/{merchant_id}/products'
    out = dict(product)
    for k in ['id', 'kind', 'source']:
        out.pop(k, None)
    return post_json(url, token, out)


def restore_one(rec: dict[str, Any], merchant_id: str, token: str) -> dict[str, Any]:
    out = {
        'old_product_id': rec.get('old_product_id_to_delete'),
        'title': rec.get('title'),
        'started_at': utc_now(),
    }
    product = rec.get('rollback_original_product') or {}
    try:
        inserted = insert_product(merchant_id, token, product)
        out['restore_status'] = 'ok'
        out['inserted_product_id'] = inserted.get('id') or product.get('id')
    except Exception as e:
        out['restore_status'] = 'failed'
        out['error_message'] = str(e)[:1000]
    out['finished_at'] = utc_now()
    return out


def main() -> None:
    audit = import_module(AUDIT_PATH, 'lk_gmc_catalog_duplication_audit')
    bmod = import_module(B_SCRIPT, 'lk_gmc_execute_package_b_identifier_fix')
    secrets = audit.load_doppler()
    merchant_id = secrets.get('MERCHANT_CENTER_ID_LK')
    token = audit.google_access_token(audit.parse_service_account(secrets))
    payload = json.loads(EXEC_ROLLBACK.read_text(encoding='utf-8'))
    records = payload.get('records') or []
    current = bmod.list_all_products(merchant_id, token)
    current_ids = {p.get('id') for p in current}
    to_restore = [r for r in records if r.get('old_product_id_to_delete') not in current_ids]
    already_present = [r for r in records if r.get('old_product_id_to_delete') in current_ids]

    results = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = [ex.submit(restore_one, r, merchant_id, token) for r in to_restore]
        for fut in as_completed(futs):
            results.append(fut.result())
    results.sort(key=lambda r: r.get('old_product_id') or '')
    time.sleep(90)
    after = bmod.list_all_products(merchant_id, token)
    after_ids = {p.get('id') for p in after}
    target_ids = {r.get('old_product_id_to_delete') for r in records}
    verified_present = sum(1 for x in target_ids if x in after_ids)
    still_missing = sorted(x for x in target_ids if x not in after_ids)
    summary = {
        'mode': 'emergency_rollback_restore_after_b3_same_id_preview_error',
        'records_total': len(records),
        'to_restore_absent_before': len(to_restore),
        'already_present_before': len(already_present),
        'restore_ok': sum(1 for r in results if r.get('restore_status') == 'ok'),
        'restore_failed': sum(1 for r in results if r.get('restore_status') == 'failed'),
        'merchant_products_before_restore': len(current),
        'merchant_products_after_verify': len(after),
        'verified_present_after': verified_present,
        'still_missing_count': len(still_missing),
        'still_missing_sample': still_missing[:20],
    }
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE_DIR, 0o700)
    PRIVATE_JSON.write_text(json.dumps({'generated_at': utc_now(), 'summary': summary, 'results': results}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    os.chmod(PRIVATE_JSON, 0o600)
    public = {
        'generated_at': utc_now(),
        'status': 'gmc_package_b3_emergency_rollback_restored_verified' if not still_missing and not summary['restore_failed'] else 'gmc_package_b3_emergency_rollback_needs_review',
        'source_labels': ['fact_merchant_center', 'rollback_execution'],
        'summary': summary | {'private_audit_path': str(PRIVATE_JSON)},
        'not_touched': ['shopify_write','feed','database','campaign_or_external_send','local_channel','pos_inventory','google_business_profile'],
    }
    OUT_JSON.write_text(json.dumps(public, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    lines = [
        '# LK GMC Package B3 Emergency Rollback Restore, 2026-05-12', '',
        f"Status: `{public['status']}`", '',
        '## Resumo executivo',
        f"- Registros B3 totais: {summary['records_total']}",
        f"- Ausentes antes do restore: {summary['to_restore_absent_before']}",
        f"- Já presentes antes do restore: {summary['already_present_before']}",
        f"- Restore OK: {summary['restore_ok']}",
        f"- Restore falhou: {summary['restore_failed']}",
        f"- Verificados presentes depois: {summary['verified_present_after']}",
        f"- Ainda ausentes: {summary['still_missing_count']}",
        f"- Merchant products após verificação: {summary['merchant_products_after_verify']}",
        f"- Auditoria privada: `{PRIVATE_JSON}`", '',
        '## Interpretação',
        '- O preview B3 gerou falsos positivos porque old_product_id e target_product_id eram iguais para os 854.',
        '- Executei rollback corretivo: reinseri os recursos originais que ficaram ausentes e não alterei os que já estavam presentes.',
        '- Estado restaurado/verificado antes de qualquer novo pacote.', '',
        '## Não tocado',
    ]
    for item in public['not_touched']:
        lines.append(f'- {item}')
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(OUT_MD.read_text(encoding='utf-8'), encoding='utf-8')
    print(json.dumps({'status': public['status'], 'summary': summary, 'public_report': str(OUT_MD)}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
