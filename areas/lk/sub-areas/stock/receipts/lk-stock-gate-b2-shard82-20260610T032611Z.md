# Receipt — LK Stock Gate B.2 shard 82

Data/hora UTC: 20260610T032611Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard82_20260610T031213Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard82-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard82-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard82-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 226
- `availability_claim_allowed = 1`: 200
- Bloqueadas: 26
- Issues abertas: 26

### Status

- `matched_exact_sku_stock_resolved`: 200
- `shopify_variant_tiny_missing`: 20
- `shopify_duplicate_sku_blocked`: 6

### Duplicidade Shopify bloqueada

- `U1906LOC-38`
- `U1906LOC-39`
- `U1906LOC-40`
- `U1906LOC-42`
- `U1906LOC-43`
- `U1906LOC-44`

### Duplicidade Tiny bloqueada

- Nenhuma

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `tenis-new-balance-1906l-silver-metallic-black-prata`: 7
- `tenis-adidas-samba-jane-chalk-white-wonder-quartz-branco`: 1
- `tenis-adidas-samba-og-crystal-linen-ivory-gum-branco`: 1
- `tenis-asics-marvel-vs-capcom-x-kith-x-asics-gel-kayano-14-ryu-branco`: 1
- `tenis-new-balance-204l-reflection-bege`: 1
- `tenis-new-balance-204l-sea-salt-linen-bege`: 1
- `tenis-new-balance-gator-run-black-preto`: 1
- `tenis-new-balance-gator-run-shadow-red-vermelho`: 1
- `tenis-new-balance-gator-run-star-burst-bege`: 1
- `tenis-new-balance-gator-run-timberwolf-bege`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 3.622s

OK
20260610T032611Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
