# Receipt — Curadoria LK PDP — DEV Cloudtilt mixed — 2026-06-06

## Status

DEV write executed after Lucas approval:

`Aprovo DEV completo: conservador + Cloudtilt mixed regular/Loewe`

No Production write executed.

## Scope executed

- DEV theme: `155065450718` (`role=unpublished`)
- Production theme: `155065417950` (`role=main`)
- Asset: `snippets/lk-variante-top30-visited-v2.liquid`

Added new mixed regular/Loewe group:

- Marker: `top30-on-running-cloudtilt-regular-loewe`
- `tenis-on-running-cloudtilt-preto-e-branco` — label `Black Ivory`
- `tenis-on-running-cloudtilt-loewe-denim-blue-azul` — label `Loewe Blue`
- `tenis-on-running-cloudtilt-loewe-denim-grey-cinza` — label `Loewe Grey`

## Backups / artifacts

- DEV backup before Cloudtilt write: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/dev-before-cloudtilt-mixed-20260606T165438Z.liquid`
- Target file: `/opt/data/tmp/lk_curadoria_cloudtilt_mixed_target_20260606T165438Z.liquid`
- Readback file: `/opt/data/tmp/lk_curadoria_cloudtilt_mixed_readback_20260606T165438Z.liquid`
- QA JSON: `/opt/data/tmp/lk_curadoria_cloudtilt_mixed_qa_20260606T165438Z.json`

## Readback evidence

- DEV before SHA: `aab594549624f48312ba3e9a51509e4e679cd7081c25c91b120d30da08c4862a`
- DEV target SHA: `11e1939aad3adfccc3fb6ea33cf0eb9c7f5050de72803ec45a6d6af2393b773d`
- DEV readback SHA: `11e1939aad3adfccc3fb6ea33cf0eb9c7f5050de72803ec45a6d6af2393b773d`
- Readback match: `true`
- Marker count: `1`
- Production before/after SHA unchanged: `f0b86521f3e85dd528405d2b09655fab98325f92a65d99da51ecbc80438b5723`

## Static QA evidence

Cloudtilt mixed group:

- Found: true
- Handles/labels/images/titles: `3/3/3/3`
- Aligned: true
- Missing handles: `0`
- Missing labels: `0`
- Expected cards per PDP after current-product exclusion: `2`
- Malformed URL patterns: `0`
- Placeholder `TenisMoldeLK`: false
- Image checks: all 3 CDN image URLs returned HTTP 200

Post-apply refreshed coverage scan:

- DEV covered handles: `607`
- Production covered handles: `595`
- DEV groups detected: `41`
- Production groups detected: `38`

## Public preview/storefront QA caveat

Public unauthenticated preview requests again dropped `preview_theme_id`, so marker-level DEV preview proof is inconclusive.

Additional focused public retries showed transient storefront 503s on Cloudtilt HTML/JS, but image CDN and Admin readback/static QA are correct:

- Cloudtilt Black Ivory HTML: 503 on retry; `.js`: 200 on retry
- Cloudtilt Loewe Blue HTML: 503 on retry; `.js`: 200 on retry
- Cloudtilt Loewe Grey HTML: 200 on retry; `.js`: one retry 503

Classification: storefront/CDN/rate-limit noise on public unauthenticated QA, not source/readback failure.

## Rollback

To rollback this Cloudtilt DEV addition, restore:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/dev-before-cloudtilt-mixed-20260606T165438Z.liquid`

No Production rollback needed because Production was not changed.

## Next decision

DEV now contains the full approved round:

- Sambae Hello Kitty
- NB 2002R Protection Pack
- ASICS Gel-NYC
- On Running Cloudtilt regular/Loewe mixed

Next step, if Lucas wants: prepare the separate **merge para Production** packet for this DEV scope.
