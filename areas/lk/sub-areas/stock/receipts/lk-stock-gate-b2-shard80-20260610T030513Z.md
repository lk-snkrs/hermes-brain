# Receipt — LK Stock Gate B.2 shard 80

Data/hora UTC: 20260610T030513Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard80_20260610T030034Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard80-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard80-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard80-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 65
- `availability_claim_allowed = 1`: 58
- Bloqueadas: 7
- Issues abertas: 7

### Status

- `matched_exact_sku_stock_resolved`: 58
- `shopify_duplicate_sku_blocked`: 6
- `shopify_variant_tiny_missing`: 1

### Duplicidade Shopify bloqueada

- `Rep06`
- `Rep13`
- `Rep15`
- `Rep17`
- `Rep19`
- `Rep20`

### Duplicidade Tiny bloqueada

- Nenhuma

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `camiseta-represent-clo-patron-of-the-club-washed-grey-cinza`: 1
- `camiseta-represent-clo-revere-manor-aged-white-branco`: 1
- `camiseta-represent-clo-revere-manor-stained-black-preto`: 1
- `camiseta-represent-clo-shark-jaws-off-black-preto`: 1
- `camiseta-represent-clo-storms-in-heaven-black-preto`: 1
- `onitsuka-tiger-mexico-66-white`: 1
- `shorts-represent-clo-owners-club-flat-white-branco`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 5.108s

OK
20260610T030513Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
