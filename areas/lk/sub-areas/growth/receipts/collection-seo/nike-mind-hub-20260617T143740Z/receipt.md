# Receipt — Collection SEO/FAQ — Nike Mind Hub

Timestamp UTC: 20260617T143740Z

Status: OK / public QA mixed cache propagation

## Coleção

- Handle: `nike-mind-001`
- URL: `https://lksneakers.com.br/collections/nike-mind-001`
- Collection ID: `gid://shopify/Collection/463377826014`
- Products count read-only before/after target: 18

## Aprovação

Lucas aprovou aplicar na coleção `/collections/nike-mind-001` somente `seo.title`, `seo.description` e descrição/FAQ da coleção conforme o packet Nike Mind Hub Collection 2026-06-17, sem mexer em produtos, preço, estoque, desconto, feed/GMC, campanhas, theme production, checkout, Klaviyo/WhatsApp ou outras coleções/produtos, com backup, QA, rollback e revisão D+7/D+14.

## Escopo executado

- `seo.title`: `Nike Mind 001 e 002 Original no Brasil | LK`
- `seo.description`: `Nike Mind 001 e 002 original no Brasil: compare slides e sneakers Nike Mind com curadoria LK, autenticidade e atendimento humano para escolher modelo.`
- `descriptionHtml`: bloco answer-first + FAQ aprovado

## Escopo bloqueado / não alterado por este script

- produtos da coleção
- preço
- estoque
- desconto
- feed/GMC
- campanhas
- theme production
- checkout
- Klaviyo/WhatsApp
- outras coleções/produtos

## QA

- Admin readback: OK
- Público: mixed cache propagation
- Pass counts: {"title_new": 3, "meta_new": 3, "copy_new": 3, "faq_new": 6, "h1_marker": 6}

## Backup e rollback

- Backup: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/collection-seo/nike-mind-hub-20260617T143740Z/backup-before.json`
- Rollback payload: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/collection-seo/nike-mind-hub-20260617T143740Z/rollback-payload.json`
- QA: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/collection-seo/nike-mind-hub-20260617T143740Z/qa-after.json`

Rollback: executar `collectionUpdate` com `seo` e `descriptionHtml` salvos em `rollback-payload.json`.

## Revisão de impacto

- D+7: 2026-06-24
- D+14: 2026-07-01

values_printed=false
