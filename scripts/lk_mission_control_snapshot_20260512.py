#!/usr/bin/env python3
"""LK OS Mission Control snapshot v1.

Read-only executive control plane for Lucas. It consolidates active reports/crons,
manual approval gates, safe next actions, and blocked actions without touching
Shopify, Tiny, Klaviyo, Merchant Center, GSC, suppliers, customers, or n8n.
"""
from __future__ import annotations

import csv
import json
import pathlib
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
PHASE8 = ROOT / 'reports/lk-phase8-completion-audit-2026-05-11.json'
LEDGER = ROOT / 'reports/lk-os-approval-learning-ledger-2026-05-11.json'
KLAVIYO = ROOT / 'reports/lk-klaviyo-crm-draft-readiness-watcher-2026-05-11.json'
SOURCING = ROOT / 'reports/lk-on-demand-sourcing-router-readiness-guard-2026-05-11.json'
MERCHANT = ROOT / 'reports/lk-merchant-center-feed-readonly-router-2026-05-11.json'
NEEDS_DATA_AUTOFIX = ROOT / 'reports/lk-needs-data-autofix-readonly-2026-05-12.json'
GMC_CORRECTION_PREVIEW = ROOT / 'reports/lk-gmc-correction-preview-2026-05-12.json'
GMC_P0_URL_REVIEW = ROOT / 'reports/lk-gmc-p0-url-checkout-review-2026-05-12.json'
GMC_REQUIRED_ATTRS_PREVIEW = ROOT / 'reports/lk-gmc-required-attrs-preview-2026-05-12.json'
OUT_JSON = ROOT / 'reports/lk-mission-control-snapshot-2026-05-12.json'
OUT_MD = ROOT / 'reports/lk-mission-control-snapshot-2026-05-12.md'
OUT_CSV = ROOT / 'reports/lk-mission-control-snapshot-2026-05-12.csv'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/mission-control-snapshot-2026-05-12.md'

EXPECTED_CRONS = [
    {'id': '7c688553e293', 'name': 'Daily Sales Brief', 'cadence': 'diário 08:00 BRT', 'mode': 'mandatory_report', 'status': 'active'},
    {'id': '953b9055458e', 'name': 'Weekly CEO Review', 'cadence': 'segunda 09:00 BRT', 'mode': 'mandatory_report', 'status': 'active'},
    {'id': '15777e3416dc', 'name': 'SEO/CRO Weekly', 'cadence': 'segunda 10:00 BRT', 'mode': 'read_only_preview', 'status': 'active'},
    {'id': 'd4c26da4cd48', 'name': 'GMC Review', 'cadence': 'quinta 09:00 BRT', 'mode': 'mandatory_report', 'status': 'active'},
]


def load(path: pathlib.Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding='utf-8'))


def money_brl(v: Any) -> str:
    try:
        return f"R$ {float(v):,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    except Exception:
        return 'n/a'


