# Receipt — LKGOC NB530 single-section DEV

Data: 2026-06-09

## Pedido
Fazer a collection sem duplicar HERO.

## Arquitetura correta testada
- `templates/collection.lkgoc.json` contém somente a section `lk-collection`.
- `sections/lk-collection.liquid` opera em `lkgoc_template_mode: true`.
- O HERO é o próprio `coll-banner` em modo LKGOC, não uma section separada.
- Guide LKGOC é renderizado pós-grid dentro da mesma section, substituindo o guide antigo da 530 neste modo.

## Collection teste
- `new-balance-530`
- Preview DEV:
  `https://lksneakers.com.br/collections/new-balance-530?preview_theme_id=155065450718&view=lkgoc`

## DEV Shopify
Tema:
- `lk-new-theme/dev`
- ID: `155065450718`
- role: `unpublished`

## Branch
- `hermes/lkgoc-shopify-native-v1-nb530-test`
- commit: `Implement single-section LKGOC mode for NB530`

## QA
Arquivo:
`/opt/data/profiles/lk-collection-optimizer/output/lkgoc-shopify-native-nb530-test-20260609/qa_nb530_single_section_lkgoc_result.json`

Mobile:
- roleUnpublished: true
- Liquid error: false
- h1Count: 1
- separate hero `.lk-goc-v1-hero`: 0
- banner LKGOC: true
- bannerCount: 1
- heroMedia: 1
- heroImages: 3
- grid: true
- guide: true
- old guide panel: 0
- guideBullets: 4
- gridBeforeGuide: true
- inherited204l: false
- termos proibidos: false

Desktop:
- mesmos critérios OK.

## Evidências
- Mobile: `/opt/data/profiles/lk-collection-optimizer/output/lkgoc-shopify-native-nb530-test-20260609/nb530-mobile-single-section-lkgoc.png`
- Desktop: `/opt/data/profiles/lk-collection-optimizer/output/lkgoc-shopify-native-nb530-test-20260609/nb530-desktop-single-section-lkgoc.png`

## Observação
Production não alterada. `template_suffix` da collection não alterado. Teste via DEV preview `view=lkgoc`.
