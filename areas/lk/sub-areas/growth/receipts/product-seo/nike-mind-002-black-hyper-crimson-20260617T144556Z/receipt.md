# Receipt — Product SEO/FAQ — Nike Mind 002 Black Hyper Crimson

Timestamp UTC: 20260617T144556Z

Status: OK / public QA consistent

## Produto

- Handle: `tenis-nike-mind-002-black-hyper-crimson-preto`
- URL: `https://lksneakers.com.br/products/tenis-nike-mind-002-black-hyper-crimson-preto`
- Product ID: `gid://shopify/Product/9118022566110`

## Aprovação

Lucas aprovou aplicar no PDP `/products/tenis-nike-mind-002-black-hyper-crimson-preto` somente `seo.title`, `seo.description` e descrição/FAQ do produto conforme o packet Nike Mind 002 Black Hyper Crimson 2026-06-17, sem mexer em preço, estoque, desconto, feed/GMC, campanhas, theme production fora do escopo, checkout, Klaviyo/WhatsApp ou outros produtos, com backup, QA, rollback e revisão D+7/D+14.

## Escopo executado

- `seo.title`: `Nike Mind 002 Black Hyper Crimson Original no Brasil | LK`
- `seo.description`: `Nike Mind 002 Black Hyper Crimson original no Brasil: sneaker escultural Nike Mind com curadoria exclusiva LK, autenticidade e atendimento humano.`
- `descriptionHtml`: bloco answer-first + FAQ aprovado

## Escopo bloqueado / não alterado por este script

- preço
- estoque
- desconto
- feed/GMC
- campanhas
- theme production fora do escopo
- checkout
- Klaviyo/WhatsApp
- outros produtos

## QA

- Admin readback: OK
- Público: consistent
- Pass counts: {"title_new": 6, "meta_new": 6, "copy_new": 6, "faq_new": 6, "product_marker": 6}

## Backup e rollback

- Backup: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/product-seo/nike-mind-002-black-hyper-crimson-20260617T144556Z/backup-before.json`
- Rollback payload: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/product-seo/nike-mind-002-black-hyper-crimson-20260617T144556Z/rollback-payload.json`
- QA: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/product-seo/nike-mind-002-black-hyper-crimson-20260617T144556Z/qa-after.json`

Rollback: executar `productUpdate` com `seo` e `descriptionHtml` salvos em `rollback-payload.json`.

## Revisão de impacto

- D+7: 2026-06-24
- D+14: 2026-07-01

values_printed=false
