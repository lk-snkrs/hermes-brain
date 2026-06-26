# Receipt — PDP size guide brand tables DEV

Date: 2026-06-15
Owner: LK Shopify
Scope: Shopify DEV/unpublished theme only

## User approval / scope

Lucas asked to do all previously listed PDP size-guide table improvements. Execution was scoped to DEV first; Production was not merged/published.

## Target

- Theme: `lk-new-theme/dev`
- Theme ID: `155065450718`
- Role verified before upload: `unpublished`
- Asset: `sections/lk-pdp.liquid`

## Changes added to DEV

Added/expanded hardcoded PDP size-guide detection and tables for:

- Onitsuka Tiger / Mexico 66
- Adidas general, including Samba/Gazelle/Spezial copy
- ASICS lifestyle/running guidance
- Adidas Yeezy / Yeezy 350-style half-size-up guidance
- UGG
- Birkenstock
- Nike general fallback

Preserved existing exceptions:

- Nike Mind 001
- Nike Mind 002
- Nike Vomero Premium
- Jordan 1 Low
- Jordan 1 Mid
- Jordan 1 High
- New Balance-style fallback

## Evidence

Sources/references used during preparation:

- Onitsuka Tiger official size guide / fit guidance snippet: loose fit one size up; Mexico 66 narrow signal from size-guide search result.
- Adidas official shoe chart and official Samba size-guide snippet: regular size, half size up for wider fit.
- ASICS official shoe-size guide plus lifestyle/running fit references.
- Yeezy fit references: Boost 350 V2 commonly runs small / half size up.
- UGG official all-gender sizing information.
- Birkenstock official/retailer size-chart references; EU whole-size footbed guidance.

Shopify readback:

- Old DEV asset SHA-12: `8444d3aede2f`
- New local/readback SHA-12: `578d423d3f13`
- Readback matched local after retry: yes
- `values_printed=false`

Backup:

- `/opt/data/worktrees/lk-new-theme-remove-mk-custom-20260615/backups/shopify-dev-sizeguide-brand-tables-20260615/sections__lk-pdp.liquid.20260615-201518.liquid`

## DEV QA

Representative product handles checked in DEV preview session:

- Onitsuka: `tenis-onitsuka-tiger-mexico-66-kill-bill-amarelo`
- Adidas: `samba-og-white-scarlet`
- ASICS: `tenis-asics-gt-2160-white-putty-branco`
- Yeezy: `yeezy-slide-glow-green`
- UGG: `tenis-ugg-zora-ballet-flat-chestnut-marrom`
- Nike general: `nike-dunk-low-rose-whisper`
- Control Jordan Mid: `air-jordan-1-mid-wolf-grey`
- Control Vomero Premium: `tenis-nike-vomero-premium-black-volt-preto`

Result:

- Size-guide modal present on all tested pages.
- New brand labels/copies/tables present where expected.
- Jordan Mid and Vomero controls preserved.
- No size-guide-specific Liquid error observed.

Known unrelated DEV issue observed:

- DEV storefront HTML shows pre-existing layout-level error: `Liquid error (layout/theme line 513): Could not find asset snippets/lk-growth-geo-faq-schema.liquid`.
- This is outside `sections/lk-pdp.liquid`; markers still rendered correctly. Needs separate DEV theme cleanup if desired.

## Non-actions

- No Production merge/publish.
- No live/main theme write.
- No product/price/stock/variant/metafield changes.
- No GMC/Klaviyo/WhatsApp/campaign action.

## Rollback

DEV rollback: upload the backup asset above back to theme `155065450718`, asset `sections/lk-pdp.liquid`, then read back SHA and QA representative PDPs.

Production path if approved later: branch from `origin/production`, reapply the scoped `sections/lk-pdp.liquid` size-guide block only, PR into `production`, merge, Shopify Production readback, live public QA, receipt.
