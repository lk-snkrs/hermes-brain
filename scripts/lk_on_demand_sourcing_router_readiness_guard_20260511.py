#!/usr/bin/env python3
"""LK-AUTO-006 On-demand sourcing router readiness guard.

Manual/read-only guard. It validates that LK sourcing intelligence is ready for
per-item Lucas/Júlio decisions without performing external marketplace calls,
supplier contact, purchases, cron creation, or Shopify/Tiny writes.
"""
from __future__ import annotations

import csv
import json
import pathlib
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
ROUTER_JSON = ROOT / 'reports/lk-os-on-demand-sourcing-router-2026-05-04_2026-05-10.json'
FILA_A_JSON = ROOT / 'reports/lk-os-next-stage-fila-a-sourcing-preview-2026-05-11.json'
QUOTE_JSON = ROOT / 'reports/lk-fila-a-sourcing-validation-and-quote-preview-2026-05-11.json'
OUT_JSON = ROOT / 'reports/lk-on-demand-sourcing-router-readiness-guard-2026-05-11.json'
OUT_CSV = ROOT / 'reports/lk-on-demand-sourcing-router-readiness-guard-2026-05-11.csv'
OUT_MD = ROOT / 'reports/lk-on-demand-sourcing-router-readiness-guard-2026-05-11.md'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/on-demand-sourcing-router-readiness-guard-2026-05-11.md'

FORBIDDEN = [
    'external_marketplace_call', 'supplier_contact', 'purchase', 'purchase_order',
    'reservation', 'shopify_write', 'tiny_write', 'price_or_stock_change',
    'campaign_or_customer_send', 'cron_or_full_sync'
]
EXTERNAL_SOURCES = {'GOAT', 'Droper', 'StockX', 'KicksDev'}
SOURCE_LABELS_REQUIRED = {'fact_shopify', 'fact_tiny_stock'}


def load(path: pathlib.Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding='utf-8'))


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def brl(value: float | int | None) -> str:
    if value is None:
        return 'n/d'
    return 'R$ ' + f'{float(value):,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


