# Batch 16 Production Merge — Shox TL + Samba Jane

- timestamp UTC: `2026-06-03T14:45:15.693323+00:00`
- live theme: `155065450718` / `lk-new-theme/dev` / role `main`
- preview theme: `156623372510` / `LK Curadoria Force Fix Preview 2026-06-03` / role `unpublished`
- live before SHA: `cb3209f6ea06`
- target/readback SHA: `3918da96d152` / `3918da96d152`
- readback matches: `True`

## QA estático
- arrays equal: `True`
- top30-nike-shox-tl: handles `7`, labels `7`, images `7`, malformed `0`
- top30-adidas-samba-jane: handles `7`, labels `7`, images `7`, malformed `0`

## QA live multi-round
- all_sampled_ok: `True`
- total_bad: `0`
- round 1: `16/16` OK; bad `[]`
- round 2: `16/16` OK; bad `[]`

## Rollback
- restore asset from `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/lk-variante/batch16-production-merge-shox-samba-jane-20260603T1506Z/live-before.liquid`