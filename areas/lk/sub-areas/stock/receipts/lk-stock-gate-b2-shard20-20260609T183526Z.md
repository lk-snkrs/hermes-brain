# Receipt — LK Stock Gate B.2 shard 20

Data/hora UTC: 20260609T183526Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard20_20260609T182446Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard20-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard20-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard20-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 122
- `availability_claim_allowed = 1`: 103
- Bloqueadas: 19
- Issues abertas: 19

### Status

- `matched_exact_sku_stock_resolved`: 103
- `shopify_variant_tiny_missing`: 12
- `shopify_duplicate_sku_blocked`: 5
- `matched_exact_sku_stock_missing_deposit`: 2

### Duplicidade Shopify bloqueada

- `DH6927161`
- `DH7534200`
- `DN1555-200`
- `G1379`
- `ID0444`

### Duplicidade Tiny bloqueada

- Nenhuma

### Depósito oficial ausente

- `DD1503-603-5`
- `SF2BSP5-4`

### Top handles por bloqueios

- `camiseta-sufgang-basic-pack-5-8-verde`: 2
- `tenis-air-jordan-1-high-og-green-glow-verde`: 2
- `tenis-air-jordan-1-low-se-silver-metallic-cinza`: 2
- `tenis-air-jordan-4-retro-military-blue-branco`: 2
- `tenis-nike-dunk-low-light-carbon-cinza`: 2
- `nike-sb-dunk-low-prm-paisley-brown`: 1
- `tenis-adidas-samba-cardboard-marrom`: 1
- `tenis-adidas-samba-og-off-white-oat-violet-tone-branco`: 1
- `tenis-adidas-sambae-x-kseniaschnaiderc-black-multicolor-colorido`: 1
- `tenis-air-jordan-1-low-light-green-verde`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 7.385s

OK
20260609T183526Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
