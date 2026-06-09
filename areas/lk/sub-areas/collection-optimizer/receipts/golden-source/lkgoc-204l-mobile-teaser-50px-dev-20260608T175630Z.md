# Receipt — LKGOC 204L mobile teaser 50px

Data UTC: 20260608T175630Z
Status: concluído em GitHub dev + Shopify DEV/unpublished

## Pedido Lucas
Mostrar menos a imagem no mobile collapsed: alterar teaser para `max-height:50px`.

## Execução
- Arquivo: `layout/theme.liquid`
- Alteração: `max-height:96px!important` → `max-height:50px!important`
- Commit dev: `8afd6b5` — `fix(lkgoc): tighten NB 204L mobile teaser height`

## Shopify DEV/unpublished
- Tema: `lk-new-theme/dev`
- ID: `155065450718`
- Push: sucesso
- Production/main: não alterado

## QA real
- Chromium com cookie preview confirmou:
  - theme dev: sim
  - role unpublished: sim
  - `max-height:50px`: sim
  - `max-height:96px`: não
- Screenshot: `/opt/data/profiles/lk-collection-optimizer/output/204l-mobile-audit/204l-mobile-shopify-dev-teaser-50px-20260608.png`
