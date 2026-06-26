# Receipt — DEV Curadoria LK PDP Onitsuka Versace + Gazelle Indoor Collabs

Date: 2026-06-07
Timestamp: 20260607T004957Z

## Approval

Lucas replied: `Aprovado` immediately after the DEV approval packet for:

- Onitsuka Tiger x Versace TAI-CHI Sakura
- Adidas Gazelle Indoor collabs/specials

Interpreted scope: DEV/unpublished theme write only. No Production approval.

## Worker invocation receipt

- demand_classification: LK Shopify / Curadoria LK PDP DEV approved execution
- canonical_playbook: `lk-shopify-variant-thumbnails` approved DEV split-snippet workflow
- workers_selected:
  - Shopify theme preflight/readback lane
  - Liquid snippet/render-call lane
  - Static QA lane
  - Public preview attempt lane
- workers_skipped: Production promotion, product/metafield/tag, stock/Tiny, GMC/feed, Klaviyo/CRM, paid media, WhatsApp/email
- delegation_tool_used: no
- reason_if_no_delegation: no delegate_task tool available in runtime; lanes executed directly by LK Shopify Hermes with tool-backed verification
- owner_agent_final_decision: DEV applied and readback-clean; public preview HTML was inconclusive due Shopify preview/session behavior; do not Production-merge without separate approval

## Theme preflight

DEV theme:

- Theme ID: `155065450718`
- Name: `lk-new-theme/dev`
- Role: `unpublished`

Production theme:

- Theme ID: `155065417950`
- Name: `lk-new-theme/production`
- Role: `main`

## Assets written

Only DEV/unpublished assets:

1. `snippets/lk-variante-onitsuka-versace-gazelle-collabs-20260607.liquid`
2. `sections/lk-pdp.liquid`

No Production write.

## Groups added on DEV

### Onitsuka Tiger x Versace TAI-CHI Sakura

Marker: `top30-onitsuka-versace-tai-chi-sakura`

Handles:

1. `tenis-onitsuka-tiger-x-versace-tai-chi-sakura-metallic-sneakers-silver-gold-prateado`
2. `tenis-onitsuka-tiger-x-versace-tai-chi-sakura-suede-sneakers-blue-azul`
3. `tenis-onitsuka-tiger-x-versace-tai-chi-sakura-suede-sneakers-green`
4. `tenis-onitsuka-tiger-x-versace-tai-chi-sakura-nappa-sneakers-brown-yellow-amarelo`
5. `tenis-onitsuka-tiger-x-versace-tai-chi-sakura-nappa-sneakers-black-brown-preto`
6. `tenis-onitsuka-tiger-x-versace-tai-chi-sakura-nappa-sneakers-pink-rosa`
7. `tenis-onitsuka-tiger-x-versace-tai-chi-sakura-suede-sneakers-brown-bege`

Labels:

- Metallic Silver Gold
- Suede Blue
- Suede Green
- Nappa Brown Yellow
- Nappa Black Brown
- Nappa Pink
- Suede Brown

### Adidas Gazelle Indoor collabs/specials

Marker: `top30-adidas-gazelle-indoor-collabs`

Handles:

1. `tenis-adidas-gazelle-indoor-bad-bunny-cabo-rojo-rosa`
2. `tenis-adidas-gazelle-indoor-liberty-london-floral-embroidery-stripes-multi-color`
3. `tenis-adidas-gazelle-indoor-liberty-london-floral-embroidery-multi-color`
4. `tenis-adidas-gazelle-indoor-x-clot-by-edison-chen-off-white-branco`
5. `tenis-adidas-bad-bunny-gazelle-indoor-x-messi-cardboard-marrom`
6. `tenis-adidas-gazelle-indoor-x-hello-kity-anniversary-cloud-white-red-branco`
7. `tenis-adidas-gazelle-indoor-x-bad-bunny-san-juan-azul`

Labels:

- Bad Bunny Cabo Rojo
- Liberty Stripes
- Liberty Floral
- Clot Off White
- Bad Bunny Messi
- Hello Kitty
- Bad Bunny San Juan

## Readback evidence

Readback SHA matched target for both written assets:

- `sections/lk-pdp.liquid`: `d1aecd6784a3303491f4ac17b0ccfcd148c8288f5f83aa7522d165b43764b893`
- `snippets/lk-variante-onitsuka-versace-gazelle-collabs-20260607.liquid`: `f25d727cf39b46df0676afaabbfe06d989ecd75e5a2d5904b24482172a946ecb`

Production unchanged:

- `prod_section_unchanged`: `true`
- `prod_snippet_unchanged`: `true`
- Production did not have this split snippet before.

## QA evidence

Public product/image preflight:

- 14/14 product `.js` checks returned `200`
- 14/14 image URL checks returned `200`

Static/readback QA:

- `static_readback_problems`: `[]`
- Render line count in `sections/lk-pdp.liquid`: `1`
- Marker counts:
  - `top30-onitsuka-versace-tai-chi-sakura`: `1`
  - `top30-adidas-gazelle-indoor-collabs`: `1`
- Required classes:
  - `lk-variante__head`: `2`
  - `lk-variante__rail`: `2`
  - `lk-variante__media`: `2`
- Prohibited classes:
  - `lk-variante__grid`: `0`
  - `lk-variante__image-wrap`: `0`
- Simulation: every current product excludes itself and renders 5 cards from the group.

Public preview attempt:

- Attempted `preview_theme_id=155065450718` for one Onitsuka and one Gazelle PDP.
- HTTP status: `200`
- Markers not found in returned public HTML.
- Liquid errors: `false`
- Interpretation: inconclusive preview public HTML; Shopify may strip preview cookie/session. Asset API DEV readback is authoritative for DEV source in this receipt.

## Artifact paths

Apply JSON:

- `/opt/data/tmp/lk_curadoria_onitsuka_gazelle_dev_apply_20260607T004957Z.json`

Static QA JSON:

- `/opt/data/tmp/lk_curadoria_onitsuka_gazelle_dev_qa_static_20260607T004957Z.json`

DEV readbacks:

- `/opt/data/tmp/lk_curadoria_onitsuka_gazelle_dev_section_readback_20260607T004957Z.liquid`
- `/opt/data/tmp/lk_curadoria_onitsuka_gazelle_dev_snippet_readback_20260607T004957Z.liquid`

Backups:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/dev-onitsuka-versace-gazelle-collabs-20260607/20260607T004957Z-before-section__lk-pdp.liquid`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/dev-onitsuka-versace-gazelle-collabs-20260607/20260607T004957Z-before-snippet__lk-variante-onitsuka-versace-gazelle-collabs-20260607.liquid`

## Rollback

DEV rollback only:

1. Restore the backed-up `sections/lk-pdp.liquid` to DEV theme `155065450718`.
2. Delete or blank the DEV snippet `snippets/lk-variante-onitsuka-versace-gazelle-collabs-20260607.liquid`.
3. Re-read both assets and verify the two markers are absent.

Production rollback not needed because Production was unchanged.

## Non-actions

- No Production write.
- No merge para Production.
- No product/metafield/tag write.
- No stock, price, discount, checkout, fulfillment, GMC/feed, Klaviyo, Meta, WhatsApp, email or campaign change.

## Next decision

If Lucas approves Production after reviewing DEV/source evidence, use separate explicit Production approval. Suggested phrase:

`Aprovo merge para Production Onitsuka Versace + Gazelle Indoor Collabs`
