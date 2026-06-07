# Receipt — Curadoria LK PDP — DEV conservative next round — 2026-06-06

## Status

DEV write executed after Lucas approval via Telegram choice:

`Aprovo DEV conservador: Sambae Hello Kitty + NB 2002R + ASICS Gel-NYC`

No Production write executed.

## Scope executed

Theme/asset:

- DEV theme: `155065450718` (`role=unpublished`)
- Production theme: `155065417950` (`role=main`)
- Asset: `snippets/lk-variante-top30-visited-v2.liquid`

Changes:

1. Expanded existing `top30-adidas-sambae-regular` group with:
   - `tenis-adidas-sambae-x-hello-kitty-cloud-white-clear-pink-branco` — label `Hello Kitty`
2. Added new marker `top30-new-balance-2002r-protection-pack`:
   - `tenis-new-balance-2002r-protection-pack-phantom-cinza-camurca-mesh` — label `Phantom`
   - `tenis-new-balance-2002r-protection-pack-rain-cloud-suede-mesh` — label `Rain Cloud`
3. Added new marker `top30-asics-gel-nyc-regular-special`:
   - `tenis-asics-gel-nyc-graphite-grey-black-preto` — label `Graphite Grey`
   - `tenis-asics-gel-nyc-x-pleasures-barely-rose-rosa` — label `Pleasures Rose`

## Backups / artifacts

- Pre-write DEV backup: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/dev-before-conservative-next-round-20260606T164820Z.liquid`
- Initial malformed DEV backup before repair: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/dev-broken-before-repair-20260606T165102Z.liquid`
- Final repaired target: `/opt/data/tmp/lk_curadoria_conservative_next_round_target_repaired_20260606T165102Z.liquid`
- Final readback: `/opt/data/tmp/lk_curadoria_conservative_next_round_readback_repaired_20260606T165102Z.liquid`
- Final QA JSON: `/opt/data/tmp/lk_curadoria_conservative_next_round_qa_repaired_20260606T165102Z.json`
- Approval packet: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/approval-packets/curadoria-lk-pdp-next-products-round-20260606.md`

## Readback evidence

Final repaired apply:

- DEV target SHA: `aab594549624f48312ba3e9a51509e4e679cd7081c25c91b120d30da08c4862a`
- DEV readback SHA: `aab594549624f48312ba3e9a51509e4e679cd7081c25c91b120d30da08c4862a`
- Readback match: `true`
- Production SHA remained unchanged: `f0b86521f3e85dd528405d2b09655fab98325f92a65d99da51ecbc80438b5723`

Post-apply refreshed coverage scan:

- DEV covered handles: `604`
- Production covered handles: `595`
- DEV groups detected: `40`
- Production groups detected: `38`

## Static QA evidence

All final static checks passed:

- `top30-adidas-sambae-regular`: found, 11 handles / 11 labels / 11 images / 11 titles, aligned, missing expected = 0, expected cards per PDP = 5.
- `top30-new-balance-2002r-protection-pack`: found, 2 handles / 2 labels / 2 images / 2 titles, aligned, missing expected = 0, expected cards per PDP = 1.
- `top30-asics-gel-nyc-regular-special`: found, 2 handles / 2 labels / 2 images / 2 titles, aligned, missing expected = 0, expected cards per PDP = 1.
- Malformed URL patterns: `0`
- `TenisMoldeLK` placeholder: `false`
- Current-product exclusion simulation: passed for all touched groups.

## Public preview QA caveat

Public unauthenticated preview requests dropped `preview_theme_id` and served canonical/live URLs, so public DEV preview HTML is inconclusive. This is the known Shopify preview caveat; source proof is Admin Asset API readback + static QA.

Samples:

- Sambae Hello Kitty: HTTP 200, final URL dropped preview param, live Curadoria present but DEV marker not provable.
- NB 2002R Phantom: HTTP 200, final URL dropped preview param, live Curadoria present but DEV marker not provable.
- ASICS Gel-NYC Graphite: HTTP 200, final URL dropped preview param, live Curadoria not present, consistent with live/Production not yet containing DEV group.

## Issue detected and repaired during QA

The first DEV PUT had a malformed Sambae append caused by bad string insertion before the Liquid `{%- assign ... %}` line. Static QA caught it immediately. Repair action:

1. Backed up the malformed DEV readback.
2. Regenerated the final target from the pre-write backup.
3. Re-uploaded only the approved DEV scope.
4. Re-ran readback/static QA successfully.

Final DEV source is clean and readback-matched.

## Rollback

To rollback DEV, restore the pre-write backup:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/dev-before-conservative-next-round-20260606T164820Z.liquid`

Production rollback is not needed because Production was not changed.

## Next decision

If Lucas approves, next step is authenticated visual DEV review or wait for a separate Production approval packet/merge path. Cloudtilt mixed regular/Loewe remains deferred unless explicitly approved.
