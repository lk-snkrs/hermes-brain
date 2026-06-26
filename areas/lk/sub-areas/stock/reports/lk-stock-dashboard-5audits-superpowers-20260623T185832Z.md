# LK Stock Dashboard — 5 ciclos Superpowers audit + melhoria

Data UTC: 2026-06-23T18:58:32Z

## Pedido

Executar 5 ciclos sequenciais completos de audit + melhoria no Dashboard Estoque (`estoque.lkskrs.online` / Stock OS), cobrindo backend, frontend, API, DB/Stock OS, UX, performance, segurança, contrato de dados, filtros, freshness, filas P0/P1/P2, qualidade da base e testes. Guardrails: Tiny write 0, Shopify write 0, Notion write 0, compra/reserva/cliente/public availability 0.

## Baseline auditado antes dos ciclos

Produção/container `lk-estoque-web` e DB Stock OS atual:

- `current_local_stock`: 12.592 linhas.
- `current_stock_scored`: 903 linhas.
- Filas scored DB: P0=4, P1=13, P2=1, P3=885.
- API `/api/estoque/summary`: HTTP 200 autenticado; HTTP 401 sem auth.
- `stock_os_total_count=12592`, `stock_os_result_count=12592`, `stock_os_truncated=false`.
- Freshness: `sourceObservedAtMin=2026-06-12T00:53:54Z`, `sourceObservedAtMax=2026-06-23T16:20:45Z`, `latestSyncFinishedAt=2026-06-23T16:46:32Z`.
- Qualidade: `notLocalConsultSafe=351`, `identityBlocked=980`, `negativeRows=39`, `positiveBlockedRows=4`.
- Guardrails API: Tiny write 0, Shopify write 0, external writes 0, public availability 0, availability claim 0.

## Ciclo 1 — Performance backend/API

### Audit

Cada endpoint protegido (`summary`, `detail`, `bootstrap`) fazia nova leitura upstream completa da Stock OS API. Baseline live mostrou chamadas de detail/summary em ~1,9s–2,9s quando não havia cache quente.

### RED

Adicionado teste `Stock OS feed cache avoids repeated upstream reads across dashboard endpoints within TTL` exigindo que `summary` seguido de `detail` use apenas 1 chamada upstream e exponha `stock_os_cache.status` (`miss` depois `hit`). O teste falhou com `upstreamCalls=2`.

### Fix

Implementado cache em memória de feed Stock OS com TTL configurável (`STOCK_OS_FEED_CACHE_TTL_MS`, default 30s) em `carregarEstoqueStockOs()`.

### GREEN

Teste focado passou. Full suite final passou.

## Ciclo 2 — Contrato de filtros

### Audit

`applyQuickFilter()` caía para `available` quando recebia filtro desconhecido, mas `/api/estoque/detail` preservava o texto desconhecido em `filters.quickFilter`. Isso gerava contrato ambíguo: a resposta dizia um filtro, mas aplicava outro.

### RED

Teste em `/api/estoque/detail?quickFilter=does-not-exist` exigiu:

- `filters.requestedQuickFilter='does-not-exist'`;
- `filters.quickFilter='available'`;
- `filterWarnings=['unknown_quick_filter_fell_back_to_available']`.

O teste falhou porque o contrato não existia.

### Fix

Criado `VALID_STOCK_QUICK_FILTERS` + `normalizeQuickFilter()`. O endpoint agora torna explícito o fallback seguro.

### GREEN

Teste focado passou. Full suite final passou.

## Ciclo 3 — UX/paginação API

### Audit

Quando a UI/API solicitava `page` acima de `totalPages`, a API retornava página vazia mantendo `page=99`. Isso podia gerar tela vazia apesar de haver itens no filtro.

### RED

Teste em `/api/estoque/detail?page=99&pageSize=2&q=tenis` exigiu clamp para última página: `page=2`, `totalPages=2`, `produtos.length=2`. Falhou com `page=99`.

### Fix

`buildStockDetailPayload()` agora calcula `totalPages`, limita `page` para `boundedPage` e fatia pelo índice da página válida.

### GREEN

Teste focado passou. Full suite final passou.

## Ciclo 4 — Botão de atualização / freshness operacional

### Audit

Frontend tinha botão `Atualizar leitura` chamando `/api/sync`, mas o backend não tinha rota correspondente. Resultado: botão funcionalmente quebrado/sem contrato de refresh, especialmente depois do cache.

### RED

Teste exigiu `/api/sync` HTTP 200, `status=ok`, `stock_os_cache.status='refreshed'` e guardrails Tiny/Shopify `0`. Falhou antes da rota.

### Fix

Criada rota protegida `/api/sync` que invalida o cache local, relê Stock OS read-only e responde summary com `stock_os_cache.status='refreshed'`.

### GREEN

Teste focado passou. Smoke produção confirmou `/api/sync` 200 e cache `refreshed`.

