# Receipt — Dev theme upload: cart drawer scroll + Judge.me empty rating gap

Data: 2026-06-17
values_printed=false

## Aprovação
Lucas aprovou em Telegram: `aprovo, subir dev`.

## Escopo executado
Upload para **Dev/unpublished theme** somente dos arquivos aprovados:

- `snippets/lk-cart-drawer.liquid`
- `sections/lk-pdp.liquid`
- `snippets/judgeme_widgets.liquid`

Não feito:

- Não publiquei tema.
- Não toquei production/main.
- Não alterei produto, preço, estoque, checkout, app, campanha ou cliente.

## Theme alvo
- Theme: `lk-new-theme/dev`
- ID: `155065450718`
- Role: `unpublished`

Production observado, sem alteração:
- Theme: `lk-new-theme/production`
- ID: `155065417950`
- Role: `main`

## Upload/readback
Upload executado via Shopify Admin Asset API com Doppler `lk-shopify`.

Readback Admin:

- assets uploaded: `3`
- all_readback_match: `true`
- receipt JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/theme-cart-scroll-judgeme-empty-rating-dev-20260617/receipt.json`

Readback markers:

- `sections/lk-pdp.liquid`
  - has `:has([data-number-of-reviews=`: true
  - has JS fallback `count === 0`: true
  - has `No reviews` guard: true
- `snippets/lk-cart-drawer.liquid`
  - has `#cart-drawer-body`: true
  - has `min-height: 0` / scroll pattern: true
- `snippets/judgeme_widgets.liquid`
  - has `No reviews` guard: true

## Preview URLs
- Home: https://www.lksneakers.com.br/?preview_theme_id=155065450718
- PDP referência: https://www.lksneakers.com.br/products/new-balance-530-white-natural-indigo-1?preview_theme_id=155065450718
- Cart: https://www.lksneakers.com.br/cart?preview_theme_id=155065450718
- PDP sem rating usado em QA: https://www.lksneakers.com.br/products/nike-dunk-low-rose-whisper?preview_theme_id=155065450718
- PDP com rating usado em QA: https://www.lksneakers.com.br/products/air-jordan-1-mid-wolf-grey?preview_theme_id=155065450718

## QA público/preview
Arquivo: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/theme-cart-scroll-judgeme-empty-rating-dev-20260617/dev_preview_qa.json`

Resultados:

- Home preview HTTP 200: true
- Cart preview HTTP 200: true
- Liquid errors: 0
- PDP com rating mantém anchor rating: true
- Cart scroll CSS detectado em preview: true

Observação: o HTML público de preview ainda mostrou conteúdo antigo/produção para a remoção estrutural do anchor em produto sem rating, apesar do Admin readback do Dev theme estar correto. Para mitigar, deixei a correção em duas camadas:

1. Guard Liquid para não renderizar quando `data-number-of-reviews='0'` / `No reviews`.
2. CSS `:has()` + fallback JS que zera `display` e `margin` quando o badge tiver `data-number-of-reviews=0`.

Isso remove o espaço visual mesmo se o wrapper vier no HTML por cache/edge/app.

## Rollback
Backups dos 3 arquivos antes do primeiro upload Dev estão em:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/theme-cart-scroll-judgeme-empty-rating-dev-20260617/backup/`

Rollback Dev: reenviar os 3 arquivos do backup para o theme `155065450718`.

Production rollback não aplicável porque production não foi alterado.

## Próximo passo
Abrir preview no navegador e validar visualmente:

1. PDP sem avaliação: não deve sobrar espaço entre título e próximo bloco.
2. PDP com avaliação: badge deve continuar aparecendo/clicável.
3. PDP com carrinho cheio/mobile: drawer deve rolar internamente e manter footer/checkout acessível.

Production continua bloqueado até aprovação separada.
