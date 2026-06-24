# LK Stock Dashboard — Server-side detail follow-up

Data UTC: 2026-06-23T18:22:51Z

## Escopo

Continuação após o bootstrap summary-first: conectar interações da UI (quick filter e busca) ao endpoint paginado `/api/estoque/detail`, evitando depender só do subconjunto inicial carregado no browser.

## Mudança aplicada

- Busca do campo `searchInput` agora chama `agendarDetalheEstoque()` com debounce de 250ms.
- Quick filters e toggle de estoque positivo agora chamam `carregarDetalheEstoque({ page: 1 })`.
- Nova função `montarParametrosDetalheEstoque()` monta `page`, `pageSize`, `quickFilter` e `q`.
- Nova função `carregarDetalheEstoque()` chama `/api/estoque/detail?...`, atualiza `stockDetailAtual`, `todosOsProdutos`, sidebar/filtros locais e renderização.
- `resultCount` passa a mostrar página atual vs. `totalFiltered` retornado pelo servidor.

## Evidência TDD / testes

- RED: teste HTML novo falhou exigindo `function carregarDetalheEstoque`, fetch para `/api/estoque/detail`, `oninput="agendarDetalheEstoque()"` e quick filter chamando `carregarDetalheEstoque({ page: 1 })`.
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
  "hasDetailFunction": true,
  "hasServerFetch": true,
  "hasDebounce": true,
  "p0Status": 200,
  "p0Total": 4,
  "p0Rows": 4,
  "p0FilteredSummary": true,
  "searchStatus": 200,
  "searchQ": "9060",
  "searchRows": 5,
  "unauth": 401
}
```

## Git / deploy / rollback

- Commit: `2cd4e66810a6086d69a9921e74b55c1559e16c03` — `Fetch stock detail server-side from dashboard filters`.
- Branch remoto: `feat/stock-os-api-adapter`, SHA local=remoto verificado.
- Rollback pré-deploy: `lk-estoque-web-web:rollback-pre-dashboard-server-detail-20260623T182251Z` (`sha256:c2196c8d31b6...`).
- Imagem pós-deploy: `lk-estoque-web-web:stock-dashboard-server-detail-20260623T182251Z` (`sha256:3f734306da9e...`).

## Guardrails

- Tiny write: `0`.
- Shopify write: `0`.
- Notion write: `0`.
- Compra/fornecedor/reserva/cliente: `0`.
- Promessa pública de disponibilidade: `0`.
- Secrets impressos: `false`.

## Próximo gap opcional

A navegação já usa detail server-side para busca/quick filters. Próxima melhoria natural: adicionar paginação explícita “próxima/anterior” na UI e/ou mover filtros de marca/tamanho/cor para query server-side para cobrir 100% do universo com facetas globais.