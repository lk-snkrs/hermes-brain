# Audit Superpowers — Dashboard Estoque LK pós-correção

- Gerado em: 2026-06-23 16:17:05 UTC
- Escopo: `https://estoque.lkskrs.online`, Stock OS API adapter, DB local Stock OS, dashboard repo `LK-Estoque-Web-inicial`
- Modo: audit read-only pós-correção; nenhum deploy/write produtivo nesta auditoria
- Skills aplicadas: `superpowers`, `lk-stock`, `verification-before-completion`, referência `stock-control-dashboard-audit-pattern-20260612.md`

## Veredito

O dashboard passou do estado “lista de inventário parcialmente truncada” para um cockpit operacional utilizável: a produção agora lê a base completa, separa prioridade de saneamento de prioridade de ação e mostra a fila real P0/P1/P2 alinhada com `current_stock_scored`.

Ainda existem gaps importantes de produto/controle: metadata de freshness no nível API é enganosa por usar a primeira linha ordenada, thumbnails seguem ausentes no contrato, há 39 saldos negativos, 351 linhas não consultáveis localmente, 900 linhas com identidade não resolvida e a primeira carga ainda é pesada por trazer 12.592 linhas em vez de summary/detail paginado.

## Evidência coletada

### Produção

- `/health`: HTTP 200
- `/api/estoque/summary` autenticado: HTTP 200
- `/api/estoque/summary` sem auth: HTTP 401
- `/api/vendas/executive-summary` autenticado: HTTP 200
- `values_printed=false`

Produção `/api/estoque/summary`:

```json
{
  "status": "ok",
  "total": 12592,
  "stock_os_total_count": 12592,
  "stock_os_result_count": 12592,
  "stock_os_truncated": false,
  "stock_freshness": "tiny_full_sync_nightly",
  "source_observed_at": "2026-06-23T07:20:42Z",
  "summary": {
    "totalRows": 12592,
    "positiveRows": 870,
    "zeroOrNegativeRows": 11722,
    "negativeRows": 39,
    "totalUnits": 1286,
    "uniqueAvailableProducts": 425,
    "brandsWithStock": 12,
    "actionQueues": {"P0": 4, "P1": 13, "P2": 1, "P3": 12574},
    "brokenGrades": 373,
    "lowStockRows": 629,
    "demandNoStock": 17,
    "highDemandLowStock": 0,
    "identityBlocked": 980
  },
  "guardrails": {
    "tiny_write": 0,
    "shopify_write": 0,
    "writes_externos": 0,
    "public_availability_safe": 0,
    "availability_claim_allowed": 0
  }
}
```

Produção `/api/vendas/executive-summary`:

- `status=attention`
- `action_counts`: P0 `35`, P1 `3`, P2 `12`, total `50`
- `freshness.status=ok`
- `last_order_at=2026-06-23T03:26:48Z`
- guardrails: Tiny write `0`, Shopify write `0`, external write `0`, public availability promise `0`, auto purchase `0`

### DB Stock OS atual

- DB: `areas/lk/sub-areas/stock/data/lk_stock_os_current_tiny_full_sync_20260623T152044Z.db`
- Tamanho: `129.15 MB`
- `current_local_stock`: `12.592` linhas
- Estoque positivo bruto DB: `874` linhas / `1290` unidades
- Estoque positivo local-consult-safe: `870` linhas / `1286` unidades
- Diferença: 4 linhas positivas existem na DB mas são bloqueadas para consulta local segura (`local_consult_safe=0`), então o dashboard corretamente não as trata como estoque operacional confirmado.
- Zero: `11.679` linhas
- Negativo: `39` linhas
- `local_consult_safe=1`: `12.241`
- `identity_resolved_safe=1`: `11.692`
- `public_availability_safe_sum=0`
- `availability_claim_allowed_sum=0`

Último Tiny full sync:

- `run_id=20260623T152044Z`
- `started_at=2026-06-23T15:20:50Z`
- `finished_at=2026-06-23T15:46:35Z`
- `rows_scanned=975`
- `rows_updated=975`
- `rows_failed=0`
- `rows_skipped=0`
- `status=ok`
- `tiny_write=0`, `shopify_write=0`, `writes_externos=0`

`current_stock_scored`:

- total: `903`
- P0: `4`
- P1: `13`
- P2: `1`
- P3: `885`

`demand_signals_stock_os`:

- linhas: `352`
- `units_signal=3486`
- `store_units_signal=1444`

### Adapter/API payload direto

`lookup_stock('all', limit=20000)`:

- `status=confirmado`
- `total_count=12592`
- `result_count=12592`
- `truncated=false`
- `action_priority_counts`: P0 `4`, P1 `13`, P2 `1`, P3 `12574`
- `with_operational_score=18`
- `with_demand=18`
- `with_thumbnail=0`
- `public_availability_safe_sum=0`
- `availability_claim_allowed_sum=0`

Top sanity/saneamento separado de decisão:

- `PENDING_CATALOG_BACKFILL`: 8792
- `P2_saneamento`: 2440
- `P1_saneamento`: 1134
- `P0_saneamento`: 108
- outros POS/Tiny gaps: menor volume

