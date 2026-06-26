# Receipt — LKGOC 204L mobile teaser force measured

Data UTC: 20260608T190909Z
Status: corrigido em GitHub dev + Shopify DEV/unpublished

## Problema
No print do DEV, o teaser ainda aparecia grande porque o primeiro fix estava limitado a `max-width:749px` e/ou não travava o card interno de forma suficiente para o viewport real.

## Correção
- Arquivo: `layout/theme.liquid`
- Commit dev final: `152502b` — `fix(lkgoc): apply NB 204L teaser guard through mobile preview`
- `@media` do fix 204L ampliado para `max-width:989px`.
- Hard guard collapsed adicionado:
  - collage: `height:28px`, `max-height:28px`, `overflow:hidden`
  - card principal: `height:84px`, `max-height:84px`, `aspect-ratio:auto`, `translateY(-42px)`

## Shopify DEV/unpublished
- Tema: `lk-new-theme/dev`
- ID: `155065450718`
- Role medido: `unpublished`
- Production/main: não alterado

## Medição objetiva via Chromium/CDP
Viewport: 575x900
- Theme: `lk-new-theme/dev`
- Role: `unpublished`
- Body: `template-collection`
- Collage rect height: `28`
- Collage computed height: `28px`
- Collage max-height: `28px`
- Card rect height: `84`
- Card max-height: `84px`
- Card aspect-ratio: `auto`
- Card transform: `matrix(... -42)`

Screenshot medido:
`/opt/data/profiles/lk-collection-optimizer/output/204l-mobile-audit/204l-mobile-shopify-dev-force-measured-575-20260608.png`
