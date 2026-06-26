# Receipt — LK Stock Gate B.2 shard 75

Data/hora UTC: 20260610T022753Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard75_20260610T022353Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard75-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard75-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard75-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 64
- `availability_claim_allowed = 1`: 62
- Bloqueadas: 2
- Issues abertas: 2

### Status

- `matched_exact_sku_stock_resolved`: 62
- `shopify_variant_tiny_missing`: 2

### Duplicidade Shopify bloqueada

- Nenhuma

### Duplicidade Tiny bloqueada

- Nenhuma

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `moletom-becalm-hoodie-cropped-ultra-suave-modal-algodao`: 1
- `tenis-alo-yoga-alo-recovery-mode-sneaker-pink-wild-rose-rosa-copia`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 3.883s

OK
20260610T022753Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
