# Receipt — LK Stock Gate B.2 shard 88

Data/hora UTC: 20260610T042954Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard88_20260610T041734Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard88-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard88-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard88-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 197
- `availability_claim_allowed = 1`: 159
- Bloqueadas: 38
- Issues abertas: 38

### Status

- `matched_exact_sku_stock_resolved`: 159
- `shopify_duplicate_sku_blocked`: 22
- `shopify_variant_tiny_missing`: 16

### Duplicidade Shopify bloqueada

- `1201A906-001-34`
- `1201A906-001-35`
- `1201A906-001-36`
- `1201A906-001-37`
- `1201A906-001-38`
- `1201A906-001-39`
- `1201A906-001-40`
- `1201A906-001-41`
- `1201A906-001-42`
- `1201A906-001-43`
- `1201A906-001-44`
- `FQ8138-600-34`
- `FQ8138-600-35`
- `FQ8138-600-36`
- `FQ8138-600-37`
- `FQ8138-600-38`
- `FQ8138-600-39`
- `FQ8138-600-40`
- `FQ8138-600-41`
- `FQ8138-600-42`
- `FQ8138-600-43`
- `FQ8138-600-44`

### Duplicidade Tiny bloqueada

- Nenhuma

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `tenis-asics-gel-1130-black-pure-silver-prata`: 12
- `tenis-jordan-4-retro-toro-bravo-2026-vermelho`: 12
- `tenis-adidas-ballerina-bad-bunny-flamboyan-vermelho`: 1
- `tenis-asics-gel-1130-white-pure-silver-prata`: 1
- `tenis-asics-gel-nyc-graphite-grey-black-preto`: 1
- `tenis-jordan-1-retro-high-og-sp-fragment-x-union-la-sport-royal`: 1
- `tenis-jordan-11-retro-low-university-blue-2026-azul`: 1
- `tenis-jordan-4-retro-lakers-roxo`: 1
- `tenis-jordan-5-retro-white-metallic-2026-metalizado`: 1
- `tenis-jordan-5-retro-wolf-grey-2026-cinza`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 3.299s

OK
20260610T042954Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
