# LK Stock Dashboard — Follow-up 5 audits sequenciais

Data UTC: 2026-06-23T18:05:11Z

## Escopo

Pedido Lucas: continuar (`seguir`) a execução de ciclos sequenciais de audit + melhoria no Dashboard Estoque (`estoque.lkskrs.online` / Stock OS), preservando guardrails de read-only operacional.

## Resultado executivo

Foram fechados 5 ciclos de hardening incremental sobre a rodada já publicada dos 5 audits anteriores, com foco no cockpit operacional e nos filtros de decisão:

1. **Audit 1 — filtros operacionais visíveis na UI**
   - Gap: backend/utilitários já tinham filtros P0/P1/P2/identity/positive-blocked, mas a UI não oferecia botões explícitos para todos.
   - Melhoria: adicionados botões `P0 ação`, `P1 identidade`, `P2 monitorar`, `Identidade`, `Bloqueado c/ estoque`.
   - Teste: `test/app.test.js` valida presença dos `data-filter`.

2. **Audit 2 — resumo por filtro no endpoint detail**
   - Gap: `/api/estoque/detail` paginava, mas não devolvia o resumo do subconjunto filtrado.
   - Melhoria: `filteredSummary` e `filters` no payload, mantendo `summary` global.
   - Teste: detail com `q=tenis` valida `filteredSummary.totalRows` e `filteredSummary.quality.negativeRows`.

3. **Audit 3 — separação visual do score operacional**
   - Gap: o painel operacional precisava deixar mais claro o universo pontuado (`current_stock_scored`) vs. base total/unscored.
   - Melhoria: `buildOperationalAnalytics` expõe `scoredRows`, `unscoredRows`, `scoredActionQueues`; UI mostra `Score Stock OS` e usa fila P0 pontuada quando disponível.
   - Teste: `test/dashboard-utils.test.js` valida `scoredRows`, `unscoredRows` e `scoredActionQueues.P3`.

4. **Audit 4 — smoke de produção e contrato real**
   - Gap: produção ainda não refletia `filteredSummary` até hot patch/deploy.
   - Melhoria: deploy controlado no container `lk-estoque-web`, com rollback criado antes.
   - Smoke: `/api/estoque/detail?quickFilter=p0` agora retorna `hasFilteredSummary=true` e `filteredP0=4`.

5. **Audit 5 — verificação final, GitHub e imagem pós-deploy**
   - Testes: `npm test`, adapter Python, `git diff --check`, Impeccable.
   - GitHub: commit web `09d57c664579ae397635f55e628ce9309ab0daa7`, branch `feat/stock-os-api-adapter`, SHA remoto verificado.
   - Imagem pós-deploy: `lk-estoque-web-web:stock-dashboard-filtered-summary-20260623T180511Z`.

## Evidência de produção

Smoke autenticado no container `lk-estoque-web`:

```json
{
  "summaryStatus": 200,
  "unauth": 401,
  "total": 12592,
  "total_count": 12592,
  "truncated": false,
  "p0": 4,
  "scoredP0": 4,
  "detailP0": 200,
  "totalFilteredP0": 4,
  "hasFilteredSummary": true,
  "filteredP0": 4,
  "positiveBlocked": 4,
  "positiveBlockedSummary": 4
}
```

## Testes e gates

- Web: `npm test` — `38/38` passou.
- Adapter Python: `python3 -m unittest areas/lk/sub-areas/stock/evaluation/test_stock_api_adapter.py` — `11/11` passou.
- `git diff --check` — passou.
- `npx --yes impeccable detect --json src/public src/index.js` — `[]`.
- Produção: HTTP `200` autenticado e HTTP `401` sem auth.

## Commits / deploy / rollback

- Web commit: `09d57c664579ae397635f55e628ce9309ab0daa7` — `Expose dashboard operational filtered summaries`.
- Web branch remoto verificado: `feat/stock-os-api-adapter`, `match=yes`.
- Rollback pré-deploy: `lk-estoque-web-web:rollback-pre-dashboard-filtered-summary-20260623T180511Z` (`sha256:bc6aa33bc128...`).
- Imagem pós-deploy: `lk-estoque-web-web:stock-dashboard-filtered-summary-20260623T180511Z` (`sha256:1ab01794278f...`).

## Guardrails

- Tiny write: `0`.
- Shopify write: `0`.
- Notion write: `0`.
- Compra/fornecedor/reserva/cliente: `0`.
- Promessa pública de disponibilidade: `0`.
- Secrets impressos: `false`.

## Próximo gap opcional

A próxima melhoria arquitetural continua sendo migrar a primeira carga da UI para `summary-first + detail paginado/lazy`, reduzindo payload inicial sem perder visão operacional. Não foi executado nesta rodada para não alterar mais profundamente o comportamento da UI após os filtros/summary já publicados.
