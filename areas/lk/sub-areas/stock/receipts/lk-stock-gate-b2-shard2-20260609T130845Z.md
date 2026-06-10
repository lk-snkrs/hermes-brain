# LK Stock — Gate B.2 catálogo local/read-only — shard 2

- Data UTC: 2026-06-09T13:08:45Z
- Pedido: Lucas disse “seguir” após shard 1 reexecutado com regra `shopify_duplicate_sku_blocked`.
- Interpretação segura: avançar para shard 2 local/read-only, sem ativar cron/webhook/runtime.
- Runtime ativado: nenhum.
- Webhook/cron/bot ativado: nenhum.
- Tiny write: 0.
- Shopify write: 0.
- Writes externos: 0.
- Secrets impressos: não.

## Seleção do shard 2

Arquivo de seleção:

- `areas/lk/sub-areas/stock/reports/gate-b2-shard2-selected-skus-20260609.json`

Arquivo com prefixes executados:

- `areas/lk/sub-areas/stock/reports/gate-b2-shard2-executed-prefixes-20260609.json`

Prefixes executados:

- `DV1748601]`
- `DC0774-006`
- `CW1590-601`
- `DD1503-300`
- `DB2908`
- `DO93922000`
- `DO9392200`
- `DM7866162`
- `HP6772`
- `DX1419300`
- `CV9388100`
- `DR5415103`
- `DQ4040400`
- `DD1391400`
- `DD1391402`
- `DZ5350288`
- `DV1681100`
- `DD1391401`
- `DR9705100`
- `DJ9955600`

Observação: a seleção do catálogo usou base SKU normalizada para evitar misturar tamanho como parte do modelo; a execução preservou o prefixo Shopify legível quando havia hífen no código (`DC0774-006`, `CW1590-601`, etc.).

## DB local

`areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard2_20260609T125613Z.db`

## Resultado consolidado

```json
{
  "sku_count": 20,
  "total": 139,
  "allowed": 103,
  "blocked": 36,
  "writes_externos": 0
}
```

Por status:

```json
[
  {"mapping_status":"matched_exact_sku_stock_resolved","count":103},
  {"mapping_status":"shopify_variant_tiny_missing","count":25},
  {"mapping_status":"matched_exact_sku_stock_missing_deposit","count":5},
  {"mapping_status":"shopify_duplicate_sku_blocked","count":3},
  {"mapping_status":"tiny_duplicate_exact_code_blocked","count":3}
]
```

## Issues abertas

Total: 36.

Categorias:

- 25 × Shopify variant/SKU sem Tiny exato resolvido.
- 5 × Tiny encontrado, mas sem confirmação do depósito oficial `LK | CONTROLE ESTOQUE`.
- 3 × duplicidade exata de SKU no Shopify.
- 3 × duplicidade exata de código no Tiny.

Produtos/handles com mais bloqueios:

```json
[
  {"handle":"nike-dunk-low-pink-foam-black","total":5,"allowed":2,"blocked":3},
  {"handle":"nike-dunk-low-pink-red-white","total":4,"allowed":1,"blocked":3},
  {"handle":"nike-dunk-low-teddy-bear","total":11,"allowed":8,"blocked":3},
  {"handle":"nike-dunk-low-valerian-blue","total":11,"allowed":8,"blocked":3},
  {"handle":"nike-sb-dunk-low-prm-phillies","total":9,"allowed":6,"blocked":3},
  {"handle":"yeezy-500-blush","total":12,"allowed":9,"blocked":3}
]
```

Duplicidade Shopify detectada no shard 2:

- `DD1391402`
- `DM7866162`
- `DO9392200`

Duplicidade Tiny detectada no shard 2:

- `CW1590-601-1`
- `CW1590-601-3`
- `CW1590-601-5`

## Execução

A primeira chamada de execução bateu timeout do terminal após 600s quando 16/20 prefixes já tinham persistido. Retomei os 4 prefixes restantes no mesmo DB local. Não houve write externo.

## Verificação

Comando:

```bash
python3 -m unittest discover -s areas/lk/sub-areas/stock/evaluation -p 'test_*.py'
```

Resultado:

```text
Ran 20 tests in 6.075s
OK
```

## Decisão operacional

Shard 2 concluído e válido como evidência local/read-only.

Próximo passo seguro: avançar para shard 3 local/read-only, mantendo a execução em lotes/checkpoints para evitar timeout longo do Tiny.
