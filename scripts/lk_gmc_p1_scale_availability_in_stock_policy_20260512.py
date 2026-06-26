#!/usr/bin/env python3
"""Scale approved LK GMC P1-B availability=in stock in controlled batches.

Lucas chose option 1 after a successful 25-item pilot: scale remaining exact online
Merchant products in controlled batches, with rollback before each batch and
post-delay verification/retry. This script does not touch Tiny, Shopify, feed,
DB, POS, campaigns, deletes, prices, titles, links, or images.
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import os
import pathlib
import time
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
EXECUTOR_PATH = ROOT / 'scripts/lk_gmc_p1_execute_availability_in_stock_policy_20260512.py'
INPUT_CSV = ROOT / 'reports/lk-gmc-2026-05-12-p1-availability-in-stock-policy-packet.csv'
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
RUN_STAMP = '2026-05-12-p1-availability-in-stock-policy-scale-batches'
PUBLIC_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
PUBLIC_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
CONTROL = ROOT / 'areas/lk/projetos/lk-os-implementation-control.md'
INDEX = ROOT / 'empresa/rotinas/_index.md'
TARGET_VALUE = 'in stock'


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def import_executor():
    spec = importlib.util.spec_from_file_location('availability_executor', EXECUTOR_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def load_packet_rows() -> list[dict[str, Any]]:
    with INPUT_CSV.open(newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def write_retry_snapshot(records: list[dict[str, Any]], batch_no: int) -> pathlib.Path:
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE_DIR, 0o700)
    path = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-batch-{batch_no:02d}-retry-rollback-{datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")}.json'
    payload = {
        'generated_at': utc_now(),
        'approval_context': 'Lucas chose option 1: scale in controlled batches after successful pilot 25.',
        'scope': f'retry remaining non-verified IDs inside batch {batch_no}; availability=in stock only',
        'records': records,
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    os.chmod(path, 0o600)
    return path


def retry_not_verified(exe, merchant_id: str, token: str, verified: list[dict[str, Any]], batch_no: int) -> tuple[list[dict[str, Any]], pathlib.Path | None]:
    failed_ids = [v['product_id'] for v in verified if not v.get('availability_is_in_stock')]
    if not failed_ids:
        return [], None
    records = []
    results = []
    for pid in failed_ids:
        current = exe.get_product(merchant_id, pid, token)
        records.append({'product_id': pid, 'current_product_resource': current, 'retry_update': {'availability': TARGET_VALUE}})
    rollback = write_retry_snapshot(records, batch_no)
    for rec in records:
        pid = rec['product_id']
        try:
            updated = exe.upsert_product(merchant_id, exe.prepare_updated_product(rec['current_product_resource']), token)
            results.append({'product_id': pid, 'execution_status': 'retry_updated_availability_in_stock', 'availability_after_response': updated.get('availability')})
        except Exception as e:
            results.append({'product_id': pid, 'execution_status': 'retry_failed', 'error': str(e)[:1200]})
            break
        time.sleep(0.2)
    return results, rollback


def productstatus_missing_for_ids(exe, statuses: list[dict[str, Any]], ids: set[str]) -> list[str]:
    out = []
    for st in statuses:
        pid = st.get('productId')
        if pid in ids and 'availability' in exe.missing_required_attrs(st):
            out.append(pid)
    return out


def write_consolidated_report(payload: dict[str, Any]) -> None:
    PUBLIC_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    lines = [
        '# LK GMC P1-B Availability In-Stock Policy Scale Batches, 2026-05-12', '',
        f"Status: `{payload['status']}`", '',
        '## Aprovação usada',
        '- Lucas escolheu `1`: escala em lotes controlados depois do piloto 25 bem-sucedido.', '',
        '## Escopo',
        '- Campo alterado: `availability` apenas.',
        '- Valor aplicado: `in stock`.',
        '- Produtos: exact online Merchant IDs do packet P1-B corrigido.',
        '- Regra: GMC deve mostrar disponível mesmo se Tiny estiver zerado.', '',
        '## Resultado consolidado',
        f"- Batch size: {payload['batch_size']}",
        f"- Lotes executados: {payload['summary'].get('batches_executed')}",
        f"- Updates em escala com sucesso: {payload['summary'].get('updated_total')}",
        f"- Retries com sucesso: {payload['summary'].get('retry_updated_total')}",
        f"- Falhas finais: {payload['summary'].get('failed_total')}",
        f"- Total verificado `products.get` como in stock nos lotes de escala: {payload['summary'].get('verified_in_stock_total')}",
        f"- Total do packet P1-B agora em stock pelo preflight final: {payload['summary'].get('final_already_in_stock_or_clean')}/{payload['summary'].get('packet_rows')}",
        f"- Restantes prontos/pendentes pelo preflight final: {payload['summary'].get('final_ready_total')}",
        f"- Ainda com diagnóstico availability em productstatuses no packet: {payload['summary'].get('final_productstatus_missing_availability')}", '',
        '## Lotes',
    ]
    for b in payload.get('batches', []):
        lines.append(f"- Batch {b['batch_no']}: selected={b['selected']} updated={b['updated']} retry_updated={b['retry_updated']} verified_in_stock={b['verified_in_stock']} failed={b['failed']} rollback_saved=yes")
    lines += ['', '## Rollbacks privados']
    for p in payload.get('rollback_paths', []):
        lines.append(f'- `{p}`')
    lines += ['', '## Não executado']
    for n in payload.get('not_performed', []):
        lines.append(f'- {n}')
    content = '\n'.join(lines) + '\n'
    PUBLIC_MD.write_text(content, encoding='utf-8')
    BRAIN_DOC.write_text(content, encoding='utf-8')
    if CONTROL.exists():
        marker = '### 2026-05-12 — GMC P1-B availability in-stock policy scale batches'
        text = CONTROL.read_text(encoding='utf-8')
        block = (f"\n{marker}\n\n"
                 f"- Status: `{payload['status']}`.\n"
                 f"- Aprovação: Lucas escolheu opção 1, escala em lotes controlados.\n"
                 f"- Escopo: exact online Merchant IDs; `availability=in stock` apenas.\n"
                 f"- Resultado: updates escala={payload['summary'].get('updated_total')}; retries={payload['summary'].get('retry_updated_total')}; final_ready={payload['summary'].get('final_ready_total')}; final_status_missing={payload['summary'].get('final_productstatus_missing_availability')}.\n")
        if marker not in text:
            CONTROL.write_text(text.rstrip() + block + '\n', encoding='utf-8')
    if INDEX.exists():
        line = f'| LK GMC P1-B Availability In-Stock Policy Scale Batches 2026-05-12 | `areas/lk/rotinas/gmc-{RUN_STAMP}.md` | Escala aprovada em lotes: availability=in stock para exact online Merchant IDs; rollback privado por lote e verificação products.get/productstatuses |'
        text = INDEX.read_text(encoding='utf-8')
        if line not in text:
            INDEX.write_text(text.rstrip() + '\n' + line + '\n', encoding='utf-8')


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--batch-size', type=int, default=200)
    ap.add_argument('--max-batches', type=int, default=20)
    ap.add_argument('--verify-delay', type=int, default=60)
    ap.add_argument('--final-delay', type=int, default=60)
    args = ap.parse_args()
    exe = import_executor()
    audit = exe.import_audit()
    secrets = audit.load_doppler()
    merchant_id = secrets.get('MERCHANT_CENTER_ID_LK')
    if not merchant_id:
        raise RuntimeError('missing_merchant_center_id')
    token = audit.google_access_token(audit.parse_service_account(secrets))
    packet_rows = load_packet_rows()
    batches = []
    rollback_paths = []
    all_execution = []
    all_retry = []
    all_verified = []
    status = 'running'

    for batch_no in range(1, args.max_batches + 1):
        products = audit.list_all('products', merchant_id, token)
        statuses = audit.list_all('productstatuses', merchant_id, token)
        rows, summary = exe.build_ready_rows(packet_rows, products, statuses, args.batch_size)
        if summary.get('selected_for_apply', 0) == 0:
            status = 'gmc_p1_availability_in_stock_scale_complete_no_more_selected'
            break
        execution, rollback = exe.apply_selected(merchant_id, token, rows, products, args.batch_size)
        rollback_paths.append(str(rollback))
        verified = exe.verify_results(merchant_id, token, execution, args.verify_delay)
        retry_results, retry_rollback = retry_not_verified(exe, merchant_id, token, verified, batch_no)
        if retry_rollback:
            rollback_paths.append(str(retry_rollback))
            # Reverify the original execution selection after retry and a short consistency wait.
            time.sleep(args.verify_delay)
            verified = exe.verify_results(merchant_id, token, execution, 0)
        all_execution.extend(execution)
        all_retry.extend(retry_results)
        all_verified.extend(verified)
        counts = Counter(r.get('execution_status') for r in execution)
        retry_counts = Counter(r.get('execution_status') for r in retry_results)
        failed = counts.get('failed_http_or_validation', 0) + retry_counts.get('retry_failed', 0)
        batches.append({
            'batch_no': batch_no,
            'selected': summary.get('selected_for_apply'),
            'ready_total_before_batch': summary.get('ready_total'),
            'updated': counts.get('updated_availability_in_stock', 0),
            'retry_updated': retry_counts.get('retry_updated_availability_in_stock', 0),
            'verified_in_stock': sum(1 for v in verified if v.get('availability_is_in_stock')),
            'failed': failed,
            'rollback_path': str(rollback),
            'retry_rollback_path': str(retry_rollback) if retry_rollback else None,
        })
        partial = {
            'generated_at': utc_now(),
            'status': 'partial_running' if failed == 0 else 'stopped_after_failure',
            'batch_size': args.batch_size,
            'summary': {
                'packet_rows': len(packet_rows),
                'batches_executed': len(batches),
                'updated_total': sum(1 for r in all_execution if r.get('execution_status') == 'updated_availability_in_stock'),
                'retry_updated_total': sum(1 for r in all_retry if r.get('execution_status') == 'retry_updated_availability_in_stock'),
                'failed_total': failed,
                'verified_in_stock_total': sum(1 for r in all_verified if r.get('availability_is_in_stock')),
            },
            'batches': batches,
            'rollback_paths': rollback_paths,
            'not_performed': ['merchant_delete','merchant_price_title_link_image_update','tiny_call','tiny_write','shopify_write','feed_update_or_fetch','database_write','pos_write','campaign_or_external_send','sourcing_or_supplier_contact'],
        }
        write_consolidated_report(partial)
        print(json.dumps({'batch': batch_no, 'selected': summary.get('selected_for_apply'), 'updated': batches[-1]['updated'], 'retry_updated': batches[-1]['retry_updated'], 'verified_in_stock': batches[-1]['verified_in_stock'], 'failed': failed}, ensure_ascii=False), flush=True)
        if failed:
            status = 'gmc_p1_availability_in_stock_scale_stopped_after_failure'
            break
    else:
        status = 'gmc_p1_availability_in_stock_scale_stopped_after_max_batches'

    if args.final_delay:
        time.sleep(args.final_delay)
    products = audit.list_all('products', merchant_id, token)
    statuses = audit.list_all('productstatuses', merchant_id, token)
    final_rows, final_summary = exe.build_ready_rows(packet_rows, products, statuses, args.batch_size)
    packet_ids = {r.get('product_id') for r in packet_rows if r.get('product_id')}
    final_missing = productstatus_missing_for_ids(exe, statuses, packet_ids)
    clean_or_in_stock = len(packet_rows) - final_summary.get('ready_total', 0)
    if final_summary.get('ready_total', 0) == 0 and not final_missing:
        status = 'gmc_p1_availability_in_stock_scale_complete_verified'
    payload = {
        'generated_at': utc_now(),
        'status': status,
        'approval_context': 'Lucas chose option 1: scale in controlled batches after successful pilot 25.',
        'batch_size': args.batch_size,
        'summary': {
            'packet_rows': len(packet_rows),
            'batches_executed': len(batches),
            'updated_total': sum(1 for r in all_execution if r.get('execution_status') == 'updated_availability_in_stock'),
            'retry_updated_total': sum(1 for r in all_retry if r.get('execution_status') == 'retry_updated_availability_in_stock'),
            'failed_total': sum(b['failed'] for b in batches),
            'verified_in_stock_total': sum(1 for r in all_verified if r.get('availability_is_in_stock')),
            'final_ready_total': final_summary.get('ready_total'),
            'final_decision_state_counts': final_summary.get('decision_state_counts'),
            'final_already_in_stock_or_clean': clean_or_in_stock,
            'final_productstatus_missing_availability': len(final_missing),
            'final_productstatus_missing_availability_sample': final_missing[:50],
        },
        'batches': batches,
        'rollback_paths': rollback_paths,
        'execution_results': all_execution,
        'retry_results': all_retry,
        'verified_results': all_verified,
        'not_performed': ['merchant_delete','merchant_price_title_link_image_update','tiny_call','tiny_write','shopify_write','feed_update_or_fetch','database_write','pos_write','campaign_or_external_send','sourcing_or_supplier_contact'],
    }
    write_consolidated_report(payload)
    print(json.dumps({'status': status, 'summary': payload['summary'], 'public_report': str(PUBLIC_MD)}, ensure_ascii=False, indent=2), flush=True)


if __name__ == '__main__':
    main()
