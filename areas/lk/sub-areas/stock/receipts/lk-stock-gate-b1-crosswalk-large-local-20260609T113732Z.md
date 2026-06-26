# LK Stock — Gate B.1 crosswalk local/offline — lote maior

- Data UTC: 2026-06-09T11:37:32Z
- Pedido: Lucas disse “Seguir” após segundo piloto controlado.
- Interpretação segura: expandir lote local/read-only Gate B.1, sem ativar runtime.
- Runtime ativado: Nenhum.
- Webhook/cron/bot ativado: Nenhum.
- Tiny write: 0.
- Shopify write: 0.
- Writes externos executados: 0.
- Secrets impressos: não.

## Lote selecionado

Selecionado via Shopify Admin GraphQL read-only entre produtos ativos com grade real, excluindo os SKUs já usados em pilotos anteriores.

SKUs:

- `DZ5318640`
- `DC0774801`
- `CU9225100`
- `CI0919600`
- `DD1503122`
- `DH9765003`
- `DD1503100`
- `CZ0775801`
- `DA8301100`
- `DQ8561001`

## Artefatos locais

- DB SQLite: `areas/lk/sub-areas/stock/data/gate_b1_crosswalk_large_local_20260609T113224Z.db`
- Reports JSON/CSV por SKU: `areas/lk/sub-areas/stock/reports/tiny-shopify-crosswalk-<sku>-gateb1-large-20260609T113224Z.*`

## Resultado agregado do lote

```json
{
  "total": 78,
  "allowed": 76,
  "blocked": 2,
  "writes_externos": 0
}
```

Por status:

```json
[
  {"mapping_status":"matched_exact_sku_stock_resolved","count":76},
  {"mapping_status":"shopify_variant_tiny_missing","count":1},
  {"mapping_status":"tiny_duplicate_exact_code_blocked","count":1}
]
```

Por produto:

```json
[
  {"prefix":"CI0919600","total":7,"allowed":7,"blocked":0},
  {"prefix":"CU9225100","total":10,"allowed":8,"blocked":2},
  {"prefix":"CZ0775801","total":9,"allowed":9,"blocked":0},
  {"prefix":"DA8301100","total":7,"allowed":7,"blocked":0},
  {"prefix":"DC0774801","total":9,"allowed":9,"blocked":0},
  {"prefix":"DD1503100","total":7,"allowed":7,"blocked":0},
  {"prefix":"DD1503122","total":8,"allowed":8,"blocked":0},
  {"prefix":"DH9765003","total":6,"allowed":6,"blocked":0},
  {"prefix":"DQ8561001","total":6,"allowed":6,"blocked":0},
  {"prefix":"DZ5318640","total":9,"allowed":9,"blocked":0}
]
```

## Issues abertas do lote

```json
[
  {"sku":"CU9225100","issue_type":"shopify_variant_tiny_missing","severity":"blocked","status":"open"},
  {"sku":"CU9225100-9","issue_type":"tiny_duplicate_exact_code_blocked","severity":"blocked","status":"open"}
]
```

Detalhe operacional:

- `CU9225100` parent/base: Shopify possui SKU/base, mas Tiny não retornou código exato resolvido.
- `CU9225100-9` tamanho 39.5: Tiny retornou mais de um produto ativo com o mesmo código exato; disponibilidade bloqueada até saneamento.

## Resultado acumulado dos pilotos Gate B.1

Somando os pilotos `U204LMMC`, segundo piloto de 4 produtos e este lote de 10 produtos:

```json
{
  "total_rows": 130,
  "allowed": 124,
  "blocked": 6
}
```

## Verificação

Comando:

```bash
python3 -m unittest discover -s areas/lk/sub-areas/stock/evaluation -p 'test_*.py'
```

Resultado final:

```text
Ran 20 tests in 4.110s
OK
```

## Decisão recomendada

Gate B.1 local está validado para operar como índice/cache de saneamento e consulta rápida. Ainda não houve ativação de cron/webhook/runtime.

Próximo gate recomendado: preparar `Gate B.2` como lote completo local/read-only do catálogo ativo com receipt e fila consolidada de saneamento. Depois disso, criar packet separado de aprovação para cron de madrugada real.