## Ciclo 5 — Segurança/cache HTTP dos dados operacionais

### Audit

Endpoints `/api/*` não explicitavam `Cache-Control: no-store`. Como o dashboard carrega dados operacionais internos de estoque, o contrato de segurança deveria evitar cache por browser/proxy.

### RED

Teste em `/api/estoque/summary` exigiu header `Cache-Control` contendo `no-store`. Falhou com header vazio.

### Fix

Middleware pós-auth para `/api/*` adiciona:

- `Cache-Control: no-store, max-age=0`;
- `Pragma: no-cache`.

### GREEN

Teste focado passou. Smoke externo confirmou `noStore=true`.

## Verificação final local

Comandos executados:

```bash
npm test
python3 -m unittest areas/lk/sub-areas/stock/evaluation/test_stock_api_adapter.py
git diff --check
npx --yes impeccable detect --json src/public src/index.js src/stock-os.js
```

Resultados:

- `npm test`: 39/39 passou.
- Adapter Python: 11/11 passou.
- `git diff --check`: passou.
- `impeccable detect`: `[]`.

## Deploy / rollback / smoke produção

Rollback criado antes do hot patch:

- `lk-estoque-web-web:rollback-pre-5audit-hardening-20260623T185640Z`
- digest: `sha256:703f6994df564ad918aa9050be5f35dd0420c0eb64a607503f46c806acac29e3`

Deploy/hot patch:

- `docker cp src/index.js lk-estoque-web:/app/src/index.js`
- `docker restart lk-estoque-web`
- imagem pós-deploy: `lk-estoque-web-web:stock-dashboard-5audit-hardening-20260623T185640Z`
- digest pós-deploy: `sha256:b8d126fb8d4439cd5094cab5a7e7671000583713da7d91923f82a8a0d8f12568`
- `latest` retagueada para a imagem pós-deploy.

### Smoke interno container

```json
{
  "summary1": {
    "status": 200,
    "ms": 576,
    "cache": { "status": "hit", "ttl_ms": 30000 },
    "totalRows": 12592,
    "noStore": true,
    "truncated": false,
    "total": 12592,
    "result": 12592
  },
  "summary2": {
    "status": 200,
    "ms": 316,
    "cache": { "status": "hit", "ttl_ms": 30000 },
    "noStore": true
  },
  "p0": {
    "status": 200,
    "page": 2,
    "totalPages": 2,
    "totalFiltered": 4,
    "rows": 2,
    "actionQueues": { "P0": 4, "P1": 0, "P2": 0, "P3": 0 }
  },
  "invalid": {
    "status": 200,
    "filters": { "quickFilter": "available", "requestedQuickFilter": "does-not-exist" },
    "warnings": ["unknown_quick_filter_fell_back_to_available"],
    "rows": 5
  },
  "sync": {
    "status": 200,
    "cache": { "status": "refreshed", "ttl_ms": 30000 }
  },
  "positiveBlocked": { "status": 200, "totalFiltered": 4, "rows": 4 },
  "unauth": { "status": 401 }
}
```

### Smoke externo `https://estoque.lkskrs.online`

```json
{
  "health": { "status": 200, "ms": 194 },
  "summary": {
    "status": 200,
    "ms": 422,
    "cache": { "status": "hit", "ttl_ms": 30000 },
    "noStore": true,
    "totalRows": 12592,
    "truncated": false,
    "guardrails": {
      "tiny_write": 0,
      "shopify_write": 0,
      "writes_externos": 0,
      "public_availability_safe": 0,
      "availability_claim_allowed": 0
    }
  },
  "detail": { "status": 200, "totalFiltered": 4, "rows": 3 },
  "invalid": {
    "status": 200,
    "filters": { "quickFilter": "available", "requestedQuickFilter": "xpto" },
    "warnings": ["unknown_quick_filter_fell_back_to_available"]
  },
  "sync": { "status": 200, "cache": { "status": "refreshed", "ttl_ms": 30000 } },
  "unauth": { "status": 401 },
  "values_printed": false
}
```

## GitHub

Commit dashboard:

- `449eeb22a5bc469ba832abddea665c80a18aa471` — `Harden stock dashboard audit loop`.

Branch remoto:

- `feat/stock-os-api-adapter`.
- SHA local = SHA remoto verificado: `449eeb22a5bc469ba832abddea665c80a18aa471`.

## Guardrails preservados

- Tiny write: 0.
- Shopify write: 0.
- Notion write: 0.
- Compra/fornecedor: 0.
- Reserva/cliente/public availability: 0.
- Secrets impressos: false.

## Status final

Os 5 ciclos sequenciais foram concluídos com TDD, deploy com rollback, smoke interno+externo, commit+push e SHA remoto verificado.

Melhorias aplicadas: cache read-through seguro, contrato honesto para filtros inválidos, clamp de paginação, rota `/api/sync` real e headers `no-store` nos dados operacionais.