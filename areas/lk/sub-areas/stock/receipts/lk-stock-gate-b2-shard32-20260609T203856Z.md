# Receipt — LK Stock Gate B.2 shard 32

Data/hora UTC: 20260609T203856Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard32_20260609T203220Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard32-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard32-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard32-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 106
- `availability_claim_allowed = 1`: 98
- Bloqueadas: 8
- Issues abertas: 8

### Status

- `matched_exact_sku_stock_resolved`: 98
- `tiny_duplicate_exact_code_blocked`: 4
- `shopify_variant_tiny_missing`: 3
- `shopify_duplicate_sku_blocked`: 1

### Duplicidade Shopify bloqueada

- `CDGP2`

### Duplicidade Tiny bloqueada

- `471321-4`
- `CDGP1-5`
- `HQ2059-11`
- `IH3719`

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `camiseta-kaws-x-uniqlo-warhol-ut-graphic-branco`: 2
- `polo-comme-des-garcons-play-preto`: 2
- `tenis-adidas-yeezy-boost-350-v2-granite-marrom`: 2
- `polo-comme-des-garcons-play-branco`: 1
- `tenis-adidas-gazelle-indoor-x-clot-by-edison-chen-off-white-branco`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 6.053s

OK
20260609T203856Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
