# Receipt — LK Stock Gate B.2 shard 19

Data/hora UTC: 20260609T182446Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard19_20260609T181524Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard19-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard19-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard19-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 130
- `availability_claim_allowed = 1`: 105
- Bloqueadas: 25
- Issues abertas: 25

### Status

- `matched_exact_sku_stock_resolved`: 105
- `shopify_variant_tiny_missing`: 12
- `shopify_duplicate_sku_blocked`: 7
- `matched_exact_sku_stock_missing_deposit`: 3
- `tiny_duplicate_exact_code_blocked`: 3

### Duplicidade Shopify bloqueada

- `DJ6188002`
- `IG5929-1`
- `IG5929-3`
- `IG5929-5`
- `MR530RD`
- `U9060GCB`
- `U9060GRY`

### Duplicidade Tiny bloqueada

- `DJ6188002-34-1`
- `ID0477-7`
- `IG5929-7`

### Depósito oficial ausente

- `AQ9129-170-3`
- `FN5214-141-7`
- `ID0478-6`

### Top handles por bloqueios

- `tenis-adidas-gazelle-indoor-collegiate-green-verde`: 5
- `tenis-adidas-samba-og-maroon-cream-white-vinho`: 3
- `tenis-adidas-sambae-cloud-white-branco`: 2
- `tenis-air-jordan-4-retro-metallic-gold-branco`: 2
- `tenis-nike-dunk-low-concord-roxo`: 2
- `tenis-nike-sb-dunk-low-x-rayssa-leal-bege`: 2
- `nike-dunk-low-black-masculino`: 1
- `nike-dunk-low-black-panda`: 1
- `tenis-adidas-handball-spezial-preloved-green-verde`: 1
- `tenis-adidas-samba-og-cream-white-core-black-bege`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 10.618s

OK
20260609T182446Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
