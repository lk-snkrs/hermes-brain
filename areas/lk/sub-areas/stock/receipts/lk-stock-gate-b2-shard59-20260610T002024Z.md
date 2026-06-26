# Receipt — LK Stock Gate B.2 shard 59

Data/hora UTC: 20260610T002024Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard59_20260610T001126Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard59-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard59-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard59-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 153
- `availability_claim_allowed = 1`: 152
- Bloqueadas: 1
- Issues abertas: 1

### Status

- `matched_exact_sku_stock_resolved`: 152
- `shopify_variant_tiny_missing`: 1

### Duplicidade Shopify bloqueada

- Nenhuma

### Duplicidade Tiny bloqueada

- Nenhuma

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `990v6-made-in-usa-triple-black`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 3.132s

OK
20260610T002024Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
