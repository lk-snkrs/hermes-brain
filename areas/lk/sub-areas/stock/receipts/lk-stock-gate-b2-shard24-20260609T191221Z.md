# Receipt — LK Stock Gate B.2 shard 24

Data/hora UTC: 20260609T191221Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard24_20260609T190336Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard24-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard24-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard24-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 149
- `availability_claim_allowed = 1`: 144
- Bloqueadas: 5
- Issues abertas: 5

### Status

- `matched_exact_sku_stock_resolved`: 144
- `shopify_duplicate_sku_blocked`: 2
- `tiny_duplicate_exact_code_blocked`: 2
- `shopify_variant_tiny_missing`: 1

### Duplicidade Shopify bloqueada

- `FQ2947-100-1`
- `IH3144`

### Duplicidade Tiny bloqueada

- `1183C102 751-7`
- `M1000AC1-12`

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `tenis-new-balance-1000-x-aime-leon-dore-sea-salt-concrete-branco`: 2
- `air-jordan-1-high-og-denim`: 1
- `tenis-adidas-gazelle-x-clot-by-edison-chen-halo-ivory-bege`: 1
- `tenis-onitsuka-tiger-mexico-66-kill-bill-amarelo`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 3.549s

OK
20260609T191221Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
