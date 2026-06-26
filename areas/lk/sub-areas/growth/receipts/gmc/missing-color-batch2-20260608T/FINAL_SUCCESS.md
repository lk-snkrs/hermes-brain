# FINAL RECEIPT — GMC Missing Color Batch 2 — 2026-06-08

- Escopo aprovado: Batch 2 preview de 500 candidatos.
- Ação: Merchant API `productInputs.patch`.
- updateMask: `productAttributes.color`.
- Shopify alterado: não.
- Preço/estoque/GTIN/título/link alterados: não por este patch.

## Resultado
- preview_count: `500`
- patch_rows: `500`
- patch_ok: `495`
- patch_fail: `5`
- readback_total: `500`
- readback_errors: `0`
- readback_confirmed_color: `495`
- still_missing_color_readback: `5`
- non_color_field_changes_detected: `0`

## Itens não aplicados por bloqueio de fonte
- `11810372920072143991` — datasource não é API input / origem fileInput
- `3876299146406606317` — datasource não é API input / origem fileInput
- `6562590402534581177` — datasource não é API input / origem fileInput
- `10002025469927148791` — datasource não é API input / origem fileInput
- `2258634078163248862` — datasource não é API input / origem fileInput

## Evidências

- Snapshot pré-write: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/missing-color-batch2-20260608T/snapshot_before_patch.json`
- Patch results: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/missing-color-batch2-20260608T/patch_results.jsonl`
- Readback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/missing-color-batch2-20260608T/readback_after_patch.json`
- Summary: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/missing-color-batch2-20260608T/summary.json`

## Rollback

- Snapshot pré-write salvo.
- Como os targets estavam sem `color`, rollback/correção exige patch específico de `productAttributes.color` por offerId, se alguma inferência for julgada incorreta.

## Scan pós-Batch 2

- total_products: `22663`
- products_with_missing_item_attribute_for_product_type: `1391`
- issue_instances_missing_item_attribute_for_product_type: `9050`
- products_with_missing_issue_and_no_color: `1166`
- products_with_landing_page_error: `13`
- scan_file: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/missing-color-batch2-20260608T/post_batch2_issue_scan.json`
