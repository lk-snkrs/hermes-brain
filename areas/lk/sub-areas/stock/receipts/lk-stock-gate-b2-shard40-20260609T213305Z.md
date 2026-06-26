# Receipt — LK Stock Gate B.2 shard 40

Data/hora UTC: 20260609T213305Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard40_20260609T212914Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard40-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard40-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard40-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 51
- `availability_claim_allowed = 1`: 48
- Bloqueadas: 3
- Issues abertas: 3

### Status

- `matched_exact_sku_stock_resolved`: 48
- `shopify_duplicate_sku_blocked`: 3

### Duplicidade Shopify bloqueada

- `LIP`
- `LIP5`
- `LIPCASE-11`

### Duplicidade Tiny bloqueada

- Nenhuma

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `lip-case-rhode-by-hailey-bieber`: 1
- `the-peptide-lip-tints-rhode-limited-edition-shade-dourado`: 1
- `the-peptide-lip-tints-rhode-multicolor`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 3.930s

OK
20260609T213305Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
