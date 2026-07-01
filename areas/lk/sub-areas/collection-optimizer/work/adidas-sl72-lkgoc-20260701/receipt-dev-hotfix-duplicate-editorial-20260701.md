# Receipt — Adidas SL 72 LKGOC DEV hotfix duplicate editorial

UTC: 2026-07-01T15:11:17Z
Profile: lk-collection-optimizer
Scope: DEV/unpublished only

## Target
- Collection: /collections/adidas-sl-72
- DEV theme: 155065450718 / lk-new-theme/dev / UNPUBLISHED
- Production: not intentionally written by this LKGOC hotfix

## Issue
Lucas flagged two editorial blocks. QA confirmed duplicated editorial surface: legacy collection description/rich-content plus new LKGOC guide.

## Actions
- Upserted DEV section `sections/lk-collection.liquid` with:
  - post-grid render for `adidas-sl-72` via `render 'lk-goc-adidas-sl72-guide-panel'`;
  - explicit exclusion of `adidas-sl-72` from legacy `coll-rich-content` path;
  - safety CSS `lk-sl72-dev-hide-legacy-rich-content-20260701` for legacy `.coll-rich-content` in Adidas SL72.
- DEV guide snippet exists: `snippets/lk-goc-adidas-sl72-guide-panel.liquid`.
- DEV section candidate kept in workdir: /opt/data/work/lkgoc-adidas-sl-72-20260701T142720Z

## Verification
- Shopify Admin readback confirms DEV theme role UNPUBLISHED and `sections/lk-collection.liquid` checksum updated after hotfix.
- Public storefront fetch without preview cookie resolves to production/main, not DEV, so visual storefront readback for DEV via fetch is not decision-grade in this turn.
- Public production still must not be changed/promoted without explicit production approval.

## Status
DEV_HOTFIX_APPLIED_ADMIN_READBACK_OK / STOREFRONT_DEV_PREVIEW_COOKIE_NOT_VERIFIED

## Next
Open DEV preview in browser/session with preview cookie, confirm only one Guia LK block after products, then prepare approval packet for production if Lucas approves.
