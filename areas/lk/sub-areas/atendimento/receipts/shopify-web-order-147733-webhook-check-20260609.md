# Shopify web order #147733 webhook check — 2026-06-09

## Scope

Lucas asked whether all webhook calls were returning 200 and whether the newly received website order arrived.

Read-only checks only. No Shopify/Tiny/WhatsApp/Vercel writes, no customer send.

## Shopify evidence

Latest order observed in Shopify Admin read-only:

- Order: `#147733`
- Shopify order ID: `7405649625310`
- Created at: `2026-06-09T16:22:22-03:00`
- Updated at: `2026-06-09T16:39:11-03:00`
- Source: `web`
- App ID: `580111`
- Financial status: `pending`
- Cancelled: `false`
- Customer present: yes
- Phone present: yes
- Line item count: `1`
- Sanitized item: `Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo`, variant `37`, SKU `1183C102 751-4`, quantity `1`

## Vercel/Hermes ingress evidence

Vercel production logs for `https://hermes-webhooks.vercel.app` checked for the last 40 minutes:

- Matching `/webhooks/lk-shopify-pos-restock` requests: `1`
- That request was the signed probe sent earlier at approximately `2026-06-09T19:45:41Z`, status `200`.
- No matching request for order `#147733` / `7405649625310` was observed.
- 401 count in the last 40 minutes: `0`
- 500 count in the last 40 minutes: `0`
- 502 count in the last 40 minutes: `0`

## Local queue/state evidence

- POS post-purchase queue has no job for `#147733` / `7405649625310`.
- Local webhook state has no sent/delivery key for `#147733` / `7405649625310`.
- `last_webhook_at` in local POS state was from the signed probe, not this web order.
- Auto-worker is running; latest worker result had `errors=0`, `would_send=0`, `sent=0`.

## Interpretation

The website order did not arrive at the `lk-shopify-pos-restock` route because the registered Shopify webhook for that route is `orders/paid`, and this order is currently `financial_status=pending`. Also, even if paid later, the POS post-purchase flow intentionally ignores `source_name=web` because it is scoped to POS orders (`source_name=pos` / POS app).

This is not evidence of a current 500/401. It is evidence that no relevant webhook delivery for this pending web order was expected/observed on this POS route.

## Caveat

If LK needs website-order automation too, it should be designed as a separate flow/route or explicitly broadened from POS-only, with approval and guardrails. Do not infer stock/pronta entrega from this route; stock remains `lk-stock`/Tiny-owned.
