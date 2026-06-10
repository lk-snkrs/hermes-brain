# Receipt — LK Stock Gate B.2 shard 66

Data/hora UTC: 20260610T010917Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard66_20260610T010545Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard66-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard66-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard66-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 56
- `availability_claim_allowed = 1`: 56
- Bloqueadas: 0
- Issues abertas: 0

### Status

- `matched_exact_sku_stock_resolved`: 56

### Duplicidade Shopify bloqueada

- Nenhuma

### Duplicidade Tiny bloqueada

- Nenhuma

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- Nenhum

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 2.831s

OK
20260610T010917Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
