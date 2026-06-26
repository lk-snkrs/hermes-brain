# Receipt — Curadoria LK PDP — DEV Dunk Low regular

Data: 2026-06-06
Executor: Hermes lk-shopify
Status: DEV aplicado e verificado; Production intacto

## Aprovação

Lucas aprovou via Telegram:

`Aprovo`

Contexto imediato: approval packet do item 1, `Dunk Low regular`, aguardando aprovação explícita de upload DEV.

## Escopo

Tema DEV: `155065450718` (`unpublished`)
Tema Production: `155065417950` (`main`)
Asset: `snippets/lk-variante-top30-visited-v2.liquid`

Upload somente no DEV.

## Grupo adicionado no DEV

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

SB/collabs ficaram fora desta rodada.

## Artifacts

Approval packet:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/approval-packets/curadoria-lk-pdp-dunk-low-regular-dev-20260606.md`

Apply:

- Script: `/opt/data/tmp/lk_apply_curadoria_dunk_low_regular_dev_20260606.py`
- Apply JSON: `/opt/data/tmp/lk_curadoria_dunk_low_regular_apply_20260606T180840Z.json`
- Backup DEV antes do write: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/dev-before-dunk-low-regular-20260606T180840Z.liquid`
- Target: `/opt/data/tmp/lk_curadoria_dunk_low_regular_target_20260606T180840Z.liquid`
- Readback: `/opt/data/tmp/lk_curadoria_dunk_low_regular_readback_20260606T180840Z.liquid`

QA:

- Script: `/opt/data/tmp/lk_qa_curadoria_dunk_low_regular_dev_20260606.py`
- QA JSON: `/opt/data/tmp/lk_curadoria_dunk_low_regular_qa_20260606T180840Z.json`

## Readback

- DEV before SHA: `d0f835bc1fd639a98688d47f36f3d8532848adb8f4f0a1a1316e6dda5514ff27`
- DEV target/readback SHA: `3a8e1987300c5f5b1e067922d10c8d3bf7c92ce3501bae5b6c10551781b43f93`
- Readback match: `true`
- Production before/after SHA: `10f3456c5506da3a459715a2781f9a004dae9333ef8b9e76725088c007717738`
- Production unchanged: `true`

## QA estático

Passou:

- Marker count: `1`
- Arrays handles/labels/images/titles: `10/10/10/10`
- Expected render cards: `5`
- Missing handles: `[]`
- Imagens: `10/10` HTTP 200
- URL malformada: `false`
- Placeholder `TenisMoldeLK`: `false`

## Scan pós-DEV

Scanner padrão pós-apply:

- `product_count`: `2331`
- `covered_handles_dev`: `642`
- `covered_handles_prod`: `621`
- `groups_detected_dev`: `44`
- `groups_detected_prod`: `43`

## QA público DEV

Public preview foi inconclusivo:

- As URLs com `preview_theme_id` foram servidas como canonical/live, removendo o parâmetro.
- HTML retornou `200`, mas sem marker/hint DEV — esperado quando Shopify serve live em preview público não autenticado.
- Prova principal: Admin Asset API readback + QA estático + image preflight.

## Correção durante apply

O primeiro preflight bloqueou corretamente 9 imagens por URLs antigas/erradas no script gerado. As imagens foram recarregadas do scan read-only atual e o apply foi refeito com URLs válidas. Nenhum PUT ocorreu antes da correção; o write só aconteceu após `10/10` imagens validarem HTTP 200.

## Rollback

Rollback DEV restaurando:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/dev-before-dunk-low-regular-20260606T180840Z.liquid`

## Próxima decisão

Se Lucas aprovar, próximo passo é **merge para Production** desta rodada DEV.

Depois disso: preparar SB Dunk Low collabs/cápsulas em rodada separada.
