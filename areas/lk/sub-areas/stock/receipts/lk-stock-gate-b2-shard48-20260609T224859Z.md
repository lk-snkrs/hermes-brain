# Receipt — LK Stock Gate B.2 shard 48

Data/hora UTC: 20260609T224859Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard48_20260609T224019Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard48-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard48-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard48-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 154
- `availability_claim_allowed = 1`: 151
- Bloqueadas: 3
- Issues abertas: 3

### Status

- `matched_exact_sku_stock_resolved`: 151
- `tiny_duplicate_exact_code_blocked`: 2
- `shopify_duplicate_sku_blocked`: 1

### Duplicidade Shopify bloqueada

- `U9060EEG`

### Duplicidade Tiny bloqueada

- `1183A353-127-9`
- `1183B566.201`

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `tenis-new-balance-9060-driftwood-castlerock-marrom`: 1
- `tenis-onitsuka-tiger-gsm-cream-black-gum-off-white`: 1
- `tenis-onitsuka-tiger-mexico-66-gold-white-dourado`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 2.346s

OK
20260609T224859Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
