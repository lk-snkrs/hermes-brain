# Receipt — DEV Vomero Search + Size Guide Polish — 2026-06-16

## Escopo aprovado

Lucas aprovou subir em DEV:

1. `sections/lk-search.liquid`
   - adicionar aliases `vomero`, `vômero`, `nike vomero` para sugerir `Nike Vomero Premium`.
2. `sections/lk-pdp.liquid`
   - polish de copy/espaçamento no Guia de Tamanhos para frases Nike/Vomero/Mind.

Sem Production, sem SEO fields/produtos, sem preço, estoque, campanha ou app write.

## Target Shopify

- DEV theme: `lk-new-theme/dev`
- DEV theme id: `155065450718`
- DEV role: `unpublished`
- Production theme verificado: `lk-new-theme/production`
- Production role: `main`
- Production theme id: `155065417950`

## Backups antes do write

Backups salvos em:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/backups/dev-theme-vomero-search-sizeguide-polish-20260616/`

Arquivos:

- `sections__lk-search.liquid.before.liquid`
- `sections__lk-pdp.liquid.before.liquid`

## Readback antes

DEV antes:

- `sections/lk-search.liquid`
  - sha256: `384fff2e6d3cbb7a8a9d6610c4cf516db41bd2e7d57c6ec8fb7127b70b0f1170`
  - bytes: `38966`
- `sections/lk-pdp.liquid`
  - sha256: `834b18e897f94cbb8ca49b8aac103c7f61acc7b02498772e28885f9ed6f64ff3`
  - bytes: `166366`

Production antes:

- `sections/lk-search.liquid`
  - sha256: `384fff2e6d3cbb7a8a9d6610c4cf516db41bd2e7d57c6ec8fb7127b70b0f1170`
- `sections/lk-pdp.liquid`
  - sha256: `a3cd7e5c20a5c99d3b350e1feb5060be4731301e91bccf8c0e3a8f5036105043`

## Write executado

Asset API PUT somente no DEV theme `155065450718`.

Arquivos alterados:

- `sections/lk-search.liquid`
  - target sha256: `b1063d65e2ca0f6dfbc0867443ec39f419e9a55b9c41247e02591d9c8a676e55`
  - bytes: `38992`
- `sections/lk-pdp.liquid`
  - target sha256: `0f1101684a14656b1ff45a4b0d08b7e9a2aef0afb8c09fd22330ae917706605d`
  - bytes: `166452`

## Readback depois

DEV depois:

- `sections/lk-search.liquid`
  - matches target: `true`
- `sections/lk-pdp.liquid`
  - matches target: `true`

Production depois:

- `sections/lk-search.liquid`
  - unchanged: `true`
- `sections/lk-pdp.liquid`
  - unchanged: `true`

## QA mobile DEV

Viewport: mobile `390x844`, Chromium headless/CDP.

### Busca

Resultado do QA focado salvo em:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/dev-vomero-search-sizeguide-qa-20260616/dev-search-focused-results.json`

Passou:

- `vomero` → `Ver coleção: Nike Vomero Premium` — OK
- `vômero` → `Ver coleção: Nike Vomero Premium` — OK
- `vomero premium` → `Ver coleção: Nike Vomero Premium` — OK
- `vomero 5` → `Ver coleção: Nike Vomero 5` + `Nike Vomero Premium` — OK/observação
- `204L` → `Ver coleção: New Balance 204L` — OK
- `9060` → `Ver coleção: New Balance 9060` — OK
- `530` → `Ver coleção: New Balance 530` — OK

Todos com:

- `Liquid error`: `0`
- overflow horizontal: `false`

Observação: `vomero 5` continua exibindo `Nike Vomero 5` primeiro e também `Nike Vomero Premium` como segunda sugestão por match de substring. Aceitável para DEV atual, mas pode ser refinado se Lucas quiser sugestão única.

### Guia de tamanhos

Resultado do QA focado salvo em:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/dev-vomero-search-sizeguide-qa-20260616/dev-sizeguide-focused-results.json`

Passou:

- Vomero Premium
  - copy: `O Nike Vomero Premium costuma vestir normal. Recomendamos comprar seu tamanho habitual.`
  - modal abriu, `aria-hidden=false`
- Nike Mind 002
  - copy: `O Nike Mind 002 masculino tem forma correta. Recomendamos comprar seu tamanho habitual.`
  - modal abriu, `aria-hidden=false`
- Yeezy Slide controle
  - copy `+1 tamanho inteiro acima` preservada
  - modal abriu, `aria-hidden=false`
- New Balance 530 controle
  - recomendação habitual preservada
  - modal abriu, `aria-hidden=false`

Todos com:

- `Liquid error`: `0`
- overflow horizontal: `false`

## Links de preview para Lucas

Base preview:

`https://lksneakers.com.br/?preview_theme_id=155065450718`

Busca:

- `https://lksneakers.com.br/search?type=product&q=vomero&preview_theme_id=155065450718`
- `https://lksneakers.com.br/search?type=product&q=v%C3%B4mero&preview_theme_id=155065450718`
- `https://lksneakers.com.br/search?type=product&q=vomero%20premium&preview_theme_id=155065450718`
- `https://lksneakers.com.br/search?type=product&q=vomero%205&preview_theme_id=155065450718`

PDP/Guia:

- `https://lksneakers.com.br/products/tenis-nike-vomero-premium-black-volt-preto?preview_theme_id=155065450718`
- `https://lksneakers.com.br/products/tenis-nike-mind-002-sail-bege?preview_theme_id=155065450718`
- `https://lksneakers.com.br/products/yeezy-slide-glow-green?preview_theme_id=155065450718`
- `https://lksneakers.com.br/products/new-balance-530-white-natural-indigo-1?preview_theme_id=155065450718`

## Rollback

Para rollback de DEV:

1. Reaplicar os arquivos de backup:
   - `sections__lk-search.liquid.before.liquid`
   - `sections__lk-pdp.liquid.before.liquid`
2. PUT somente no DEV theme `155065450718`.
3. Readback SHA esperado do DEV rollback:
   - search: `384fff2e6d3cbb7a8a9d6610c4cf516db41bd2e7d57c6ec8fb7127b70b0f1170`
   - PDP: `834b18e897f94cbb8ca49b8aac103c7f61acc7b02498772e28885f9ed6f64ff3`

## Status final

- DEV alterado e verificado.
- Production intacta.
- QA mobile passou em busca e guia de tamanhos.
- Próxima decisão: Lucas revisar links de preview e decidir se promove para Production depois de aprovar visualmente.
