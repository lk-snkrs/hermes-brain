#!/usr/bin/env python3
"""Execute approved LK GMC B3 delete-old-only duplicate identifier cleanup.

Approved by Lucas: delete 854 old duplicate Merchant product IDs while keeping
correct existing product IDs. Creates private rollback snapshot and public
sanitized reports. Does not touch Shopify, feeds, DB, local inventory, campaigns.
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import os
import pathlib
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / 'scripts/lk_gmc_catalog_duplication_audit_20260512.py'
B_SCRIPT = ROOT / 'scripts/lk_gmc_execute_package_b_identifier_fix_20260512.py'
PREVIEW_JSON = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-12-package-b3-delete-old-duplicates-preview-rollback-preview.json')
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
RUN_STAMP = '2026-05-12-package-b3-delete-old-duplicates-execution'
PRIVATE_JSON = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-rollback.json'
OUT_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
OUT_CSV = ROOT / f'reports/lk-gmc-{RUN_STAMP}.csv'
OUT_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
CONTROL = ROOT / 'areas/lk/projetos/lk-os-implementation-control.md'
INDEX = ROOT / 'empresa/rotinas/_index.md'
PACKAGE = 'B3_delete_old_duplicate_identifier_execution'


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def import_module(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def send_json(url: str, token: str, method: str) -> dict[str, Any]:
    req = urllib.request.Request(url, method=method)
    req.add_header('Authorization', 'Bearer ' + token)
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            raw = r.read().decode()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        raw = e.read().decode(errors='replace')
        if method == 'DELETE' and e.code == 404:
            return {'status': 'not_found_idempotent'}
        raise RuntimeError(f'http_{e.code}: {raw[:800]}') from e


def delete_product(merchant_id: str, product_id: str, token: str) -> dict[str, Any]:
    pid = urllib.parse.quote(product_id, safe='')
    url = f'https://shoppingcontent.googleapis.com/content/v2.1/{merchant_id}/products/{pid}'
    return send_json(url, token, 'DELETE')


def load_preview_records() -> list[dict[str, Any]]:
    payload = json.loads(PREVIEW_JSON.read_text(encoding='utf-8'))
    return payload.get('records') or []


def execute_one(rec: dict[str, Any], merchant_id: str, token: str) -> dict[str, Any]:
    out = dict(rec)
    old_pid = rec.get('old_product_id_to_delete')
    started = utc_now()
    try:
        delete_product(merchant_id, old_pid, token)
        out['delete_status'] = 'ok_or_already_absent'
        out['execution_status'] = 'applied_delete_old_only_keep_correct_existing'
    except Exception as e:
        out['delete_status'] = 'failed'
        out['execution_status'] = 'failed_old_left_intact_or_unknown'
        out['error_message'] = str(e)[:800]
    out['started_at'] = started
    out['finished_at'] = utc_now()
    return out


def write_reports(summary: dict[str, Any], rows: list[dict[str, Any]]) -> None:
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE_DIR, 0o700)
    PRIVATE_JSON.write_text(json.dumps({
        'generated_at': utc_now(),
        'mode': 'approved_apply_delete_old_only',
        'scope': PACKAGE,
        'approval': 'Lucas approved option 1 on 2026-05-12 Telegram: execute B3.',
        'rollback_note': 'For each applied row, rollback by reinserting rollback_original_product via Content API products.insert. Correct existing product was not touched.',
        'records': rows,
    }, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    os.chmod(PRIVATE_JSON, 0o600)

    public_rows = []
    for r in rows:
        public_rows.append({
            'old_product_id_deleted': r.get('old_product_id_to_delete'),
            'old_offer_id': r.get('old_offer_id'),
            'correct_existing_product_id_kept': r.get('correct_existing_product_id_to_keep'),
            'correct_offer_id': r.get('correct_offer_id'),
            'title': r.get('title'),
            'execution_status': r.get('execution_status'),
            'delete_status': r.get('delete_status'),
            'error_message': r.get('error_message'),
        })
    payload = {
        'generated_at': utc_now(),
        'status': 'gmc_package_b3_delete_old_duplicates_applied_pending_or_verified' if not summary.get('verified_absent_old') else 'gmc_package_b3_delete_old_duplicates_applied_verified',
        'scope': PACKAGE,
        'source_labels': ['fact_merchant_center', 'fact_shopify', 'derived_reconciliation', 'manual_approval_lucas_2026_05_12'],
        'summary': summary | {'private_rollback_path': str(PRIVATE_JSON)},
        'public_rows': public_rows,
        'not_touched': ['shopify_write','feed','database','campaign_or_external_send','local_channel','pos_inventory','google_business_profile'],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    fields = ['old_product_id_deleted','old_offer_id','correct_existing_product_id_kept','correct_offer_id','title','execution_status','delete_status','error_message']
    with OUT_CSV.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(public_rows)
    lines = [
        '# LK GMC Package B3 Delete Old Duplicate Identifiers Execution, 2026-05-12', '',
        f"Status: `{payload['status']}`", '',
        '## Resumo executivo',
        '- Pacote: `B3_delete_old_duplicate_identifier_execution`',
        '- Aprovação: Lucas opção 1, executar B3',
        f"- Linhas aprovadas: {summary.get('approved_rows')}",
        f"- Deletes OK/idempotentes: {summary.get('delete_ok')}",
        f"- Falhas: {summary.get('failed')}",
        f"- Old IDs verificados ausentes: {summary.get('verified_absent_old', 0)}",
        f"- Correct IDs verificados presentes: {summary.get('verified_present_correct', 0)}",
        f"- Snapshot privado de rollback: `{PRIVATE_JSON}`", '',
        '## Interpretação',
        '- Delete-old-only remove os IDs antigos duplicados e mantém os IDs corretos existentes no Merchant.',
        '- Nenhum produto correto, Shopify, feed, banco, local/POS ou campanha foi alterado.', '',
        '## Não tocado',
    ]
    for item in payload['not_touched']:
        lines.append(f'- {item}')
    lines.extend(['', '## Arquivos', f'- JSON: `{OUT_JSON}`', f'- CSV: `{OUT_CSV}`'])
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(OUT_MD.read_text(encoding='utf-8'), encoding='utf-8')

    if CONTROL.exists():
        marker = '### 2026-05-12 — GMC Package B3 delete-old duplicates execution'
        text = CONTROL.read_text(encoding='utf-8')
        block = f"\n{marker}\n\n- Status: {payload['status']}.\n- Escopo aprovado por Lucas: B3 delete-old-only dos IDs antigos duplicados.\n- Deletes OK/idempotentes: {summary.get('delete_ok')}; falhas={summary.get('failed')}; verified_absent_old={summary.get('verified_absent_old',0)}; verified_present_correct={summary.get('verified_present_correct',0)}.\n- Snapshot privado de rollback: `{PRIVATE_JSON}`.\n- Não tocado: Shopify, feed, banco, local/POS, campanhas, Google Business Profile.\n\n"
        if marker not in text:
            CONTROL.write_text(text.rstrip() + block, encoding='utf-8')
    if INDEX.exists():
        line = f'| LK GMC Package B3 Delete Old Duplicates Execution 2026-05-12 | `areas/lk/rotinas/gmc-{RUN_STAMP}.md` | Execução aprovada delete-old-only: removeu IDs antigos duplicados mantendo IDs corretos existentes, com rollback privado |'
        text = INDEX.read_text(encoding='utf-8')
        if line not in text:
            INDEX.write_text(text.rstrip() + '\n' + line + '\n', encoding='utf-8')


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--workers', type=int, default=8)
    ap.add_argument('--verify-delay', type=float, default=90.0)
    args = ap.parse_args()
    if not args.apply:
        raise SystemExit('Refusing to run without --apply; approval exists but explicit apply flag is required.')

    audit = import_module(AUDIT_PATH, 'lk_gmc_catalog_duplication_audit')
    bmod = import_module(B_SCRIPT, 'lk_gmc_execute_package_b_identifier_fix')
    secrets = audit.load_doppler()
    merchant_id = secrets.get('MERCHANT_CENTER_ID_LK')
    if not merchant_id:
        raise RuntimeError('missing_merchant_center_id')
    token = audit.google_access_token(audit.parse_service_account(secrets))
    records = load_preview_records()
    unsafe_same_id = [r for r in records if r.get('old_product_id_to_delete') == r.get('correct_existing_product_id_to_keep')]
    if unsafe_same_id:
        raise RuntimeError(f'unsafe_same_product_id_delete_blocked_count_{len(unsafe_same_id)}')
    if len(records) != 854:
        raise RuntimeError(f'unexpected_record_count_{len(records)}_expected_854')

    rows: list[dict[str, Any]] = []
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = [ex.submit(execute_one, r, merchant_id, token) for r in records]
        for fut in as_completed(futs):
            rows.append(fut.result())
    rows.sort(key=lambda r: r.get('old_product_id_to_delete') or '')
    delete_ok = sum(1 for r in rows if r.get('delete_status') == 'ok_or_already_absent')
    failed = sum(1 for r in rows if r.get('delete_status') == 'failed')

    summary = {
        'approved_rows': len(records),
        'delete_ok': delete_ok,
        'failed': failed,
        'workers': args.workers,
        'verify_delay_seconds': args.verify_delay,
        'merchant_products_current_read_before_verify': None,
    }
    write_reports(summary, rows)

    if args.verify_delay > 0:
        time.sleep(args.verify_delay)
    current = bmod.list_all_products(merchant_id, token)
    current_ids = {p.get('id') for p in current}
    old_ids = {r.get('old_product_id_to_delete') for r in records}
    correct_ids = {r.get('correct_existing_product_id_to_keep') for r in records}
    old_absent = sum(1 for x in old_ids if x not in current_ids)
    correct_present = sum(1 for x in correct_ids if x in current_ids)
    still_present_old = sorted(x for x in old_ids if x in current_ids)
    missing_correct = sorted(x for x in correct_ids if x not in current_ids)
    summary |= {
        'merchant_products_current_read_after_verify': len(current),
        'verified_absent_old': old_absent,
        'verified_present_correct': correct_present,
        'still_present_old_count': len(still_present_old),
        'missing_correct_count': len(missing_correct),
        'still_present_old_sample': still_present_old[:20],
        'missing_correct_sample': missing_correct[:20],
    }
    # Add verification fields to private records, without mutating originals.
    for r in rows:
        r['old_absent_live_verified'] = r.get('old_product_id_to_delete') not in current_ids
        r['correct_existing_present_live_verified'] = r.get('correct_existing_product_id_to_keep') in current_ids
    write_reports(summary, rows)
    print(json.dumps({'status': 'ok', 'summary': summary, 'public_report': str(OUT_MD)}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
