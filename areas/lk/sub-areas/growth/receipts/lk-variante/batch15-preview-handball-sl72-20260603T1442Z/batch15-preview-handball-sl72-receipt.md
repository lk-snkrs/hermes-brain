# Batch 15 Preview — Handball Spezial + SL 72

- timestamp UTC: `2026-06-03T14:15:54.467352+00:00`
- preview: `156623372510` / `LK Curadoria Force Fix Preview 2026-06-03` / role `unpublished`
- live unchanged: `True`
- preview before/target/readback: `6fe202381a4f` / `45fb1292baf1` / `45fb1292baf1`
- readback matches: `True`

## Changes
- `top30-adidas-handball-spezial` final count `13`; added `5`
  - `tenis-adidas-handball-spezial-preloved-brown-orange-tint-gum-marrom` → Preloved Brown Orange
  - `tenis-adidas-handball-spezial-sand-strata-clear-sky-bege` → Sand Strata Clear Sky
  - `tenis-adidas-handball-spezial-lucid-pink-almost-yellow-rosa` → Lucid Pink Yellow
  - `tenis-adidas-handball-spezial-spark-lucid-pink-amarelo` → Spark Lucid Pink
  - `tenis-adidas-handball-spezial-preloved-green-verde` → Preloved Green
- `top30-sl72-og` final count `16`; added `6`
  - `tenis-adidas-sl-72-og-clear-sky-sand-strata-cream-white-azul` → OG Clear Sky
  - `tenis-adidas-sl-72-rs-aurora-ivy-off-white-verde` → RS Aurora Ivy
  - `tenis-adidas-sl-72-rs-earth-strata-warm-vanilla-marrom` → RS Earth Strata
  - `tenis-adidas-sl-72-og-bright-royal-pink-spark-azul` → OG Bright Royal
  - `tenis-adidas-sl72-rs-cloud-white-core-black-spark-branco` → RS Cloud White Black
  - `tenis-adidas-sl-72-og-silver-metallic-black-prata` → OG Silver Metallic

## QA estático
- arrays equal: `True`
- `top30-adidas-handball-spezial`: handles `13`, labels `13`, images `13`, malformed `0`
- `top30-sl72-og`: handles `16`, labels `16`, images `16`, malformed `0`

## Rollback
- restore preview from `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/lk-variante/batch15-preview-handball-sl72-20260603T1442Z/preview-before.liquid`