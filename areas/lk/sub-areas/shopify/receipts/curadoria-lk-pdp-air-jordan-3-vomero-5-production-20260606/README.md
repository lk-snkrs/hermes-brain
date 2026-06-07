# Receipt — Curadoria LK PDP — Air Jordan 3 + Vomero 5 — Production — 2026-06-06

## Status

Production merge completed and verified.

## Approval

Lucas approved after the DEV receipt/next decision for: `merge para Production Curadoria Air Jordan 3 + Vomero 5`.

## Scope executed

- Repository: `lk-snkrs/lk-new-theme`
- Base branch: `production`
- PR: `#30` — `https://github.com/lk-snkrs/lk-new-theme/pull/30`
- Merge SHA: `2a255ce95c890e54c623d1e089a0869b27e09715`
- Production theme: `155065417950` (`main`)
- Asset changed: `snippets/lk-variante-top30-visited-v2.liquid`
- Diff: `72 insertions`, one file only

No product, price, stock, checkout, CSS, app, image upload, campaign, or collection change was made.

## Groups added

### Air Jordan 3

- Marker: `top30-air-jordan-3-regular-special`
- Handles: 4
- Labels: 4
- Images: 4
- Titles: 4

Handles:

1. `tenis-nike-air-jordan-3-og-rare-air-preto`
2. `tenis-air-jordan-3-retro-black-cat-preto`
3. `tenis-air-jordan-3-retro-x-j-balvin-rio-preto`
4. `tenis-air-jordan-3-retro-x-wnba-desert-camo-bege`

### Nike Zoom Vomero 5

- Marker: `top30-nike-zoom-vomero-5-regular-special`
- Handles: 4
- Labels: 4
- Images: 4
- Titles: 4

Handles:

1. `tenis-nike-air-zoom-vomero-5-doernbecher-2023-laranja`
2. `tenis-nike-zoom-vomero-5-metallic-silver-blue-tint-prateado-azul`
3. `tenis-nike-zoom-vomero-5-metallic-silver-platinum-violet-prateado-violeta`
4. `tenis-nike-zoom-vomero-5-photon-dust-metallic-silver-cinza`

## Static readback

Before:

- Live Shopify SHA: `83d10c80e6fe674e01ed924cb136e6aaa742e0b59b2c7eafb3c396ca87e59a3f`
- Repo SHA: `83d10c80e6fe674e01ed924cb136e6aaa742e0b59b2c7eafb3c396ca87e59a3f`
- Both new markers absent before merge.

After:

- Repo Production SHA: `88ce7b094aeeeb3686024cbd996b15ea50244300e4a264a70e296b560c63dba9`
- Live Shopify SHA: `88ce7b094aeeeb3686024cbd996b15ea50244300e4a264a70e296b560c63dba9`
- Shopify sync converged on poll attempt 2.
- Final status: `ok`

Validation:

- Air Jordan 3 marker count: 1
- Vomero 5 marker count: 1
- Handles/labels/images/titles aligned: yes
- Duplicate handles: 0
- Bad image URLs: 0

## Visual QA — Production

Chrome headless / CDP computed-style checks.

### Air Jordan 3

Passing PDPs:

- `tenis-air-jordan-3-retro-black-cat-preto`
  - Marker: `top30-air-jordan-3-regular-special`
  - Title text: `Outras variações`
  - Title font weight: `300`
  - Label font weight: `300`
  - Label `::after` font weight: `300`

- `tenis-air-jordan-3-retro-x-j-balvin-rio-preto`
  - Marker: `top30-air-jordan-3-regular-special`
  - Title text: `Outras variações`
  - Title font weight: `300`
  - Label font weight: `300`
  - Label `::after` font weight: `300`

- `tenis-air-jordan-3-retro-x-wnba-desert-camo-bege`
  - Marker: `top30-air-jordan-3-regular-special`
  - Title text: `Outras variações`
  - Title font weight: `300`
  - Label font weight: `300`
  - Label `::after` font weight: `300`

Observation:

- `tenis-nike-air-jordan-3-og-rare-air-preto` did not render the block in the browser QA despite the handle being present in the live snippet. The other 3 Air Jordan 3 handles render correctly. This should be monitored separately if Lucas expects the Rare Air PDP to show the block; likely page/product-template/render condition difference, not a missing marker in the deployed snippet.

### Nike Zoom Vomero 5

Passing PDP:

- `tenis-nike-zoom-vomero-5-photon-dust-metallic-silver-cinza`
  - Marker: `top30-nike-zoom-vomero-5-regular-special`
  - Title text: `Outras variações`
  - Title font weight: `300`
  - Label font weight: `300`
  - Label `::after` font weight: `300`

## Rollback

Preferred rollback:

1. Revert PR `#30` / merge SHA `2a255ce95c890e54c623d1e089a0869b27e09715` on branch `production`.
2. Wait for Shopify GitHub sync.
3. Read back `snippets/lk-variante-top30-visited-v2.liquid` from theme `155065417950` and confirm both new markers are absent.

Emergency rollback backup:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-air-jordan-3-vomero-5-production-20260606/20260606T154545Z-production-theme-155065417950-snippets__lk-variante-top30-visited-v2.before.liquid`

Readback after merge:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-air-jordan-3-vomero-5-production-20260606/20260606T154545Z-production-theme-155065417950-snippets__lk-variante-top30-visited-v2.after.liquid`

Machine receipt:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-air-jordan-3-vomero-5-production-20260606/20260606T154545Z-merge-receipt.json`
