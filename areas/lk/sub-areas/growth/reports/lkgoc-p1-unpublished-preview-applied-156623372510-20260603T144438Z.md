# LKGOC P1 — Applied to unpublished preview theme

- Timestamp UTC: 2026-06-03T14:44:38.930839+00:00
- Theme: `156623372510` — `LK Curadoria Force Fix Preview 2026-06-03`
- Shopify role verified before/after: `unpublished`
- Production writes: none
- Scope respected: no price, stock, products, campaigns, GMC, Klaviyo or checkout changes.

## Assets changed in preview

- `snippets/lk-sambae-204l-hero.liquid` — created in preview.
- `snippets/lk-sambae-204l-guide.liquid` — created in preview.
- `sections/lk-collection.liquid` — updated in preview.
- `sections/main-page.liquid` — updated in preview.
- Dependency snippets created in preview:
  - `snippets/lk-samba-jane-editorial-v3.liquid`
  - `snippets/lk-guide-samba-jane-dev-v7-align.liquid`
- NB 204L guide namespace added in preview:
  - `sections/lk-nb204l-guide-lkgoc.liquid`

## Final QA

- QA file: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/collection-optimizer/qa-runs/lkgoc-unpublished-156623372510-final-qa-20260603T144413Z.json`
- Receipt: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-dev/lkgoc-p1-dev-unpublished-156623372510-20260603T144049Z`
- Core QA result: `True`

Checks:

- Sambae collection: HTTP 200; new copy marker 1; refs marker 3; Liquid errors 0.
- Samba Jane collection: HTTP 200; FAQ schema specific marker 2; Liquid errors 0.
- Sambae guide: HTTP 200; LKGOC namespace 2; FAQPage 1; Liquid errors 0.
- Samba Jane guide: HTTP 200; LKGOC namespace 2; FAQPage 1; Liquid errors 0.
- NB 204L guide: HTTP 200; LKGOC namespace 2; FAQPage 1; Liquid errors 0.

## Remaining limitation

This is preview/unpublished only. Public production still has the previously audited P1 gaps until Lucas explicitly approves a separate production promotion.

## Rollback

Use the `before__*` files in the receipt for assets that existed before. Assets marked `.MISSING` were created in preview and can be removed/reverted if needed. Production was untouched.

## Production approval required separately

Suggested phrase if Lucas wants to promote after visual review:

`Aprovo promover para production o pacote LKGOC P1 validado no theme unpublished 156623372510, com rollback pelos assets do receipt, sem alterar preço/estoque/produtos/campanhas/GMC/Klaviyo/checkout.`
