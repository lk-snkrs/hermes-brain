# FINAL RECEIPT — GMC Residual Manual Enrichment Batch 8 High/Medium — 2026-06-09

- Aprovação: Lucas `Seguir` após decisões: prefill A, adult/unisex, size BR/P-M-G-GG/Único, não fazer fileInput.
- Escopo: somente linhas high/medium do prefill API-input.
- Ação: Merchant API `productInputs.patch`.
- Campos possíveis: `color`, `size`, `ageGroup`, `gender`.
- Shopify alterado: não.
- fileInput/fonte externa alterado: não.
- Preço/estoque/GTIN/título/link alterados: não por este patch.

## Resultado
- rows_in_source: `95`
- targets_after_safety_filter: `95`
- skipped_before_patch: `0`
- patch_ok: `95`
- patch_fail: `0`
- readback_total: `95`
- readback_confirmed: `0`
- non_target_field_changes_detected: `0`

## Post-scan
- total_products: `22595`
- products_with_missing_item_attribute_for_product_type: `224`
- issue_attribute_instances: `[('color', 655), ('age group', 555), ('gender', 555), ('size', 535)]`

## Evidências

- Snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/residual-manual-enrichment-batch8-high-medium-20260609T/snapshot_before_patch.json`
- Patch results: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/residual-manual-enrichment-batch8-high-medium-20260609T/patch_results.jsonl`
- Readback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/residual-manual-enrichment-batch8-high-medium-20260609T/readback_after_patch.json`
- Summary: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/residual-manual-enrichment-batch8-high-medium-20260609T/summary.json`

## Rollback

- Snapshot pré-write salvo.
- Rollback/correção por offerId usando os valores anteriores dos campos alterados.

## Size rollback correction

Detectei que parte do prefill inferiu `size` por sufixo do offerId mesmo quando o produto já tinha `size` correto no readback/snapshot. Para evitar sobrescrever tamanho correto, executei rollback pontual do campo `size` para o valor pré-write nesses casos.

- rollback_candidates: `33`
- rollback_ok: `33`
- rollback_fail: `0`
- results: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/residual-manual-enrichment-batch8-high-medium-20260609T/rollback_size_mismatches_results.jsonl`
- summary: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/residual-manual-enrichment-batch8-high-medium-20260609T/rollback_size_mismatches_summary.json`


## Final post-rollback scan

- total_products: `22595`
- products_with_missing_item_attribute_for_product_type: `168`
- issue_attribute_instances: `[('age group', 555), ('gender', 555), ('size', 535), ('color', 375)]`
- file: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/residual-manual-enrichment-batch8-high-medium-20260609T/final_post_rollback_issue_scan.json`
