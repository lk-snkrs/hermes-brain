# Receipt — LK Stock Gate B.2 shard 41

Data/hora UTC: 20260609T213737Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard41_20260609T213306Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard41-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard41-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard41-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 73
- `availability_claim_allowed = 1`: 70
- Bloqueadas: 3
- Issues abertas: 3

### Status

- `matched_exact_sku_stock_resolved`: 70
- `shopify_variant_tiny_missing`: 2
- `tiny_duplicate_exact_code_blocked`: 1

### Duplicidade Shopify bloqueada

- Nenhuma

### Duplicidade Tiny bloqueada

- `U9060ZGF-8`

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `tenis-new-balance-9060-sea-salt-raincloud-cinza`: 2
- `tenis-new-balance-9060-kids-rose-sugar-ice-wine-rosa`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 2.263s

OK
20260609T213737Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
