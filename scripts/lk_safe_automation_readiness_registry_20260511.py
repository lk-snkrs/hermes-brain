#!/usr/bin/env python3
"""LK OS safe automation readiness registry.

Builds the Phase 8 automation candidate list without creating cron jobs, n8n flows,
external sends, database writes, Shopify writes, or production changes.
"""
from __future__ import annotations

import csv
import json
import pathlib
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT_JSON = ROOT / 'reports/lk-safe-automation-readiness-registry-2026-05-11.json'
OUT_CSV = ROOT / 'reports/lk-safe-automation-readiness-registry-2026-05-11.csv'
OUT_MD = ROOT / 'reports/lk-safe-automation-readiness-registry-2026-05-11.md'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/safe-automation-readiness-registry-2026-05-11.md'


def candidate(**kw: Any) -> dict[str, Any]:
    base = {
        'automation_id': '',
        'name': '',
        'source_artifacts': [],
        'trigger': '',
        'cadence_candidate': '',
        'mode_now': 'dry_run_only',
        'risk_level': 'low',
        'approval_required_before_activation': True,
        'silent_ok_contract': '',
        'alert_conditions': [],
        'rollback_plan': [],
        'dry_run_test': '',
        'activation_blockers': [],
        'allowed_now': ['generate local report', 'update Brain artifact via PR'],
        'forbidden_now': [],
        'recommended_next_step': '',
    }
    base.update(kw)
    return base


def build() -> dict[str, Any]:
    candidates = [
        candidate(
            automation_id='LK-AUTO-001',
            name='Daily Sales Brief read-only',
            source_artifacts=['areas/lk/rotinas/daily-sales-brief-readonly-2026-05-11.md'],
            trigger='Every business morning or on demand',
            cadence_candidate='daily 08:00 BRT',
            risk_level='low',
            silent_ok_contract='If generated successfully with no material anomaly, stay silent or save to Brain only; alert only on relevant sales/stock anomaly.',
            alert_conditions=['Shopify read fails', 'GA4 read fails', 'Tiny read fails', 'material revenue/session drop', 'stock rupture in P0 item'],
            rollback_plan=['Pause/remove cron if created', 'delete generated local report if wrong', 'no external state to revert in dry-run mode'],
            dry_run_test='Run the existing read-only briefing script/report generation manually and verify no PII/secrets before any recurring delivery.',
            forbidden_now=['Telegram auto-send', 'email send', 'WhatsApp send', 'Shopify/Tiny writes'],
            recommended_next_step='Run 3 manual dry-runs on separate days before cron approval.',
        ),
        candidate(
            automation_id='LK-AUTO-002',
            name='Weekly CEO Review read-only',
            source_artifacts=['areas/lk/rotinas/weekly-ceo-review-readonly-2026-05-11.md'],
            trigger='Closed week available',
            cadence_candidate='weekly Monday 09:00 BRT',
            risk_level='low',
            silent_ok_contract='Save report quietly; alert Lucas only if P0/P1 decisions are generated or data source is stale.',
            alert_conditions=['P0/P1 stock/sales decision appears', 'source freshness stale', 'material attribution anomaly'],
            rollback_plan=['Pause/remove cron', 'mark report superseded if methodology wrong'],
            dry_run_test='Generate next weekly review locally with Shopify+GA4+Tiny read-only and compare source freshness labels.',
            forbidden_now=['recurring Telegram delivery', 'campaign/customer action', 'stock/price writes'],
            recommended_next_step='Candidate for first read-only cron after one more clean manual run.',
        ),
        candidate(
            automation_id='LK-AUTO-003',
            name='SEO/CRO weekly monitor read-only',
            source_artifacts=['areas/lk/rotinas/seo-cro-weekly-improvement-loop.md', 'areas/lk/rotinas/approval-learning-ledger-2026-05-11.md'],
            trigger='Weekly SEO data window closed',
            cadence_candidate='weekly Monday 10:00 BRT',
            risk_level='low',
            silent_ok_contract='Alert only when new P1/P2 SEO opportunity or Merchant issue appears; do not auto-write Shopify.',
            alert_conditions=['new P1 GSC opportunity', 'Merchant disapproval spike', 'PDP traffic high with zero/low conversion'],
            rollback_plan=['Pause/remove cron', 'discard generated preview', 'no Shopify rollback because writes are blocked'],
            dry_run_test='Run Search Console, Merchant, PDP low-conversion routers manually and confirm writes_allowed_now=0.',
            forbidden_now=['Shopify SEO writes', 'H1/body/theme edits', 'Merchant/feed writes', 'Indexing API submits'],
            recommended_next_step='Safe as read-only monitor only after Lucas approves cadence/delivery.',
        ),
        candidate(
            automation_id='LK-AUTO-004',
            name='Approval Learning Ledger refresh',
            source_artifacts=['areas/lk/rotinas/approval-learning-ledger-2026-05-11.md'],
            trigger='After any approval/correction/execution artifact changes',
            cadence_candidate='on-demand or post-PR hook, not time-based initially',
            risk_level='low',
            silent_ok_contract='No message unless a pending item changes status or a contradiction is detected.',
            alert_conditions=['executed item appears again as needs_approval', 'pending_future item is proposed for execution', 'missing rollback for executed write'],
            rollback_plan=['Revert ledger PR', 'regenerate from source artifacts'],
            dry_run_test='Regenerate ledger locally and compare counts/status with source artifacts.',
            forbidden_now=['automatic approval', 'automatic execution', 'external notifications'],
            recommended_next_step='Keep as manual post-action step until ledger pattern stabilizes.',
        ),
        candidate(
            automation_id='LK-AUTO-005',
            name='Klaviyo CRM draft watcher',
            source_artifacts=['areas/lk/projetos/lk-os-implementation-control.md'],
            trigger='CRM/RFM segment or campaign draft changes',
            cadence_candidate='manual only for now',
            risk_level='medium',
            silent_ok_contract='No automatic send; only surface draft readiness/risks.',
            alert_conditions=['campaign not in draft', 'deep link unverified', 'PII leakage risk', 'duplicate product cards'],
            rollback_plan=['Disable watcher', 'do not send campaign', 'revert draft metadata only after preview'],
            dry_run_test='List campaign/draft IDs read-only and produce readiness packet without UI deep links unless verified.',
            activation_blockers=['Requires platform-specific safe Klaviyo read-only implementation and Lucas approval'],
            forbidden_now=['send campaign', 'schedule campaign', 'customer contact', 'unverified deep link in output'],
            recommended_next_step='Do not automate yet; keep on-demand readiness preview.',
        ),
        candidate(
            automation_id='LK-AUTO-006',
            name='On-demand sourcing router',
            source_artifacts=['areas/lk/rotinas/on-demand-sourcing-router-readonly-2026-05-11.md', 'areas/lk/rotinas/approval-learning-ledger-2026-05-11.md'],
            trigger='Approved needs_approval sourcing decision only',
            cadence_candidate='event/manual only',
            risk_level='medium',
            silent_ok_contract='No background full-sync; run only for named approved item and return preview.',
            alert_conditions=['approved decision missing destination', 'supplier/contact target unclear', 'lead time/cost data missing'],
            rollback_plan=['Cancel run before send', 'archive generated lookup as superseded', 'no supplier contact without separate approval'],
            dry_run_test='Given one approved mock decision, generate a no-contact lookup plan and verify no network contact/send occurs.',
            activation_blockers=['Needs explicit Lucas/Júlio approval per item'],
            forbidden_now=['supplier contact', 'purchase commitment', 'full-sync prices', 'stock write'],
            recommended_next_step='Wait for one specific sourcing approval; do not create cron.',
        ),
    ]
    counts: dict[str, int] = {}
    risks: dict[str, int] = {}
    for c in candidates:
        counts[c['mode_now']] = counts.get(c['mode_now'], 0) + 1
        risks[c['risk_level']] = risks.get(c['risk_level'], 0) + 1
    return {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'LK OS Phase 8 safe automation readiness registry',
        'mode': 'planning_and_dry_run_only',
        'summary': {
            'candidate_automations': len(candidates),
            'mode_counts': counts,
            'risk_counts': risks,
            'crons_created': 0,
            'n8n_flows_created': 0,
            'external_sends': 0,
            'production_writes': 0,
            'activation_requires_lucas_approval': len(candidates),
        },
        'candidates': candidates,
        'global_activation_gates': [
            'At least one clean manual dry-run for each automation before approval request.',
            'Secret/PII scan clean on generated artifacts.',
            'Rollback/pause command documented before cron/n8n activation.',
            'Silent-OK contract defined: no spam when everything is normal.',
            'Medium/high risk automations require explicit Lucas approval with cadence and delivery target.',
        ],
    }


