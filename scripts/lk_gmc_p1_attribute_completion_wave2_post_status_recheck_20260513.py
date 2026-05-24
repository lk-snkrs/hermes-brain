#!/usr/bin/env python3
"""Read-only post-status recheck after GMC P1 Attribute Completion Onda 2 scale apply.

No Merchant writes. Fetches fresh products/productstatuses, verifies Onda 1 + Onda 2
applied IDs against current diagnostics, and writes sanitized local reports.
"""
from __future__ import annotations

import csv
import importlib.util
import json
import pathlib
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / 'scripts/lk_gmc_catalog_duplication_audit_20260512.py'
WAVE2_EXEC_JSON = ROOT / 'reports/lk-gmc-2026-05-13-p1-attribute-completion-wave2-pilot-executor.json'
ONDA1_EXEC_JSON = ROOT / 'reports/lk-gmc-2026-05-13-p1-attribute-completion-onda1-executor.json'
PACKET_JSON = ROOT / 'reports/lk-gmc-p1-attribute-completion-packet-v2-2026-05-13.json'
RUN_STAMP = '2026-05-13-p1-attribute-wave2-post-status-recheck'
OUT_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
OUT_CSV = ROOT / f'reports/lk-gmc-{RUN_STAMP}-remaining-wave2.csv'
OUT_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
CONTROL = ROOT / 'areas/lk/projetos/lk-os-implementation-control.md'
INDEX = ROOT / 'empresa/rotinas/_index.md'
REQ_CODES = {'item_missing_required_attribute', 'missing_item_attribute_for_product_type'}
TARGET_ATTRS = {'size', 'age group', 'gender'}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def import_audit():
    spec = importlib.util.spec_from_file_location('audit', AUDIT_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


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


def all_issue_counts(statuses: list[dict[str, Any]]) -> tuple[Counter, Counter, int]:
    codes = Counter()
    req_attrs = Counter()
    total = 0
    for s in statuses:
        for issue in s.get('itemLevelIssues') or []:
            total += 1
            code = issue.get('code') or 'unknown'
            codes[code] += 1
            if code in REQ_CODES:
                a = norm_attr(issue.get('attributeName')) or 'unknown'
                req_attrs[a] += 1
    return codes, req_attrs, total


def load_selected(path: pathlib.Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding='utf-8'))
    return [r for r in data.get('public_rows') or [] if r.get('selected_for_apply')]


def expected_for(row: dict[str, Any]) -> dict[str, Any]:
    suggested = row.get('suggested_attributes') or {}
    return {
        'sizes': row.get('suggested_sizes') or suggested.get('sizes') or [],
        'ageGroup': row.get('suggested_age_group') if row.get('suggested_age_group') is not None else suggested.get('ageGroup'),
        'gender': row.get('suggested_gender') if row.get('suggested_gender') is not None else suggested.get('gender'),
    }


def norm_list(v: Any) -> list[str]:
    if v is None:
        return []
    if isinstance(v, list):
        return [str(x).strip() for x in v if str(x).strip()]
    t = str(v).strip()
    return [t] if t else []


