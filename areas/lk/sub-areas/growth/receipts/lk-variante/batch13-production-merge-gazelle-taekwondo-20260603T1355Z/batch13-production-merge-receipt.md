# Batch 13 Production Merge — Gazelle + Taekwondo Mei

- timestamp UTC: `2026-06-03T13:47:02.326163+00:00`
- live theme: `155065450718` / `lk-new-theme/dev` / role `main`
- preview theme: `156623372510` / `LK Curadoria Force Fix Preview 2026-06-03` / role `unpublished`
- live before SHA: `ef0b8f1c2002`
- target/readback SHA: `db6aff95ac0c` / `db6aff95ac0c`
- readback matches: `True`

## QA estático
- arrays equal: `True`
- top30-adidas-gazelle: handles `11`, labels `11`, images `11`, malformed `0`
- top30-adidas-taekwondo-mei: handles `9`, labels `9`, images `9`, malformed `0`

## QA live multi-round
- all_sampled_ok: `True`
- total_bad: `0`
- round 1: `6/6` OK; bad `[]`
- round 2: `6/6` OK; bad `[]`
- round 3: `6/6` OK; bad `[]`

## Rollback
- restore asset from `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/lk-variante/batch13-production-merge-gazelle-taekwondo-20260603T1355Z/live-before.liquid`