#!/usr/bin/env python3
"""LK Phase 8 completion audit.

Consolidates the final state of LK-AUTO-001..007 after PRD cron reconciliation.
Does not create/update cron jobs, does not call business APIs, and does not perform writes.
"""
from __future__ import annotations

import csv
import json
import pathlib
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
OP_REG = ROOT / 'reports/lk-phase8-operational-automation-registry-2026-05-11.json'
LEDGER_GUARD = ROOT / 'reports/lk-approval-ledger-refresh-guard-2026-05-11.json'
KLAVIYO_GUARD = ROOT / 'reports/lk-klaviyo-crm-draft-readiness-watcher-2026-05-11.json'
SOURCING_GUARD = ROOT / 'reports/lk-on-demand-sourcing-router-readiness-guard-2026-05-11.json'
MERCHANT_REPORT = ROOT / 'reports/lk-merchant-center-feed-readonly-router-2026-05-11.json'
OUT_JSON = ROOT / 'reports/lk-phase8-completion-audit-2026-05-11.json'
OUT_CSV = ROOT / 'reports/lk-phase8-completion-audit-2026-05-11.csv'
OUT_MD = ROOT / 'reports/lk-phase8-completion-audit-2026-05-11.md'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/phase8-completion-audit-2026-05-11.md'

EXPECTED_CRONS = {
    'LK-AUTO-001': {'job_id': '7c688553e293', 'name': 'LK Daily Sales Brief read-only mandatory delivery', 'schedule_utc': '0 11 * * *', 'cadence': 'daily 08:00 BRT'},
    'LK-AUTO-002': {'job_id': '953b9055458e', 'name': 'LK Weekly CEO Review read-only mandatory delivery', 'schedule_utc': '0 12 * * 1', 'cadence': 'weekly Monday 09:00 BRT'},
    'LK-AUTO-003': {'job_id': '15777e3416dc', 'name': 'LK SEO/CRO weekly Claude SEO improvement loop', 'schedule_utc': '0 13 * * 1', 'cadence': 'weekly Monday 10:00 BRT'},
    'LK-AUTO-007': {'job_id': 'd4c26da4cd48', 'name': 'LK GMC Review read-only mandatory delivery', 'schedule_utc': '0 12 * * 4', 'cadence': 'weekly Thursday 09:00 BRT'},
}


