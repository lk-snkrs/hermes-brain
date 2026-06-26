# Receipt — LK Stock Gate B.2 shard 29

Data/hora UTC: 20260609T200552Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard29_20260609T195630Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard29-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard29-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard29-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 155
- `availability_claim_allowed = 1`: 153
- Bloqueadas: 2
- Issues abertas: 2

### Status

- `matched_exact_sku_stock_resolved`: 153
- `shopify_duplicate_sku_blocked`: 2

### Duplicidade Shopify bloqueada

- `HF8828100`
- `MR530PR`

### Duplicidade Tiny bloqueada

- Nenhuma

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `tenis-air-jordan-1-low-x-paris-saint-germain-sail-and-off-noir-preto`: 1
- `tenis-new-balance-530-x-salehe-bembury-prosperity-be-the-prize-verde`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 13.074s

OK
20260609T200552Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
