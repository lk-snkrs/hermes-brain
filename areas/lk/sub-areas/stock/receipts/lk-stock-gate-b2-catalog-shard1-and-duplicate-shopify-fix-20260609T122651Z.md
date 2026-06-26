# LK Stock — Gate B.2 catálogo local/read-only — shard 1 + correção duplicidade Shopify

- Data UTC: 2026-06-09T12:26:51Z
- Pedido: Lucas disse “Seguir” após Gate B.1 lote maior.
- Interpretação segura: iniciar Gate B.2 local/read-only do catálogo ativo, sem ativar cron/webhook/runtime.
- Runtime ativado: Nenhum.
- Webhook/cron/bot ativado: Nenhum.
- Tiny write: 0.
- Shopify write: 0.
- Writes externos executados: 0.
- Secrets impressos: não.

## Descoberta de escala do catálogo ativo

Consulta Shopify Admin GraphQL read-only:

```json
{
  "active_variants_seen": 15447,
  "base_groups": 2213,
  "grade_groups_2_to_30": 1152,
  "estimated_rows_with_parent": 9463
}
```

Conclusão: catálogo completo precisa ser rodado em shards locais; rodar tudo em um único comando síncrono seria lento e frágil por causa da API Tiny.

## Shard 1 executado

Selecionados 20 SKUs ainda não usados nos pilotos anteriores:

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

DB local do shard:

- `areas/lk/sub-areas/stock/data/gate_b2_crosswalk_catalog_shard1_20260609T120544Z.db`

Resumo inicial do shard antes da correção de duplicidade Shopify:

```json
{
  "total": 178,
  "allowed": 143,
  "blocked": 35,
  "writes_externos": 0
}
```

Status observados:

```json
[
  {"mapping_status":"matched_exact_sku_stock_resolved","count":143},
  {"mapping_status":"shopify_variant_tiny_missing","count":28},
  {"mapping_status":"matched_exact_sku_stock_missing_deposit","count":6},
  {"mapping_status":"tiny_duplicate_exact_code_blocked","count":1}
]
```

## Issue crítica descoberta durante validação

No `B75806`, o relatório mostrou múltiplas variants Shopify com o mesmo SKU base `B75806`. A persistência local anterior tinha `UNIQUE(sku, source)` e podia deduplicar silenciosamente essas variants, escondendo conflito de grade.

Regra nova aplicada:

- Duplicidade exata de SKU em variants Shopify agora bloqueia o SKU com status `shopify_duplicate_sku_blocked`.
- Não é permitido prometer disponibilidade quando Shopify tem múltiplas variants com o mesmo SKU.

Arquivos alterados:

- `areas/lk/sub-areas/stock/scripts/schema_gate_b.sql`
- `areas/lk/sub-areas/stock/scripts/stock_local_db.py`
- `areas/lk/sub-areas/stock/scripts/lk_stock_tiny_shopify_crosswalk.py`
- skill `lk-stock` reference `gate-b1-crosswalk-local-persistence-pattern-20260609.md`

## Probe de correção

Reexecutei `B75806` após a correção.

DB probe:

- `areas/lk/sub-areas/stock/data/gate_b2_duplicate_shopify_fix_probe_20260609T122537Z.db`

Resultado:

```json
{
  "total_rows": 8,
  "matched_exact_sku_stock_resolved": 7,
  "shopify_duplicate_sku_blocked": 1,
  "unresolved_or_blocked": 1,
  "writes_externos": 0
}
```

Linha bloqueada:

```json
{
  "sku":"B75806",
  "mapping_status":"shopify_duplicate_sku_blocked",
  "availability_claim_allowed":0,
  "issue_reason":"Shopify retornou mais de uma variant ativa com o mesmo SKU; bloquear disponibilidade até saneamento da grade/SKU."
}
```

## Verificação

Comando:

```bash
python3 -m unittest discover -s areas/lk/sub-areas/stock/evaluation -p 'test_*.py'
```

Resultado:

```text
Ran 20 tests in 3.322s
OK
```

## Status operacional

Gate B.2 avançou, mas o shard 1 inicial deve ser tratado como evidência de carga e descoberta, não como resultado final de saneamento, porque foi executado antes da regra `shopify_duplicate_sku_blocked`.

Próximo passo recomendado: reexecutar o shard 1 inteiro com a correção nova e então continuar shards 2+ do catálogo ativo.
