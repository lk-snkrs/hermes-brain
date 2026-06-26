# Receipt DEV — LKGOC P0 Nike x Jacquemus Moon Shoe SP

Data UTC: 2026-06-05T20:14:34.018585+00:00
Tema DEV: `155065450718` (`unpublished` verificado)
Handle: `nike-x-jacquemus-moon-shoe-sp`

## Fonte de priorização

- Score de marca/modelo corrigido por LK Growth: Nike #1 em receita 90d; Moon Shoe/Jacquemus é o maior modelo mapeado.
- Arquivo de prioridade: `work/lkgoc-priority-brand-score-20260605/lkgoc-priority-list-brand-score-corrected.md`.

## Assets alterados no DEV

- `snippets/lk-goc-collection.liquid`
  - Adicionado branch hero `nike-x-jacquemus-moon-shoe-sp`.
  - Adicionado branch guide `nike-x-jacquemus-moon-shoe-sp`.
  - Ajuste desktop de alinhamento específico Moon Shoe: collage `translateY(-160px)`.
- `sections/lk-collection.liquid`
  - Para Moon Shoe, hero agora chama `render 'lk-goc-collection', part: 'hero'`.
  - Pós-grid para Moon Shoe chama `render 'lk-goc-collection', part: 'guide'`.
  - Removida Moon Shoe do branch legado Phase 1 para evitar duplicidade.
- `templates/collection.jacquemus-nike.json`
  - Criado no DEV para o template suffix existente da coleção renderizar `lk-collection`.
- `snippets/lk-goc-guide-contract.liquid`
  - Criado stub guard para eliminar render legado ausente.
- `snippets/lk-goc-title-headline-contract-v2.liquid`
  - Criado stub guard para eliminar render legado ausente.

## QA DEV

Desktop 1440px:
- Hero LKGOC: OK
- Guide LKGOC: OK
- Liquid error: false
- Something went wrong: false
- Read more desktop: oculto
- `.coll-rich-content`: ausente
- Delta imagens/breadcrumb: `0px`
- H2: `Collab escultural, energia de fenômeno.`

Mobile 390px:
- Hero LKGOC: OK
- Guide LKGOC: OK
- Liquid error: false
- Something went wrong: false
- Read more: visível no mobile
- `.coll-rich-content`: ausente

## Preview

https://lk-sneakerss.myshopify.com/collections/nike-x-jacquemus-moon-shoe-sp?preview_theme_id=155065450718

## Rollback

Restaurar os arquivos `.before` em:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/lkgoc-moon-shoe-p0-20260605`

## Status

DEV pronto para validação Lucas. Production não alterada.


## Correção visual — imagens em uso, não packshot

Data UTC: 2026-06-05T21:04:53.011542+00:00

Após feedback do Lucas, o hero Moon Shoe foi corrigido no DEV para seguir a regra visual LKGOC: **usar pessoas usando o produto / contexto editorial**, não imagens isoladas do produto.

Readback/QA:
- Hero com 3 imagens editoriais/de uso.
- Packshot/product-only no hero: false.
- Desktop QA: hero/guide OK, Liquid error false, deltaTop 0, “Ler mais” oculto.
- Mobile QA: hero/guide OK, Liquid error false.

Regra criada: `rules/REGRA-LKGOC-IMAGENS-EM-USO-NAO-PACKSHOT.md`.


## Correção visual — alinhamento bottom

Data UTC: 2026-06-05T21:23:18.807269+00:00

Após feedback do Lucas, o enquadramento das imagens editoriais do hero Moon Shoe foi corrigido para alinhar pelo **bottom**, não pelo meio.

QA computado:
- `object-position`: `50% 100%` nas 3 imagens do hero.
- Packshot/product-only no hero: false.
- Desktop: hero/guide OK, Liquid error false, deltaTop 0, “Ler mais” oculto.
- Mobile: hero/guide OK, Liquid error false.

Regra criada: `rules/REGRA-LKGOC-IMAGENS-ALINHAMENTO-BOTTOM.md`.


## Correção — guia pós-grid voltou ao padrão LKGOC

Data UTC: 2026-06-05T21:55:42.241760+00:00

Após feedback do Lucas, o guide da Moon Shoe foi refeito para copiar/adaptar o padrão aprovado das coleções-base.

Correções:
- ID corrigido para `lk-guia-nike-x-jacquemus-moon-shoe-sp`.
- Grid com `lk-guide-standard-grid`.
- Card com `lk-guide-standard-card lk-guide-standard-card--wide`.
- FAQ com `lk-guide-standard-faq`.
- Media com `lk-guide-standard-media`.
- CTA com `lk-guide-standard-panel__cta`.
- Copy ajustada para padrão comercial: modelo + styling/compra segura, produto-first, orientação humana LK.

QA específico:
- Guide standard: true.
- FAQ count: 4.
- Liquid error: false.
- `.coll-rich-content`: false.

Regra criada: `rules/REGRA-LKGOC-GUIA-POS-GRID-PADRAO.md`.


## Correção — FAQ duplicada removida visualmente

Data UTC: 2026-06-05T22:07:31.238709+00:00

Após feedback do Lucas, foi confirmado que havia duas áreas de pergunta: a FAQ correta dentro do guia editorial LKGOC e uma FAQ legada `.coll-faq` fora do guia.

Correção DEV:
- Mantida visível apenas a FAQ dentro de `#lk-guia-nike-x-jacquemus-moon-shoe-sp`.
- FAQ legada `.coll-faq`/`.collection-faq`/`.faq-section` ocultada para esta coleção.

QA específico:
- FAQ dentro do guia: visível.
- Perguntas/details dentro do guia: 4.
- `details` visíveis fora do guia: 0.
- `.coll-faq` fora do guia: presente no DOM, mas não visível.
- Liquid error: false.

Regra criada: `rules/REGRA-LKGOC-FAQ-UNICA-DENTRO-DO-GUIA.md`.
