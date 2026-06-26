# LK Stock — Gate B.2 catálogo local/read-only — shard 9

- Data UTC: 2026-06-09T16:26:04Z
- Pedido: Lucas disse “Seguir” após shard 8 concluído.
- Interpretação segura: avançar para shard 9 local/read-only, sem ativar cron/webhook/runtime.
- Runtime ativado: nenhum.
- Webhook/cron/bot ativado: nenhum.
- Tiny write: 0.
- Shopify write: 0.
- Writes externos: 0.
- Secrets impressos: não.

## Seleção do shard 9

Arquivo de seleção:

- `areas/lk/sub-areas/stock/reports/gate-b2-shard9-selected-skus-20260609.json`

Arquivo com prefixes executados:

- `areas/lk/sub-areas/stock/reports/gate-b2-shard9-executed-prefixes-20260609.json`

Prefixes executados:

- `DN1431103-34`
- `DD1503117`
- `DQ7579300`
- `DH9765401`
- `DQ8396600`
- `DD1873102`
- `DH7004109`
- `553560052`
- `CZ0790001`
- `DQ5130400`
- `DX5930001`
- `DV3054001`
- `allstar`
- `555088063`
- `553560412`
- `DC7267500`
- `dd1873-100`
- `DN1431101`
- `DX2937100`
- `DZ5485031`

Observação: a seleção do shard 9 excluiu bases e handles já processados nos shards 1–8 e também bloqueou handle duplicado dentro do próprio shard.

## DB local

`areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard9_20260609T161646Z.db`

## Resultado consolidado

```json
{
  "sku_count": 20,
  "total": 121,
  "allowed": 98,
  "blocked": 23,
  "writes_externos": 0
}
```

Por status:

```json
[
  {"mapping_status":"matched_exact_sku_stock_resolved","count":98},
  {"mapping_status":"shopify_variant_tiny_missing","count":9},
  {"mapping_status":"shopify_duplicate_sku_blocked","count":6},
  {"mapping_status":"tiny_duplicate_exact_code_blocked","count":6},
  {"mapping_status":"matched_exact_sku_stock_missing_deposit","count":2}
]
```

## Issues abertas

Total: 23.

Categorias:

- 9 × Shopify variant/SKU sem Tiny exato resolvido.
- 6 × duplicidade exata de SKU no Shopify.
- 6 × duplicidade exata de código no Tiny.
- 2 × Tiny encontrado, mas sem confirmação do depósito oficial `LK | CONTROLE ESTOQUE`.

Produtos/handles com mais bloqueios:

```json
[
  {"handle":"air-jordan-1-low-true-blue","total":6,"allowed":1,"blocked":5},
  {"handle":"nike-dunk-low-next-nature-black-white","total":13,"allowed":11,"blocked":2},
  {"handle":"air-jordan-1-high-og-lucky-green","total":8,"allowed":6,"blocked":2},
  {"handle":"air-jordan-1-low-se-pink-velvet","total":7,"allowed":5,"blocked":2},
  {"handle":"nike-dunk-low-lx-black-team-gold","total":4,"allowed":2,"blocked":2}
]
```

Duplicidade Shopify detectada no shard 9:

- `553560052`
- `555088063`
- `DC7267500`
- `DN1431101`
- `DV3054001`
- `DZ5485031`

Duplicidade Tiny detectada no shard 9:

- `553560412-2`
- `553560412-3`
- `553560412-4`
- `553560412-5`
- `553560412-6`
- `DZ5485031-7`

Depósito oficial faltando no shard 9:

- `DD1873102-8`
- `DQ5130400-42`

## Verificação

Comando:

```bash
python3 -m unittest discover -s areas/lk/sub-areas/stock/evaluation -p 'test_*.py'
```

Resultado:

```text
Ran 20 tests in 12.627s
OK
```

## Decisão operacional

Shard 9 concluído e válido como evidência local/read-only.

Próximo passo seguro: avançar para shard 10 local/read-only, mantendo exclusão por base e handle já processados e handle único dentro do shard.
