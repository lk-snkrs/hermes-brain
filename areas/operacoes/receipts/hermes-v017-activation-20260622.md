# Hermes v0.17 runtime activation — 2026-06-22

Status: activated
Scope: default Hermes Telegram gateway runtime (`HERMES_HOME=/opt/data`)

## What was done

Lucas approved option 1 (`Fazer 1`) to activate the already-staged Hermes v0.17 update in the live Telegram gateway.

Actions performed:
- Captured pre-restart gateway roster.
- Ran scoped default gateway restart with `HERMES_HOME=/opt/data` and the active mounted venv.
- Validated the live post-restart runtime.
- Compared pre/post specialist gateway roster.
- Ran config, cron, memory, webhook, API health, and log checks.
- Secret-scanned run artifacts.

## Evidence

Run directory:
- `/opt/data/backups/hermes-v017-activation-20260622T100043Z`

Key files:
- `pre_gateway_roster.json`
- `restart.log`
- `post_failed_restart_probe.log`
- `post_restart_cli_checks.log`
- `post_restart_log_since_1003.log`
- `final_gateway_roster_strict.json`
- `final_health_check.log`

Validated state:
- Live default gateway restarted: yes
- Default PID after restart: `1`
- Runtime version via API health: `0.17.0`
- `hermes --version`: `Hermes Agent v0.17.0 (2026.6.19)`
- Config version: `30 ✓`
- Cron status: gateway running; 39 active jobs
- Memory provider: Honcho available
- Webhooks: 14 subscriptions listed
- Telegram startup log: connected in polling mode
- API server startup log: connected on port 8642
- Webhook startup log: connected on port 8644

Roster comparison:
- Pre profiles: 12
- Post profiles: 12
- Missing after restart: none
- Specialist API/webhook surfaces open after restart: none

## Notes

The restart command returned `rc=1` because it hit an `Another gateway instance is already running` race after PID 1 had already been replaced. Follow-up evidence showed the default gateway had a fresh start time, API health reported v0.17.0, and all pre-existing specialist gateways were accounted for. This was classified as a non-fatal restart race, not an activation failure.

The v0.16-era inline marker smoke from an older reference was not applicable to the installed v0.17 scheduler symbol name (`_extract_inline_buttons_marker` is no longer importable from `cron.scheduler`). This does not block the v0.17 runtime activation; it should be handled separately only if Telegram inline-button delivery regresses.

Secret hygiene:
- `values_printed=false`
- Secret artifact scan: no Telegram bot token, private key, or generic secret assignment hits in run artifacts.

## Boundaries

No Docker, Traefik, VPS, DNS, external business API, or secret value changes were performed.

Rollback shape if needed:
- Restore backed-up config from the staging backup if config regression appears.
- Reinstall previous package into the active venv: `uv pip install 'hermes-agent==0.16.0' --python /opt/data/hermes-0.15.1-venv/bin/python`
- Restart only after scoped approval and repeat the same validation checklist.
