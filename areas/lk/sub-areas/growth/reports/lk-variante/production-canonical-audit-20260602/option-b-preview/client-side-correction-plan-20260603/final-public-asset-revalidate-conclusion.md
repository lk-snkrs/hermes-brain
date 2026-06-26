# Curadoria LK / LK Variante — public asset revalidate conclusion

Source timestamp: 2026-06-03T01:26:28.856013+00:00

## Evidence

File: `public-asset-revalidate-after-30min.json`

Result: `pass=false`

Rows checked:

- `air-jordan-1-high-85-college-navy`: live HTML fetched, but `asset=null`, `asset_marker=null`
- `tenis-nike-shox-tl-black-cave-stone-preto`: live HTML fetched, but `asset=null`, `asset_marker=null`
- `tenis-adidas-sambae-linen-gum-bege`: live HTML fetched, but `asset=null`, `asset_marker=null`
- `tenis-adidas-tokyo-off-white-core-black-branco`: live HTML fetched, but `asset=null`, `asset_marker=null`
- `moletom-alo-yoga-cropped-serenity-coverup-athletic-heather-grey-cinza`: live HTML fetched, but `asset=null`, `asset_marker=null`
- Control `new-balance-530-white-natural-indigo-1`: live HTML fetched, but `asset=null`, `asset_marker=null`

## Interpretation

The client-side fallback via `assets/lk-footer.js` cannot be called live/effective after the 30-minute wait.

The public PDP HTML did not expose a usable `lk-footer.js` asset reference for the verifier, so the exact public asset-body layer could not confirm the hotfix marker. This matches the cache pitfall: Admin Asset API readback can be clean while the public storefront continues to serve stale rendered HTML and/or stale asset references.

## Decision

Stop retrying blind cache-bust writes on Production theme/assets/products. The remaining safe next path is escalation/documentation:

1. Use the existing Shopify Support packet and append this failed public-asset revalidate evidence.
2. Ask Shopify Support for purge/investigation of rendered product HTML cache and public asset reference propagation for specific PDP routes.
3. If a workaround is still required, design a new approach only after identifying an asset/script that the stale HTML definitely loads on the affected PDPs, verified by exact public asset-body fetch.

## Non-actions

No new Shopify/GMC/Klaviyo/Meta/Tiny write is authorized by this conclusion.

## Rollback

The production footer hotfix has a local before backup in `production-footer-hotfix-20260603T005234Z/assets__lk-footer.before.js`. Rollback would require explicit Lucas approval because it is a Production theme asset write.
