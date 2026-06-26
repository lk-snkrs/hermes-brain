# LK Curadoria PDP — Batch 10 Dev apply receipt

- Timestamp UTC: 2026-06-02T19:38:23.659004+00:00
- Asset: `snippets/lk-variante-top30-visited.liquid`
- Dev theme: `155065450718` / `lk-new-theme/dev` / role `unpublished`
- Production theme: `155065417950` / role `main`

## Resultado

- Dev before SHA: `0b530160154a`
- Dev readback SHA: `e6f3323a13c7`
- Readback matches candidate: `True`
- Production unchanged: `True` (`0b530160154a` → `0b530160154a`)
- QA static/readback pass: `True`

## Grupos adicionados no Dev

### `top30-air-jordan-1-low-regular`
- Items: 10
- Marker readback: True / count 1
- Handles:
  - `air-jordan-1-low-vintage-grey`
  - `tenis-air-jordan-1-low-se-legend-coffee-marrom`
  - `tenis-air-jordan-1-low-jade-smoke-multicolor`
  - `tenis-air-jordan-1-low-midnight-navy-wolf-grey-azul-marinho`
  - `air-jordan-1-low-palomino`
  - `air-jordan-1-low-royal-toe`
  - `air-jordan-1-low-black-medium-grey`
  - `air-jordan-1-low-guava-ice`
  - `air-jordan-1-low-gym-red-black`
  - `air-jordan-1-low-inside-out-black`

### `top30-air-jordan-1-low-og-regular`
- Items: 10
- Marker readback: True / count 1
- Handles:
  - `tenis-air-jordan-1-low-og-obsidian-unc-azul`
  - `tenis-air-jordan-1-low-og-mocha-marrom`
  - `tenis-nike-air-jordan-1-low-og-olive-verde`
  - `tenis-air-jordan-1-low-og-rookie-of-year-marrom`
  - `tenis-air-jordan-1-low-og-year-of-snake-2025-cinza`
  - `tenis-air-jordan-1-low-og-year-of-dragon-chinese-new-year-verde`
  - `tenis-air-jordan-1-low-og-metallic-silver-cinza`
  - `tenis-air-jordan-1-low-og-barrons-cinza`
  - `air-jordan-1-low-og-unc`
  - `tenis-air-jordan-1-low-og-oxidized-white-green-branco`

### `top30-adidas-sambae-regular`
- Items: 10
- Marker readback: True / count 1
- Handles:
  - `tenis-adidas-sambae-linen-gum-bege`
  - `tenis-adidas-sambae-x-kseniaschnaiderc-black-multicolor-colorido`
  - `tenis-adidas-sambae-denim-azul`
  - `tenis-adidas-sambae-core-black-metallic-gold-preto`
  - `tenis-adidas-sambae-cloud-white-silver-metallic-gold-branco`
  - `tenis-adidas-sambae-cloud-white-collegiate-green-branco`
  - `tenis-adidas-sambae-cloud-white-branco`
  - `tenis-adidas-sambae-cloud-white-better-scarlet-branco`
  - `adidas-sambae-black-white-gum`
  - `tenis-adidas-sambae-white-green-gum-branco`

## QA público preview

- Preview público não autenticado removeu `preview_theme_id`; portanto marker no HTML público não é autoritativo para Dev.
- Sem Liquid error nas amostras públicas: `True`

## Rollback

- Reverter Dev aplicando backup: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/batch10-readonly-20260602T192139Z/dev-apply-revised/dev-before.liquid` ao asset `snippets/lk-variante-top30-visited.liquid` no theme `155065450718`.
- Production rollback não necessário: Production permaneceu intocada.

## Não ações

- Não alterei Production.
- Não alterei produtos, preços, estoque, apps, GMC, Klaviyo, Meta, Tiny ou checkout.