# Receipt — LK Stock Gate B.2 shard 27

Data/hora UTC: 20260609T194013Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard27_20260609T193143Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard27-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard27-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard27-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 146
- `availability_claim_allowed = 1`: 144
- Bloqueadas: 2
- Issues abertas: 2

### Status

- `matched_exact_sku_stock_resolved`: 144
- `shopify_duplicate_sku_blocked`: 1
- `tiny_duplicate_exact_code_blocked`: 1

### Duplicidade Shopify bloqueada

- `DM0950-104`

### Duplicidade Tiny bloqueada

- `IH4769`

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `tenis-adidas-gazelle-indoor-alumina-black-bege`: 1
- `tenis-nike-cortez-white-laser-fuchsia-branco`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 4.187s

OK
20260609T194013Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
