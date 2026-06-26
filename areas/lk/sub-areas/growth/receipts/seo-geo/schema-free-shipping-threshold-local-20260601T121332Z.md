# LK SEO/GEO — schema free shipping threshold local implementation

Date: 2026-06-01T12:13:32Z
Scope: local theme files only, no Shopify upload performed.

## Lucas correction

- Organization `aggregateRating` 4.89 is valid because it represents Google rating, not Judge.me/product Dynamic reviews.
- Do not remove the Organization rating on this basis.
- Fixed promo: free shipping above R$499 can be represented in schema.

## Local implementation

Patched local theme files under `/opt/data/hermes_bruno_ingest/lk-new-theme`:

- `sections/lk-header.liquid`
- `sections/lk-pdp.liquid`
- `snippets/product-structured-data.liquid`

Change: added `name: "Frete grátis acima de R$499"` and represented the shipping rule via `ShippingRateSettings` with:

```json
{
  "@type": "ShippingRateSettings",
  "shippingRate": {
    "@type": "MonetaryAmount",
    "value": 0,
    "currency": "BRL"
  },
  "freeShippingThreshold": {
    "@type": "MonetaryAmount",
    "value": 499,
    "currency": "BRL"
  }
}
```

## Why this approach

- Avoids inventing non-standard `OfferPromo` / `OfferPromotion` schema.
- Uses Schema.org-supported `freeShippingThreshold` on `ShippingRateSettings`.
- Keeps existing `Product + Offer + shippingDetails` architecture.
- Keeps Organization rating unchanged.

## Verification

Local text verification confirmed each patched file contains exactly one:

- `"@type": "ShippingRateSettings"`
- `"freeShippingThreshold"`
- `"value": 499`

No live storefront readback was performed because no Shopify upload/deploy was executed.

## Risk

- Low schema risk: `freeShippingThreshold` is Schema.org-supported, but Google rich result support may vary because it is a Schema.org feature rather than a guaranteed visible rich result.
- Commercial accuracy: safe if R$499 free shipping is fixed and visible on storefront.
- No price/stock/product/customer data changed.

## Rollback

Revert the three local file edits by changing `shippingRate` from `ShippingRateSettings` back to plain `MonetaryAmount` value `0`, and removing the `name`/`freeShippingThreshold` fields.

## Pending approval / next step

To affect the storefront, upload/publish to the selected Shopify theme is still required. This was not done in this step.
