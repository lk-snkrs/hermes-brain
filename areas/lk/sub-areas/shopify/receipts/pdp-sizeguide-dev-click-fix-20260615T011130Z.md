# Receipt — PDP Size Guide DEV click fix

- Timestamp UTC: 2026-06-15T01:11:30Z
- Storefront surface: LK Sneakers PDP
- Asset: `sections/lk-pdp.liquid`
- DEV theme: `lk-new-theme/dev` (`155065450718`, unpublished)
- Production theme: `lk-new-theme/production` (`155065417950`, main)

## Root cause after Lucas retest

The first DEV patch removed the `sgFocusTrap` JavaScript error, but the popup still did not open because the script captured/bound the `.pi-size-guide` trigger before the rendered trigger was available. Real browser QA showed clicking the button kept the modal as `sg-modal`, `aria-hidden=true`, `visibility=hidden`, `opacity=0`.

## Action performed

Uploaded a second scoped DEV-only fix to `sections/lk-pdp.liquid`:

- introduced `initSizeGuideModal()`;
- guarded binding with `data-lk-size-guide-bound`;
- runs initialization immediately, on `DOMContentLoaded`, and on `load`;
- uses delegated click handling for `.pi-size-guide`;
- preserves modal open/close, Escape, backdrop close, focus restoration, and tab behavior.

No Production upload/publish was performed.

## Verification

Shopify Asset API readback:

- DEV before SHA256: `42b85cd44027f6323dd6e228531f984850a516dc87c50d4ef5e8d3f519380b39`
- DEV after SHA256: `89c7d06d9b99f8c51686a63541d854650b63ee5f4f412a292eeaa365f13d6c7a`
- Target SHA256: `89c7d06d9b99f8c51686a63541d854650b63ee5f4f412a292eeaa365f13d6c7a`
- Production before SHA256: `5597dc4d04dc2c284441c295a5a47b0a5573cecea57bebb2de841275c44a5116`
- Production after SHA256: `5597dc4d04dc2c284441c295a5a47b0a5573cecea57bebb2de841275c44a5116`
- Production unchanged: yes

Real Chromium/CDP preview QA after click:

- Button found: yes (`.pi-size-guide`)
- After click modal class: `sg-modal is-open`
- After click `aria-hidden`: `false`
- Body overflow: `hidden`
- Modal visibility: `visible`
- Modal opacity: `1`
- `sgFocusTrap`: absent

Screenshot after click saved locally:

`/tmp/lk_sizeguide_after_click.png`

## Backup

Backup directory:

`areas/lk/sub-areas/shopify/backups/theme-assets/pdp-sizeguide-dev-delegated-click-20260615T011130Z`

Rollback file:

`dev-before-sections__lk-pdp.liquid`

## Rollback

PUT `dev-before-sections__lk-pdp.liquid` back to theme `155065450718`, asset `sections/lk-pdp.liquid`, then rerun readback and preview QA.

## Status

DEV fixed and verified by real headless-browser click. Production remains unchanged. Pending Lucas confirmation before Production promotion.
