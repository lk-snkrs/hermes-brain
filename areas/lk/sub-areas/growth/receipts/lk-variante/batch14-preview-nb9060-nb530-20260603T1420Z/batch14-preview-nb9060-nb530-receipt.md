# Batch 14 Preview — NB 9060 + NB 530

- timestamp UTC: `2026-06-03T14:01:51.255607+00:00`
- preview: `156623372510` / `LK Curadoria Force Fix Preview 2026-06-03` / role `unpublished`
- live unchanged: `True`
- preview before/target/readback: `6c887b0cebc0` / `6fe202381a4f` / `6fe202381a4f`
- readback matches: `True`

## Changes
- `top30-nb-9060` final count `18`; added `7`
  - `tenis-new-balance-9060-magnet-cinza` → Magnet Cinza
  - `tenis-new-balance-9060-quartz-grey-cinza` → Quartz Grey Cinza
  - `tenis-new-balance-9060-slate-grey-raincloud-cinza` → Slate Grey Raincloud Cinza
  - `tenis-new-balance-9060-earth-shadow-flat-taupe-marrom` → Earth Shadow Taupe
  - `tenis-new-balance-9060-garter-snake-pearl-grey-verde` → Garter Snake
  - `tenis-new-balance-9060-bisque-frosted-glass-bege` → Bisque Frosted Glass
  - `tenis-new-balance-9060-black-castlerock-preto` → Black Castlerock Preto
- `top30-nb-530` final count `16`; added `6`
  - `tenis-new-balance-530-brown-tan-marrom` → Brown Tan Marrom
  - `tenis-new-balance-530-silver-metallic-black-cement-prateado` → Silver Black Cement
  - `tenis-new-balance-530-white-pearl-grey-branco` → White Pearl Grey Branco
  - `tenis-new-balance-530-grey-matter-silver-metallic-cinza` → Grey Matter Silver
  - `tenis-new-balance-530-sea-salt-white-mercury-rede-branco` → Sea Salt Mercury Red
  - `tenis-new-balance-530-silver-black-cinza` → Silver Black Cinza

## QA estático
- arrays equal: `True`
- `top30-nb-9060`: handles `18`, labels `18`, images `18`, malformed `0`
- `top30-nb-530`: handles `16`, labels `16`, images `16`, malformed `0`

## Rollback
- restore preview from `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/lk-variante/batch14-preview-nb9060-nb530-20260603T1420Z/preview-before.liquid`