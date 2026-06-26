# GMC Local LIA link_template micro-pilot — 20 offers

- Generated at: 2026-06-11T11:49:48.438175+00:00
- Approval: Lucas via Telegram: “Aprovo”
- Scope: first 20 local offers from lk-gmc-link-template-preview-2026-06-11.csv with `offer_id` prefix `LIA_` and PDP link.
- Writes: Merchant API `productInputs.patch` only. No Shopify, price, stock, campaign or customer-facing writes.
- Patch OK: 20/20
- Patch failed: 0
- Patch response link_template OK: 20/20
- Immediate processed-product readback link_template OK: 0/20
- Immediate processed-product still has issue `mhlsf_full_missing_valid_link_template`: 20

## Rollback

Use `before_products.json` to restore prior `linkTemplate`, `mobileLinkTemplate` and `adsRedirect` on the same ProductInputs, or allow Simprosys local feed/API source to overwrite if the patch is not sticky.

## Files

- `targets.json`
- `url_checks.json`
- `before_products.json`
- `patch_results.json`
- `immediate_readback.json`
- `summary.json`
## Delayed readback update

- 2026-06-11T11:57:44Z: processed product readback shows `link_template` propagated on 17/20 offers; 3/20 still have `mhlsf_full_missing_valid_link_template` pending/lagging.
- `productInputs.get` is not exposed by the current discovery resource; patch response + processed product readback are the verification surfaces used.
