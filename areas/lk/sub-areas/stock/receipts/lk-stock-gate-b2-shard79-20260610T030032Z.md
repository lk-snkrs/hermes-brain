# Receipt — LK Stock Gate B.2 shard 79

Data/hora UTC: 20260610T030032Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard79_20260610T025155Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard79-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard79-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard79-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 140
- `availability_claim_allowed = 1`: 122
- Bloqueadas: 18
- Issues abertas: 18

### Status

- `matched_exact_sku_stock_resolved`: 122
- `shopify_duplicate_sku_blocked`: 11
- `shopify_variant_tiny_missing`: 6
- `tiny_duplicate_exact_code_blocked`: 1

### Duplicidade Shopify bloqueada

- `U204L86W-1`
- `U204L86W-10`
- `U204L86W-11`
- `U204L86W-2`
- `U204L86W-3`
- `U204L86W-4`
- `U204L86W-5`
- `U204L86W-6`
- `U204L86W-7`
- `U204L86W-8`
- `U204L86W-9`

### Duplicidade Tiny bloqueada

- `HQ4307-003-15`

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `tenis-new-balance-204l-grey-matter-shipyard-cinza`: 12
- `slide-nike-mind-001-light-smoke-grey-cinza`: 1
- `tenis-new-balance-204l-cortado-marrom`: 1
- `tenis-nike-air-rift-sail-bege`: 1
- `tenis-nike-x-skims-rift-mesh-archaeo-brown-marrom`: 1
- `tenis-on-running-cloudtilt-preto-e-branco`: 1
- `yeezy-boost-350-v2-earth-bege`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 18.445s

OK
20260610T030032Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
