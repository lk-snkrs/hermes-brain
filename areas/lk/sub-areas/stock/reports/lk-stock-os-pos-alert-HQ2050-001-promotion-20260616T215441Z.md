# LK Stock OS — correção alerta POS HQ2050-001

- Run ID: `20260616T215441Z`
- Input DB: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/data/lk_stock_os_current_internal_consult_overlay_20260616T_INTERNAL_CONSULT_FIX.db`
- Output DB: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/data/lk_stock_os_current_pos_live_promoted_HQ2050_001_20260616T215441Z.db`
- Linhas promovidas: `15`
- SKU alvo: `HQ2050-001-5` / tamanho 38
- Estoque Tiny LK | CONTROLE ESTOQUE: `0.0`
- Guardrails: Tiny write 0; Shopify write 0; writes externos 0; public availability 0.

Correção local/read-only: o alerta POS caiu em `não encontrado` porque o produto novo ainda não estava na superfície local `current_local_stock`. Foi feito crosswalk live read-only Shopify↔Tiny por prefixo `HQ2050-001`, com match exato e sem duplicidades, e as variantes foram promovidas para consulta local.
