# Report — LK Stock OS internal consult overlay

- Run ID: `20260618T1757POS147857U204LSWD`
- Input DB: `areas/lk/sub-areas/stock/data/lk_stock_os_current_variant_promotion_20260618T175635Z.db`
- Output DB: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/data/lk_stock_os_current_internal_consult_overlay_20260618T1757POS147857U204LSWD.db`
- Decisions total: `560`
- Tiny unique rows promoted to internal consult: `249`
- Parent/base rows classified as non-stock variants: `301`
- Tiny readback failures/skips: `10`
- Non-consultable blocked rows after: `352`
- Identity unresolved rows after: `902`

## Guardrails

- Tiny write: 0
- Shopify write: 0
- Writes externos: 0
- Public availability/pronta entrega pública: 0

## Nota

Este overlay melhora consulta interna e leitura de quantidade quando há readback Tiny único. Ele não corrige cadastro externo nem libera promessa pública.
