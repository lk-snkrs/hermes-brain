# Receipt — LK Stock Gate B.2 shard 42

Data/hora UTC: 20260609T215238Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard42_20260609T213739Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard42-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard42-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard42-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 256
- `availability_claim_allowed = 1`: 253
- Bloqueadas: 3
- Issues abertas: 3

### Status

- `matched_exact_sku_stock_resolved`: 253
- `shopify_duplicate_sku_blocked`: 1
- `shopify_variant_tiny_missing`: 1
- `tiny_duplicate_exact_code_blocked`: 1

### Duplicidade Shopify bloqueada

- `1183C468301-1`

### Duplicidade Tiny bloqueada

- `U9060ZGE-11`

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `new-balance-9060-black-cement-black-cat-preto`: 2
- `onitsuka-tiger-mexico-66-sd-metallic-series-jade-cream-verde`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 2.325s

OK
20260609T215238Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
