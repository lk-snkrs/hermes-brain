# FINAL RECEIPT — GMC Category Correction Batch 7 — 2026-06-08

- Aprovação: Lucas `Aprovo`.
- Ação: Merchant API `productInputs.patch`.
- updateMask: `productAttributes.googleProductCategory`.
- Shopify alterado: não.
- Preço/estoque/GTIN/título/link/color alterados: não por este patch.

## Resultado
- preview_count: `34`
- targets_after_safety_filter: `34`
- skipped_before_patch: `0`
- patch_ok: `34`
- patch_fail: `0`
- readback_total: `34`
- readback_confirmed_category: `0`
- non_category_field_changes_detected: `0`

## Evidências

- Snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/category-correction-batch7-20260608T/snapshot_before_patch.json`
- Patch results: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/category-correction-batch7-20260608T/patch_results.jsonl`
- Readback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/category-correction-batch7-20260608T/readback_after_patch.json`
- Summary: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/category-correction-batch7-20260608T/summary.json`

## Rollback

- Snapshot pré-write salvo com categoria anterior por offerId.
- Rollback: patch de `productAttributes.googleProductCategory` de volta ao valor anterior, se necessário.

## Readback second pass

- readback_total: `34`
- found: `34`
- readback_confirmed_category: `11`
- not_confirmed: `23`
- file: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/category-correction-batch7-20260608T/readback_after_patch_second_pass.json`

Nota: a resposta do `productInputs.patch` confirmou 34/34. O processed product pode lagar ou normalizar categoria; monitorar D+1/D+7.


## Post-scan Batch 7

- total_products: `22629`
- products_with_missing_item_attribute_for_product_type: `296`
- issue_attribute_instances: `[('color', 850), ('age group', 725), ('gender', 725), ('size', 705)]`
- file: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/category-correction-batch7-20260608T/post_batch7_issue_scan.json`
