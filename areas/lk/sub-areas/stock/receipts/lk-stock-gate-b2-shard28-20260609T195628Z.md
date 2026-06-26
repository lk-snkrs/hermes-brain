# Receipt — LK Stock Gate B.2 shard 28

Data/hora UTC: 20260609T195628Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard28_20260609T194015Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard28-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard28-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard28-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 276
- `availability_claim_allowed = 1`: 269
- Bloqueadas: 7
- Issues abertas: 7

### Status

- `matched_exact_sku_stock_resolved`: 269
- `shopify_duplicate_sku_blocked`: 5
- `tiny_duplicate_exact_code_blocked`: 2

### Duplicidade Shopify bloqueada

- `1183C102100`
- `183A872`
- `CD4487-100`
- `FN6040-400`
- `IH4823`

### Duplicidade Tiny bloqueada

- `183A872-9`
- `DC0774-161`

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `tenis-onitsuka-tiger-mexico-66-sd-kill-bill-amarelo`: 2
- `tenis-adidas-sl72-rs-cloud-white-core-black-spark-branco`: 1
- `tenis-air-jordan-1-high-og-sp-x-travis-scott-mocha`: 1
- `tenis-air-jordan-1-low-bordeaux-roxo`: 1
- `tenis-nike-dunk-sb-x-verdy-visty-azul`: 1
- `tenis-onitsuka-tiger-mexico-66-white-blue-branco`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 5.560s

OK
20260609T195628Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
