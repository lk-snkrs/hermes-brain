# Receipt — LK Stock Gate B.2 shard 31

Data/hora UTC: 20260609T203218Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard31_20260609T201659Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard31-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard31-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard31-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 236
- `availability_claim_allowed = 1`: 223
- Bloqueadas: 13
- Issues abertas: 13

### Status

- `matched_exact_sku_stock_resolved`: 223
- `shopify_duplicate_sku_blocked`: 8
- `tiny_duplicate_exact_code_blocked`: 3
- `shopify_variant_tiny_missing`: 2

### Duplicidade Shopify bloqueada

- `39884702`
- `DM4044108`
- `U9060EEB`
- `U9060GCB`
- `U9060GRY`
- `U9060VNG`
- `U9060ZGA`
- `V1004001060001`

### Duplicidade Tiny bloqueada

- `39884602-6`
- `PLAYPRINTED-2`
- `PLAYPRINTED-3`

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `camiseta-comme-des-garcons-play-printed-heart-branco`: 2
- `tenis-puma-speedcat-og-red-white-vermelho`: 2
- `tenis-new-balance-9060-moonbeam-vintage-rose-lime-colorido`: 1
- `tenis-new-balance-9060-moonrock-linen-dark-artic-greycinza`: 1
- `tenis-new-balance-9060-nori-verde`: 1
- `tenis-new-balance-9060-rain-cloud-grey-cinza`: 1
- `tenis-new-balance-9060-reflection-raincloud-quarry-blue-bege`: 1
- `tenis-new-balance-9060-sea-salt-concrete-branco`: 1
- `tenis-nike-cortez-forrest-gump-2024-branco`: 1
- `tenis-puma-speedcat-archive-haute-coffee-frosted-ivory-marrom`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 3.751s

OK
20260609T203218Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
