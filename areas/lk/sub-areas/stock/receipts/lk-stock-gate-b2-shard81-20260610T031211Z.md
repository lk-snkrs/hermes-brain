# Receipt — LK Stock Gate B.2 shard 81

Data/hora UTC: 20260610T031211Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard81_20260610T030515Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard81-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard81-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard81-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 111
- `availability_claim_allowed = 1`: 105
- Bloqueadas: 6
- Issues abertas: 6

### Status

- `matched_exact_sku_stock_resolved`: 105
- `shopify_variant_tiny_missing`: 5
- `shopify_duplicate_sku_blocked`: 1

### Duplicidade Shopify bloqueada

- `Rep01`

### Duplicidade Tiny bloqueada

- Nenhuma

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `alo-runner-sweet-pink-rosa`: 1
- `moletom-represent-clo-masking-tape-initial-cedar-marrom`: 1
- `tenis-nike-air-jordan-4-retro-black-cat-preto`: 1
- `tenis-nike-mind-002-black-hyper-crimson-preto`: 1
- `tenis-nike-mind-002-light-khaki-bege`: 1
- `tenis-nike-mind-002-light-smoke-grey-cinza`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 4.164s

OK
20260610T031211Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
