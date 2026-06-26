# Receipt — LK Stock Gate B.2 shard 56

Data/hora UTC: 20260610T000412Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard56_20260609T235843Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard56-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard56-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard56-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 84
- `availability_claim_allowed = 1`: 69
- Bloqueadas: 15
- Issues abertas: 15

### Status

- `matched_exact_sku_stock_resolved`: 69
- `shopify_duplicate_sku_blocked`: 11
- `shopify_variant_tiny_missing`: 3
- `tiny_duplicate_exact_code_blocked`: 1

### Duplicidade Shopify bloqueada

- `FN0432-100`
- `FZ8117100`
- `dc0774-202`
- `dz5485-402`
- `fv5029-100`
- `fz8117-102`
- `fz8117-204`
- `hm9208-001`
- `m2002rda`
- `m2002rdb`
- `u1906lbn`

### Duplicidade Tiny bloqueada

- `u1906lbn11`

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `tenis-new-balance-1906l-preto-couro-mesh-casual`: 2
- `tenis-air-jordan-1-low-archaeo-brown-nike-casual`: 1
- `tenis-air-jordan-1-retro-high-og-unc-reimagined-nike-esportivo-couro`: 1
- `tenis-air-jordan-1-retro-low-og-sp-trophy-room-rookie-card-away`: 1
- `tenis-air-jordan-4-retro-og-nike-white-cement-couro`: 1
- `tenis-jordan-jumpman-jack-tr-travis-scott-bright-cactus-couro-lona`: 1
- `tenis-new-balance-1906l-rich-oak-suede-camurca-slip-on`: 1
- `tenis-new-balance-1906l-silver-shadow-grey-mesh-sintetico-slip-on`: 1
- `tenis-new-balance-2002r-protection-pack-phantom-cinza-camurca-mesh`: 1
- `tenis-new-balance-2002r-protection-pack-rain-cloud-suede-mesh`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 4.280s

OK
20260610T000412Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
