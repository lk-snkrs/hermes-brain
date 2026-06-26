# Receipt — Teste LKGOC Shopify-native com New Balance 530

Data: 2026-06-09
Dono: LK Collection Optimizer

## Pedido Lucas
Seguir com o LKGOC correto, documentado e testar com a coleção New Balance 530/530L.

## Collection usada
Handle real encontrado na Shopify:
- `new-balance-530`
- id: `430151598302`
- title: `New Balance 530`
- `template_suffix`: `""` no objeto original.

## Guardrail
Não alterado `template_suffix` da collection, porque este campo é global na Shopify. Como o template `collection.lkgoc` ainda só existe no DEV/unpublished, mudar a collection poderia afetar Production. Teste feito por preview DEV com `view=lkgoc`.

## Implementação Shopify-native
Branch:
- `hermes/lkgoc-shopify-native-v1-nb530-test`

Commit:
- `593eab9 Create Shopify-native LKGOC collection test for NB530`

Assets criados/alterados:
- `templates/collection.lkgoc.json`
- `sections/lk-goc-collection-hero.liquid`
- `sections/lk-goc-collection-guide.liquid`
- `sections/lk-collection.liquid`

Arquitetura testada:
- `collection.lkgoc.json`
  - section `lkgoc_hero`: `lk-goc-collection-hero`
  - section `main`: `lk-collection` com `lkgoc_template_mode: true`
  - section `lkgoc_guide`: `lk-goc-collection-guide`
- `lk-collection` em `lkgoc_template_mode` foi ajustada para atuar como grid-only:
  - sem banner/descrição padrão;
  - sem trust strip do template base;
  - sem guides hardcoded antigos.

## DEV Shopify
Tema atualizado:
- `lk-new-theme/dev`
- theme ID: `155065450718`
- role: `unpublished`

Preview correto:
`https://lksneakers.com.br/collections/new-balance-530?preview_theme_id=155065450718&view=lkgoc`

## QA real
Arquivo QA:
`/opt/data/profiles/lk-collection-optimizer/output/lkgoc-shopify-native-nb530-test-20260609/qa_nb530_native_result.json`

Resultado mobile:
- roleUnpublished: true
- Liquid error: false
- h1: `New Balance 530: running retrô, conforto e proporção fácil`
- hero: true
- hero aria: `Contexto editorial New Balance 530`
- hero images: 3
- grid: true
- guide: true
- guide bullets: 4
- product links: 49
- gridBeforeGuide: true
- inherited204l: false
- linguagem proibida estoque/pronta entrega: false

Resultado desktop:
- roleUnpublished: true
- Liquid error: false
- hero: true
- grid: true
- guide: true
- product links: 49
- gridBeforeGuide: true
- inherited204l: false
- linguagem proibida estoque/pronta entrega: false

## Evidências visuais
- Mobile: `/opt/data/profiles/lk-collection-optimizer/output/lkgoc-shopify-native-nb530-test-20260609/nb530-mobile-shopify-native-lkgoc.png`
- Desktop: `/opt/data/profiles/lk-collection-optimizer/output/lkgoc-shopify-native-nb530-test-20260609/nb530-desktop-shopify-native-lkgoc.png`

## Observações
Este é um MVP Shopify-native com dados no JSON template. Para escala real, próxima fase deve migrar conteúdo para metafields/metaobjects de collection, conforme documentação Shopify.dev registrada no contrato.
