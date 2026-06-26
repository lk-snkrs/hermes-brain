# Receipt — Production merge LKGOC New Balance 530

Data/hora: 2026-06-05T16:27:09
Aprovador: Lucas Cimino, aprovação no Telegram: "Aprovo".
Tema Production: `lk-new-theme/production` — ID `155065417950` — role verificado: `main`.
URL: https://lksneakers.com.br/collections/new-balance-530

## Escopo publicado
- `sections/lk-collection.liquid`
- `snippets/lk-goc-new-balance-530-hero-204l-clone.liquid`
- `snippets/lk-goc-new-balance-530-guide-panel.liquid`

## Mudança
- Coleção New Balance 530 publicada como Full LKGOC no padrão visual/editorial 204L.
- Hero editorial com classe `lk-goc-coll-preview--530`.
- Guia pós-grid LKGOC com FAQ editorial e FAQPage schema.
- Descrição/FAQ legado da collection suprimido para evitar duplicidade e termos operacionais antigos.
- Contrato mobile class-based para H1 e headline, sem selector por aria-label/handle/ID para override visual.

## Observação técnica
- `sections/lk-collection.liquid` estava próximo ao limite rígido de 256KB da Shopify.
- Para viabilizar o merge, foram removidos comentários Liquid não-renderizados do asset principal.
- Sem impacto visual/renderizado esperado.
- Section final aceita pela Shopify: 260614 bytes reportados no write; abaixo do limite de 262144 bytes.

## Backups
- Section Production antes do merge: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/new-balance-530-lkgoc-full-20260605/production-merge-approved-20260605/prod-before-final__sections__lk-collection.liquid`
- Snippets 530 não existiam antes em Production (404), portanto rollback é remover snippets e repor section.

## QA Production público
- Mobile 390x844: passou.
  - H1 New Balance 530 40px.
  - Headline 31px Cormorant.
  - Hero 530 presente.
  - Guia LKGOC presente.
  - FAQPage schema presente.
  - Sem FAQ legado/textos operacionais antigos renderizados.
- Desktop 1440x1200: passou.
  - Hero 530 presente.
  - Guia em grid LKGOC.
  - FAQPage schema presente.
- Arquivo QA: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/new-balance-530-lkgoc-full-20260605/production-merge-approved-20260605/qa-prod-530-summary.json`
- Prints:
  - `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/new-balance-530-lkgoc-full-20260605/production-merge-approved-20260605/prod-new-balance-530-390.png`
  - `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/new-balance-530-lkgoc-full-20260605/production-merge-approved-20260605/prod-new-balance-530-1440.png`

## Rollback
1. Repor `sections/lk-collection.liquid` com `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/new-balance-530-lkgoc-full-20260605/production-merge-approved-20260605/prod-before-final__sections__lk-collection.liquid`.
2. Remover ou ignorar:
   - `snippets/lk-goc-new-balance-530-hero-204l-clone.liquid`
   - `snippets/lk-goc-new-balance-530-guide-panel.liquid`
3. Validar URL pública e ausência de `.lk-goc-coll-preview--530`.

## Impact review
Revisar em aproximadamente 7 dias: 2026-06-12.
Métricas recomendadas: GA4 sessões/conversão/receita da collection, GSC impressões/cliques/CTR/posição para queries New Balance 530, eventos PDP→cart→checkout e comparação com pré-merge.
