#!/usr/bin/env python3
"""Read-only post-apply verification for GMC P1 attribute completion Onda 1
and review-sample preparation for Onda 2.

No Merchant writes. Uses Content API only for products/productstatuses reads.
"""
from __future__ import annotations

import csv
import importlib.util
import json
import pathlib
from collections import Counter, defaultdict
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / 'scripts/lk_gmc_catalog_duplication_audit_20260512.py'
PACKET_JSON = ROOT / 'reports/lk-gmc-p1-attribute-completion-packet-v2-2026-05-13.json'
ONDA1_EXEC_JSON = ROOT / 'reports/lk-gmc-2026-05-13-p1-attribute-completion-onda1-executor.json'
RUN_STAMP = '2026-05-13-p1-attribute-post-apply-wave2-review'
OUT_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
OUT_CSV = ROOT / f'reports/lk-gmc-{RUN_STAMP}-wave2-sample.csv'
OUT_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
CONTROL = ROOT / 'areas/lk/projetos/lk-os-implementation-control.md'
INDEX = ROOT / 'empresa/rotinas/_index.md'
REQ_CODES = {'item_missing_required_attribute', 'missing_item_attribute_for_product_type'}
ONDA2_STATE = 'candidate_medium_confidence_attr_preview_needs_review'


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def import_audit():
    spec = importlib.util.spec_from_file_location('audit', AUDIT_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


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


def classify_wave2(row: dict[str, Any], product: dict[str, Any] | None, status: dict[str, Any] | None) -> dict[str, Any]:
    suggested = row.get('suggested_attributes') or {}
    current_missing = missing_required_attrs(status or {})
    current_sizes = normalize_list(product.get('sizes')) if product else []
    current_age = product.get('ageGroup') if product else None
    current_gender = product.get('gender') if product else None
    suggested_sizes = normalize_list(suggested.get('sizes'))
    decision = 'review_required'
    reasons = []
    if not product:
        decision = 'blocked_product_not_currently_present'
        reasons.append('product_id not present in fresh products list')
    else:
        if 'age group' in current_missing or 'gender' in current_missing or 'size' in current_missing:
            reasons.append('fresh productstatus still reports required metadata missing')
        else:
            reasons.append('fresh productstatus no longer reports the packet missing metadata')
        if not suggested_sizes:
            decision = 'blocked_missing_suggested_size'
            reasons.append('no suggested size')
        elif current_sizes and current_sizes != suggested_sizes:
            decision = 'review_existing_size_conflict'
            reasons.append('existing Merchant sizes differ from Shopify suggestion')
        elif suggested.get('ageGroup') != 'adult' or suggested.get('gender') != 'unisex':
            decision = 'review_non_default_age_gender'
            reasons.append('suggested age/gender not default adult/unisex')
        elif {'age group', 'gender', 'size'} & current_missing:
            decision = 'candidate_wave2_review_default_adult_unisex_size'
            reasons.append('default adult/unisex + Shopify size evidence but needs human approval')
        else:
            decision = 'skipped_already_resolved_or_not_currently_flagged'
    return {
        'product_id': row.get('product_id'),
        'offer_id': row.get('offer_id'),
        'merchant_title': product.get('title') if product else row.get('merchant_title'),
        'shopify_product_title': row.get('shopify_product_title'),
        'shopify_variant_title': row.get('shopify_variant_title'),
        'packet_missing_attributes': row.get('missing_attributes') or [],
        'fresh_missing_required_attrs': sorted(current_missing),
        'current_sizes': current_sizes,
        'current_age_group': current_age,
        'current_gender': current_gender,
        'suggested_sizes': suggested_sizes,
        'suggested_age_group': suggested.get('ageGroup'),
        'suggested_gender': suggested.get('gender'),
        'review_decision_state': decision,
        'review_reasons': reasons,
        'apply_allowed_now': False,
    }


def choose_wave2_sample(rows: list[dict[str, Any]], sample_size: int = 80) -> list[dict[str, Any]]:
    # Include a broad, deterministic sample by title prefix/product family while keeping only review candidates.
    eligible = [r for r in rows if r['review_decision_state'] == 'candidate_wave2_review_default_adult_unisex_size']
    by_family: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for r in eligible:
        title = (r.get('merchant_title') or '').strip()
        family = ' '.join(title.split()[:5]).lower() or 'unknown'
        by_family[family].append(r)
    sample = []
    for family in sorted(by_family):
        if len(sample) >= sample_size:
            break
        sample.append(sorted(by_family[family], key=lambda x: x.get('product_id') or '')[0])
    if len(sample) < sample_size:
        seen = {r['product_id'] for r in sample}
        for r in sorted(eligible, key=lambda x: x.get('product_id') or ''):
            if r['product_id'] not in seen:
                sample.append(r); seen.add(r['product_id'])
            if len(sample) >= sample_size:
                break
    return sample


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
    exec_payload = json.loads(ONDA1_EXEC_JSON.read_text(encoding='utf-8'))
    onda1_rows = [r for r in exec_payload.get('public_rows') or [] if r.get('selected_for_apply')]
    onda1_verify = []
    for r in onda1_rows:
        pid = r['product_id']
        prod = product_by_id.get(pid)
        stat = status_by_id.get(pid) or {}
        expected = r.get('suggested_sizes') or []
        actual = normalize_list(prod.get('sizes')) if prod else []
        fresh_missing = missing_required_attrs(stat)
        onda1_verify.append({
            'product_id': pid,
            'merchant_title': prod.get('title') if prod else r.get('merchant_title'),
            'expected_sizes': expected,
            'current_sizes': actual,
            'sizes_match_expected': actual == expected,
            'fresh_missing_required_attrs': sorted(fresh_missing),
            'size_issue_still_present': 'size' in fresh_missing,
            'product_present': bool(prod),
        })

    wave2_packet_rows = [r for r in packet.get('candidates') or [] if r.get('decision_state') == ONDA2_STATE]
    wave2_rows = [classify_wave2(r, product_by_id.get(r.get('product_id')), status_by_id.get(r.get('product_id'))) for r in wave2_packet_rows]
    wave2_sample = choose_wave2_sample(wave2_rows, 80)

    summary = {
        'fresh_merchant_products_current': len(products),
        'fresh_merchant_productstatuses_current': len(statuses),
        'onda1_selected_applied': len(onda1_rows),
        'onda1_product_present': sum(1 for r in onda1_verify if r['product_present']),
        'onda1_sizes_match_expected': sum(1 for r in onda1_verify if r['sizes_match_expected']),
        'onda1_size_issue_still_present': sum(1 for r in onda1_verify if r['size_issue_still_present']),
        'onda1_any_required_issue_still_present': sum(1 for r in onda1_verify if r['fresh_missing_required_attrs']),
        'wave2_packet_rows': len(wave2_packet_rows),
        'wave2_review_state_counts': dict(Counter(r['review_decision_state'] for r in wave2_rows)),
        'wave2_fresh_missing_attr_counts': dict(Counter(a for r in wave2_rows for a in r['fresh_missing_required_attrs'])),
        'wave2_sample_rows': len(wave2_sample),
        'write_allowed_now': 0,
    }
    payload = {
        'generated_at': utc_now(),
        'status': 'gmc_p1_attribute_post_apply_onda1_verified_wave2_review_ready_no_write',
        'scope': 'Read-only post-apply status refresh for Onda 1 + review sample for Onda 2. No Merchant writes.',
        'source_labels': ['fact_merchant_center', 'fact_shopify_local_snapshot', 'derived_reconciliation'],
        'summary': summary,
        'onda1_verify_rows': onda1_verify,
        'wave2_sample_rows': wave2_sample,
        'not_performed': ['merchant_write', 'merchant_delete', 'feed_update_or_fetch', 'shopify_write', 'tiny_call_or_write', 'database_write', 'pos_write', 'klaviyo_or_whatsapp_send', 'notion_or_n8n_write', 'loyalty_or_judgeme_action'],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    fields = ['product_id','merchant_title','shopify_variant_title','packet_missing_attributes','fresh_missing_required_attrs','current_sizes','current_age_group','current_gender','suggested_sizes','suggested_age_group','suggested_gender','review_decision_state','review_reasons','apply_allowed_now']
    with OUT_CSV.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        w.writeheader()
        for r in wave2_sample:
            out = {k: r.get(k) for k in fields}
            for k in ['packet_missing_attributes','fresh_missing_required_attrs','current_sizes','suggested_sizes','review_reasons']:
                out[k] = '; '.join(out.get(k) or [])
            w.writerow(out)
    lines = [
        '# LK GMC P1 Attribute Completion — Post-Apply Onda 1 + Onda 2 Review, 2026-05-13', '',
        f"Status: `{payload['status']}`", '',
        '## O que foi feito',
        '- Reconsulta read-only de Merchant products e productstatuses.',
        '- Medição pós-apply dos 60 IDs da Onda 1.',
        '- Preparação de amostra revisável da Onda 2, sem apply.', '',
        '## Onda 1 — resultado pós-propagação',
        f"- IDs aplicados na Onda 1: {summary['onda1_selected_applied']}",
        f"- Produtos ainda presentes: {summary['onda1_product_present']}",
        f"- `sizes` esperado confirmado agora: {summary['onda1_sizes_match_expected']}/{summary['onda1_selected_applied']}",
        f"- IDs ainda com issue fresh de `size`: {summary['onda1_size_issue_still_present']}",
        f"- IDs ainda com qualquer required-attribute issue: {summary['onda1_any_required_issue_still_present']}", '',
        '## Onda 2 — estado read-only',
        f"- Rows no packet Onda 2: {summary['wave2_packet_rows']}",
        '- Estados fresh:',
    ]
    for k, v in sorted(summary['wave2_review_state_counts'].items()):
        lines.append(f'  - {k}: {v}')
    lines.extend(['- Missing attrs fresh na Onda 2:'])
    for k, v in sorted(summary['wave2_fresh_missing_attr_counts'].items()):
        lines.append(f'  - {k}: {v}')
    lines.extend(['', '## Amostra revisável Onda 2'])
    for r in wave2_sample[:25]:
        lines.append(f"- `{r['product_id']}` — {r.get('merchant_title')} — missing={r.get('fresh_missing_required_attrs')} — sugestão: size={r.get('suggested_sizes')}, ageGroup={r.get('suggested_age_group')}, gender={r.get('suggested_gender')}")
    lines.extend(['', '## Guardrail', '- A Onda 2 continua como `review/no-write`: usa default `adult/unisex` + tamanho por Shopify, mas ainda precisa aprovação explícita antes de qualquer apply.', '', '## Não executado'])
    for n in payload['not_performed']:
        lines.append(f'- {n}')
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(OUT_MD.read_text(encoding='utf-8'), encoding='utf-8')
    if CONTROL.exists():
        marker = '### 2026-05-13 — GMC P1 attribute post-apply Onda 1 + Onda 2 review'
        text = CONTROL.read_text(encoding='utf-8')
        block = (f"\n{marker}\n\n"
                 f"- Status: `{payload['status']}`.\n"
                 f"- Onda 1 pós-apply: {summary['onda1_sizes_match_expected']}/{summary['onda1_selected_applied']} com `sizes` esperado; size issues fresh remanescentes={summary['onda1_size_issue_still_present']}.\n"
                 f"- Onda 2: {summary['wave2_packet_rows']} rows revisadas read-only; amostra de {summary['wave2_sample_rows']} preparada; nenhum apply/write.\n")
        if marker not in text:
            CONTROL.write_text(text.rstrip() + block + '\n', encoding='utf-8')
    if INDEX.exists():
        line = f'| LK GMC P1 Attribute Post-Apply + Onda 2 Review 2026-05-13 | `areas/lk/rotinas/gmc-{RUN_STAMP}.md` | Reconsulta read-only pós-Onda 1 e amostra revisável Onda 2 sem apply |'
        text = INDEX.read_text(encoding='utf-8')
        if line not in text:
            INDEX.write_text(text.rstrip() + '\n' + line + '\n', encoding='utf-8')
    print(json.dumps({'status': payload['status'], 'summary': summary, 'public_report': str(OUT_MD), 'wave2_sample_csv': str(OUT_CSV)}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
