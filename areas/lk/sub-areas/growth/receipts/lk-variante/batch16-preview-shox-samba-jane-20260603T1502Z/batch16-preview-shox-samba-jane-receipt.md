# Batch 16 Preview — Shox TL + Samba Jane

- timestamp UTC: `2026-06-03T14:41:07.689726+00:00`
- preview: `156623372510` / `LK Curadoria Force Fix Preview 2026-06-03` / role `unpublished`
- live unchanged: `True`
- preview before/target/readback: `96ae61c1fdb0` / `e7ed4390565a` / `e7ed4390565a`
- readback matches: `True`

## Changes
- `top30-nike-shox-tl` mode `append_new_group` final count `7`; added `7`
  - `tenis-nike-shox-tl-orewood-brown-cave-stone-bege` → Orewood Brown Cave Stone
  - `tenis-nike-shox-tl-pumice-night-maroon-cinza` → Pumice Night Maroon
  - `tenis-nike-shox-tl-blue-tint-orange-azul` → Blue Tint Orange
  - `tenis-nike-shox-tl-velvet-brown-denim-turquoise-marrom` → Velvet Brown Turquoise
  - `tenis-nike-shox-tl-sunrise-gradient-laranja` → Sunrise Gradient
  - `tenis-nike-shox-tl-black-cave-stone-preto` → Black Cave Stone
  - `tenis-nike-shox-tl-black-dynamic-yellow-preto` → Black Dynamic Yellow
- `top30-adidas-samba-jane` mode `append_new_group` final count `7`; added `7`
  - `tenis-adidas-samba-jane-chalk-white-wonder-quartz-branco` → Chalk White Quartz
  - `tenis-adidas-samba-jane-cream-black-gum-bege` → Cream Black Gum
  - `tenis-adidas-samba-jane-white-blue-gum-branco` → White Blue Gum
  - `tenis-adidas-samba-jane-green-white-gum-verde` → Green White Gum
  - `tenis-adidas-samba-jane-black-white-gum-preto` → Black White Gum
  - `tenis-adidas-samba-jane-white-black-branco` → White Black
  - `tenis-adidas-samba-jane-scarlet-gum-vermelho` → Scarlet Gum

## QA estático
- arrays equal: `True`
- `top30-nike-shox-tl`: handles `7`, labels `7`, images `7`, malformed `0`
- `top30-adidas-samba-jane`: handles `7`, labels `7`, images `7`, malformed `0`

## Rollback
- restore preview from `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/lk-variante/batch16-preview-shox-samba-jane-20260603T1502Z/preview-before.liquid`