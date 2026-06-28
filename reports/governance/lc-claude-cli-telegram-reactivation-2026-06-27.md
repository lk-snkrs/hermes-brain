# LC Claude CLI Telegram bot reactivation — 2026-06-27

Status: done / runtime verified.
values_printed=false

## Request
Lucas asked to reactivate `https://t.me/hermesclaude_lcbot`.

## Scope executed
- Identified the matching Hermes profile: `/opt/data/profiles/lc-claude-cli`.
- Validated the profile-local Telegram token with Bot API `getMe` without printing token values.
- Confirmed expected bot username: `hermesclaude_lcbot`.
- Backed up relevant local files before mutation.
- Updated the global Hermes profile watchdog so `lc-claude-cli` is now an explicitly managed Telegram gateway profile.
- Ran the watchdog to start the profile gateway with API/webhook surfaces forced off.
- Verified live runtime by exact `HERMES_HOME` process environment and Telegram state.

## Backup
Backup directory:
- `/opt/data/backups/lc-claude-cli-reactivation-20260627T231353Z`

Backed up:
- `/opt/data/scripts/hermes_all_gateway_watchdog.py`
- `/opt/data/profiles/lc-claude-cli/.env`
- `/opt/data/profiles/lc-claude-cli/config.yaml`

## Runtime evidence
- `getMe_ok=true`
- Bot username: `hermesclaude_lcbot`
- Token fingerprint only: `e98200edddc8`
- Live PID: `1756060`
- Live `HERMES_HOME`: `/opt/data/profiles/lc-claude-cli`
- `gateway_state`: `running`
- Telegram state: `connected`
- API server enabled: `false`
- API key present in live child env: `false`
- Webhook enabled: `false`
- Webhook secret present in live child env: `false`
- Lucas allowlist present: `true`
- Live process count for this profile: `1`

## Verification
- `/opt/data/scripts/hermes_all_gateway_watchdog.py` py_compile: OK
- Focused secret scan on touched watchdog script: 0 hits
- Brain health: All checks passed
- Gateway stdout log exists at `/opt/data/logs/hermes-all-gateway-watchdog/lc-claude-cli.stdout.log`; startup warning about missing `raft` CLI is non-blocking for Telegram connectivity.

## Safety
- Docker/VPS/Traefik: not touched
- Main/default gateway: not restarted
- Other specialist gateways: not restarted by this task
- API/webhook surfaces for this profile: forced off
- Telegram token values printed: 0
- External business writes: 0

## Remaining manual proof
The bot is connected and polling. Full Telegram round-trip proof still requires Lucas to send a message to `@hermesclaude_lcbot` and confirm it replies in that chat.
