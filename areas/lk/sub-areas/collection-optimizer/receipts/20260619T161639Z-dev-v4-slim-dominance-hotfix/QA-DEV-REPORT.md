# QA DEV — v4 slim dominance hotfix

- Data UTC: 2026-06-19T16:20:12.206024+00:00
- Theme testado: `lk-new-theme/dev` / `155065450718` / role `unpublished`
- Escopo: 4 coleções, desktop + mobile, preview DEV.
- Production: não alterada.

## Verdict

**OK em DEV para approval de merge production.**

## Critérios validados

- `.coll-rich-content__inner`: `display:block`, `grid-template-columns:none`.
- Fundo do bloco: `#faf8f4`.
- Cards de lista: desktop em grid 3 colunas, mobile empilhado.
- `Resumo LK`: fundo branco, sem bloco preto.
- Labels pseudo-element: `Guia LK` e `Resumo LK`.
- Asset renderizado no preview DEV: `/cdn/shop/t/92/assets/lk-collection-v2.css`.

## Resultado por página
- adidas-handball-spezial / desktop: OK
  - inner: block; columns: none; ul: grid / 287.328px 287.328px 287.344px; resumo bg: rgb(255, 255, 255)
  - asset: https://lksneakers.com.br/cdn/shop/t/92/assets/lk-collection-v2.css?v=40195525142795396301781885867
- adidas-handball-spezial / mobile: OK
  - inner: block; columns: none; ul: block / none; resumo bg: rgb(255, 255, 255)
  - asset: https://lksneakers.com.br/cdn/shop/t/92/assets/lk-collection-v2.css?v=40195525142795396301781885867
- new-balance-1906l / desktop: OK
  - inner: block; columns: none; ul: grid / 287.328px 287.328px 287.344px; resumo bg: rgb(255, 255, 255)
  - asset: https://lksneakers.com.br/cdn/shop/t/92/assets/lk-collection-v2.css?v=40195525142795396301781885867
- new-balance-1906l / mobile: OK
  - inner: block; columns: none; ul: block / none; resumo bg: rgb(255, 255, 255)
  - asset: https://lksneakers.com.br/cdn/shop/t/92/assets/lk-collection-v2.css?v=40195525142795396301781885867
- alo-yoga-1 / desktop: OK
  - inner: block; columns: none; ul: grid / 287.328px 287.328px 287.344px; resumo bg: rgb(255, 255, 255)
  - asset: https://lksneakers.com.br/cdn/shop/t/92/assets/lk-collection-v2.css?v=40195525142795396301781885867
- alo-yoga-1 / mobile: OK
  - inner: block; columns: none; ul: block / none; resumo bg: rgb(255, 255, 255)
  - asset: https://lksneakers.com.br/cdn/shop/t/92/assets/lk-collection-v2.css?v=40195525142795396301781885867
- air-jordan-1-low / desktop: OK
  - inner: block; columns: none; ul: grid / 287.328px 287.328px 287.344px; resumo bg: rgb(255, 255, 255)
  - asset: https://lksneakers.com.br/cdn/shop/t/92/assets/lk-collection-v2.css?v=40195525142795396301781885867
- air-jordan-1-low / mobile: OK
  - inner: block; columns: none; ul: block / none; resumo bg: rgb(255, 255, 255)
  - asset: https://lksneakers.com.br/cdn/shop/t/92/assets/lk-collection-v2.css?v=40195525142795396301781885867

## Evidências

- QA dir: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/qa/20260619T-dev-v4-slim-dominance-hotfix-qa`
- `computed-style-qa.json`
- `summary.json`
- screenshots full page e screenshots do elemento rico.
