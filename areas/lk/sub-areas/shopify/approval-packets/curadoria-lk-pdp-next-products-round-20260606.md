# Approval Packet — Curadoria LK PDP — Next products round — DEV — 2026-06-06

## Status

Prepared read-only. No Shopify/theme write executed in this step.

## Current request

Lucas asked to continue adding more products to LK Thumbnails PDP / Curadoria LK and to define the order of importance using subagents.

Per LK Shopify guardrails: this is read-only continuation + DEV approval packet. It does **not** authorize a Shopify theme upload.

## Worker/subagent lanes used

- **Parser/Readback:** refreshed DEV + Production active snippet coverage.
- **Curadoria Semântica:** ranked same-model/silhouette fit, existing-group expansion vs net-new sparse groups, and mixed regular/collab caveats.
- **Imagens/Publicação:** validated PDP HTML, `/products/<handle>.js`, CDN image and product availability for candidates.
- **QA Visual:** planned post-DEV checks for card count, current-product exclusion, CSS/typography light layers.

## Evidence — refreshed baseline

- Timestamp: `2026-06-06T16:41:26.707893+00:00`
- DEV theme: `155065450718`
- Production theme: `155065417950`
- Active asset: `snippets/lk-variante-top30-visited-v2.liquid`
- Catalog products scanned: `2331`
- DEV covered handles: `599`
- Production covered handles: `595`
- Covered union: `599`
- Detected Curadoria render groups in DEV/Production: `38`
- Read-only scan output: `/opt/data/tmp/lk_curadoria_more_products_readonly_20260606.json`

## Recommended order of importance

### P1 — Expand existing Adidas Sambae group with Hello Kitty

Why first:

- Existing group already exists and is dense: `top30-adidas-sambae-regular` currently has 10 handles.
- Adds one currently uncovered, public-valid and available PDP into a rail that already renders meaningful alternatives.
- Better UX than creating a new 2-product sparse rail.

Candidate:

- `tenis-adidas-sambae-x-hello-kitty-cloud-white-clear-pink-branco`
  - Label: `Hello Kitty`
  - PDP HTML: 200
  - Product JS: 200
  - CDN image: 200
  - Available: true
  - Caveat: collab/capsule inside a mostly regular Sambae group; acceptable only if Lucas wants breadth inside same silhouette.

### P2 — On Running Cloudtilt regular/special group, only if Lucas accepts mixed pricing/capsule

Why second:

- Highest remaining uncovered clean-ish cluster by count: 3 public-valid and available products.
- Same Cloudtilt silhouette, but it mixes regular Cloudtilt with Loewe Cloudtilt.

Candidates:

- `tenis-on-running-cloudtilt-preto-e-branco` — label `Black Ivory` — available true
- `tenis-on-running-cloudtilt-loewe-denim-blue-azul` — label `Loewe Denim Blue` — available true
- `tenis-on-running-cloudtilt-loewe-denim-grey-cinza` — label `Loewe Denim Grey` — available true

Caveat:

- 3-product group renders up to 2 alternatives after current-product exclusion.
- Price/capsule jump is large: regular Cloudtilt around R$3.999, Loewe around R$9.999 in public JS price units. This should be explicit.

### P3 — New Balance 2002R Protection Pack micro-group

Why third:

- Very clean semantic fit: same model + same Protection Pack language.
- Both public-valid and available.

Candidates:

- `tenis-new-balance-2002r-protection-pack-phantom-cinza-camurca-mesh` — label `Phantom`
- `tenis-new-balance-2002r-protection-pack-rain-cloud-suede-mesh` — label `Rain Cloud`

Caveat:

- 2-product group renders only 1 alternative card after excluding the current PDP.

### P4 — ASICS Gel-NYC micro-group

Why fourth:

- Same model; both public-valid and available.
- Semantically weaker than NB 2002R because it mixes regular Graphite Grey with Pleasures collab.

Candidates:

- `tenis-asics-gel-nyc-graphite-grey-black-preto` — label `Graphite Grey`
- `tenis-asics-gel-nyc-x-pleasures-barely-rose-rosa` — label `Pleasures Rose`

Caveat:

- 2-product group renders only 1 alternative card.

### Hold / do not prioritize now

These are public-valid and available, but they are singletons or too sparse to create useful rails today:

- `air-max-plus-black-university-blue`
- `tenis-jordan-11-retro-low-university-blue-2026-azul`
- `tenis-new-balance-740-x-concepts-saignee-verde`
- `tenis-on-running-loewe-lightspray-cloudmonster-branco`

## Recommended DEV scope for the next round

Conservative breadth round:

1. Expand `top30-adidas-sambae-regular` with Hello Kitty.
2. Add `top30-new-balance-2002r-protection-pack` micro-group.
3. Add `top30-asics-gel-nyc-regular-special` micro-group.

Optional if Lucas accepts mixed regular/Loewe:

4. Add `top30-on-running-cloudtilt-regular-loewe`.

## Risk

- DEV write would touch only `snippets/lk-variante-top30-visited-v2.liquid` in unpublished theme `155065450718`.
- Micro-groups can look sparse because 2-product groups render only 1 alternative.
- Cloudtilt has a premium/collab price jump and should not be slipped into the batch without explicit acceptance.
- Existing Curadoria groups and CSS light typography must be preserved.

## QA plan if DEV approved

1. Backup DEV asset before write.
2. Apply a scoped patch only to `snippets/lk-variante-top30-visited-v2.liquid`.
3. Read back DEV asset until expected markers/handles appear exactly once.
4. Static QA:
   - handles/labels/images/titles aligned;
   - duplicate handles: 0;
   - malformed image URLs: 0;
   - current product excluded from rendered cards;
   - existing markers preserved.
5. Public DEV preview QA on at least one PDP per touched group.
6. Typography QA:
   - `.lk-variante__title` font-weight 300;
   - `.lk-variante__label` font-weight 300;
   - `.lk-variante__label::after` font-weight 300 or `content: none`.
7. Record receipt in Brain.

## Rollback plan

Restore the pre-write DEV backup of `snippets/lk-variante-top30-visited-v2.liquid`.

## Requested approval options

- Conservative DEV: `Aprovo DEV Curadoria Sambae Hello Kitty + NB 2002R + ASICS Gel-NYC`
- Full breadth DEV including Cloudtilt mixed: `Aprovo DEV Curadoria Sambae + NB 2002R + ASICS Gel-NYC + Cloudtilt mixed`

No Production action is included. Production would require a separate GitHub PR/review → merge para Production → Shopify readback/QA approval.
