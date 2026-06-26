# Receipt DEV — Adidas Campus 00s guide/FAQ preview — 2026-06-25

Approval: Lucas Telegram current turn approved dev/preview only.

## Executed

Dev theme write only:
- Theme: `lk-new-theme/dev`
- Theme ID: `155065450718`
- Asset: `snippets/lk-goc-guide-contract.liquid`

Reason for using this asset: `sections/lk-collection.liquid` is oversized and previously hit Shopify 256 KB limit; `lk-goc-guide-contract` is already rendered by the collection section and was empty, so the change is conditionally scoped to `collection.handle == 'adidas-campus'`.

## Preview

`https://lksneakers.com.br/collections/adidas-campus?preview_theme_id=155065450718&cache=false&qa=campus-dev-final-20260625`

## Content prepared

Guide/FAQ focused on:
- Adidas Campus 00s
- authenticity/originality
- feminino/masculino/unissex
- colors: preto, cinza, branco, verde, rosa
- styling/how to wear

## Not changed

- Production theme not changed.
- SEO title/meta not changed.
- Collection description not changed.
- Products, price, stock, ordering not changed.
- GMC, campaigns, Klaviyo, checkout not changed.

## QA

- Dev asset readback: Campus conditional present.
- Public dev preview: guide present; no Liquid error.
- Production public Campus URL: guide absent/unchanged.
- SL72 preview regression check: no Campus guide injected.

Evidence: `QA_FINAL.json`, `DEV_READBACK_RETRY.json`, `dev-before-lk-goc-guide-contract.liquid`, `dev-after-retry-lk-goc-guide-contract.liquid`.

## Production approval text

`Aprovo publicar em produção o guia/FAQ Adidas Campus 00s conforme preview dev 155065450718, limitado ao asset snippets/lk-goc-guide-contract.liquid com condição para collection.handle == 'adidas-campus', sem alterar SEO title/meta, descrição da coleção, produtos, preço, estoque, ordenação, GMC, campanhas, Klaviyo ou checkout, com rollback e readback público.`
