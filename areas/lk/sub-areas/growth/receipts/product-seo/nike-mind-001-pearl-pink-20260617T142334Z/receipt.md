# Receipt — Product SEO/FAQ — Nike Mind 001 Pearl Pink

Timestamp UTC: 20260617T142334Z

Status: OK / public QA consistent

## Produto

- Handle: `slide-nike-mind-001-pearl-pink-rosa`
- URL: `https://lksneakers.com.br/products/slide-nike-mind-001-pearl-pink-rosa`
- Product ID: `gid://shopify/Product/9172212678878`

## Aprovação

Lucas aprovou aplicar somente `seo.title`, `seo.description` e descrição/FAQ do produto conforme o packet Pearl Pink, sem mexer em preço, estoque, desconto, feed/GMC, campanhas, theme production fora do escopo, checkout, Klaviyo/WhatsApp ou outros produtos, com backup, QA, rollback e revisão D+7/D+14, mesmo com o Black Chrome ainda em propagação pública mista.

## Escopo executado

- `seo.title`: `Nike Mind 001 Pearl Pink Original no Brasil | LK`
- `seo.description`: `Nike Mind 001 Pearl Pink original no Brasil: slide sensorial Nike em rosa claro, com curadoria exclusiva LK, autenticidade e atendimento humano.`
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

- Backup: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/product-seo/nike-mind-001-pearl-pink-20260617T142334Z/backup-before.json`
- Rollback payload: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/product-seo/nike-mind-001-pearl-pink-20260617T142334Z/rollback-payload.json`
- QA: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/product-seo/nike-mind-001-pearl-pink-20260617T142334Z/qa-after.json`

Rollback: executar `productUpdate` com o `seo` e `descriptionHtml` salvos em `rollback-payload.json`.

## Revisão de impacto

- D+7: 2026-06-24
- D+14: 2026-07-01

values_printed=false
