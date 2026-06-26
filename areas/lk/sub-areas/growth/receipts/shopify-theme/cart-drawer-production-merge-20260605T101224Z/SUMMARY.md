# LK Cart Drawer — Production merge receipt — 2026-06-05

## Escopo aprovado

Lucas aprovou merge do cart drawer validado em Dev para Production.

## Temas verificados antes do write

- Dev: `lk-new-theme/dev` / `155065450718` / role `unpublished`
- Production: `lk-new-theme/production` / `155065417950` / role `main`

Production foi verificado como `role=main` imediatamente antes do write.

## Assets alterados em Production

- `snippets/lk-cart-drawer.liquid`
- `layout/theme.liquid`

## Readback

- Snippet before SHA: `74d5295e0fd6f8ed9b8d3b230483a1e235f7fdd14acc63f76e167937fbc1139b`
- Snippet readback SHA: `7f747d409ebe5d93b7fe256b4fa7e7f163333eeb86d510401d912ead30ca8db3`
- Snippet readback OK: `True`
- Layout before SHA: `2ceceee359e11694e79c2c60c14cfb0173a6dabee2e21c6499357b14ec817db8`
- Layout readback SHA: `b084c5b1c83c30fed3af1692f941dacc0c20300b913c3d5f3e644466869a29ee`
- Layout readback OK: `True`
- Layout tinha render antes: `False`
- Layout tem render depois: `True`

## QA público

Observação: primeira tentativa pública logo após upload pegou edge/cache antigo sem drawer. Repetição com cache-buster confirmou o source renderizado.

QA CDP mobile live final:

- Drawer presente no DOM: `True`
- Código de modelo presente: `True`
- Drawer abriu: `True`
- Título upsell: `Mais vendidos do modelo`
- Produto atual excluído dos upsells: `True`

Upsells renderizados:
- `tenis-new-balance-530-silver-white-branco` — Tênis New Balance 530 Silver White Branco
- `tenis-new-balance-530-arid-stone-cinza` — Tênis New Balance 530 Arid Stone Cinza
- `tenis-new-balance-530-brown-tan-marrom` — Tênis New Balance 530 Brown Tan Marrom
- `tenis-new-balance-530-turtledove-mushroom-mesh-casual` — Tênis New Balance 530 Turtledove Mushroom Mesh Bege

Spot checks HTTP:
- `https://www.lksneakers.com.br/products/new-balance-530-white-natural-indigo-1?lkqa=prod-final-1780654476` — status `200`, drawer `True`, model logic `True`, title `True`
- `https://www.lksneakers.com.br/cart?lkqa=prod-final-1780654476` — status `200`, drawer `True`, model logic `True`, title `True`

## Artifacts

- Receipt dir: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-theme/cart-drawer-production-merge-20260605T101224Z`
- Screenshot live final: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-theme/cart-drawer-production-merge-20260605T101224Z/cart-drawer-production-mobile-r2.png`
- QA JSON final: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-theme/cart-drawer-production-merge-20260605T101224Z/cdp-production-check-r2.json`

## Rollback

Restaurar em Production:

- `prod-snippet-before.liquid`
- `prod-layout-before.liquid`

Esses backups estão neste receipt dir.
