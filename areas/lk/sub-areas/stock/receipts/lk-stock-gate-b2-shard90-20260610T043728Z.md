# Receipt — LK Stock Gate B.2 shard 90

Data/hora UTC: 20260610T043728Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard90_20260610T043437Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard90-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard90-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard90-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 7
- Linhas persistidas: 37
- `availability_claim_allowed = 1`: 26
- Bloqueadas: 11
- Issues abertas: 11

### Status

- `matched_exact_sku_stock_resolved`: 26
- `shopify_variant_tiny_missing`: 10
- `shopify_duplicate_sku_blocked`: 1

### Duplicidade Shopify bloqueada

- `IQ7604-101`

### Duplicidade Tiny bloqueada

- Nenhuma

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `tenis-new-balance-9060-grey-day-kids-td-cinza`: 7
- `tenis-air-jordan-4-og-sp-x-nigel-sylvester-brick-after-brick-branco`: 1
- `tenis-nike-air-jordan-1-retro-low-og-howard-university-vermelho`: 1
- `tenis-nike-air-jordan-1-retro-low-og-sp-travis-scott-sail-tropical-pink-rosa`: 1
- `tenis-nike-air-jordan-1-retro-low-og-sp-travis-scott-shy-pink-bege`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 3.230s

OK
20260610T043728Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
