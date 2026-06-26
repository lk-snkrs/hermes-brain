# Receipt — Rollback NB530 teste LKGOC por hero duplicado

Data: 2026-06-09

## Motivo
Lucas identificou corretamente que o teste Shopify-native NB530 duplicou o HERO ao criar uma section `lk-goc-collection-hero` separada acima do fluxo visual existente da collection.

## Ação
- Revertido commit `593eab9 Create Shopify-native LKGOC collection test for NB530`.
- Novo commit rollback: `c557765`.
- Push feito para branch `hermes/lkgoc-shopify-native-v1-nb530-test`.
- Tema DEV/unpublished restaurado:
  - `sections/lk-collection.liquid`
  - `templates/collection.lkgoc.json`
- Assets experimentais deletados do tema DEV:
  - `sections/lk-goc-collection-hero.liquid`
  - `sections/lk-goc-collection-guide.liquid`

## Estado
- Production não alterada.
- `template_suffix` de collection não alterado.
- Experimento com hero separado encerrado.

## Aprendizado
O LKGOC escalável não pode adicionar um segundo hero acima da collection. A próxima versão deve usar apenas um HERO: ou adaptar o topo existente da `lk-collection`, ou transformar o bloco visual 204L aprovado em uma única section que substitui o topo, sem manter o banner/hero anterior.
