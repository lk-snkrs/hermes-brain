# Receipt — LK Stock Gate B.2 shard 25

Data/hora UTC: 20260609T192156Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard25_20260609T191222Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard25-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard25-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard25-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 165
- `availability_claim_allowed = 1`: 161
- Bloqueadas: 4
- Issues abertas: 4

### Status

- `matched_exact_sku_stock_resolved`: 161
- `tiny_duplicate_exact_code_blocked`: 2
- `shopify_duplicate_sku_blocked`: 1
- `shopify_variant_tiny_missing`: 1

### Duplicidade Shopify bloqueada

- `U9060NV-1`

### Duplicidade Tiny bloqueada

- `DM4044-105`
- `U9060ECA-14`

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `tenis-new-balance-9060-sea-salt-concrete-branco`: 2
- `tenis-new-balance-9060-eclipse-azul-marinho`: 1
- `tenis-nike-cortez-white-black-branco`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 4.475s

OK
20260609T192156Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
