# LK theme production receipt — Schema free shipping threshold

Date: 2026-06-01T12:42:42Z
Approval: Lucas asked to publish to Production and reminded the required method: Dev→Production merge/promotion, not loose production patch.

## Method

Used Shopify dev theme as source of truth:

- Source: `lk-new-theme/dev` / theme ID `155065450718` / role `unpublished`
- Destination: `lk-new-theme/production` / theme ID `155065417950` / role `main`

Fetched source asset values from the dev theme readback and uploaded those exact values to production. This was a Dev→Production promotion of the approved dev state, not a production-only patch.

## Assets promoted

- `sections/lk-header.liquid`
- `sections/lk-pdp.liquid`
- `snippets/product-structured-data.liquid`

## Change promoted

Schema.org free shipping threshold for LK fixed promo:

- `OfferShippingDetails.name`: `Frete grátis acima de R$499`
- `shippingRate.@type`: `ShippingRateSettings`
- `shippingRate.shippingRate`: `MonetaryAmount`, value `0`, currency `BRL`
- `shippingRate.freeShippingThreshold`: `MonetaryAmount`, value `499`, currency `BRL`

Organization `aggregateRating` was preserved unchanged per Lucas correction: `4.89` is valid Google rating.

## Admin API readback

All production assets were backed up before upload and then read back after upload with SHA match to the dev-source value.

- `sections/lk-header.liquid`: `ShippingRateSettings=1`, `freeShippingThreshold=1`, `value 499=1`
- `sections/lk-pdp.liquid`: `ShippingRateSettings=1`, `freeShippingThreshold=1`, `value 499=1`
- `snippets/product-structured-data.liquid`: `ShippingRateSettings=1`, `freeShippingThreshold=1`, `value 499=1`

JSON receipt: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-production/schema-free-shipping-threshold-dev-to-production-20260601T124242Z/receipt.json`

## Storefront QA

Final live QA with cache-busting/default view:

- Homepage: `https://lksneakers.com.br/?view=default&hermes_schema_final=20260601`
  - status: 200
  - JSON-LD blocks: 2
  - parse errors: 0
  - `freeShippingThreshold` objects: 1
  - `ShippingRateSettings` text count: 1

- PDP sample: `https://lksneakers.com.br/products/nike-dunk-low-rose-whisper?hermes_schema_final=20260601`
  - status: 200
  - JSON-LD blocks: 4
  - parse errors: 0
  - `freeShippingThreshold` objects: 9
  - `ShippingRateSettings` text count: 9

Note: an initial bare-homepage request showed old cached markup, but production asset readback was already correct; adding `view=default`/cache-busting returned the updated JSON-LD.

## Non-actions

No changes to:

- products
- price
- stock
- checkout
- GMC/feed
- Judge.me
- Klaviyo/campaigns
- apps/settings beyond the three theme assets above

## Rollback

Rollback backups are in the same directory as `.production-before.liquid` files. To rollback, upload each production-before file back to `lk-new-theme/production` for the matching asset key and verify SHA/readback + live JSON-LD.
