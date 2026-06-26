# Receipt — LK Stock Gate B.2 shard 87

Data/hora UTC: 20260610T041732Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard87_20260610T040824Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard87-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard87-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard87-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 150
- `availability_claim_allowed = 1`: 131
- Bloqueadas: 19
- Issues abertas: 19

### Status

- `matched_exact_sku_stock_resolved`: 131
- `shopify_duplicate_sku_blocked`: 14
- `shopify_variant_tiny_missing`: 5

### Duplicidade Shopify bloqueada

- `1201A933-100-34`
- `1201A933-100-35`
- `1201A933-100-36`
- `1201A933-100-37`
- `1201A933-100-38`
- `1201A933-100-39`
- `1201A933-100-40`
- `1201A933-100-41`
- `1201A933-100-42`
- `1201A933-100-43`
- `1201A933-100-44`
- `NP20`
- `ST4-1`
- `ST5-1`

### Duplicidade Tiny bloqueada

- Nenhuma

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `tenis-asics-gel-1130-white-black-silver-prata`: 12
- `bolsa-minimal-saint-studio-cacto-caramelo`: 1
- `bolsa-minimal-saint-studio-cacto-off-white`: 1
- `camiseta-fear-of-god-essentials-varsity-90s-short-sleeve-tee-cinza`: 1
- `moletom-nude-project-cult-hoodie-black-beige-preto`: 1
- `tenis-asics-gel-1130-white-clay-canyon-branco`: 1
- `tenis-nike-air-jordan-1-low-se-repaired-denim-swoosh-azul`: 1
- `tenis-on-running-x-kith-on-k-tech-2-spirulina-barley-verde`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 2.274s

OK
20260610T041732Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
