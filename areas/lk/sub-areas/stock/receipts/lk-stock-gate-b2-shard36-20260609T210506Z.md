# Receipt — LK Stock Gate B.2 shard 36

Data/hora UTC: 20260609T210506Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard36_20260609T205645Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard36-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard36-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard36-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 141
- `availability_claim_allowed = 1`: 128
- Bloqueadas: 13
- Issues abertas: 13

### Status

- `matched_exact_sku_stock_resolved`: 128
- `shopify_duplicate_sku_blocked`: 13

### Duplicidade Shopify bloqueada

- `DM7866-202`
- `HF3144 100-1`
- `HF3144 100-10`
- `HF3144 100-11`
- `HF3144 100-2`
- `HF3144 100-3`
- `HF3144 100-4`
- `HF3144 100-5`
- `HF3144 100-6`
- `HF3144 100-7`
- `HF3144 100-8`
- `HF3144 100-9`
- `HF4084-200`

### Duplicidade Tiny bloqueada

- Nenhuma

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `tenis-air-jordan-1-low-og-year-of-snake-2025-cinza`: 11
- `tenis-air-jordan-1-low-og-sp-x-travis-scott-velvet-brown-marrom`: 1
- `tenis-nike-air-force-1-low-x-a-ma-maniere-while-you-were-sleeping-rose`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 5.601s

OK
20260609T210506Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
