# Batch 15 Production Merge — Handball Spezial + SL 72

- timestamp UTC: `2026-06-03T14:25:58.666697+00:00`
- live theme: `155065450718` / `lk-new-theme/dev` / role `main`
- preview theme: `156623372510` / `LK Curadoria Force Fix Preview 2026-06-03` / role `unpublished`
- live before SHA: `634762593b93`
- target/readback SHA: `aa85a6617301` / `aa85a6617301`
- readback matches: `True`

## QA estático
- arrays equal: `True`
- top30-adidas-handball-spezial: handles `13`, labels `13`, images `13`, malformed `0`
- top30-sl72-og: handles `16`, labels `16`, images `16`, malformed `0`

## QA live multi-round
- all_sampled_ok: `False`
- total_bad: `3`
- round 1: `12/13` OK; bad `['tenis-adidas-handball-spezial-sand-strata-clear-sky-bege']`
- round 2: `12/13` OK; bad `['tenis-adidas-handball-spezial-sand-strata-clear-sky-bege']`
- round 3: `12/13` OK; bad `['tenis-adidas-handball-spezial-sand-strata-clear-sky-bege']`

## Repair pós-QA
- removido de live + preview: `tenis-adidas-handball-spezial-sand-strata-clear-sky-bege`
- motivo: PDP público 200 mas sem hint da Curadoria em 3/3 rounds; removido para manter só PDPs com render path verificado
- hash live após repair: `cb3209f6ea06`
- hash preview após repair: `96ae61c1fdb0`
- repair readback matches: `True`
- receipt repair: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/lk-variante/batch15-production-repair-remove-handball-sand-20260603T1453Z/batch15-production-repair-remove-handball-sand-receipt.md`

## QA live final após repair
- round 1: `12/12` OK
- round 2: `11/12` OK; 1 intermitência sem hint em SL 72 Aurora Ivy
- retry focado Aurora Ivy: `200` + Curadoria hint na primeira tentativa
- artifact: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/lk-variante/batch15-production-merge-handball-sl72-20260603T1448Z/batch15-final-live-qa-after-repair.json`

## Rollback
- restore original pre-Batch15 asset from `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/lk-variante/batch15-production-merge-handball-sl72-20260603T1448Z/live-before.liquid`
- restore pre-repair asset from `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/lk-variante/batch15-production-repair-remove-handball-sand-20260603T1453Z/live-before-repair.liquid`