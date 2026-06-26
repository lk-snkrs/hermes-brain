# Receipt — NB530 LKGOC existente como clone 204L verificado

Data: 2026-06-09

## Contexto
Após rollback das tentativas erradas, foi verificado o caminho correto: não criar layout novo. A collection New Balance 530 já possui implementação LKGOC baseada no padrão visual da 204L.

## Implementação existente encontrada
Em `sections/lk-collection.liquid`:
- `{%- render 'lk-goc-new-balance-530-hero-204l-clone' -%}`

Snippets existentes:
- `snippets/lk-goc-new-balance-530-hero-204l-clone.liquid`
- `snippets/lk-goc-new-balance-530-guide-panel.liquid`

## URLs verificadas
DEV:
- `https://lksneakers.com.br/collections/new-balance-530?preview_theme_id=155065450718`

Production:
- `https://lksneakers.com.br/collections/new-balance-530`

## Resultado QA
DEV mobile/desktop:
- roleUnpublished: true
- banner: true
- clone `.lk-goc-coll-preview--530`: true
- cloneCount: 1
- cloneImgs: 3
- grid: true
- guide `#lk-guia-new-balance-530`: true
- productLinks: 49
- orderOk: true
- Liquid error: false
- termos proibidos estoque/pronta entrega: false

Production mobile/desktop:
- clone `.lk-goc-coll-preview--530`: true
- cloneCount: 1
- cloneImgs: 3
- grid: true
- guide: true
- orderOk: true
- Liquid error: false

## Evidências
- `/opt/data/profiles/lk-collection-optimizer/output/lkgoc-shopify-native-nb530-test-20260609/nb530-existing-clone-dev-mobile.png`
- `/opt/data/profiles/lk-collection-optimizer/output/lkgoc-shopify-native-nb530-test-20260609/nb530-existing-clone-dev-desktop.png`
- `/opt/data/profiles/lk-collection-optimizer/output/lkgoc-shopify-native-nb530-test-20260609/nb530-existing-clone-prod-mobile.png`
- `/opt/data/profiles/lk-collection-optimizer/output/lkgoc-shopify-native-nb530-test-20260609/nb530-existing-clone-prod-desktop.png`

## Decisão
Não houve novo write. O caminho correto para próximas coleções deve partir deste padrão existente: snippet clone 204L + guide panel dentro de `lk-collection`, antes de qualquer tentativa de abstração Shopify-native.
