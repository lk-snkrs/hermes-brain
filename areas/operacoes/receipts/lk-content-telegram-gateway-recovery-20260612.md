# Receipt — LK Content Telegram gateway recovery

Date: 2026-06-12
Profile: `lk-content`
Bot username: `@hermes_lk_producaodeconteudo_bot`
Values printed: false
External business writes: 0
Secrets printed: 0

## Problem
Lucas reported `@hermes_lk_producaodeconteudo_bot` stopped responding.

## Root cause
The live `lk-content` gateway process was running with the wrong Telegram bot identity inherited from the parent/default runtime environment. The profile-local `.env` token for `@hermes_lk_producaodeconteudo_bot` was valid, but the process had bound a different bot username.

## Actions taken
- Verified the profile-local Telegram token with Telegram `getMe` without printing token values.
- Backed up the global gateway watchdog before changes:
  - `/opt/data/backups/lk-content-gateway-token-fix-20260612T201819Z/`
- Patched `/opt/data/scripts/hermes_all_gateway_watchdog.py` so `lk-content` managed restarts explicitly load the profile-local `TELEGRAM_BOT_TOKEN` and do not inherit the default bot token.
- Added a scoped identity guard for `lk-content`: if a future live process has a different Telegram token from the profile-local token, the watchdog terminates it and restarts the profile with the correct identity.
- Restarted only the local `lk-content` gateway process; no Docker/VPS/Traefik/prod infrastructure changes.

## Verification
- `HERMES_HOME=/opt/data/profiles/lk-content hermes gateway status`: running.
- Live process count for `lk-content`: 1.
- Telegram `getMe`: ok.
- Live bot username: `hermes_lk_producaodeconteudo_bot`.
- `pending_update_count`: 0.
- Gateway mode: Telegram polling; webhook URL unset.
- `API_SERVER_ENABLED=false` and `WEBHOOK_ENABLED=false` in child process.
- `DOPPLER_TOKEN` absent from child process.
- Global watchdog dry-run stdout length: 0 (silent-OK).
- Watchdog script compile: ok.

## Guardrail
This does not guarantee physical impossibility of downtime. It does add automatic local recovery and identity mismatch correction via the existing 1-minute global gateway watchdog.
