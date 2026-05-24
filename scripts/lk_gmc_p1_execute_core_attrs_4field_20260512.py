#!/usr/bin/env python3
"""LK GMC P1 4-field core attribute executor (dry-run by default).

Lucas chose the conservative scope: prepare execution for title/link/imageLink/price
only, excluding availability because LK stock truth is Tiny.

Default mode is dry-run/preflight only. --apply is intentionally gated and would:
- re-fetch each exact product resource;
- save full rollback snapshots privately with chmod 600;
- update only title/link/imageLink/price for exact online product IDs;
- not touch availability, local rows, Shopify, Tiny, feeds, DB, POS, or campaigns.
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
INPUT_JSON = ROOT / 'reports/lk-gmc-2026-05-12-p1-core-attributes-approval-packet-preview.json'
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
RUN_STAMP = '2026-05-12-p1-core-attrs-4field-executor'
PUBLIC_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
PUBLIC_CSV = ROOT / f'reports/lk-gmc-{RUN_STAMP}.csv'
PUBLIC_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
CONTROL = ROOT / 'areas/lk/projetos/lk-os-implementation-control.md'
INDEX = ROOT / 'empresa/rotinas/_index.md'
TARGET_FIELDS = ['title', 'link', 'imageLink', 'price']
EXCLUDED_FIELDS = ['availability']
REQ_CODES = {'item_missing_required_attribute', 'missing_item_attribute_for_product_type'}


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


def update_product(merchant_id: str, product_id: str, product: dict[str, Any], token: str) -> dict[str, Any]:
    # Content API product writes are upserts through products.insert (POST /products).
    # The previous PUT /products/{productId} path returned 404 in this environment.
    if product.get('offerId') and product_id.split(':', 3)[-1] != product.get('offerId'):
        raise RuntimeError(f'offer_id_mismatch_for_upsert: {product_id}')
    url = f'https://shoppingcontent.googleapis.com/content/v2.1/{merchant_id}/products'
    return request_json(url, token=token, method='POST', payload=product)


def chan(pid: str) -> str:
    return (pid or '').split(':', 1)[0] if ':' in (pid or '') else 'unknown'


def normalize_price(value: Any) -> dict[str, str] | None:
    if isinstance(value, dict) and value.get('value') and value.get('currency'):
        return {'value': str(value['value']), 'currency': str(value['currency'])}
    if isinstance(value, str):
        parts = value.strip().split()
        if len(parts) == 2:
            return {'value': parts[0], 'currency': parts[1]}
    return None


def field_present(product: dict[str, Any], field: str) -> bool:
    if field == 'price':
        p = product.get('price')
        return bool((isinstance(p, dict) and p.get('value')) or p)
    return bool(product.get(field))


def status_missing_attrs(status: dict[str, Any]) -> set[str]:
    out = set()
    for issue in status.get('itemLevelIssues') or []:
        if issue.get('code') in REQ_CODES:
            attr = str(issue.get('attributeName') or '').strip().lower().replace('_', ' ')
            if attr:
                out.add(attr)
    return out


def build_candidates(packet: dict[str, Any]) -> list[dict[str, Any]]:
    rows = []
    for c in packet.get('candidates') or []:
        pid = c.get('product_id') or ''
        proposed_all = c.get('proposed_core_attributes') or {}
        proposed = {k: proposed_all.get(k) for k in TARGET_FIELDS if proposed_all.get(k) not in (None, '', [])}
        if set(proposed.keys()) != set(TARGET_FIELDS):
            rows.append({
                'product_id': pid,
                'offer_id': c.get('offer_id'),
                'decision_state': 'blocked_missing_required_4field_proposal',
                'blocked_reason': 'candidate lacks one or more of title/link/imageLink/price in approval packet',
                'proposed_4field_attributes': proposed,
            })
            continue
        price = normalize_price(proposed.get('price'))
        if not price:
            rows.append({
                'product_id': pid,
                'offer_id': c.get('offer_id'),
                'decision_state': 'blocked_invalid_price_shape',
                'blocked_reason': 'price could not be converted to Content API Price object',
                'proposed_4field_attributes': proposed,
            })
            continue
        proposed['price'] = price
        rows.append({
            'product_id': pid,
            'offer_id': c.get('offer_id'),
            'decision_state': 'candidate_4field_exact_update_preflight',
            'proposed_4field_attributes': proposed,
            'excluded_fields': EXCLUDED_FIELDS,
            'source_packet_evidence': c.get('evidence') or {},
            'write_allowed_now': False,
        })
    return rows


def preflight(candidates: list[dict[str, Any]], products: list[dict[str, Any]], statuses: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    product_by_id = {p.get('id'): p for p in products}
    status_by_id = {s.get('productId'): s for s in statuses}
    rows = []
    counters: Counter[str] = Counter()
    for c in candidates:
        pid = c.get('product_id') or ''
        if c.get('decision_state') != 'candidate_4field_exact_update_preflight':
            rows.append(c)
            counters[c.get('decision_state') or 'blocked_unknown'] += 1
            continue
        if chan(pid) != 'online':
            c['decision_state'] = 'blocked_non_online_product_id'
            c['blocked_reason'] = 'only exact online product IDs are in scope'
            rows.append(c); counters[c['decision_state']] += 1; continue
        product = product_by_id.get(pid)
        status = status_by_id.get(pid) or {}
        if not product:
            c['decision_state'] = 'blocked_product_not_currently_present'
            c['blocked_reason'] = 'fresh Merchant products.list did not include the exact product ID'
            rows.append(c); counters[c['decision_state']] += 1; continue
        missing = status_missing_attrs(status)
        c['fresh_missing_required_attrs'] = sorted(missing)
        c['current_target_field_presence'] = {f: field_present(product, f) for f in TARGET_FIELDS}
        c['current_availability_present'] = field_present(product, 'availability')
        if 'availability' not in missing:
            c['availability_note'] = 'availability no longer reported missing; still excluded by scope'
        else:
            c['availability_note'] = 'availability still missing but intentionally excluded by Lucas option 1 / Tiny stock-truth policy'
        # For direct product PUT, excluding availability may still leave item disapproved or the API may reject the full resource.
        c['api_risk_note'] = 'Direct Content API products.update may reject or keep disapproved rows because availability remains missing; executor is fail-fast and no apply is authorized by dry-run.'
        c['rollback_required_before_write'] = True
        c['rollback_snapshot_path_if_apply'] = str(PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-rollback-APPLY_TIMESTAMP.json')
        c['write_scope_if_approved'] = 'update exact Merchant product resource fields: title, link, imageLink, price only'
        c['decision_state'] = 'ready_for_4field_apply_if_lucas_approves'
        rows.append(c)
        counters[c['decision_state']] += 1
    summary = {
        'fresh_merchant_products_current': len(products),
        'fresh_merchant_productstatuses_current': len(statuses),
        'input_candidates': len(candidates),
        'decision_state_counts': dict(counters),
        'ready_for_4field_apply_if_lucas_approves': counters.get('ready_for_4field_apply_if_lucas_approves', 0),
        'blocked_or_skipped': len(candidates) - counters.get('ready_for_4field_apply_if_lucas_approves', 0),
        'target_fields': TARGET_FIELDS,
        'excluded_fields': EXCLUDED_FIELDS,
        'write_allowed_now': 0,
    }
    return rows, summary


def prepare_updated_product(current: dict[str, Any], proposed: dict[str, Any]) -> dict[str, Any]:
    out = json.loads(json.dumps(current, ensure_ascii=False))
    # Preserve all fields except output-only fields known to be rejected by product writes.
    for k in ['id', 'kind', 'source']:
        out.pop(k, None)
    for k in TARGET_FIELDS:
        out[k] = proposed[k]
    # Explicitly do not set availability in this scope.
    return out


def write_private_snapshot(mode: str, records: list[dict[str, Any]]) -> pathlib.Path | None:
    if mode != 'apply':
        return None
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE_DIR, 0o700)
    path = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-rollback-{datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")}.json'
    payload = {
        'generated_at': utc_now(),
        'scope': 'P1 core attrs 4field exact Merchant product update rollback resources',
        'target_fields': TARGET_FIELDS,
        'excluded_fields': EXCLUDED_FIELDS,
        'rollback_instruction': 'PUT/insert the saved current_product_resource back for each product_id if rollback is needed; verify via products.get and productstatuses after consistency delay.',
        'records': records,
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    os.chmod(path, 0o600)
    return path


def apply_plan(merchant_id: str, token: str, rows: list[dict[str, Any]], current_products: list[dict[str, Any]], limit: int | None) -> tuple[list[dict[str, Any]], pathlib.Path]:
    ready = [r for r in rows if r.get('decision_state') == 'ready_for_4field_apply_if_lucas_approves']
    resumed_success_ids: set[str] = set()
    for progress_file in PRIVATE_DIR.glob(f'lk-gmc-{RUN_STAMP}-progress-*.jsonl'):
        for line in progress_file.read_text(encoding='utf-8').splitlines():
            if not line.strip():
                continue
            try:
                item = json.loads(line)
            except Exception:
                continue
            if item.get('execution_status') == 'updated_4field' and item.get('product_id'):
                resumed_success_ids.add(item['product_id'])
    ready = [r for r in ready if r.get('product_id') not in resumed_success_ids]
    if limit is not None:
        ready = ready[:limit]
    current_by_id = {p.get('id'): p for p in current_products}
    rollback_records = []
    results = []
    # Save a full current product resource for every exact ID before any write.
    # This uses the fresh products.list resources fetched immediately before apply; exact
    # per-ID products.get was too slow/unreliable for the 1,627-row all-apply path.
    for r in ready:
        pid = r['product_id']
        current = current_by_id.get(pid)
        if not current or current.get('id') != pid:
            raise RuntimeError(f'pre_apply_current_resource_missing: {pid}')
        rollback_records.append({'product_id': pid, 'current_product_resource': current, 'planned_update': r})
    private_path = write_private_snapshot('apply', rollback_records)
    assert private_path is not None
    progress_path = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-progress-{private_path.stem.rsplit("-", 1)[-1]}.jsonl'
    os.chmod(PRIVATE_DIR, 0o700)
    # Fail-fast bounded writes. Any HTTP error stops the run and leaves rollback snapshot available.
    with progress_path.open('w', encoding='utf-8') as progress:
        os.chmod(progress_path, 0o600)
        for idx, rec in enumerate(rollback_records, start=1):
            r = rec['planned_update']
            pid = r['product_id']
            body = prepare_updated_product(rec['current_product_resource'], r['proposed_4field_attributes'])
            try:
                updated = update_product(merchant_id, pid, body, token)
                item = {
                    'product_id': pid,
                    'execution_status': 'updated_4field',
                    'updated_field_presence': {f: field_present(updated, f) for f in TARGET_FIELDS},
                    'availability_present_after': field_present(updated, 'availability'),
                }
                results.append(item)
                progress.write(json.dumps(item, ensure_ascii=False) + '\n')
                progress.flush()
            except Exception as e:
                item = {'product_id': pid, 'execution_status': 'failed_http_or_validation', 'error': str(e)[:1200]}
                results.append(item)
                progress.write(json.dumps(item, ensure_ascii=False) + '\n')
                progress.flush()
                break
            if idx % 50 == 0:
                time.sleep(2)
    return results, private_path


def write_outputs(mode: str, summary: dict[str, Any], rows: list[dict[str, Any]], execution_results: list[dict[str, Any]] | None = None, private_path: pathlib.Path | None = None) -> None:
    execution_results = execution_results or []
    public_rows = []
    for r in rows:
        public_rows.append({
            'product_id': r.get('product_id'),
            'offer_id': r.get('offer_id'),
            'decision_state': r.get('decision_state'),
            'target_fields': TARGET_FIELDS,
            'excluded_fields': EXCLUDED_FIELDS,
            'fresh_missing_required_attrs': r.get('fresh_missing_required_attrs'),
            'current_target_field_presence': r.get('current_target_field_presence'),
            'current_availability_present': r.get('current_availability_present'),
            'availability_note': r.get('availability_note'),
            'api_risk_note': r.get('api_risk_note'),
            'blocked_reason': r.get('blocked_reason'),
            'write_allowed_now': False if mode == 'dry-run' else None,
        })
    payload = {
        'generated_at': utc_now(),
        'status': 'gmc_p1_core_attrs_4field_executor_dry_run_ready' if mode == 'dry-run' else 'gmc_p1_core_attrs_4field_executor_apply_finished_or_stopped',
        'mode': mode,
        'scope': 'P1 exact Merchant online products; update title/link/imageLink/price only; availability excluded',
        'source_labels': ['fact_merchant_center', 'fact_shopify_local_snapshot', 'derived_reconciliation', 'manual_approval_required'],
        'summary': summary,
        'execution_results_summary': dict(Counter(r.get('execution_status') for r in execution_results)) if execution_results else {},
        'private_rollback_snapshot_path': str(private_path) if private_path else None,
        'approval_contract': {
            'dry_run_authorizes_apply': False,
            'future_apply_requires_lucas_phrase': 'Aplicar P1 4 campos Merchant agora',
            'target_fields': TARGET_FIELDS,
            'excluded_fields': EXCLUDED_FIELDS,
            'important_risk': 'Because availability remains missing, direct Content API update may reject the product resource or diagnostics may remain partially unresolved. This package intentionally prioritizes stock-truth safety over fully clearing required-attribute diagnostics.',
            'rollback_before_write': 'Full products.get resource snapshot saved privately with chmod 600 before any write in --apply mode.',
        },
        'public_rows': public_rows,
        'execution_results': execution_results,
        'not_performed_in_dry_run': ['merchant_product_update','merchant_product_delete','merchant_product_insert','content_api_custombatch','supplemental_feed_upload','datafeed_fetchNow','feed_update','shopify_write','tiny_write','database_write','pos_or_local_inventory_setting_change','campaign_or_external_send'] if mode == 'dry-run' else [],
    }
    PUBLIC_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    fields = ['product_id','offer_id','decision_state','target_fields','excluded_fields','fresh_missing_required_attrs','current_target_field_presence','current_availability_present','availability_note','api_risk_note','blocked_reason','write_allowed_now']
    with PUBLIC_CSV.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in public_rows:
            out = {k: r.get(k) for k in fields}
            for k in ['target_fields','excluded_fields','fresh_missing_required_attrs']:
                out[k] = ';'.join(out.get(k) or [])
            out['current_target_field_presence'] = json.dumps(out.get('current_target_field_presence') or {}, ensure_ascii=False)
            w.writerow(out)
    lines = [
        '# LK GMC P1 Core Attrs 4-Field Executor Dry-Run, 2026-05-12', '',
        f"Status: `{payload['status']}`", '',
        '## Escopo',
        '- Exact online Merchant product IDs only.',
        '- Campos alvo: `title`, `link`, `imageLink`, `price`.',
        '- Campo excluído: `availability`.',
        '- Motivo da exclusão: Tiny continua sendo verdade de estoque da LK.', '',
        '## Resumo executivo',
        f"- Modo: `{mode}`",
        f"- Candidatos de entrada: {summary.get('input_candidates')}",
        f"- Prontos para apply futuro: {summary.get('ready_for_4field_apply_if_lucas_approves')}",
        f"- Bloqueados/skipped: {summary.get('blocked_or_skipped')}",
        f"- Writes executados neste dry-run: {0 if mode == 'dry-run' else 'ver execution_results'}", '',
        '## Risco técnico antes do apply',
        '- Como `availability` continua fora do escopo, a Content API pode rejeitar um `products.update` direto ou manter o diagnóstico parcialmente aberto. O executor é fail-fast e cria rollback antes de qualquer write em `--apply`.', '',
        '## Não executado no dry-run',
    ]
    if mode == 'dry-run':
        for n in payload['not_performed_in_dry_run']:
            lines.append(f'- {n}')
    else:
        lines.append('- Ver JSON para execution_results; rollback privado foi criado antes dos writes.')
    lines.extend(['', '## Arquivos', f'- JSON: `{PUBLIC_JSON}`', f'- CSV: `{PUBLIC_CSV}`'])
    if private_path:
        lines.append(f'- Rollback privado: `{private_path}`')
    PUBLIC_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(PUBLIC_MD.read_text(encoding='utf-8'), encoding='utf-8')

    if CONTROL.exists():
        marker = '### 2026-05-12 — GMC P1 core attrs 4-field executor dry-run'
        text = CONTROL.read_text(encoding='utf-8')
        block = (f"\n{marker}\n\n"
                 f"- Status: {payload['status']}.\n"
                 f"- Scope: exact online IDs; campos title/link/imageLink/price; availability excluída.\n"
                 f"- Dry-run prontos para apply futuro: {summary.get('ready_for_4field_apply_if_lucas_approves')}; bloqueados/skipped={summary.get('blocked_or_skipped')}.\n"
                 f"- Nenhum write executado no dry-run; apply exige aprovação explícita e snapshot privado chmod 600.\n\n")
        if marker not in text:
            CONTROL.write_text(text.rstrip() + block, encoding='utf-8')
    if INDEX.exists():
        line = f'| LK GMC P1 Core Attrs 4-Field Executor Dry-Run 2026-05-12 | `areas/lk/rotinas/gmc-{RUN_STAMP}.md` | Executor dry-run para Merchant title/link/imageLink/price por exact product ID, excluindo availability por Tiny stock truth; apply exige aprovação |'
        text = INDEX.read_text(encoding='utf-8')
        if line not in text:
            INDEX.write_text(text.rstrip() + '\n' + line + '\n', encoding='utf-8')
    print(json.dumps({'status': payload['status'], 'mode': mode, 'summary': summary, 'public_report': str(PUBLIC_MD), 'private_rollback_snapshot_path': str(private_path) if private_path else None}, ensure_ascii=False, indent=2))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true', help='Execute Merchant updates. Requires explicit Lucas approval outside this script.')
    ap.add_argument('--limit', type=int, default=None, help='Optional apply limit for a small fail-fast batch.')
    args = ap.parse_args()
    mode = 'apply' if args.apply else 'dry-run'

    packet = json.loads(INPUT_JSON.read_text(encoding='utf-8'))
    candidates = build_candidates(packet)
    audit = import_audit()
    secrets = audit.load_doppler()
    merchant_id = secrets.get('MERCHANT_CENTER_ID_LK')
    if not merchant_id:
        raise RuntimeError('missing_merchant_center_id')
    token = audit.google_access_token(audit.parse_service_account(secrets))
    products = audit.list_all('products', merchant_id, token)
    statuses = audit.list_all('productstatuses', merchant_id, token)
    rows, summary = preflight(candidates, products, statuses)
    execution_results: list[dict[str, Any]] = []
    private_path = None
    if mode == 'apply':
        execution_results, private_path = apply_plan(merchant_id, token, rows, products, args.limit)
        summary['execution_results_summary'] = dict(Counter(r.get('execution_status') for r in execution_results))
        summary['apply_limit'] = args.limit
    write_outputs(mode, summary, rows, execution_results, private_path)


if __name__ == '__main__':
    main()
