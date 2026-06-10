# LK Stock — Gate B.2 catálogo local/read-only — shard 5

- Data UTC: 2026-06-09T14:12:53Z
- Pedido: Lucas disse “seguir” após shard 4 concluído.
- Interpretação segura: avançar para shard 5 local/read-only, sem ativar cron/webhook/runtime.
- Runtime ativado: nenhum.
- Webhook/cron/bot ativado: nenhum.
- Tiny write: 0.
- Shopify write: 0.
- Writes externos: 0.
- Secrets impressos: não.

## Seleção do shard 5

Arquivo de seleção:

- `areas/lk/sub-areas/stock/reports/gate-b2-shard5-selected-skus-20260609.json`

Arquivo com prefixes executados:

- `areas/lk/sub-areas/stock/reports/gate-b2-shard5-executed-prefixes-20260609.json`

Prefixes executados:

- `U9060TRU`
- `BB550VTC`
- `DQ4488001`
- `DD3363100`
- `DQ8475001`
- `CJ5378700`
- `DN1803300`
- `CU3244100`
- `HQ2153`
- `DV3464002`
- `DV3464400`
- `DV3464001`
- `DM0032005`
- `DQ3983001`
- `DQ3989100`
- `JRD-8534238-OS`
- `BQ6472141`
- `DN4045001`
- `554724092`
- `DQ8426517`

Observação: a seleção do shard 5 excluiu bases e handles já processados nos shards 1–4 e também bloqueou handle duplicado dentro do próprio shard.

## DB local

`areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard5_20260609T140100Z.db`

## Resultado consolidado

```json
{
  "sku_count": 20,
  "total": 142,
  "allowed": 110,
  "blocked": 32,
  "writes_externos": 0
}
```

Por status:

```json
[
  {"mapping_status":"matched_exact_sku_stock_resolved","count":110},
  {"mapping_status":"shopify_variant_tiny_missing","count":25},
  {"mapping_status":"matched_exact_sku_stock_missing_deposit","count":5},
  {"mapping_status":"shopify_duplicate_sku_blocked","count":2}
]
```

## Issues abertas

Total: 32.

Categorias:

- 25 × Shopify variant/SKU sem Tiny exato resolvido.
- 5 × Tiny encontrado, mas sem confirmação do depósito oficial `LK | CONTROLE ESTOQUE`.
- 2 × duplicidade exata de SKU no Shopify.
- 0 × duplicidade exata de código no Tiny.

Produtos/handles com mais bloqueios:

```json
[
  {"handle":"neckface-x-nike-sb-dunk-low-pro-black","total":16,"allowed":13,"blocked":3},
  {"handle":"bad-bunny-x-adidas-forum-buckle-low-white","total":15,"allowed":12,"blocked":3},
  {"handle":"air-max-plus-black-and-yellow","total":11,"allowed":8,"blocked":3},
  {"handle":"nba-x-nike-dunk-low-chicago","total":11,"allowed":8,"blocked":3},
  {"handle":"ambush-x-nike-air-force-1-low-phantom","total":9,"allowed":6,"blocked":3},
  {"handle":"concepts-x-air-max-1-sp-mellow","total":15,"allowed":13,"blocked":2},
  {"handle":"air-max-plus-black-university-blue","total":10,"allowed":8,"blocked":2},
  {"handle":"new-balance-550-white-pine-green","total":8,"allowed":6,"blocked":2},
  {"handle":"air-jordan-1-mid-university-blue-unc","total":5,"allowed":3,"blocked":2}
]
```

Duplicidade Shopify detectada no shard 5:

- `DQ3989100`
- `DQ8475001`

Duplicidade Tiny detectada no shard 5:

- nenhuma.

## Verificação

Comando:

```bash
python3 -m unittest discover -s areas/lk/sub-areas/stock/evaluation -p 'test_*.py'
```

Resultado:

```text
Ran 20 tests in 3.891s
OK
```

## Decisão operacional

Shard 5 concluído e válido como evidência local/read-only.

Próximo passo seguro: avançar para shard 6 local/read-only, mantendo exclusão por base e handle já processados e handle único dentro do shard.
