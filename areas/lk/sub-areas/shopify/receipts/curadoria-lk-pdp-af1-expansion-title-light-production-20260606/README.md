# Curadoria LK PDP — AF1 Expansion + título light — Production — 2026-06-06

## Status

Concluído: merge para Production executado via GitHub PR e validado por Shopify readback + QA visual público.

## Aprovação

Lucas autorizou o escopo: “Os dois: correção do título + expansão AF1 Special”.

## Escopo

- Theme Production: `155065417950`
- Repo: `lk-snkrs/lk-new-theme`
- Branch base: `production`
- PR: `#28` — https://github.com/lk-snkrs/lk-new-theme/pull/28
- Merge commit: `82f1737f10826fb10015650bfd9b6c5a1c89c49b`
- Arquivos alterados:
  - `snippets/lk-variante-top30-visited-v2.liquid`
  - `assets/lk-variante.css`

## Mudanças

1. Expansão do grupo `top30-nike-air-force-1-low-special`:
   - antes: 7 itens
   - depois: 18 itens
   - novos 11 handles presentes
   - arrays Curadoria: 29 grupos alinhados
   - marker count: 1

2. Correção visual do título do bloco:
   - `.lk-variante__title`
   - `font-weight: 500 → 300`
   - texto afetado: `Outras variações`

## Verificação local antes do merge

- `git diff --check`: passou
- Diff limitado a 2 assets
- Diff stat:
  - `assets/lk-variante.css`: 2 linhas alteradas
  - `snippets/lk-variante-top30-visited-v2.liquid`: 6 linhas alteradas
- Snippet local pós-candidato:
  - SHA: `83d10c80e6fe674e01ed924cb136e6aaa742e0b59b2c7eafb3c396ca87e59a3f`
  - AF1 count: 18
  - errors: `[]`
- CSS local pós-candidato:
  - SHA: `b4673719c878d3314c243580db9404e31e2156dda677edd8587197fcfd5947cd`
  - title old count: 0
  - title new count: 1

## Shopify Production readback

Polling pós-merge:

- Tentativa 1:
  - snippet SHA: `dc30f0059f131a3b326698edc3094eb02db4a949bbac91a5b3b900571353b2a8`
  - AF1 count: 7
  - CSS title light: false
- Tentativa 2:
  - snippet SHA: `83d10c80e6fe674e01ed924cb136e6aaa742e0b59b2c7eafb3c396ca87e59a3f`
  - AF1 count: 18
  - all new handles: true
  - snippet errors: `[]`
  - CSS SHA: `b4673719c878d3314c243580db9404e31e2156dda677edd8587197fcfd5947cd`
  - CSS title light: true
  - CSS old count: 0
  - CSS new count: 1

## QA visual live público

PDPs testadas:

1. `tenis-a-ma-maniere-x-air-force-1-low-triple-white-branco`
2. `tenis-nike-air-force-1-low-protro-kobe-bryant-mamba-mentality-amarelo`
3. `tenis-nike-air-force-1-low-x-supreme-wheat-marrom`

Resultado final:

- Bloco renderizou: true
- Marker: `top30-nike-air-force-1-low-special`
- Layout rail: `grid`
- Card count: 5
- Labels dos produtos: `fontWeight 300`
- `::after` das labels: `fontWeight 300`, `content none`
- Título “Outras variações”: `fontWeight 300`

Observação: a primeira leitura pública do A Ma Maniére retornou sem bloco, mas 5 retries focados em seguida renderizaram corretamente com título `300`. Tratado como propagação/cache de edge após merge.

## Backups de rollback

- Snippet antes do merge:
  - `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-af1-expansion-title-light-production-20260606/20260606T142851Z-production-theme-155065417950-snippets__lk-variante-top30-visited-v2.before.liquid`
- CSS antes do merge:
  - `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-af1-expansion-title-light-production-20260606/20260606T142851Z-production-theme-155065417950-assets__lk-variante.before.css`

Rollback: reverter PR/commit `82f1737f10826fb10015650bfd9b6c5a1c89c49b` ou restaurar os backups via Shopify asset write aprovado.

## Artefatos

- Script de merge/readback: `/opt/data/tmp/lk_prod_merge_af1_expansion_title_light.py`
- Output do merge/readback: `/opt/data/tmp/lk_prod_merge_af1_expansion_title_light.stdout`
- Receipt JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-af1-expansion-title-light-production-20260606/20260606T142851Z-github-merge-readback-receipt.json`
- QA visual live:
  - `/opt/data/tmp/lk_prod_af1_full_qa_tenis-a-ma-maniere-x-air-force-1-low-triple-white-branco.json`
  - `/opt/data/tmp/lk_prod_af1_full_qa_tenis-nike-air-force-1-low-protro-kobe-bryant-mamba-mentality-amarelo.json`
  - `/opt/data/tmp/lk_prod_af1_full_qa_tenis-nike-air-force-1-low-x-supreme-wheat-marrom.json`
