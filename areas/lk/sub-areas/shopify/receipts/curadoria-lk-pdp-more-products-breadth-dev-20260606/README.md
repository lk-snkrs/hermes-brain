# Receipt — Curadoria LK PDP — More products breadth batch — DEV — 2026-06-06

## Status

DEV applied and source/readback validated.

## Approval

Lucas approved the DEV approval packet with: `Aprovo` after the requested phrase for `DEV Curadoria breadth Adidas Superstar + ASICS Kayano 14 + Air Max 95 + NB550`.

## Scope executed

- Theme: `155065450718`
- Theme role: `unpublished`
- Asset changed: `snippets/lk-variante-top30-visited-v2.liquid`
- Action: `put`
- Production: not touched
- Products/prices/stock/checkout/apps/campaigns: not touched

## Groups added

### Adidas Superstar special/collab

- Marker: `top30-adidas-superstar-special`
- Handles: 3
- Labels: 3
- Images: 3
- Titles: 3

Handles:

1. `tenis-adidas-superstar-x-clot-chinese-new-year-preto`
2. `tenis-adidas-superstar-x-korn-30th-anniversary-preto`
3. `tenis-adidas-superstar-x-wales-bonner-croc-wonder-white-branco`

### ASICS Gel-Kayano 14 special/collab

- Marker: `top30-asics-gel-kayano-14-special`
- Handles: 3
- Labels: 3
- Images: 3
- Titles: 3

Handles:

1. `tenis-asics-gel-kayano-14-x-senna-black-gold-preto`
2. `tenis-asics-gel-kayano-14-x-senna-white-red-branco`
3. `tenis-asics-marvel-vs-capcom-x-kith-x-asics-gel-kayano-14-ryu-branco`

### Nike Air Max 95 x Levi's

- Marker: `top30-nike-air-max-95-levis`
- Handles: 3
- Labels: 3
- Images: 3
- Titles: 3

Handles:

1. `tenis-levis-x-nike-air-max-95-og-black-anthracite-denim`
2. `tenis-levis-x-nike-air-max-95-og-light-orewood-brown-denim`
3. `tenis-levis-x-nike-air-max-95-og-obsidian-denim-casual`

### New Balance 550 regular/special

- Marker: `top30-new-balance-550-regular-special`
- Handles: 3
- Labels: 3
- Images: 3
- Titles: 3

Handles:

1. `tenis-new-balance-550-sashiko-pack-pecan-marrom`
2. `new-balance-550-white-pine-green`
3. `tenis-new-balance-550-x-aime-leon-dore-brown-marrom`

## Readback

- Before SHA: `114bd5b4e097e32ac2c6419ac22870372c75129265ebac2402397a890ad47230`
- After SHA: `438020496c5844d86eb1d4a5abb6a96317aedf5b92438bcd145ecf337c12e539`
- Shopify readback converged on poll attempt 2.
- Final static status: `ok`

Static validation:

- Marker count: 1 for each new group
- Handles/labels/images/titles aligned: yes
- Duplicate handles: 0
- Bad/malformed image URLs: 0
- Placeholder image URLs: 0

## Visual QA — DEV preview

Chrome headless / CDP preview QA.

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

The browser landed on `Just a moment... / Your connection needs to be verified before you can proceed`, so those preview visual checks were blocked by the public anti-bot/verification layer, not by source/readback failure.

## Caveat

Each group has 3 products. Since the current PDP is excluded, each rail can render up to 2 alternatives.

## Rollback

Restore the pre-write DEV backup of `snippets/lk-variante-top30-visited-v2.liquid`:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-more-products-breadth-dev-20260606/20260606T155715Z-dev-theme-155065450718-before.liquid`

Readback after write:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-more-products-breadth-dev-20260606/20260606T155715Z-dev-theme-155065450718-after.liquid`

Machine receipt:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-more-products-breadth-dev-20260606/20260606T155715Z-receipt.json`

## Next decision

If Lucas approves the DEV result despite the public preview challenge caveat, next step is a scoped GitHub PR / merge para Production for these four groups.
