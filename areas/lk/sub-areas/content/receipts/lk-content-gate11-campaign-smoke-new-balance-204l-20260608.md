# LK Content — Gate 11 campaign smoke package

Date: 2026-06-08
Profile: `lk-content`
Scope: Gate 11 — campanha ponta a ponta segura/local

## Result

Status: OK — local/documental campaign smoke package created and verified.

Campaign theme: New Balance 204L — perfil baixo, leitura fashion.

## Artifacts created

- `/opt/data/profiles/lk-content/campanhas/gate11-smoke-new-balance-204l-20260608.md`
- `/opt/data/profiles/lk-content/scripts/shopify_products_readonly_for_campaign_smoke.py`
- One-shot local cron output: `/opt/data/profiles/lk-content/cron/output/9290ad07f177/2026-06-08_09-27-30.md`

## Sources used

- LK home page: `https://lksneakers.com.br/`
- LK New Balance 204L collection page: `https://lksneakers.com.br/collections/new-balance-204l`
- Shopify read-only product sample via Doppler-loaded credentials, sanitized output only.

## Verification

- Campaign artifact was read back successfully.
- LK site fetch returned current New Balance 204L collection language and colorways.
- Shopify read-only one-shot returned HTTP 200 and 12 product records using sanitized fields only.
- Active cron jobs after one-shot: 3 recurring approved Gate 10 jobs only; the one-shot job did not remain active.

## Guardrails observed

- Writes externos: 0.
- Klaviyo draft/send/schedule/flow activation: not executed.
- Shopify/Tiny/Merchant writes: not executed.
- Product truth: copy limited to facts available from LK site/collection; no price, size, stock, delivery, reservation or discount promises.
- Secrets printed: no; `values_printed=false`.

## Next gate

Explicit current approval is required to create a Klaviyo draft. Safe approval phrase:

“Pode criar o draft Klaviyo da campanha New Balance 204L, sem agendar e sem enviar.”

Send/schedule remains blocked until sequential double confirmation in Telegram.
