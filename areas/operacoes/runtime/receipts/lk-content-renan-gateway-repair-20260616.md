# LK Content Telegram gateway repair — Renan allowlist / self-killing cron

- Date: 2026-06-16
- Scope: `/opt/data/profiles/lk-content` Telegram gateway only
- External writes: none
- Secret values printed: false

## Symptom

The LK Content Telegram bot connected to Telegram, discovered the group, then received SIGTERM seconds after `Cron ticker started`. Renan was already present in the live non-secret allowlist, but the profile gateway was unstable.

## Root cause

A profile-local one-shot cron job was still active:

- Job id: `a427776f4917`
- Name: `authorize-renan-lk-content-telegram`
- Script: `authorize_renan_lk_content_gateway_20260616.py`
- Previous state: `enabled=true`, `state=scheduled`, `repeat.completed=0`

Because the job was past-due, the LK Content gateway ran it immediately when its cron ticker started. The script included `restart_scoped_gateway()` and killed all live LK Content gateway PIDs, creating a self-SIGTERM loop.

## Fix applied

- Confirmed live allowlist contained Lucas and Renan without printing secret values.
- Backed up profile cron registry:
  - `/opt/data/profiles/lk-content/cron/jobs.json.before-disable-renan-restart-20260616T210443Z`
- Paused/disabled only job `a427776f4917` after its one-time purpose was complete.
- Restored `/opt/data/scripts/hermes_all_gateway_watchdog.py` `lk-content` entry to `mode=managed`.
- Resumed global watchdog job `b78ae7ac81d0`.
- Updated `lucas-runtime-operations` skill with the pitfall.

## Verification

- `lk-content` gateway live PID observed after >5 minutes and multiple cron ticks.
- Live process env checks (booleans only): token present, Lucas allowed, Renan allowed.
- No new shutdown diagnostic after `2026-06-16T20:57:17Z` during validation.
- Global watchdog job `b78ae7ac81d0` resumed and reported `last_status=ok`.

## Remaining manual verification

Ask Renan to send a message in `[LK] Produção de Conteúdo`. If the bot does not answer, inspect message routing/logs next; the process/runtime issue is fixed at time of receipt.
