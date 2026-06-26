# FINAL RECEIPT — GMC Missing Color Batch 5 Handle Color — 2026-06-08

- Aprovação: Lucas `seguir`.
- Escopo: missing color residual API-input, inferência por sufixo do handle/URL.
- Ação: Merchant API `productInputs.patch`.
- updateMask: `productAttributes.color`.
- Shopify alterado: não.
- Preço/estoque/GTIN/título/link alterados: não por este patch.

## Resultado
- target_count: `85`
- patch_ok: `85`
- patch_fail: `0`
- readback_total: `85`
- readback_confirmed_color: `0`
- still_missing_color_readback: `85`
- non_color_field_changes_detected: `0`

## Scan pós-Batch 5
- total_products: `22663`
- issue_products: `402`
- issue_no_color: `177`
- skipped_nonapi_no_color: `24`
- handle_color_candidates_remaining: `0`

## Evidências

- Preview: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/missing-color-batch5-handle-20260608T/preview_candidates.json`
- Snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/missing-color-batch5-handle-20260608T/snapshot_before_patch.json`
- Patch results: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/missing-color-batch5-handle-20260608T/patch_results.jsonl`
- Readback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/missing-color-batch5-handle-20260608T/readback_after_patch.json`

## Readback second pass

- readback_total: `85`
- found: `85`
- readback_confirmed_color: `85`
- still_missing_color_readback: `0`
- file: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/missing-color-batch5-handle-20260608T/readback_after_patch_second_pass.json`
