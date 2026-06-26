# Receipt — LK Stock Gate B.2 shard 63

Data/hora UTC: 20260610T010222Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard63_20260610T004853Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard63-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard63-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard63-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 213
- `availability_claim_allowed = 1`: 212
- Bloqueadas: 1
- Issues abertas: 1

### Status

- `matched_exact_sku_stock_resolved`: 212
- `shopify_duplicate_sku_blocked`: 1

### Duplicidade Shopify bloqueada

- `AIME11`

### Duplicidade Tiny bloqueada

- Nenhuma

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `bone-5-panel-aime-leon-dore-unisphere-azul`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 12.309s

OK
20260610T010222Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
