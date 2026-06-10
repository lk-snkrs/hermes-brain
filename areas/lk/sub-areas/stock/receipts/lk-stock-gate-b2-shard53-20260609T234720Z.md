# Receipt — LK Stock Gate B.2 shard 53

Data/hora UTC: 20260609T234720Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard53_20260609T234046Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard53-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard53-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard53-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 111
- `availability_claim_allowed = 1`: 106
- Bloqueadas: 5
- Issues abertas: 5

### Status

- `matched_exact_sku_stock_resolved`: 106
- `shopify_variant_tiny_missing`: 3
- `shopify_duplicate_sku_blocked`: 1
- `tiny_duplicate_exact_code_blocked`: 1

### Duplicidade Shopify bloqueada

- `LIP5`

### Duplicidade Tiny bloqueada

- `U9060NRJ-44`

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `new-balance-9060-triple-white`: 2
- `tenis-new-balance-530-turtledove-mushroom-mesh-casual`: 1
- `tenis-new-balance-9060-grey-day-2025-esportivo-casual`: 1
- `the-peptide-lip-tints-rhode-limited-edition-shade-dourado`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 2.769s

OK
20260609T234720Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
