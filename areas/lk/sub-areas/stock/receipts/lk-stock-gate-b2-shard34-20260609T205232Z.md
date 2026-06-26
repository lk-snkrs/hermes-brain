# Receipt — LK Stock Gate B.2 shard 34

Data/hora UTC: 20260609T205232Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard34_20260609T204712Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard34-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard34-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard34-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 88
- `availability_claim_allowed = 1`: 81
- Bloqueadas: 7
- Issues abertas: 7

### Status

- `matched_exact_sku_stock_resolved`: 81
- `shopify_duplicate_sku_blocked`: 5
- `shopify_variant_tiny_missing`: 1
- `tiny_duplicate_exact_code_blocked`: 1

### Duplicidade Shopify bloqueada

- `DZ2795-601`
- `IH3261`
- `MR530EMA`
- `MR530LG`
- `U9060EEC`

### Duplicidade Tiny bloqueada

- `MR530EMA-4`

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `tenis-new-balance-530-silver-white-branco`: 2
- `oculos-de-sol-balenciaga-bb0133s-001-preto`: 1
- `tenis-adidas-samba-x-wales-bonner-wonder-white-marrom`: 1
- `tenis-new-balance-530-grey-matter-silver-metallic-cinza`: 1
- `tenis-new-balance-9060-olivine-verde`: 1
- `tenis-nike-cortez-picante-red-vermelho`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 3.638s

OK
20260609T205232Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
