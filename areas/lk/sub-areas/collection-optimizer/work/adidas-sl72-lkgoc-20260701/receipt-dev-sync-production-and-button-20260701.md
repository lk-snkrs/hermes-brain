# Receipt — Adidas SL72 DEV sync from Production + guide button

UTC: 2026-07-01T17:24:44Z
Profile: lk-collection-optimizer / LKGOC

## Request
Lucas: Production theme is correct; DEV is outdated; add a button for "Abrir Guia Adidas SL 72 OG vs RS".

## Actions
- Verified Production theme: `155065417950` / `lk-new-theme/production` / MAIN.
- Verified DEV theme: `155065450718` / `lk-new-theme/dev` / UNPUBLISHED.
- Synced from Production to DEV:
  - `sections/lk-collection.liquid`
  - `templates/collection.json`
  - missing referenced sections required by production template:
    - `sections/lk-lululemon-ai-visibility-v3.liquid`
    - `sections/lk-travis-scott-ai-visibility-v4.liquid`
    - `sections/lk-samba-jane-ai-visibility-v5.liquid`
- Added styled button in collection description link:
  - class `lk-goc-sl72-guide-button`
  - text `Abrir Guia Adidas SL 72 OG vs RS`
  - href `/pages/adidas-sl-72-og-vs-rs-guia-lk`

## Verification
- DEV readback: synced section files checksums match Production for all files above except `templates/collection.json`, whose remote checksum differs after Shopify normalization, but body readback is raw-equal to Production.
- Public readback: button class count 1; button text count 1; old duplicate markers `LK_ADIDAS_SL72` and `lk-guia-adidas-sl72-serp` count 0; Liquid error count 0.

## Workdir
/opt/data/work/lkgoc-adidas-sl72-dev-sync-button-20260701T172303Z

## Status
DONE
