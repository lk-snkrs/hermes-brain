# Receipt — LK Stock Gate B.2 shard 85

Data/hora UTC: 20260610T035746Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard85_20260610T034511Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard85-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard85-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard85-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 208
- `availability_claim_allowed = 1`: 186
- Bloqueadas: 22
- Issues abertas: 22

### Status

- `matched_exact_sku_stock_resolved`: 186
- `shopify_variant_tiny_missing`: 15
- `shopify_duplicate_sku_blocked`: 7

### Duplicidade Shopify bloqueada

- `3ME106929791`
- `IH4000-35`
- `IH4000-36`
- `JR4790-34`
- `JR4790-37`
- `JR4790-39`
- `JR4790-40`

### Duplicidade Tiny bloqueada

- Nenhuma

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `adidas-wmns-tokyo-mj-core-black-cream-white-gold-metallic`: 3
- `tenis-adidas-tokyo-mary-jane-sandy-pink-earth-strata-rosa`: 3
- `tenis-adidas-tokyo-mary-jane-black-cream-white-gold-metallic-preto`: 2
- `slide-nike-mind-001-sail-bege`: 1
- `slide-nike-mind-001-white-speed-red-branco`: 1
- `tenis-adidas-badbo-1-0-rise-branco`: 1
- `tenis-adidas-taekwondo-mei-ballet-cream-white-branco`: 1
- `tenis-adidas-tokyo-mary-jane-cream-white-red-gold-metallic-creme`: 1
- `tenis-adidas-tokyo-mary-jane-crystal-sky-cream-white-azul`: 1
- `tenis-alo-yoga-alo-recovery-mode-sneaker-pink-wild-rose-rosa-copia`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 3.216s

OK
20260610T035746Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
