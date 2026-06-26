# Receipt — LK Stock Gate B.2 shard 33

Data/hora UTC: 20260609T204709Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard33_20260609T203858Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard33-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard33-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard33-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 122
- `availability_claim_allowed = 1`: 111
- Bloqueadas: 11
- Issues abertas: 11

### Status

- `matched_exact_sku_stock_resolved`: 111
- `shopify_duplicate_sku_blocked`: 4
- `tiny_duplicate_exact_code_blocked`: 4
- `shopify_variant_tiny_missing`: 3

### Duplicidade Shopify bloqueada

- `1203A766200`
- `MR530SZ`
- `ST11`
- `ST27`

### Duplicidade Tiny bloqueada

- `41499220121-4`
- `41499662711-4`
- `41499672090-4`
- `ST27-2`

### Depósito oficial ausente

- Nenhum

### Top handles por bloqueios

- `chinelo-havaianas-x-dolce-gabanna-blue-mediterraneo-azul`: 2
- `chinelo-havaianas-x-dolce-gabanna-carreto-ciciliano-vermelho`: 2
- `chinelo-havaianas-x-dolce-gabanna-zebra-preto`: 2
- `regata-saint-studio-canelada-egipcio-off-white`: 2
- `calca-saint-studio-wide-alfaiataria-caqui`: 1
- `tenis-asics-gel-kayano-14-x-senna-white-red-branco`: 1
- `tenis-new-balance-530-sea-salt-white-mercury-rede-branco`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 5.014s

OK
20260609T204709Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
