# Receipt — NB530 alinhamento visual com 204L em DEV

Data: 2026-06-09

## Motivo
Lucas apontou corretamente que a NB530 estava diferente da 204L, apesar de existir como clone. Foi feita comparação por DOM/medidas reais entre 204L e 530.

## Divergências encontradas
Antes:
- collage desktop 204L: 450px
- collage desktop 530: 340px
- guide 204L: 1376px / left 32px
- guide 530: 1180px / left 130px
- headline 530 quebrava em 2 linhas

## Correção aplicada em DEV
Assets:
- `snippets/lk-goc-new-balance-530-hero-204l-clone.liquid`
- `sections/lk-collection.liquid`

Mudanças:
- altura desktop do collage 530 travada em 450px, igual ao gold 204L;
- margin/transform do collage 530 alinhados ao comportamento 204L;
- headline 530 encurtada para preservar uma linha no desktop;
- guide 530 alinhado ao contrato do guide 204L: width 1376px, left 32px, grid/padding compatíveis.

## Medição pós-correção DEV
Desktop:
- 204L collage: 450px
- 530 collage: 450px
- 204L guide width: 1376px
- 530 guide width: 1376px
- 204L guide left: 32px
- 530 guide left: 32px
- headline desktop: 38.75px nos dois

## Branch
- `hermes/lkgoc-shopify-native-v1-nb530-test`
- commit: `Align NB530 LKGOC visual contract with 204L`

## Preview
- `https://lksneakers.com.br/collections/new-balance-530?preview_theme_id=155065450718`

## Observação
Production não alterada. Correção aplicada apenas ao tema DEV/unpublished.
