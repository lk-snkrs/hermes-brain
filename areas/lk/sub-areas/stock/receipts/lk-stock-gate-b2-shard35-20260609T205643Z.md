# Receipt — LK Stock Gate B.2 shard 35

Data/hora UTC: 20260609T205643Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard35_20260609T205235Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard35-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard35-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard35-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 62
- `availability_claim_allowed = 1`: 57
- Bloqueadas: 5
- Issues abertas: 5

### Status

- `matched_exact_sku_stock_resolved`: 57
- `shopify_duplicate_sku_blocked`: 3
- `tiny_duplicate_exact_code_blocked`: 2

### Duplicidade Shopify bloqueada

- `FZ1267`
- `PC9060GY`
- `U9060BLK`

### Duplicidade Tiny bloqueada

- `PC9060GY-2`
- `U9060BLK-6`

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `tenis-new-balance-9060-black-castlerock-grey-preto`: 2
- `tenis-new-balance-9060-kids-raincloud-cinza`: 2
- `tenis-adidas-yeezy-boost-350-v2-zyon-marrom`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 4.633s

OK
20260609T205643Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
