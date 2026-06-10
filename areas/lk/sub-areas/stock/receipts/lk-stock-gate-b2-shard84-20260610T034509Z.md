# Receipt — LK Stock Gate B.2 shard 84

Data/hora UTC: 20260610T034509Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard84_20260610T033204Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard84-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard84-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard84-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 214
- `availability_claim_allowed = 1`: 198
- Bloqueadas: 16
- Issues abertas: 16

### Status

- `matched_exact_sku_stock_resolved`: 198
- `shopify_variant_tiny_missing`: 16

### Duplicidade Shopify bloqueada

- Nenhuma

### Duplicidade Tiny bloqueada

- Nenhuma

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `slide-nike-mind-001-geode-teal-verde`: 1
- `tenis-new-balance-530-beige-angora-creme-1069960456`: 1
- `tenis-nike-mind-002-thunder-blue-azul`: 1
- `tenis-nike-vomero-premium-volt-tint-sapphire-verde`: 1
- `tenis-onitsuka-tiger-mexico-66-sabot-black-black-preto`: 1
- `tenis-onitsuka-tiger-mexico-66-sabot-dark-brown-marrom`: 1
- `tenis-onitsuka-tiger-mexico-66-sabot-pure-silver-cream-cinza`: 1
- `tenis-onitsuka-tiger-x-versace-sakura-leather-loafers-brown-blue-marrom`: 1
- `tenis-onitsuka-tiger-x-versace-sakura-leather-loafers-brown-white-marrom`: 1
- `tenis-onitsuka-tiger-x-versace-tai-chi-sakura-metallic-sneakers-silver-gold-prateado`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 7.122s

OK
20260610T034509Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
