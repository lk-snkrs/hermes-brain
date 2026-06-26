# FINAL RECEIPT — GMC Residual Attrs Batch 6 Size/Age/Gender — 2026-06-08

- Aprovação: Lucas `Seguir`.
- Escopo: API-input residual com issue `size`, `age group` e/ou `gender`.
- Ação: Merchant API `productInputs.patch`.
- Campos possíveis: `productAttributes.sizes`, `productAttributes.ageGroup`, `productAttributes.gender`.
- Defaults aplicados quando issue pede: `ageGroup=adult`, `gender=unisex`.
- Size inferido de título/offerId.
- Shopify alterado: não.
- Preço/estoque/GTIN/título/link/color alterados: não por este patch.

## Resultado
- target_count: `39`
- patch_ok: `0`
- patch_fail: `39`
- readback_total: `39`
- readback_confirmed: `0`
- non_target_field_changes_detected: `0`
- remaining_size_age_gender_api_candidates: `39`

## Evidências

- Preview: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/residual-attrs-batch6-size-age-gender-20260608T/preview_candidates.json`
- Snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/residual-attrs-batch6-size-age-gender-20260608T/snapshot_before_patch.json`
- Patch results: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/residual-attrs-batch6-size-age-gender-20260608T/patch_results.jsonl`
- Readback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/residual-attrs-batch6-size-age-gender-20260608T/readback_after_patch.json`

## Correction pass — size field

A primeira tentativa usou `productAttributes.sizes`, que a Merchant API rejeitou. Corrigi para o campo canônico `productAttributes.size` e reexecutei o mesmo escopo.

- target_count: `39`
- patch_ok: `39`
- patch_fail: `0`
- readback_total: `39`
- readback_confirmed: `0`
- still_missing_attrs_after_readback: `39`
- results: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/residual-attrs-batch6-size-age-gender-20260608T/repatch_size_field_results.jsonl`
- readback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/residual-attrs-batch6-size-age-gender-20260608T/repatch_size_field_readback.json`


## Post-scan Batch 6

- total_products: `22663`
- products_with_missing_item_attribute_for_product_type: `375`
- issue_attribute_instances: `[['size', 1090], ['age group', 915], ['gender', 915], ['color', 885]]`
- file: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/residual-attrs-batch6-size-age-gender-20260608T/post_batch6_issue_scan.json`

Nota: o response de `productInputs.patch` confirmou os campos usando os nomes canônicos (`size`, `ageGroup`, `gender`). O processed-product readback pode lagar; o scan global já caiu de 402 para 375 produtos com issue.
