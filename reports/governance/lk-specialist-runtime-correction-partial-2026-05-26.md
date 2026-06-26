# LK specialist runtime correction — partial receipt

Date: 2026-05-26
Scope approved by Lucas: LK Shopify, LK Trends, LK Ops specialist gateways only; no Docker/VPS/root/SSH/Traefik/volumes/networks and no external writes.

## Evidence collected

- LK Shopify: profile state file indicated Telegram connected, but live `/proc` inspection later showed no current process for `/opt/data/profiles/lk-shopify` in this execution namespace. Recent logs showed a successful restart at 18:17 UTC, Telegram connected, channel directory with 1 target, and a simple inbound Telegram round trip completed in ~10s with smart model routing to `gpt-5.4-mini`.
- LK Trends: profile state file indicated Telegram connected, but live `/proc` inspection later showed no current process for `/opt/data/profiles/lk-trends` in this execution namespace. Recent logs showed successful restart at 18:17 UTC and Telegram connected; earlier logs showed very slow deep tasks, stale non-streaming calls, and long responses.
- LK Ops: profile state file indicated Telegram connected plus a stale webhook retry error for route `lk-shopify-pos-restock` missing HMAC secret. Recent logs showed that after the later restart the gateway connected Telegram only, channel directory had 1 target, and `agent.max_turns` was active as 40. The webhook route remains documented/configured but `platforms.webhook.enabled: false` in config; no webhook/external write was activated.

## Local changes applied

- `/opt/data/profiles/lk-shopify/.env`: aligned `HERMES_MAX_ITERATIONS` from 90 to 50, matching profile config.
- `/opt/data/profiles/lk-trends/.env`: aligned `HERMES_MAX_ITERATIONS` from 90 to 45, matching profile config.
- `/opt/data/profiles/lk-ops/.env`: aligned `HERMES_MAX_ITERATIONS` from 90 to 40, matching profile config.
- Removed `terminal` from Telegram toolsets in:
  - `/opt/data/profiles/lk-shopify/config.yaml`
  - `/opt/data/profiles/lk-trends/config.yaml`
  - `/opt/data/profiles/lk-ops/config.yaml`

## Activation status

- Not fully activated/verified in live specialist processes during this turn.
- A restart/start attempt for LK Shopify specialist gateway was blocked by Task Router approval guardrail after the local config edits.
- No Docker/VPS/main-Hermes/external write was executed.

## Risk

- The local config files are corrected, but LK Shopify/LK Trends/LK Ops specialist gateways need a scoped restart/start to prove those changes are active.
- LK Ops webhook should remain disabled unless a separate HMAC-secret activation is explicitly approved.

## Rollback

- Set the three profile `.env` values back to `HERMES_MAX_ITERATIONS=90` if the tighter budgets create regressions.
- Re-add `terminal` under each affected profile's `platform_toolsets.telegram` only if a specialist Telegram bot explicitly needs local shell tools again.
- Restart only the affected specialist gateway after rollback; do not touch Docker/VPS/main Hermes.

## Next decision

Approve one bounded activation step: start/restart only LK Shopify, LK Trends, and LK Ops specialist gateways with API/webhook disabled, then verify logs for Telegram connected, exact `HERMES_HOME`, active max_iterations, smart routing, and no webhook retry.
