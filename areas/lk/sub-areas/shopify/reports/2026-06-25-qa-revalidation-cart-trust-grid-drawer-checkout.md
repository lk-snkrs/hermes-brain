# QA revalidation — `/cart` Trust Grid, cart drawer, checkout Google Reviews

- **Data:** 2026-06-25
- **Agente:** lk-shopify
- **Pedido:** Lucas escolheu “Fazer QA/revalidação dos 3 itens: `/cart` Trust Grid, cart drawer, checkout”.
- **Writes externos:** nenhum nesta etapa de QA; apenas leitura/Admin readback, browser público e arquivos locais.
- **Secrets:** nenhum valor impresso; `values_printed=false`.

## Veredito

| Item | Status |
|---|---|
| `/cart` Trust Grid Google Reviews | **Source/Admin OK; public live bloqueado** por 429/verificação |
| Cart drawer `MAIS VENDIDOS LK` + add button | **Source/Admin OK; public live bloqueado** por 429/verificação |
| Checkout Google Reviews 420 | **Deploy/source OK; public live bloqueado** por 429/verificação |

## Evidência — Admin/source

### `/cart` Trust Grid

Arquivo Production readback:

- `sections/lk-cart.liquid`
- `sha256=05046002f21bb087113b3175184ecda8ccd3c2b82c03534d66b534c904b1ffaf`
- `lk_google_review_count`: 3 ocorrências
- `376 avaliações`: 0 ocorrências

Interpretação: o `/cart` está com a lógica dinâmica que lê `shop.metafields.lk_google.reviews.value`.

### Shopify metafield Google Reviews

Readback Admin GraphQL pós-sync:

- `shop.metafields.lk_google.reviews`
- `type=json`
- `rating=4.9`
- `count=420`
- `userRatingCount=420`
- `source=google_places`

Interpretação: a fonte do `/cart` está atualizada em 420.

### Cart drawer

Arquivo Production readback:

- `snippets/lk-cart-drawer.liquid`
- `sha256=7e1e11ffdcf107757beb5d6877de117fb9a68a6e9fa639917673e10bbfd0315c`
- `cart-drawer__upsell`: 28 ocorrências
- `window.location.reload`: 0 ocorrências

Interpretação: Production contém o bloco de upsell e removeu o reload frágil do add button. Static check local indica ordem `items -> upsell -> footer` no alvo aplicado.

### Checkout extension

Projeto:

- `/opt/data/projects/lk-gift-bag-checkout-app`
- arquivo `extensions/social-proof/src/Checkout.jsx`
- `420 avaliações`: 2 ocorrências
- `411 avaliações`: 0 ocorrências
- deploy publicado: `lk-gift-bag-checkout-18`
- version URL: `https://dev.shopify.com/dashboard/50805400/apps/380136325121/versions/1029022711809`

Interpretação: checkout extension foi atualizado para o valor 420 e publicado.

## Evidência — browser público

Script CDP/Chromium:

- `/opt/data/profiles/lk-shopify/workdirs/qa-revalidate-cart-checkout-20260625/qa_cdp_cart_checkout.py`
- resultado: `/opt/data/profiles/lk-shopify/workdirs/qa-revalidate-cart-checkout-20260625/qa_cdp_result.json`

Resultado público:

- Tentativa de montar carrinho via Storefront: produtos retornaram `product_http_429`.
- `/cart`: carregou sem carrinho válido; Trust Grid não renderizou.
- Home/cart drawer: página caiu em verificação/limitação; drawer DOM não disponível.
- `/checkout`: redirecionou para página de verificação “Your connection needs to be verified before you can proceed”.
- `/checkouts/`: retornou `Not Found`.

Interpretação: QA visual público não pôde ser fechado por limitação anti-bot/rate limit, não por evidência de regressão no código.

## Artefatos locais

- `/opt/data/profiles/lk-shopify/workdirs/qa-revalidate-cart-checkout-20260625/shopify_admin_readback.json`
- `/opt/data/profiles/lk-shopify/workdirs/qa-revalidate-cart-checkout-20260625/qa_cdp_result.json`
- `/opt/data/profiles/lk-shopify/workdirs/qa-revalidate-cart-checkout-20260625/qa_static_summary.json`

## Rollback

Sem write nesta etapa. Rollbacks dos deploys anteriores permanecem:

- Cart drawer/cart add: revert PR #94.
- `/cart` Trust Grid: revert PR #95.
- Cron/metafield sync: restaurar backups em `workdirs/google-reviews-cron-sync-20260625/*.before` e/ou ajustar metafield manualmente.
- Checkout 420: restaurar `workdirs/checkout-google-reviews-420-20260625/Checkout.jsx.before`, build e deploy nova versão.

## Reminder OS

- **Reminder OS loop needed:** yes
- **Reminder OS owner:** lk-shopify
- **Reminder OS next action:** repetir QA público real-browser dos 3 itens quando o rate limit/verificação baixar: carrinho com item, `/cart` Trust Grid mostrando 420, drawer com `MAIS VENDIDOS LK` abaixo da lista e add button funcional, checkout social proof mostrando `4,9 • 420 avaliações`.
- **Reminder OS review trigger:** após cooldown de 60–120 min ou em uma janela com menor tráfego/menos bloqueio anti-bot.
- **Reminder OS evidence:** Admin/source/readback OK nos artefatos listados; public QA bloqueado por 429/verificação.
