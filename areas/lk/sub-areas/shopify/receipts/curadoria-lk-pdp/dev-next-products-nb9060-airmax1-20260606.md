# Receipt — Curadoria LK PDP — DEV próximos produtos NB 9060 adultos + Air Max 1

Data: 2026-06-06
Executor: Hermes lk-shopify
Status: DEV aplicado e verificado; Production intacto

## Aprovação

Lucas aprovou via Telegram/clarify:

`Aprovo DEV próximos produtos: NB 9060 adultos + Air Max 1`

## Escopo

Tema DEV: `155065450718` (`unpublished`)
Tema Production: `155065417950` (`main`)
Asset: `snippets/lk-variante-top30-visited-v2.liquid`

Upload somente no DEV.

## Grupos adicionados no DEV

### `top30-new-balance-9060-adult-breadth`

Handles:

- `new-balance-9060-black-cement-black-cat-preto` — `Black Cat`
- `tenis-new-balance-9060-black-castlerock-grey-preto` — `Castlerock`
- `tenis-new-balance-9060-black-magnet-preto` — `Black Magnet`
- `tenis-new-balance-9060-chrome-blue-azul` — `Chrome Blue`
- `tenis-new-balance-9060-eclipse-azul-marinho` — `Eclipse`
- `tenis-new-balance-9060-great-plains-marrom` — `Great Plains`
- `tenis-new-balance-9060-incense-raincloud-arid-stone-marrom` — `Incense`

Observação: `kids`, `TD` e o handle com imagem `TenisMoldeLK` foram excluídos desta rodada.

### `top30-nike-air-max-1-regular-collabs`

Handles:

- `kasina-x-nike-air-max-1-won-ang-grey` — `Kasina Grey`
- `concepts-x-air-max-1-sp-mellow` — `Concepts Mellow`
- `tenis-nike-air-max-1-87-stranger-things-steve-harrington-branco` — `Stranger Things`
- `tenis-nike-air-max-1-x-patta-hyper-crimson-branco` — `Patta Crimson`
- `tenis-nike-air-max-1-x-patta-monarch-laranja` — `Patta Monarch`
- `tenis-nike-air-max-1-x-patta-noise-aqua-azul` — `Patta Aqua`
- `travis-scott-x-nike-air-max-1-cactus-brown` — `Cactus Brown`
- `travis-scott-x-nike-air-max-1-cactus-gold` — `Cactus Gold`

## Artifacts

Approval packet:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/approval-packets/curadoria-lk-pdp-next-products-after-prod-merge-20260606.md`

Apply:

- Script: `/opt/data/tmp/lk_apply_curadoria_next_products_nb9060_airmax1_dev_20260606.py`
- Apply JSON: `/opt/data/tmp/lk_curadoria_next_products_nb9060_airmax1_apply_20260606T172745Z.json`
- Backup DEV antes do write: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/dev-before-next-products-nb9060-airmax1-20260606T172745Z.liquid`
- Target: `/opt/data/tmp/lk_curadoria_next_products_nb9060_airmax1_target_20260606T172745Z.liquid`
- Readback: `/opt/data/tmp/lk_curadoria_next_products_nb9060_airmax1_readback_20260606T172745Z.liquid`

QA:

- Script: `/opt/data/tmp/lk_qa_curadoria_next_products_nb9060_airmax1_dev_20260606.py`
- QA JSON: `/opt/data/tmp/lk_curadoria_next_products_nb9060_airmax1_qa_20260606T172745Z.json`

## Readback

- DEV before SHA: `11e1939aad3adfccc3fb6ea33cf0eb9c7f5050de72803ec45a6d6af2393b773d`
- DEV target/readback SHA: `d0f835bc1fd639a98688d47f36f3d8532848adb8f4f0a1a1316e6dda5514ff27`
- Readback match: `true`
- Production before/after SHA: `571fb07f73aa1cce794ac8481a645bbbaf46eb98cc52f4092f07d607db3d3acb`
- Production unchanged: `true`

## QA estático

Passou:

- `top30-new-balance-9060-adult-breadth`
  - marker count: `1`
  - handles/labels/images/titles: `7/7/7/7`
  - render esperado por PDP: `5` cards
  - missing handles: `[]`
- `top30-nike-air-max-1-regular-collabs`
  - marker count: `1`
  - handles/labels/images/titles: `8/8/8/8`
  - render esperado por PDP: `5` cards
  - missing handles: `[]`
- Image checks: `15/15` HTTP 200
- URL malformada: `false`
- Placeholder `TenisMoldeLK`: `false`

## Scan pós-DEV

Scanner padrão pós-apply:

- `product_count`: `2331`
- `covered_handles_dev`: `625`
- `covered_handles_prod`: `603`
- `groups_detected_dev`: `43`
- `groups_detected_prod`: `41`

Warning não bloqueante conhecido:

- `FutureWarning: Possible set symmetric difference at position 2` no regex do scanner.

## QA público DEV

Caveat esperado:

- Public preview removeu `preview_theme_id` em algumas URLs e/ou retornou `503` em uma amostra.
- Amostras 200 não mostraram hint DEV, porque o Shopify serviu live/canonical sem preservar preview.
- Portanto, prova principal do DEV é Admin Asset API readback + QA estático + image preflight.

## Rollback

Rollback DEV restaurando:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/dev-before-next-products-nb9060-airmax1-20260606T172745Z.liquid`

## Próxima decisão

Se Lucas aprovar, próximo passo é preparar packet de merge para Production desta rodada DEV.

Depois disso, preparar split específico de:

- Nike Dunk Low regular
- Nike SB Dunk Low collabs
