# Receipt — LK Stock Gate B.2 shard 10

Data/hora UTC: 2026-06-09T16:39:33Z

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

- DB local: `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard10_20260609T163154Z.db`
- Seleção: `areas/lk/sub-areas/stock/reports/gate-b2-shard10-selected-skus-20260609.json`
- Prefixes executados: `areas/lk/sub-areas/stock/reports/gate-b2-shard10-executed-prefixes-20260609.json`
- Resumo: `areas/lk/sub-areas/stock/reports/gate-b2-shard10-summary-20260609.json`

## Prefixes executados

- `CZ0790-104`
- `FJ4555100`
- `553558062`
- `553558066`
- `554724069`
- `BQ6817302`
- `BQ6817500`
- `CD2563006`
- `CV1655600`
- `CZ0790061`
- `CZ2239600`
- `DD1872100`
- `DH6927017`
- `DH7138006`
- `DH7820700`
- `DM160210-40`
- `dn1431102`
- `DQ8423616`
- `553558411`
- `AQ9129103`

## Resultado consolidado

- Prefixes/SKUs processados: 20
- Linhas persistidas: 87
- `availability_claim_allowed = 1`: 65
- Bloqueadas: 22
- Issues abertas: 22

### Status

- `matched_exact_sku_stock_resolved`: 65
- `shopify_variant_tiny_missing`: 11
- `shopify_duplicate_sku_blocked`: 6
- `tiny_duplicate_exact_code_blocked`: 4
- `matched_exact_sku_stock_missing_deposit`: 1

### Duplicidade Shopify bloqueada

- `553558062`
- `BQ6817302`
- `BQ6817500`
- `CV1655600`
- `CZ0790061`
- `DH7820700`

### Duplicidade Tiny bloqueada

- `CD2563006-9`
- `CZ0790-104-5`
- `CZ2239600-3`
- `DH7138006-5`

### Depósito oficial ausente

- `DH7138006-6`

### Top handles por bloqueios

- `air-jordan-4-se-black-canvas`: 4
- `nike-sb-dunk-low-pro-iso-black-gum`: 4
- `nike-sb-dunk-low-pro-classic-green`: 3
- `nike-sb-dunk-low-what-the-p-rod`: 3

## Verificação

Comando:

```bash
python3 -m unittest discover -s areas/lk/sub-areas/stock/evaluation -p 'test_*.py'
```

Resultado:

```text
....................
----------------------------------------------------------------------
Ran 20 tests in 4.260s

OK
20260609T163933Z
```

## Observação

Este shard é baseline local de saneamento/crosswalk. Não é promessa de disponibilidade pública nem autorização de venda/pronta entrega.
