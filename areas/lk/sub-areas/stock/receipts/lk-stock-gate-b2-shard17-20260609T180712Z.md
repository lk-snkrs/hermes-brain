# Receipt — LK Stock Gate B.2 shard 17

Data/hora UTC: 20260609T180712Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard17_20260609T175934Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard17-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard17-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard17-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 104
- `availability_claim_allowed = 1`: 75
- Bloqueadas: 29
- Issues abertas: 29

### Status

- `matched_exact_sku_stock_resolved`: 75
- `shopify_variant_tiny_missing`: 15
- `shopify_duplicate_sku_blocked`: 8
- `tiny_duplicate_exact_code_blocked`: 4
- `matched_exact_sku_stock_missing_deposit`: 2

### Duplicidade Shopify bloqueada

- `BY1604`
- `DC0774102`
- `DR6970071`
- `EF290523`
- `FJ3445001`
- `IF9734`
- `U9060EEB`
- `VN0009QC6BT`

### Duplicidade Tiny bloqueada

- `DX1193200`
- `FQ9112100-8`
- `MR530SG-7`
- `MR530SG-8`

### Depósito oficial ausente

- `FB9109102-1`
- `IF9734-5`

### Top handles por bloqueios

- `new-balance-530-white-natural-indigo-1`: 5
- `tenis-new-balance-9060-moonrock-linen-dark-artic-greycinza`: 3
- `yeezy-boost-350-v2-oreo`: 3
- `tenis-adidas-gazelle-indoor-x-bad-bunny-san-juan-azul`: 2
- `tenis-air-jordan-1-low-se-gs-glitter-swoosh-branco-1`: 2
- `tenis-air-jordan-4-bred-reimagined-preto`: 2
- `tenis-jordan-1-low-dune-red-vermelho`: 2
- `tenis-nike-dunk-low-x-off-white-lot-23-cinza`: 2
- `nike-air-force-1-flax`: 1
- `nike-dunk-low-gs-laser-fuchsia`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 4.919s

OK
20260609T180712Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
