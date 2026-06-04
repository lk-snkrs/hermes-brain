# Batch 12 Curadoria LK — AJ1 Low OG merge produção

Timestamp UTC: `2026-06-03T13:27:52+00:00`

Live theme: `155065450718` — lk-new-theme/dev / role `main`

## Handles
- `tenis-air-jordan-1-low-og-obsidian-unc-azul` → Obsidian UNC
- `tenis-nike-air-jordan-1-low-og-olive-verde` → Olive
- `tenis-air-jordan-1-low-og-rookie-of-year-marrom` → Rookie Year
- `air-jordan-1-low-og-black-toe-2023` → Black Toe
- `air-jordan-1-low-og-bleached-coral` → Bleached Coral
- `tenis-air-jordan-1-low-og-oxidized-white-green-branco` → Oxidized Green
- `air-jordan-1-low-og-unc` → UNC
- `air-jordan-1-low-og-ex-black-and-smoke-grey` → Black Smoke

## Readback
- before: `13133993edf5`
- target: `ef0b8f1c2002`
- readback: `ef0b8f1c2002`
- matches: `True`

## QA live
- round 1: ok `6`, bad `0`
- round 2: ok `5`, bad `1`
- round 3: ok `6`, bad `0`
- round 4: ok `6`, bad `0`

## Rollback
- Restore: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/lk-variante/batch12-aj1lowog-production-merge-20260603T1325Z/live-before.liquid`


## QA live complementar
- Final QA 3 rounds × 8 handles: total bad `5` — mistura de cache público/404 transitório; `/products/*.js` confirmou produtos públicos e disponíveis nos handles problemáticos.
- Late QA 2 rounds × 8 handles: round 1 `8/8` OK; round 2 `7/8` OK, com `Olive` servindo HTML sem bloco em uma amostra.
- Veredito: merge/readback correto; live ainda apresenta intermitência de cache público em amostragem, semelhante ao incidente anterior.
