# Curadoria LK PDP — Production Yeezy Slide apply

- timestamp UTC: `2026-06-05T18:51:47.395435+00:00`
- approval: `Lucas approved in Telegram: apply to Production/main scoped merge for Curadoria LK PDP Yeezy Slide in active asset snippets/lk-variante-top30-visited-v2.liquid, adding only marker top30-yeezy-slide-regular with 7 validated handles/labels/images, preserving 26 existing groups, backup before, readback after, cache-busted public QA.`
- write executed: `True`
- Production target: `155065417950` / `lk-new-theme/production` / role `main`
- asset: `snippets/lk-variante-top30-visited-v2.liquid`
- DEV source SHA12: `493429e95ac5`
- hashes before/proposed/readback: `01af5cea362d` / `493429e95ac5` / `493429e95ac5`

## Merge
- mode: `append-new-marker`
- marker count before/after: `26` / `27`
- existing Production markers preserved/order: `True`
- new marker added: `True`

## Static QA readback
- arrays equal: `True`
- marker count: `1`
- group index: `26`
- handles/labels/images: `7` / `7` / `7`
- handles match: `True`
- labels match: `True`
- images match: `True`
- images valid: `True`
- bad URL occurrences: `{'https:https://': 0, 'https://https://': 0, 'TenisMoldeLK': 0}`

## Public QA cache-busted
- rounds: `4`
- all ok every round: `False`
- all handles seen ok at least once: `False`
- `tenis-adidas-yeezy-slide-slate-marine-azul-escuro`: `0/4` ok rounds, never_ok `True`
- `yeezy-slide-azure`: `0/4` ok rounds, never_ok `True`
- `yeezy-slide-bone-937693978`: `0/4` ok rounds, never_ok `True`
- `yeezy-slide-glow-green`: `1/4` ok rounds, never_ok `False`
- `yeezy-slide-ochre-925686464`: `1/4` ok rounds, never_ok `False`
- `yeezy-slide-onyx`: `1/4` ok rounds, never_ok `False`
- `yeezy-slide-pure-2022`: `0/4` ok rounds, never_ok `True`

## Rollback
- backup: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-theme/curadoria-lk-prod-yeezy-slide-apply-20260605T185111Z/live-before.liquid`
- plan: Restore live-before.liquid to snippets/lk-variante-top30-visited-v2.liquid on Production/main after explicit rollback approval.

## Non-actions
- No product write
- No price/stock/app/GMC/Tiny/Klaviyo/Meta/checkout/discount/fulfillment write
- No full-file Dev-to-Production sync beyond scoped asset merge

## Focused public QA retry
- source/readback remained correct; this retry checked public CDN/edge rendering only.
- all ok every round: `False`
- all handles seen ok at least once: `False`
- `tenis-adidas-yeezy-slide-slate-marine-azul-escuro`: `0/5` ok rounds, marker rounds `0`, curadoria rounds `5`, never_ok `True`
- `yeezy-slide-azure`: `0/5` ok rounds, marker rounds `0`, curadoria rounds `5`, never_ok `True`
- `yeezy-slide-bone-937693978`: `0/5` ok rounds, marker rounds `0`, curadoria rounds `5`, never_ok `True`
- `yeezy-slide-glow-green`: `1/5` ok rounds, marker rounds `1`, curadoria rounds `5`, never_ok `False`
- `yeezy-slide-ochre-925686464`: `0/5` ok rounds, marker rounds `0`, curadoria rounds `5`, never_ok `True`
- `yeezy-slide-onyx`: `0/5` ok rounds, marker rounds `0`, curadoria rounds `5`, never_ok `True`
- `yeezy-slide-pure-2022`: `0/5` ok rounds, marker rounds `0`, curadoria rounds `5`, never_ok `True`
- raw focused QA: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-theme/curadoria-lk-prod-yeezy-slide-apply-20260605T185111Z/focused-public-qa.json`
