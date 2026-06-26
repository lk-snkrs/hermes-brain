# LK Stock — Gate B.2 shard 1 reexecutado com regra `shopify_duplicate_sku_blocked`

- Data UTC: 2026-06-09T12:44:40Z
- Pedido: Lucas disse “seguir” após descoberta de duplicidade Shopify no shard 1.
- Interpretação segura: reexecutar shard 1 inteiro com a regra nova antes de avançar shard 2.
- Escopo: local/read-only.
- Runtime ativado: nenhum.
- Webhook/cron/bot ativado: nenhum.
- Tiny write: 0.
- Shopify write: 0.
- Writes externos: 0.
- Secrets impressos: não.

## DB local

`areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard1_rerun_20260609T123107Z.db`

## SKUs reexecutados

- `B75806`
- `DX5930100`
- `DJ9955101`
- `CW1588601`
- `DD1503103`
- `DB4612300`
- `H06426`
- `H06423`
- `H06442`
- `HQ6447`
- `FZ5897`
- `FY4567`
- `HP8739`
- `GY3969`
- `HQ4540`
- `GW3773`
- `GW2869`
- `FW3042`
- `HP5425`
- `B75571`

## Resultado consolidado

```json
{
  "sku_count": 20,
  "total": 178,
  "allowed": 139,
  "blocked": 39,
  "writes_externos": 0
}
```

Por status:

```json
[
  {"mapping_status":"matched_exact_sku_stock_resolved","count":139},
  {"mapping_status":"shopify_variant_tiny_missing","count":27},
  {"mapping_status":"matched_exact_sku_stock_missing_deposit","count":6},
  {"mapping_status":"shopify_duplicate_sku_blocked","count":5},
  {"mapping_status":"tiny_duplicate_exact_code_blocked","count":1}
]
```

## Issues abertas

Total: 39.

Categorias:

- 27 × Shopify variant/SKU sem Tiny exato resolvido.
- 6 × Tiny encontrado, mas sem confirmação do depósito oficial `LK | CONTROLE ESTOQUE`.
- 5 × duplicidade exata de SKU no Shopify.
- 1 × duplicidade exata de código no Tiny.

Produtos com mais bloqueios:

```json
[
  {"prefix":"FY4567","total":21,"allowed":16,"blocked":5},
  {"prefix":"B75571","total":12,"allowed":9,"blocked":3},
  {"prefix":"FZ5897","total":21,"allowed":18,"blocked":3},
  {"prefix":"GW2869","total":10,"allowed":7,"blocked":3},
  {"prefix":"GW3773","total":9,"allowed":6,"blocked":3},
  {"prefix":"H06423","total":9,"allowed":6,"blocked":3},
  {"prefix":"HP5425","total":13,"allowed":10,"blocked":3},
  {"prefix":"HQ4540","total":12,"allowed":9,"blocked":3}
]
```

## Verificação

Comando:

```bash
python3 -m unittest discover -s areas/lk/sub-areas/stock/evaluation -p 'test_*.py'
```

Resultado:

```text
Ran 20 tests in 6.148s
OK
```

## Decisão operacional

Shard 1 agora está válido como baseline local com a regra nova.

Próximo passo seguro: avançar para shard 2 local/read-only, mantendo o mesmo padrão de bloqueio para Tiny duplicado, Shopify duplicado, Tiny missing e depósito oficial não confirmado.
