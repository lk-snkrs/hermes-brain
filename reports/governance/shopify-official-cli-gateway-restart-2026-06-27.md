# Shopify official CLI gateway activation restart — 2026-06-27

## Status

- status: partial_done
- approval: Lucas said "Pode reiniciar"
- goal: restart Hermes gateways so the Shopify official CLI policy is loaded by live specialist agents
- values_printed: false
- external business writes: 0
- Shopify mutations: 0
- Docker/VPS/Traefik changes: 0

## What was restarted

Managed secondary Telegram gateways were restarted via the global local watchdog path, with API/webhook surfaces forced off:

- mordomo
- lk-growth
- spiti
- spiti-atendimento
- lk-ops
- lk-shopify
- lk-trends
- lk-collection-optimizer
- lk-stock
- lk-finance
- lk-content

Pre-state managed secondary gateway count: 11.
Post-state managed secondary gateway count: 11.
Watchdog restore stdout/stderr: 0 bytes / 0 bytes (silent-OK).

## Main/default gateway

Main/default gateway (`HERMES_HOME=/opt/data`, PID 1) was not restarted by this tool session.

Reason: Hermes blocks `hermes gateway restart` from inside the gateway process because the restart would kill the command before completion. The attempted command returned the platform safety error: restart must be run from a separate shell outside the running gateway.

Current main/default status remained OK and connected; it was not killed.

## Post-restart validation

| Check | Result |
|---|---:|
| Managed secondary profiles with exactly one live gateway | 11/11 |
| Specialist API surfaces | disabled |
| Specialist webhook surfaces | disabled |
| Specialist Telegram token present boolean | true for all |
| Specialist allowlist present boolean | true for all |
| Global gateway watchdog after restart | silent-OK |
| Shopify official CLI smoke | OK |
| Shopify store readback | `lk-sneakerss.myshopify.com` |
| Brain health | All checks passed |
| Focused secret scan | 0 hits |

## Evidence notes

- New managed secondary PIDs were observed with fresh process age under ~60 seconds after restart.
- Main/default PID remained PID 1, check-only and connected.
- No secret values, OAuth cache values, service account JSON, refresh tokens or token previews were printed.

## Remaining activation gap

If Lucas wants the main/default gateway itself reloaded too, it needs one of:

1. Lucas sends `/restart` to the main Telegram gateway, or
2. an operator runs `HERMES_HOME=/opt/data /opt/data/hermes-0.15.1-venv/bin/hermes gateway restart` from a separate shell outside the gateway process.

This is a runtime execution limitation, not a Shopify auth/config issue.

## Rollback

For secondary profiles, rerun `/opt/data/scripts/hermes_all_gateway_watchdog.py` to restore expected managed roster, or terminate/restart only the affected profile gateway using the same profile-scoped watchdog path. No external Shopify state was modified.
