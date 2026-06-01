# LK Sneakers — Production publish receipt

Data UTC: 2026-05-31 21:44–21:47

## Escopo
- Tema Production: `155065417950` (`lk-new-theme/production`, role `main`)
- Asset: `sections/lk-collection.liquid`
- Alteração segmentada para coleção `/collections/sneakers`
- Sem alterações em produto, preço, estoque, feed/GMC, campanha, Klaviyo ou WhatsApp.

## Aprovação
Lucas aprovou no turno atual: “Ótimo aprovar, fazer merge na branch Production”.

## Publicado em Production
- Hero da coleção Sneakers com 3 fotos novas da loja:
  - `GF_3805_hi.jpg?v=1728506174`
  - `GF_3812_hi.jpg?v=1728506174`
  - `GF_3840_hi.jpg?v=1728506174`
- Intro SEO/GEO com dois parágrafos dentro do “Ler mais”.
- Guia editorial pós-grid `lk-sneakers-hub-panel`.
- FAQ visível + `FAQPage` JSON-LD.
- Links internos para New Balance, Adidas, Nike, Air Jordan, Onitsuka Tiger, lançamentos e Sale.
- Foto antiga `Loja-LK.jpg?v=1705163797` removida/substituída.
- Trust bar visualmente removida/ocultada quando o hero de fotos da Sneakers está presente.

## Verificação final
Fresh verification após o write:
- `api_prod_has_hero_photos`: true
- `api_prod_has_guide_faq`: true
- `api_prod_has_no_trustbar_css`: true
- `api_prod_old_photo_absent`: true
- `public_status_200`: true
- `public_has_hero_photos`: true
- `public_has_guide_faq`: true
- `public_has_no_trustbar_css`: true
- `public_old_photo_absent`: true

## URL live
https://www.lksneakers.com.br/collections/sneakers

## Observação
O primeiro fetch público veio com HTML antigo por cache/propagação. Após aguardar e revalidar com cache-bust, os marcadores públicos apareceram corretamente.

## Rollback
Restaurar o snapshot:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-production/sneakers-production-publish-20260531T214417Z/production.before.liquid`

Receipt técnico:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-production/sneakers-production-publish-20260531T214417Z/receipt.json`
