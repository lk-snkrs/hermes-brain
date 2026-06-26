# Receipt — LK Stock Gate B.2 shard 15

Data/hora UTC: 20260609T175015Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard15_20260609T174017Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard15-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard15-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard15-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 138
- `availability_claim_allowed = 1`: 108
- Bloqueadas: 30
- Issues abertas: 30

### Status

- `matched_exact_sku_stock_resolved`: 108
- `shopify_variant_tiny_missing`: 18
- `shopify_duplicate_sku_blocked`: 8
- `matched_exact_sku_stock_missing_deposit`: 3
- `tiny_duplicate_exact_code_blocked`: 1

### Duplicidade Shopify bloqueada

- `553558065`
- `553558065-1`
- `553558615`
- `CD0461002`
- `CV1659001`
- `CZ5127001`
- `DO9404400`
- `DV7210001`

### Duplicidade Tiny bloqueada

- `dc0774-800`

### Depósito oficial ausente

- `FD1437020-2`
- `FD2562400-1`
- `FZ8319300-2`

### Top handles por bloqueios

- `air-jordan-1-high-gs-palomino`: 3
- `nike-dunk-low-setsubun`: 3
- `air-jordan-1-mid-se-red-stardust-white`: 2
- `april-skateboards-x-nike-sb-dunk-low-turbo-green`: 2
- `jarritos-x-nike-sb-dunk-low`: 2
- `run-the-jewels-x-dunk-low-sb-4-20`: 2
- `the-powerpuff-girls-x-nike-sb-dunk-low-blossom`: 2
- `the-powerpuff-girls-x-nike-sb-dunk-low-bubbles`: 2
- `the-powerpuff-girls-x-nike-sb-dunk-low-buttercup-1`: 2
- `air-jordan-1-high-seafoam`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 12.011s

OK
20260609T175015Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
