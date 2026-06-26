# Visual QA — Dev theme cart drawer + Judge.me empty rating

Data: 2026-06-17
values_printed=false

## Escopo
Preview Dev/unpublished theme `lk-new-theme/dev` (`155065450718`).

Testado em Chromium headless mobile viewport `390x844`:

- PDP sem rating: `nike-dunk-low-rose-whisper`
- PDP com rating: `air-jordan-1-mid-wolf-grey`
- Cart drawer mobile com carrinho temporário de sessão do navegador

Nenhum checkout, pedido, cliente, preço, estoque, campanha ou production write foi feito. O carrinho temporário foi limpo ao final do teste.

## Veredito
PASS.

Checks:

- PDP sem avaliação não mostra rating gap: `true`
- PDP com avaliação mantém rating visível: `true`
- Drawer mobile com área de itens rolável: `true`
- Liquid errors: `0`

## Evidência técnica
Fonte: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/theme-cart-scroll-judgeme-empty-rating-dev-20260617/visual-qa/visual_qa.json`

PDP sem rating:

- `ratingExists`: false
- `liquidError`: false
- `priceRect.t` = `595.828125`, igual ao fim do título `nameRect.b` = `595.828125`, indicando ausência do gap entre título e preço.

PDP com rating:

- `ratingExists`: true
- `ratingDisplay`: `inline-block`
- `reviewCountAttr`: `1`
- `liquidError`: false

Drawer mobile:

- `addOk`: true
- `variantsAdded`: 8
- `cartItemCount`: 8
- `bodyDisplay`: `flex`
- `bodyFlexDirection`: `column`
- `bodyMinHeight`: `0px`
- `itemsOverflowY`: `auto`
- `itemsMinHeight`: `0px`
- `itemsOverscroll`: `contain`
- `itemsRect.scrollHeight`: 1313
- `itemsRect.clientHeight`: 183
- Evidência de overflow real: `scrollHeight > clientHeight`
- `liquidError`: false

## Screenshots

- PDP sem rating: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/theme-cart-scroll-judgeme-empty-rating-dev-20260617/visual-qa/zero-pdp-mobile.png`
- PDP com rating: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/theme-cart-scroll-judgeme-empty-rating-dev-20260617/visual-qa/positive-pdp-mobile.png`
- Drawer mobile: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/theme-cart-scroll-judgeme-empty-rating-dev-20260617/visual-qa/drawer-mobile.png`

## Status production
Production/main não foi alterado.

## Rollback
Rollback Dev permanece o mesmo do receipt principal: reenviar os 3 arquivos em `../backup/` para o theme `155065450718`.
