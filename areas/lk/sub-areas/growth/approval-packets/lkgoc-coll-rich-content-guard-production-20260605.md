# Approval packet — LKGOC remover `coll-rich-content` legado em Production

Data: 2026-06-05T17:50:28

## Objetivo
Corrigir o tema Production para que coleções otimizadas com LKGOC não renderizem o bloco legado `.coll-rich-content` / "Perguntas frequentes" antigo.

## Escopo
Arquivo:
- `sections/lk-collection.liquid`

Tema Production:
- `155065417950` — `lk-new-theme/production` — role `live/main`

Tema DEV já aplicado e verificado:
- `155065450718` — `lk-new-theme/dev` — role `unpublished`

## Mudança técnica
Alterar a condição que renderiza o bloco legado de descrição/FAQ:

- Antes: excluía apenas `new-balance-530` e `onitsuka-tiger-mexico-66`.
- Depois: exclui qualquer coleção com `custom.lkgoc_status = optimized` e também handles LKGOC conhecidos:
  - `new-balance-204l`
  - `new-balance-9060`
  - `new-balance-530`
  - `onitsuka-tiger-mexico-66`

## Evidência DEV
QA HTML preview DEV `155065450718`:
- `new-balance-9060`: `legacy_div_count = 0`
- `new-balance-530`: `legacy_div_count = 0`
- `new-balance-204l`: `legacy_div_count = 0`
- `onitsuka-tiger-mexico-66`: `legacy_div_count = 0`

Arquivo QA:
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/lkgoc-coll-rich-content-guard-20260605/qa-preview-html-div-no-coll-rich-results.json`

## Risco
Baixo.
- Afeta apenas a renderização do bloco legado de FAQ/descrição para coleções LKGOC.
- Não altera produtos, preço, estoque, checkout, campanhas ou dados.

## Rollback
Restaurar backup de Production:
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/lkgoc-coll-rich-content-guard-20260605/before__sections__lk-collection__production-155065417950__20260605T175028.liquid`

## Approval necessário
Lucas aprovar merge do arquivo candidato para Production:
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/lkgoc-coll-rich-content-guard-20260605/prod-current/sections/lk-collection.liquid`
