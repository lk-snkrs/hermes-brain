# Receipt — Production merge: cart drawer scroll + Judge.me empty rating gap

Data: 2026-06-17
values_printed=false

## Aprovação
Lucas aprovou em Telegram: `fazer merge para production`.

## Escopo executado
Merge para branch `production` do repo `lk-snkrs/lk-new-theme`, com promoção dos 3 arquivos validados em Dev:

- `snippets/lk-cart-drawer.liquid`
- `sections/lk-pdp.liquid`
- `snippets/judgeme_widgets.liquid`

Não feito:

- Não alterei produto, preço, estoque, checkout, app, campanha ou cliente.
- Não usei write direto manual no live theme como caminho primário; fluxo foi PR GitHub → merge em `production` → readback Shopify.

## GitHub
- PR: https://github.com/lk-snkrs/lk-new-theme/pull/84
- PR number: `84`
- State: `closed`
- Merged: `true`
- Merge SHA: `f4b2a637f7a072f180526bfc239b0a0d09628c29`
- Branch temporária: `fix/cart-scroll-judgeme-empty-rating-20260617-prod-142454`

Verificação GitHub production:

- `snippets/lk-cart-drawer.liquid`: GitHub production blob = target blob
- `sections/lk-pdp.liquid`: GitHub production blob = target blob
- `snippets/judgeme_widgets.liquid`: GitHub production blob = target blob
- all_match: `true`

Observação de segurança: antes de aplicar `sections/lk-pdp.liquid`, baixei o arquivo atual de GitHub `production` porque a cópia local de `origin/production` estava stale nesse arquivo. Apliquei só os hunks aprovados sobre a versão atual de production para evitar sobrescrever drift.

## Shopify production readback
Theme:

- `lk-new-theme/production`
- ID: `155065417950`
- role: `main`

Readback Admin/API:

- all_match: `true`
- attempt: `1`
- arquivo: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/theme-cart-scroll-judgeme-empty-rating-production-20260617/shopify_production_readback.json`

Hashes:

- `snippets/lk-cart-drawer.liquid`
  - target/readback SHA256: `1960968c3e5f...` / `1960968c3e5f...`
  - marker `#cart-drawer-body`: true
  - marker `overscroll-behavior: contain`: true
- `sections/lk-pdp.liquid`
  - target/readback SHA256: `7058bc607de6...` / `7058bc607de6...`
  - marker CSS `:has([data-number-of-reviews=`: true
  - marker JS `count === 0`: true
  - marker `No reviews`: true
- `snippets/judgeme_widgets.liquid`
  - target/readback SHA256: `ebfd20fbd4cc...` / `ebfd20fbd4cc...`
  - marker `No reviews`: true

## QA público live
Arquivo: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/theme-cart-scroll-judgeme-empty-rating-production-20260617/production_public_qa.json`

Resultados públicos:

- Home HTTP 200: true
- Cart HTTP 200: true
- PDP sem rating HTTP 200: true
- PDP com rating HTTP 200: true
- Liquid errors: 0
- Cart scroll CSS detectado no live PDP: true
- PDP com rating mantém anchor: true

Caveat público:

- Depois de múltiplas tentativas com cache-busting, o HTML público ainda não refletia todos os markers novos do guard de rating (`:has([data-number-of-reviews=`, JS fallback) embora GitHub `production` e Shopify Admin readback estejam 100% iguais ao target.
- Isso indica cache/edge/render público ainda defasado para esse trecho, não falha de merge/deploy no Admin source.

## Rollback
Caminho seguro:

1. Reverter PR 84 ou criar PR revertendo o merge SHA `f4b2a637f7a072f180526bfc239b0a0d09628c29` em `production`.
2. Aguardar deploy/readback do theme `155065417950`.
3. Validar Shopify Admin readback e QA público.

Backups Dev pré-change continuam em:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/theme-cart-scroll-judgeme-empty-rating-dev-20260617/backup/`

## Próxima validação recomendada
Abrir live no navegador real depois da propagação de cache:

- PDP sem rating: https://www.lksneakers.com.br/products/nike-dunk-low-rose-whisper
- PDP com rating: https://www.lksneakers.com.br/products/air-jordan-1-mid-wolf-grey
- Carrinho: https://www.lksneakers.com.br/cart

Validar visualmente:

1. Sem gap vazio abaixo do título em produto sem review.
2. Badge continua aparecendo em produto com review.
3. Drawer mobile com muitos itens rola internamente e mantém checkout/footer acessível.
