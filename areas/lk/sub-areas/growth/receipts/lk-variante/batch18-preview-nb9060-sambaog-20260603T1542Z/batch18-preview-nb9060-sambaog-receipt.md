# Batch 18 Preview — NB 9060 + Adidas Samba OG

- timestamp UTC: `2026-06-03T15:46:54.278493+00:00`
- approval: `Lucas approved in Telegram: Aprovo (preview Batch 18 NB 9060 + Adidas Samba OG)`
- preview: `156623372510` / `LK Curadoria Force Fix Preview 2026-06-03` / role `unpublished`
- live unchanged: `True`
- target/readback: `ae760e1e26a6` / `ae760e1e26a6`
- readback matches: `True`

## Changes
- `top30-nb-9060` / New Balance 9060 mode `expand_existing_group` before `18` after `26`; added `8`
  - `tenis-new-balance-9060-linen-blue-cinza` → Linen Blue
  - `tenis-new-balance-9060-reflection-black-suede-casual` → Reflection Black Suede
  - `tenis-new-balance-9060-camurca-mesh-cinza-slate-grey-calcium` → Mesh Slate Grey Calcium
  - `tenis-new-balance-9060-linen-burgundy-bege` → Linen Burgundy
  - `tenis-new-balance-9060-grey-day-2025-esportivo-casual` → Grey Day 2025
  - `tenis-new-balance-9060-driftwood-castlerock-marrom` → Driftwood Castlerock
  - `tenis-new-balance-9060-pearl-grey-linen-azul` → Pearl Grey Linen
  - `tenis-new-balance-9060-incense-raincloud-arid-stone-marrom` → Incense Raincloud Arid Stone
- `top30-samba-og` / Samba OG mode `expand_existing_group` before `10` after `18`; added `8`
  - `tenis-adidas-samba-og-crystal-linen-ivory-gum-branco` → adidas Samba OG Crystal Linen
  - `tenis-adidas-samba-og-off-white-earth-strata-gum-bege` → Off White Earth Strata Gum
  - `tenis-adidas-samba-og-snakeskin-collegiate-green-verde` → Snakeskin Collegiate Green
  - `tenis-adidas-samba-og-hazy-green-sky-tint-verde` → Hazy Green Sky Tint
  - `tenis-adidas-samba-og-better-scarlet-white-vermelho` → Better Scarlet White
  - `tenis-adidas-samba-og-sanda-strata-sky-tint-bege` → Sanda Strata Sky Tint
  - `tenis-adidas-samba-og-shadow-brown-powder-yellow-marrom` → Shadow Brown Powder Yellow
  - `tenis-adidas-samba-og-white-night-indigo-branco` → White Night Indigo

## QA estático
- arrays equal: `True`
- array lengths: `{'lk_top30_markers': 22, 'lk_top30_names': 22, 'lk_top30_handles_groups': 22, 'lk_top30_labels_groups': 22, 'lk_top30_images_groups': 22}`
- bad URL occurrences: `{'https:https://': 0, 'https://https://': 0, 'TenisMoldeLK': 0}`
- `top30-nb-9060`: handles `26`, labels `26`, images `26`, malformed `0`
- `top30-samba-og`: handles `18`, labels `18`, images `18`, malformed `0`

## Rollback
- restore preview from `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/lk-variante/batch18-preview-nb9060-sambaog-20260603T1542Z/preview-before.liquid`

## Non-actions
- No live/main write
- No production merge
- No product/price/stock/app/GMC/Tiny/Klaviyo/Meta/checkout write