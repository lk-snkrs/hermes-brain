# Receipt — Curadoria LK PDP — Production merge Dunk Low regular

Data: 2026-06-06
Executor: Hermes lk-shopify
Status: Production source aplicado e verificado; public HTML sem prova de render no momento

## Aprovação

Lucas aprovou explicitamente via Telegram:

`Aprovo merge`

Contexto imediato: DEV Dunk Low regular já aplicado/readback/QA e aguardava merge para Production.

## Escopo

Tema DEV: `155065450718` (`unpublished`)
Tema Production: `155065417950` (`main`)
Asset: `snippets/lk-variante-top30-visited-v2.liquid`

Merge scoped: extrair do DEV somente o bloco aprovado `top30-nike-dunk-low-regular-breadth` e inserir no Production atual, preservando grupos existentes.

## Grupo publicado no source Production

Marker:

`top30-nike-dunk-low-regular-breadth`

Produtos:

- `nike-dunk-low-ucla` — `UCLA`
- `dunk-low-light-ocean-bliss` — `Ocean Bliss`
- `dunk-low-next-nature-pink-pale-coral` — `Pink Coral`
- `nba-x-nike-dunk-low-chicago` — `NBA Chicago`
- `tenis-nike-dunk-low-halloween-2021-laranja` — `Halloween`
- `tenis-nike-dunk-low-miami-dolphins-azul` — `Miami Dolphins`
- `tenis-nike-dunk-low-university-blue-azul` — `University Blue`
- `tenis-nike-dunk-low-bicoastal-verde` — `Bicoastal`
- `nike-dunk-low-black-paisley` — `Black Paisley`
- `nike-dunk-low-black-panda` — `Black Panda`

## Artifacts

Merge script:

- `/opt/data/tmp/lk_merge_dunk_low_regular_to_production_20260606.py`

Merge JSON:

- `/opt/data/tmp/lk_curadoria_dunk_low_regular_prod_merge_20260606T182819Z.json`

Backup Production antes do merge:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/prod-before-dunk-low-regular-20260606T182819Z.liquid`

Target/readback:

- Target: `/opt/data/tmp/lk_curadoria_dunk_low_regular_prod_target_20260606T182819Z.liquid`
- Readback: `/opt/data/tmp/lk_curadoria_dunk_low_regular_prod_readback_20260606T182819Z.liquid`

QA:

- Script: `/opt/data/tmp/lk_qa_dunk_low_regular_production_20260606.py`
- JSON: `/opt/data/tmp/lk_curadoria_dunk_low_regular_prod_qa_20260606T182819Z.json`

## Readback / SHA

- DEV SHA before/after: `3a8e1987300c5f5b1e067922d10c8d3bf7c92ce3501bae5b6c10551781b43f93`
- DEV unchanged: `true`
- Production before SHA: `10f3456c5506da3a459715a2781f9a004dae9333ef8b9e76725088c007717738`
- Production target/readback SHA: `3289f066f3d4202e21148bd2fbaa4f862c85a7fcad4e67ca3749e002af289b60`
- Readback match: `true`

## Preserve checks

Markers preservados no readback Production:

- `top30-new-balance-9060-adult-breadth`: `1`
- `top30-nike-air-max-1-regular-collabs`: `1`
- `top30-on-running-cloudtilt-regular-loewe`: `1`
- novo `top30-nike-dunk-low-regular-breadth`: `1`

## QA estático

Passou:

- Marker count: `1`
- Arrays handles/labels/images/titles: `10/10/10/10`
- Expected render cards: `5`
- Missing handles: `[]`
- Duplicates: `false`
- Imagens: `10/10` HTTP 200
- URL malformada: `false`
- Placeholder `TenisMoldeLK`: `false`

## Scanner pós-Production

- `product_count`: `2331`
- `covered_handles_dev`: `642`
- `covered_handles_prod`: `638`
- `groups_detected_dev`: `44`
- `groups_detected_prod`: `44`

## QA público

Public HTML no momento não provou render do bloco:

- 10/10 amostras Dunk responderam HTTP `200`, mas sem `lk-variante`, `Outras variações` ou marker novo.
- Controles públicos também vieram sem Curadoria no HTML capturado (`NB 9060`, `Air Max 1`, `NB 550`), apesar de o source Production/readback estar atualizado.

Interpretação: source Production está correto; render público da superfície Curadoria não foi comprovado nesta bateria. Não é motivo automático para rollback porque o Admin Asset API/readback/static QA passaram e o comportamento também afetou controles já publicados.

## Rollback

Restaurar o backup Production:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/prod-before-dunk-low-regular-20260606T182819Z.liquid`

## Próxima decisão

- Monitorar/retestar público mais tarde; ou
- preparar próxima rodada SB Dunk Low collabs/cápsulas em DEV.