def build() -> dict[str, Any]:
    phase8 = load(PHASE8)
    ledger = load(LEDGER)
    klaviyo = load(KLAVIYO)
    sourcing = load(SOURCING)
    merchant = load(MERCHANT)
    needs_data_autofix = load(NEEDS_DATA_AUTOFIX) if NEEDS_DATA_AUTOFIX.exists() else {'summary': {}, 'results': []}
    gmc_correction_preview = load(GMC_CORRECTION_PREVIEW) if GMC_CORRECTION_PREVIEW.exists() else {'summary': {}, 'packages': []}
    gmc_p0_url_review = load(GMC_P0_URL_REVIEW) if GMC_P0_URL_REVIEW.exists() else {'summary': {}, 'results': []}
    gmc_required_attrs_preview = load(GMC_REQUIRED_ATTRS_PREVIEW) if GMC_REQUIRED_ATTRS_PREVIEW.exists() else {'summary': {}, 'results': []}

    records = ledger.get('records') or []
    status_counts = Counter(r.get('status') for r in records)
    risk_counts = Counter(r.get('risk') for r in records)

    approvals = [r for r in records if r.get('status') == 'needs_approval']
    needs_data = [r for r in records if r.get('status') == 'needs_data']
    pending_future = [r for r in records if r.get('status') == 'pending_future']
    executed = [r for r in records if r.get('status') == 'executed_verified']

    sourcing_summary = sourcing.get('summary') or {}
    merchant_summary = merchant.get('summary') or {}
    gmc_preview_summary = gmc_correction_preview.get('summary') or {}
    gmc_p0_url_summary = gmc_p0_url_review.get('summary') or {}
    gmc_required_attrs_summary = gmc_required_attrs_preview.get('summary') or {}
    klaviyo_summary = klaviyo.get('summary') or {}
    phase8_summary = phase8.get('summary') or {}

    needs_data_autofix_summary = needs_data_autofix.get('summary') or {}
    needs_data_autofix_results = needs_data_autofix.get('results') or []
    remaining_data_followup = needs_data_autofix_summary.get('keep_internal_data_followup', len(needs_data))
    resolved_to_monitor = needs_data_autofix_summary.get('move_from_needs_data_to_monitor_or_stock_ok', 0)
    internal_code_hygiene = needs_data_autofix_summary.get('internal_code_hygiene_then_decision', 0)

    checks: list[dict[str, Any]] = []

    def check(name: str, ok: bool, detail: str, evidence: dict[str, Any] | None = None, severity: str = 'fail') -> None:
        checks.append({'name': name, 'ok': bool(ok), 'severity': severity, 'detail': detail, 'evidence': evidence or {}})

    check('phase8_guardrails_green', phase8.get('completion_status') == 'phase8_complete_with_guardrails' and phase8_summary.get('fail_count') == 0, 'Fase 8 must be green before Mission Control v1.', phase8_summary)
    check('mandatory_crons_count', phase8_summary.get('active_crons') == 4 and phase8_summary.get('mandatory_deliveries') == 3, 'Expected 4 active LK crons and 3 mandatory deliveries after GMC reconciliation.', phase8_summary)
    check('ledger_has_open_decisions', status_counts.get('needs_approval', 0) == 5 and len(needs_data) == 3 and remaining_data_followup == 0, 'Mission Control must expose 5 approvals and zero remaining data blockers after autonomous needs_data autofix.', {'ledger_counts': dict(status_counts), 'needs_data_autofix': needs_data_autofix_summary})
    check('no_writes_or_external_actions', all(phase8_summary.get(k, 0) == 0 for k in ['production_writes','external_sends_or_contacts','purchases_or_pos','external_marketplace_calls','n8n_flows_created']), 'Mission Control snapshot must remain read-only/no-external-action.', phase8_summary)
    check('klaviyo_draft_safe', klaviyo.get('readiness_status') == 'ready_for_lucas_review_no_send' and klaviyo_summary.get('campaign_sends') == 0 and klaviyo_summary.get('campaign_schedules') == 0, 'Klaviyo must remain Draft/no-send.', klaviyo_summary)
    check('sourcing_safe', sourcing.get('readiness_status') == 'ready_for_per_item_lucas_julio_decision_no_external_action' and sourcing_summary.get('external_marketplace_calls') == 0, 'Sourcing must remain decision-only/no marketplace calls.', sourcing_summary)
    check('merchant_safe', merchant_summary.get('writes_allowed_now') == 0 and merchant_summary.get('product_statuses_read', 0) > 0, 'GMC must be read-only with product statuses available.', merchant_summary)
    check('gmc_correction_preview_safe', gmc_preview_summary.get('write_allowed_now', 0) == 0 and gmc_preview_summary.get('packages', 0) >= 1, 'GMC correction preview must package issues without permitting writes.', gmc_preview_summary, severity='warn')
    check('gmc_p0_url_review_safe', gmc_p0_url_summary.get('write_allowed_now', 0) == 0 and gmc_p0_url_summary.get('p0_rows_reviewed', 0) > 0, 'GMC P0 URL/checkout review must provide SKU/URL evidence without writes.', gmc_p0_url_summary, severity='warn')
    check('gmc_required_attrs_preview_safe', gmc_required_attrs_summary.get('write_allowed_now', 0) == 0 and gmc_required_attrs_summary.get('required_attr_rows_reviewed', 0) > 0, 'GMC required-attributes preview must propose local corrections without writes.', gmc_required_attrs_summary, severity='warn')

    open_items = []
    for r in approvals[:5]:
        open_items.append({
            'lane': 'approval_needed',
            'priority': 'P1',
            'title': r.get('item_label'),
            'owner': r.get('owner'),
            'next_safe_action': r.get('allowed_next_action'),
            'blocked': ', '.join((r.get('blocked_actions') or [])[:4]),
            'source': r.get('source_artifact'),
        })
    for r in needs_data_autofix_results:
        lane = 'data_resolved_monitor' if r.get('recommended_route') == 'move_from_needs_data_to_monitor_or_stock_ok' else 'internal_code_hygiene'
        open_items.append({
            'lane': lane,
            'priority': r.get('priority') or 'P1',
            'title': r.get('family') or r.get('product_title'),
            'owner': 'Hermes/LK data spine',
            'next_safe_action': r.get('reason'),
            'blocked': 'external sourcing/contact/purchase still blocked; local/read-only hygiene allowed',
            'source': 'reports/lk-needs-data-autofix-readonly-2026-05-12.json',
        })

    crm_gate = {
        'lane': 'crm_gate',
        'priority': 'P1',
        'title': 'Klaviyo P1 draft, loja física recompra',
        'status': klaviyo.get('readiness_status'),
        'next_safe_action': 'Lucas review by verified list/template/campaign IDs; prepare send packet only if explicitly requested.',
        'blocked': 'send, schedule, flow, customer contact',
        'campaign_id': (klaviyo.get('klaviyo_objects') or {}).get('campaign_id'),
    }
    gmc_gate = {
        'lane': 'google_feed',
        'priority': 'P1',
        'title': 'GMC feed diagnostics',
        'status': 'read_only_queue_ready',
        'next_safe_action': 'Required attributes preview ready locally: 80 offer_ids mapped with age_group/gender/size suggestions. Next safe step is Lucas-approved supplemental-feed/feed-rule write, not Shopify product mutation.',
        'blocked': 'Merchant/feed/Shopify/GSC writes',
        'queue_items': merchant_summary.get('queue_items'),
        'p1_items': merchant_summary.get('p1_items'),
        'correction_packages': gmc_preview_summary.get('packages'),
        'p0_packages': gmc_preview_summary.get('p0_packages'),
        'p0_rows_reviewed': gmc_p0_url_summary.get('p0_rows_reviewed'),
        'p0_pdp_http_200_rows': gmc_p0_url_summary.get('public_url_http_200_rows'),
        'required_attr_rows_reviewed': gmc_required_attrs_summary.get('required_attr_rows_reviewed'),
        'required_attr_preview_rows': gmc_required_attrs_summary.get('supplemental_feed_preview_rows'),
    }

    immediate_safe_next = [
        'Acompanhar primeira entrega Daily Sales Brief em 2026-05-12 08:00 BRT.',
        'Manter Klaviyo P1 em Draft; só preparar pacote de envio se Lucas pedir explicitamente.',
        'Preparar uma fila de decisão curta para sourcing: 4 famílias aprováveis; os 3 antigos needs_data foram reconciliados em modo read-only/local.',
        'GMC required attributes: preview local pronto para 80 offer_ids; próximo passo com aprovação é aplicar supplemental feed/feed rule mínimo e pedir recheck Merchant.',
    ]

    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'LK OS Mission Control snapshot v1',
        'status': 'mission_control_ready_readonly' if all(c['ok'] for c in checks if c['severity'] == 'fail') else 'blocked_needs_fix',
        'summary': {
            'active_crons': phase8_summary.get('active_crons'),
            'mandatory_deliveries': phase8_summary.get('mandatory_deliveries'),
            'ledger_records': len(records),
            'executed_verified': len(executed),
            'needs_approval': len(approvals),
            'needs_data_original_ledger': len(needs_data),
            'needs_data_remaining_after_autofix': remaining_data_followup,
            'needs_data_resolved_to_monitor': resolved_to_monitor,
            'needs_data_internal_code_hygiene': internal_code_hygiene,
            'pending_future': len(pending_future),
            'klaviyo_campaign_status': klaviyo_summary.get('campaign_status'),
            'sourcing_ready_after_manual_approval': sourcing_summary.get('ready_after_manual_approval_count'),
            'gmc_queue_items': merchant_summary.get('queue_items'),
            'gmc_p1_items': merchant_summary.get('p1_items'),
            'gmc_correction_packages': gmc_preview_summary.get('packages'),
            'gmc_correction_p0_packages': gmc_preview_summary.get('p0_packages'),
            'gmc_p0_rows_reviewed': gmc_p0_url_summary.get('p0_rows_reviewed'),
            'gmc_p0_pdp_http_200_rows': gmc_p0_url_summary.get('public_url_http_200_rows'),
            'gmc_required_attr_rows_reviewed': gmc_required_attrs_summary.get('required_attr_rows_reviewed'),
            'gmc_required_attr_preview_rows': gmc_required_attrs_summary.get('supplemental_feed_preview_rows'),
            'production_writes': phase8_summary.get('production_writes'),
            'external_sends_or_contacts': phase8_summary.get('external_sends_or_contacts'),
            'purchases_or_pos': phase8_summary.get('purchases_or_pos'),
            'external_marketplace_calls': phase8_summary.get('external_marketplace_calls'),
            'n8n_flows_created': phase8_summary.get('n8n_flows_created'),
            'checks': len(checks),
            'fail_count': sum(1 for c in checks if not c['ok'] and c['severity'] == 'fail'),
            'warn_count': sum(1 for c in checks if not c['ok'] and c['severity'] == 'warn'),
        },
        'crons': EXPECTED_CRONS,
        'open_items': open_items,
        'crm_gate': crm_gate,
        'gmc_gate': gmc_gate,
        'safe_next_actions': immediate_safe_next,
        'status_counts': dict(status_counts),
        'risk_counts': dict(risk_counts),
        'checks': checks,
        'not_performed': [
            'shopify_write', 'tiny_write', 'klaviyo_send_or_schedule', 'merchant_feed_write', 'gsc_admin_or_indexing_submit',
            'supplier_contact', 'marketplace_lookup', 'purchase_order', 'customer_contact', 'n8n_flow_creation'
        ],
    }
    return payload


