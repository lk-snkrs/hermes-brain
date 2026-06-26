# Receipt — LK Stock Gate B.2 shard 70

Data/hora UTC: 20260610T014915Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard70_20260610T013827Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard70-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard70-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard70-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 179
- `availability_claim_allowed = 1`: 175
- Bloqueadas: 4
- Issues abertas: 4

### Status

- `matched_exact_sku_stock_resolved`: 175
- `shopify_duplicate_sku_blocked`: 3
- `tiny_duplicate_exact_code_blocked`: 1

### Duplicidade Shopify bloqueada

- `HV8547-001`
- `HV8547-600`
- `JQ1687`

### Duplicidade Tiny bloqueada

- `HV8547-700-14`

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `nike-moon-shoe-sp-jacquemus-alabaster-amarelo`: 1
- `tenis-adidas-tokyo-crew-white-floral-embroidery-branco`: 1
- `tenis-nike-moon-shoe-sp-jacquemus-off-noir-preto`: 1
- `tenis-nike-moon-shoe-sp-jacquemus-university-red-vermelho`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 3.375s

OK
20260610T014915Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
