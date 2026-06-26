# Receipt — LK Stock Gate B.2 shard 39

Data/hora UTC: 20260609T212913Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard39_20260609T211814Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard39-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard39-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard39-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 184
- `availability_claim_allowed = 1`: 181
- Bloqueadas: 3
- Issues abertas: 3

### Status

- `matched_exact_sku_stock_resolved`: 181
- `shopify_duplicate_sku_blocked`: 2
- `tiny_duplicate_exact_code_blocked`: 1

### Duplicidade Shopify bloqueada

- `U997AIM`
- `VN000E3QBX9`

### Duplicidade Tiny bloqueada

- `1183A592200`

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `tenis-new-balance-997-made-in-usa-x-aime-leon-dore-dark-moss-angora-marrom`: 1
- `tenis-onitsuka-tiger-mexico-66-sd-birch-silver-bege`: 1
- `tenis-vans-knu-skool-mte-1-lx-imran-potato-azul`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 3.611s

OK
20260609T212913Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