def load(path: pathlib.Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding='utf-8'))


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def build() -> dict[str, Any]:
    op = load(OP_REG)
    ledger = load(LEDGER_GUARD)
    klaviyo = load(KLAVIYO_GUARD)
    sourcing = load(SOURCING_GUARD)
    merchant = load(MERCHANT_REPORT)
    checks: list[dict[str, Any]] = []

    def check(name: str, ok: bool, severity: str, detail: str, evidence: dict[str, Any] | None = None) -> None:
        checks.append({'name': name, 'ok': bool(ok), 'severity': severity, 'detail': detail, 'evidence': evidence or {}})

    op_by_id = {a.get('automation_id'): a for a in op.get('automations') or []}
    check('base_registry_six_plus_gmc_reconciled', len(op_by_id) == 6, 'fail', 'Historical Phase 8 registry had 6 entries before Lucas identified missing GMC Review; completion audit extends final state to 7.', {'historical_registry_count': len(op_by_id), 'final_state_count': 7})
    check('daily_weekly_mandatory', all((op_by_id.get(k) or {}).get('status') == 'active_cron_mandatory_delivery' for k in ('LK-AUTO-001','LK-AUTO-002')), 'fail', 'Daily/Weekly must remain mandatory delivery crons.', {})
    check('seo_cro_readonly_preview_cron', (op_by_id.get('LK-AUTO-003') or {}).get('status') == 'active_existing_agent_cron_readonly_preview', 'fail', 'SEO/CRO cron must remain read-only preview.', {})
    check('ledger_guard_passed', ledger.get('status') == 'passed' and (ledger.get('summary') or {}).get('fail_count') == 0, 'fail', 'LK-AUTO-004 ledger guard must pass.', ledger.get('summary'))
    check('klaviyo_ready_no_send', klaviyo.get('readiness_status') == 'ready_for_lucas_review_no_send' and (klaviyo.get('summary') or {}).get('campaign_sends') == 0 and (klaviyo.get('summary') or {}).get('campaign_schedules') == 0, 'fail', 'LK-AUTO-005 must be review-ready with no send/schedule.', klaviyo.get('summary'))
    check('sourcing_ready_no_external_action', sourcing.get('readiness_status') == 'ready_for_per_item_lucas_julio_decision_no_external_action' and (sourcing.get('summary') or {}).get('external_marketplace_calls') == 0 and (sourcing.get('summary') or {}).get('supplier_contacts') == 0 and (sourcing.get('summary') or {}).get('purchases') == 0, 'fail', 'LK-AUTO-006 must be decision-ready with no marketplace/supplier/purchase action.', sourcing.get('summary'))
    check('gmc_review_readonly_report_ready', (merchant.get('summary') or {}).get('merchant_center_id_present') is True and (merchant.get('summary') or {}).get('writes_allowed_now') == 0, 'fail', 'LK-AUTO-007 GMC Review must be read-only with no Merchant/feed/Shopify writes.', merchant.get('summary'))

    all_counts = {
        'n8n_flows_created': (op.get('summary') or {}).get('n8n_flows_created', 0) + (klaviyo.get('summary') or {}).get('n8n_flows_created', 0) + (sourcing.get('summary') or {}).get('n8n_flows_created', 0),
        'production_writes': (ledger.get('summary') or {}).get('production_writes', 0) + (klaviyo.get('summary') or {}).get('production_writes', 0) + (sourcing.get('summary') or {}).get('shopify_writes', 0) + (sourcing.get('summary') or {}).get('tiny_writes', 0) + (sourcing.get('summary') or {}).get('price_or_stock_changes', 0) + (merchant.get('summary') or {}).get('writes_allowed_now', 0),
        'external_sends_or_contacts': (ledger.get('summary') or {}).get('external_sends', 0) + (klaviyo.get('summary') or {}).get('campaign_sends', 0) + (klaviyo.get('summary') or {}).get('customer_contacts', 0) + (sourcing.get('summary') or {}).get('supplier_contacts', 0),
        'purchases_or_pos': (sourcing.get('summary') or {}).get('purchases', 0) + (sourcing.get('summary') or {}).get('purchase_orders', 0),
        'external_marketplace_calls': (sourcing.get('summary') or {}).get('external_marketplace_calls', 0),
    }
    check('no_new_external_or_write_actions', all(v == 0 for v in all_counts.values()), 'fail', 'Completion audit must show zero n8n, writes, sends/contacts, purchases and marketplace calls.', all_counts)
    check('p0_p1_delivery_semantics', (op.get('plain_language') or {}).get('delivery_rule') == 'Daily e Weekly são enviados sempre na cadência aprovada; P0/P1 só priorizam a leitura.', 'fail', 'P0/P1 must remain priority labels, not delivery triggers.', op.get('plain_language'))

    status_rows = [
        {'automation_id': 'LK-AUTO-001', 'name': 'Daily Sales Brief', 'final_status': 'active mandatory daily report', 'job_id': EXPECTED_CRONS['LK-AUTO-001']['job_id'], 'risk': 'low', 'allowed_now': 'send mandatory internal/origin report only', 'blocked': 'writes/campaigns/customer sends/n8n'},
        {'automation_id': 'LK-AUTO-002', 'name': 'Weekly CEO Review', 'final_status': 'active mandatory weekly report', 'job_id': EXPECTED_CRONS['LK-AUTO-002']['job_id'], 'risk': 'low', 'allowed_now': 'send mandatory internal/origin report only', 'blocked': 'writes/campaigns/customer sends/n8n'},
        {'automation_id': 'LK-AUTO-003', 'name': 'SEO/CRO weekly loop', 'final_status': 'active read-only preview cron', 'job_id': EXPECTED_CRONS['LK-AUTO-003']['job_id'], 'risk': 'low', 'allowed_now': 'generate preview/queue', 'blocked': 'Shopify/Merchant/GSC/theme writes without approval'},
        {'automation_id': 'LK-AUTO-004', 'name': 'Approval Learning Ledger refresh', 'final_status': 'manual guard passed', 'job_id': '', 'risk': 'low', 'allowed_now': 'manual ledger refresh/validation', 'blocked': 'auto-approve/auto-execute/cron'},
        {'automation_id': 'LK-AUTO-005', 'name': 'Klaviyo CRM draft watcher', 'final_status': 'manual read-only readiness ready, no send', 'job_id': '', 'risk': 'medium', 'allowed_now': 'verify draft IDs/status via GET', 'blocked': 'send/schedule/flow/customer contact/deep link guessing'},
        {'automation_id': 'LK-AUTO-006', 'name': 'On-demand sourcing router', 'final_status': 'manual per-item readiness ready, no external action', 'job_id': '', 'risk': 'medium', 'allowed_now': 'decision queue/readiness only', 'blocked': 'marketplace calls/supplier contact/purchase/PO/write/full-sync'},
        {'automation_id': 'LK-AUTO-007', 'name': 'GMC Review', 'final_status': 'active mandatory weekly read-only report', 'job_id': EXPECTED_CRONS['LK-AUTO-007']['job_id'], 'risk': 'low', 'allowed_now': 'read Merchant Center statuses and deliver internal/origin report', 'blocked': 'Merchant/feed/Shopify/GSC writes, content publish, campaigns/sends'},
    ]

    fail_count = sum(1 for c in checks if not c['ok'] and c['severity'] == 'fail')
    warn_count = sum(1 for c in checks if not c['ok'] and c['severity'] == 'warn')
    return {
        'generated_at': now(),
        'scope': 'LK OS Phase 8 completion audit: safe-by-default automations final state',
        'completion_status': 'phase8_complete_with_guardrails' if fail_count == 0 else 'blocked_needs_fix',
        'summary': {
            'automations_tracked': 7,
            'active_crons': 4,
            'mandatory_deliveries': 3,
            'readonly_preview_crons': 1,
            'manual_guards_ready': 3,
            'medium_risk_manual_only': 2,
            'checks': len(checks),
            'fail_count': fail_count,
            'warn_count': warn_count,
            **all_counts,
        },
        'final_state': status_rows,
        'checks': checks,
        'rollback': {
            'LK-AUTO-001': 'pause/remove cron 7c688553e293',
            'LK-AUTO-002': 'pause/remove cron 953b9055458e',
            'LK-AUTO-003': 'pause/remove cron 15777e3416dc',
            'LK-AUTO-007': 'pause/remove cron d4c26da4cd48',
            'manual_artifacts': 'revert PR or supersede report; no recurring job exists for LK-AUTO-004/005/006',
        },
        'next_gates': [
            'Monitor first Daily mandatory report delivery at 2026-05-12 08:00 BRT.',
            'Monitor first Weekly mandatory report delivery at 2026-05-18 09:00 BRT.',
            'Keep SEO/CRO as preview; write actions require explicit preview approval.',
            'Monitor first GMC Review mandatory report delivery at 2026-05-14 09:00 BRT.',
            'Klaviyo remains no-send until Lucas explicitly approves a send/schedule packet.',
            'Sourcing remains per-item only; no marketplace lookup/contact/purchase without named approval.',
        ],
    }


