# Receipt — Rollback segunda tentativa Puma Speedcat

Data: 2026-06-09

## Trigger
Lucas informou: "continua errado" após tentativa de usar o mesmo template_suffix da 204L.

## Ação imediata
Rollback completo da última intervenção.

## Shopify collection object
Puma Speedcat restaurada para o estado anterior:
- Antes do rollback: `template_suffix = ""`
- Depois do rollback: `template_suffix = "puma-speedcat"`

## Git
- Branch: `hermes/lkgoc-template-standard-20260609`
- Commit revertido: `632255d Add Speedcat to default collection template like 204L`
- Commit rollback: `e0f7295 Revert "Add Speedcat to default collection template like 204L"`
- Push realizado.

## Shopify DEV theme
Tema DEV restaurado a partir do branch revertido:
- theme: `lk-new-theme/dev`
- theme_id: `155065450718`
- role: `unpublished`

Assets restaurados:
- `templates/collection.lkgoc.json`
- `sections/lk-collection.liquid`
- `snippets/lk-goc-collection.liquid`

## Readback pós-rollback
- `/collections/puma-speedcat?preview_theme_id=155065450718`: Liquid error 0; `lk-guia-puma-speedcat` 0; `Contexto editorial Puma Speedcat` 0.
- `/collections/puma-speedcat?preview_theme_id=155065450718&view=lkgoc`: Liquid error 0; `lk-guia-puma-speedcat` 0; `Contexto editorial Puma Speedcat` 0.

## Guardrail
Não tentar nova implementação sem inspeção visual/histórica do template realmente aprovado na Shopify e do cadastro exato usado na 204L.
