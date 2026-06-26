# FINAL RECEIPT — GMC Missing Color Batch 3 API-input-only — 2026-06-08

- Aprovação: Lucas `SEGUIR APROVADO`.
- Ação: Merchant API `productInputs.patch`.
- updateMask: `productAttributes.color`.
- Data source: API-input allowlist only.
- Shopify alterado: não.
- Preço/estoque/GTIN/título/link alterados: não por este patch.

## Resultado
- candidate_count_all: `904`
- preview_count: `500`
- patch_ok: `500`
- patch_fail: `0`
- readback_total: `500`
- readback_errors: `0`
- readback_confirmed_color: `473`
- still_missing_color_readback: `27`
- non_color_field_changes_detected: `0`

## Scan pós-Batch 3
- total_products: `22663`
- issue_products: `891`
- issue_no_color: `666`
- high_confidence_api_candidates_remaining: `404`

## Evidências

- Preview: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/missing-color-batch3-20260608T/preview_candidates.json`
- Snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/missing-color-batch3-20260608T/snapshot_before_patch.json`
- Patch results: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/missing-color-batch3-20260608T/patch_results.jsonl`
- Readback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/missing-color-batch3-20260608T/readback_after_patch.json`
- Post-scan: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/missing-color-batch3-20260608T/post_batch3_issue_scan.json`

## Rollback

- Snapshot pré-write salvo.
- Rollback/correção por offerId via `productAttributes.color`, se necessário.

## Readback second pass

- readback_total: `500`
- found: `500`
- readback_confirmed_color: `500`
- still_missing_color_readback: `0`
- file: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/missing-color-batch3-20260608T/readback_after_patch_second_pass.json`
