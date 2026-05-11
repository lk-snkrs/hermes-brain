#!/usr/bin/env python3
"""LK Phase 8 operational automation registry.

Reconciles the original readiness registry with the cron jobs actually active
after Lucas corrected Daily/Weekly delivery semantics.
This script writes only local Brain/report artifacts.
"""
from __future__ import annotations

import csv
import json
import pathlib
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT_JSON = ROOT / 'reports/lk-phase8-operational-automation-registry-2026-05-11.json'
OUT_CSV = ROOT / 'reports/lk-phase8-operational-automation-registry-2026-05-11.csv'
OUT_MD = ROOT / 'reports/lk-phase8-operational-automation-registry-2026-05-11.md'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/phase8-operational-automation-registry-2026-05-11.md'

AUTOMATIONS: list[dict[str, Any]] = [
    {
        'automation_id': 'LK-AUTO-001',
        'name': 'Daily Sales Brief read-only mandatory delivery',
        'status': 'active_cron_mandatory_delivery',
        'risk_level': 'low',
        'cadence_brt': 'daily 08:00 BRT',
        'cron_schedule_utc': '0 11 * * *',
        'job_id': '7c688553e293',
        'delivery': 'origin/Telegram',
        'execution_mode': 'no_agent script',
        'script': '/opt/data/scripts/lk_daily_sales_brief_watchdog.py',
        'contract': 'Always deliver the generated daily report; P0/P1 only prioritize content.',
        'writes_allowed': 0,
        'external_actions_allowed': 0,
        'rollback': 'cronjob list, then pause/remove job_id 7c688553e293.',
        'next_gate': 'Monitor first scheduled delivery on 2026-05-12 08:00 BRT.',
    },
    {
        'automation_id': 'LK-AUTO-002',
        'name': 'Weekly CEO Review read-only mandatory delivery',
        'status': 'active_cron_mandatory_delivery',
        'risk_level': 'low',
        'cadence_brt': 'weekly Monday 09:00 BRT',
        'cron_schedule_utc': '0 12 * * 1',
        'job_id': '953b9055458e',
        'delivery': 'origin/Telegram',
        'execution_mode': 'no_agent script',
        'script': '/opt/data/scripts/lk_weekly_ceo_review_watchdog.py',
        'contract': 'Always deliver the generated weekly report; P0/P1 only prioritize content.',
        'writes_allowed': 0,
        'external_actions_allowed': 0,
        'rollback': 'cronjob list, then pause/remove job_id 953b9055458e.',
        'next_gate': 'Monitor first scheduled delivery on 2026-05-18 09:00 BRT.',
    },
    {
        'automation_id': 'LK-AUTO-003',
        'name': 'SEO/CRO weekly Claude SEO improvement loop',
        'status': 'active_existing_agent_cron_readonly_preview',
        'risk_level': 'low',
        'cadence_brt': 'weekly Monday 10:00 BRT',
        'cron_schedule_utc': '0 13 * * 1',
        'job_id': '15777e3416dc',
        'delivery': 'origin/Telegram',
        'execution_mode': 'agent cron with SEO skills',
        'script': '',
        'contract': 'Generate read-only SEO/CRO queue and previews; writes require explicit approval.',
        'writes_allowed': 0,
        'external_actions_allowed': 0,
        'rollback': 'cronjob list, then pause/remove job_id 15777e3416dc.',
        'next_gate': 'Keep as read-only preview loop; do not auto-apply Shopify/Merchant/theme changes.',
    },
    {
        'automation_id': 'LK-AUTO-004',
        'name': 'Approval Learning Ledger refresh',
        'status': 'manual_post_action_only',
        'risk_level': 'low',
        'cadence_brt': 'after approval/correction/execution artifacts, manual',
        'cron_schedule_utc': '',
        'job_id': '',
        'delivery': 'Brain artifact/PR only',
        'execution_mode': 'manual script',
        'script': 'scripts/lk_os_approval_learning_ledger_20260511.py',
        'contract': 'Regenerate after meaningful decisions; do not auto-approve or auto-execute.',
        'writes_allowed': 0,
        'external_actions_allowed': 0,
        'rollback': 'revert ledger PR or regenerate from source artifacts.',
        'next_gate': 'Stay manual until pattern stabilizes; possible post-PR hook later with separate approval.',
    },
    {
        'automation_id': 'LK-AUTO-005',
        'name': 'Klaviyo CRM draft watcher',
        'status': 'blocked_manual_readiness_only',
        'risk_level': 'medium',
        'cadence_brt': 'manual only',
        'cron_schedule_utc': '',
        'job_id': '',
        'delivery': 'preview only',
        'execution_mode': 'not activated',
        'script': '',
        'contract': 'No send/schedule; only readiness and risk packet with verified IDs/links.',
        'writes_allowed': 0,
        'external_actions_allowed': 0,
        'rollback': 'no recurring job exists; discard/supersede readiness packet.',
        'next_gate': 'Needs Klaviyo read-only implementation and explicit Lucas approval.',
    },
    {
        'automation_id': 'LK-AUTO-006',
        'name': 'On-demand sourcing router',
        'status': 'manual_per_item_approval_only',
        'risk_level': 'medium',
        'cadence_brt': 'manual/event only',
        'cron_schedule_utc': '',
        'job_id': '',
        'delivery': 'preview only',
        'execution_mode': 'manual script',
        'script': 'scripts/lk_os_on_demand_sourcing_router_20260511.py',
        'contract': 'Run only for named approved item; no full-sync, supplier contact, purchase, price or stock write.',
        'writes_allowed': 0,
        'external_actions_allowed': 0,
        'rollback': 'no recurring job exists; cancel before contact/purchase.',
        'next_gate': 'Needs explicit Lucas/Júlio approval per item and real lead-time/cost parameters.',
    },
]


