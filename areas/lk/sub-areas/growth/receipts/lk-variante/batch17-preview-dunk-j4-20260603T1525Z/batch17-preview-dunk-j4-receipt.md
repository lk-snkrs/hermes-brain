# Batch 17 Preview — Nike Dunk Low + Air Jordan 4

- timestamp UTC: `2026-06-03T15:09:55.850442+00:00`
- approval: `Lucas approved via clarify: Aprovar preview Batch 17`
- preview: `156623372510` / `LK Curadoria Force Fix Preview 2026-06-03` / role `unpublished`
- live unchanged: `True`
- target/readback: `d847bda0a9c2` / `d847bda0a9c2`
- readback matches: `True`

## Changes
- `top30-nike-dunk-low-regular` mode `append_new_group` final count `10`; added `10`
  - `tenis-nike-dunk-low-baroque-brown-marrom` → Baroque Brown
  - `tenis-nike-dunk-low-denim-turquoise-azul` → Denim Turquoise
  - `tenis-nike-dunk-low-viotech-rosa` → Viotech
  - `tenis-nike-dunk-low-next-nature-aster-pink-rosa` → Next Nature Aster Pink
  - `tenis-nike-dunk-flax-suede-marrom` → Flax Suede
  - `tenis-nike-dunk-low-suede-panda-preto` → Suede Panda
  - `tenis-nike-dunk-low-safari-oil-green-verde` → Safari Oil Green
  - `tenis-nike-dunk-low-safari-phantom-bege` → Safari Phantom
  - `tenis-nike-dunk-low-medium-olive-hemp-verde` → Medium Olive Hemp
  - `tenis-nike-dunk-low-twist-university-blue-azul` → Twist University Blue
- `top30-air-jordan-4-regular` mode `expand_existing_group` final count `16`; added `8`
  - `tenis-nike-air-jordan-4-cave-stone-and-black-marrom` → Cave Stone and Black
  - `tenis-air-jordan-4-retro-military-blue-branco-copia` → Oxidized Green
  - `tenis-air-jordan-4-retro-forget-me-not-azul` → Forget Me Not
  - `tenis-air-jordan-4-retro-seafoam-verde` → Seafoam
  - `tenis-air-jordan-4-retro-orchid-rosa` → Orchid
  - `tenis-air-jordan-4-retro-white-thunder-preto` → White Thunder
  - `tenis-air-jordan-4-retro-shimmer-rosa` → Shimmer
  - `tenis-air-jordan-4-retro-oxidized-branco` → Oxidized

## QA estático
- arrays equal: `True`
- array lengths: `{'lk_top30_markers': 22, 'lk_top30_names': 22, 'lk_top30_handles_groups': 22, 'lk_top30_labels_groups': 22, 'lk_top30_images_groups': 22}`
- bad URL occurrences: `{'https:https://': 0, 'https://https://': 0, 'TenisMoldeLK': 0}`
- `top30-nike-dunk-low-regular`: handles `10`, labels `10`, images `10`, malformed `0`
- `top30-air-jordan-4-regular`: handles `16`, labels `16`, images `16`, malformed `0`

## Rollback
- restore preview from `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/lk-variante/batch17-preview-dunk-j4-20260603T1525Z/preview-before.liquid`

## Non-actions
- No live/main write
- No production merge
- No product/price/stock/app/GMC/Tiny/Klaviyo/Meta/checkout write