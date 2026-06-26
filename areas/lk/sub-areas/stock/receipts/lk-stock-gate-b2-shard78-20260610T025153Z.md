# Receipt — LK Stock Gate B.2 shard 78

Data/hora UTC: 20260610T025153Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard78_20260610T024033Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard78-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard78-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard78-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 195
- `availability_claim_allowed = 1`: 190
- Bloqueadas: 5
- Issues abertas: 5

### Status

- `matched_exact_sku_stock_resolved`: 190
- `shopify_duplicate_sku_blocked`: 5

### Duplicidade Shopify bloqueada

- `NDP006-1`
- `NDP006-2`
- `NDP006-3`
- `NDP006-4`
- `NDP006-5`

### Duplicidade Tiny bloqueada

- Nenhuma

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `camiseta-nude-project-global-soon-ash-cinza`: 5

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 4.009s

OK
20260610T025153Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
