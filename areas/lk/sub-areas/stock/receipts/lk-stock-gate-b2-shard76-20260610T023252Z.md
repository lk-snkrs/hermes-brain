# Receipt — LK Stock Gate B.2 shard 76

Data/hora UTC: 20260610T023252Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard76_20260610T022755Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard76-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard76-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard76-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 80
- `availability_claim_allowed = 1`: 67
- Bloqueadas: 13
- Issues abertas: 13

### Status

- `matched_exact_sku_stock_resolved`: 67
- `shopify_duplicate_sku_blocked`: 11
- `shopify_variant_tiny_missing`: 2

### Duplicidade Shopify bloqueada

- `a0827u-1`
- `a0827u-10`
- `a0827u-11`
- `a0827u-2`
- `a0827u-3`
- `a0827u-4`
- `a0827u-5`
- `a0827u-6`
- `a0827u-7`
- `a0827u-8`
- `a0827u-9`

### Duplicidade Tiny bloqueada

- Nenhuma

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `slipper-alo-yoga-recovery-saddle-ivory-bege`: 12
- `tenis-alo-yoga-alo-sunset-sneaker-sandstone-bege`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 2.497s

OK
20260610T023252Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
