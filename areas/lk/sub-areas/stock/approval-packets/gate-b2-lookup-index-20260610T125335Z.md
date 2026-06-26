# Gate B2 — índice de lookup local — 20260610T125335Z

Objetivo: consultar rapidamente por SKU, handle ou título e cair no packet local correto sem mexer em Shopify/Tiny. Inclui bloqueios Gate B2 e os 6 matches P0 resolvidos em cache local.

## Totais
- rows: `911`
- unique_skus: `903`
- handles: `558`
- lane_counts: `{'BLOCKED_TINY_MISSING': 459, 'BLOCKED_SHOPIFY_DUPLICATE': 293, 'BLOCKED_TINY_DUPLICATE': 96, 'BLOCKED_TINY_DEPOSIT_MISSING': 57, 'CONSULTABLE_LOCAL_RESOLVED': 6}`
- priority_counts: `{'P0_saneamento': 90, 'P1_saneamento': 319, 'P2_saneamento': 502}`
- writes_externos: `0`
- public_availability_safe_rows: `0`
- includes_p0_resolved_cache_rows: `6`

- FTS SQLite: `True`

## Arquivos
- SQLite lookup: `areas/lk/sub-areas/stock/data/gate_b2_lookup_index_20260610T125335Z.db`
- JSON: `areas/lk/sub-areas/stock/reports/gate-b2-lookup-index-20260610T125335Z.json`
- CSV: `areas/lk/sub-areas/stock/reports/gate-b2-lookup-index-20260610T125335Z.csv`
- Fonte fila bloqueios: `areas/lk/sub-areas/stock/data/gate_b2_all_lanes_local_work_queue_20260610T123635Z.db`
- Fonte resolvidos P0: `areas/lk/sub-areas/stock/data/gate_b2_p0_consultable_crosswalk_20260610T120920Z.db`

## Guardrails
- Local/cache only
- Tiny write: 0
- Shopify write: 0
- Disponibilidade pública: 0
