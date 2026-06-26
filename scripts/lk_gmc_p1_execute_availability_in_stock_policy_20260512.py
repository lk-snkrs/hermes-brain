#!/usr/bin/env python3
"""Execute approved LK GMC P1-B availability=in stock policy pilot.

Approved by Lucas in Telegram with "Aprovo" after the recommended option was a
pilot of 25 exact online Merchant products. This script:
- reads the corrected no-write packet;
- re-fetches Merchant products/statuses;
- selects exact online products still missing availability;
- saves full rollback resources privately before any write;
- updates only `availability` to `in stock` through products.insert upsert;
- verifies the updated resources after a consistency delay.
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
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / 'scripts/lk_gmc_catalog_duplication_audit_20260512.py'
INPUT_JSON = ROOT / 'reports/lk-gmc-2026-05-12-p1-availability-in-stock-policy-packet.json'
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
RUN_STAMP = '2026-05-12-p1-availability-in-stock-policy-executor'
PUBLIC_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
PUBLIC_CSV = ROOT / f'reports/lk-gmc-{RUN_STAMP}.csv'
PUBLIC_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
CONTROL = ROOT / 'areas/lk/projetos/lk-os-implementation-control.md'
INDEX = ROOT / 'empresa/rotinas/_index.md'
REQ_CODES = {'item_missing_required_attribute', 'missing_item_attribute_for_product_type'}
TARGET_FIELD = 'availability'
TARGET_VALUE = 'in stock'


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def import_audit():
    spec = importlib.util.spec_from_file_location('audit', AUDIT_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def request_json(url: str, token: str, method: str = 'GET', payload: dict[str, Any] | None = None, max_attempts: int = 5) -> dict[str, Any]:
    data = None if payload is None else json.dumps(payload, ensure_ascii=False).encode('utf-8')
    last_error = ''
    for attempt in range(1, max_attempts + 1):
        req = urllib.request.Request(url, data=data, method=method)
        req.add_header('Authorization', 'Bearer ' + token)
        if payload is not None:
            req.add_header('Content-Type', 'application/json; charset=utf-8')
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                raw = r.read().decode()
                return json.loads(raw) if raw else {}
        except urllib.error.HTTPError as e:
            raw = e.read().decode(errors='replace')
            last_error = f'http_{e.code}: {raw[:1200]}'
            if e.code not in {429, 500, 502, 503, 504} or attempt == max_attempts:
                raise RuntimeError(last_error) from e
            time.sleep(min(60, 2 ** attempt))
        except Exception as e:
            last_error = str(e)[:1200]
            if attempt == max_attempts:
                raise RuntimeError(last_error) from e
            time.sleep(min(60, 2 ** attempt))
    raise RuntimeError(last_error or 'request_failed')


def product_url(merchant_id: str, product_id: str) -> str:
    return f'https://shoppingcontent.googleapis.com/content/v2.1/{merchant_id}/products/{urllib.parse.quote(product_id, safe="")}'


def get_product(merchant_id: str, product_id: str, token: str) -> dict[str, Any]:
    return request_json(product_url(merchant_id, product_id), token=token)


def upsert_product(merchant_id: str, product: dict[str, Any], token: str) -> dict[str, Any]:
    url = f'https://shoppingcontent.googleapis.com/content/v2.1/{merchant_id}/products'
    return request_json(url, token=token, method='POST', payload=product)


def chan(pid: str) -> str:
    return (pid or '').split(':', 1)[0] if ':' in (pid or '') else 'unknown'


def missing_required_attrs(status: dict[str, Any]) -> set[str]:
    out = set()
    for issue in status.get('itemLevelIssues') or []:
        if issue.get('code') in REQ_CODES:
            attr = str(issue.get('attributeName') or '').strip().lower().replace('_', ' ')
            if attr:
                out.add(attr)
    return out


def prepare_updated_product(current: dict[str, Any]) -> dict[str, Any]:
    out = json.loads(json.dumps(current, ensure_ascii=False))
    for k in ['id', 'kind', 'source']:
        out.pop(k, None)
    out[TARGET_FIELD] = TARGET_VALUE
    return out


def write_private_snapshot(records: list[dict[str, Any]], mode: str, limit: int) -> pathlib.Path:
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE_DIR, 0o700)
    path = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-rollback-{datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")}.json'
    payload = {
        'generated_at': utc_now(),
        'approval_context': 'Lucas Telegram: Aprovo; interpreted as recommended pilot 25 from prior approval options.',
        'scope': f'P1-B corrected GMC availability policy pilot limit={limit}; update exact online product availability to in stock only',
        'target_field': TARGET_FIELD,
        'target_value': TARGET_VALUE,
        'mode': mode,
        'rollback_instruction': 'Use products.insert/upsert with current_product_resource for each product_id to restore if rollback is needed; verify after consistency delay.',
        'records': records,
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    os.chmod(path, 0o600)
    return path


def build_ready_rows(packet_rows: list[dict[str, Any]], products: list[dict[str, Any]], statuses: list[dict[str, Any]], limit: int) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    product_by_id = {p.get('id'): p for p in products}
    status_by_id = {s.get('productId'): s for s in statuses}
    rows: list[dict[str, Any]] = []
    counters: Counter[str] = Counter()
    seen: set[str] = set()
    for pr in packet_rows:
        pid = pr.get('product_id') or ''
        if pid in seen:
            continue
        seen.add(pid)
        product = product_by_id.get(pid)
        status = status_by_id.get(pid) or {}
        if chan(pid) != 'online':
            decision = 'blocked_non_online_product_id'
        elif not product:
            decision = 'blocked_product_not_currently_present'
        else:
            missing = missing_required_attrs(status)
            if product.get('availability') == TARGET_VALUE and 'availability' not in missing:
                decision = 'skipped_already_in_stock_no_current_diagnostic'
            elif product.get('availability') and product.get('availability') != TARGET_VALUE:
                decision = 'ready_overwrite_existing_availability_if_lucas_approves'
            else:
                decision = 'ready_for_in_stock_policy_apply_if_lucas_approves'
        counters[decision] += 1
        row = {
            'product_id': pid,
            'offer_id': pr.get('offer_id'),
            'merchant_title': product.get('title') if product else pr.get('merchant_title'),
            'current_availability': product.get('availability') if product else '',
            'fresh_missing_required_attrs': sorted(missing_required_attrs(status)),
            'proposed_availability': TARGET_VALUE,
            'decision_state': decision,
            'write_scope_if_approved': 'availability only, exact online Merchant product resource, products.insert upsert',
            'rollback_required_before_write': True,
        }
        rows.append(row)
    ready = [r for r in rows if r['decision_state'] in {'ready_for_in_stock_policy_apply_if_lucas_approves', 'ready_overwrite_existing_availability_if_lucas_approves'}]
    selected_ids = {r['product_id'] for r in ready[:limit]}
    for r in rows:
        if r['product_id'] in selected_ids:
            r['selected_for_apply'] = True
        else:
            r['selected_for_apply'] = False
    summary = {
        'packet_rows': len(packet_rows),
        'fresh_merchant_products_current': len(products),
        'fresh_merchant_productstatuses_current': len(statuses),
        'decision_state_counts': dict(counters),
        'ready_total': len(ready),
        'selected_for_apply': len(selected_ids),
        'target_field': TARGET_FIELD,
        'target_value': TARGET_VALUE,
        'write_allowed_by_current_approval': f'pilot_{limit}_only',
    }
    return rows, summary


def apply_selected(merchant_id: str, token: str, rows: list[dict[str, Any]], products: list[dict[str, Any]], limit: int) -> tuple[list[dict[str, Any]], pathlib.Path]:
    current_by_id = {p.get('id'): p for p in products}
    selected = [r for r in rows if r.get('selected_for_apply')]
    rollback_records = []
    for r in selected:
        current = current_by_id.get(r['product_id'])
        if not current or current.get('id') != r['product_id']:
            raise RuntimeError(f'pre_apply_current_resource_missing: {r["product_id"]}')
        rollback_records.append({'product_id': r['product_id'], 'current_product_resource': current, 'planned_update': r})
    rollback_path = write_private_snapshot(rollback_records, mode='apply', limit=limit)
    progress_path = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-progress-{rollback_path.stem.rsplit("-", 1)[-1]}.jsonl'
    results: list[dict[str, Any]] = []
    with progress_path.open('w', encoding='utf-8') as progress:
        os.chmod(progress_path, 0o600)
        for rec in rollback_records:
            pid = rec['product_id']
            body = prepare_updated_product(rec['current_product_resource'])
            try:
                updated = upsert_product(merchant_id, body, token)
                item = {
                    'product_id': pid,
                    'execution_status': 'updated_availability_in_stock',
                    'availability_after_response': updated.get('availability'),
                }
            except Exception as e:
                item = {'product_id': pid, 'execution_status': 'failed_http_or_validation', 'error': str(e)[:1200]}
                results.append(item)
                progress.write(json.dumps(item, ensure_ascii=False) + '\n')
                progress.flush()
                break
            results.append(item)
            progress.write(json.dumps(item, ensure_ascii=False) + '\n')
            progress.flush()
            time.sleep(0.2)
    return results, rollback_path


def verify_results(merchant_id: str, token: str, results: list[dict[str, Any]], delay: int) -> list[dict[str, Any]]:
    if delay:
        time.sleep(delay)
    verified = []
    for r in results:
        pid = r.get('product_id')
        if r.get('execution_status') != 'updated_availability_in_stock' or not pid:
            verified.append({**r, 'verify_status': 'not_verified_due_to_execution_status'})
            continue
        try:
            prod = get_product(merchant_id, pid, token)
            verified.append({
                **r,
                'verify_status': 'verified_product_get',
                'availability_after_get': prod.get('availability'),
                'availability_is_in_stock': prod.get('availability') == TARGET_VALUE,
            })
        except Exception as e:
            verified.append({**r, 'verify_status': 'verify_failed', 'verify_error': str(e)[:1200]})
    return verified


def write_outputs(mode: str, summary: dict[str, Any], rows: list[dict[str, Any]], execution_results: list[dict[str, Any]], verified_results: list[dict[str, Any]], rollback_path: pathlib.Path | None, limit: int) -> None:
    execution_counts = Counter(r.get('execution_status') for r in execution_results)
    verify_counts = Counter(r.get('verify_status') for r in verified_results)
    verify_in_stock = sum(1 for r in verified_results if r.get('availability_is_in_stock'))
    payload = {
        'generated_at': utc_now(),
        'status': 'gmc_p1_availability_in_stock_policy_pilot_apply_verified' if mode == 'apply' else 'gmc_p1_availability_in_stock_policy_executor_dry_run_ready',
        'mode': mode,
        'approval_context': 'Lucas Telegram: Aprovo; interpreted as recommended pilot 25 from prior approval options.',
        'scope': f'Pilot limit={limit}; exact online Merchant products; update only availability to in stock under Lucas GMC visibility policy.',
        'source_labels': ['fact_merchant_center', 'manual_approval', 'manual_approval_policy', 'derived_reconciliation'],
        'summary': {**summary, 'execution_results_summary': dict(execution_counts), 'verify_results_summary': dict(verify_counts), 'verified_in_stock': verify_in_stock},
        'private_rollback_snapshot_path': str(rollback_path) if rollback_path else None,
        'public_rows': rows,
        'execution_results': execution_results,
        'verified_results': verified_results,
        'not_performed': ['merchant_delete', 'merchant_price_title_link_image_update', 'tiny_call', 'tiny_write', 'shopify_write', 'feed_update_or_fetch', 'database_write', 'pos_write', 'campaign_or_external_send', 'sourcing_or_supplier_contact'],
    }
    PUBLIC_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    fields = ['product_id','offer_id','merchant_title','current_availability','fresh_missing_required_attrs','proposed_availability','decision_state','selected_for_apply','write_scope_if_approved','rollback_required_before_write']
    with PUBLIC_CSV.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        w.writeheader()
        for r in rows:
            out = {k: r.get(k) for k in fields}
            out['fresh_missing_required_attrs'] = ';'.join(out.get('fresh_missing_required_attrs') or [])
            w.writerow(out)
    lines = [
        '# LK GMC P1-B Availability In-Stock Policy Executor, 2026-05-12', '',
        f"Status: `{payload['status']}`", '',
        '## Aprovação usada',
        '- Lucas respondeu: `Aprovo`.',
        '- Interpretação aplicada: opção recomendada anterior, piloto 25, não todos os 1.616.', '',
        '## Escopo executado',
        f'- Modo: `{mode}`',
        f'- Limite aprovado/aplicado: {limit}',
        '- Campo alterado: `availability` apenas.',
        '- Valor aplicado: `in stock`.',
        '- Regra: GMC deve mostrar disponível mesmo com Tiny zerado.', '',
        '## Resultado',
        f"- Ready total no fresh preflight: {summary.get('ready_total')}",
        f"- Selecionados para apply: {summary.get('selected_for_apply')}",
        f"- Updates com sucesso: {execution_counts.get('updated_availability_in_stock', 0)}",
        f"- Falhas: {execution_counts.get('failed_http_or_validation', 0)}",
        f"- Verificados via products.get como `in stock`: {verify_in_stock}", '',
        '## IDs aplicados/verificados',
    ]
    for r in verified_results:
        lines.append(f"- `{r.get('product_id')}` — exec={r.get('execution_status')} verify={r.get('verify_status')} availability={r.get('availability_after_get') or r.get('availability_after_response')}")
    lines.extend(['', '## Rollback privado', f'- `{rollback_path}`' if rollback_path else '- Não criado no dry-run.', '', '## Não executado'])
    for n in payload['not_performed']:
        lines.append(f'- {n}')
    PUBLIC_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(PUBLIC_MD.read_text(encoding='utf-8'), encoding='utf-8')
    if CONTROL.exists():
        marker = '### 2026-05-12 — GMC P1-B availability in-stock policy pilot apply'
        text = CONTROL.read_text(encoding='utf-8')
        block = (f"\n{marker}\n\n"
                 f"- Status: `{payload['status']}`.\n"
                 f"- Aprovação: Lucas `Aprovo`; interpretado como piloto recomendado de {limit}.\n"
                 f"- Escopo: exact online Merchant IDs; `availability=in stock` apenas; Tiny/Shopify/feed/DB/POS/campanha/sourcing não tocados.\n"
                 f"- Resultado: {execution_counts.get('updated_availability_in_stock', 0)} updates; {verify_in_stock} verificados `in stock`; rollback privado salvo.\n")
        if marker not in text:
            CONTROL.write_text(text.rstrip() + block + '\n', encoding='utf-8')
    if INDEX.exists():
        line = f'| LK GMC P1-B Availability In-Stock Policy Executor 2026-05-12 | `areas/lk/rotinas/gmc-{RUN_STAMP}.md` | Execução aprovada piloto 25: availability=in stock para exact online Merchant IDs; rollback privado e verificação products.get |'
        text = INDEX.read_text(encoding='utf-8')
        if line not in text:
            INDEX.write_text(text.rstrip() + '\n' + line + '\n', encoding='utf-8')
    print(json.dumps({'status': payload['status'], 'summary': payload['summary'], 'public_report': str(PUBLIC_MD), 'private_rollback_snapshot_path': str(rollback_path) if rollback_path else None}, ensure_ascii=False, indent=2))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true', help='Execute Merchant availability writes. Requires explicit Lucas approval.')
    ap.add_argument('--limit', type=int, default=25, help='Pilot apply limit; default 25 because Lucas approved recommended pilot.')
    ap.add_argument('--verify-delay', type=int, default=45, help='Seconds to wait before products.get verification.')
    args = ap.parse_args()
    mode = 'apply' if args.apply else 'dry-run'
    packet = json.loads(INPUT_JSON.read_text(encoding='utf-8'))
    packet_rows = packet.get('samples') or []
    # Use full CSV rows because packet JSON only carries a 25-row sample.
    if len(packet_rows) < packet.get('summary', {}).get('online_rows_missing_availability', 0):
        csv_path = pathlib.Path(packet.get('files', {}).get('public_csv') or '')
        if csv_path.exists():
            with csv_path.open(newline='', encoding='utf-8') as f:
                packet_rows = list(csv.DictReader(f))
    audit = import_audit()
    secrets = audit.load_doppler()
    merchant_id = secrets.get('MERCHANT_CENTER_ID_LK')
    if not merchant_id:
        raise RuntimeError('missing_merchant_center_id')
    token = audit.google_access_token(audit.parse_service_account(secrets))
    products = audit.list_all('products', merchant_id, token)
    statuses = audit.list_all('productstatuses', merchant_id, token)
    rows, summary = build_ready_rows(packet_rows, products, statuses, args.limit)
    execution_results: list[dict[str, Any]] = []
    verified_results: list[dict[str, Any]] = []
    rollback_path = None
    if mode == 'apply':
        execution_results, rollback_path = apply_selected(merchant_id, token, rows, products, args.limit)
        verified_results = verify_results(merchant_id, token, execution_results, args.verify_delay)
    write_outputs(mode, summary, rows, execution_results, verified_results, rollback_path, args.limit)


if __name__ == '__main__':
    main()
