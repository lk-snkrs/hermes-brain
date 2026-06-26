#!/usr/bin/env python3
"""Execute approved LK GMC local C/D cleanup: delete exactly 63 old local LIA rows.

Approval: Lucas selected option 1 in Telegram on 2026-05-12, authorizing
execution exactly for the final approval packet in
reports/lk-gmc-2026-05-12-local-cd-final-approval-packet.json.

Safety contract:
- load candidates from final packet JSON only;
- abort if packet guard_failures_count != 0;
- delete only exact old local product IDs from candidates;
- abort if any old ID equals any replacement ID;
- preflight requires all replacement local IDs still present;
- never touches replacement rows, online rows, Shopify, Tiny, feed, DB, POS settings,
  campaigns, or customer-facing surfaces;
- treats 404 on delete as idempotent;
- verifies old IDs absent and replacement IDs present after Content API delay.
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import os
import pathlib
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / 'scripts/lk_gmc_catalog_duplication_audit_20260512.py'
PACKET_JSON = ROOT / 'reports/lk-gmc-2026-05-12-local-cd-final-approval-packet.json'
SOURCE_ROLLBACK_JSON = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-12-local-cd-pos-source-validation-rollback-snapshot.json')
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
RUN_STAMP = '2026-05-12-local-cd-63-old-lia-cleanup-execution'
PRIVATE_JSON = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-rollback-and-execution.json'
OUT_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
OUT_CSV = ROOT / f'reports/lk-gmc-{RUN_STAMP}.csv'
OUT_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
CONTROL = ROOT / 'areas/lk/projetos/lk-os-implementation-control.md'
INDEX = ROOT / 'empresa/rotinas/_index.md'
PACKAGE = 'local_cd_63_old_lia_cleanup_execution'
EXPECTED_ROWS = 63


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


def load_packet() -> dict[str, Any]:
    payload = json.loads(PACKET_JSON.read_text(encoding='utf-8'))
    if payload.get('status') != 'gmc_local_cd_final_approval_packet_ready_no_execution':
        raise RuntimeError(f"unexpected_packet_status_{payload.get('status')}")
    if (payload.get('summary') or {}).get('guard_failures_count') != 0:
        raise RuntimeError('packet_guard_failures_nonzero_abort')
    candidates = payload.get('candidates') or []
    if len(candidates) != EXPECTED_ROWS:
        raise RuntimeError(f'unexpected_candidate_count_{len(candidates)}_expected_{EXPECTED_ROWS}')
    return payload


def build_records(packet: dict[str, Any], current_ids: set[str], rollback_by_id: dict[str, dict[str, Any]]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    guard_failures: list[dict[str, Any]] = []
    old_ids_seen: set[str] = set()
    for c in packet.get('candidates') or []:
        old_pid = c.get('old_product_id_to_delete_if_approved') or ''
        repl_ids = list(c.get('replacement_local_product_ids_present') or [])
        fail_reasons: list[str] = []
        if not old_pid.startswith('local:pt:BR:LIA_'):
            fail_reasons.append('old_pid_not_expected_local_lia_prefix')
        if old_pid in old_ids_seen:
            fail_reasons.append('duplicate_old_pid_in_packet')
        old_ids_seen.add(old_pid)
        if not repl_ids:
            fail_reasons.append('no_replacement_ids_in_packet')
        if old_pid in repl_ids:
            fail_reasons.append('old_pid_equals_replacement_pid_blocked')
        missing_repl = [x for x in repl_ids if x not in current_ids]
        if missing_repl:
            fail_reasons.append('replacement_missing_in_live_preflight')
        if fail_reasons:
            guard_failures.append({'old_product_id': old_pid, 'fail_reasons': fail_reasons, 'missing_replacements': missing_repl})
        rb = rollback_by_id.get(old_pid) or {}
        rows.append({
            'package': PACKAGE,
            'old_product_id_to_delete': old_pid,
            'old_offer_id': c.get('old_offer_id'),
            'old_normalized_sku': c.get('old_normalized_sku'),
            'title': c.get('merchant_title'),
            'package_origin': c.get('package_origin'),
            'replacement_local_product_ids_kept': repl_ids,
            'replacement_local_present_preflight': len([x for x in repl_ids if x in current_ids]),
            'old_present_preflight': old_pid in current_ids,
            'rollback_original_product': rb.get('merchant_product_resource') or {},
            'rollback_original_status': rb.get('merchant_product_status') or {},
            'execution_status': 'planned_not_executed',
        })
    if guard_failures:
        raise RuntimeError('hard_guard_preflight_failed: ' + json.dumps(guard_failures[:10], ensure_ascii=False))
    return rows, {
        'approved_rows': len(rows),
        'old_present_preflight': sum(1 for r in rows if r['old_present_preflight']),
        'old_already_absent_preflight': sum(1 for r in rows if not r['old_present_preflight']),
        'unique_replacement_ids': len({x for r in rows for x in r['replacement_local_product_ids_kept']}),
    }


def execute_one(rec: dict[str, Any], merchant_id: str, token: str) -> dict[str, Any]:
    out = dict(rec)
    started = utc_now()
    try:
        delete_product(merchant_id, out['old_product_id_to_delete'], token)
        out['delete_status'] = 'ok_or_already_absent'
        out['execution_status'] = 'applied_delete_old_local_only_keep_replacement'
    except Exception as e:
        out['delete_status'] = 'failed'
        out['execution_status'] = 'failed_old_left_intact_or_unknown'
        out['error_message'] = str(e)[:800]
    out['started_at'] = started
    out['finished_at'] = utc_now()
    return out


def write_reports(mode: str, summary: dict[str, Any], rows: list[dict[str, Any]]) -> None:
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE_DIR, 0o700)
    private_payload = {
        'generated_at': utc_now(),
        'mode': mode,
        'scope': PACKAGE,
        'approval': 'Lucas approved option 1 on 2026-05-12 Telegram: execute exactly the 63 old local LIA IDs in final approval packet.',
        'source_packet': str(PACKET_JSON),
        'source_rollback_snapshot': str(SOURCE_ROLLBACK_JSON),
        'rollback_note': 'For any affected row, restore by reinserting rollback_original_product via Content API products.insert, then verify exact old ID presence and replacement IDs still present.',
        'records': rows,
    }
    PRIVATE_JSON.write_text(json.dumps(private_payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    os.chmod(PRIVATE_JSON, 0o600)

    public_rows: list[dict[str, Any]] = []
    for r in rows:
        public_rows.append({
            'old_product_id_deleted': r.get('old_product_id_to_delete'),
            'old_offer_id': r.get('old_offer_id'),
            'old_normalized_sku': r.get('old_normalized_sku'),
            'replacement_local_product_ids_kept': ';'.join(r.get('replacement_local_product_ids_kept') or []),
            'title': r.get('title'),
            'package_origin': r.get('package_origin'),
            'old_present_preflight': r.get('old_present_preflight'),
            'replacement_local_present_preflight': r.get('replacement_local_present_preflight'),
            'execution_status': r.get('execution_status'),
            'delete_status': r.get('delete_status'),
            'old_absent_live_verified': r.get('old_absent_live_verified'),
            'replacement_ids_present_live_verified': r.get('replacement_ids_present_live_verified'),
            'error_message': r.get('error_message'),
        })
    status = 'gmc_local_cd_63_old_lia_cleanup_dry_run_ready'
    if mode == 'apply':
        if summary.get('failed', 0) == 0 and summary.get('still_present_old_count', 1) == 0 and summary.get('missing_replacement_count', 1) == 0:
            status = 'gmc_local_cd_63_old_lia_cleanup_applied_verified'
        else:
            status = 'gmc_local_cd_63_old_lia_cleanup_applied_needs_review'
    payload = {
        'generated_at': utc_now(),
        'status': status,
        'scope': PACKAGE,
        'source_labels': ['fact_merchant_center', 'fact_shopify', 'fact_tiny_stock', 'derived_reconciliation', 'manual_approval_lucas_2026_05_12'],
        'summary': summary | {'private_rollback_and_execution_path': str(PRIVATE_JSON)},
        'public_rows': public_rows,
        'not_touched': ['online_products','replacement_local_rows','local_inventory_channel_or_pos_settings','shopify','tiny','feed','database','campaign_or_external_send','customer_facing_surfaces'],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    fields = ['old_product_id_deleted','old_offer_id','old_normalized_sku','replacement_local_product_ids_kept','title','package_origin','old_present_preflight','replacement_local_present_preflight','execution_status','delete_status','old_absent_live_verified','replacement_ids_present_live_verified','error_message']
    with OUT_CSV.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(public_rows)

    lines = [
        '# LK GMC Local C/D 63 Old LIA Cleanup Execution, 2026-05-12', '',
        f"Status: `{payload['status']}`", '',
        '## Resumo executivo',
        f'- Pacote: `{PACKAGE}`',
        '- Aprovação: Lucas opção 1 no Telegram, executar exatamente os 63 IDs locais antigos do approval packet final.',
        f"- Modo: `{mode}`",
        f"- Linhas aprovadas: {summary.get('approved_rows')}",
        f"- Old IDs presentes no preflight: {summary.get('old_present_preflight')}",
        f"- Old IDs já ausentes no preflight/idempotentes: {summary.get('old_already_absent_preflight')}",
        f"- Deletes OK/idempotentes: {summary.get('delete_ok', 0)}",
        f"- Falhas: {summary.get('failed', 0)}",
        f"- Old IDs verificados ausentes: {summary.get('verified_absent_old', 0)}",
        f"- Old IDs ainda presentes: {summary.get('still_present_old_count', 0)}",
        f"- Replacement IDs verificados presentes: {summary.get('verified_present_replacement', 0)} / {summary.get('unique_replacement_ids', 0)}",
        f"- Replacement IDs ausentes: {summary.get('missing_replacement_count', 0)}",
        f"- Snapshot privado rollback+execução: `{PRIVATE_JSON}`", '',
        '## Interpretação',
        '- Foram removidos somente IDs locais antigos `local:pt:BR:LIA_<old_sku>` aprovados no pacote final.',
        '- As linhas replacement locais atuais foram preservadas e verificadas após a execução.', '',
        '## Não tocado',
    ]
    for item in payload['not_touched']:
        lines.append(f'- {item}')
    lines.extend(['', '## Arquivos', f'- JSON: `{OUT_JSON}`', f'- CSV: `{OUT_CSV}`'])
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(OUT_MD.read_text(encoding='utf-8'), encoding='utf-8')

    if CONTROL.exists():
        marker = '### 2026-05-12 — GMC local C/D 63 old LIA cleanup execution'
        text = CONTROL.read_text(encoding='utf-8')
        block = (
            f"\n{marker}\n\n"
            f"- Status: {payload['status']}.\n"
            f"- Escopo aprovado por Lucas: delete exato de 63 IDs locais antigos `LIA_`, mantendo replacement rows locais.\n"
            f"- Deletes OK/idempotentes: {summary.get('delete_ok',0)}; falhas={summary.get('failed',0)}; old_absent={summary.get('verified_absent_old',0)}; old_still_present={summary.get('still_present_old_count',0)}; replacements_present={summary.get('verified_present_replacement',0)}/{summary.get('unique_replacement_ids',0)}.\n"
            f"- Snapshot privado rollback+execução: `{PRIVATE_JSON}`.\n"
            f"- Não tocado: online products, replacement local rows, Shopify, Tiny, feed, banco, POS/local channel, campanhas/clientes.\n\n"
        )
        if marker in text:
            text = re.sub(
                rf'\n{re.escape(marker)}\n\n.*?(?=\n### |\Z)',
                block.rstrip() + '\n',
                text,
                count=1,
                flags=re.S,
            )
            CONTROL.write_text(text.rstrip() + '\n', encoding='utf-8')
        else:
            CONTROL.write_text(text.rstrip() + block, encoding='utf-8')
    if INDEX.exists():
        line = f'| LK GMC Local C/D 63 Old LIA Cleanup Execution 2026-05-12 | `areas/lk/rotinas/gmc-{RUN_STAMP}.md` | Execução aprovada: delete exato dos 63 IDs locais antigos LIA, mantendo replacement rows locais, com rollback privado e verificação pós-Content API |'
        text = INDEX.read_text(encoding='utf-8')
        if line not in text:
            INDEX.write_text(text.rstrip() + '\n' + line + '\n', encoding='utf-8')


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true', help='execute approved exact Merchant deletes')
    ap.add_argument('--workers', type=int, default=4)
    ap.add_argument('--verify-delay', type=float, default=90.0)
    args = ap.parse_args()

    audit = import_module(AUDIT_PATH, 'lk_gmc_catalog_duplication_audit')
    secrets = audit.load_doppler()
    merchant_id = secrets.get('MERCHANT_CENTER_ID_LK')
    if not merchant_id:
        raise RuntimeError('missing_merchant_center_id')
    token = audit.google_access_token(audit.parse_service_account(secrets))
    packet = load_packet()
    rollback_payload = json.loads(SOURCE_ROLLBACK_JSON.read_text(encoding='utf-8'))
    rollback_by_id = {r.get('product_id'): r for r in (rollback_payload.get('records') or [])}

    current = audit.list_all('products', merchant_id, token)
    current_ids = {p.get('id') for p in current}
    rows, summary = build_records(packet, current_ids, rollback_by_id)
    summary |= {
        'merchant_products_current_read_preflight': len(current),
        'workers': args.workers,
        'verify_delay_seconds': args.verify_delay,
        'apply_flag': bool(args.apply),
    }

    if not args.apply:
        write_reports('dry_run', summary, rows)
        print(json.dumps({'status': 'dry_run_ready', 'summary': summary, 'public_report': str(OUT_MD)}, ensure_ascii=False, indent=2))
        return

    executed: list[dict[str, Any]] = []
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = [ex.submit(execute_one, r, merchant_id, token) for r in rows]
        for fut in as_completed(futs):
            executed.append(fut.result())
    executed.sort(key=lambda r: r.get('old_product_id_to_delete') or '')
    summary |= {
        'delete_ok': sum(1 for r in executed if r.get('delete_status') == 'ok_or_already_absent'),
        'failed': sum(1 for r in executed if r.get('delete_status') == 'failed'),
    }
    write_reports('apply', summary, executed)

    if args.verify_delay > 0:
        time.sleep(args.verify_delay)
    current_after = audit.list_all('products', merchant_id, token)
    current_after_ids = {p.get('id') for p in current_after}
    old_ids = {r.get('old_product_id_to_delete') for r in rows}
    repl_ids = {x for r in rows for x in (r.get('replacement_local_product_ids_kept') or [])}
    still_present_old = sorted(x for x in old_ids if x in current_after_ids)
    missing_repl = sorted(x for x in repl_ids if x not in current_after_ids)
    summary |= {
        'merchant_products_current_read_after_verify': len(current_after),
        'verified_absent_old': sum(1 for x in old_ids if x not in current_after_ids),
        'still_present_old_count': len(still_present_old),
        'still_present_old_sample': still_present_old[:20],
        'verified_present_replacement': sum(1 for x in repl_ids if x in current_after_ids),
        'missing_replacement_count': len(missing_repl),
        'missing_replacement_sample': missing_repl[:20],
    }
    for r in executed:
        r['old_absent_live_verified'] = r.get('old_product_id_to_delete') not in current_after_ids
        r['replacement_ids_present_live_verified'] = all(x in current_after_ids for x in (r.get('replacement_local_product_ids_kept') or []))
    write_reports('apply', summary, executed)
    print(json.dumps({'status': 'ok', 'summary': summary, 'public_report': str(OUT_MD)}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
