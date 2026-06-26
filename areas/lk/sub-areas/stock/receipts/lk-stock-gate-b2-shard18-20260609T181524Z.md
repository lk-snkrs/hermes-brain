# Receipt — LK Stock Gate B.2 shard 18

Data/hora UTC: 20260609T181524Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard18_20260609T180712Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard18-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard18-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard18-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 117
- `availability_claim_allowed = 1`: 99
- Bloqueadas: 18
- Issues abertas: 18

### Status

- `matched_exact_sku_stock_resolved`: 99
- `shopify_variant_tiny_missing`: 10
- `shopify_duplicate_sku_blocked`: 4
- `matched_exact_sku_stock_missing_deposit`: 3
- `tiny_duplicate_exact_code_blocked`: 1

### Duplicidade Shopify bloqueada

- `CW1590-103`
- `DH6927111`
- `FJ3453-200`
- `IE1058`

### Duplicidade Tiny bloqueada

- `DZ5485-010`

### Depósito oficial ausente

- `FJ2260-001-2`
- `GY9473-2`
- `IF3219-12`

### Top handles por bloqueios

- `crocs-classic-clog-x-the-cars-lightning-mcqueen-vermelho`: 2
- `tenis-adidas-campus-00s-ambient-sky-azul`: 2
- `tenis-adidas-responce-cl-x-bad-bunny-wonder-branco`: 2
- `tenis-air-jordan-1-low-year-of-dragon-2024-vinho`: 2
- `tenis-nike-dunk-low-lx-brown-ostrich-marrom`: 2
- `tenis-nike-dunk-low-university-blue-azul`: 2
- `tenis-adidas-gazelle-indor-beam-pink-solar-red-rosa`: 1
- `tenis-adidas-yeezy-boost-350-v2-steel-grey-cinza`: 1
- `tenis-air-jordan-1-high-og-black-white-preto`: 1
- `tenis-air-jordan-1-low-eastside-golf-azul-marinho`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 13.109s

OK
20260609T181524Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
