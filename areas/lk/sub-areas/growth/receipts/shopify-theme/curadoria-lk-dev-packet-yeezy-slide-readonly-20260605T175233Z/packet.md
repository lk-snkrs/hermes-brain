# Curadoria LK PDP — DEV packet read-only — Yeezy Slide

Created UTC: 20260605T175233Z

## Scope
No Shopify write. Prepare approved DEV package only.

## Proposed marker
top30-yeezy-slide-regular

## Candidates
- `tenis-adidas-yeezy-slide-slate-marine-azul-escuro` — Slate Marine — image_ok=True — public=200 — status=active
- `yeezy-slide-azure` — Azure — image_ok=True — public=200 — status=active
- `yeezy-slide-bone-937693978` — Bone — image_ok=True — public=200 — status=active
- `yeezy-slide-glow-green` — Glow Green — image_ok=True — public=200 — status=active
- `yeezy-slide-ochre-925686464` — Ochre — image_ok=True — public=200 — status=active
- `yeezy-slide-onyx` — Onyx — image_ok=True — public=200 — status=active
- `yeezy-slide-pure-2022` — Pure — image_ok=True — public=200 — status=active

## Test products
- `tenis-adidas-yeezy-slide-slate-marine-azul-escuro`
- `yeezy-slide-azure`

## QA plan
- Asset API readback on DEV snippet
- Static check: marker present once, 7 handles, 7 labels, 7 images, no malformed URLs
- Preview/public QA with preview_theme_id=155065450718 for Slate Marine and Azure
- Verify Curadoria LK and Outras variações present
- Verify current product excluded
- Verify 5 cards render with images and font-weight 400
- No product/price/stock/app writes