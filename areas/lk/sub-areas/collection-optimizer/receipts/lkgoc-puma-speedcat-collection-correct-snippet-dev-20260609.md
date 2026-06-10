# Receipt — Puma Speedcat Collection Correct / Snippet LKGOC DEV

Data: 2026-06-09  
Tema: `lk-new-theme/dev`  
Theme ID: `155065450718`  
Role: `unpublished`

## Correção de direção
Lucas corrigiu: o problema era a **collection**, não o Guia em `/pages`.

Diagnóstico aplicado:
- Gold ativo de collection: `LKGOC Gold Source — New Balance 204L Hero/Guide`.
- Arquitetura correta: `snippets/lk-goc-collection.liquid` com branch por handle e render via `sections/lk-collection.liquid`.
- Não usar a página Guia LK como referência para corrigir a collection.

## Assets alterados em DEV
- `snippets/lk-goc-collection.liquid`
  - adicionado branch hero `when 'puma-speedcat'` clonado do branch `new-balance-204l`.
  - adicionado branch guide `when 'puma-speedcat'` clonado do guide 204L.
  - preservado shell visual 204L: `lk-goc-coll-preview lk-goc-coll-preview--204l lk-204l-coll-preview`.
  - não foi criada classe visual `lk-goc-coll-preview--speedcat`.
- `sections/lk-collection.liquid`
  - adicionado `puma-speedcat` ao render LKGOC `part: 'hero'`.
  - adicionado `puma-speedcat` ao render LKGOC `part: 'guide'`.
  - adicionado desc override de banner para Speedcat.
- `templates/collection.puma-speedcat.json`
  - mantido alinhado ao template padrão de collection.

## QA readback
URL DEV:
`https://lksneakers.com.br/collections/puma-speedcat?preview_theme_id=155065450718`

Readback:
- status: `200`
- role unpublished: `1`
- `Liquid error`: `0`
- `Contexto editorial Puma Speedcat`: presente
- `Puma Speedcat: perfil baixo`: presente
- linguagem proibida `pronta entrega`: `0`
- linguagem proibida `estoque imediato`: `0`

## QA Playwright
Speedcat mobile:
- roleUnpublished: true
- liquid: false
- hero: true
- guide: true
- visibleBad: false
- heroClass: `lk-goc-coll-preview lk-goc-coll-preview--204l lk-204l-coll-preview`
- heroAria: `Contexto editorial Puma Speedcat`
- guideText: `Puma Speedcat: perfil baixo, herança motorsport e compra segura`
- cards: 3
- imgs: 3

Speedcat desktop:
- roleUnpublished: true
- liquid: false
- hero: true
- guide: true
- visibleBad: false
- heroClass: `lk-goc-coll-preview lk-goc-coll-preview--204l lk-204l-coll-preview`
- heroAria: `Contexto editorial Puma Speedcat`
- guideText: `Puma Speedcat: perfil baixo, herança motorsport e compra segura`
- cards: 3
- imgs: 3

## Evidências
- Mobile side-by-side: `/opt/data/profiles/lk-collection-optimizer/output/puma-speedcat-collection-correct-20260609/side-by-side-204l-vs-speedcat-mobile-collection-correct-20260609.png`
- Desktop side-by-side: `/opt/data/profiles/lk-collection-optimizer/output/puma-speedcat-collection-correct-20260609/side-by-side-204l-vs-speedcat-desktop-collection-correct-20260609.png`
- JSON QA: `/opt/data/profiles/lk-collection-optimizer/output/puma-speedcat-collection-correct-20260609/qa_collection_correct_result.json`

## Guardrail
Production não foi alterada. Qualquer promoção para `main` exige aprovação explícita de Lucas.
