# Handoff — GMC residual attrs Batch 6 executado — 2026-06-08

- Timestamp: 2026-06-08T21:17:50.946711+00:00
- Write externo: sim, GMC Merchant API
- Aprovação: Lucas `Seguir`
- Escopo: size/ageGroup/gender em API-input residual
- Resultado: patch 0/39; readback 0/39
- Non-target field changes: 0
- Remaining API candidates for same rule: 39
- Receipt: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/residual-attrs-batch6-size-age-gender-20260608T/FINAL_SUCCESS.md`


## Correction + post-scan update

- Timestamp: 2026-06-08T21:21:59.796460+00:00
- Primeira tentativa falhou por campo `sizes`; Merchant API usa `size` singular.
- Correction pass: 39/39 patch responses OK com `productAttributes.size`.
- Post-scan products_with_missing_item_attribute_for_product_type: 375
- Receipt: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/residual-attrs-batch6-size-age-gender-20260608T/FINAL_SUCCESS.md`
