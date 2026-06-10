# Gate B2 — visão canônica local atual — 20260610T130644Z

Objetivo: consulta futura deve priorizar o estado local atual por SKU+handle. Quando um match resolvido existe, ele supera bloqueio antigo do mesmo SKU+handle, mantendo histórico superseded para auditoria.

## Totais
- canonical_rows: `903`
- input_rows: `911`
- superseded_rows: `8`
- handles: `558`
- unique_skus: `903`
- status_counts: `{'CONSULTABLE_LOCAL_RESOLVED': 6, 'BLOCKED_TINY_MISSING': 457, 'BLOCKED_TINY_DUPLICATE': 96, 'BLOCKED_SHOPIFY_DUPLICATE': 287, 'BLOCKED_TINY_DEPOSIT_MISSING': 57}`
- priority_counts: `{'P0_saneamento': 89, 'P1_saneamento': 318, 'P2_saneamento': 496}`
- resolved_current_rows: `6`
- writes_externos: `0`
- tiny_write: `0`
- shopify_write: `0`
- public_availability_safe_rows: `0`

## Status canônico
- CONSULTABLE_LOCAL_RESOLVED: `6`
- BLOCKED_TINY_MISSING: `457`
- BLOCKED_TINY_DUPLICATE: `96`
- BLOCKED_SHOPIFY_DUPLICATE: `287`
- BLOCKED_TINY_DEPOSIT_MISSING: `57`

## Arquivos
- SQLite: `areas/lk/sub-areas/stock/data/gate_b2_canonical_current_index_20260610T130644Z.db`
- JSON: `areas/lk/sub-areas/stock/reports/gate-b2-canonical-current-index-20260610T130644Z.json`
- CSV: `areas/lk/sub-areas/stock/reports/gate-b2-canonical-current-index-20260610T130644Z.csv`
- Fonte lookup: `areas/lk/sub-areas/stock/data/gate_b2_lookup_index_20260610T125335Z.db`

## Guardrails
- Local/cache only
- Tiny write: 0
- Shopify write: 0
- Disponibilidade pública/pronta entrega: 0
- Histórico superseded preservado; nada apagado dos artefatos anteriores.
