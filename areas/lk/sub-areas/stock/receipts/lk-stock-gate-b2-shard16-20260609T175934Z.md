# Receipt — LK Stock Gate B.2 shard 16

Data/hora UTC: 20260609T175934Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard16_20260609T175015Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard16-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard16-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard16-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 135
- `availability_claim_allowed = 1`: 107
- Bloqueadas: 28
- Issues abertas: 28

### Status

- `matched_exact_sku_stock_resolved`: 107
- `shopify_variant_tiny_missing`: 13
- `shopify_duplicate_sku_blocked`: 11
- `matched_exact_sku_stock_missing_deposit`: 3
- `tiny_duplicate_exact_code_blocked`: 1

### Duplicidade Shopify bloqueada

- `CQ9446400`
- `CU1727100`
- `DC0774113`
- `DJ9955100`
- `DZ5365601`
- `DZ6333083`
- `FB9907102`
- `FD8780116`
- `FQ0997-389`
- `GY0042`
- `HQ8707`

### Duplicidade Tiny bloqueada

- `553558053-13`

### Depósito oficial ausente

- `553558053-37`
- `DV0426-012-9`
- `DZ5485400-3`

### Top handles por bloqueios

- `air-jordan-1-low-vintage-grey`: 4
- `air-jordan-1-low-gs-fierce-pink`: 3
- `air-jordan-1-low-gs-rabbit`: 2
- `air-jordan-1-low-se-sky-j-mauve`: 2
- `jersey-off-white-x-nike-allover-print-kelly-green-verde`: 2
- `nike-dunk-low-se-animal`: 2
- `tenis-air-jordan-1-high-og-unc-toe-azul`: 2
- `wmns-air-jordan-1-low-se-light-steel-grey`: 2
- `air-jordan-1-low-royal-toe`: 1
- `air-jordan-1-mid-gs-fierce-pink`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 5.565s

OK
20260609T175934Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
