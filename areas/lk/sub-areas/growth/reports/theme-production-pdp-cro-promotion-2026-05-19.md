# LK Theme Production Promotion — PDP CRO

Data: 2026-05-19T15:29:50Z
Contexto: LK Sneakers / Shopify theme production
Aprovador: Lucas, via Telegram: “subir para o PRODUCTION”

## Escopo executado

- Tema verificado: `lk-new-theme/production`
- Theme ID: `155065417950`
- Role: `main`
- Asset tocado: `sections/lk-pdp.liquid`
- Tipo: promoção/hotfix de PDP CRO já validado em dev/local

## Não executado

- Sem alteração de produto, preço, estoque, coleção, checkout, app, campanha, Klaviyo, Meta, Merchant Center ou atendimento.
- Sem publish/criação de tema novo.
- Sem envio externo.

## Evidência técnica

- Store Admin: `lk-sneakerss.myshopify.com`
- HTTP PUT Asset API: `200`
- Readback Asset API: `200`
- SHA readback/local: `7cb348c5c893b0b75ba8c1a651c7b885f3a39a79240677cdf5cb49eb2d34e973`
- Readback bateu com o asset pós-upload: `true`
- Request ID: `c2c7f2fa-22ca-4bb9-bc1e-480b2dc353f2-1779204435`

Marcadores no readback:

- `#2a2725 !important` no trust grid: `true`
- `.shopify-payment-button__button` com `display: flex !important` e `min-height: 50px !important`: `true`
- `.pi-preorder-card` com margem 12px: `true`

## Backup / rollback

Backup de produção criado em:

`/opt/data/hermes_bruno_ingest/lk-new-theme-cro-weekly-20260519/backups/theme-production/20260519T152714Z_telegram_prod_promotion`

Arquivos:

- `sections__lk-pdp.liquid.before`
- `sections__lk-pdp.liquid.after`
- `sections__lk-pdp.liquid.readback`
- `manifest.json`
- `receipt.json`

Rollback: re-subir o arquivo `sections__lk-pdp.liquid.before` para o mesmo asset `sections/lk-pdp.liquid` do tema `155065417950`, depois readback por SHA e validação visual da PDP.

## QA storefront

URL validada sem `preview_theme_id`:

`https://lksneakers.com.br/products/tenis-adidas-samba-jane-black-white-gum-preto?lkprodqa=20260519T152714`

Resultado DOM/computed style:

- Botão real `.pi-actions .shopify-payment-button__button`: visível
- Texto: `COMPRE JÁ`
- Largura/altura: `389 × 50`
- Visibilidade: `visible`
- Opacidade: `1`
- Wrapper `.shopify-payment-button`: visível
- Trust grid: visível, sem overflow óbvio na validação
- Aviso: `Sujeito a encomenda · 4-6 semanas · Confirme no WhatsApp`, visível

Screenshot de evidência:

`/opt/data/profiles/lk-growth/cache/screenshots/browser_screenshot_e14ecb6457794814906ff91a84d631b6.png`

## Revisão de impacto D+7

Agendar/verificar por volta de 2026-05-26:

- GA4: PDP views, add_to_cart, begin_checkout, purchase/revenue dos PDPs afetados.
- Shopify: pedidos/conversão dos produtos/coleções priorizados.
- GSC/SEO: sem expectativa de impacto imediato; monitorar apenas anomalia de indexação/renderização.
- CRO: checar se `COMPRE JÁ`, trust grid e aviso continuam visíveis no mobile e sem interferência de apps.
