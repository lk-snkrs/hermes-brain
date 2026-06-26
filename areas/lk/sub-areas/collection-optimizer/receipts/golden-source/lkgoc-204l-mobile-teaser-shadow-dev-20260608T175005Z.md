# Receipt — LKGOC 204L mobile teaser/shadow correction

Data UTC: 20260608T175005Z
Status: concluído em GitHub dev + Shopify DEV/unpublished

## Feedback Lucas
A imagem mobile collapsed estava aparecendo inteira. Isso estava errado.
O padrão correto é mostrar apenas uma prévia/sombra/corte, incentivando clique em `Ler mais` para ver as imagens completas.

## Correção
- Arquivo: `layout/theme.liquid`
- Commit dev: `1c00853` — `fix(lkgoc): restore NB 204L mobile image teaser`
- Mobile collapsed:
  - collage com `max-height:96px`
  - `overflow:hidden`
  - gradient/sombra inferior
  - imagem principal cortada/preview
- Mobile expanded `.is-open`:
  - `max-height:none`
  - `overflow:visible`
  - remove overlay
  - mostra collage completa

## Shopify DEV/unpublished
- Tema: `lk-new-theme/dev`
- Theme ID: `155065450718`
- Role validado: `unpublished`
- Push: sucesso, apenas `layout/theme.liquid`
- Production/main: não alterado

## QA
- Preview real via Chromium com cookie de preview confirmou:
  - `lk-new-theme/dev`: sim
  - `role=unpublished`: sim
  - `max-height:96px`: presente
  - gradient teaser: presente
- Screenshot real DEV:
  - `/opt/data/profiles/lk-collection-optimizer/output/204l-mobile-audit/204l-mobile-shopify-dev-teaser-shadow-20260608.png`
- Screenshots locais:
  - collapsed: `/opt/data/profiles/lk-collection-optimizer/output/204l-mobile-audit/204l-mobile-teaser-shadow-collapsed-20260608.png`
  - expanded: `/opt/data/profiles/lk-collection-optimizer/output/204l-mobile-audit/204l-mobile-teaser-shadow-expanded-20260608.png`
