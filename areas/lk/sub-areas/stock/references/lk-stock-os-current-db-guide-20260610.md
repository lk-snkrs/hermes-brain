# LK Stock OS — guia da DB atual local

## DB atual

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/data/lk_stock_os_current_20260610T165523Z.db`

Pointer estável:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/data/lk_stock_os_current_pointer.json`

## Tabelas

- `current_local_stock`: visão principal por SKU+handle.
- `stock_observations`: 8.333 observações/propostas detalhadas vindas dos batches Gate B2.
- `master_register`: 558 linhas por priority/lane/handle.
- `data_quality_gaps`: contagem dos bloqueios/gaps remanescentes.
- `source_metadata`: fontes e resumo.

## Consultas úteis

```bash
sqlite3 /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/data/lk_stock_os_current_20260610T165523Z.db   "select canonical_status,count(*) from current_local_stock group by canonical_status;"

sqlite3 /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/data/lk_stock_os_current_20260610T165523Z.db   "select priority,decision_lane,count(*) from current_local_stock group by priority,decision_lane order by priority,decision_lane;"

sqlite3 /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/data/lk_stock_os_current_20260610T165523Z.db   "select sku,handle,size,canonical_status,stock_quantity_observed_values from current_local_stock where stock_positive_observed=1 limit 20;"
```

## Regra operacional

- `local_consult_safe=1` significa que a linha pode ser consultada internamente com seu status/gap.
- `identity_resolved_safe=1` significa match local resolvido, mas **não libera pronta entrega**.
- `public_availability_safe=0` em todas as linhas.
- Antes de responder cliente/pronta entrega: consultar Tiny/fonte viva no momento.
