# Batch 19 Production Merge — SB Dunk Low + Mexico 66 SD + NB 530

- timestamp UTC: `2026-06-03T16:37:07.020338+00:00`
- live theme: `155065450718` / `lk-new-theme/dev` / role `main`
- preview theme: `156623372510` / `LK Curadoria Force Fix Preview 2026-06-03` / role `unpublished`
- live before SHA: `6d127babb763`
- target/readback SHA: `e84a5562d59e` / `e84a5562d59e`
- readback matches: `True`

## Changes
- `top30-nike-sb-dunk-low` / Nike SB Dunk Low mode `append_new_group` before `0` after `8` added `8`
- `top30-mexico66-sd` / Onitsuka Mexico 66 SD mode `expand_existing_group` before `12` after `20` added `8`
- `top30-nb-530` / New Balance 530 mode `expand_existing_group` before `16` after `21` added `5`

## QA estático
- arrays equal: `True`
- array lengths: `{'lk_top30_markers': 23, 'lk_top30_names': 23, 'lk_top30_handles_groups': 23, 'lk_top30_labels_groups': 23, 'lk_top30_images_groups': 23}`
- bad URL occurrences: `{'https:https://': 0, 'https://https://': 0, 'TenisMoldeLK': 0}`
- `top30-nike-sb-dunk-low`: handles `8`, labels `8`, images `8`, malformed `0`
- `top30-mexico66-sd`: handles `20`, labels `20`, images `20`, malformed `0`
- `top30-nb-530`: handles `21`, labels `21`, images `21`, malformed `0`

## QA live multi-round
- all_sampled_ok: `False`
- seen_ok_all_handles: `False`
- total_bad: `16`
- round 1: `13/23` OK; bad `['tenis-nike-sb-dunk-low-trocadero-gardens-marrom', 'nike-sb-dunk-low-pro-classic-green', 'nike-sb-dunk-low-prm-phillies', 'nike-sb-dunk-low-club-58-gulf', 'tenis-onitsuka-tiger-mexico-66-sd-exposed-black-black-preto', 'tenis-onitsuka-tiger-mexico-66-sd-clay-canyon-marrom', 'tenis-onitsuka-tiger-mexico-66-sd-exposed-foam-jade-verde', 'tenis-onitsuka-tiger-mexico-66-sd-vin-mantle-green-ivory-verde', 'tenis-new-balance-530-white-green-matcha-verde', 'tenis-new-balance-530-sea-salt-white-marsh-green-branco']`
- round 2: `17/23` OK; bad `['tenis-nike-sb-dunk-low-trocadero-gardens-marrom', 'nike-sb-dunk-low-prm-phillies', 'nike-sb-dunk-low-club-58-gulf', 'tenis-onitsuka-tiger-mexico-66-sd-exposed-foam-jade-verde', 'onitsuka-tiger-mexico-66-sd-metallic-series-jade-cream-verde', 'tenis-new-balance-530-white-green-matcha-verde']`

## Rollback
- restore asset from `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/lk-variante/batch19-production-merge-sbdunk-mexico66sd-nb530-20260603T1638Z/live-before.liquid`