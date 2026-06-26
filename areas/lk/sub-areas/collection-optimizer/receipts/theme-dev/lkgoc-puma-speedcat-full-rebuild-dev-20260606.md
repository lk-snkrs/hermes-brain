# Receipt — LKGOC Puma Speedcat Full Rebuild DEV

Data: 2026-06-06T15:38:48.259089+00:00

## Pedido
Lucas: "seguir" após decisão de começar do zero.

## Gold source registrado
- Collection gold source: New Balance 204L (`/collections/new-balance-204l`).
- Código copiado/adaptado: bloco `collection.handle == 'new-balance-204l'` em `sections/lk-collection.liquid`.
- Guide gold source: `snippets/lk-goc-new-balance-204l-guide-panel.liquid`.

## Workers/guardrails
Ledger: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/puma-speedcat-full-rebuild-20260606/WORKERS.md`

## Tema alvo
- Theme: `lk-new-theme/dev`
- ID: `155065450718`
- Role: `unpublished`

## Assets DEV escritos
- `snippets/lk-goc-puma-speedcat-hero.liquid`
- `snippets/lk-goc-puma-speedcat-guide-panel.liquid`
- `sections/lk-collection.liquid`

## Readback Admin API
- Hero equal: `True`
- Guide equal: `True`
- Section hero render: `True`
- Section guide render: `True`
- Old bad marker present: `False`
- Production has new Puma render: `False`

## DOM/preview checks
- Puma hero present: `True`
- Puma guide present: `True`
- Gold source classes present: `True`
- Liquid error: `False`
- FAQ schema count: `1`
- Order banner → hero → grid → guide: `True`

## QA visual
Screenshots:
- Puma mobile: `work/puma-speedcat-full-rebuild-20260606/qa/puma-speedcat-rebuild-mobile.png`
- Puma desktop: `work/puma-speedcat-full-rebuild-20260606/qa/puma-speedcat-rebuild-desktop.png`
- Gold 204L mobile: `work/puma-speedcat-full-rebuild-20260606/qa/gold-new-balance-204l-mobile.png`
- Gold 204L desktop: `work/puma-speedcat-full-rebuild-20260606/qa/gold-new-balance-204l-desktop.png`

## Bloqueio antes de produção
Hero usa referência editorial/lifestyle externa para DEV. Antes de produção, trocar por asset aprovado/licenciado LK.

## Rollback DEV
Restaurar arquivos `.before` neste diretório:
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/puma-speedcat-full-rebuild-20260606/sections__lk-collection.liquid.before`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/puma-speedcat-full-rebuild-20260606/snippets__lk-goc-puma-speedcat-hero.liquid.before`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/puma-speedcat-full-rebuild-20260606/snippets__lk-goc-puma-speedcat-guide-panel.liquid.before`

Production não foi alterada.
