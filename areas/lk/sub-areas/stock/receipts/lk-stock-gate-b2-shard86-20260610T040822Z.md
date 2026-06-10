# Receipt — LK Stock Gate B.2 shard 86

Data/hora UTC: 20260610T040822Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard86_20260610T035748Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard86-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard86-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard86-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 167
- `availability_claim_allowed = 1`: 150
- Bloqueadas: 17
- Issues abertas: 17

### Status

- `matched_exact_sku_stock_resolved`: 150
- `shopify_variant_tiny_missing`: 17

### Duplicidade Shopify bloqueada

- Nenhuma

### Duplicidade Tiny bloqueada

- Nenhuma

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `slide-nike-mind-001-blackened-blue-azul`: 1
- `slide-nike-mind-001-mineral-slate-verde`: 1
- `slide-nike-mind-001-pearl-pink-rosa`: 1
- `tenis-new-balance-1906l-black-suede-preto`: 1
- `tenis-nike-mind-002-grey-football-grey-cinza`: 1
- `tenis-nike-shox-tl-black-cave-stone-preto`: 1
- `tenis-nike-shox-tl-black-dynamic-yellow-preto`: 1
- `tenis-nike-shox-tl-blue-tint-orange-azul`: 1
- `tenis-nike-shox-tl-orewood-brown-cave-stone-bege`: 1
- `tenis-nike-shox-tl-pumice-night-maroon-cinza`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 1.735s

OK
20260610T040822Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
