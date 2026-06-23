# Receipt final — Sequência aprovada 1/2/3 — Alo, Crocs, GMC

- Data UTC: 2026-06-22T17:37:55.546056+00:00
- Aprovação Lucas: `APROVO OS 3 EM SEQUENCIA, 1 2 e 3`
- Writes externos executados: Shopify production + GMC Merchant API.
- values_printed=false.
- Estoque/preço/campanhas/Klaviyo/ads: não alterados.

## 1. Alo Yoga redirect

### Write

- Shopify URL redirect atualizado/criado:
  - `/collections/alo-yoga` → `/collections/alo-yoga-1`

### QA público

- Request `/collections/alo-yoga` retorna 301 para `/collections/alo-yoga-1`.
- Final HTTP: 200.
- Canonical final: `https://lksneakers.com.br/collections/alo-yoga-1`.
- H1: 1 (`Alo Yoga`).
- Liquid error: false.

### Rollback

- Restaurar/remover redirect ID `440823415006` conforme backup `backup-before-alo-crocs.json`.

## 2. Crocs Relâmpago McQueen collection FAQ lite

### Writes

- `collectionUpdate` em `/collections/crocs-relampago-mcqueen`:
  - descriptionHtml com intro citável + 4 FAQs.
- Theme production asset:
  - `snippets/lk-growth-geo-faq-schema.liquid`
  - branch escopado para `/collections/crocs-relampago-mcqueen` com `FAQPage` JSON-LD.

### QA público

- HTTP: 200.
- H1: 1 (`Crocs Relâmpago McQueen`).
- Canonical: `https://lksneakers.com.br/collections/crocs-relampago-mcqueen`.
- FAQPage string: 1.
- FAQPage JSON-LD: 1.
- Questions: 4.
- Intro nova presente: true.
- Liquid error: false.

### Observação técnica

- Primeiro PUT do asset de schema retornou 422/sem readback; foi corrigido com patch menor e readback posterior confirmou marker e aplicação.

### Rollback

- Restaurar `descriptionHtml` da collection e asset Liquid pelo backup `backup-before-alo-crocs.json`.

## 3. GMC micro-piloto link_template — 10 offers

### Write

- Merchant API `productInputs.patch` em 10 offers locais/LIA.
- Campos alterados:
  - `productAttributes.linkTemplate`
  - `productAttributes.mobileLinkTemplate`
  - `productAttributes.adsRedirect`
- Template aplicado: link PDP + `store_code={store_code}`.
- Não houve write em Shopify/preço/estoque/campanha.

### Resultado

- Targets loaded: 10.
- URL checks OK: 10.
- Patch OK: 10.
- Patch failed: 0.
- Patch response link_template OK: 10.
- Immediate processed readback link_template OK: 10.
- Immediate remaining issue: 0.
- Delayed 20s link_template OK: 10/10.
- Delayed 20s remaining issue: 0.
- Read errors: 0.

### Rollback

- Usar `before_products.json` para restaurar valores anteriores nos mesmos ProductInputs.
- Arquivo rollback base: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-micro-pilot-10-20260622T/before_products.json`.

## Evidências

### Shopify Alo/Crocs

Pasta:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-production/alo-crocs-approved-20260622T`

Arquivos principais:
- `backup-before-alo-crocs.json`
- `apply-receipt-alo-crocs.json`
- `schema-fix-receipt.json`
- `public-qa-after-alo-crocs.json`

### GMC

Pasta:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-micro-pilot-10-20260622T`

Arquivos principais:
- `APPROVAL_PACKET.md`
- `targets.json`
- `before_products.json`
- `patch_results.json`
- `immediate_readback.json`
- `delayed_readback_20s.json`
- `RECEIPT.md`

## Próximos controles

- Recheck GMC em D+1 para confirmar que Simprosys não sobrescreveu o campo.
- Medir impacto orgânico de Alo/Crocs no próximo ciclo GSC.
- Não escalar GMC para lote maior sem novo packet/approval.
