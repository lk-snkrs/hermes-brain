# LK GMC P1 Price Wave6 — Blocked after safe apply attempts

Status: `blocked_requires_merchant_api_v1_registration_or_primary_source_write`

## What was attempted

- Matched all 35 remaining missing-price products to LK Shopify/Data Spine prices.
- Dry-run found safe price source for 35/35:
  - 34 via Shopify handle from Merchant link
  - 1 via exact normalized title
- Applied Content API v2.1 `products.insert` / `products.update` style writes with rollback snapshot.
- Verified via `products.get` and `productstatuses` after delay.

## Result

- Content API accepted the POST/PATCH calls without HTTP error but did **not** persist `price` on these product inputs.
- Fresh recheck still shows:
  - Required attribute rows: 35
  - Required attribute instances: 35
  - Required attribute counts: `{price: 35}`

## Root cause found

Merchant API `products_v1beta` can read these products and identifies the primary product data source:

- `accounts/5297679409/dataSources/10636492695`
- Display name: `Content API`
- Channel: `PRODUCTS`
- Feed label/language: `BR` / `pt`
- Input: `API`

The required update path for `price` is Merchant API ProductInputs v1 (`productAttributes.price` with `amountMicros` + `currencyCode`).

But Merchant API v1 currently returns:

- `GCP_NOT_REGISTERED`
- Project: `openclaw-hst`
- Message: project is not registered with the Merchant account.

Merchant API v1beta PATCH returns:

- `V1BETA_RAMP_DOWN`
- v1beta discontinued on 2026-02-28.

## Safety decision

Did not register/change Merchant API developer settings automatically because that is an account/API configuration write. Needs explicit approval or a credential/project already registered for Merchant API v1.

## Rollback

Content API write attempts are covered by the rollback snapshot generated before apply:

`/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-13-p1-attribute-wave6-price-shopify-source-executor-rollback-20260513T152343Z.json`

No price persisted, so no rollback execution is currently needed.

## Next action options

1. Register/authorize the existing GCP project `openclaw-hst` in Merchant Center for Merchant API v1, then rerun Wave6 via Merchant API ProductInputs PATCH.
2. Use another already-registered Google project/service account for Merchant API v1.
3. Correct the primary source that generated dataSource `10636492695`, if it is controlled outside this credential.
