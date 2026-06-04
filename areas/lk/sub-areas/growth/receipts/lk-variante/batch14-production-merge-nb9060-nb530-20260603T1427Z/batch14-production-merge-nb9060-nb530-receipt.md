# Batch 14 Production Merge — NB 9060 + NB 530

- timestamp UTC: `2026-06-03T14:08:28.584803+00:00`
- live theme: `155065450718` / `lk-new-theme/dev` / role `main`
- preview theme: `156623372510` / `LK Curadoria Force Fix Preview 2026-06-03` / role `unpublished`
- live before SHA: `db6aff95ac0c`
- target/readback SHA: `634762593b93` / `634762593b93`
- readback matches: `True`

## QA estático
- arrays equal: `True`
- top30-nb-9060: handles `18`, labels `18`, images `18`, malformed `0`
- top30-nb-530: handles `16`, labels `16`, images `16`, malformed `0`

## QA live multi-round
- all_sampled_ok: `False`
- total_bad: `8`
- round 1: `12/15` OK; bad `['tenis-new-balance-9060-black-castlerock-preto', 'tenis-new-balance-530-grey-matter-silver-metallic-cinza', 'new-balance-530-white-natural-indigo-1']`
- round 2: `12/15` OK; bad `['tenis-new-balance-9060-earth-shadow-flat-taupe-marrom', 'tenis-new-balance-530-silver-black-cinza', 'air-jordan-1-low-og-black-toe-2023']`
- round 3: `13/15` OK; bad `['tenis-new-balance-9060-bisque-frosted-glass-bege', 'tenis-new-balance-530-brown-tan-marrom']`

## QA live supplemental
- initial multi-round had intermittent storefront `503` responses, not source/readback mismatch
- focused retry on representative bad handles: HTML `200` + Curadoria hint on first retry for all rechecked
- product `.js`: `200` for all rechecked
- supplemental artifact: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/lk-variante/batch14-production-merge-nb9060-nb530-20260603T1427Z/batch14-production-supplemental-live-qa.json`

## Rollback
- restore asset from `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/lk-variante/batch14-production-merge-nb9060-nb530-20260603T1427Z/live-before.liquid`