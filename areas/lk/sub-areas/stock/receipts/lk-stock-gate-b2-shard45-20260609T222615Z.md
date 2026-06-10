# Receipt — LK Stock Gate B.2 shard 45

Data/hora UTC: 20260609T222615Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard45_20260609T221306Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard45-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard45-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard45-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 226
- `availability_claim_allowed = 1`: 225
- Bloqueadas: 1
- Issues abertas: 1

### Status

- `matched_exact_sku_stock_resolved`: 225
- `shopify_variant_tiny_missing`: 1

### Duplicidade Shopify bloqueada

- Nenhuma

### Duplicidade Tiny bloqueada

- Nenhuma

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `yuto-horigome-x-dunk-low-sb-matcha`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 2.150s

OK
20260609T222615Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
