# Receipt — LKGOC 204L mobile teaser 28px

Data UTC: 20260608T180351Z
Status: concluído em GitHub dev + Shopify DEV/unpublished

## Pedido Lucas
Ainda estava mostrando muita imagem. Reduzir mais o teaser collapsed.

## Execução
- `layout/theme.liquid`: teaser collapsed `max-height:28px`, card principal curto/deslocado.
- `sections/lk-collection.liquid`: regra-base 204L alinhada para `max-height:28px`.
- Commits dev:
  - `f11bc4f` — `fix(lkgoc): reduce NB 204L mobile teaser strip`
  - `c47d158` — `fix(lkgoc): align NB 204L base teaser height`

## Shopify DEV/unpublished
- Tema: `lk-new-theme/dev`
- ID: `155065450718`
- Push: sucesso
- Production/main: não alterado

## QA real
- Chromium com cookie preview confirmou:
  - theme dev: sim
  - role unpublished: sim
  - `max-height:28px`: 2 ocorrências
  - `transform:translateY(-28px)`: presente
- Screenshot: `/opt/data/profiles/lk-collection-optimizer/output/204l-mobile-audit/204l-mobile-shopify-dev-teaser-28px-v2-20260608.png`
