# LK Stock — Gate B.2 catálogo local/read-only — shard 6

- Data UTC: 2026-06-09T14:27:18Z
- Pedido: Lucas disse “seguir” após shard 5 concluído.
- Interpretação segura: avançar para shard 6 local/read-only, sem ativar cron/webhook/runtime.
- Runtime ativado: nenhum.
- Webhook/cron/bot ativado: nenhum.
- Tiny write: 0.
- Shopify write: 0.
- Writes externos: 0.
- Secrets impressos: não.

## Seleção do shard 6

Arquivo de seleção:

- `areas/lk/sub-areas/stock/reports/gate-b2-shard6-selected-skus-20260609.json`

Arquivo com prefixes executados:

- `areas/lk/sub-areas/stock/reports/gate-b2-shard6-executed-prefixes-20260609.json`

Prefixes executados:

- `JRD-9681118-OS`
- `DM4657004`
- `JRD-0696926-OS`
- `555088134`
- `555088036`
- `BQ4422400`
- `GV9544`
- `GX4634`
- `DD1390100`
- `DH7755001`
- `FD8777100`
- `DM9652001`
- `553558701`
- `DZ1382001`
- `553558371`
- `555088037`
- `GW1931`
- `BQ6817303`
- `DC6991200`
- `DH6927140`

Observação: a seleção do shard 6 excluiu bases e handles já processados nos shards 1–5 e também bloqueou handle duplicado dentro do próprio shard.

## DB local

`areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard6_20260609T141530Z.db`

## Resultado consolidado

```json
{
  "sku_count": 20,
  "total": 170,
  "allowed": 150,
  "blocked": 20,
  "writes_externos": 0
}
```

Por status:

```json
[
  {"mapping_status":"matched_exact_sku_stock_resolved","count":150},
  {"mapping_status":"shopify_variant_tiny_missing","count":12},
  {"mapping_status":"shopify_duplicate_sku_blocked","count":5},
  {"mapping_status":"tiny_duplicate_exact_code_blocked","count":3}
]
```

## Issues abertas

Total: 20.

Categorias:

- 12 × Shopify variant/SKU sem Tiny exato resolvido.
- 5 × duplicidade exata de SKU no Shopify.
- 3 × duplicidade exata de código no Tiny.
- 0 × Tiny encontrado sem depósito oficial.

Produtos/handles com mais bloqueios:

```json
[
  {"handle":"air-jordan-1-low-se-mocha","total":11,"allowed":8,"blocked":3},
  {"handle":"air-jordan-1-high-og-stealth","total":10,"allowed":8,"blocked":2},
  {"handle":"air-jordan-1-mid-se-craft-inside-out-black","total":10,"allowed":8,"blocked":2},
  {"handle":"nike-sb-dunk-high-pro-black-and-metallic-gold","total":10,"allowed":8,"blocked":2},
  {"handle":"adi2000-triple-black","total":9,"allowed":7,"blocked":2},
  {"handle":"adidas-adi2000-chalk-white","total":8,"allowed":6,"blocked":2}
]
```

Duplicidade Shopify detectada no shard 6:

- `553558701`
- `555088036`
- `555088134`
- `BQ4422400`
- `DZ1382001`

Duplicidade Tiny detectada no shard 6:

- `555088037-44`
- `DC6991200-1`
- `DC6991200-15`

## Verificação

Comando:

```bash
python3 -m unittest discover -s areas/lk/sub-areas/stock/evaluation -p 'test_*.py'
```

Resultado:

```text
Ran 20 tests in 8.400s
OK
```

## Decisão operacional

Shard 6 concluído e válido como evidência local/read-only.

Próximo passo seguro: avançar para shard 7 local/read-only, mantendo exclusão por base e handle já processados e handle único dentro do shard.
