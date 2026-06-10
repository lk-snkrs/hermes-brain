# Receipt — LK Stock Gate B.2 shard 13

Data/hora UTC: 20260609T173116Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard13_20260609T172136Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard13-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard13-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard13-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 134
- `availability_claim_allowed = 1`: 100
- Bloqueadas: 34
- Issues abertas: 34

### Status

- `matched_exact_sku_stock_resolved`: 100
- `shopify_variant_tiny_missing`: 18
- `shopify_duplicate_sku_blocked`: 9
- `matched_exact_sku_stock_missing_deposit`: 4
- `tiny_duplicate_exact_code_blocked`: 3

### Duplicidade Shopify bloqueada

- `B75807`
- `CP9654`
- `DH7695600`
- `DJ9955800`
- `DR6496116`
- `DV0833400`
- `DZ7292200`
- `FZ5823`
- `HQ6638`

### Duplicidade Tiny bloqueada

- `FD2627200-9`
- `FN7645133-9`
- `FQ1180001-6`

### Depósito oficial ausente

- `01424-002-4`
- `B75807-6`
- `FB2216200-5`
- `FN7645133-7`

### Top handles por bloqueios

- `albino-preto-x-nike-sb-dunk-low-pearl-white`: 4
- `nike-dunk-low-se-australia`: 4
- `yuto-horigome-x-nike-sb-dunk-low`: 4
- `air-jordan-1-low-vintage-unc-grey`: 3
- `nike-dunk-low-polar-blue`: 3
- `tenis-air-jordan-1-mid-gs-rookie-season-branco-vermelho`: 3
- `adidas-samba-og-black-gum`: 2
- `born-x-raised-x-nike-sb-dunk-low-one-block-at-a-time`: 2
- `yeezy-boost-350-v2-zebra`: 2
- `adidas-campus-00s-kids-black-white-gum`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 9.170s

OK
20260609T173116Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
