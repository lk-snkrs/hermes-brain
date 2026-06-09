# FINAL RECEIPT — GMC Missing Color Batch 4 API-input-only — 2026-06-08

- Aprovação: Lucas `SEGUIR`.
- Ação: Merchant API `productInputs.patch`.
- updateMask: `productAttributes.color`.
- Data source: API-input allowlist only.
- Shopify alterado: não.
- Preço/estoque/GTIN/título/link alterados: não por este patch.

## Resultado
- candidate_count_all: `404`
- preview_count: `404`
- patch_ok: `404`
- patch_fail: `0`
- readback_total: `404`
- readback_errors: `0`
- readback_confirmed_color: `394`
- still_missing_color_readback: `10`
- non_color_field_changes_detected: `0`

## Scan pós-Batch 4
- total_products: `22663`
- issue_products: `487`
- issue_no_color: `262`
- high_confidence_api_candidates_remaining: `0`

## Evidências

- Preview: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/missing-color-batch4-20260608T/preview_candidates.json`
- Snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/missing-color-batch4-20260608T/snapshot_before_patch.json`
- Patch results: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/missing-color-batch4-20260608T/patch_results.jsonl`
- Readback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/missing-color-batch4-20260608T/readback_after_patch.json`
- Post-scan: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/missing-color-batch4-20260608T/post_batch4_issue_scan.json`

## Rollback

- Snapshot pré-write salvo.
- Rollback/correção por offerId via `productAttributes.color`, se necessário.

## Readback second pass

- readback_total: `404`
- found: `404`
- readback_confirmed_color: `404`
- still_missing_color_readback: `0`
- file: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/missing-color-batch4-20260608T/readback_after_patch_second_pass.json`
