# Batch 18 Production Merge — NB 9060 + Adidas Samba OG

- timestamp UTC: `2026-06-03T16:27:52.607714+00:00`
- live theme: `155065450718` / `lk-new-theme/dev` / role `main`
- preview theme: `156623372510` / `LK Curadoria Force Fix Preview 2026-06-03` / role `unpublished`
- live before SHA: `ce223a18b60b`
- target/readback SHA: `6d127babb763` / `6d127babb763`
- readback matches: `True`

## Changes
- `top30-nb-9060` / New Balance 9060 mode `expand_existing_group` before `18` after `26` added `8`
- `top30-samba-og` / Samba OG mode `expand_existing_group` before `10` after `18` added `8`

## QA estático
- arrays equal: `True`
- array lengths: `{'lk_top30_markers': 22, 'lk_top30_names': 22, 'lk_top30_handles_groups': 22, 'lk_top30_labels_groups': 22, 'lk_top30_images_groups': 22}`
- bad URL occurrences: `{'https:https://': 0, 'https://https://': 0, 'TenisMoldeLK': 0}`
- `top30-nb-9060`: handles `26`, labels `26`, images `26`, malformed `0`
- `top30-samba-og`: handles `18`, labels `18`, images `18`, malformed `0`

## QA live multi-round
- all_sampled_ok: `True`
- seen_ok_all_handles: `True`
- total_bad: `0`
- round 1: `18/18` OK; bad `[]`
- round 2: `18/18` OK; bad `[]`

## Rollback
- restore asset from `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/lk-variante/batch18-production-merge-nb9060-sambaog-20260603T1550Z/live-before.liquid`