# Receipt — Elle Observer Reports rescheduled

Date: 2026-06-14
Owner: lk-ops
Scope: Local Hermes cron registry only (`/opt/data/profiles/lk-ops/cron/jobs.json`).

## Change

Lucas corrected the preferred delivery window: reports should arrive around 17h / 17h10 BRT, not after 18h.

Updated jobs:

- `3f044d9c6f99` — LK Elle atendimento diário — seg-sex 17h10 BRT
  - cron: `10 20 * * 1-5` (20:10 UTC = 17:10 BRT)
  - next run: `2026-06-15T20:10:00+00:00`

- `45a6cd07c138` — LK Elle atendimento diário — sábado 17h10 BRT
  - cron: `10 20 * * 6` (20:10 UTC = 17:10 BRT)
  - next run: `2026-06-20T20:10:00+00:00`

- `74c828f4331b` — LK Elle atendimento semanal — sábado 17h00 BRT
  - cron: `0 20 * * 6` (20:00 UTC = 17:00 BRT)
  - next run: `2026-06-20T20:00:00+00:00`

## Verification

Read-only verification with:

`HERMES_HOME=/opt/data/profiles/lk-ops /opt/hermes/.venv/bin/hermes cron list`

Confirmed all three jobs active with the updated schedules and `deliver: origin`.

## Notes

No external systems were changed. No Shopify, Chatwoot, Tiny, WhatsApp, Docker, or gateway mutation performed.
