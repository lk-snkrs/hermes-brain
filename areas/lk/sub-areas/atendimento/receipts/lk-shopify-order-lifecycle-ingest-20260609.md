# LK Shopify order lifecycle ingest — record-only

Timestamp UTC: 2026-06-09T20:29:12Z

## Objective

Extend LK Shopify all-orders ingest beyond `orders/create` to include order lifecycle changes as record-only ledger events, without customer messaging, stock writes, Shopify writes beyond webhook registration, or Tiny changes.

## Changes applied

- Updated Hermes dynamic subscription `lk-shopify-orders-ingest` events:
  - `orders/create`
  - `orders/updated`
  - `orders/cancelled`
- Created Shopify Admin webhooks pointing to the canonical Vercel proxy:
  - `orders/updated` -> `https://hermes-webhooks.vercel.app/webhooks/lk-shopify-orders-ingest`
  - `orders/cancelled` -> `https://hermes-webhooks.vercel.app/webhooks/lk-shopify-orders-ingest`
- Updated local deterministic ingest script documentation to describe order lifecycle ingest.

## Shopify registry readback

Hermes-related Shopify webhooks after change:

- `orders/cancelled` -> `/webhooks/lk-shopify-orders-ingest` — ID `1654036562142`
- `orders/create` -> `/webhooks/lk-shopify-orders-ingest` — ID `1653972795614`
- `orders/updated` -> `/webhooks/lk-shopify-orders-ingest` — ID `1654036529374`
- `orders/paid` -> `/webhooks/lk-shopify-pos-restock` — ID `1641004826846`

## Probe verification

Signed public probes through Vercel/Hermes returned:

- `orders/create`: HTTP `200`, status `recorded`, action `record_only`
- `orders/updated`: HTTP `200`, status `recorded`, action `record_only`
- `orders/cancelled`: HTTP `200`, status `recorded`, action `record_only`

Probe ledger entries were removed after verification:

- removed: `3`
- remaining fake probe entries: `0`

## Safety boundaries

- No WhatsApp/customer message was sent.
- No Tiny/stock write was performed.
- No Shopify order data was mutated.
- Secrets were not printed (`values_printed=false`).
- POS post-purchase automation remains isolated on `orders/paid` route `lk-shopify-pos-restock`.

## Current status

Technically operational for Shopify order lifecycle ingestion. Final business proof remains the next real Shopify order event hitting the ledger.
