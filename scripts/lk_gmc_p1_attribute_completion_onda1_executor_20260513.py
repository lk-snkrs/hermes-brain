#!/usr/bin/env python3
"""LK GMC P1 attribute completion Onda 1 executor/dry-run.

Default mode is dry-run only. It re-fetches Merchant Center products/statuses,
selects exact online product IDs from the 2026-05-13 packet v2 Onda 1
(high-confidence size-only rows), and prepares the exact fields that would be
upserted if Lucas later approves an apply.

No Merchant writes happen unless --apply is passed with an explicit approval
text. Even then, the script writes private rollback snapshots before touching
any product and updates only the approved attribute fields.
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
INPUT_JSON = ROOT / 'reports/lk-gmc-p1-attribute-completion-packet-v2-2026-05-13.json'
RUN_STAMP = '2026-05-13-p1-attribute-completion-onda1-executor'
PUBLIC_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
PUBLIC_CSV = ROOT / f'reports/lk-gmc-{RUN_STAMP}.csv'
PUBLIC_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
CONTROL = ROOT / 'areas/lk/projetos/lk-os-implementation-control.md'
INDEX = ROOT / 'empresa/rotinas/_index.md'
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
REQ_CODES = {'item_missing_required_attribute', 'missing_item_attribute_for_product_type'}
ONDA1_STATE = 'candidate_high_confidence_attr_preview'
APPROVAL_TEXT_REQUIRED = 'Lucas approved GMC P1 Attribute Onda 1 apply'


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


def channel(pid: str) -> str:
    return (pid or '').split(':', 1)[0] if ':' in (pid or '') else 'unknown'


def missing_required_attrs(status: dict[str, Any]) -> set[str]:
    out = set()
    for issue in status.get('itemLevelIssues') or []:
        if issue.get('code') in REQ_CODES:
            attr = str(issue.get('attributeName') or '').strip().lower().replace('_', ' ')
            if attr:
                out.add(attr)
    return out


def normalize_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(x).strip() for x in value if str(x).strip()]
    text = str(value).strip()
    return [text] if text else []


def load_onda1_candidates() -> list[dict[str, Any]]:
    packet = json.loads(INPUT_JSON.read_text(encoding='utf-8'))
    rows = [r for r in packet.get('candidates') or [] if r.get('decision_state') == ONDA1_STATE]
    rows.sort(key=lambda r: r.get('product_id') or '')
    return rows


def prepare_updated_product(current: dict[str, Any], suggested: dict[str, Any]) -> dict[str, Any]:
    out = json.loads(json.dumps(current, ensure_ascii=False))
    for k in ['id', 'kind', 'source']:
        out.pop(k, None)
    for field in ['sizes', 'ageGroup', 'gender', 'color']:
        if field in suggested:
            out[field] = suggested[field]
    return out


def build_rows(candidates: list[dict[str, Any]], products: list[dict[str, Any]], statuses: list[dict[str, Any]], limit: int) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    product_by_id = {p.get('id'): p for p in products}
    status_by_id = {s.get('productId'): s for s in statuses}
    counters: Counter[str] = Counter()
    rows: list[dict[str, Any]] = []
    seen: set[str] = set()
    for c in candidates:
        pid = c.get('product_id') or ''
        if pid in seen:
            counters['blocked_duplicate_candidate_id'] += 1
            continue
        seen.add(pid)
        product = product_by_id.get(pid)
        status = status_by_id.get(pid) or {}
        fresh_missing = missing_required_attrs(status)
        suggested = c.get('suggested_attributes') or {}
        suggested_sizes = normalize_list(suggested.get('sizes'))
        current_sizes = normalize_list(product.get('sizes')) if product else []
        expected_missing = set(c.get('missing_attributes') or [])
        if channel(pid) != 'online':
            decision = 'blocked_non_online_product_id'
        elif not product:
            decision = 'blocked_product_not_currently_present'
        elif c.get('decision_state') != ONDA1_STATE:
            decision = 'blocked_not_onda1_high_confidence'
        elif expected_missing != {'size'} or set(suggested.keys()) != {'sizes'}:
            decision = 'blocked_not_size_only_scope'
        elif not suggested_sizes:
            decision = 'blocked_missing_suggested_size'
        elif current_sizes and current_sizes != suggested_sizes:
            decision = 'needs_review_existing_size_conflict'
        elif 'size' not in fresh_missing and current_sizes == suggested_sizes:
            decision = 'skipped_already_corrected_size_present'
        elif 'size' not in fresh_missing and not current_sizes:
            decision = 'needs_review_status_not_currently_missing_size'
        else:
            decision = 'ready_for_onda1_size_apply_if_lucas_approves'
        counters[decision] += 1
        rows.append({
            'product_id': pid,
            'offer_id': c.get('offer_id'),
            'merchant_title': product.get('title') if product else c.get('merchant_title'),
            'shopify_product_title': c.get('shopify_product_title'),
            'shopify_variant_title': c.get('shopify_variant_title'),
            'current_sizes': current_sizes,
            'fresh_missing_required_attrs': sorted(fresh_missing),
            'missing_attributes_from_packet': c.get('missing_attributes') or [],
            'suggested_sizes': suggested_sizes,
            'decision_state': decision,
            'selected_for_apply': False,
            'write_scope_if_approved': 'sizes only, exact online Merchant product resource, products.insert upsert',
            'rollback_required_before_write': True,
        })
    ready = [r for r in rows if r['decision_state'] == 'ready_for_onda1_size_apply_if_lucas_approves']
    selected_ids = {r['product_id'] for r in ready[:limit]}
    for r in rows:
        r['selected_for_apply'] = r['product_id'] in selected_ids
    summary = {
        'candidate_rows_onda1': len(candidates),
        'fresh_merchant_products_current': len(products),
        'fresh_merchant_productstatuses_current': len(statuses),
        'decision_state_counts': dict(counters),
        'ready_total': len(ready),
        'selected_for_apply_if_approved': len(selected_ids),
        'target_fields': ['sizes'],
        'limit': limit,
        'write_allowed_now': 0,
    }
    return rows, summary


def write_private_snapshot(records: list[dict[str, Any]], limit: int) -> pathlib.Path:
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE_DIR, 0o700)
    path = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-rollback-{datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")}.json'
    payload = {
        'generated_at': utc_now(),
        'scope': f'P1 attribute completion Onda 1 apply limit={limit}; update sizes only for exact online Merchant product IDs',
        'approval_text_required': APPROVAL_TEXT_REQUIRED,
        'rollback_instruction': 'Use products.insert/upsert with current_product_resource for each product_id to restore; verify after consistency delay.',
        'records': records,
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    os.chmod(path, 0o600)
    return path


def apply_selected(merchant_id: str, token: str, rows: list[dict[str, Any]], products: list[dict[str, Any]], limit: int) -> tuple[list[dict[str, Any]], pathlib.Path]:
    current_by_id = {p.get('id'): p for p in products}
    selected = [r for r in rows if r.get('selected_for_apply')]
    rollback_records = []
    for r in selected:
        current = current_by_id.get(r['product_id'])
        if not current or current.get('id') != r['product_id']:
            raise RuntimeError(f'pre_apply_current_resource_missing: {r["product_id"]}')
        rollback_records.append({'product_id': r['product_id'], 'current_product_resource': current, 'planned_update': r})
    rollback_path = write_private_snapshot(rollback_records, limit=limit)
    progress_path = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-progress-{rollback_path.stem.rsplit("-", 1)[-1]}.jsonl'
    results: list[dict[str, Any]] = []
    with progress_path.open('w', encoding='utf-8') as progress:
        os.chmod(progress_path, 0o600)
        for rec in rollback_records:
            planned = rec['planned_update']
            body = prepare_updated_product(rec['current_product_resource'], {'sizes': planned['suggested_sizes']})
            try:
                updated = upsert_product(merchant_id, body, token)
                item = {'product_id': planned['product_id'], 'execution_status': 'updated_sizes', 'sizes_after_response': updated.get('sizes')}
            except Exception as e:
                item = {'product_id': planned['product_id'], 'execution_status': 'failed_http_or_validation', 'error': str(e)[:1200]}
                results.append(item)
                progress.write(json.dumps(item, ensure_ascii=False) + '\n')
                progress.flush()
                break
            results.append(item)
            progress.write(json.dumps(item, ensure_ascii=False) + '\n')
            progress.flush()
            time.sleep(0.2)
    return results, rollback_path


def verify_results(merchant_id: str, token: str, rows: list[dict[str, Any]], results: list[dict[str, Any]], delay: int) -> list[dict[str, Any]]:
    if delay:
        time.sleep(delay)
    row_by_id = {r['product_id']: r for r in rows}
    verified = []
    for r in results:
        pid = r.get('product_id')
        expected = row_by_id.get(pid, {}).get('suggested_sizes') or []
        if r.get('execution_status') != 'updated_sizes' or not pid:
            verified.append({**r, 'verify_status': 'not_verified_due_to_execution_status'})
            continue
        try:
            prod = get_product(merchant_id, pid, token)
            actual = normalize_list(prod.get('sizes'))
            verified.append({**r, 'verify_status': 'verified_product_get', 'sizes_after_get': actual, 'sizes_match_expected': actual == expected})
        except Exception as e:
            verified.append({**r, 'verify_status': 'verify_failed', 'verify_error': str(e)[:1200]})
    return verified


def write_outputs(mode: str, summary: dict[str, Any], rows: list[dict[str, Any]], execution_results: list[dict[str, Any]], verified_results: list[dict[str, Any]], rollback_path: pathlib.Path | None, limit: int) -> None:
    execution_counts = Counter(r.get('execution_status') for r in execution_results)
    verify_counts = Counter(r.get('verify_status') for r in verified_results)
    verify_match = sum(1 for r in verified_results if r.get('sizes_match_expected'))
    payload = {
        'generated_at': utc_now(),
        'status': 'gmc_p1_attribute_completion_onda1_apply_verified' if mode == 'apply' else 'gmc_p1_attribute_completion_onda1_executor_dry_run_ready',
        'mode': mode,
        'scope': 'Onda 1 high-confidence only; exact online Merchant product IDs; update sizes only if later approved.',
        'source_labels': ['fact_merchant_center', 'fact_shopify_local_snapshot', 'derived_reconciliation'],
        'approval_required_for_apply': APPROVAL_TEXT_REQUIRED,
        'summary': {**summary, 'execution_results_summary': dict(execution_counts), 'verify_results_summary': dict(verify_counts), 'verified_sizes_match_expected': verify_match},
        'private_rollback_snapshot_path': str(rollback_path) if rollback_path else None,
        'public_rows': rows,
        'execution_results': execution_results,
        'verified_results': verified_results,
        'not_performed': ['merchant_write' if mode != 'apply' else 'merchant_delete', 'merchant_delete', 'merchant_price_title_link_image_update', 'availability_update', 'feed_update_or_fetch', 'shopify_write', 'tiny_call_or_write', 'database_write', 'pos_or_local_inventory_write', 'klaviyo_or_whatsapp_send', 'notion_or_n8n_write', 'loyalty_or_judgeme_action'],
    }
    PUBLIC_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    fields = ['product_id','offer_id','merchant_title','shopify_variant_title','current_sizes','fresh_missing_required_attrs','missing_attributes_from_packet','suggested_sizes','decision_state','selected_for_apply','write_scope_if_approved','rollback_required_before_write']
    with PUBLIC_CSV.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        w.writeheader()
        for r in rows:
            out = {k: r.get(k) for k in fields}
            for k in ['current_sizes', 'fresh_missing_required_attrs', 'missing_attributes_from_packet', 'suggested_sizes']:
                out[k] = ';'.join(out.get(k) or [])
            w.writerow(out)
    lines = [
        '# LK GMC P1 Attribute Completion — Onda 1 Executor, 2026-05-13', '',
        f"Status: `{payload['status']}`", '',
        '## Escopo',
        f'- Modo: `{mode}`',
        '- Onda: 1 high-confidence do packet v2.',
        '- Campo alvo: `sizes` apenas.',
        '- Canal: `online` apenas.',
        '- Apply produtivo: bloqueado até aprovação inline específica.', '',
        '## Resultado do preflight',
        f"- Candidatos Onda 1 no packet: {summary.get('candidate_rows_onda1')}",
        f"- Merchant products atuais consultados: {summary.get('fresh_merchant_products_current')}",
        f"- Productstatuses atuais consultados: {summary.get('fresh_merchant_productstatuses_current')}",
        f"- Ready para apply futuro: {summary.get('ready_total')}",
        f"- Selecionados pelo limite atual se aprovado: {summary.get('selected_for_apply_if_approved')}", '',
        '## Estados',
    ]
    for key, val in sorted(summary.get('decision_state_counts', {}).items()):
        lines.append(f'- {key}: {val}')
    lines.extend(['', '## Amostra ready'])
    for r in [x for x in rows if x['decision_state'] == 'ready_for_onda1_size_apply_if_lucas_approves'][:12]:
        lines.append(f"- `{r['product_id']}` — {r.get('merchant_title')} — sizes {r.get('current_sizes') or []} → {r.get('suggested_sizes')}")
    lines.extend(['', '## Aprovação necessária para apply futuro', f'- Texto exato requerido pelo executor: `{APPROVAL_TEXT_REQUIRED}`', '- Recomendação operacional: se aprovar, rodar primeiro com limite pequeno/fail-fast e verificar `products.get` antes de escalar.', '', '## Rollback privado'])
    lines.append(f'- `{rollback_path}`' if rollback_path else '- Não criado no dry-run; será criado antes de qualquer apply.')
    lines.extend(['', '## Não executado'])
    for n in payload['not_performed']:
        lines.append(f'- {n}')
    PUBLIC_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(PUBLIC_MD.read_text(encoding='utf-8'), encoding='utf-8')
    if CONTROL.exists():
        marker = '### 2026-05-13 — GMC P1 attribute completion Onda 1 dry-run executor'
        text = CONTROL.read_text(encoding='utf-8')
        block = (f"\n{marker}\n\n"
                 f"- Status: `{payload['status']}`.\n"
                 f"- Escopo: Onda 1 high-confidence do packet v2; exact online Merchant IDs; `sizes` apenas.\n"
                 f"- Resultado dry-run: {summary.get('ready_total')} ready; {summary.get('selected_for_apply_if_approved')} selecionados pelo limite atual; nenhum Merchant/Shopify/Tiny/feed/write executado.\n"
                 f"- Apply futuro exige aprovação inline: `{APPROVAL_TEXT_REQUIRED}`.\n")
        if marker not in text:
            CONTROL.write_text(text.rstrip() + block + '\n', encoding='utf-8')
    if INDEX.exists():
        line = f'| LK GMC P1 Attribute Completion Onda 1 Executor 2026-05-13 | `areas/lk/rotinas/gmc-{RUN_STAMP}.md` | Dry-run/executor Onda 1 high-confidence: exact online IDs, sizes only, apply bloqueado por aprovação inline |'
        text = INDEX.read_text(encoding='utf-8')
        if line not in text:
            INDEX.write_text(text.rstrip() + '\n' + line + '\n', encoding='utf-8')
    print(json.dumps({'status': payload['status'], 'mode': mode, 'summary': payload['summary'], 'public_report': str(PUBLIC_MD), 'private_rollback_snapshot_path': str(rollback_path) if rollback_path else None}, ensure_ascii=False, indent=2))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true', help='Execute Merchant sizes writes. Requires explicit Lucas approval text.')
    ap.add_argument('--approval-text', default='', help='Required exact text for apply safety gate.')
    ap.add_argument('--limit', type=int, default=60, help='Max Onda 1 rows to select/apply if approved.')
    ap.add_argument('--verify-delay', type=int, default=45, help='Seconds to wait before products.get verification after apply.')
    args = ap.parse_args()
    mode = 'apply' if args.apply else 'dry-run'
    if args.apply and args.approval_text != APPROVAL_TEXT_REQUIRED:
        raise RuntimeError(f'apply_blocked_missing_exact_approval_text: {APPROVAL_TEXT_REQUIRED}')
    candidates = load_onda1_candidates()
    audit = import_audit()
    secrets = audit.load_doppler()
    merchant_id = secrets.get('MERCHANT_CENTER_ID_LK')
    if not merchant_id:
        raise RuntimeError('missing_merchant_center_id')
    token = audit.google_access_token(audit.parse_service_account(secrets))
    products = audit.list_all('products', merchant_id, token)
    statuses = audit.list_all('productstatuses', merchant_id, token)
    rows, summary = build_rows(candidates, products, statuses, args.limit)
    execution_results: list[dict[str, Any]] = []
    verified_results: list[dict[str, Any]] = []
    rollback_path = None
    if mode == 'apply':
        execution_results, rollback_path = apply_selected(merchant_id, token, rows, products, args.limit)
        verified_results = verify_results(merchant_id, token, rows, execution_results, args.verify_delay)
    write_outputs(mode, summary, rows, execution_results, verified_results, rollback_path, args.limit)


if __name__ == '__main__':
    main()