def build() -> dict[str, Any]:
    router = load(ROUTER_JSON)
    fila_a = load(FILA_A_JSON)
    quote = load(QUOTE_JSON)
    checks: list[dict[str, Any]] = []

    def check(name: str, ok: bool, severity: str, detail: str, evidence: dict[str, Any] | None = None) -> None:
        checks.append({'name': name, 'ok': bool(ok), 'severity': severity, 'detail': detail, 'evidence': evidence or {}})

    router_rows = router.get('sourcing_router') or []
    router_summary = router.get('summary') or {}
    quote_records = quote.get('records') or []
    quote_summary = quote.get('summary') or {}
    fila_summary = fila_a.get('summary') or {}
    pending_excluded = fila_a.get('pending_excluded') or {}
    guardrails = [str(g).lower() for g in (quote.get('guardrails') or []) + (fila_a.get('guardrails') or [])]

    check('router_read_only_flag', router.get('read_only') is True, 'fail', 'Router payload must be explicitly read-only.', {'read_only': router.get('read_only')})
    check('router_rows_present', len(router_rows) > 0, 'fail', 'Router must contain decision-scoped rows.', {'rows': len(router_rows)})
    check('external_sources_on_demand_only', set(router.get('external_sources_defined_as_on_demand_only') or []) == EXTERNAL_SOURCES, 'fail', 'External sources must be defined only as on-demand tools.', {'sources': router.get('external_sources_defined_as_on_demand_only')})
    check('no_rows_eligible_for_external_lookup_now', all(r.get('eligible_for_external_lookup_now') is False for r in router_rows), 'fail', 'No row may authorize immediate external marketplace lookup.', {'eligible_true_count': sum(1 for r in router_rows if r.get('eligible_for_external_lookup_now') is True)})
    check('all_rows_block_forbidden_actions', all(set(FORBIDDEN).issubset(set(r.get('not_authorized_by_this_row') or [])) for r in router_rows), 'fail', 'Every row must explicitly block contact/purchase/write/full-sync actions.', {'forbidden': FORBIDDEN})
    check('source_labels_include_truth_sources', all(SOURCE_LABELS_REQUIRED.issubset(set(r.get('source_labels') or [])) for r in router_rows), 'fail', 'Rows must label Shopify/Tiny source boundaries.', {'required': sorted(SOURCE_LABELS_REQUIRED)})
    check('size_normalization_required_for_external', all('US Men vs US Women' in str(r.get('size_normalization_required') or '') for r in router_rows if r.get('recommended_source_sequence')), 'fail', 'Rows with StockX/GOAT future sources must require US Men vs US Women size normalization.', {})
    check('decision_scoped_no_full_sync', all(r.get('persist_only_decision_scoped_summary') is True and r.get('do_not_full_sync_external_prices') is True for r in router_rows), 'fail', 'External price results, if approved later, must persist only decision-scoped summaries, not full-sync tables.', {})

    check('fila_a_pending_excluded', (pending_excluded.get('count') or 0) >= 0 and 'pending' in str(pending_excluded.get('decision') or ''), 'warn', 'Fila A should explicitly exclude stand-by residuals from sourcing.', pending_excluded)
    check('quote_preview_has_records', len(quote_records) == int(quote_summary.get('top_items_validated') or len(quote_records)), 'fail', 'Quote preview records must match summary top_items_validated.', {'records': len(quote_records), 'top_items_validated': quote_summary.get('top_items_validated')})
    purchase_terms = ('comprar', 'compra', 'purchase', 'purchase order')
    purchase_guard_ok = all(
        ('não comprar' in str(r.get('recommended_action_preview') or '').lower())
        or ('não compra' in str(r.get('quote_logic') or '').lower())
        or ('cotar' in str(r.get('recommended_action_preview') or '').lower() and not any(term in str(r.get('recommended_action_preview') or '').lower() for term in purchase_terms))
        for r in quote_records
    )
    check('quote_qty_not_purchase_qty', purchase_guard_ok, 'fail', 'Quote records must not imply purchase approval; optional rows may say cotar/monitorar only.', {})
    check('supplier_fields_required_not_filled_as_truth', all('fornecedor' in [str(x).lower() for x in (r.get('supplier_fields_required') or [])] for r in quote_records), 'warn', 'Supplier data must remain required/pending rather than invented.', {})
    lead_gate_ok = all(any(term in str(r.get('lead_time_gate') or '').lower() for term in ('lead time', 'pronta-entrega', 'remessa de p0')) for r in quote_records)
    check('lead_time_gate_present', lead_gate_ok, 'fail', 'Each quote preview record must carry a lead-time or pronta-entrega/remessa gate.', {})
    check('cost_caps_not_real_margin', all('pendente de preço/fornecedor real' in str(r.get('internal_validation_status') or '').lower() for r in quote_records), 'fail', 'Margins must be represented as cost ceilings, not actual margin claims.', {})
    guardrail_blob = ' | '.join(guardrails)
    check('quote_guardrails_no_external_actions', all(term in guardrail_blob for term in ['sem contato', 'sem compra', 'sem shopify/tiny write']), 'fail', 'Source guardrails must explicitly prohibit supplier contact, purchases, and Shopify/Tiny writes.', {'guardrails': guardrails})

    fail_count = sum(1 for c in checks if not c['ok'] and c['severity'] == 'fail')
    warn_count = sum(1 for c in checks if not c['ok'] and c['severity'] == 'warn')
    ready_families = [r for r in router_rows if r.get('sourcing_router_status') == 'ready_for_manual_quote_approval_then_on_demand_lookup']
    top5 = sorted(quote_records, key=lambda r: int(r.get('rank') or 999))[:5]

    return {
        'generated_at': now(),
        'automation_id': 'LK-AUTO-006',
        'name': 'On-demand sourcing router',
        'mode': 'manual_readonly_per_item_readiness_guard',
        'readiness_status': 'ready_for_per_item_lucas_julio_decision_no_external_action' if fail_count == 0 else 'blocked_needs_fix_before_sourcing_decision',
        'summary': {
            'checks': len(checks),
            'fail_count': fail_count,
            'warn_count': warn_count,
            'router_rows': len(router_rows),
            'ready_after_manual_approval_count': router_summary.get('ready_after_manual_approval_count'),
            'optional_bundle_count': router_summary.get('optional_bundle_count'),
            'blocked_needs_data_count': router_summary.get('blocked_needs_data_count'),
            'fila_a_rows_considered': fila_summary.get('fila_a_rows_considered'),
            'executive_top_count': fila_summary.get('executive_top_count'),
            'quote_records': len(quote_records),
            'preview_quote_qty_total_not_purchase_qty': quote_summary.get('preview_quote_qty_total'),
            'external_marketplace_calls': 0,
            'supplier_contacts': 0,
            'purchases': 0,
            'purchase_orders': 0,
            'shopify_writes': 0,
            'tiny_writes': 0,
            'price_or_stock_changes': 0,
            'crons_created': 0,
            'n8n_flows_created': 0,
        },
        'ready_families_after_manual_approval_only': [
            {
                'sourcing_request_id': r.get('sourcing_request_id'),
                'family': r.get('family'),
                'approval_gate': r.get('approval_gate'),
                'future_sources_if_approved': r.get('recommended_source_sequence'),
                'revenue_signal_fact_shopify': r.get('revenue_signal_fact_shopify'),
            } for r in ready_families
        ],
        'top_quote_preview_not_purchase': [
            {
                'rank': r.get('rank'),
                'family': r.get('family'),
                'name': r.get('name'),
                'sku': r.get('sku'),
                'variant': r.get('variant'),
                'priority': r.get('priority'),
                'revenue_signal': r.get('revenue_signal'),
                'quote_qty_preview_not_purchase_qty': r.get('quote_qty_preview'),
                'lead_time_gate': r.get('lead_time_gate'),
            } for r in top5
        ],
        'checks': checks,
        'guardrails': [
            'No Droper/StockX/GOAT/KicksDev call executed by this guard.',
            'No supplier contact executed.',
            'No purchase, PO, reservation, or payment executed.',
            'No Shopify/Tiny write executed.',
            'No price, stock, product, campaign, or customer change executed.',
            'No full-sync external price table created.',
            'Quote quantity remains reference quantity, not purchase quantity.',
            'Actual per-item external search requires explicit Lucas/Júlio approval naming the family/SKU/scope.',
        ],
        'source_files': {
            'router': str(ROUTER_JSON.relative_to(ROOT)),
            'fila_a': str(FILA_A_JSON.relative_to(ROOT)),
            'quote_preview': str(QUOTE_JSON.relative_to(ROOT)),
        },
        'next_gate': 'Choose one family/SKU for a separate on-demand external price search, or keep as internal decision queue. Any supplier contact/purchase remains separate approval.',
    }


