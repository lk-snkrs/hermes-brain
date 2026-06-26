# LK Stock — Gate B.2 catálogo local/read-only — shard 7

- Data UTC: 2026-06-09T15:24:08Z
- Pedido: Lucas disse “Seguir” após shard 6 concluído.
- Interpretação segura: avançar para shard 7 local/read-only, sem ativar cron/webhook/runtime.
- Runtime ativado: nenhum.
- Webhook/cron/bot ativado: nenhum.
- Tiny write: 0.
- Shopify write: 0.
- Writes externos: 0.
- Secrets impressos: não.

## Seleção do shard 7

Arquivo de seleção:

- `areas/lk/sub-areas/stock/reports/gate-b2-shard7-selected-skus-20260609.json`

Arquivo com prefixes executados:

- `areas/lk/sub-areas/stock/reports/gate-b2-shard7-executed-prefixes-20260609.json`

Prefixes executados:

- `CD2563101`
- `DO9395400`
- `BQ6817600`
- `DR9654100`
- `DH6931001`
- `DM1199100`
- `FD8775100`
- `553558163`
- `555088105`
- `HQ6448`
- `GX4472`
- `FD8776800`
- `BQ6817401`
- `DJ6188001`
- `DD1391104`
- `DD1649001-Mans`
- `DD9335641`
- `DQ8394301`
- `FD8775001`
- `DX5549400`

Observação: a seleção do shard 7 excluiu bases e handles já processados nos shards 1–6 e também bloqueou handle duplicado dentro do próprio shard.

## DB local

`areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard7_20260609T151105Z.db`

## Resultado consolidado

```json
{
  "sku_count": 20,
  "total": 208,
  "allowed": 200,
  "blocked": 8,
  "writes_externos": 0
}
```

Por status:

```json
[
  {"mapping_status":"matched_exact_sku_stock_resolved","count":200},
  {"mapping_status":"shopify_duplicate_sku_blocked","count":3},
  {"mapping_status":"tiny_duplicate_exact_code_blocked","count":3},
  {"mapping_status":"shopify_variant_tiny_missing","count":2}
]
```

## Issues abertas

Total: 8.

Categorias:

- 3 × duplicidade exata de SKU no Shopify.
- 3 × duplicidade exata de código no Tiny.
- 2 × Shopify variant/SKU sem Tiny exato resolvido.
- 0 × Tiny encontrado sem depósito oficial.

Produtos/handles com mais bloqueios:

```json
[
  {"handle":"air-jordan-1-high-atmosphere","total":9,"allowed":7,"blocked":2},
  {"handle":"concepts-x-nike-sb-dunk-low-orange-lobster","total":9,"allowed":7,"blocked":2},
  {"handle":"air-jordan-1-low-se-tie-dye","total":11,"allowed":10,"blocked":1},
  {"handle":"nike-sb-dunk-low-pro-chicago","total":11,"allowed":10,"blocked":1},
  {"handle":"air-jordan-1-high-dark-mocha","total":4,"allowed":3,"blocked":1},
  {"handle":"yeezy-slide-onyx","total":1,"allowed":0,"blocked":1}
]
```

Duplicidade Shopify detectada no shard 7:

- `555088105`
- `DM1199100`
- `HQ6448`

Duplicidade Tiny detectada no shard 7:

- `BQ6817600`
- `DD9335641-9`
- `FD8776800-8`

## Verificação

Comando:

```bash
python3 -m unittest discover -s areas/lk/sub-areas/stock/evaluation -p 'test_*.py'
```

Resultado:

```text
Ran 20 tests in 5.771s
OK
```

## Decisão operacional

Shard 7 concluído e válido como evidência local/read-only.

Próximo passo seguro: avançar para shard 8 local/read-only, mantendo exclusão por base e handle já processados e handle único dentro do shard.
