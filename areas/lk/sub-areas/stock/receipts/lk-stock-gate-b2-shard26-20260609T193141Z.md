# Receipt — LK Stock Gate B.2 shard 26

Data/hora UTC: 20260609T193141Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard26_20260609T192158Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard26-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard26-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard26-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 167
- `availability_claim_allowed = 1`: 163
- Bloqueadas: 4
- Issues abertas: 4

### Status

- `matched_exact_sku_stock_resolved`: 163
- `tiny_duplicate_exact_code_blocked`: 2
- `shopify_duplicate_sku_blocked`: 1
- `shopify_variant_tiny_missing`: 1

### Duplicidade Shopify bloqueada

- `1183C102100`

### Duplicidade Tiny bloqueada

- `553560-141-6`
- `IF9735-9`

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `tenis-adidas-gazelle-x-bad-bunny-core-white-bege`: 2
- `tenis-air-jordan-1-low-midnight-navy-wolf-grey-azul-marinho`: 1
- `tenis-onitsuka-tiger-mexico-66-white-blue-branco`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 4.908s

OK
20260609T193141Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
