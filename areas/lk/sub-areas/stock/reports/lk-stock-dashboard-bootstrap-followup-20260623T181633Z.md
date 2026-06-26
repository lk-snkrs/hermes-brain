# LK Stock Dashboard — Bootstrap summary-first follow-up

Data UTC: 2026-06-23T18:16:33Z

## Escopo

Continuação após o follow-up dos 5 audits: atacar o próximo gap documentado — reduzir o payload inicial do dashboard sem perder visão operacional global.

## Mudança aplicada

- Criado endpoint protegido `/api/estoque/bootstrap`.
- O endpoint carrega a Stock OS uma vez e devolve:
  - `summary`: resumo global da base completa;
  - `detail`: primeira página filtrada/paginada, por padrão `quickFilter=available&pageSize=500`.
- A UI deixou de fazer `fetch('/api/estoque')` no carregamento inicial.
- A UI passou a carregar `/api/estoque/bootstrap?page=1&pageSize=500&quickFilter=available`.
- Cards de overview e métricas operacionais usam `stockSummaryAtual` para preservar contagens globais mesmo com lista inicial reduzida.
- `/api/estoque/detail` continua disponível para filtros/paginação e agora reaproveita helper comum `buildStockDetailPayload`.

## Evidência TDD / testes

- RED inicial: teste novo falhou porque `/api/estoque/bootstrap` não existia e a UI ainda chamava `fetch('/api/estoque')`.
- GREEN: implementado endpoint + UI bootstrap.
- `node --test test/app.test.js --test-name-pattern 'paginated stock detail|Dashboard HTML'` — `13/13` passou no subset executado.
- `npm test` — `38/38` passou.
- Adapter Python: `python3 -m unittest areas/lk/sub-areas/stock/evaluation/test_stock_api_adapter.py` — `11/11` passou.
- `git diff --check` — passou.
- `npx --yes impeccable detect --json src/public src/index.js` — `[]`.

## Produção / smoke

Smoke autenticado no container `lk-estoque-web` após hot patch:

```json
{
  "bootstrapStatus": 200,
  "unauth": 401,
  "bootstrapRows": 500,
  "bootstrapTotalFiltered": 870,
  "bootstrapSummaryTotal": 12592,
  "bootstrapBytes": 531458,
  "legacyRows": 12592,
  "legacyBytes": 13491393,
  "byteRatio": 0.039,
  "p0FilteredSummary": true,
  "p0": 4
}
```

Interpretação:

- Bootstrap inicial entrega `500` linhas disponíveis de `870` filtradas, com resumo global `12.592` linhas.
- Payload inicial caiu para aproximadamente `3,9%` do endpoint legado completo medido no mesmo container.
- Auth preservado: sem senha retorna `401`.
- Contrato P0/filteredSummary preservado.

## Git / deploy / rollback

- Commit: `79446a68e9ecadd0bee8e1c7ff493f73d77d03cc` — `Load stock dashboard from bootstrap payload`.
- Branch remoto: `feat/stock-os-api-adapter`, SHA local=remoto verificado.
- Rollback pré-deploy: `lk-estoque-web-web:rollback-pre-dashboard-bootstrap-20260623T181633Z` (`sha256:e68ae6ff0ab6...`).
- Imagem pós-deploy: `lk-estoque-web-web:stock-dashboard-bootstrap-20260623T181633Z` (`sha256:7c02cb0f884...`).

## Guardrails

- Tiny write: `0`.
- Shopify write: `0`.
- Notion write: `0`.
- Compra/fornecedor/reserva/cliente: `0`.
- Promessa pública de disponibilidade: `0`.
- Secrets impressos: `false`.

## Próximo gap opcional

A UI agora reduz muito a carga inicial, mas ainda usa filtros client-side sobre a página carregada. Próxima melhoria natural: conectar mudanças de quick filter/busca/página ao `/api/estoque/detail` server-side para navegar todo o universo sem recarregar a base completa.
