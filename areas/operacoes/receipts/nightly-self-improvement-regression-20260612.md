# Receipt — nightly self-improvement regression added

Date: 2026-06-12
Scope: add recent auto-improvement checks to existing madrugada cron
Values printed: false
External writes: 0
New cron jobs created: 0
Runtime/Docker/VPS/Traefik mutations: 0
Cron prompt/registry backup: `/opt/data/backups/nightly-self-improvement-cron-registry-20260612T225225Z/jobs.json.before`

## Implemented

The existing 02:00 BRT job `LC Hermes daily intelligence loop — systemwide audit + self-improvement` already runs script:

- `/opt/data/scripts/hermes_daily_intelligence_preflight.py`

This script was upgraded from schema `lc_hermes_daily_intelligence_preflight.v3` to `v4` and now includes:

- `nightly_self_improvement_regression`

## Checks added

- Reminder OS health gate
- Reminder OS ingress audit
- Reminder OS watchdog silent-OK
- Hermes all Telegram gateways watchdog silent-OK
- Memory OS daytime alerting watchdog silent-OK
- Memory OS latest/daytime/scorecard status artifacts
- Reminder OS synthetic cross-agent test

## Alert behavior

- Healthy state stays local/silent.
- If regression status is not `ok`, it is added to `alert_dedupe` as `nightly_self_improvement_regression_attention` and then to the mistake ledger for safe next action.
- No reminders are executed automatically.
- No gateway restart is requested by this nightly gate.

## Local artifact

Latest local regression artifact:

- `reports/hermes-self-improvement-regression/latest.json`

## Verification

Fresh run after implementation:

- `python3 -m py_compile /opt/data/scripts/hermes_daily_intelligence_preflight.py`: ok
- `python3 /opt/data/scripts/hermes_daily_intelligence_preflight.py`: ok
- schema: `lc_hermes_daily_intelligence_preflight.v4`
- `nightly_status`: `ok`
- `nightly_issues`: `[]`
- `reminder_health`: ok
- `reminder_ingress`: ok
- `reminder_watchdog`: silent-OK
- `gateway_watchdog`: silent-OK
- `memory_daytime`: silent-OK
- `synthetic_cross_agent`: ok

Cron registry readback:

- job: `LC Hermes daily intelligence loop — systemwide audit + self-improvement`
- schedule: `0 5 * * *` / 02:00 BRT
- script: `hermes_daily_intelligence_preflight.py`
- enabled: true
- next run: 2026-06-13T05:00:00+00:00