def write_outputs(payload: dict[str, Any]) -> None:
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    with OUT_CSV.open('w', encoding='utf-8', newline='') as f:
        fields = ['lane', 'priority', 'title', 'owner', 'next_safe_action', 'blocked', 'source']
        writer = csv.DictWriter(f, fieldnames=fields, lineterminator='\n')
        writer.writeheader()
        for row in payload['open_items']:
            writer.writerow({k: row.get(k, '') for k in fields})
    s = payload['summary']
    lines = [
        '# LK Mission Control Snapshot, 2026-05-12', '',
        f"Generated at: `{payload['generated_at']}`", '',
        '## Veredito', '',
        f"Status: `{payload['status']}`", '',
        'Mission Control v1 consolida crons ativos, relatórios obrigatórios, aprovações abertas, bloqueios de dados, Klaviyo Draft, sourcing readiness e GMC queue. É uma visão executiva read-only; não cria UI, não dispara campanha, não compra, não altera catálogo/feed e não cria n8n.', '',
        '## Painel curto', '',
        f"- Crons ativos LK: {s['active_crons']}",
        f"- Reports obrigatórios: {s['mandatory_deliveries']}",
        f"- Ledger: {s['ledger_records']} registros, {s['executed_verified']} executados verificados, {s['needs_approval']} aguardando aprovação, {s['needs_data_remaining_after_autofix']} bloqueados por dados após autofix, {s['pending_future']} futuros",
        f"- Needs_data resolvidos: {s['needs_data_resolved_to_monitor']} para monitor/estoque OK, {s['needs_data_internal_code_hygiene']} para higiene interna de código",
        f"- Klaviyo P1: {s['klaviyo_campaign_status']} / sem envio",
        f"- Sourcing: {s['sourcing_ready_after_manual_approval']} famílias prontas só após aprovação manual",
        f"- GMC: {s['gmc_queue_items']} itens P1/P2, {s['gmc_p1_items']} P1, {s['gmc_correction_packages']} pacotes preview-only; P0: {s['gmc_p0_rows_reviewed']} linhas / {s['gmc_p0_pdp_http_200_rows']} PDPs HTTP 200; atributos: {s['gmc_required_attr_rows_reviewed']} revisados / {s['gmc_required_attr_preview_rows']} em preview local",
        f"- Writes/envios/contatos/compras/marketplace/n8n: {s['production_writes']}/{s['external_sends_or_contacts']}/{s['purchases_or_pos']}/{s['external_marketplace_calls']}/{s['n8n_flows_created']}", '',
        '## Crons operacionais', '',
    ]
    for c in payload['crons']:
        lines.append(f"- `{c['id']}` — {c['name']}: {c['cadence']}, {c['mode']}, {c['status']}")
    lines.extend(['', '## Top decisões / bloqueios', ''])
    for row in payload['open_items']:
        lines.extend([
            f"### {row['priority']} · {row['lane']} · {row['title']}",
            f"- Dono: {row.get('owner') or 'n/a'}",
            f"- Próximo passo seguro: {row.get('next_safe_action') or 'n/a'}",
            f"- Bloqueado: {row.get('blocked') or 'n/a'}",
            f"- Fonte: `{row.get('source') or 'n/a'}`", '',
        ])
    lines.extend(['## Gates especiais', ''])
    crm = payload['crm_gate']
    lines.extend([
        f"- CRM/Klaviyo: `{crm['status']}`, campaign `{crm['campaign_id']}`, próximo seguro: {crm['next_safe_action']}",
        f"- GMC/feed: {payload['gmc_gate']['queue_items']} itens na fila, {payload['gmc_gate']['p1_items']} P1, {payload['gmc_gate'].get('correction_packages')} pacotes preview-only, P0 aberto {payload['gmc_gate'].get('p0_rows_reviewed')} linhas / {payload['gmc_gate'].get('p0_pdp_http_200_rows')} PDPs HTTP 200, atributos {payload['gmc_gate'].get('required_attr_rows_reviewed')} revisados / {payload['gmc_gate'].get('required_attr_preview_rows')} em preview, próximo seguro: {payload['gmc_gate']['next_safe_action']}", '',
        '## Próximas ações seguras', '',
    ])
    for a in payload['safe_next_actions']:
        lines.append(f'- {a}')
    lines.extend(['', '## Checks', ''])
    for c in payload['checks']:
        mark = 'OK' if c['ok'] else c['severity'].upper()
        lines.append(f"- {mark}: `{c['name']}` — {c['detail']}")
    lines.extend(['', '## Não executado', ''])
    for n in payload['not_performed']:
        lines.append(f'- {n}')
    text = '\n'.join(lines) + '\n'
    OUT_MD.write_text(text, encoding='utf-8')
    BRAIN_DOC.write_text(text, encoding='utf-8')


def main() -> None:
    payload = build()
    write_outputs(payload)
    print(json.dumps({'ok': payload['summary']['fail_count'] == 0, 'status': payload['status'], 'summary': payload['summary']}, ensure_ascii=False))
    if payload['summary']['fail_count']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
