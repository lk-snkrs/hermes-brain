#!/usr/bin/env python3
"""GMC P1 Wave3 high-confidence color-tag executor.

Default dry-run only. Scope is the tiny high-confidence bucket where fresh GMC
required-attribute diagnostics still flag `color` and the local Shopify snapshot
has an explicit `color:*` tag. Apply requires exact inline approval and writes a
private rollback snapshot before any Merchant upsert.
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
PREVIEW_JSON = ROOT / 'reports/lk-gmc-2026-05-13-p1-attribute-remaining-wave3-preview.json'
RUN_STAMP = '2026-05-13-p1-attribute-wave3-color-tag-executor'
PUBLIC_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
PUBLIC_CSV = ROOT / f'reports/lk-gmc-{RUN_STAMP}.csv'
PUBLIC_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
REQ_CODES = {'item_missing_required_attribute', 'missing_item_attribute_for_product_type'}
APPROVAL_TEXT_REQUIRED = 'Lucas approved GMC P1 Attribute Wave3 color-tag apply'


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
    last = ''
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
            last = f'http_{e.code}: {raw[:1200]}'
            if e.code not in {429, 500, 502, 503, 504} or attempt == max_attempts:
                raise RuntimeError(last) from e
            time.sleep(min(60, 2 ** attempt))
        except Exception as e:
            last = str(e)[:1200]
            if attempt == max_attempts:
                raise RuntimeError(last) from e
            time.sleep(min(60, 2 ** attempt))
    raise RuntimeError(last or 'request_failed')


def product_url(mid: str, pid: str) -> str:
    return f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/products/{urllib.parse.quote(pid, safe="")}'


def get_product(mid: str, pid: str, token: str) -> dict[str, Any]:
    return request_json(product_url(mid, pid), token=token)


def upsert_product(mid: str, product: dict[str, Any], token: str) -> dict[str, Any]:
    return request_json(f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/products', token=token, method='POST', payload=product)


def norm_attr(value: Any) -> str:
    return str(value or '').strip().lower().replace('_', ' ')


def required_attrs(status: dict[str, Any] | None) -> set[str]:
    out = set()
    for issue in (status or {}).get('itemLevelIssues') or []:
        if issue.get('code') in REQ_CODES:
            a = norm_attr(issue.get('attributeName'))
            if a:
                out.add(a)
    return out


def load_preview_rows() -> list[dict[str, Any]]:
    data = json.loads(PREVIEW_JSON.read_text(encoding='utf-8'))
    rows = [r for r in data.get('rows') or [] if r.get('decision_state') == 'candidate_wave3_color_tag_high_confidence']
    rows.sort(key=lambda r: r.get('product_id') or '')
    return rows


def build_rows(candidates: list[dict[str, Any]], products: list[dict[str, Any]], statuses: list[dict[str, Any]], limit: int) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    p_by_id = {p.get('id'): p for p in products}
    s_by_id = {s.get('productId'): s for s in statuses}
    rows = []
    counters = Counter()
    for c in candidates:
        pid = c.get('product_id')
        prod = p_by_id.get(pid)
        stat = s_by_id.get(pid)
        fresh = required_attrs(stat)
        sugg = c.get('suggested_attributes') or {}
        evidence = c.get('evidence') or {}
        decision = 'ready_for_wave3_color_tag_apply_if_lucas_approves'
        reasons = []
        if not prod:
            decision = 'blocked_product_not_currently_present'; reasons.append('fresh product missing')
        elif 'color' not in fresh:
            decision = 'skipped_not_freshly_missing_color'; reasons.append('fresh status does not flag color')
        elif prod.get('color'):
            decision = 'skipped_color_already_present'; reasons.append('product already has color')
        elif set(sugg.keys()) != {'color'} or not sugg.get('color'):
            decision = 'blocked_suggestion_not_color_only'; reasons.append('suggestion not color-only')
        elif evidence.get('color') != 'shopify_tag_color':
            decision = 'blocked_not_shopify_tag_evidence'; reasons.append('evidence is not explicit Shopify color tag')
        else:
            reasons.append('fresh color diagnostic + explicit Shopify color tag')
        counters[decision] += 1
        rows.append({
            'product_id': pid,
            'merchant_title': prod.get('title') if prod else c.get('merchant_title'),
            'fresh_required_attrs': sorted(fresh),
            'current_color': prod.get('color') if prod else None,
            'suggested_color': sugg.get('color'),
            'evidence': evidence,
            'decision_state': decision,
            'decision_reasons': reasons,
            'selected_for_apply': False,
            'write_scope_if_approved': 'color only, exact online Merchant product resource, products.insert upsert',
            'rollback_required_before_write': True,
        })
    ready = [r for r in rows if r['decision_state'] == 'ready_for_wave3_color_tag_apply_if_lucas_approves']
    selected = {r['product_id'] for r in ready[:limit]}
    for r in rows:
        r['selected_for_apply'] = r['product_id'] in selected
    return rows, {
        'preview_candidates': len(candidates),
        'fresh_merchant_products_current': len(products),
        'fresh_merchant_productstatuses_current': len(statuses),
        'decision_state_counts': dict(counters),
        'ready_total': len(ready),
        'selected_for_apply_if_approved': len(selected),
        'target_fields': ['color'],
        'limit': limit,
        'write_allowed_now': 0,
    }


def prepare_product(current: dict[str, Any], row: dict[str, Any]) -> dict[str, Any]:
    out = json.loads(json.dumps(current, ensure_ascii=False))
    for k in ['id', 'kind', 'source']:
        out.pop(k, None)
    out['color'] = row['suggested_color']
    return out


def snapshot(records: list[dict[str, Any]], limit: int) -> pathlib.Path:
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE_DIR, 0o700)
    path = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-rollback-{datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")}.json'
    path.write_text(json.dumps({'generated_at': utc_now(), 'scope': f'Wave3 color-tag apply limit={limit}; update color only', 'approval_text_required': APPROVAL_TEXT_REQUIRED, 'rollback_instruction': 'Use products.insert/upsert with current_product_resource; verify after delay.', 'records': records}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    os.chmod(path, 0o600)
    return path


def apply_selected(mid: str, token: str, rows: list[dict[str, Any]], products: list[dict[str, Any]], limit: int) -> tuple[list[dict[str, Any]], pathlib.Path]:
    current = {p.get('id'): p for p in products}
    records = []
    for r in [x for x in rows if x.get('selected_for_apply')]:
        cur = current.get(r['product_id'])
        if not cur:
            raise RuntimeError('pre_apply_current_resource_missing: ' + str(r['product_id']))
        records.append({'product_id': r['product_id'], 'current_product_resource': cur, 'planned_update': r})
    rollback = snapshot(records, limit)
    results = []
    progress = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-progress-{rollback.stem.rsplit("-", 1)[-1]}.jsonl'
    with progress.open('w', encoding='utf-8') as f:
        os.chmod(progress, 0o600)
        for rec in records:
            r = rec['planned_update']
            try:
                updated = upsert_product(mid, prepare_product(rec['current_product_resource'], r), token)
                item = {'product_id': r['product_id'], 'execution_status': 'updated_color', 'color_after_response': updated.get('color')}
            except Exception as e:
                item = {'product_id': r['product_id'], 'execution_status': 'failed_http_or_validation', 'error': str(e)[:1200]}
                results.append(item); f.write(json.dumps(item, ensure_ascii=False) + '\n'); f.flush(); break
            results.append(item); f.write(json.dumps(item, ensure_ascii=False) + '\n'); f.flush(); time.sleep(0.2)
    return results, rollback


def verify(mid: str, token: str, rows: list[dict[str, Any]], results: list[dict[str, Any]], delay: int) -> list[dict[str, Any]]:
    if delay:
        time.sleep(delay)
    byid = {r['product_id']: r for r in rows}
    out = []
    for res in results:
        pid = res.get('product_id'); r = byid.get(pid, {})
        if res.get('execution_status') != 'updated_color' or not pid:
            out.append({**res, 'verify_status': 'not_verified_due_to_execution_status'}); continue
        try:
            prod = get_product(mid, pid, token)
            ok = prod.get('color') == r.get('suggested_color')
            out.append({**res, 'verify_status': 'verified_product_get', 'color_after_get': prod.get('color'), 'attrs_match_expected': ok})
        except Exception as e:
            out.append({**res, 'verify_status': 'verify_failed', 'verify_error': str(e)[:1200]})
    return out


def write_outputs(mode: str, summary: dict[str, Any], rows: list[dict[str, Any]], exec_results: list[dict[str, Any]], verified: list[dict[str, Any]], rollback: pathlib.Path | None) -> None:
    ec = Counter(r.get('execution_status') for r in exec_results)
    vc = Counter(r.get('verify_status') for r in verified)
    matched = sum(1 for r in verified if r.get('attrs_match_expected'))
    payload = {
        'generated_at': utc_now(),
        'status': 'gmc_p1_attribute_wave3_color_tag_apply_verified' if mode == 'apply' else 'gmc_p1_attribute_wave3_color_tag_dry_run_ready',
        'mode': mode,
        'scope': 'Wave3 high-confidence color-tag bucket; color only; exact online IDs.',
        'source_labels': ['fact_merchant_center', 'fact_shopify_local_snapshot', 'derived_reconciliation'],
        'approval_required_for_apply': APPROVAL_TEXT_REQUIRED,
        'summary': {**summary, 'execution_results_summary': dict(ec), 'verify_results_summary': dict(vc), 'verified_attrs_match_expected': matched},
        'private_rollback_snapshot_path': str(rollback) if rollback else None,
        'public_rows': rows,
        'execution_results': exec_results,
        'verified_results': verified,
        'not_performed': ['merchant_write' if mode != 'apply' else 'merchant_delete', 'merchant_delete', 'merchant_price_title_link_image_availability_update', 'feed_update_or_fetch', 'shopify_write', 'tiny_call_or_write', 'database_write', 'pos_or_local_inventory_write', 'klaviyo_or_whatsapp_send', 'notion_or_n8n_write', 'loyalty_or_judgeme_action'],
    }
    PUBLIC_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    fields = ['product_id','merchant_title','fresh_required_attrs','current_color','suggested_color','evidence','decision_state','selected_for_apply','decision_reasons','write_scope_if_approved','rollback_required_before_write']
    with PUBLIC_CSV.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        w.writeheader()
        for r in rows:
            out = {k: r.get(k) for k in fields}
            out['fresh_required_attrs'] = '; '.join(out.get('fresh_required_attrs') or [])
            out['decision_reasons'] = '; '.join(out.get('decision_reasons') or [])
            out['evidence'] = json.dumps(out.get('evidence') or {}, ensure_ascii=False)
            w.writerow(out)
    lines = [
        '# LK GMC P1 Attribute Completion — Wave3 Color Tag Executor, 2026-05-13', '',
        f"Status: `{payload['status']}`", '',
        '## Escopo', f'- Modo: `{mode}`', '- Bucket: `candidate_wave3_color_tag_high_confidence`.', '- Campo alvo: `color` apenas.', '- Evidência exigida: tag Shopify explícita `color:*`.', '- Apply produtivo: bloqueado até aprovação inline específica.', '',
        '## Resultado do preflight', f"- Preview candidates: {summary['preview_candidates']}", f"- Ready: {summary['ready_total']}", f"- Selecionados se aprovado: {summary['selected_for_apply_if_approved']}", '', '## Estados'
    ]
    for k, v in sorted(summary['decision_state_counts'].items()):
        lines.append(f'- {k}: {v}')
    lines.extend(['', '## IDs selecionados'])
    for r in [x for x in rows if x.get('selected_for_apply')]:
        lines.append(f"- `{r['product_id']}` — {r.get('merchant_title')} — color={r.get('suggested_color')}")
    lines.extend(['', '## Aprovação necessária para apply futuro', f'- Texto exato requerido pelo executor: `{APPROVAL_TEXT_REQUIRED}`', '- Scope: aplicar `color` apenas nesses IDs high-confidence, com rollback privado antes do write e verificação via `products.get`.', '', '## Rollback privado', f'- `{rollback}`' if rollback else '- Não criado no dry-run; será criado imediatamente antes de qualquer apply.', '', '## Não executado'])
    for n in payload['not_performed']:
        lines.append(f'- {n}')
    PUBLIC_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(PUBLIC_MD.read_text(encoding='utf-8'), encoding='utf-8')
    print(json.dumps({'status': payload['status'], 'mode': mode, 'summary': payload['summary'], 'public_report': str(PUBLIC_MD), 'private_rollback_snapshot_path': str(rollback) if rollback else None}, ensure_ascii=False, indent=2))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--approval-text', default='')
    ap.add_argument('--limit', type=int, default=25)
    ap.add_argument('--verify-delay', type=int, default=90)
    args = ap.parse_args()
    mode = 'apply' if args.apply else 'dry-run'
    if args.apply and args.approval_text != APPROVAL_TEXT_REQUIRED:
        raise RuntimeError(f'apply_blocked_missing_exact_approval_text: {APPROVAL_TEXT_REQUIRED}')
    audit = import_audit()
    secrets = audit.load_doppler()
    mid = secrets.get('MERCHANT_CENTER_ID_LK')
    if not mid:
        raise RuntimeError('missing_merchant_center_id')
    token = audit.google_access_token(audit.parse_service_account(secrets))
    products = audit.list_all('products', mid, token)
    statuses = audit.list_all('productstatuses', mid, token)
    rows, summary = build_rows(load_preview_rows(), products, statuses, args.limit)
    exec_results = []
    verified = []
    rollback = None
    if mode == 'apply':
        exec_results, rollback = apply_selected(mid, token, rows, products, args.limit)
        verified = verify(mid, token, rows, exec_results, args.verify_delay)
    write_outputs(mode, summary, rows, exec_results, verified, rollback)


if __name__ == '__main__':
    main()
