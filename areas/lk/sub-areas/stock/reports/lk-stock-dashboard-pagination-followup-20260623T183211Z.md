# LK Stock Dashboard — Detail pagination follow-up

Data UTC: 2026-06-23T18:32:11Z

## Escopo

Continuação após o detail server-side: adicionar navegação explícita de páginas na UI para que o dashboard percorra o universo filtrado por `/api/estoque/detail` sem recarregar a base inteira.

## Mudança aplicada

- Adicionado bloco `stockPagination` na toolbar do dashboard.
- Botões `Anterior` e `Próxima` (`stockPrevPage`, `stockNextPage`) chamam `navegarPaginaEstoque(-1/+1)`.
- Nova função `atualizarPaginacaoEstoque()` mostra `Página atual/total · resultados` e desabilita botões nos limites.
- Nova função `navegarPaginaEstoque(delta)` calcula `nextPage` e chama `carregarDetalheEstoque({ page: nextPage })`.
- A paginação é atualizada após bootstrap inicial e após cada fetch server-side de detalhe.

## Evidência TDD / testes

- RED: teste HTML novo falhou exigindo `id="stockPagination"`, `stockPrevPage`, `stockNextPage`, `function atualizarPaginacaoEstoque`, `function navegarPaginaEstoque` e chamada `carregarDetalheEstoque({ page: nextPage })`.
- GREEN: UI implementada.
- `node --test test/app.test.js --test-name-pattern 'Dashboard HTML'` — `13/13` passou no subset executado.
- `npm test` — `38/38` passou.
- Adapter Python: `python3 -m unittest areas/lk/sub-areas/stock/evaluation/test_stock_api_adapter.py` — `11/11` passou.
- `git diff --check` — passou.
- `npx --yes impeccable detect --json src/public src/index.js` — `[]`.

## Produção / smoke

Smoke autenticado no container `lk-estoque-web` após hot patch:

```json
{
  "htmlStatus": 200,
  "hasPagination": true,
  "hasPrev": true,
  "hasNext": true,
  "hasNavigate": true,
  "hasNextPageCall": true,
  "page1": 1,
  "page2": 2,
  "totalPages": 174,
  "page1Rows": 5,
  "page2Rows": 5,
  "differentFirstSku": true,
  "totalFiltered": 870,
  "unauth": 401
}
```

## Git / deploy / rollback

- Commit: `cd459349140213ac7ef849cb7825b02d57c66124` — `Add stock dashboard detail pagination controls`.
- Branch remoto: `feat/stock-os-api-adapter`, SHA local=remoto verificado.
- Rollback pré-deploy: `lk-estoque-web-web:rollback-pre-dashboard-pagination-20260623T183211Z` (`sha256:9972bcb99287...`).
- Imagem pós-deploy: `lk-estoque-web-web:stock-dashboard-pagination-20260623T183211Z` (`sha256:77b4a3f7ad22...`).

## Guardrails

- Tiny write: `0`.
- Shopify write: `0`.
- Notion write: `0`.
- Compra/fornecedor/reserva/cliente: `0`.
- Promessa pública de disponibilidade: `0`.
- Secrets impressos: `false`.

## Próximo gap opcional

A paginação já percorre o universo filtrado por quick filter/busca. Próxima melhoria natural: mover facetas de marca/tamanho/cor para query server-side ou expor facet counts globais no endpoint detail/bootstrap.