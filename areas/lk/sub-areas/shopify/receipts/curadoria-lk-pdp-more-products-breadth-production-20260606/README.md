# Receipt — Curadoria LK PDP — More products breadth batch — Production — 2026-06-06

## Status

Production merge completed and source/readback validated.

## Approval

Lucas approved: `Aprovo merge` after DEV application/readback for the breadth batch:

- Adidas Superstar special/collab
- ASICS Gel-Kayano 14 special/collab
- Nike Air Max 95 x Levi's
- New Balance 550 regular/special

## Scope executed

- Repository: `lk-snkrs/lk-new-theme`
- Base branch: `production`
- PR: `#31` — `https://github.com/lk-snkrs/lk-new-theme/pull/31`
- Merge SHA: `f5c5bdd518360db034167baf8269202799c3a39a`
- Production theme: `155065417950` (`main`)
- Asset changed: `snippets/lk-variante-top30-visited-v2.liquid`
- Diff: `147 insertions`, one file only

No product, price, stock, checkout, CSS, app, image upload, campaign, or collection change was made.

## Groups added

### Adidas Superstar special/collab

- Marker: `top30-adidas-superstar-special`
- Handles/labels/images/titles: 3/3/3/3

### ASICS Gel-Kayano 14 special/collab

- Marker: `top30-asics-gel-kayano-14-special`
- Handles/labels/images/titles: 3/3/3/3

### Nike Air Max 95 x Levi's

- Marker: `top30-nike-air-max-95-levis`
- Handles/labels/images/titles: 3/3/3/3

### New Balance 550 regular/special

- Marker: `top30-new-balance-550-regular-special`
- Handles/labels/images/titles: 3/3/3/3

## Static readback

Before:

- Live Shopify SHA: `88ce7b094aeeeb3686024cbd996b15ea50244300e4a264a70e296b560c63dba9`
- Repo SHA: `88ce7b094aeeeb3686024cbd996b15ea50244300e4a264a70e296b560c63dba9`
- The four new markers were absent before merge.

After:

- Repo Production SHA: `f0b86521f3e85dd528405d2b09655fab98325f92a65d99da51ecbc80438b5723`
- Live Shopify SHA: `f0b86521f3e85dd528405d2b09655fab98325f92a65d99da51ecbc80438b5723`
- Shopify sync converged on poll attempt 2.
- Final status: `ok`

Validation:

- Marker count: 1 for each new group
- Handles/labels/images/titles aligned: yes
- Duplicate handles: 0
- Bad/malformed image URLs: 0
- Placeholder images: 0

## Visual QA — Production

Chrome headless / CDP computed-style checks.

Passing sample:

- PDP: `tenis-adidas-superstar-x-clot-chinese-new-year-preto`
- Marker: `top30-adidas-superstar-special`
- Title text: `Outras variações`
- Title font weight: `300`
- Label text sample: `Korn 30th`
- Label font weight: `300`
- Label `::after` font weight: `300`

Inconclusive samples due storefront verification challenge:

- `tenis-asics-gel-kayano-14-x-senna-black-gold-preto`
- `tenis-levis-x-nike-air-max-95-og-black-anthracite-denim`
- `tenis-new-balance-550-sashiko-pack-pecan-marrom`

The browser landed on `Just a moment... / Your connection needs to be verified before you can proceed`, so those visual checks were blocked by the public verification layer, not by source/readback failure.

## Caveat

Each group has 3 products. Since the current PDP is excluded, each rail can render up to 2 alternatives.

## Rollback

Preferred rollback:

1. Revert PR `#31` / merge SHA `f5c5bdd518360db034167baf8269202799c3a39a` on branch `production`.
2. Wait for Shopify GitHub sync.
3. Read back `snippets/lk-variante-top30-visited-v2.liquid` from theme `155065417950` and confirm the four new markers are absent.

Emergency rollback backup:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-more-products-breadth-production-20260606/20260606T160335Z-production-theme-155065417950-snippets__lk-variante-top30-visited-v2.before.liquid`

Readback after merge:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-more-products-breadth-production-20260606/20260606T160335Z-production-theme-155065417950-snippets__lk-variante-top30-visited-v2.after.liquid`

Machine receipt:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-more-products-breadth-production-20260606/20260606T160335Z-merge-receipt.json`
