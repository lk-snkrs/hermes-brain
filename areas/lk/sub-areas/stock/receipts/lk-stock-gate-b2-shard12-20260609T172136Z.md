# Receipt — LK Stock Gate B.2 shard 12

Data/hora UTC: 20260609T172136Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard12_20260609T171247Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard12-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard12-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard12-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 132
- `availability_claim_allowed = 1`: 112
- Bloqueadas: 20
- Issues abertas: 20

### Status

- `matched_exact_sku_stock_resolved`: 112
- `shopify_variant_tiny_missing`: 12
- `matched_exact_sku_stock_missing_deposit`: 4
- `shopify_duplicate_sku_blocked`: 2
- `tiny_duplicate_exact_code_blocked`: 2

### Duplicidade Shopify bloqueada

- `DR2630100`
- `ID2529`

### Duplicidade Tiny bloqueada

- `553558030`
- `553558040-12`

### Depósito oficial ausente

- `DV1333100-99`
- `DV5464500-8`
- `DZ5485051-6`
- `ID2529-7`

### Top handles por bloqueios

- `air-jordan-1-low-black-medium-grey`: 3
- `air-jordan-1-low-light-smoke-grey`: 3
- `bad-bunny-x-adidas-campus-brown`: 3
- `air-jordan-1-high-og-washed-black`: 2
- `air-jordan-1-low-gs-se-concord`: 2
- `tenis-nike-sb-dunk-low-pro-iso-orange-label-court-purple-roxo`: 2
- `yeezy-boost-350-v2-bone`: 2
- `air-jordan-1-low-og-black-toe-2023`: 1
- `nike-x-nocta-x-cpfm-t-shirt-white`: 1
- `nike-x-off-white-short-sleeve-top-black`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 3.240s

OK
20260609T172136Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