def write_outputs(payload: dict[str, Any]) -> None:
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    fields = ['automation_id','name','risk_level','mode_now','cadence_candidate','approval_required_before_activation','recommended_next_step']
    with OUT_CSV.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for c in payload['candidates']:
            w.writerow({k: c.get(k) for k in fields})
    s = payload['summary']
    lines = [
        '# LK Safe Automation Readiness Registry, 2026-05-11', '',
        f"Generated at: `{payload['generated_at']}`", '',
        '## Veredito', '',
        'Fase 8 foi aberta no modo correto: catálogo e dry-run, sem criar cron, n8n, envio externo ou write produtivo.', '',
        '## Snapshot', '',
        f"- Automações candidatas: {s['candidate_automations']}",
        f"- Crons criados: {s['crons_created']}",
        f"- n8n flows criados: {s['n8n_flows_created']}",
        f"- Envios externos: {s['external_sends']}",
        f"- Writes produtivos: {s['production_writes']}",
        f"- Ativações exigindo aprovação Lucas: {s['activation_requires_lucas_approval']}", '',
        '## Gates globais de ativação', '',
    ]
    for gate in payload['global_activation_gates']:
        lines.append(f'- {gate}')
    lines.extend(['', '## Automações candidatas', ''])
    for c in payload['candidates']:
        lines.extend([
            f"### {c['automation_id']} · {c['name']}", '',
            f"- Risco: `{c['risk_level']}`",
            f"- Modo agora: `{c['mode_now']}`",
            f"- Cadência candidata: {c['cadence_candidate']}",
            f"- Contrato silent-OK: {c['silent_ok_contract']}",
            f"- Dry-run: {c['dry_run_test']}",
            f"- Próximo passo recomendado: {c['recommended_next_step']}",
            f"- Proibido agora: {', '.join(c['forbidden_now'])}", '',
        ])
    text = '\n'.join(lines) + '\n'
    OUT_MD.write_text(text, encoding='utf-8')
    BRAIN_DOC.write_text(text, encoding='utf-8')


def main() -> None:
    payload = build()
    write_outputs(payload)
    print(json.dumps({'ok': True, 'summary': payload['summary']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
