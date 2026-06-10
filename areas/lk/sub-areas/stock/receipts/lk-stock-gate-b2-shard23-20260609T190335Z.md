# Receipt — LK Stock Gate B.2 shard 23

Data/hora UTC: 20260609T190335Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard23_20260609T185609Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard23-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard23-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard23-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 126
- `availability_claim_allowed = 1`: 122
- Bloqueadas: 4
- Issues abertas: 4

### Status

- `matched_exact_sku_stock_resolved`: 122
- `shopify_duplicate_sku_blocked`: 4

### Duplicidade Shopify bloqueada

- `BQ6472303`
- `IG5349`
- `U9060EED`
- `U9060SFB`

### Duplicidade Tiny bloqueada

- Nenhuma

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `air-jordan-1-mid-aqua-blue-tint`: 1
- `tenis-new-balance-9060-chrome-blue-azul`: 1
- `tenis-new-balance-9060-pink-granite-silver-metallic-silver-cinza`: 1
- `yeezy-foam-runner-carbon`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 3.890s

OK
20260609T190335Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
