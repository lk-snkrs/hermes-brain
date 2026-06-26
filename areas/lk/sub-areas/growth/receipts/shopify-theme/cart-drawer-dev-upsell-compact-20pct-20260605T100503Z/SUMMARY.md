# LK Cart Drawer — upsell compact 20% DEV — 2026-06-05

## Feedback Lucas

Diminuir em 20% o bloco `Mais vendidos do modelo`, que estava visualmente grande no drawer.

## Mudança aplicada

Asset Shopify alterado somente em Dev/unpublished:

- Theme: `lk-new-theme/dev`
- Theme ID: `155065450718`
- Asset: `snippets/lk-cart-drawer.liquid`

Ajustes visuais do bloco de upsell:

- card: `120px → 96px`
- imagem: `120px → 96px`
- padding interno: `16px 24px → 13px 19px`
- gap: `12px → 10px`
- título: `9px → 8px`
- nome: `11px → 10px`
- preço: `14px → 12px`
- botão: `9px → 8px`, padding `6px 14px → 5px 11px`

A lógica de best sellers do modelo foi preservada.

## Readback

- Dev before SHA: `aa185c16d14b7ffeb288991fdcc4ce935b27f7a5f7dba88b099cef4f21b33d47`
- Dev readback SHA: `7f747d409ebe5d93b7fe256b4fa7e7f163333eeb86d510401d912ead30ca8db3`
- Readback OK: `True`
- Production unchanged: `True`

## QA browser mobile

- Produto no carrinho: `new-balance-530-white-natural-indigo-1`
- Drawer abriu: `True`
- Título: `Mais vendidos do modelo`
- Sugestões seguem o mesmo modelo:
- `tenis-new-balance-530-silver-white-branco` — Tênis New Balance 530 Silver White Branco
- `tenis-new-balance-530-arid-stone-cinza` — Tênis New Balance 530 Arid Stone Cinza
- `tenis-new-balance-530-brown-tan-marrom` — Tênis New Balance 530 Brown Tan Marrom
- `tenis-new-balance-530-turtledove-mushroom-mesh-casual` — Tênis New Balance 530 Turtledove Mushroom Mesh Bege

## Artifacts

- Receipt dir: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-theme/cart-drawer-dev-upsell-compact-20pct-20260605T100503Z`
- Screenshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-theme/cart-drawer-dev-upsell-compact-20pct-20260605T100503Z/cart-drawer-upsell-compact-20pct-mobile.png`
- QA JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-theme/cart-drawer-dev-upsell-compact-20pct-20260605T100503Z/cdp-upsell-compact-20pct-check.json`

## Rollback

Restaurar `dev-snippet-before.liquid` deste receipt no tema Dev.
Production não requer rollback porque não foi alterada.