def write_outputs(payload: dict[str, Any]) -> None:
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    with OUT_CSV.open('w', encoding='utf-8', newline='') as f:
        fields = ['sourcing_request_id', 'family', 'approval_gate', 'future_sources_if_approved', 'revenue_signal_fact_shopify']
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in payload['ready_families_after_manual_approval_only']:
            out = dict(row)
            out['future_sources_if_approved'] = ', '.join(out.get('future_sources_if_approved') or [])
            writer.writerow(out)

    s = payload['summary']
    lines = [
        '# LK On-demand Sourcing Router Readiness Guard, 2026-05-11', '',
        f"Generated at: `{payload['generated_at']}`", '',
        '## Veredito', '',
        f"Status: `{payload['readiness_status']}`", '',
        'LK-AUTO-006 avançou para guard manual/read-only por item. Ele valida que a fila de sourcing está pronta para decisão Lucas/Júlio, mas não consulta marketplaces, não fala com fornecedor, não compra e não escreve em Shopify/Tiny.', '',
        '## Snapshot', '',
        f"- Checks: {s['checks']}",
        f"- Fails: {s['fail_count']}",
        f"- Warnings: {s['warn_count']}",
        f"- Router rows: {s['router_rows']}",
        f"- Ready only after manual approval: {s['ready_after_manual_approval_count']}",
        f"- Optional bundle: {s['optional_bundle_count']}",
        f"- Blocked needs data: {s['blocked_needs_data_count']}",
        f"- Fila A rows considered: {s['fila_a_rows_considered']}",
        f"- Quote preview records: {s['quote_records']}",
        f"- Quote qty total, not purchase qty: {s['preview_quote_qty_total_not_purchase_qty']}",
        f"- External marketplace calls: {s['external_marketplace_calls']}",
        f"- Supplier contacts: {s['supplier_contacts']}",
        f"- Purchases/POs: {s['purchases']}/{s['purchase_orders']}",
        f"- Shopify/Tiny writes: {s['shopify_writes']}/{s['tiny_writes']}", '',
        '## Famílias prontas apenas após aprovação manual', '',
    ]
    for row in payload['ready_families_after_manual_approval_only']:
        lines.extend([
            f"### {row['sourcing_request_id']} | {row['family']}",
            f"- Gate: {row['approval_gate']}",
            f"- Fontes futuras se aprovado: {', '.join(row['future_sources_if_approved'])}",
            f"- Sinal receita Shopify: {brl(row['revenue_signal_fact_shopify'])}", '',
        ])
    lines.extend(['## Top quote preview, não compra', ''])
    for row in payload['top_quote_preview_not_purchase']:
        lines.extend([
            f"- #{row['rank']} {row['name']} | SKU `{row['sku']}` | variação `{row['variant']}` | {row['priority']} | quote qty `{row['quote_qty_preview_not_purchase_qty']}` | receita {brl(row['revenue_signal'])}",
        ])
    lines.extend(['', '## Checks', ''])
    for c in payload['checks']:
        mark = 'OK' if c['ok'] else c['severity'].upper()
        lines.append(f"- {mark}: `{c['name']}` — {c['detail']}")
    lines.extend(['', '## Guardrails', ''])
    for g in payload['guardrails']:
        lines.append(f'- {g}')
    lines.extend(['', '## Próximo gate', '', payload['next_gate']])
    text = '\n'.join(lines) + '\n'
    OUT_MD.write_text(text, encoding='utf-8')
    BRAIN_DOC.write_text(text, encoding='utf-8')


def main() -> None:
    payload = build()
    write_outputs(payload)
    print(json.dumps({'ok': payload['summary']['fail_count'] == 0, 'status': payload['readiness_status'], 'summary': payload['summary']}, ensure_ascii=False))
    if payload['summary']['fail_count']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
