# Receipt — Production Promotion Vomero Search + Size Guide Black70 — 2026-06-16

## Aprovação

Lucas solicitou: `fazer merge para production` após aprovar o comportamento em DEV.

## Fluxo usado

Seguindo a regra de Production via GitHub, a promoção foi feita por PR scoped a partir de `production`, não por write direto no tema Production via Asset API.

Repo:

- `lk-snkrs/lk-new-theme`

PR:

- PR #82: `https://github.com/lk-snkrs/lk-new-theme/pull/82`
- Branch: `promote/vomero-search-sizeguide-production-20260616`
- Base: `production`
- State: `MERGED`
- Merge commit: `d72c763aa4113babc751f2d273ff6f3e10c2da0f`
- Merged at: `2026-06-16T16:46:47Z`

## Escopo promovido

Apenas dois arquivos:

- `sections/lk-search.liquid`
- `sections/lk-pdp.liquid`

Sem alteração de produto, SEO fields, preço, estoque, campanha, app ou GMC.

## Shopify Production readback

Production theme:

- Theme: `lk-new-theme/production`
- Theme id: `155065417950`
- Role: `main`

Readback Production pós-merge:

- `sections/lk-search.liquid`
  - sha256: `b1063d65e2ca0f6dfbc0867443ec39f419e9a55b9c41247e02591d9c8a676e55`
  - matches approved DEV target: `true`
  - bytes: `38992`
- `sections/lk-pdp.liquid`
  - sha256: `006dcb8fe9e83c996514e60eb77ca1dd0e2dabf16cfa259df7b424a787362b0e`
  - matches approved DEV target: `true`
  - bytes: `167005`

GitHub production content SHAs pós-merge:

- `sections/lk-search.liquid`: `8e971991674973923b2b63ebad4c9c8ef4e0e69a`
- `sections/lk-pdp.liquid`: `c1579b821ae9ca32acaa2218efae534d177f4cc4`

## QA live Production

Script:

`/tmp/lkqa-cdp/prod_vomero_sizeguide_black70_qa_20260616.js`

Resultado:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/prod-vomero-sizeguide-black70-qa-20260616/prod-vomero-sizeguide-black70-results.json`

Screenshot:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/prod-vomero-sizeguide-black70-qa-20260616/prod-vomero-sizeguide-black70.jpg`

Viewport:

- mobile `390x844`

### Busca

- `vomero` → `Ver coleção: Nike Vomero Premium` — OK
- `vômero` → `Ver coleção: Nike Vomero Premium` — OK
- `vomero premium` → `Ver coleção: Nike Vomero Premium` — OK
- `vomero 5` → `Ver coleção: Nike Vomero 5` + `Nike Vomero Premium` — OK/observação

Todos:

- Liquid errors: `0`
- overflow horizontal: `false`

### Guia de Tamanhos / backdrop

PDP testado:

- `https://lksneakers.com.br/products/tenis-nike-vomero-premium-black-volt-preto`

Resultado:

- modal aberto: `true`
- `aria-hidden=false`
- modal background: `rgba(0, 0, 0, 0.7)`
- backdrop background: `rgba(0, 0, 0, 0.7)`
- backdrop position: `fixed`
- painel branco começa em `top=58px`
- ponto no topo (`y=20`) retorna `.sg-modal__backdrop`, não PDP atrás
- Liquid errors: `0`
- overflow horizontal: `false`
- copy Vomero Premium preservada: `true`

## Links live

Busca:

- `https://lksneakers.com.br/search?type=product&q=vomero`
- `https://lksneakers.com.br/search?type=product&q=v%C3%B4mero`
- `https://lksneakers.com.br/search?type=product&q=vomero%20premium`
- `https://lksneakers.com.br/search?type=product&q=vomero%205`

PDPs:

- `https://lksneakers.com.br/products/tenis-nike-vomero-premium-black-volt-preto`
- `https://lksneakers.com.br/products/tenis-nike-mind-002-sail-bege`

## Rollback

Rollback recomendado via GitHub:

1. Reverter merge commit `d72c763aa4113babc751f2d273ff6f3e10c2da0f` em branch nova a partir de `production`.
2. Abrir PR de rollback para `production`.
3. Aguardar sync/deploy para Shopify Production.
4. Confirmar readback dos dois assets e QA live.

Alternativa emergencial somente com aprovação explícita: reverter os dois assets via backup/Asset API direto no Production theme.

## Status final

- PR scoped criado e mergeado.
- Shopify Production sincronizado.
- Readback Production bate com DEV aprovado.
- QA live Production passou.