def build() -> dict[str, Any]:
    counts: dict[str, int] = {}
    risk_counts: dict[str, int] = {}
    for a in AUTOMATIONS:
        counts[a['status']] = counts.get(a['status'], 0) + 1
        risk_counts[a['risk_level']] = risk_counts.get(a['risk_level'], 0) + 1
    return {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'LK OS Phase 8 operational automation registry after mandatory Daily/Weekly correction',
        'summary': {
            'automations_tracked': len(AUTOMATIONS),
            'active_cron_jobs': len([a for a in AUTOMATIONS if a['job_id']]),
            'mandatory_report_deliveries': 2,
            'active_readonly_preview_crons': 1,
            'manual_only_or_blocked': len([a for a in AUTOMATIONS if not a['job_id']]),
            'n8n_flows_created': 0,
            'production_writes_allowed': 0,
            'external_actions_allowed': 0,
            'status_counts': counts,
            'risk_counts': risk_counts,
        },
        'plain_language': {
            'p0': 'Urgente hoje; pode exigir ação no mesmo dia.',
            'p1': 'Importante acompanhar/decidir; não é necessariamente incêndio.',
            'delivery_rule': 'Daily e Weekly são enviados sempre na cadência aprovada; P0/P1 só priorizam a leitura.',
        },
        'automations': AUTOMATIONS,
    }


def write_outputs(payload: dict[str, Any]) -> None:
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    with OUT_CSV.open('w', encoding='utf-8', newline='') as f:
        fields = ['automation_id','name','status','risk_level','cadence_brt','cron_schedule_utc','job_id','delivery','execution_mode','contract','writes_allowed','external_actions_allowed','next_gate']
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in payload['automations']:
            writer.writerow({k: row.get(k, '') for k in fields})
    s = payload['summary']
    lines = [
        '# LK Phase 8 Operational Automation Registry, 2026-05-11', '',
        f"Generated at: `{payload['generated_at']}`", '',
        '## Veredito', '',
        'A Fase 8 agora tem um registro operacional reconciliado: Daily e Weekly são entregas obrigatórias; SEO/CRO weekly já existe como cron read-only de preview; ledger, Klaviyo e sourcing continuam manuais/bloqueados conforme risco.', '',
        '## P0/P1 em linguagem simples', '',
        f"- P0: {payload['plain_language']['p0']}",
        f"- P1: {payload['plain_language']['p1']}",
        f"- Regra de envio: {payload['plain_language']['delivery_rule']}", '',
        '## Resumo', '',
        f"- Automações rastreadas: {s['automations_tracked']}",
        f"- Cronjobs ativos: {s['active_cron_jobs']}",
        f"- Entregas obrigatórias: {s['mandatory_report_deliveries']}",
        f"- Crons read-only de preview: {s['active_readonly_preview_crons']}",
        f"- Manual-only ou bloqueadas: {s['manual_only_or_blocked']}",
        f"- n8n flows criados: {s['n8n_flows_created']}",
        f"- Writes produtivos permitidos: {s['production_writes_allowed']}", '',
        '## Automações', '',
    ]
    for a in payload['automations']:
        lines.extend([
            f"### {a['automation_id']} · {a['name']}", '',
            f"- Status: `{a['status']}`",
            f"- Risco: `{a['risk_level']}`",
            f"- Cadência: {a['cadence_brt'] or 'não recorrente'}",
            f"- Job ID: `{a['job_id'] or 'none'}`",
            f"- Entrega: {a['delivery']}",
            f"- Contrato: {a['contract']}",
            f"- Próximo gate: {a['next_gate']}", '',
        ])
    lines.extend(['## Guardrails', '', '- Nenhum n8n criado.', '- Nenhum write em Shopify/Tiny/Merchant/GSC.', '- Nenhuma campanha/envio para cliente/fornecedor.', '- Medium risk permanece manual com aprovação específica.'])
    text = '\n'.join(lines) + '\n'
    OUT_MD.write_text(text, encoding='utf-8')
    BRAIN_DOC.write_text(text, encoding='utf-8')


def main() -> None:
    payload = build()
    write_outputs(payload)
    print(json.dumps({'ok': True, 'summary': payload['summary']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
