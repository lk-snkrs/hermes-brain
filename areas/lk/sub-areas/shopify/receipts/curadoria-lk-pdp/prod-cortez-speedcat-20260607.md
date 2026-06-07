# Receipt — Production merge Curadoria LK PDP Cortez + Speedcat

Date: 2026-06-07

## Scope

Lucas approved Production immediately after the requested phrase `Aprovo merge para Production Cortez + Speedcat`.

Executed scope: **merge para Production** for Curadoria LK PDP Cortez + Speedcat only.

No product, price, stock, collection, GMC, Klaviyo, ads, WhatsApp, email, campaign, Tiny, checkout, discount, fulfillment, or non-theme change was executed.

## GitHub Production merge

Repository: `lk-snkrs/lk-new-theme`

- Base branch: `production`
- Work branch: `hermes/cortez-speedcat-production-20260607`
- PR: `https://github.com/lk-snkrs/lk-new-theme/pull/33`
- PR state: closed/merged
- Merge commit SHA: `be953b4c18e9f2d7825b5a1d07099cfd1d4adf2a`
- Production branch head after merge: `be953b4c18e9f2d7825b5a1d07099cfd1d4adf2a`
- Work branch deleted: yes, GitHub ref returned 404 after merge/delete

Changed files:

1. `sections/lk-pdp.liquid`
   - Added scoped render call:
     - `{%- render 'lk-variante-cortez-speedcat-20260607', product: product -%}`
2. `snippets/lk-variante-cortez-speedcat-20260607.liquid`
   - New split snippet containing:
     - `top30-nike-cortez-breadth`
     - `top30-puma-speedcat-breadth`

## Shopify Production readback

Production theme:

- Theme ID: `155065417950`
- Role: `main`

Readback receipt JSON:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/prod-cortez-speedcat-20260607/20260607T003442Z-receipt.json`

Readback files:

- Section: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/prod-cortez-speedcat-20260607/20260607T003442Z-prod-section__lk-pdp.liquid`
- Snippet: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/prod-cortez-speedcat-20260607/20260607T003442Z-prod-snippet__lk-variante-cortez-speedcat-20260607.liquid`

Readback SHA:

- Snippet SHA: `3a75dcd37a40a264176300326190c3fb40e82fe7b24f254a7cc6bc7c7b7d91fc`
- Section SHA: `bef0b79427372f1bb241e697e6a61ffafeccf02bfcf5a4a8209d8c7c2c9878b3`

## Static QA

Passed on Production readback:

- snippet exists: yes
- section render call count: 1
- `lk-variante__grid`: 0
- `lk-variante__image-wrap`: 0
- `lk-variante__rail`: 2
- `lk-variante__media`: 2
- `lk-variante__head`: 2
- CSS tag in split snippet: 1
- group membership guards: 2
- marker `top30-nike-cortez-breadth`: 1
- marker `top30-puma-speedcat-breadth`: 1
- Cortez handles present: 7/7
- Speedcat handles present: 5/5
- duplicate handles: 0

## Public Production QA

Initial representative QA:

- Cortez `tenis-nike-cortez-sl-white-gym-red-branco`: HTTP 200, expected marker present, wrong marker absent, rail present.
- Cortez `tenis-nike-cortez-white-laser-fuchsia-branco`: HTTP 200, expected marker present, wrong marker absent, rail present.
- Speedcat `tenis-puma-speedcat-og-red-white-vermelho`: HTTP 200, marker absent in this first capture.

Focused Speedcat multi-round QA showed intermittent Shopify edge/cache propagation:

- `tenis-puma-speedcat-og-pele-yellow-black-amarelo`: marker present in sample.
- `tenis-puma-speedcat-silk-chocotart-warm-white-marrom`: marker present in sample.
- `tenis-puma-speedcat-og-pink-white-rosa`: present in rounds 1-3, absent in round 4.
- `tenis-puma-speedcat-og-red-white-vermelho`: present in round 1, absent in rounds 2-4.
- `tenis-puma-speedcat-og-team-royal-white-azul`: absent in round 1, present in rounds 2-4.

Classification:

- Source/readback/static QA: **ok**.
- Public storefront: **partially propagated / edge intermittent**, not a source failure.

## Rollback

Preferred rollback path:

1. Open a revert PR against `production` reverting merge commit `be953b4c18e9f2d7825b5a1d07099cfd1d4adf2a`.
2. Verify Shopify Production readback after revert:
   - `sections/lk-pdp.liquid` no longer contains the Cortez/Speedcat render call.
   - `snippets/lk-variante-cortez-speedcat-20260607.liquid` removed or no longer deployed.

Emergency rollback path, only with explicit approval:

- Restore `sections/lk-pdp.liquid` to the pre-merge Production source and remove/delete the split snippet from the Production theme.

## Next decision

No further Production write is needed right now.

Recommended next step: monitor public Speedcat/Cortez for edge stabilization before starting another Production merge. If one specific handle remains permanently absent after focused retries, prepare a targeted repair packet instead of rolling back the whole merge.
