# Receipt — Production merge Curadoria LK PDP Onitsuka Versace + Gazelle Indoor Collabs

Date: 2026-06-07

## Scope

Lucas replied `Aprovo` immediately after the requested phrase for Production. Interpreted as approval for:

`Aprovo merge para Production Onitsuka Versace + Gazelle Indoor Collabs`

Executed scope: **merge para Production** for the previously DEV-approved Curadoria LK PDP package only.

No product, price, stock, collection, metafield, tag, GMC/feed, Klaviyo, ads, WhatsApp, email, campaign, Tiny, checkout, discount, fulfillment, or non-theme change was executed.

## Worker invocation receipt

- demand_classification: LK Shopify / Curadoria LK PDP Production merge after DEV approval
- canonical_playbook: `lk-shopify-variant-thumbnails` → scoped Dev-to-Production merge, not blind sync
- workers_selected:
  - GitHub PR/merge lane
  - Shopify Production readback lane
  - Static/source QA lane
  - Public storefront QA lane
- workers_skipped: product/metafield/tag, stock/Tiny, GMC/feed, Klaviyo/CRM, paid media, WhatsApp/email
- delegation_tool_used: no
- reason_if_no_delegation: no delegate_task tool available in runtime; lanes executed directly by LK Shopify Hermes with tool-backed verification
- owner_agent_final_decision: GitHub Production merge complete; Shopify Production source/readback clean; public storefront partially/intermittently propagated in edge cache

## GitHub Production merge

Repository: `lk-snkrs/lk-new-theme`

- Base branch: `production`
- Work branch: `hermes/onitsuka-gazelle-production-20260607`
- PR: `https://github.com/lk-snkrs/lk-new-theme/pull/34`
- PR state: closed/merged
- Merge commit SHA: `79bcc44ece6c832fb4d981e68bce124b225fb213`
- Production branch head after merge: `79bcc44ece6c832fb4d981e68bce124b225fb213`
- Work branch deleted: yes, GitHub API delete returned `204`

Changed files:

1. `sections/lk-pdp.liquid`
   - Added scoped render call:
     - `{%- render 'lk-variante-onitsuka-versace-gazelle-collabs-20260607', product: product -%}`
2. `snippets/lk-variante-onitsuka-versace-gazelle-collabs-20260607.liquid`
   - New split snippet containing:
     - `top30-onitsuka-versace-tai-chi-sakura`
     - `top30-adidas-gazelle-indoor-collabs`

## Shopify Production readback

Production theme:

- Theme ID: `155065417950`
- Role: `main`

Readback receipt JSON:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/prod-onitsuka-versace-gazelle-collabs-20260607/20260607T005418Z-receipt.json`

Readback files:

- Section: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/prod-onitsuka-versace-gazelle-collabs-20260607/20260607T005418Z-prod-section__lk-pdp.liquid`
- Snippet: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/prod-onitsuka-versace-gazelle-collabs-20260607/20260607T005418Z-prod-snippet__lk-variante-onitsuka-versace-gazelle-collabs-20260607.liquid`

Readback SHA matched target immediately:

- Section SHA: `c483cfe4a8486f056aa3a3fab4fc4f453b54fb358fd5b769e1cd25da21bebc81`
- Snippet SHA: `f25d727cf39b46df0676afaabbfe06d989ecd75e5a2d5904b24482172a946ecb`

## Static/source QA

Passed on Production readback:

- `readback_match.section`: `true`
- `readback_match.snippet`: `true`
- `render_count`: `1`
- marker `top30-onitsuka-versace-tai-chi-sakura`: `1`
- marker `top30-adidas-gazelle-indoor-collabs`: `1`
- `lk-variante__grid`: `0`
- `lk-variante__image-wrap`: `0`
- `lk-variante__head`: `2`
- `lk-variante__rail`: `2`
- `lk-variante__media`: `2`
- static problems: `[]`

## Public Production QA

Initial public representative QA immediately after readback:

- 2 representative PDPs returned HTTP `200`, no Liquid errors, but no marker visible yet.
- Classified as likely edge/cache propagation, not source failure.

Follow-up multi-round QA:

- File: `/opt/data/tmp/lk_curadoria_onitsuka_gazelle_prod_focused_missing_qa_20260607T005644Z.json`
- Adidas Gazelle Bad Bunny Cabo Rojo:
  - rounds 1–3: marker present, 5 media cards, current link excluded, no Liquid error
  - round 4: marker absent again
- Onitsuka Suede Green:
  - round 3: marker present, 5 media cards, current link excluded, no Liquid error
  - other rounds: marker absent

Full batch public sample:

- File: `/opt/data/tmp/lk_curadoria_onitsuka_gazelle_prod_public_fullqa_20260607T005550Z.json`
- Observed markers in 12/14 PDP captures at that moment:
  - Onitsuka marker: 6/7
  - Gazelle marker: 6/7
- Several captures had the expected block with `5` media cards and no Liquid error.

Classification:

- Source/readback/static QA: **OK**.
- Public storefront: **partially propagated / intermittent Shopify edge cache**, consistent with prior Curadoria Production merges.
- No Liquid syntax/runtime error observed.

## Rollback

Preferred rollback path:

1. Open a revert PR against `production` reverting merge commit `79bcc44ece6c832fb4d981e68bce124b225fb213`.
2. Verify Shopify Production readback after revert:
   - `sections/lk-pdp.liquid` no longer contains the Onitsuka/Gazelle split-snippet render call.
   - `snippets/lk-variante-onitsuka-versace-gazelle-collabs-20260607.liquid` removed or no longer deployed.

Emergency rollback path, only with explicit approval:

- Restore the pre-merge Production source and remove/delete the split snippet from the Production theme.

## Next decision

No further source write is recommended right now. Let public edge/cache settle; if a specific handle remains permanently absent after focused retries, prepare a targeted repair packet instead of repeating broad writes.
