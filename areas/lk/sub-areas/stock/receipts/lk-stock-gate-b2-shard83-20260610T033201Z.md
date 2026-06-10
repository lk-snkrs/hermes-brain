# Receipt — LK Stock Gate B.2 shard 83

Data/hora UTC: 20260610T033201Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard83_20260610T032613Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard83-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard83-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard83-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 91
- `availability_claim_allowed = 1`: 85
- Bloqueadas: 6
- Issues abertas: 6

### Status

- `matched_exact_sku_stock_resolved`: 85
- `shopify_variant_tiny_missing`: 6

### Duplicidade Shopify bloqueada

- Nenhuma

### Duplicidade Tiny bloqueada

- Nenhuma

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `tenis-new-balance-204l-lone-star-grey-cinza`: 1
- `tenis-nike-air-jordan-1-low-og-chinese-new-year-2026-cinza`: 1
- `tenis-nike-air-max-90-x-patta-sp-cyber-branco`: 1
- `tenis-nike-air-max-90-x-patta-sp-sapphire-azul-branco`: 1
- `tenis-nike-x-tom-sachs-mars-yard-3-0-bege`: 1
- `tenis-onitsuka-tiger-tokuten-charcoal-birch-cinza`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 7.582s

OK
20260610T033201Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
