# LK Ops runtime repair receipt — 2026-05-27

## Trigger
Lucas asked: "Repare" after the LK Ops specialist was observed disconnected/stopped.

## Scope
- Repair only the local LK Ops specialist gateway.
- Keep API server disabled.
- Keep webhook disabled.
- No Docker/VPS/Main Hermes changes.
- No external writes.

## Action taken
Started the existing local watchdog launcher only:

- `/opt/data/scripts/lk_ops_gateway_watchdog.sh`

## Verification
### Runtime process
- Live gateway process present with exact profile `HERMES_HOME=/opt/data/profiles/lk-ops`.
- Current PID observed: `2806`.

### Gateway state
- `gateway_state=running`.
- Telegram state: `connected`.

### Log evidence
The lk-ops gateway log shows fresh startup and Telegram connection at `2026-05-27 10:57 UTC`:

- `Starting Hermes Gateway...`
- `Agent budget: max_iterations=40`
- `Active profile: lk-ops`
- `Connected to Telegram (polling mode)`
- `Gateway running with 1 platform(s)`

## Notes
- The launcher script explicitly keeps `API_SERVER_ENABLED=false` and `WEBHOOK_ENABLED=false` and unsets the related secret/port/env variables.
- The persisted `gateway_state.json` still contains an older webhook retry note from prior runs, but the live gateway is running with Telegram connected and no webhook/API surface enabled.

## What was not done
- No Docker/VPS/Traefik/root/SSH/compose changes.
- No Main Hermes restart.
- No external business writes.
- No secrets printed or stored.

## Remaining validation
- A real Telegram round-trip message to LK Ops is still the last mile proof.
