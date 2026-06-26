# Receipt — correção DEV NB9060 LKGOC título/subtítulo

Data UTC: 2026-06-05T10:13:00Z

## Aprovação
Lucas aprovou explicitamente a correção no DEV em conversa atual.

## Escopo executado
Correção visual mobile do Full LKGOC New Balance 9060 para herdar o contrato final do gold source New Balance 204L.

## Ambiente
- Tema: `lk-new-theme/dev`
- Theme ID: `155065450718`
- Role verificado por API antes do write: `unpublished`
- Produção/main: não tocada.

## Asset alterado
- `sections/lk-collection.liquid`

## Patch aplicado
Inserido CSS DEV:
- `lk-goc-9060-mobile-title-headline-contract-20260605`

O CSS aplica ao 9060 o mesmo contrato mobile da 204L para:
- `.coll-banner__title`
- `.lk-collection-v2__headline`

## QA after — mobile 390px
Status: `True`

### H1 coleção
9060:
- x: `16`
- font-size: `40px`
- line-height: `40.8px`
- padding: `0px`
- letter-spacing: `-2.2px`

204L:
- x: `16`
- font-size: `40px`
- line-height: `40.8px`
- padding: `0px`
- letter-spacing: `-2.2px`

### Headline/subtítulo
9060:
- x: `16`
- font-size: `31px`
- line-height: `31px`
- padding: `0px`
- letter-spacing: `-1.395px`

204L:
- x: `16`
- font-size: `31px`
- line-height: `31px`
- padding: `0px`
- letter-spacing: `-1.395px`

## Evidências
- `new-balance-9060-mobile-after.png`
- `new-balance-204l-mobile-after.png`
- `mobile-title-headline-compare-after.json`
- `readback-qa.json`

## Rollback
Restaurar `sections__lk-collection.liquid.before` neste mesmo diretório para `sections/lk-collection.liquid` no tema DEV.
