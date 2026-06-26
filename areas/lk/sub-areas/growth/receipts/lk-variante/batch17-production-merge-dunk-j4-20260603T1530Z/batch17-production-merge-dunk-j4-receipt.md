# Batch 17 Production Merge — Nike Dunk Low + Air Jordan 4

- timestamp UTC: `2026-06-03T15:14:00.422678+00:00`
- live theme: `155065450718` / `lk-new-theme/dev` / role `main`
- preview theme: `156623372510` / `LK Curadoria Force Fix Preview 2026-06-03` / role `unpublished`
- live before SHA: `3918da96d152`
- target/readback SHA: `ce223a18b60b` / `ce223a18b60b`
- readback matches: `True`

## Changes
- `top30-nike-dunk-low-regular` mode `append_new_group` before `0` after `10` added `10`
- `top30-air-jordan-4-regular` mode `expand_existing_group` before `8` after `16` added `8`

## QA estático
- arrays equal: `True`
- array lengths: `{'lk_top30_markers': 22, 'lk_top30_names': 22, 'lk_top30_handles_groups': 22, 'lk_top30_labels_groups': 22, 'lk_top30_images_groups': 22}`
- bad URL occurrences: `{'https:https://': 0, 'https://https://': 0, 'TenisMoldeLK': 0}`
- `top30-nike-dunk-low-regular`: handles `10`, labels `10`, images `10`, malformed `0`
- `top30-air-jordan-4-regular`: handles `16`, labels `16`, images `16`, malformed `0`

## QA live multi-round
- all_sampled_ok: `False`
- total_bad: `10`
- round 1: `16/20` OK; bad `['tenis-nike-dunk-low-denim-turquoise-azul', 'tenis-nike-dunk-low-medium-olive-hemp-verde', 'tenis-air-jordan-4-retro-white-thunder-preto', 'tenis-air-jordan-4-retro-oxidized-branco']`
- round 2: `14/20` OK; bad `['tenis-nike-dunk-low-viotech-rosa', 'tenis-nike-dunk-low-suede-panda-preto', 'tenis-nike-dunk-low-safari-oil-green-verde', 'tenis-nike-dunk-low-safari-phantom-bege', 'tenis-air-jordan-4-retro-seafoam-verde', 'tenis-air-jordan-4-retro-oxidized-branco']`

## Rollback
- restore asset from `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/lk-variante/batch17-production-merge-dunk-j4-20260603T1530Z/live-before.liquid`