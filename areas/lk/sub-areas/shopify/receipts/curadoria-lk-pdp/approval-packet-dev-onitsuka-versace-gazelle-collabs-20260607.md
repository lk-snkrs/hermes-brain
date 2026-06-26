# Approval packet — DEV Curadoria LK PDP Onitsuka Versace + Gazelle Indoor Collabs

Date: 2026-06-07

## User signal

Lucas said: `Perfeito seguir` after the Production merge for Cortez + Speedcat.

Interpretation: continue autonomously in **read-only discovery / next DEV approval packet**. This does **not** authorize DEV upload, Production merge, product writes, stock/price changes, GMC, Klaviyo, Meta, WhatsApp, email, campaign, Tiny, checkout, discount, fulfillment, or external writes.

## Worker invocation receipt

- demand_classification: LK Shopify / Curadoria LK PDP continuation after Production merge
- canonical_playbook: `lk-shopify-variant-thumbnails` read-only next-batch continuation
- workers_selected:
  - Parser/Readback lane: current production branch/source parsing and coverage scan
  - Curadoria Semântica lane: candidate grouping by silhouette/capsule/collab
  - Validação de Imagens lane: public `.js` + CDN image validation
  - QA Visual/Public-readiness lane: public URL readiness; no preview/theme write
- workers_skipped: paid media, GMC/feed, stock/Tiny, Klaviyo/CRM, LKGOC
- delegation_tool_used: no
- reason_if_no_delegation: no delegate_task tool is available in this runtime; lanes executed directly by LK Shopify Hermes with tool-backed evidence
- owner_agent_final_decision: recommend a narrow DEV packet with two clean groups only; hold Production until after DEV readback/QA and separate approval

## Evidence read-only

Catalog/public scan:

- Public catalog products scanned: 1809
- Current Curadoria covered handles estimated from Production source: 572
- Current Curadoria markers in Production source: 53
- Candidate validation used public product `.js` and first image CDN URL checks.
- Output JSON: `/opt/data/tmp/lk_curadoria_post_prod_next_readonly_20260607.json`

Production already has existing broad groups for:

- Samba OG
- New Balance 9060
- Adidas Gazelle Indoor regular
- Adidas Handball Spezial regular

Therefore this packet avoids duplicating existing regular groups and proposes clean **collab/capsule split snippets** for uncovered PDPs.

## Recommended DEV batch

### Group 1 — Onitsuka Tiger x Versace TAI-CHI Sakura

Why safe:

- Same collaboration/capsule: Onitsuka Tiger x Versace TAI-CHI Sakura.
- Same product family; variations are material/color differences (Metallic, Suede, Nappa).
- 7/7 public product `.js` OK.
- 7/7 image CDN OK.
- No current Production Curadoria marker detected for this capsule.

Proposed marker:

- `top30-onitsuka-versace-tai-chi-sakura`

Proposed handles:

1. `tenis-onitsuka-tiger-x-versace-tai-chi-sakura-metallic-sneakers-silver-gold-prateado`
2. `tenis-onitsuka-tiger-x-versace-tai-chi-sakura-suede-sneakers-blue-azul`
3. `tenis-onitsuka-tiger-x-versace-tai-chi-sakura-suede-sneakers-green`
4. `tenis-onitsuka-tiger-x-versace-tai-chi-sakura-nappa-sneakers-brown-yellow-amarelo`
5. `tenis-onitsuka-tiger-x-versace-tai-chi-sakura-nappa-sneakers-black-brown-preto`
6. `tenis-onitsuka-tiger-x-versace-tai-chi-sakura-nappa-sneakers-pink-rosa`
7. `tenis-onitsuka-tiger-x-versace-tai-chi-sakura-suede-sneakers-brown-bege`

Suggested short labels:

- Metallic Silver Gold
- Suede Blue
- Suede Green
- Nappa Brown Yellow
- Nappa Black Brown
- Nappa Pink
- Suede Brown

### Group 2 — Adidas Gazelle Indoor collabs/specials

Why safe:

- Same silhouette: Adidas Gazelle Indoor.
- Existing Production group covers Gazelle Indoor regular; these are cleanly separated as collabs/specials (Bad Bunny, Liberty London, Clot, Hello Kitty/Messi).
- 7/7 public product `.js` OK.
- 7/7 image CDN OK.
- Separate group avoids mixing collabs into the existing regular Gazelle marker.

Proposed marker:

- `top30-adidas-gazelle-indoor-collabs`

Proposed handles:

1. `tenis-adidas-gazelle-indoor-bad-bunny-cabo-rojo-rosa`
2. `tenis-adidas-gazelle-indoor-liberty-london-floral-embroidery-stripes-multi-color`
3. `tenis-adidas-gazelle-indoor-liberty-london-floral-embroidery-multi-color`
4. `tenis-adidas-gazelle-indoor-x-clot-by-edison-chen-off-white-branco`
5. `tenis-adidas-bad-bunny-gazelle-indoor-x-messi-cardboard-marrom`
6. `tenis-adidas-gazelle-indoor-x-hello-kity-anniversary-cloud-white-red-branco`
7. `tenis-adidas-gazelle-indoor-x-bad-bunny-san-juan-azul`

Suggested short labels:

- Bad Bunny Cabo Rojo
- Liberty Stripes
- Liberty Floral
- Clot Off White
- Bad Bunny Messi
- Hello Kitty
- Bad Bunny San Juan

## Deferred / not recommended now

- Samba OG animal/pony/leopard: 10 public-valid products, but mixes Samba OG and Samba LT. Good future packet after manual split decision.
- New Balance 9060: broad existing group already exists; first candidate had placeholder `TenisMoldeLK`, so not clean for this round.
- Adidas Handball Spezial: existing regular group exists; uncovered Sporty & Rich pair is only 2 products and one extra regular product, so too small/mixed for this round.
- Air Max 90 Patta: clean but only 2 products; hold unless Lucas wants smaller 2-item groups.

## Proposed implementation if approved

DEV/unpublished only:

1. Verify exact DEV theme role is `unpublished` before upload.
2. Backup DEV `sections/lk-pdp.liquid` and any target snippet before write.
3. Use split snippet pattern because Production active Curadoria snippet is near/over the practical 256 KB asset limit.
4. Create one dedicated snippet, e.g. `snippets/lk-variante-onitsuka-versace-gazelle-collabs-20260607.liquid`.
5. Add one render call in DEV `sections/lk-pdp.liquid` only.
6. Each group section must have `{%- if lk_handles contains product.handle -%}` guard.
7. Split snippet must load `lk-variante.css` locally and use its own render guard, not `lk_top30_rendered` from another render scope.
8. Use canonical classes only:
   - `lk-variante__head`
   - `lk-variante__rail`
   - `lk-variante__media`
9. Prohibited classes:
   - `lk-variante__grid`
   - `lk-variante__image-wrap`
10. Read back DEV assets by Shopify Asset API and compare SHA/markers.
11. Static QA:
   - marker count 1 each
   - handles aligned with labels/images/titles
   - no duplicate handles
   - no malformed/placeholder image URLs
   - current PDP excluded from cards
   - wrong sibling marker absent for representative PDPs
12. Public preview QA if Shopify preview HTML serves DEV; otherwise mark preview public HTML as inconclusive and rely on readback/static QA.

## Approval needed

To apply this packet to DEV only, Lucas can approve with:

`Aprovo DEV Onitsuka Versace + Gazelle Indoor Collabs`

This approval would not authorize Production. Production would require a separate phrase after DEV readback/QA.
