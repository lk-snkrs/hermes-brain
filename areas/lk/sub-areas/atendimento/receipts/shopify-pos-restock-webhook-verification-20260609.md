# LK Shopify POS restock webhook verification — 2026-06-09

- Timestamp UTC: 2026-06-09T19:45:53Z
- Timestamp BRT: 2026-06-09T16:45:53-0300
- Scope: read-only verification + signed non-POS/non-paid public probe for `lk-shopify-pos-restock`.
- Secrets: checked via Doppler/runtime presence only; values were not printed (`values_printed=false`).

## Evidence

1. Required runtime secrets present:
   - `SHOPIFY_WEBHOOK_SECRET`: present
   - `SHOPIFY_STORE_URL`/`SHOPIFY_STORE`: present
   - `SHOPIFY_ACCESS_TOKEN`: present

2. Shopify webhook registry readback:
   - HTTP status: 200
   - Total webhooks: 17
   - Matching `orders/paid` webhook pointing exactly to `https://hermes-webhooks.vercel.app/webhooks/lk-shopify-pos-restock`: 1
   - Match:
     - id: 1641004826846
     - topic: `orders/paid`
     - address_host: `hermes-webhooks.vercel.app`
     - address_path: `/webhooks/lk-shopify-pos-restock`
     - format: `json`
     - updated_at: `2026-05-23T17:52:30-03:00`

3. Signed public probe through Vercel/Hermes:
   - URL: `https://hermes-webhooks.vercel.app/webhooks/lk-shopify-pos-restock`
   - Shopify HMAC: valid, generated from runtime secret; value not printed.
   - HTTP status: 200
   - Response:
     - status: `ignored`
     - route: `lk-shopify-pos-restock`
     - event: `orders/paid`
     - reason: `not_paid_active_pos_order`
     - queued_count: 0
     - sent_count: 0

## Verdict

Operational for receiving Shopify `orders/paid` webhooks at the public Vercel endpoint and forwarding them into Hermes. The probe was intentionally non-POS/not-paid, so no customer message was queued or sent.

## Caveat

Final proof of real-business behavior is the next real eligible POS paid order arriving and being queued/processed according to the POS post-purchase guardrails. Current verification proves ingress, HMAC, route registration, and Hermes acceptance.
