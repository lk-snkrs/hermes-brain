# LK Sneakers — Sneakers collection DEV preview receipt — 2026-05-31

## Scope

Approved by Lucas in Telegram: `Aprovo dev`.

Applied only to Shopify DEV theme:

- Theme ID: `155065450718`
- Theme name/role: `lk-new-theme/dev` / `unpublished`
- Asset: `sections/lk-collection.liquid`
- Route: `/collections/sneakers`

No production, product, price, stock, campaign, checkout, collection-admin, or customer-facing writes were made.

## Change summary

- Added compact top description override for collection handle `sneakers`:
  - `Sneakers originais para diferentes estilos, marcas e momentos.`
- Added post-grid Sneakers hub panel after product pagination and after CollectionPage JSON-LD.
- Added internal navigation links:
  - New Balance
  - Adidas
  - Nike
  - Air Jordan
  - Onitsuka Tiger
  - Lançamentos
  - Sale
- Added visible FAQ and matching FAQPage JSON-LD only under the `collection.handle == 'sneakers'` guard.
- Confirmed forbidden wording absent:
  - no `sneakers selecionados pela curadoria` copy.

## Validation

Primary receipt directory:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-dev/sneakers-collection-dev-preview-20260531T165840Z`

Key readback evidence:

- DEV readback matched target: `true`
- Production asset unchanged: `true`
- Required Sneakers markers present in DEV readback: `true`
- Forbidden curated-selection copy present: `false`
- Sneakers panel after product pagination: `true`
- Sneakers panel after CollectionPage schema: `true`
- Existing remote DEV Nike Mind markers preserved:
  - `lk-nike-mind-collection-hero`: present
  - `lk-nike-mind-guide-panel`: present

Preview URL:

`https://www.lksneakers.com.br/collections/sneakers?preview_theme_id=155065450718`

Public unauthenticated fetch stripped `preview_theme_id` and returned live/cached production HTML, so visual preview could not be proven by unauthenticated HTTP. Asset API readback is the authoritative DEV validation. Public live URL was checked read-only and did not expose the DEV marker.

## Rollback

Rollback DEV only:

`PUT /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-dev/sneakers-collection-dev-preview-20260531T165840Z/sections.lk-collection.dev.before.liquid back to DEV theme 155065450718 asset sections/lk-collection.liquid.`

## Notes

An earlier attempt used the local theme file and could have temporarily replaced remote DEV-only changes. The final successful receipt patched from the pre-attempt DEV backup and preserved the remote-only Nike Mind dev markers before adding Sneakers.
