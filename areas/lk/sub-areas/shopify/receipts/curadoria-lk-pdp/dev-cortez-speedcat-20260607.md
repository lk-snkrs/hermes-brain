# Receipt — DEV Curadoria LK PDP Cortez + Speedcat

Date: 2026-06-07

## Scope

Lucas approved the previously prepared DEV packet with a short `Aprovo` immediately after the requested approval phrase for DEV Curadoria Cortez + Speedcat.

Executed scope: DEV/unpublished theme only.

No Production write, no product write, no price/stock/collection/GMC/Klaviyo/ads/campaign changes.

## Theme

- DEV theme: `155065450718` (`lk-new-theme/dev`, unpublished)

## Assets touched

1. `snippets/lk-variante-cortez-speedcat-20260607.liquid`
2. `sections/lk-pdp.liquid`

Reason for section touch: main Curadoria snippet is above Shopify practical upload limit, so the new split snippet was rendered from the smaller PDP section instead of appending inline to the large asset.

## Actions

Initial apply:

- Created split snippet for:
  - `top30-nike-cortez-breadth`
  - `top30-puma-speedcat-breadth`
- Added render call in DEV PDP section:
  - `{%- render 'lk-variante-cortez-speedcat-20260607', product: product -%}`

Render-scope hotfix:

- Rewrote snippet not to depend on `lk_top30_rendered` assigned inside sibling `{% render %}` calls.
- Added local guard:
  - `lk_cortez_speedcat_rendered`
- Added `lk-variante.css` loading in the split snippet.

## Readback

Initial apply receipt:

- Receipt: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/dev-cortez-speedcat-20260607/20260607T002543Z-receipt.json`
- Snippet target/readback SHA: `a1ee35a3b2064f7db168bdb8678f00c88441edab26650d19562c6b8bfb297fa0`
- Section target/readback SHA: `677726e48834180fe656b31b2ed2c3f43eb674db604f40b672a82f038afa1e1e`
- Readback match: yes

Render-scope hotfix receipt:

- Receipt: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/dev-cortez-speedcat-20260607/20260607T002826Z-render-scope-hotfix-receipt.json`
- Snippet before SHA: `a1ee35a3b2064f7db168bdb8678f00c88441edab26650d19562c6b8bfb297fa0`
- Snippet target/readback SHA: `3a75dcd37a40a264176300326190c3fb40e82fe7b24f254a7cc6bc7c7b7d91fc`
- Readback match: yes

## Static QA

Final source QA passed:

- `lk-variante__grid`: 0
- `lk-variante__image-wrap`: 0
- `lk-variante__rail`: 2
- `lk-variante__media`: 2
- `lk-variante__head`: 2
- group membership guards: 2
- CSS tag count in split snippet: 1
- section render count: 1
- marker `top30-nike-cortez-breadth`: 1
- marker `top30-puma-speedcat-breadth`: 1
- duplicate handles: 0
- malformed image URLs: 0
- handles/labels/images/titles aligned: yes

Public preflight before write:

- Product JS + image URL checks: 24 checks
- Failures: 0
- The previously uncertain 7th Cortez (`tenis-nike-cortez-white-laser-fuchsia-branco`) passed public validation before write.

## Preview QA

Public preview URLs returned HTTP 200 but did not show the newly uploaded DEV markers. This matches the known `preview_theme_id` caveat: public HTML can serve live/main or stale non-preview content for an unpublished theme.

Preview result classification:

- `source_ok_preview_inconclusive`

Representative preview checks attempted:

- `tenis-nike-cortez-sl-white-gym-red-branco`
- `tenis-nike-cortez-white-laser-fuchsia-branco`
- `tenis-puma-speedcat-og-red-white-vermelho`

In all three, source/readback was correct, but public HTML did not expose the new markers, so this was not treated as a source failure.

## Rollback

For full DEV rollback:

1. Restore `sections/lk-pdp.liquid` from:
   - `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/dev-cortez-speedcat-20260607/20260607T002543Z-before-section__lk-pdp.liquid`
2. Remove or restore `snippets/lk-variante-cortez-speedcat-20260607.liquid` using the before backup:
   - `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/dev-cortez-speedcat-20260607/20260607T002543Z-before-snippet__lk-variante-cortez-speedcat-20260607.liquid`

For hotfix-only rollback:

- Restore snippet from:
  - `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/dev-cortez-speedcat-20260607/20260607T002826Z-before-render-scope-hotfix-snippet.liquid`

## Next decision

Do not merge Production yet.

Next safe step: Lucas tests DEV/preview manually if available; if approved, prepare a separate Production merge packet preserving current Production assets and using a scoped merge, not full sync.
