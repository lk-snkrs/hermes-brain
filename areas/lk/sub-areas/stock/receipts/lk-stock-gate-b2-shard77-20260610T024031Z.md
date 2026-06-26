# Receipt — LK Stock Gate B.2 shard 77

Data/hora UTC: 20260610T024031Z

## Escopo

- Perfil/dono: `[LK] Estoque Loja Física` / `lk-stock`
- Tarefa: Gate B.2 crosswalk Tiny↔Shopify em shard de catálogo ativo
- Modo: local/read-only/dry-run
- Writes externos: 0
- Tiny write: 0
- Shopify write: 0
- Cron/webhook/runtime: nenhum ativado
- Secrets impressos: não

## Artefatos

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard77_20260610T023254Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard77-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard77-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard77-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 127
- `availability_claim_allowed = 1`: 124
- Bloqueadas: 3
- Issues abertas: 3

### Status

- `matched_exact_sku_stock_resolved`: 124
- `shopify_duplicate_sku_blocked`: 3

### Duplicidade Shopify bloqueada

- `553560118`
- `553560800`
- `554725-132-1`

### Duplicidade Tiny bloqueada

- Nenhuma

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `air-jordan-1-low-gs-light-arctic-pink`: 1
- `air-jordan-1-low-white-university-red`: 1
- `jordan-1-mid-tropical-twist-igloo-gs`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 4.207s

OK
20260610T024031Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
