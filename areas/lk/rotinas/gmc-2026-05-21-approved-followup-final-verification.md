# LK GMC approved follow-up final verification — 2026-05-21

Generated: `2026-05-21T20:26:00Z`
Approval: Lucas Telegram — `Corrigir tudo acima`.

## Scope executed

- Packet A: attempted/updated the 2 Adidas Gazelle x Bad Bunny offer IDs.
- Packet B: applied `color` to 181 high-confidence missing-color offers.
- Packet C: applied Merchant-only reversible suppression for 19 Shopify `DRAFT` / public `.js 404` offers using `excludedDestinations` including `Shopping`.

## Surface used

Primary write surface actually used: Google Content API `products.insert` for exact Merchant product resources.

The first supplemental-feed/Gist route was attempted only up to local CSV preparation and then blocked before any Gist/datafeed write because the current accessible Merchant account has no Content API datafeed `407508563`. No Gist patch/datafeed write was performed in that failed route.

## Verification readback

### Packet B — color

- Target high-confidence color offers: `181`
- Readback matched exact target color: `181/181`
- Result: `verified`

### Packet C — DRAFT / 404 landing products

- Target DRAFT/public `.js 404` offers: `19`
- Readback has `Shopping` in `excludedDestinations`: `19/19`
- Productstatus issue sample after suppression: no item-level issues returned for the sampled Packet C rows in the verification pass.
- Result: `verified as Merchant Shopping suppression`; Shopify products were not published/unpublished.

### Packet A — Adidas price

Targets:

- `online:pt:BR:IF9737` → target `2199.99 BRL`
- `online:pt:BR:IF9735-9` → target `2199.99 BRL`

Readback:

- Content API product price currently reads `1799.99 BRL` for both offers.
- Public Shopify `.js` exact variants still read `2199.99 BRL` for SKUs `IF9737` and `IF9735-9`.
- Productstatus no longer shows the prior P0 `price_mismatch` / `price_out_of_range` disapproval shape; it now shows `price_updated` / automatic price update with `servability: unaffected`.

Interpretation: the P0 Shopping disapproval appears mitigated, but exact Merchant product-resource price is not locked to `2199.99`; Merchant/Google automatic price update is normalizing these two offers to `1799.99`, likely from storefront visible/metadata signals that still include `R$ 1.799,99` on the page. A deeper storefront/structured-data price cleanup is needed if Lucas wants Merchant readback to show exactly `2199.99` instead of only clearing the P0.

## Rollback snapshots

- Full pre-write Content API rollback snapshot: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-approved-followup-contentapi-rollback-20260521T200637Z.json`
- Resume retry snapshot: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-approved-followup-resume-snapshot-20260521T202119Z.json`

Rollback instruction: re-insert the saved `before_product` resources from the rollback snapshot through Content API `products.insert`.

## Not performed

- Shopify write
- Shopify publish/unpublish
- Stock write
- `salePrice` / compare-at write
- Theme/checkout write
- GSC write
- Campaign send
- Customer/supplier contact
- Purchase/PO
- External marketplace call
- n8n flow creation
