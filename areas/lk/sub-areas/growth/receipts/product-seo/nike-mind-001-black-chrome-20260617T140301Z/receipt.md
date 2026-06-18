# Receipt — Product SEO/FAQ — Nike Mind 001 Black Chrome

Timestamp UTC: 20260617T140301Z

Status: OK / public QA status 200

## Produto

- Handle: `slide-nike-mind-001-black-chrome-preto`
- URL: `https://lksneakers.com.br/products/slide-nike-mind-001-black-chrome-preto`
- Product ID: `gid://shopify/Product/9102273642718`

## Aprovação

Lucas aprovou aplicar somente `seo.title`, `seo.description` e descrição/FAQ do produto conforme o packet Next P1 Factory 2026-06-17, sem mexer em preço, estoque, desconto, feed/GMC, campanhas, theme production fora do escopo, checkout, Klaviyo/WhatsApp ou outros produtos, com backup, QA, rollback e revisão D+7/D+14.

## Escopo executado

- `seo.title`: `Nike Mind 001 Black Chrome Original no Brasil | LK`
- `seo.description`: `Nike Mind 001 Black Chrome original no Brasil: slide escultural da linha Nike Mind com curadoria exclusiva LK, autenticidade e atendimento humano.`
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
- Público HTTP: 200
- Title/meta público: title_ok=True; meta_ok=False
- FAQ público: faq_ok=False
- Marcador de produto: product_marker_ok=True

## Backup e rollback

- Backup: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/product-seo/nike-mind-001-black-chrome-20260617T140301Z/backup-before.json`
- Rollback payload: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/product-seo/nike-mind-001-black-chrome-20260617T140301Z/rollback-payload.json`
- QA: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/product-seo/nike-mind-001-black-chrome-20260617T140301Z/qa-after.json`

Rollback: executar `productUpdate` com o `seo` e `descriptionHtml` salvos em `rollback-payload.json`.

## Revisão de impacto

- D+7: 2026-06-24
- D+14: 2026-07-01

Métricas: GSC query+URL para `nike mind 001` e `chinelo nike mind 001`, page CTR/cliques/impressões/posição, GA4/Shopify organic landing/PDP/add-to-cart/receita quando disponível.

values_printed=false
