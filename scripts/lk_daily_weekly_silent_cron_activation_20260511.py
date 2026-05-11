#!/usr/bin/env python3
"""Record LK Daily + Weekly silent cron activation.

This script only writes local Brain/report artifacts documenting cron activation.
It does not create jobs itself and does not call external business systems.
"""
from __future__ import annotations

import json
import pathlib
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT_JSON = ROOT / 'reports/lk-daily-weekly-silent-cron-activation-2026-05-11.json'
OUT_MD = ROOT / 'reports/lk-daily-weekly-silent-cron-activation-2026-05-11.md'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/daily-weekly-silent-cron-activation-2026-05-11.md'
VALIDATION = ROOT / 'reports/lk-daily-weekly-dry-run-validation-2026-05-11.json'


def build() -> dict[str, Any]:
    validation = json.loads(VALIDATION.read_text(encoding='utf-8'))
    jobs = [
        {
            'automation_id': 'LK-AUTO-001',
            'job_id': '7c688553e293',
            'name': 'LK Daily Sales Brief read-only silent watchdog',
            'schedule_utc': '0 11 * * *',
            'schedule_brt': 'daily 08:00 BRT',
            'script': '/opt/data/scripts/lk_daily_sales_brief_watchdog.py',
            'no_agent': True,
            'deliver': 'origin',
            'next_run_at_utc': '2026-05-12T11:00:00+00:00',
            'silent_ok_contract': 'rc=0 + empty stdout stays silent; rc=0 + stdout alerts; nonzero rc sends watchdog failure.',
            'alert_only_when': ['P0/P1 anomaly', 'API/source failure', 'explicit script failure'],
            'blocked_actions': ['n8n_flow', 'campaign', 'Shopify write', 'Tiny write', 'Klaviyo send', 'WhatsApp send', 'supplier contact'],
        },
        {
            'automation_id': 'LK-AUTO-002',
            'job_id': '953b9055458e',
            'name': 'LK Weekly CEO Review read-only silent watchdog',
            'schedule_utc': '0 12 * * 1',
            'schedule_brt': 'weekly Monday 09:00 BRT',
            'script': '/opt/data/scripts/lk_weekly_ceo_review_watchdog.py',
            'no_agent': True,
            'deliver': 'origin',
            'next_run_at_utc': '2026-05-18T12:00:00+00:00',
            'silent_ok_contract': 'rc=0 + empty stdout stays silent; rc=0 + stdout alerts; nonzero rc sends watchdog failure.',
            'alert_only_when': ['P0/P1 anomaly', 'API/source failure', 'explicit script failure'],
            'blocked_actions': ['n8n_flow', 'campaign', 'Shopify write', 'Tiny write', 'Klaviyo send', 'WhatsApp send', 'supplier contact'],
        },
    ]
    return {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'LK Phase 8 activation for Daily + Weekly read-only silent watchdog cronjobs',
        'approval_interpretation': 'Lucas said “Seguir” after the exact proposed cadence/delivery gate for Daily 08:00 BRT and Weekly Monday 09:00 BRT.',
        'validation_source': str(VALIDATION.relative_to(ROOT)),
        'validation_summary': validation.get('summary'),
        'summary': {
            'cronjobs_created': len(jobs),
            'no_agent_jobs': len([j for j in jobs if j['no_agent']]),
            'n8n_flows_created': 0,
            'telegram_immediate_sends': 0,
            'external_sends_now': 0,
            'production_writes_now': 0,
            'business_system_writes_allowed': 0,
            'silent_ok_enabled': len(jobs),
        },
        'jobs': jobs,
        'rollback': [
            'Pause/remove job_id 7c688553e293 for Daily.',
            'Pause/remove job_id 953b9055458e for Weekly.',
            'Cron scripts are local at /opt/data/scripts and can be edited/disabled without touching Shopify/Tiny/GA4.',
        ],
    }


def write_outputs(payload: dict[str, Any]) -> None:
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    s = payload['summary']
    lines = [
        '# LK Daily + Weekly Silent Cron Activation, 2026-05-11', '',
        f"Generated at: `{payload['generated_at']}`", '',
        '## Veredito', '',
        'Daily Sales Brief e Weekly CEO Review foram ativados como cronjobs read-only, `no_agent`, com contrato silent-OK. Isso cria recorrência operacional sem n8n, sem envio imediato e sem write produtivo.', '',
        '## Snapshot', '',
        f"- Cronjobs criados: {s['cronjobs_created']}",
        f"- Jobs no_agent: {s['no_agent_jobs']}",
        f"- n8n flows criados: {s['n8n_flows_created']}",
        f"- Telegram sends imediatos: {s['telegram_immediate_sends']}",
        f"- Envios externos agora: {s['external_sends_now']}",
        f"- Writes produtivos agora: {s['production_writes_now']}", '',
        '## Jobs', '',
    ]
    for job in payload['jobs']:
        lines.extend([
            f"### {job['automation_id']} · {job['name']}", '',
            f"- Job ID: `{job['job_id']}`",
            f"- Agenda UTC: `{job['schedule_utc']}`",
            f"- Agenda BRT: {job['schedule_brt']}",
            f"- Script: `{job['script']}`",
            f"- no_agent: `{job['no_agent']}`",
            f"- Próxima execução: `{job['next_run_at_utc']}`",
            f"- Silent-OK: {job['silent_ok_contract']}",
            f"- Alerta só quando: {', '.join(job['alert_only_when'])}", '',
        ])
    lines.extend(['## Rollback', ''])
    for item in payload['rollback']:
        lines.append(f'- {item}')
    lines.extend(['', '## Não realizado', '', '- Nenhum n8n flow criado.', '- Nenhum envio imediato executado.', '- Nenhuma campanha enviada/agendada.', '- Nenhum write em Shopify/Tiny/Merchant/GSC/produção.'])
    text = '\n'.join(lines) + '\n'
    OUT_MD.write_text(text, encoding='utf-8')
    BRAIN_DOC.write_text(text, encoding='utf-8')


def main() -> None:
    payload = build()
    write_outputs(payload)
    print(json.dumps({'ok': True, 'summary': payload['summary']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
