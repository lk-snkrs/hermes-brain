# Report — LK Stock OS internal consult overlay

- Run ID: `20260616T_INTERNAL_CONSULT_FIX`
- Input DB: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/data/lk_stock_os_current_tiny_full_sync_20260616T082014Z.db`
- Output DB: `areas/lk/sub-areas/stock/data/lk_stock_os_current_internal_consult_overlay_20260616T_INTERNAL_CONSULT_FIX.db`
- Decisions total: `473`
- Tiny unique rows promoted to internal consult: `218`
- Parent/base rows classified as non-stock variants: `255`
- Tiny readback failures/skips: `0`
- Non-consultable blocked rows after: `179`
- Identity unresolved rows after: `718`

## Guardrails

- Tiny write: 0
- Shopify write: 0
- Writes externos: 0
- Public availability/pronta entrega pública: 0

## Nota

Este overlay melhora consulta interna e leitura de quantidade quando há readback Tiny único. Ele não corrige cadastro externo nem libera promessa pública.
