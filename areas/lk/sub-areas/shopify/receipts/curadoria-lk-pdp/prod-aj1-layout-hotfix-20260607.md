# Curadoria LK PDP — AJ1 layout hotfix Production

Date: 2026-06-07T00:02:10Z

## Trigger

Lucas reported via mobile screenshot that the newly merged Air Jordan 1 Curadoria block was rendering vertically/unstyled on the live PDP.

## Scope approved in chat

User message: `Deu erro no layout corrigir`

Interpreted as approval for a narrow repair of the broken AJ1 Curadoria layout only.

## Root cause

The dedicated split snippet `snippets/lk-variante-aj1-low-high-20260606.liquid` used non-canonical classes:

- `lk-variante__grid`
- `lk-variante__image-wrap`

The live CSS `assets/lk-variante.css` styles the canonical Curadoria markup:

- `lk-variante__head`
- `lk-variante__rail`
- `lk-variante__media`

So the AJ1 block appeared as a vertical list despite the global CSS being present.

## Change applied

Asset repaired in DEV and Production to keep themes aligned:

- DEV theme `155065450718`, role `unpublished`
- Production theme `155065417950`, role `main`
- Asset: `snippets/lk-variante-aj1-low-high-20260606.liquid`

Patch:

- Replaced heading/grid wrapper with canonical head + rail markup.
- Replaced image wrapper with canonical media wrapper.
- Did not change products, labels, image URLs, prices, stock, collections, or campaigns.

## Readback evidence

DEV:

- Before SHA: `4d612836286a203e89325d38dde29ec5ceaf3de324276b76c2bdc3c6cb77b7f0`
- Target/readback SHA: `31d37c719a038f0145d5f482c8aeac987bb202088e614de8ad46e2a780aee0df`
- Readback match: true
- Old `lk-variante__grid`: 2 → 0
- Old `lk-variante__image-wrap`: 2 → 0
- New `lk-variante__rail`: 2
- New `lk-variante__media`: 2
- New `lk-variante__head`: 2

Production:

- Before SHA: `4d612836286a203e89325d38dde29ec5ceaf3de324276b76c2bdc3c6cb77b7f0`
- Target/readback SHA: `31d37c719a038f0145d5f482c8aeac987bb202088e614de8ad46e2a780aee0df`
- Readback match: true
- Old `lk-variante__grid`: 2 → 0
- Old `lk-variante__image-wrap`: 2 → 0
- New `lk-variante__rail`: 2
- New `lk-variante__media`: 2
- New `lk-variante__head`: 2

## Public checks

Cache-busted public checks returned HTTP 200 and fresh canonical classes:

- `tenis-air-jordan-1-low-eastside-golf-azul-marinho`
  - status: 200
  - `Curadoria LK`: true
  - `lk-variante.css`: true
  - `lk-variante__rail`: true
  - `lk-variante__grid`: false
  - `lk-variante__media`: true
  - `lk-variante__image-wrap`: false

- `tenis-air-jordan-1-high-og-unc-toe-azul`
  - status: 200
  - `Curadoria LK`: true
  - `lk-variante.css`: true
  - `lk-variante__rail`: true
  - `lk-variante__grid`: false
  - `lk-variante__media`: true
  - `lk-variante__image-wrap`: false

## Artifacts

JSON:

- `/opt/data/tmp/lk_aj1_layout_hotfix_20260607T000210Z.json`

Backups:

- DEV: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/dev-before-aj1-layout-hotfix-20260607T000210Z.liquid`
- Production: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/prod-before-aj1-layout-hotfix-20260607T000210Z.liquid`

Readbacks:

- DEV: `/opt/data/tmp/dev-aj1-layout-hotfix-readback-20260607T000210Z.liquid`
- Production: `/opt/data/tmp/prod-aj1-layout-hotfix-readback-20260607T000210Z.liquid`

## Rollback

Restore `snippets/lk-variante-aj1-low-high-20260606.liquid` from:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/prod-before-aj1-layout-hotfix-20260607T000210Z.liquid`

For full AJ1 removal rollback, also restore the pre-AJ1 main snippet backup and delete the AJ1 split snippet, per the original AJ1 merge receipt.
