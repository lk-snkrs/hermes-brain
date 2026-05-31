# Receipt — Onitsuka Tiger collection layout to 204L/new LK standard

Data: 2026-05-30 17:07 BRT
Theme: LK dev/unpublished `155065450718`
Asset: `sections/lk-collection.liquid`
Scope: collection top layout for `onitsuka-tiger` and `onitsuka-tiger-todos-os-modelos`

## Change

- Removed broad Onitsuka handles from the older `lk-next-coll-preview` route.
- Added a scoped `lk-204l-coll-preview` block for Onitsuka Tiger using the same premium collection scaffold used by New Balance 204L:
  - dark editorial hero;
  - breadcrumb + serif H1;
  - `Curadoria LK` copy column;
  - three-image editorial collage column;
  - same reveal/modal behavior classes.

## Backup / rollback

Pre-write backup:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/backups/theme-dev/onitsuka-v2-layout-20260530T170441/sections__lk-collection.liquid`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/backups/theme-dev/onitsuka-v2-layout-20260530T170441/layout__theme.liquid`

Rollback: upload the backed-up `sections__lk-collection.liquid` back to dev theme `155065450718` as `sections/lk-collection.liquid`.

## Verification

Admin API readback after retry:

- patched asset bytes: `219800`
- SHA prefix: `e0ba9fd981e86519`
- readback contained scoped Onitsuka 204L block: yes
- `lk_next_collection_handles` no longer includes broad Onitsuka handles.

Browser preview verification:

- URL: `https://lksneakers.com.br/collections/onitsuka-tiger-todos-os-modelos?preview_theme_id=155065450718&lkqa=onitsuka-vision`
- DOM markers:
  - `.lk-204l-coll-preview`: present
  - `.lk-next-coll-preview`: absent
  - H1: `Onitsuka Tiger`
  - hero aria-label: `Contexto editorial Onitsuka Tiger`
- Visual QA: hero now follows the 204L-style premium mold. Visible overlay noise is from Shopify preview bar / chat widget, not from the section scaffold.

## Non-actions

- No production/main theme write.
- No product, price, stock, collection SEO field, navigation, campaign, GMC or Klaviyo changes.

## Next decision

If Lucas approves this preview, promote the same scoped `sections/lk-collection.liquid` patch to production/main with fresh production backup + public storefront verification.