Isso confirma que a correção crítica funcionou: a prioridade de ação já não é inflada pelos estados de saneamento.

### Runtime/Git

- Container `lk-estoque-web`: up
- Container `lk-estoque-stock-api`: up/healthy
- Dashboard repo último commit: `b419a02 Fix Stock OS dashboard feed limit`
- Worktree do dashboard: somente `.hermes/` não rastreado, contendo backups antigos de Impeccable.

## Verificações executadas

- `npm test` no dashboard: 36/36 passou
- `python3 -m unittest areas/lk/sub-areas/stock/evaluation/test_stock_api_adapter.py`: 10/10 passou
- `npx --yes impeccable detect --json src/public src/index.js`: `[]`

## Achados por severidade

### P0 — nenhum blocker crítico encontrado nesta rodada

Os dois problemas críticos do audit anterior estão corrigidos em produção:

1. `stock_os_truncated=false`, com 12.592/12.592 linhas no payload.
2. `actionQueues` do dashboard agora batem com a fila real do score: P0 `4`, P1 `13`, P2 `1`.

Guardrails de segurança também estão preservados em `0`.

### P1 — metadata de freshness da API é enganosa

Produção mostra `source_observed_at=2026-06-23T07:20:42Z`, mas a DB atual tem `max(source_observed_at)=2026-06-23T15:20:44Z` e o Tiny full sync terminou `15:46:35Z`.

Causa observada: o adapter usa `first.get("source_observed_at")` da primeira linha ordenada por prioridade, não um max/min/summary global. Como as primeiras linhas são P0, esse campo pode parecer mais velho que o snapshot real.

Impacto: operador pode achar que o dashboard está stale quando parte da base está fresca. Recomendação: expor `source_observed_at_min`, `source_observed_at_max`, `latest_sync_finished_at` e/ou `freshness_summary` no payload.

### P1 — thumbnails continuam ausentes no contrato

`with_thumbnail=0` no payload do Stock OS adapter.

Impacto: UI continua dependente de fallback público por handle/card. Funciona como contingência, mas é mais lento/frágil para operação de loja.

Recomendação: cache/enrichment read-only de `thumbnail_url` no Stock OS/read model e métrica `% cardsWithThumbnail`.

### P1 — carga inicial ainda é pesada

O endpoint principal agora retorna a base completa (`12.592` linhas). Isso é correto para auditoria/controle, mas ainda não é ideal para UX/mobile.

Recomendação: próximo passo de arquitetura deve ser `summary` leve + endpoints paginados/detail, sem regredir cobertura completa.

### P1 — identidade/consulta segura ainda tem dívida operacional

- `identity_resolved_safe=11.692` de 12.592; ou seja, 900 linhas ainda sem identidade totalmente resolvida.
- `local_consult_safe=12.241`; 351 linhas ainda não consultáveis localmente.
- Existem 4 linhas com estoque positivo bruto, mas bloqueadas para consulta local segura.

A UI faz bem em não transformar isso em disponibilidade, mas o cockpit deve transformar esses casos em fila de saneamento, não deixar escondido.

### P1 — saldos negativos precisam de fila própria

DB e dashboard mostram `negativeRows=39`.

Impacto: estoque negativo é sinal de divergência operacional/sync/processo; deve virar fila `investigar negativo`, separada de compra/reposição.

### P2 — “Mudanças desde último sync” ainda deveria usar ledger

Há `tiny_full_sync_item_ledger` e sync recente, mas a análise ainda não confirmou painel de deltas completo: entrou estoque, saiu estoque, foi a zero, voltou positivo, ficou negativo.

Recomendação: derivar deltas do ledger/full sync, não de campo `previous_estoque` no feed.

## Estado estratégico

O dashboard agora tem base para ser sistema de controle de estoque, mas ainda não terminou essa transição.

- **Atendimento/loja:** bom o suficiente para busca interna protegida quando `local_consult_safe=1`, com guardrails públicos em zero.
- **Controle/compras:** a fila P0/P1/P2 está alinhada com o score real, mas compra/reposição ainda precisa de reconfirmação e regra de janelas D30/D90/D180 antes de qualquer Notion/compra.
- **Qualidade de base:** precisa de painel mais explícito para 351 não consultáveis, 900 identidade pendente e 39 negativos.
- **UX/performance:** precisa evoluir de feed completo para cockpit-first + detail paginado.

## Próximos passos recomendados

1. Corrigir metadata de freshness global no adapter/API.
2. Implementar `thumbnail_url` cacheado no contrato Stock OS.
3. Criar endpoint/detail paginado preservando summary completo.
4. Criar painel “Qualidade da base” com 351 não consultáveis, 900 identidade pendente e 39 negativos.
5. Criar painel “Mudanças desde último sync” com ledger do Tiny full sync.
6. Manter P0/P1/P2 como decisão interna: sem compra automática, sem Notion write, sem promessa pública.

## Writes nesta auditoria

- Tiny write: 0
- Shopify write: 0
- Notion write: 0
- Compra/fornecedor: 0
- Deploy/prod change: 0
- Public availability promise: 0
- Secrets printed: false
