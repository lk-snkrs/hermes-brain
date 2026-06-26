# LK Stock — Gate B.2 catálogo local/read-only — shard 8

- Data UTC: 2026-06-09T16:05:16Z
- Pedido: Lucas disse “Seguir” após shard 7 concluído.
- Interpretação segura: avançar para shard 8 local/read-only, sem ativar cron/webhook/runtime.
- Runtime ativado: nenhum.
- Webhook/cron/bot ativado: nenhum.
- Tiny write: 0.
- Shopify write: 0.
- Writes externos: 0.
- Secrets impressos: não.

## Seleção do shard 8

Arquivo de seleção:

- `areas/lk/sub-areas/stock/reports/gate-b2-shard8-selected-skus-20260609.json`

Arquivo com prefixes executados:

- `areas/lk/sub-areas/stock/reports/gate-b2-shard8-executed-prefixes-20260609.json`

Prefixes executados:

- `DM0807300`
- `DJ6188003`
- `DH7577001`
- `553558052`
- `DC0774141`
- `DV1308004`
- `CT0979101`
- `GY7164`
- `FD9923111`
- `DD1503001`
- `555112401`
- `DM9036104`
- `DZ5485612`
- `HQ2060`
- `FD1449100`
- `DD1503601`
- `DV3054600`
- `DH4401100`
- `DH9765600`
- `DD1503120`

Observação: a seleção do shard 8 excluiu bases e handles já processados nos shards 1–7 e também bloqueou handle duplicado dentro do próprio shard.

## DB local

`areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard8_20260609T155241Z.db`

## Resultado consolidado

```json
{
  "sku_count": 20,
  "total": 193,
  "allowed": 184,
  "blocked": 9,
  "writes_externos": 0
}
```

Por status:

```json
[
  {"mapping_status":"matched_exact_sku_stock_resolved","count":184},
  {"mapping_status":"shopify_variant_tiny_missing","count":4},
  {"mapping_status":"tiny_duplicate_exact_code_blocked","count":3},
  {"mapping_status":"shopify_duplicate_sku_blocked","count":2}
]
```

## Issues abertas

Total: 9.

Categorias:

- 4 × Shopify variant/SKU sem Tiny exato resolvido.
- 3 × duplicidade exata de código no Tiny.
- 2 × duplicidade exata de SKU no Shopify.
- 0 × Tiny encontrado sem depósito oficial.

Produtos/handles com mais bloqueios:

```json
[
  {"handle":"air-jordan-1-mid-se-space-jam","total":9,"allowed":7,"blocked":2},
  {"handle":"nike-dunk-gs-triple-pink","total":7,"allowed":5,"blocked":2},
  {"handle":"tenis-air-jordan-1-high-og-denim-azul","total":2,"allowed":0,"blocked":2},
  {"handle":"air-jordan-1-high-chicago-lost-and-found","total":13,"allowed":12,"blocked":1},
  {"handle":"nike-dunk-low-pink-paisley","total":8,"allowed":7,"blocked":1},
  {"handle":"nike-dunk-low-lx-pink-foam","total":6,"allowed":5,"blocked":1}
]
```

Duplicidade Shopify detectada no shard 8:

- `DV1308004`
- `DZ5485612`

Duplicidade Tiny detectada no shard 8:

- `DM9036104-6`
- `DM9036104-9`
- `DV1308004-10`

## Verificação

Comando:

```bash
python3 -m unittest discover -s areas/lk/sub-areas/stock/evaluation -p 'test_*.py'
```

Resultado:

```text
Ran 20 tests in 3.163s
OK
```

## Decisão operacional

Shard 8 concluído e válido como evidência local/read-only.

Próximo passo seguro: avançar para shard 9 local/read-only, mantendo exclusão por base e handle já processados e handle único dentro do shard.
