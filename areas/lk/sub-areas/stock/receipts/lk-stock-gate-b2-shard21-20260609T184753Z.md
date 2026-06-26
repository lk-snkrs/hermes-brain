# Receipt — LK Stock Gate B.2 shard 21

Data/hora UTC: 20260609T184753Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard21_20260609T183758Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard21-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard21-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard21-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 159
- `availability_claim_allowed = 1`: 145
- Bloqueadas: 14
- Issues abertas: 14

### Status

- `matched_exact_sku_stock_resolved`: 145
- `shopify_variant_tiny_missing`: 8
- `matched_exact_sku_stock_missing_deposit`: 2
- `shopify_duplicate_sku_blocked`: 2
- `tiny_duplicate_exact_code_blocked`: 2

### Duplicidade Shopify bloqueada

- `ID2056`
- `U9060VNG`

### Duplicidade Tiny bloqueada

- `FZ3775-133`
- `ID2534-11`

### Depósito oficial ausente

- `FN0344-001-3`
- `HF6061-400-7`

### Top handles por bloqueios

- `pre-venda-tenis-korn-x-adidas-campus-2-0-carbon-cinza`: 3
- `pre-venda-camiseta-manga-longa-adidas-x-korn`: 2
- `tenis-air-jordan-3-retro-x-j-balvin-rio-preto`: 2
- `tenis-bad-bunny-x-adidas-campus-the-last-campus-marrom`: 2
- `tenis-nike-sb-dunk-low-x-futura-skateboard-bleached-aqua-azul`: 2
- `tenis-adidas-samba-og-night-navy-gum-azul-marinho`: 1
- `tenis-new-balance-9060-nori-verde`: 1
- `tenis-nike-dunk-low-give-her-flowers-branco`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 5.149s

OK
20260609T184753Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
