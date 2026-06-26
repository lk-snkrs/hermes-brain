# Receipt — LK Stock Gate B.2 shard 89

Data/hora UTC: 20260610T043435Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard89_20260610T042956Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard89-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard89-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard89-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 70
- `availability_claim_allowed = 1`: 64
- Bloqueadas: 6
- Issues abertas: 6

### Status

- `matched_exact_sku_stock_resolved`: 64
- `shopify_variant_tiny_missing`: 5
- `tiny_duplicate_exact_code_blocked`: 1

### Duplicidade Shopify bloqueada

- Nenhuma

### Duplicidade Tiny bloqueada

- `1073003`

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `camiseta-aime-leon-dore-postcard-cream-bege`: 1
- `tenis-adidas-stella-mccartney-x-adidas-wmns-sportswear-x-trainers-core-black-preto`: 1
- `tenis-nike-craft-general-purpose-shoe-tom-sachs`: 1
- `tenis-nike-craft-general-purpose-shoe-tom-sachs-archive-dark-sulfur`: 1
- `tenis-nike-craft-general-purpose-shoe-tom-sachs-field-brown-marrom`: 1
- `tenis-tom-sachs-x-nikecraft-general-purpose-summit-white-branco`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 3.283s

OK
20260610T043435Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