def write_outputs(payload: dict[str, Any]) -> None:
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    with OUT_CSV.open('w', encoding='utf-8', newline='') as f:
        fields = ['automation_id', 'name', 'final_status', 'job_id', 'risk', 'allowed_now', 'blocked']
        writer = csv.DictWriter(f, fieldnames=fields, lineterminator='\n')
        writer.writeheader()
        writer.writerows(payload['final_state'])
    s = payload['summary']
    lines = [
        '# LK Phase 8 Completion Audit, 2026-05-11', '',
        f"Generated at: `{payload['generated_at']}`", '',
        '## Veredito', '',
        f"Status: `{payload['completion_status']}`", '',
        'Fase 8 consolidada após reconciliação do PRD: 7 automações LK-AUTO têm estado final documentado, rollback e próximos gates. O que está ativo é read-only/preview ou report obrigatório interno; medium risk permanece manual.', '',
        '## Snapshot', '',
        f"- Automations tracked: {s['automations_tracked']}",
        f"- Active crons: {s['active_crons']}",
        f"- Mandatory deliveries: {s['mandatory_deliveries']}",
        f"- Read-only preview crons: {s['readonly_preview_crons']}",
        f"- Manual guards ready: {s['manual_guards_ready']}",
        f"- Medium risk manual-only: {s['medium_risk_manual_only']}",
        f"- Checks: {s['checks']}",
        f"- Fails: {s['fail_count']}",
        f"- Warnings: {s['warn_count']}",
        f"- n8n flows created: {s['n8n_flows_created']}",
        f"- Production writes: {s['production_writes']}",
        f"- External sends/contacts: {s['external_sends_or_contacts']}",
        f"- Purchases/POs: {s['purchases_or_pos']}",
        f"- External marketplace calls: {s['external_marketplace_calls']}", '',
        '## Estado final', '',
    ]
    for row in payload['final_state']:
        lines.extend([
            f"### {row['automation_id']} | {row['name']}",
            f"- Status: {row['final_status']}",
            f"- Job ID: `{row['job_id'] or 'n/a'}`",
            f"- Risco: {row['risk']}",
            f"- Permitido agora: {row['allowed_now']}",
            f"- Bloqueado: {row['blocked']}", '',
        ])
    lines.extend(['## Checks', ''])
    for c in payload['checks']:
        mark = 'OK' if c['ok'] else c['severity'].upper()
        lines.append(f"- {mark}: `{c['name']}` — {c['detail']}")
    lines.extend(['', '## Rollback', ''])
    for k, v in payload['rollback'].items():
        lines.append(f'- {k}: {v}')
    lines.extend(['', '## Próximos gates', ''])
    for g in payload['next_gates']:
        lines.append(f'- {g}')
    text = '\n'.join(lines) + '\n'
    OUT_MD.write_text(text, encoding='utf-8')
    BRAIN_DOC.write_text(text, encoding='utf-8')


def main() -> None:
    payload = build()
    write_outputs(payload)
    print(json.dumps({'ok': payload['summary']['fail_count'] == 0, 'status': payload['completion_status'], 'summary': payload['summary']}, ensure_ascii=False))
    if payload['summary']['fail_count']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
