# LK Trends + LK Shopify runtime recovery receipt — 2026-05-27

## Trigger
Lucas reported in Telegram: "Os agentes LK trends e LK Shopify não funcionam".

## Scope approved
Lucas approved: relink/restart only LK Trends and LK Shopify local specialist gateways.

## Guardrails
- No Docker/VPS/Traefik/Main Hermes changes.
- No external business writes.
- API server kept disabled for both specialist profiles.
- Webhook kept disabled for both specialist profiles.
- Secrets were not printed.

## Root cause evidence
After the Main Hermes gateway restart around 2026-05-27 09:58 UTC, both specialist profile states showed stopped/disconnected and no live gateway process with the exact profile `HERMES_HOME`:

- `/opt/data/profiles/lk-shopify/gateway_state.json`: `gateway_state=stopped`, Telegram `disconnected`.
- `/opt/data/profiles/lk-trends/gateway_state.json`: `gateway_state=stopped`, Telegram `disconnected`.
- No live process found for either exact profile before recovery.

## Action taken
Started existing local watchdog launchers only:

- `/opt/data/scripts/lk_shopify_gateway_watchdog.sh`
- `/opt/data/scripts/lk_trends_gateway_watchdog.sh`

## Verification after recovery

### LK Shopify
- Live gateway process: present.
- `HERMES_HOME=/opt/data/profiles/lk-shopify`.
- `API_SERVER_ENABLED=false`.
- `API_SERVER_KEY` absent in live env.
- `WEBHOOK_ENABLED=false`.
- `HERMES_MAX_ITERATIONS=50`.
- `gateway_state=running`.
- Telegram state: `connected`.
- Log evidence: `Connected to Telegram (polling mode)` and `Gateway running with 1 platform(s)` at 2026-05-27 10:15 UTC.

### LK Trends
- Live gateway process: present.
- `HERMES_HOME=/opt/data/profiles/lk-trends`.
- `API_SERVER_ENABLED=false`.
- `API_SERVER_KEY` absent in live env.
- `WEBHOOK_ENABLED=false`.
- `HERMES_MAX_ITERATIONS=45`.
- `gateway_state=running`.
- Telegram state: `connected`.
- Log evidence: `Connected to Telegram (polling mode)` and `Gateway running with 1 platform(s)` at 2026-05-27 10:15 UTC.

## Remaining validation
Telegram runtime is connected. Final conversational round-trip still depends on Lucas sending a simple test message to each specialist bot.
