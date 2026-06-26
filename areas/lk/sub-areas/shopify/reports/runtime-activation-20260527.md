# LK Shopify runtime activation — 2026-05-27

## Status

- Specialist profile: `/opt/data/profiles/lk-shopify`
- Telegram bot verified via `getMe`: `@LKShopify_HermesBot`
- Gateway: running in Telegram polling mode
- Runtime PID verified: `5478` at activation time
- API server: disabled
- Webhook server: disabled
- Main Hermes, LK Growth, Mordomo and SPITI gateways: not restarted by this activation

## Guardrails preserved

- Token was used only from the profile `.env` and was not printed in the receipt.
- No Shopify, Tiny, GMC, Klaviyo, ads, WhatsApp, email, Docker, Traefik, VPS, or production commerce write was performed.
- This activation only starts the specialist Telegram interface for LK Shopify.

## Verification evidence

- `hermes profile list` showed `lk-shopify` as `running` after activation.
- LK Shopify gateway log showed:
  - `Active profile: lk-shopify`
  - `Connected to Telegram (polling mode)`
  - `Gateway running with 1 platform(s)`
- Process environment verified exact `HERMES_HOME=/opt/data/profiles/lk-shopify`.
- Runtime API/webhook environment surfaces were empty/disabled at process level.

## Pending human validation

Lucas should send a message directly to `@LKShopify_HermesBot` to validate end-to-end reply behavior from Telegram.