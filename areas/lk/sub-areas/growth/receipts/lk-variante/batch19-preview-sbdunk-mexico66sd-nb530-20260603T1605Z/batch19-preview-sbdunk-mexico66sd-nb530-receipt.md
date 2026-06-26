# Batch 19 Preview — SB Dunk Low + Mexico 66 SD + NB 530

- timestamp UTC: `2026-06-03T16:33:53.548859+00:00`
- approval: `Lucas approved in Telegram: Aprovo (preview Batch 19 SB Dunk Low + Mexico 66 SD + NB 530)`
- preview: `156623372510` / `LK Curadoria Force Fix Preview 2026-06-03` / role `unpublished`
- live unchanged: `True`
- target/readback: `32f11bff52e4` / `32f11bff52e4`
- readback matches: `True`

## Changes
- `top30-nike-sb-dunk-low` / Nike SB Dunk Low mode `append_new_group` before `0` after `8`; added `8`
  - `tenis-nike-sb-dunk-low-pro-triple-white-branco` → Pro Triple White
  - `tenis-nike-sb-dunk-low-trocadero-gardens-marrom` → Trocadéro Gardens
  - `nike-sb-dunk-low-pro-iso-dark-russet` → Pro ISO Dark Russet
  - `nike-sb-dunk-low-pro-classic-green` → Pro Classic Green
  - `nike-sb-dunk-low-prm-paisley-brown` → PRM Paisley Brown
  - `nike-sb-dunk-low-prm-phillies` → PRM Phillies
  - `nike-sb-dunk-low-club-58-gulf` → Club 58 Gulf
  - `nike-sb-dunk-low-vx-1000-camcorder` → VX 1000 Camcorder
- `top30-mexico66-sd` / Onitsuka Mexico 66 SD mode `expand_existing_group` before `12` after `20`; added `8`
  - `tenis-onitsuka-tiger-mexico-66-sd-exposed-black-black-preto` → Exposed Black/Black
  - `tenis-onitsuka-tiger-mexico-66-sd-clay-canyon-marrom` → Exposed Clay Canyon
  - `tenis-onitsuka-tiger-mexico-66-sd-exposed-foam-jade-verde` → Exposed Foam Jade
  - `tenis-onitsuka-tiger-mexico-66-sd-exposed-foam-peacoat-azul` → Exposed Foam Peacoat
  - `tenis-onitsuka-tiger-mexico-66-sd-white-rose-gold-branco` → White/Rose Gold
  - `tenis-onitsuka-tiger-mexico-66-sd-vin-mantle-green-ivory-verde` → Vin Mantle Green Ivory
  - `tenis-onitsuka-tiger-mexico-66-sd-metallic-series-pale-mint-cream-azul-1` → Metallic Series Pale Mint Crea
  - `onitsuka-tiger-mexico-66-sd-metallic-series-jade-cream-verde` → Metallic Series Jade Cream
- `top30-nb-530` / New Balance 530 mode `expand_existing_group` before `16` after `21`; added `5`
  - `tenis-new-balance-530-white-green-matcha-verde` → White Green Matcha
  - `tenis-new-balance-530-white-chrome-blue-branco` → White Chrome Blue
  - `tenis-new-balance-530-sea-salt-white-marsh-green-branco` → Sea Salt White Marsh Green
  - `tenis-new-balance-530-white-light-crome-blue-branco` → White Light Crome Blue
  - `tenis-new-balance-530-stoneware-line-branco` → Stoneware Line

## QA estático
- arrays equal: `True`
- array lengths: `{'lk_top30_markers': 23, 'lk_top30_names': 23, 'lk_top30_handles_groups': 23, 'lk_top30_labels_groups': 23, 'lk_top30_images_groups': 23}`
- bad URL occurrences: `{'https:https://': 0, 'https://https://': 0, 'TenisMoldeLK': 0}`
- `top30-nike-sb-dunk-low`: handles `8`, labels `8`, images `8`, malformed `0`
- `top30-mexico66-sd`: handles `20`, labels `20`, images `20`, malformed `0`
- `top30-nb-530`: handles `21`, labels `21`, images `21`, malformed `0`

## Rollback
- restore preview from `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/lk-variante/batch19-preview-sbdunk-mexico66sd-nb530-20260603T1605Z/preview-before.liquid`

## Non-actions
- No live/main write
- No production merge
- No product/price/stock/app/GMC/Tiny/Klaviyo/Meta/checkout write