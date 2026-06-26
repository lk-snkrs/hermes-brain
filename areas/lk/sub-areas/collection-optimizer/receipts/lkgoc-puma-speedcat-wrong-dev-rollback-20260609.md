# Receipt — Rollback Puma Speedcat wrong DEV implementation

Data: 2026-06-09

## Trigger
Lucas informou: "continua totalmente errado".

## Ação imediata
Rollback do último write em branch DEV e tema DEV/unpublished.

## Git
- Branch: `hermes/lkgoc-template-standard-20260609`
- Commit revertido: `c653339 Fix LKGOC standard template flow for Speedcat`
- Commit de rollback: `f45fc6f Revert "Fix LKGOC standard template flow for Speedcat"`
- Push para origin: realizado.

## Shopify DEV
Tema DEV restaurado a partir do branch revertido:
- Theme ID: `155065450718`
- Name: `lk-new-theme/dev`
- Role: `unpublished`

Assets restaurados:
- `templates/collection.lkgoc.json`
- `sections/lk-collection.liquid`
- `snippets/lk-goc-collection.liquid`

## Readback pós-rollback
URL: `https://lksneakers.com.br/collections/puma-speedcat?preview_theme_id=155065450718&view=lkgoc`

Checks:
- status: 200
- role unpublished: 1
- Liquid error: 0
- componente Speedcat errado: 0

## Guardrail
Production/main não foi alterada.
Collection object/template_suffix não foi alterado.

## Próxima decisão
Não tentar novo patch até reler/identificar exatamente o template Shopify cadastrado/aprovado e o mecanismo esperado de aplicação da coleção otimizada.
