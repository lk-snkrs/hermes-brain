# Receipt — LK Stock Gate B.2 shard 73

Data/hora UTC: 20260610T021923Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard73_20260610T020633Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard73-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard73-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard73-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 220
- `availability_claim_allowed = 1`: 216
- Bloqueadas: 4
- Issues abertas: 4

### Status

- `matched_exact_sku_stock_resolved`: 216
- `shopify_variant_tiny_missing`: 2
- `tiny_duplicate_exact_code_blocked`: 2

### Duplicidade Shopify bloqueada

- Nenhuma

### Duplicidade Tiny bloqueada

- `1183C123.251-1`
- `1183C123.251-2`

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `tenis-onitsuka-tiger-mexico-66-sabot-oatmeal-habanero-bege`: 3
- `tenis-onitsuka-tiger-mexico-66-sabot-beige-green-bege`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 5.168s

OK
20260610T021923Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
