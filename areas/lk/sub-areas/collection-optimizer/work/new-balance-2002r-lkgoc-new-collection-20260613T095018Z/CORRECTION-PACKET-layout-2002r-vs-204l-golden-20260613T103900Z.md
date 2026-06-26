# Correction packet — 2002R layout aligned to 204L golden

Status: DEV corrected / Production not touched
Data UTC: 20260613T103900Z

## Issue confirmed
Lucas flagged that the New Balance 2002R layout was not matching the 204L golden layout.

Readback confirmed the first DEV implementation was divergent because it used an inline simplified hero in `sections/lk-collection.liquid` instead of rendering the canonical `lk-goc-collection` component with the 204L golden structure.

## Corrective action in DEV only
Theme: `lk-new-theme/dev`
Theme ID: `155065450718`
Role: `UNPUBLISHED`

Changed assets:
- `snippets/lk-goc-collection.liquid`
  - Rebuilt the 2002R hero branch from the approved 204L golden hero structure.
  - Kept the same structural hierarchy, read-more behavior, collage grid, modal behavior and guide contract.
  - Adapted only content, copy, image URLs, labels and SEO/editorial semantics to New Balance 2002R.
- `sections/lk-collection.liquid`
  - Removed simplified inline 2002R hero.
  - Removed simplified inline 2002R guide.
  - Replaced both with canonical renders:
    - `render 'lk-goc-collection', part: 'hero'`
    - `render 'lk-goc-collection', part: 'guide'`

## Verification by Admin API readback
- 2002R snippet case exists: OK
- 2002R read-more alignment fix exists: OK
- 2002R headline exists: OK
- Section renders canonical hero: OK
- Section renders canonical guide: OK
- Old inline hero style removed: OK
- Old inline guide removed: OK

## Production status
No production theme write was made.
Public storefront can still show the non-final/basic production state until Lucas approves merge/promotion.

## Next approval needed
Lucas must approve one of:
1. Promote corrected LKGOC 2002R from DEV to Production; or
2. Temporarily unpublish/hide the collection until visual QA/merge is complete.
