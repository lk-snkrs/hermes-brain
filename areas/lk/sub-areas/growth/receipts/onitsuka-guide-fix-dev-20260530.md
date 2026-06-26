# Receipt — Onitsuka Tiger guide fix in dev

Date: 2026-05-30
Theme: Shopify dev `155065450718`
Surface: `/collections/onitsuka-tiger-todos-os-modelos?preview_theme_id=155065450718`

## Lucas correction
The Onitsuka Tiger premium collection migration was incomplete because the after-grid Guia Editorial LK was missing. For LK collection migrations, the 204L/premium standard includes both the hero/header and the after-grid guide.

## Change applied
File: `sections/lk-collection.liquid`

- Added broad Onitsuka handles to the canonical after-grid `lk-guide-standard-panel` route:
  - `onitsuka-tiger`
  - `onitsuka-tiger-todos-os-modelos`
- Added guide anchor: `#lk-guia-onitsuka-tiger`.
- Added Onitsuka-specific guide copy:
  - editorial H2;
  - intro;
  - “Como escolher Onitsuka Tiger” bullets;
  - FAQ inside the guide panel;
  - CTA to `/pages/onitsuka-tiger-original-brasil-guia-lk`.
- Suppressed legacy `.coll-faq` for broad Onitsuka handles to avoid duplicate FAQ UX/schema.
- Added scoped CSS so broad Onitsuka uses the same canonical after-grid guide structure as 204L/Sabot/Moon Shoe.

## Verification
Admin readback after upload:

- bytes: `228713`
- sha256 prefix: `6236889868942852`
- checks:
  - broad handles in guide condition: true
  - standalone guide link present: true
  - legacy FAQ suppression broad: true
  - JSON FAQ branch present: true

Storefront DOM on dev preview:

- `#lk-guia-onitsuka-tiger`: present
- CTA href: `/pages/onitsuka-tiger-original-brasil-guia-lk`
- guide FAQ details count: 5
- `.coll-faq` legacy block: absent
- `FAQPage` JSON-LD count: 1
- guide card computed display: `grid`

Visual check: browser vision confirmed the guide appears below the product grid with premium layout: large editorial title, chooser bullets left, FAQ right, lower helper note and black CTA.

## Backup
Pre-fix server asset backup:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/backups/theme-dev/onitsuka-guide-fix-20260530T171651/sections__lk-collection.liquid`

## Documentation updated
Skill: `lk-collection-patterns`

Added reference:
`references/onitsuka-tiger-guide-omission-correction.md`

Patched skill rules to state that premium/204L collection migration is incomplete unless the after-grid Guia Editorial LK is rendered/linked, FAQ is integrated, legacy `.coll-faq` is suppressed, and live preview verifies the result.

## Production status
Production untouched. Requires Lucas approval before promotion to main theme `155065417950`.
