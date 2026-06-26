# Receipt — LK Stock Gate B.2 shard 11

Data/hora UTC: 2026-06-09T17:04:16Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard11_20260609T165652Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard11-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard11-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard11-summary-20260609.json`

## Prefixes executados

- `DD1391601`
- `DH1319200`
- `DQ8422001`
- `DV0982006`
- `GW1934`
- `HP7870`
- `ID4126`
- `ID4133`
- `DN3706401`
- `DM7866001`
- `DM0807600`
- `DM0807400`
- `DV5464001`
- `CZ4776101`
- `HQ7045`
- `starfish`
- `553558144-34`
- `ig1025`
- `AirJordan1ElevateLowGuavaIce`
- `DC0774042`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 90
- `availability_claim_allowed = 1`: 64
- Bloqueadas: 26
- Issues abertas: 26

### Status

- `matched_exact_sku_stock_resolved`: 64
- `shopify_duplicate_sku_blocked`: 12
- `shopify_variant_tiny_missing`: 9
- `matched_exact_sku_stock_missing_deposit`: 3
- `tiny_duplicate_exact_code_blocked`: 2

### Duplicidade Shopify bloqueada

- `DC0774042`
- `DD1391601`
- `DH1319200`
- `DM0807400`
- `DM0807600`
- `DM7866001`
- `DN3706401`
- `DV0982006`
- `DV5464001`
- `HP7870`
- `ID4126`
- `IG1025`

### Duplicidade Tiny bloqueada

- `CZ4776101-1`
- `HQ7045-8`

### Depósito oficial ausente

- `DM7866001-1`
- `HP7870-6`
- `ID4133-7`

### Top handles por bloqueios

- `yeezy-350-v2-carbon-beluga`: 4
- `travis-scott-x-air-jordan-1-low-og-sp-black-phantom`: 3
- `air-jordan-1-low-multi-color-royal-toe`: 2
- `air-jordan-1-low-unc-2021`: 2
- `yeezy-boost-350-v2-slate`: 2
- `yeezy-slide-azure`: 2

## Verificação

Comando:

```bash
python3 -m unittest discover -s areas/lk/sub-areas/stock/evaluation -p 'test_*.py'
```

Resultado:

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 5.372s

OK
20260609T170416Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
