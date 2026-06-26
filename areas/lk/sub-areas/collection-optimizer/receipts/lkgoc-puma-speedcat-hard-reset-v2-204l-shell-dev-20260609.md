# Receipt — Puma Speedcat Hard Reset V2 / 204L Shell DEV

Data: 2026-06-09  
Tema: `lk-new-theme/dev`  
Theme ID: `155065450718`  
Role: `unpublished`

## Status
Lucas reprovou a versão anterior: “Está errado ainda, está diferente. Corrigir do zero.”  
A execução anterior foi tratada como inválida. Foi feito hard reset visual do componente Speedcat no DEV.

## Correção aplicada
- Removido o modificador visual próprio `lk-goc-coll-preview--speedcat`.
- Speedcat agora usa exatamente o mesmo shell visual do 204L:
  - `lk-goc-coll-preview`
  - `lk-goc-coll-preview--204l`
  - `lk-204l-coll-preview`
- O bloco Speedcat foi reconstruído a partir do bloco real `{% if collection.handle == 'new-balance-204l' %}` de `sections/lk-collection.liquid`.
- O guia Speedcat foi reconstruído a partir de `snippets/lk-goc-new-balance-204l-guide-panel.liquid`.
- Para manter o CSS aprovado do guia 204L, o guia Speedcat usa o mesmo ID visual `lk-guia-new-balance-204l` dentro da página Speedcat.
- O template errado `templates/page.guia-puma-speedcat-lkgoc.json` permaneceu removido.

## Assets alterados em DEV
- `sections/lk-collection.liquid`
- `snippets/lk-goc-puma-speedcat-guide-panel.liquid`
- `templates/collection.puma-speedcat.json`

## Readback
URL: `https://lksneakers.com.br/collections/puma-speedcat?preview_theme_id=155065450718`

Readback HTTP:
- status: `200`
- role unpublished: `1`
- `Liquid error`: `0`
- `lk-goc-coll-preview--speedcat`: `0`
- `lk-goc-coll-preview--204l`: `18`
- `lk-204l-coll-preview`: `135`
- `lk-guia-new-balance-204l`: `57`

## QA Playwright
Mobile Speedcat:
- roleUnpublished: true
- liquid: false
- hero: true
- guide: true
- visibleBad: false
- heroClasses: `lk-goc-coll-preview lk-goc-coll-preview--204l lk-204l-coll-preview`
- guideId: `lk-guia-new-balance-204l`

Desktop Speedcat:
- roleUnpublished: true
- liquid: false
- hero: true
- guide: true
- visibleBad: false
- heroClasses: `lk-goc-coll-preview lk-goc-coll-preview--204l lk-204l-coll-preview`
- guideId: `lk-guia-new-balance-204l`

## Evidências
- Mobile side-by-side: `/opt/data/profiles/lk-collection-optimizer/output/puma-speedcat-hard-reset-20260609/side-by-side-204l-vs-speedcat-mobile-hard-reset-v2-20260609.png`
- Desktop side-by-side: `/opt/data/profiles/lk-collection-optimizer/output/puma-speedcat-hard-reset-20260609/side-by-side-204l-vs-speedcat-desktop-hard-reset-v2-20260609.png`
- JSON QA: `/opt/data/profiles/lk-collection-optimizer/output/puma-speedcat-hard-reset-20260609/qa_hard_reset_v2_result.json`

## Guardrail
Production não foi alterada. Qualquer promoção para `main` exige aprovação explícita de Lucas.
