# Receipt — Rollback NB530 visual errado

Data: 2026-06-09

## Motivo
Lucas enviou evidência visual mostrando que a implementação NB530 LKGOC continuava totalmente errada:
- topo preto grande demais;
- composição de imagens/collage desalinhada;
- sensação visual distante do padrão aprovado;
- tentativa técnica validava DOM, mas falhava no padrão visual.

## Ação executada
- Revertido commit `04e2134 Implement single-section LKGOC mode for NB530`.
- Novo commit rollback: `a637f43`.
- Push feito para branch `hermes/lkgoc-shopify-native-v1-nb530-test`.
- Tema DEV/unpublished restaurado a partir do estado revertido:
  - `sections/lk-collection.liquid`
  - `templates/collection.lkgoc.json`
- Assets experimentais separados confirmados/deletados:
  - `sections/lk-goc-collection-hero.liquid`
  - `sections/lk-goc-collection-guide.liquid`

## Validação pós-rollback
- `lk-lkgoc-hero-media`: 0
- `coll-banner--lkgoc`: 0
- `lk-guia-new-balance-530-lkgoc`: 0
- `Liquid error`: 0

## Aprendizado obrigatório
QA técnico de DOM não basta. Próxima tentativa deve começar por copiar o padrão visual aprovado existente, não criar uma nova composição. Antes de codar, mapear screenshot/DOM do 204L aprovado e reproduzir somente sua estrutura visual, sem inventar layout.
