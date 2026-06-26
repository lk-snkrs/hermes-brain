# Receipt — LK Stock Gate B.2 shard 22

Data/hora UTC: 20260609T185606Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard22_20260609T184803Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard22-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard22-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard22-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 133
- `availability_claim_allowed = 1`: 124
- Bloqueadas: 9
- Issues abertas: 9

### Status

- `matched_exact_sku_stock_resolved`: 124
- `tiny_duplicate_exact_code_blocked`: 5
- `shopify_duplicate_sku_blocked`: 2
- `shopify_variant_tiny_missing`: 2

### Duplicidade Shopify bloqueada

- `IG2088`
- `IH2610`

### Duplicidade Tiny bloqueada

- `FZ5167-133-5`
- `ID9065`
- `IH2612-10`
- `IH2612-2`
- `IH2612-8`

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `tenis-adidas-handball-spezial-sporty-rich-brown-marrom`: 4
- `tenis-nike-cortez-valentines-day-branco`: 2
- `tenis-adidas-handball-spezial-sporty-rich-pink-rosa`: 1
- `tenis-adidas-samba-x-humanrace-core-black-cinza`: 1
- `tenis-adidas-samba-x-humanrace-navy-aluminum-cinza`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 7.320s

OK
20260609T185606Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
