# Receipt — LK Stock Gate B.2 shard 49

Data/hora UTC: 20260609T225940Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard49_20260609T224901Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard49-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard49-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard49-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 184
- `availability_claim_allowed = 1`: 181
- Bloqueadas: 3
- Issues abertas: 3

### Status

- `matched_exact_sku_stock_resolved`: 181
- `shopify_duplicate_sku_blocked`: 1
- `shopify_variant_tiny_missing`: 1
- `tiny_duplicate_exact_code_blocked`: 1

### Duplicidade Shopify bloqueada

- `1183C468.300`

### Duplicidade Tiny bloqueada

- `HF3058-300`

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `nike-dunk-sb-dunk-low-qs-bhm-rodeo-verde`: 1
- `rhode-pocket-blush`: 1
- `tenis-onitsuka-tiger-mexico-66-sd-metallic-series-pale-mint-cream-azul`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 1.619s

OK
20260609T225940Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
