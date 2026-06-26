# Receipt DEV — Adidas Gazelle guide/FAQ/schema preview — 2026-06-25

Context: SEMrush continuation after NB530, Adidas Campus 00s and Adidas SL 72. Historical gate checked in `approval-packets/semrush-next-readback-20260625/APPROVAL-PACKET.md`.

## Executed

Dev theme write only:
- Theme: `lk-new-theme/dev`
- Theme ID: `155065450718`
- Asset: `snippets/lk-goc-guide-contract.liquid`

Added conditional block only for:
- `collection.handle == 'adidas-gazelle'`

Existing Adidas Campus and SL72 blocks remained present in dev. Production was read-only and not changed.

## Preview

- `https://lksneakers.com.br/collections/adidas-gazelle?preview_theme_id=155065450718&cache=false`
- `https://lksneakers.com.br/collections/adidas-gazelle-feminino?preview_theme_id=155065450718&cache=false`

## Content prepared

Guide/FAQ focused on:
- Adidas Gazelle feminino
- Gazelle Indoor / OG / Bold
- Gazelle vs Samba
- cores branco, prata, rosa, verde, bege/marrom
- conforto/forma
- autenticidade

## Not changed

- Production theme not changed.
- SEO title/meta not changed.
- Collection description not changed.
- Products, price, stock, ordering not changed.
- GMC, campaigns, Klaviyo, checkout not changed.

## QA

- Dev asset readback matched target after retry.
- Public dev preview Gazelle: guide present; FAQPage count 1; no Liquid error.
- Gazelle feminino route: guide present; no Liquid error.
- Production Gazelle public URL: unchanged; no Gazelle guide from this dev change.
- Regression: Campus and SL72 guides still scoped to their own pages.

Evidence: `QA_FINAL.json`, `DEV_WRITE_READBACK.json`, `collection-readback.json`, `dev-before-contract.liquid`, `dev-after-contract.liquid`.

## Production approval text

`Aprovo publicar em produção o guia/FAQ/schema Adidas Gazelle conforme preview dev 155065450718, limitado ao asset snippets/lk-goc-guide-contract.liquid com condição para collection.handle == 'adidas-gazelle', sem alterar SEO title/meta, descrição da coleção, produtos, preço, estoque, ordenação, GMC, campanhas, Klaviyo ou checkout, preservando os blocos Adidas Campus e Adidas SL 72, com rollback e readback público.`
