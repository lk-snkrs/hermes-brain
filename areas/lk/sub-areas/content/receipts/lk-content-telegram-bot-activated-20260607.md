# LK Content Telegram bot activation receipt — 2026-06-07

Status: activated locally.

## Scope executed

- Profile: `/opt/data/profiles/lk-content`
- Bot username validated by Telegram `getMe`: `@hermes_lk_producaodeconteudo_bot`
- Token stored only in the profile-local `.env`; token value not recorded here.
- `.env` permission verified as `0600`.
- Telegram allowed user configured for Lucas only: `171397651`.
- Gateway started only for `lk-content` with exact `HERMES_HOME=/opt/data/profiles/lk-content`.

## Verification evidence

- `hermes profile list` shows `lk-content` gateway: running.
- Live process verification found exactly one gateway process for `HERMES_HOME=/opt/data/profiles/lk-content`.
- Runtime env verified with API/webhook surfaces disabled/empty for the live process:
  - `API_SERVER_ENABLED=false`
  - `API_SERVER_KEY=''`
  - `API_SERVER_PORT=''`
  - `API_SERVER_HOST=''`
  - `WEBHOOK_ENABLED=false`
  - `WEBHOOK_PORT=''`
  - `WEBHOOK_SECRET=''`
- Gateway log evidence:
  - `Active profile: lk-content`
  - `Agent budget: max_iterations=60`
  - `[Telegram] Connected to Telegram (polling mode)`
  - `✓ telegram connected`
  - `Gateway running with 1 platform(s)`

## Safety / non-actions

- No Docker, VPS, Traefik, main Hermes, public API, webhook exposure, cron creation, Shopify/Tiny/Merchant/Klaviyo/ads/WhatsApp/email writes, supplier/customer contact, or production content publishing was performed.
- Cloned/static webhook surface in profile config was disabled and the copied route secret was cleared from this secondary profile config.

## Pending

- Lucas should send a direct test message to `@hermes_lk_producaodeconteudo_bot` to validate inbound/outbound Telegram round-trip from the new bot.
- Optional after round-trip: rotate the BotFather token because it was pasted in chat, then repeat token update + restart for this profile only.
