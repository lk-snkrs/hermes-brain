# Dashboard Estoque — Superpowers 5 Audits sequenciais

Data: 2026-06-23T17:04:00Z
Agente: lk-stock
Escopo: estoque.lkskrs.online / LK-Estoque-Web-inicial / Stock OS adapter

## Objetivo

Executar cinco ciclos sequenciais de audit + melhoria usando Superpowers, cobrindo backend/API, frontend/UX, contrato Stock OS, DB/read model, testes, deploy e guardrails.

## Audit 1 — filtros operacionais do cockpit

Evidência: produção tinha `/api/estoque/detail?quickFilter=p0` retornando centenas de itens disponíveis por cair no fallback `available`, em vez dos P0 reais.

Correção:
- `applyQuickFilter()` passou a suportar `p0`, `p1`, `p2`, `p3`, `identity`, `not-consult-safe` e `positive-blocked`.
- Teste regressivo adicionado em `test/dashboard-utils.test.js`.

Resultado esperado em produção após deploy:
- `p0=4`, `p1=13`, `p2=1`, `identity=980`.

## Audit 2 — mudanças canônicas via ledger

Evidência: `summary.changes` era derivado de campos por linha do feed; o Stock OS já expõe `movement_summary` derivado do `tiny_full_sync_item_ledger`.

Correção:
- `src/index.js` ganhou `buildStockSummaryResponse()`.
- Summary agora inclui `ledgerChanges`/`canonicalChanges` e `freshness` consolidado.
- Teste regressivo em `test/app.test.js`.

## Audit 3 — separar filas gerais de filas scored

Evidência: `summary.actionQueues.P3=12574` misturava linhas não pontuadas com linhas realmente avaliadas pelo `current_stock_scored`. DB direta mostrava `current_stock_scored`: P0=4, P1=13, P2=1, P3=885.

Correção:
- Adapter Python expõe `scored_in_stock_os`.
- Frontend preserva `scored_in_stock_os`.
- Summary expõe `scoredRows`, `unscoredRows` e `scoredActionQueues`.
- Testes regressivos em Python e Node.

## Audit 4 — estoque observado bruto em linhas bloqueadas

Evidência: linhas bloqueadas não devem confirmar `quantity_lk_controle_estoque`, mas o cockpit precisa enxergar estoque observado bruto para fila de qualidade.

Correção:
- Adapter mantém `quantity_lk_controle_estoque=null` quando não confirmado.
- Adapter passa a expor `observed_stock_quantity` e `raw_stock_quantity_max_observed`.
- Frontend normaliza `estoque_observado_raw`.
- `positiveBlockedRows` usa observado bruto sem liberar disponibilidade pública.

## Audit 5 — filtro positive-blocked alinhado ao summary

Evidência: o summary usava estoque observado bruto, mas o filtro `positive-blocked` ainda olhava apenas `estoque` seguro, podendo ocultar exatamente as 4 linhas bloqueadas com estoque observado.

Correção:
- Criado helper compartilhado `observedStock()` em `dashboard-utils.js`.
- `positive-blocked` agora usa `observedStock()`.
- Summary usa o mesmo helper, removendo divergência entre métrica e filtro.

## Verificações executadas

- `npm test`: 38/38 passou.
- `python3 -m unittest areas/lk/sub-areas/stock/evaluation/test_stock_api_adapter.py`: 11/11 passou.
- `git diff --check`: passou.
- `npx --yes impeccable detect --json src/public src/index.js`: `[]`.
- GitHub dashboard: local SHA = remoto.
- GitHub Brain: local SHA = remoto.
- Smoke produção autenticado:
  - `/api/estoque/summary`: HTTP 200.
  - `/api/estoque/detail?...`: HTTP 200.
  - sem auth: HTTP 401.

## Smoke produção pós-deploy

- total: 12592
- stock_os_total_count: 12592
- stock_os_result_count: 12592
- stock_os_truncated: false
- source_observed_at_max: 2026-06-23T16:20:45Z
- latest_sync_finished_at: 2026-06-23T16:46:32Z
- scoredRows: 903
- unscoredRows: 11689
- scoredActionQueues: P0=4, P1=13, P2=1, P3=885
- filters: p0=4, p1=13, p2=1, identity=980, positive-blocked=4, negative=39
- quality: negativeRows=39, notLocalConsultSafe=351, identityBlocked=980, positiveBlockedRows=4
- thumbnails: 12592/12592, coverage 100%

## Commits

- Dashboard `LK-Estoque-Web-inicial`: `6d2b8aa7a7d74abe7a2d976883307d70ea194546`
- Brain `hermes-brain`: `564a443c24439d82cc7cbfb91e293331e0fede29`

## Deploy / rollback

Rollback images:
- `lk-estoque-web-web:rollback-pre-5audits-20260623T170400Z`
- `lk-estoque-stock-api:rollback-pre-5audits-20260623T170400Z`

New images:
- `lk-estoque-web-web:stock-dashboard-5audits-20260623T170400Z`
- `lk-estoque-stock-api:stock-dashboard-5audits-20260623T170400Z`

## Guardrails

- Tiny write: 0
- Shopify write: 0
- Notion write: 0
- compra/fornecedor: 0
- contato cliente: 0
- promessa pública de disponibilidade: 0
- secrets impressos: false

## Pendências reais

- A UI ainda carrega o feed completo em `/api/estoque`; existe endpoint detail/summary, mas a migração completa da primeira carga para summary-first/lazy detail é uma próxima fase maior de performance/arquitetura.
- As 980 linhas com identidade bloqueada e 351 não consultáveis seguem como fila de saneamento; o dashboard agora as mede/filtra melhor, mas não corrige Tiny/Shopify sem aprovação escopada.
