# LK Stock OS — auditoria/correção de alertas POS `não encontrado`

- Run ID: `20260616T222042Z`
- Janela auditada: vendas POS locais desde `2026-06-01` no Shopify Sales OS
- Linhas POS auditadas: `6`
- Misses depois da correção: `0`
- Não consultáveis depois da correção: `0`
- Linhas promovidas nesta rodada: `12`
- DB anterior: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/data/lk_stock_os_current_pos_live_promoted_HQ2050_001_20260616T215441Z.db`
- DB nova: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/data/lk_stock_os_current_pos_miss_audit_promoted_20260616T222042Z.db`
- Guardrails: Tiny write 0; Shopify write 0; writes externos 0; public availability 0.

## Correções

- `JR0182` / Adidas Bad Bunny Gazelle Indoor x Messi: 12 variantes resolvidas via crosswalk live read-only Shopify↔Tiny e promovidas para consulta local.
- `JR0182-3` / tamanho 36: Tiny `LK | CONTROLE ESTOQUE` = `1.0` após venda, agora aparece como estoque interno no alerta.
- `HQ2050-001-5` já havia sido corrigido na rodada anterior e permanece consultável com saldo `0.0`.
