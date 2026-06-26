# LK theme dev receipt — Schema free shipping threshold

Date: 2026-06-01T12:13:32Z
Approved by Lucas: upload first to dev/unpublished theme for QA.

## Scope

Uploaded only these assets to Shopify dev/unpublished theme:

- `sections/lk-header.liquid`
- `sections/lk-pdp.liquid`
- `snippets/product-structured-data.liquid`

No production publish. No product/price/stock/checkout/GMC/Judge.me/Klaviyo writes.

## Theme target

- Theme ID: `155065450718`
- Name: `lk-new-theme/dev`
- Role: `unpublished`

## Change

Represent fixed free-shipping promo as Schema.org shipping threshold, not a non-standard `OfferPromo` type:

- `OfferShippingDetails.name`: `Frete grátis acima de R$499`
- `shippingRate.@type`: `ShippingRateSettings`
- `shippingRate.shippingRate`: `MonetaryAmount` value `0` `BRL`
- `shippingRate.freeShippingThreshold`: `MonetaryAmount` value `499` `BRL`

Organization `aggregateRating` was left unchanged because Lucas confirmed `4.89` is the valid Google rating.

## Admin API readback

All three uploaded assets had exact SHA readback match after upload.

- `sections/lk-header.liquid`: `ShippingRateSettings=1`, `freeShippingThreshold=1`, `value 499=1`
- `sections/lk-pdp.liquid`: `ShippingRateSettings=1`, `freeShippingThreshold=1`, `value 499=1`
- `snippets/product-structured-data.liquid`: `ShippingRateSettings=1`, `freeShippingThreshold=1`, `value 499=1`

Backup/manifest:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-dev/schema-free-shipping-threshold-dev-20260601T121332Z/manifest.json`

## Storefront preview QA

Preview URLs checked:

- Homepage: `https://lksneakers.com.br/?preview_theme_id=155065450718`
- PDP sample: `https://lksneakers.com.br/products/nike-dunk-low-rose-whisper?preview_theme_id=155065450718`

Rendered JSON-LD validation:

- Homepage: 2 JSON-LD blocks, 0 parse errors, `freeShippingThreshold` objects: 1
- PDP sample: 4 JSON-LD blocks, 0 parse errors, `freeShippingThreshold` objects: 9

## Risk

Low. `freeShippingThreshold` is Schema.org-supported, but Google rich-result display support may vary.

## Rollback

Re-upload the `.before.liquid` backups from this receipt directory to the same dev theme assets.
