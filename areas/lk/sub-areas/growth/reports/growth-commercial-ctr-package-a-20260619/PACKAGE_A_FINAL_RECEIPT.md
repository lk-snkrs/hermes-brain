# LK Growth — Pacote A CTR Comercial — Receipt — 2026-06-19

- Aprovação: “aprovo pacote A”.
- Escopo: SEO title/meta + microcopy/FAQ/intro em 3 páginas comerciais priorizadas por GSC + GA4.
- values_printed=false.

## Writes executados

- `product` `slide-nike-mind-001-black-chrome-preto` — id `9102273642718`
  - body changes: [{'action': 'append_product_ctr_faq_block', 'kind': 'nike_mind'}]
  - SEO changes: 2
- `product` `crocs-classic-clog-x-the-cars-lightning-mcqueen-vermelho` — id `8294160924894`
  - body changes: [{'action': 'append_product_ctr_faq_block', 'kind': 'crocs_mcqueen'}]
  - SEO changes: 1
- `collection` `onitsuka-tiger-todos-os-modelos` — id `458490904798`
  - body changes: [{'action': 'append_collection_intro_links_block'}]
  - SEO changes: 2

## Admin readback

- `slide-nike-mind-001-black-chrome-preto` — growth block `True`; title `Nike Mind 001 Black Chrome Original | LK Sneakers`; meta `Nike Mind 001 Black Chrome original na curadoria LK: slide escultural, autenticidade verificada e atendimento humano para orientar tamanho e estilo.`
- `crocs-classic-clog-x-the-cars-lightning-mcqueen-vermelho` — growth block `True`; title `Crocs Relâmpago McQueen Original | LK Sneakers`; meta `Crocs Relâmpago McQueen original na curadoria LK: Classic Clog The Cars, peça colecionável, autenticidade e atendimento humano para detalhes.`
- `onitsuka-tiger-todos-os-modelos` — growth block `True`; title `Onitsuka Tiger Original no Brasil | Mexico 66 | LK`; meta `Onitsuka Tiger original no Brasil: Mexico 66, SD, Sabot e modelos selecionados com curadoria LK, autenticidade e atendimento humano.`

## Public verification

- `nike_mind` — HTTP `200`; title_ok `True`; text_ok `True`; title `Nike Mind 001 Black Chrome Original | LK Sneakers`
- `crocs_mcqueen` — HTTP `200`; title_ok `True`; text_ok `True`; title `Crocs Relâmpago McQueen Original | LK Sneakers`
- `onitsuka_collection` — HTTP `200`; title_ok `False`; text_ok `False`; title `Onitsuka Tiger Original no Brasil | Mexico 66 e LK`

Observação:
- As duas PDPs (`Nike Mind 001 Black Chrome` e `Crocs McQueen`) validaram publicamente com title/meta/bloco novos no polling final.
- A collection `onitsuka-tiger-todos-os-modelos` está correta no Admin API, mas o storefront ainda serviu o title/meta/body anterior no último polling. Isso parece propagação/cache da Shopify; não houve erro de write nem duplicidade de collection pública.

## Collection Onitsuka admin check

- endpoint `smart_collections` id `458490904798` updated `2026-06-19T16:06:26-03:00` body_has_growth `True`
  - `title_tag`: Onitsuka Tiger Original no Brasil | Mexico 66 | LK
  - `description_tag`: Onitsuka Tiger original no Brasil: Mexico 66, SD, Sabot e modelos selecionados com curadoria LK, autenticidade e atendimento humano.

## Rollback

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/growth-commercial-ctr-package-a-20260619/rollback-before-package-a.json`

## Arquivos

- Receipt JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/growth-commercial-ctr-package-a-20260619/execution-receipt-package-a.json`
- Public verify: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/growth-commercial-ctr-package-a-20260619/public-final-poll-package-a.json`
- Collection admin check: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/growth-commercial-ctr-package-a-20260619/collection-duplication-admin-check.json`
