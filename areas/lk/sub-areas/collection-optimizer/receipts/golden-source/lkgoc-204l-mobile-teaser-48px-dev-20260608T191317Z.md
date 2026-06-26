# Receipt — LKGOC 204L mobile teaser 48px

Data UTC: 20260608T191317Z
Status: concluído em GitHub dev + Shopify DEV/unpublished

## Pedido Lucas
Mostrar aproximadamente 20px a mais de imagem; o ajuste de 28px estava curto demais.

## Execução
- `layout/theme.liquid`
  - collapsed teaser: 28px → 48px
  - card: 84px → 104px
  - translate: -42px/-28px → -36px/-20px conforme seletor
- `sections/lk-collection.liquid`
  - regra-base 204L: max-height 28px → 48px
- Commit dev: `f634dff` — `fix(lkgoc): increase NB 204L mobile teaser strip`

## Shopify DEV/unpublished
- Tema: `lk-new-theme/dev`
- ID: `155065450718`
- Role: `unpublished`
- Production/main: não alterado

## QA real via Chromium/CDP
Viewport: 575x900
- Collage rect height: 48
- Computed height: 48px
- Computed max-height: 48px
- Card rect height: 104
- Card max-height: 104px
- Transform: `matrix(... -36)`
- Screenshot: `/opt/data/profiles/lk-collection-optimizer/output/204l-mobile-audit/204l-mobile-shopify-dev-teaser-48px-575-20260608.png`