def evaluate_rows(label: str, rows: list[dict[str, Any]], product_by_id: dict[str, dict[str, Any]], status_by_id: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    out = []
    for r in rows:
        pid = r.get('product_id')
        p = product_by_id.get(pid)
        s = status_by_id.get(pid)
        missing = required_attrs(s)
        exp = expected_for(r)
        actual_sizes = norm_list(p.get('sizes')) if p else []
        # Onda 1 intentionally wrote `sizes` only. Onda 2 wrote the 3-field set.
        if label == 'onda1':
            attrs_match = bool(p) and actual_sizes == exp['sizes']
            target_scope = {'size'}
        else:
            attrs_match = bool(p) and actual_sizes == exp['sizes'] and p.get('ageGroup') == exp['ageGroup'] and p.get('gender') == exp['gender']
            target_scope = TARGET_ATTRS
        target_missing = sorted(missing & target_scope)
        state = 'ok_attrs_and_no_target_required_diagnostic'
        if not p:
            state = 'product_not_present'
        elif not attrs_match:
            state = 'attrs_not_matching_expected'
        elif target_missing:
            state = 'attrs_match_but_productstatus_still_flags_target_attrs'
        elif missing:
            state = 'attrs_match_target_clean_but_other_required_attrs_remain'
        out.append({
            'wave': label,
            'product_id': pid,
            'merchant_title': p.get('title') if p else r.get('merchant_title'),
            'expected_sizes': exp['sizes'],
            'expected_ageGroup': exp['ageGroup'],
            'expected_gender': exp['gender'],
            'current_sizes': actual_sizes,
            'current_ageGroup': p.get('ageGroup') if p else None,
            'current_gender': p.get('gender') if p else None,
            'attrs_match_expected': attrs_match,
            'fresh_required_attrs': sorted(missing),
            'fresh_target_required_attrs': target_missing,
            'post_status_state': state,
        })
    return out


def main() -> None:
    audit = import_audit()
    secrets = audit.load_doppler()
    merchant_id = secrets.get('MERCHANT_CENTER_ID_LK')
    if not merchant_id:
        raise RuntimeError('missing_merchant_center_id')
    token = audit.google_access_token(audit.parse_service_account(secrets))
    products = audit.list_all('products', merchant_id, token)
    statuses = audit.list_all('productstatuses', merchant_id, token)
    product_by_id = {p.get('id'): p for p in products}
    status_by_id = {s.get('productId'): s for s in statuses}

    packet = json.loads(PACKET_JSON.read_text(encoding='utf-8'))
    # Use the packet for Onda 1 because the Onda 1 executor report may be overwritten
    # by a later single-row repair run. The packet is the stable set of all 60
    # approved high-confidence Onda 1 rows.
    onda1 = [r for r in packet.get('candidates') or [] if r.get('decision_state') == 'candidate_high_confidence_attr_preview']
    wave2 = load_selected(WAVE2_EXEC_JSON)
    eval_rows = evaluate_rows('onda1', onda1, product_by_id, status_by_id) + evaluate_rows('wave2', wave2, product_by_id, status_by_id)
    issue_codes, req_attr_counts, total_issue_instances = all_issue_counts(statuses)
    wave2_remaining = [r for r in eval_rows if r['wave'] == 'wave2' and r['post_status_state'] != 'ok_attrs_and_no_target_required_diagnostic']

    packet_wave2 = [r for r in packet.get('candidates') or [] if r.get('decision_state') == 'candidate_medium_confidence_attr_preview_needs_review']
    packet_by_id = {r.get('product_id'): r for r in packet_wave2}
    applied_ids = {r.get('product_id') for r in wave2}
    not_applied_wave2 = [r for r in packet_wave2 if r.get('product_id') not in applied_ids]
    not_applied_states = Counter()
    for r in not_applied_wave2:
        s = status_by_id.get(r.get('product_id'))
        missing = required_attrs(s)
        suggested = r.get('suggested_attributes') or {}
        if not (missing & TARGET_ATTRS):
            st = 'no_current_target_required_diagnostic'
        elif set(suggested.keys()) != {'sizes', 'ageGroup', 'gender'}:
            st = 'suggestion_not_exact_3field'
        elif suggested.get('ageGroup') != 'adult' or suggested.get('gender') != 'unisex':
            st = 'non_default_age_gender_review'
        else:
            st = 'other_review_needed'
        not_applied_states[st] += 1

    summary = {
        'generated_at': utc_now(),
        'fresh_merchant_products_current': len(products),
        'fresh_merchant_productstatuses_current': len(statuses),
        'total_item_level_issue_instances_current': total_issue_instances,
        'overall_issue_code_counts_top20': dict(issue_codes.most_common(20)),
        'overall_required_attr_counts': dict(req_attr_counts.most_common()),
        'onda1_applied_ids': len(onda1),
        'wave2_applied_ids': len(wave2),
        'all_applied_ids_evaluated': len(eval_rows),
        'post_status_state_counts': dict(Counter(r['post_status_state'] for r in eval_rows)),
        'wave2_post_status_state_counts': dict(Counter(r['post_status_state'] for r in eval_rows if r['wave'] == 'wave2')),
        'wave2_remaining_needing_review_or_wait': len(wave2_remaining),
        'wave2_packet_not_applied_count': len(not_applied_wave2),
        'wave2_packet_not_applied_state_counts': dict(not_applied_states),
        'write_allowed_now': 0,
    }
    payload = {
        'status': 'gmc_p1_attribute_wave2_post_status_recheck_read_only_complete',
        'scope': 'Read-only fresh productstatuses recheck after Onda 2 scale apply. No Merchant writes.',
        'source_labels': ['fact_merchant_center', 'derived_reconciliation'],
        'summary': summary,
        'applied_eval_rows': eval_rows,
        'wave2_remaining_rows': wave2_remaining,
        'not_performed': ['merchant_write', 'merchant_delete', 'feed_update_or_fetch', 'shopify_write', 'tiny_call_or_write', 'database_write', 'pos_or_local_inventory_write', 'klaviyo_or_whatsapp_send', 'notion_or_n8n_write', 'loyalty_or_judgeme_action'],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    fields = ['wave','product_id','merchant_title','attrs_match_expected','fresh_required_attrs','fresh_target_required_attrs','post_status_state']
    with OUT_CSV.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        w.writeheader()
        for r in wave2_remaining:
            out = {k: r.get(k) for k in fields}
            for k in ['fresh_required_attrs','fresh_target_required_attrs']:
                out[k] = '; '.join(out.get(k) or [])
            w.writerow(out)

    lines = [
        '# LK GMC P1 Attribute Completion — Wave2 Post-Status Recheck, 2026-05-13', '',
        f"Status: `{payload['status']}`", '',
        '## Escopo',
        '- Reconsulta fresh read-only de `products` e `productstatuses` após Onda 2.',
        '- Verifica Onda 1 + Onda 2 contra diagnósticos atuais.',
        '- Nenhum write/delete/feed/fetch.', '',
        '## Resultado geral atual',
        f"- Merchant products atuais: {summary['fresh_merchant_products_current']}",
        f"- Productstatuses atuais: {summary['fresh_merchant_productstatuses_current']}",
        f"- Item-level issue instances atuais: {summary['total_item_level_issue_instances_current']}",
        '- Required attrs atuais por atributo:',
    ]
    for k, v in summary['overall_required_attr_counts'].items():
        lines.append(f'  - {k}: {v}')
    lines.extend(['', '## IDs aplicados avaliados'])
    lines.append(f"- Onda 1 IDs aplicados: {summary['onda1_applied_ids']}")
    lines.append(f"- Onda 2 IDs aplicados: {summary['wave2_applied_ids']}")
    lines.append('- Estados pós-status:')
    for k, v in sorted(summary['post_status_state_counts'].items()):
        lines.append(f'  - {k}: {v}')
    lines.extend(['', '## Onda 2 aplicada — estado fresh'])
    for k, v in sorted(summary['wave2_post_status_state_counts'].items()):
        lines.append(f'- {k}: {v}')
    lines.extend(['', '## Onda 2 não aplicada / ainda review'])
    lines.append(f"- Rows do packet Onda 2 não aplicadas: {summary['wave2_packet_not_applied_count']}")
    for k, v in sorted(summary['wave2_packet_not_applied_state_counts'].items()):
        lines.append(f'  - {k}: {v}')
    lines.extend(['', '## Não executado'])
    for n in payload['not_performed']:
        lines.append(f'- {n}')
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(OUT_MD.read_text(encoding='utf-8'), encoding='utf-8')

    if CONTROL.exists():
        marker = '### 2026-05-13 — GMC P1 attribute Wave2 post-status recheck'
        text = CONTROL.read_text(encoding='utf-8')
        block = (f"\n{marker}\n\n"
                 f"- Status: `{payload['status']}`.\n"
                 f"- Onda 2 aplicada: {summary['wave2_applied_ids']} IDs; productstatuses fresh avaliados.\n"
                 f"- Estados Onda 2 aplicada: {summary['wave2_post_status_state_counts']}.\n"
                 f"- Required attrs atuais no GMC: {summary['overall_required_attr_counts']}.\n"
                 f"- Nenhum write/delete adicional executado.\n")
        if marker not in text:
            CONTROL.write_text(text.rstrip() + block + '\n', encoding='utf-8')
    if INDEX.exists():
        line = f'| LK GMC P1 Attribute Wave2 Post-Status Recheck 2026-05-13 | `areas/lk/rotinas/gmc-{RUN_STAMP}.md` | Reconsulta read-only fresh após apply da Onda 2; consolidou diagnósticos remanescentes |'
        text = INDEX.read_text(encoding='utf-8')
        if line not in text:
            INDEX.write_text(text.rstrip() + '\n' + line + '\n', encoding='utf-8')
    print(json.dumps({'status': payload['status'], 'summary': summary, 'public_report': str(OUT_MD), 'remaining_csv': str(OUT_CSV)}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
