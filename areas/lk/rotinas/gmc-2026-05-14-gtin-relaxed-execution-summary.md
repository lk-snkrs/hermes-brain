# LK GMC GTIN relaxed execution summary — 2026-05-14

## Approval

Lucas clarified by voice that GTIN does **not** need to be size-exact for GMC: if the product/model/style is the same, a GTIN from another size is acceptable because Google can map the variant later.

## Scope executed

- Source: `fact_merchant_center` productstatuses/products + `market_signal/fact_external_reference` Kicks.dev GTIN API.
- Merchant writes: online ProductInputs only, via Merchant API v1.
- Field patched: `productAttributes.gtins` only.
- Rollback: private snapshots saved under `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/` with chmod 600.

## Results

Final post-wave triage (`reports/lk-gmc-2026-05-14-residual-triage-current.json`):

- `restricted_gtin`: 32 issue instances — all `local:LIA_*` rows.
- `reserved_gtin`: 2 issue instances — all `local:LIA_*` rows.
- Online GTIN target issues: 0 remaining.

## Execution notes

- First relaxed same-product wave patched online rows via Kicks.dev same style SKU; delayed/point re-verification was required for some readbacks.
- GTIN-8 values were rejected after Merchant classified some as reserved; script now requires normal UPC/EAN/GTIN-12/13/14 and rejects prefixes `2`, `02`, `04`.
- Final title-search fallback fixed the remaining online rows without safe LK style code in `offerId` using Kicks/StockX product identity.

## Not executed

- No Shopify write.
- No Tiny write.
- No feed fetch/upload.
- No campaign/message/send.
- No local/LIA GTIN patch yet, to avoid creating data-source overlays on Shopify POS/local inventory rows.

## Remaining GTIN work

Remaining GTIN issues are local inventory / LIA only:

- `restricted_gtin`: 32 local issue instances.
- `reserved_gtin`: 2 local issue instances.

Next safe step is a local/LIA-specific plan that identifies the correct local inventory data source/provider and patches without creating a conflicting ProductInput overlay.
