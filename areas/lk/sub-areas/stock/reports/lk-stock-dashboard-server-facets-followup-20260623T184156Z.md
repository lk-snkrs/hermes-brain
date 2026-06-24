# LK Stock Dashboard — Server-side facets follow-up

Data UTC: 2026-06-23T18:41:56Z

## Escopo

Lucas pediu “FAZER TODOS OS GAPS OPCIONAIS”. Depois de bootstrap summary-first, detail server-side e paginação, o gap restante era tirar marca/tamanho/cor/silhueta do escopo limitado da página carregada e expor facetas globais pelo endpoint server-side.

## Mudança aplicada

- `/api/estoque/detail` e `/api/estoque/bootstrap` agora carregam `facets` no detail:
  - `facets.brands.byBrand`, `orderedBrands`, `totalAvailableProducts`, `totalAvailableUnits`, `brandsWithStock`;
  - `facets.silhouettesByBrand`;
  - `facets.sizes`;
  - `facets.colors`.
- `/api/estoque/detail` aceita filtros server-side:
  - `marca`;
  - `silhueta`;
  - `tamanho`;
  - `cor`;
  - além de `quickFilter`, `q`, `page`, `pageSize`.
- A UI agora envia `marcaAtiva`, `silhuetaAtiva`, `tamanhoAtivo` e `corAtiva` em `montarParametrosDetalheEstoque()`.
- Sidebar usa `stockDetailAtual.facets` para counts globais em vez de depender só da página carregada.
- Tamanho/cor usam facet counts server-side com fallback local.
- Cliques de marca/silhueta/tamanho/cor chamam `carregarDetalheEstoque({ page: 1 })`.
- `stock-os.js` passou a preservar `cor` e `silhueta` vindas da Stock OS e derivar cor do nome quando a fonte não traz campo explícito.

## Evidência TDD / testes

- RED: teste API passou a exigir `filters` completos (`marca/silhueta/tamanho/cor`), facets e filtro combinado `quickFilter=available&marca=adidas&silhueta=Samba&tamanho=41&cor=branco`.
- RED: teste HTML passou a exigir envio de `marca`, `silhueta`, `tamanho`, `cor` no detail e uso de `stockDetailAtual.facets`.
- GREEN: API + UI implementadas.
- `node --test test/app.test.js --test-name-pattern 'paginated stock detail|Dashboard HTML'` — passou.
- `npm test` — `38/38` passou.
- Adapter Python: `python3 -m unittest areas/lk/sub-areas/stock/evaluation/test_stock_api_adapter.py` — `11/11` passou.
- `git diff --check` — passou.
- `npx --yes impeccable detect --json src/public src/index.js src/stock-os.js` — `[]`.

## Produção / smoke

Smoke autenticado no container `lk-estoque-web` após hot patch:

```json
{
  "htmlStatus": 200,
  "htmlHasFacetState": true,
  "htmlSendsMarca": true,
  "htmlSendsSilhueta": true,
  "htmlSendsTamanho": true,
  "htmlSendsCor": true,
  "detailStatus": 200,
  "brandCount": 12,
  "sizeCount": 54,
  "colorCount": 44,
  "totalFiltered": 870,
  "brandFilterStatus": 200,
  "brandFilter": "outros",
  "brandFilterRows": 5,
  "sizeFilterStatus": 200,
  "sizeFilter": "20",
  "sizeFilterRows": 2,
  "colorFilterStatus": 200,
  "colorFilter": "Preto",
  "colorFilterRows": 5,
  "unauth": 401
}
```

## Git / deploy / rollback

- Commits:
  - `2f37fe4b6b8daf261027ece832ede297677831f5` — `Serve stock dashboard facets from detail API`.
  - `0f190bc5a730f10d4f88fba2b9cbf5605cb53fbe` — `Derive stock color facets from product names`.
- Branch remoto: `feat/stock-os-api-adapter`, SHA local=remoto verificado em `0f190bc5a730f10d4f88fba2b9cbf5605cb53fbe`.
- Rollback pré-deploy final: `lk-estoque-web-web:rollback-pre-dashboard-facets-color-20260623T184156Z` (`sha256:b9dcbe6f9c7c...`).
- Imagem pós-deploy final: `lk-estoque-web-web:stock-dashboard-facets-color-20260623T184156Z` (`sha256:0e7622d87a02...`).

## Guardrails

- Tiny write: `0`.
- Shopify write: `0`.
- Notion write: `0`.
- Compra/fornecedor/reserva/cliente: `0`.
- Promessa pública de disponibilidade: `0`.
- Secrets impressos: `false`.

## Status dos gaps opcionais conhecidos

- Bootstrap summary-first: concluído.
- Detail server-side para quick filter/busca: concluído.
- Paginação explícita server-side: concluído.
- Facets globais + filtros server-side para marca/silhueta/tamanho/cor: concluído.

Não ficou gap opcional conhecido aberto dentro da sequência atual do Dashboard Estoque.