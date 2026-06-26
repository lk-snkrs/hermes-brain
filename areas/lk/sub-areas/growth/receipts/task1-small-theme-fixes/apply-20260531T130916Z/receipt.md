# Receipt — task1 small theme fixes applied

Data: 2026-05-31
Escopo aprovado por Lucas: aplicar em dev e depois produção, com backups/readback.

## Assets alterados

- `layout/theme.liquid`
  - adicionada branch `template.name == 'index'` no Twitter Card da home.
- `sections/lk-hero.liquid`
  - fallback de alt robusto: `image_alt > title > kicker > shop.name`.
- `sections/lk-cart.liquid`
  - carrinho vazio: `h2.cart-empty__title` → `h1.cart-empty__title`.

## Temas

- Dev: `lk-new-theme/dev`, ID `155065450718`, role `unpublished`.
- Produção: `lk-new-theme/production`, ID `155065417950`, role `main`.

## Readback Shopify Asset API

Receipt JSON:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/task1-small-theme-fixes/apply-20260531T130916Z/receipt.json`

Status:

- Dev: 3/3 assets com readback hash OK.
- Produção: 3/3 assets com readback hash OK.

## Backups/rollback

Pasta:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/task1-small-theme-fixes/apply-20260531T130916Z/`

Rollback:

- Reenviar cada arquivo `*.before` para o asset Shopify correspondente no mesmo tema.

## Validação pública imediata

### Carrinho

Status: propagado.

- `/cart` agora tem H1: `Seu carrinho está vazio`.
- DataForSEO também leu `h1: Seu carrinho está vazio`.
- `no_h1_tag` deixou de aparecer no resultado do carrinho.

### Home

Status: asset aplicado, mas storefront público ainda com cache/render antigo para parte da home.

Confirmado no Asset API de produção:

- `layout/theme.liquid` contém Twitter Card novo.
- `sections/lk-hero.liquid` contém fallback de alt novo.

Ainda não refletido no HTML público da home após rechecagens imediatas:

- `twitter:title` público ainda aparece como `LK Sneakers | Tênis Nike Dunk, adidas Samba, New Balance 530 Originais`.
- hero principal ainda aparece com `alt=""`.

Interpretação:

- A escrita em Shopify foi aceita e readback bate com o alvo.
- A rota da home parece estar servindo cache/render antigo para esses trechos, enquanto `/cart` já refletiu imediatamente.
- Não executei publish/republish/purge ou qualquer ação extra de cache/tema além do escopo aprovado.

## Diagnóstico headless

Tentado pré-requisito local:

- `playwright`: ausente.
- `selenium`: ausente.
- `pyppeteer`: ausente.
- binários Chromium/Chrome: ausentes no PATH.

Status: bloqueado localmente sem instalar ferramenta nova. Pode ser retomado se aprovarmos instalar/usar uma ferramenta headless ou outro ambiente.

## Não feito

- Nenhum produto/coleção/preço/estoque/SKU.
- Nenhum checkout/desconto/fulfillment.
- Nenhum app/Klaviyo/ads/WhatsApp/email.
- Nenhum GMC/feed.
- Nenhum publish/re-publish/purge/manual cache action.
