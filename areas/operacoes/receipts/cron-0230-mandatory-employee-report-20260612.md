# Receipt — Cron 02h30 obrigatório como relatório de funcionário

Date: 2026-06-12
Scope: Hermes daily 02h30 Telegram digest contract
Values printed: false
External writes: 0
New cron jobs created: 0
Docker/VPS/Traefik/gateway/container changes: 0

## Lucas correction

Lucas clarified that the 02h30 cron must always report what the other crons did, like an employee giving a daily work report. It must never be silent.

## Updated job

- Name: `Relatório Hermes diário 01h+02h+02h15 para Lucas — Telegram obrigatório`
- Schedule: `30 5 * * *` / 02h30 BRT
- Delivery: `origin`
- Enabled/state: enabled + scheduled
- Context sources: 01h Brain fechamento, 02h Daily Intelligence, 02h15 Memory Hygiene

## Contract added

- Always produce a final Telegram message.
- This job is not a silent-OK watchdog.
- Healthy/no-actionable runs still report what was verified and what it means operationally.
- Summarize 01h, 02h, 02h15 and relevant watchdog/autoheal changes from the last 24h.
- Tone: competent employee reporting what was done, what changed, what stayed healthy, what needs Lucas, and next safe step.
- Do not expose job IDs, raw JSON, scheduler internals, wrappers, logs, secrets, or boilerplate.

## Backup

- `/opt/data/backups/cron-0230-mandatory-employee-report-20260612T231557Z/jobs.json.before`

## Verification

- `enabled=True`
- `state=scheduled`
- `deliver=origin`
- `schedule=30 5 * * *`
- `mandatory_block=True`
- `always_final_message=True`
- `never_silent=True`
