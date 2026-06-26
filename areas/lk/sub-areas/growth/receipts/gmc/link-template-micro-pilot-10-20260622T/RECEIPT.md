# GMC link_template micro-pilot 10 — 2026-06-22

- Generated: 2026-06-22T17:36:42.937806+00:00
- Approval: Lucas `APROVO OS 3 EM SEQUENCIA, 1 2 e 3`
- Writes: Merchant API `productInputs.patch` only. No Shopify/price/stock/campaign writes.
- Targets: 10
- URL checks OK: 10
- Patch OK: 10
- Patch failed: 0
- Patch response link_template OK: 10
- Immediate processed readback link_template OK: 10
- Immediate still has issue `mhlsf_full_missing_valid_link_template`: 0

## Rollback
Restore prior `linkTemplate`, `mobileLinkTemplate`, `adsRedirect` from `before_products.json` on same ProductInputs.

## Note
Processed product/status can lag or be overwritten by Simprosys local feed; delayed readback required.

## Delayed readback 20s

- Generated: 2026-06-22T17:37:26.806696+00:00
- link_template OK: 10/10
- remaining `mhlsf_full_missing_valid_link_template`: 0
- read errors: 0
