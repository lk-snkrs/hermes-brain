# Receipt — LK Stock Gate B.2 shard 38

Data/hora UTC: 20260609T211812Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard38_20260609T211202Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard38-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard38-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard38-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 98
- `availability_claim_allowed = 1`: 93
- Bloqueadas: 5
- Issues abertas: 5

### Status

- `matched_exact_sku_stock_resolved`: 93
- `shopify_duplicate_sku_blocked`: 2
- `tiny_duplicate_exact_code_blocked`: 2
- `shopify_variant_tiny_missing`: 1

### Duplicidade Shopify bloqueada

- `ST33`
- `ST34`

### Duplicidade Tiny bloqueada

- `AX-T801-051-2`
- `U9060LBC-7`

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `tenis-new-balance-9060-rose-sugar-ice-wine-rosa`: 2
- `camisa-manga-curta-boxy-saint-studio-egipcio-listrada-marinho`: 1
- `camiseta-boxy-saint-studio-supima-preto`: 1
- `camiseta-comme-des-garcons-emblem-rhinestone-white-red-branco`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 1.925s

OK
20260609T211812Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
