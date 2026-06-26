# Receipt — LK Stock Gate B.2 shard 14

Data/hora UTC: 20260609T174017Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard14_20260609T173116Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard14-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard14-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard14-summary-20260609.json`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 132
- `availability_claim_allowed = 1`: 100
- Bloqueadas: 32
- Issues abertas: 32

### Status

- `matched_exact_sku_stock_resolved`: 100
- `shopify_duplicate_sku_blocked`: 16
- `shopify_variant_tiny_missing`: 11
- `matched_exact_sku_stock_missing_deposit`: 3
- `tiny_duplicate_exact_code_blocked`: 2

### Duplicidade Shopify bloqueada

- `553558215`
- `553558612`
- `555088108`
- `AQ9129001`
- `CZ0790161`
- `DC0774105`
- `DC0774304-2`
- `DC0774304-3`
- `DC0774304-5`
- `DC0774304-6`
- `DC0774304-8`
- `DD1503124-1`
- `DD1503500`
- `DN1635200`
- `DR8867400`
- `FN7308008`

### Duplicidade Tiny bloqueada

- `DN1635001-38-8`
- `DR8867400-3`

### Depósito oficial ausente

- `DC0774105-4`
- `DD1503124-12`
- `DV1299104`

### Top handles por bloqueios

- `tenis-air-jordan-1-low-lucky-green-verde`: 6
- `tenis-air-jordan-1-low-wolf-grey-cinza`: 3
- `air-jordan-1-high-stage-haze`: 2
- `air-jordan-4-frozen-moments`: 2
- `tenis-air-jordan-1-low-purple-roxo`: 2
- `tenis-air-jordan-1-low-se-craft-inside-out-obsidian-azul`: 2
- `tenis-air-jordan-1-low-se-reverse-ice-blue-azul`: 2
- `tenis-nike-dunk-low-cacao-wow-marrom`: 2
- `tenis-nike-dunk-low-se-just-do-it-white-phantom-branco`: 2
- `air-jordan-1-low-bred-toe-1`: 1

## Verificação

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 4.862s

OK
20260609T174017Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
