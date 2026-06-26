# Receipt DEV — Adidas SL 72 guide/FAQ/schema preview — 2026-06-26

Context: SEMrush continuation after NB530 and Adidas Campus 00s. Historical gate checked: recent packets/workdirs/receipts show Adidas Campus was already executed; Adidas SL 72 is the next pending SEMrush opportunity.

## Executed

Dev theme write only:
- Theme: `lk-new-theme/dev`
- Theme ID: `155065450718`
- Asset: `snippets/lk-goc-guide-contract.liquid`

Added conditional block only for:
- `collection.handle == 'adidas-sl-72'`

Existing Adidas Campus block remained present in dev. Production was read-only and not changed.

## Preview

`https://lksneakers.com.br/collections/adidas-sl-72?preview_theme_id=155065450718&cache=false`

## Content prepared

Guide/FAQ focused on:
- Adidas SL 72 OG vs RS
- conforto
- significado de SL
- história do modelo
- feminino/styling
- colors/use-case guidance

## Not changed

- Production theme not changed.
- SEO title/meta not changed.
- Collection description not changed.
- Products, price, stock, ordering not changed.
- GMC, campaigns, Klaviyo, checkout not changed.

## QA

- Dev asset readback matched target after retry.
- Public dev preview: SL72 guide present; FAQPage count 1; no Liquid error.
- Adidas Campus dev regression: Campus guide remains, no Liquid error.
- Production SL72 public URL: unchanged relative to this dev block; no new SL72 block marker from this dev change.

Evidence: `QA_FINAL.json`, `DEV_WRITE_READBACK.json`, `dev-before-contract.liquid`, `dev-after-contract.liquid`.

## Production approval text

`Aprovo publicar em produção o guia/FAQ/schema Adidas SL 72 conforme preview dev 155065450718, limitado ao asset snippets/lk-goc-guide-contract.liquid com condição para collection.handle == 'adidas-sl-72', sem alterar SEO title/meta, descrição da coleção, produtos, preço, estoque, ordenação, GMC, campanhas, Klaviyo ou checkout, com rollback e readback público.`
