# Latest execution status — LK collection auto-ordering pilot

Date: 2026-05-27T13:05:28Z

## Status

Executed and verified.

Update 2026-05-27T13:46Z: Nude Project visual/order correction applied after Lucas selected `NEW em estoque primeiro`. Public readback now shows available `new` products in positions 1–3, followed by prior best-sellers; unavailable `new` Side-Eye remains out of top placement.

Update 2026-05-27T15:21Z: New Balance 204L single-collection test applied. Logic used: top 4 sellable recent products (<=90d, newest first), then `best-seller`, then remaining sellable products in prior order, unavailable last. First write created a rollback snapshot and applied 5 moves; second verification readback/public check matched with no extra moves.

Update 2026-05-27T15:28Z: New Balance 204L visual NEW correction applied after Lucas confirmed. Cause: live product-card badge used `created_at <= 30 days`, so only the first two May-created products showed NEW. Fix: product-card badge now also accepts product tag `new`; tag `new` added only to products 3 and 4. Public HTML probe confirms the first 4 product cards have `pc__badge--new`.

## Scope approved by Lucas

"Aprovo o write na Shopify para aplicar o piloto de ordenação nas coleções elegíveis aprovadas, com snapshot antes, new primeiro, esgotados no final, readback depois e sem ativar cron."

## What was executed

- Shopify collection order pilot for the 10 approved collections.
- Immediate pre-write rollback snapshot was created before the 2026-05-27 write attempt.
- `collectionReorderProducts` was used only where the live order differed from the recomputed approved proposal.
- Readback/repair verification was run after the write attempt.
- Public Nude Project `products.json` top 8 was checked after Admin readback.

## 2026-05-27 run notes

- Initial apply run: processed 7 collections before local command timeout.
- The only actual move batch in that run was Pace: 42 moves, readback matched.
- Snapshot-backed repair/readback was then run for all 10 collections and returned 10/10 `readback_match=true` with 0 additional moves required.
- Final read-only Admin verification returned 10/10 `readback_match=true`.

## Verified pilot collections

- Nude Project — verified
- Jacquemus — verified
- Saint Studio — verified
- Calça | Apparels — verified
- Pace — verified
- Aimé Leon Dore — verified
- Nike Mind — verified
- Onitsuka Tiger Mexico 66 — verified
- Onitsuka Tiger Mexico 66 Sabot — verified
- Shorts — verified

## Nude Project public check

Public `/collections/nude-project/products.json?limit=8` after execution:

1. Camiseta Nude Project Global Soon
2. Camiseta Nude Project Global Soon Black Preto
3. Moletom Nude Project Kill Bill Zip-Up Ash Cinza
4. Camiseta Nude Project Xoxo Cinza
5. Moletom Nude Project Cult Hoodie Black/Beige Preto
6. Calça Nude Project Jeans Old Baggy Black/Purple Preto/Roxo
7. Camiseta Nude Project Kora Black Preto
8. Camiseta Nude Project Honor Tee Marshmallow Off White

Specific Nude Project readback checks:

- `Side-Eye Zip-Up`: position 76, Shopify positive inventory false, kept near final sold-out bucket.
- `Old Baggy Black/Purple`: position 6, Shopify positive inventory true, kept visible.
- `Juicy Cherry`: position 19, Shopify positive inventory true.

## Artifacts

- 2026-05-27 snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/auto-sort-collections/2026-05-26-pilot-apply/apply-run-20260527T125252Z/rollback-snapshot-pre-write-immediate.json`
- Initial progress receipt: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/auto-sort-collections/2026-05-26-pilot-apply/apply-run-20260527T125252Z/receipt-progress.json`
- Snapshot repair receipt: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/auto-sort-collections/2026-05-26-pilot-apply/repair-from-snapshot-20260527T130343Z/REPAIR-FROM-SNAPSHOT-RECEIPT.md`
- Final read-only verification: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/auto-sort-collections/2026-05-26-pilot-apply/readonly-verify-20260527T130528Z/READONLY-VERIFICATION.md`

## Pending

- Design weekly LK merchandising automation for `new` and `best-seller`: proposal/approval first, then snapshot, dry-run preview, readback, public probe, rollback plan, and no recurring write/cron activation without explicit approval.

## Non-actions

- No cron activated.
- No product title/description/price/stock/availability changed.
- No product tags changed, except the approved New Balance 204L visual NEW correction added `new` to products 3 and 4.
- No SEO field, checkout, campaign, Klaviyo, WhatsApp, customer communication, GMC/feed write, or discount changed.
- Theme write occurred only for the approved product-card NEW badge logic correction.

## Rollback

Rollback source for the 2026-05-27 execution is the immediate pre-write snapshot above. Restore by applying each collection's `current_order_product_ids` with `collectionReorderProducts`, polling the Shopify job, then running the same read-only verification.
