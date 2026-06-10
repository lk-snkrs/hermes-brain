# LK Stock — Gate B.2 catálogo local/read-only — shard 3

- Data UTC: 2026-06-09T13:42:49Z
- Pedido: Lucas disse “Seguir” após shard 2 concluído.
- Interpretação segura: avançar para shard 3 local/read-only, sem ativar cron/webhook/runtime.
- Runtime ativado: nenhum.
- Webhook/cron/bot ativado: nenhum.
- Tiny write: 0.
- Shopify write: 0.
- Writes externos: 0.
- Secrets impressos: não.

## Seleção do shard 3

Arquivo de seleção:

- `areas/lk/sub-areas/stock/reports/gate-b2-shard3-selected-skus-20260609.json`

Arquivo com prefixes executados:

- `areas/lk/sub-areas/stock/reports/gate-b2-shard3-executed-prefixes-20260609.json`

Prefixes executados:

- `DD1503118`
- `DD1503123`
- `DZ5318640`
- `BQ6472105`
- `DC0774801`
- `CU9225100`
- `CI0919600`
- `DC0774101`
- `DD1503122`
- `DH9765003`
- `DD1503100`
- `CZ0775801`
- `DA8301100`
- `DQ8561001`
- `JRD-1980638`
- `CZ9084001`
- `DC9936100`
- `CT2552800`
- `BQ6817009`
- `CJ5378300`

Observação: a seleção excluiu bases e handles já processados nos shards 1 e 2 para não repetir produtos com SKU malformado/alternativo do mesmo handle.

## DB local

`areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard3_20260609T133237Z.db`

## Resultado consolidado

```json
{
  "sku_count": 20,
  "total": 137,
  "allowed": 114,
  "blocked": 23,
  "writes_externos": 0
}
```

Por status:

```json
[
  {"mapping_status":"matched_exact_sku_stock_resolved","count":114},
  {"mapping_status":"shopify_variant_tiny_missing","count":15},
  {"mapping_status":"matched_exact_sku_stock_missing_deposit","count":3},
  {"mapping_status":"tiny_duplicate_exact_code_blocked","count":3},
  {"mapping_status":"shopify_duplicate_sku_blocked","count":2}
]
```

## Issues abertas

Total: 23.

Categorias:

- 15 × Shopify variant/SKU sem Tiny exato resolvido.
- 3 × Tiny encontrado, mas sem confirmação do depósito oficial `LK | CONTROLE ESTOQUE`.
- 3 × duplicidade exata de código no Tiny.
- 2 × duplicidade exata de SKU no Shopify.

Produtos/handles com mais bloqueios:

```json
[
  {"handle":"air-jordan-1-low-panda-2023","total":12,"allowed":9,"blocked":3},
  {"handle":"supreme-x-nike-air-force-1-low-box-logo-white","total":10,"allowed":7,"blocked":3},
  {"handle":"air-jordan-1-low-starfish-mans-feminino","total":9,"allowed":7,"blocked":2},
  {"handle":"air-jordan-1-mid-wolf-grey","total":9,"allowed":7,"blocked":2},
  {"handle":"nike-dunk-low-ocean-bliss","total":9,"allowed":7,"blocked":2},
  {"handle":"nike-air-force-1-low-shadow-light-soft-pink","total":7,"allowed":5,"blocked":2},
  {"handle":"nike-sb-dunk-low-strangelove","total":2,"allowed":0,"blocked":2}
]
```

Duplicidade Shopify detectada no shard 3:

- `BQ6817009`
- `DC9936100`

Duplicidade Tiny detectada no shard 3:

- `CU9225100-9`
- `DC0774101-14`
- `DC0774101-15`

## Verificação

Comando:

```bash
python3 -m unittest discover -s areas/lk/sub-areas/stock/evaluation -p 'test_*.py'
```

Resultado:

```text
Ran 20 tests in 6.422s
OK
```

## Decisão operacional

Shard 3 concluído e válido como evidência local/read-only.

Próximo passo seguro: avançar para shard 4 local/read-only, mantendo exclusão por base e handle já processados para evitar repetir produto por SKU malformado/alternativo.
