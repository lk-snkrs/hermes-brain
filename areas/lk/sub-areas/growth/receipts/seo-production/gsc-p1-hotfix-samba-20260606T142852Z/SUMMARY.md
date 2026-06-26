# LK SEO GSC P1 + Hotfix Samba Jane — Production execution summary

## Approval
Lucas approved in current turn:

> Aprovo aplicar o pacote SEO GSC P1 + hotfix Samba Jane em dev/produção conforme QA e rollback.

## Production writes executed

### Theme production
Theme: `lk-new-theme/production` / role `main` / ID `155065417950`.

Assets touched:

- `snippets/lk-samba-jane-editorial-v3.liquid`
  - created as safe shim to remove public Liquid error with minimal layout change.
  - readback match: true.
- `layout/theme.liquid`
  - homepage title/meta strings patched in head.
  - product `<title>` logic patched to respect `product.metafields.global.title_tag` before fallback title with price.
  - first PUT readback was stale/non-match; retry PUT at 2026-06-06T14:28:53Z read back exact candidate.

### Shopify SEO fields
Applied and GraphQL-verified 8/8 product/collection SEO records:

- collection `new-balance-204l`
- collection `onitsuka-tiger-todos-os-modelos`
- collection `lululemon`
- product `slide-nike-mind-001-black-chrome-preto`
- product `slide-nike-mind-001-pearl-pink-rosa`
- product `crocs-classic-clog-x-the-cars-lightning-mcqueen-vermelho`
- collection `yeezy`
- product `tenis-nike-vomero-premium-white-bright-crimson-branco`

Page `guia-nike-mind-001-002` was updated through REST global SEO fields and public head QA shows the proposed title/meta live.

Homepage was handled in `layout/theme.liquid`; public QA still showed stale old homepage title/meta immediately after deploy, while Asset API readback shows the new strings. Treat as Shopify/storefront cache propagation and re-check later.

## QA

- Public HTTP/head QA saved: `public-head-qa.json`.
- Liquid error absent in all checked URLs, including Adidas Samba Jane.
- Some public title/meta reads showed cache variance/stale storefront immediately after deploy:
  - homepage old title/meta persisted in public HTML at first QA even though theme asset readback is new.
  - GraphQL SEO fields verified for collections/products, but some public HTML reads differed between Playwright and direct urllib. Re-check after cache settles.

## Rollback

Rollback assets/records:

- `rollback.json` in this directory for theme assets and REST backups.
- GraphQL rollback SEO fields: `../gsc-p1-graphql-seo-20260606T143014Z/receipt.json` under `rollback` array.

Theme rollback:

- restore `layout__theme.before.liquid` to `layout/theme.liquid` if head logic causes regression.
- delete `snippets/lk-samba-jane-editorial-v3.liquid` if shim must be removed, or replace with previous asset if it existed.

SEO rollback:

- use GraphQL `productUpdate` / `collectionUpdate` with previous `seo.title` and `seo.description` from rollback records.

## Follow-up

One-shot D+7 impact review scheduled:

- job id: `f0993178730a`
- run at: `2026-06-13T13:00:00+00:00`
- delivery: origin
