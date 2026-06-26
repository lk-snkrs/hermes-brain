# Receipt — Production merge Opção C SWYM híbrido — 20260618T1652Z

- values_printed: false
- GitHub repo: `lk-snkrs/lk-new-theme`
- PR: `https://github.com/lk-snkrs/lk-new-theme/pull/85`
- PR state: merged
- merge commit: `a4ed8a0871a428f30fcab9c1ab990e86bb4201d3`
- theme production: `155065417950` (`lk-new-theme/production`)

## Escopo aplicado

- Added `assets/lk-swym-hybrid-v1.js`.
- Added one `layout/theme.liquid` reference for the hybrid loader.
- Disabled 2 SWYM/Wishlist Plus app embeds in `config/settings_data.json`.
- No price/stock/product/customer/channel writes.

## Readback Shopify Admin

Readback file: `/opt/data/profiles/lk-shopify/cron/output/seo_package_b_20260618/option_c_production/production-readback-20260618T164331Z.json`

- layout marker count: `1`
- asset ref count: `1`
- asset present: `true`
- SWYM enabled app blocks: `0`
- app blocks found and disabled: `2`

## Live QA

First live QA: `/opt/data/profiles/lk-shopify/cron/output/seo_package_b_20260618/option_c_production/production-option-c-live-qa-20260618T164437Z.json`

Second live QA: `/opt/data/profiles/lk-shopify/cron/output/seo_package_b_20260618/option_c_production/production-option-c-live-qa-20260618T164817Z.json`

Focused Home cache QA: `/opt/data/profiles/lk-shopify/cron/output/seo_package_b_20260618/option_c_production/production-home-focused-cache-qa-20260618T164952Z.json`

### Passed

- PDP live passed: before click SWYM `0`, after click SWYM `1`, `_swat=true`, queue `0`, no JS errors.
- Wishlist page live passed: SWYM loads intentionally, `_swat=true`, no JS errors.
- Collection live passed on second QA: before click SWYM `0`, after click SWYM `1`, `_swat=true`, queue `0`, no JS errors.

### Pending / cache propagation

- Home live is intermittently serving old cached HTML from public storefront/CDN.
- Focused home sample: 2/6 rounds served the new hybrid asset; 4/6 rounds served old SWYM auto-load HTML.
- Shopify Admin readback is correct, so this is classified as public cache convergence, not source mismatch.
- Not rolled back because routes serving the new code passed, and stale Home still preserves old SWYM behavior rather than breaking wishlist.

## Rollback

- Git rollback: revert PR #85 / merge commit `a4ed8a0871a428f30fcab9c1ab990e86bb4201d3`.
- Shopify rollback snapshots/readback artifacts stored under `/opt/data/profiles/lk-shopify/cron/output/seo_package_b_20260618/option_c_production/` and previous DEV rollback under `/option_c_dev_upload/`.

## Final status at this receipt

- Source of truth / Shopify Admin: correct.
- Public PDP/collection/wishlist: passed after propagation sampling.
- Public Home: not yet stable; monitor until consecutive new-code samples pass before claiming 100% live convergence.
