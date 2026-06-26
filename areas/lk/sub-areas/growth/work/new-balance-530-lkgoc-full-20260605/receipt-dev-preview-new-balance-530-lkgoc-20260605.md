# LKGOC New Balance 530 — DEV preview receipt

Data: 2026-06-05T12:52:16
Tema DEV: `lk-new-theme/dev` — ID `155065450718` — role verificado: `unpublished`.
Collection: `/collections/new-balance-530`.
Preview: `https://lksneakers.com.br/collections/new-balance-530?preview_theme_id=155065450718`

## Assets alterados em DEV
- `sections/lk-collection.liquid`
- `snippets/lk-goc-new-balance-530-hero-204l-clone.liquid`
- `snippets/lk-goc-new-balance-530-guide-panel.liquid`

## Padrão aplicado
- LKGOC Full baseado no gold source New Balance 204L.
- Namespace estrutural `lk-goc-*`, mantendo aliases canônicos `lk-204l-*` onde o padrão visual aprovado depende deles.
- Hero editorial, collage visual, guide pós-grid, FAQPage schema e CTA para guia completo.
- FAQ legado da descrição nativa não renderizado para 530, evitando duplicidade com o guia LKGOC.

## QA executado
- Mobile 390x844: H1 40px, headline 31px Cormorant, hero 530, guide LKGOC, contratos presentes, sem FAQ legado visível/renderizado.
- Desktop 1440x1200: hero 530, guide grid com paridade 204L, contratos presentes.
- Screenshots:
  - `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/new-balance-530-lkgoc-full-20260605/new-balance-530-390-dev-lkgoc.png`
  - `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/new-balance-530-lkgoc-full-20260605/new-balance-530-1440-dev-lkgoc.png`
- JSON QA: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/new-balance-530-lkgoc-full-20260605/qa-dev-530-summary.json`

## Rollback DEV
- Repor `sections/lk-collection.liquid` a partir de `dev-before__sections__lk-collection.liquid`.
- Remover/ignorar snippets `lk-goc-new-balance-530-*`.

## Para Production
Exige aprovação explícita de Lucas. Antes do merge: backup Production de `sections/lk-collection.liquid`, write dos snippets, readback, validação CDN e receipt de produção.
