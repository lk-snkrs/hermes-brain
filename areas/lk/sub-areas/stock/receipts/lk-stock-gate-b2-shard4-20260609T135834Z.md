# LK Stock — Gate B.2 catálogo local/read-only — shard 4

- Data UTC: 2026-06-09T13:58:34Z
- Pedido: Lucas disse “seguir” após shard 3 concluído.
- Interpretação segura: avançar para shard 4 local/read-only, sem ativar cron/webhook/runtime.
- Runtime ativado: nenhum.
- Webhook/cron/bot ativado: nenhum.
- Tiny write: 0.
- Shopify write: 0.
- Writes externos: 0.
- Secrets impressos: não.

## Seleção do shard 4

Arquivo de seleção:

- `areas/lk/sub-areas/stock/reports/gate-b2-shard4-selected-skus-20260609.json`

Arquivo com prefixes executados:

- `areas/lk/sub-areas/stock/reports/gate-b2-shard4-executed-prefixes-20260609.json`

Prefixes executados:

- `DD1503116`
- `CU1726100`
- `DD13916021`
- `DH9756101`
- `DO9776001`
- `DH4401101`
- `DR9511100`
- `DD139110`
- `DJ4702200`
- `DJ4702300`
- `DR0888001`
- `DJ4701300`
- `DX0755600`
- `DZ0480300`
- `DZ3670500`
- `DQ8656133`
- `FB8915400`
- `FB5059100`
- `DR9866001`
- `DR9866100`

Observação: a seleção do shard 4 excluiu bases e handles já processados nos shards 1–3 e também bloqueou handle duplicado dentro do próprio shard.

## DB local

`areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard4_20260609T134628Z.db`

## Resultado consolidado

```json
{
  "sku_count": 20,
  "total": 152,
  "allowed": 116,
  "blocked": 36,
  "writes_externos": 0
}
```

Por status:

```json
[
  {"mapping_status":"matched_exact_sku_stock_resolved","count":116},
  {"mapping_status":"shopify_variant_tiny_missing","count":28},
  {"mapping_status":"shopify_duplicate_sku_blocked","count":5},
  {"mapping_status":"matched_exact_sku_stock_missing_deposit","count":3}
]
```

## Issues abertas

Total: 36.

Categorias:

- 28 × Shopify variant/SKU sem Tiny exato resolvido.
- 5 × duplicidade exata de SKU no Shopify.
- 3 × Tiny encontrado, mas sem confirmação do depósito oficial `LK | CONTROLE ESTOQUE`.
- 0 × duplicidade exata de código no Tiny.

Produtos/handles com mais bloqueios:

```json
[
  {"handle":"nike-air-max-plus-dusk","total":11,"allowed":8,"blocked":3},
  {"handle":"nike-air-max-plus-m-frank-rudy","total":9,"allowed":6,"blocked":3},
  {"handle":"nike-air-force-1-low-world-champ","total":3,"allowed":0,"blocked":3},
  {"handle":"nike-air-max-plus-yellow-pink-gradient","total":10,"allowed":8,"blocked":2},
  {"handle":"nike-dunk-low-court-purple","total":10,"allowed":8,"blocked":2},
  {"handle":"nike-dunk-low-kentucky","total":10,"allowed":8,"blocked":2},
  {"handle":"nike-dunk-low-varsity-green","total":10,"allowed":8,"blocked":2},
  {"handle":"nike-dunk-low-black-masculino","total":9,"allowed":7,"blocked":2}
]
```

Duplicidade Shopify detectada no shard 4:

- `CU1726100`
- `DD139110`
- `DD1391101`
- `DD1391104-1`
- `DD1503116`

## Verificação

Comando:

```bash
python3 -m unittest discover -s areas/lk/sub-areas/stock/evaluation -p 'test_*.py'
```

Resultado:

```text
Ran 20 tests in 8.682s
OK
```

## Decisão operacional

Shard 4 concluído e válido como evidência local/read-only.

Próximo passo seguro: avançar para shard 5 local/read-only, mantendo exclusão por base e handle já processados e handle único dentro do shard.
