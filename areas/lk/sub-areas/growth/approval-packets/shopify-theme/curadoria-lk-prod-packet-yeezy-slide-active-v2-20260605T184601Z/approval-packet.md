# Approval packet — Curadoria LK PDP Yeezy Slide Production

- timestamp UTC: `2026-06-05T18:46:03.997164+00:00`
- status: read-only packet; **no Production write executed**
- DEV source: `155065450718` / `lk-new-theme/dev` / role `unpublished`
- Production target: `155065417950` / `lk-new-theme/production` / role `main`
- asset: `snippets/lk-variante-top30-visited-v2.liquid`
- active render DEV/Production: `True` / `True`

## Scope proposed
- merge mode: `append-new-marker`
- production before SHA12: `01af5cea362d`
- proposed after SHA12: `493429e95ac5`
- existing Production markers preserved/order: `True`
- marker count before/after: `26` / `27`

## Grupo
- `tenis-adidas-yeezy-slide-slate-marine-azul-escuro` → Slate Marine — `https://cdn.shopify.com/s/files/1/0621/8969/9294/files/tenis-adidas-yeezy-slide-slate-marine-azul-escuro-lk-sneakers-937161.jpg?v=1717500027`
- `yeezy-slide-azure` → Azure — `https://cdn.shopify.com/s/files/1/0621/8969/9294/products/tenis-yeezy-slide-azure-azul-262524.jpg?v=1710449811`
- `yeezy-slide-bone-937693978` → Bone — `https://cdn.shopify.com/s/files/1/0621/8969/9294/products/tenis-yeezy-slide-bone-branco-185148.webp?v=1710449811`
- `yeezy-slide-glow-green` → Glow Green — `https://cdn.shopify.com/s/files/1/0621/8969/9294/products/tenis-yeezy-slide-glow-green-verde-513437.webp?v=1710449810`
- `yeezy-slide-ochre-925686464` → Ochre — `https://cdn.shopify.com/s/files/1/0621/8969/9294/products/tenis-yeezy-slide-ochre-marrom-211761.webp?v=1710449812`
- `yeezy-slide-onyx` → Onyx — `https://cdn.shopify.com/s/files/1/0621/8969/9294/products/tenis-yeezy-slide-onyx-preto-317608.webp?v=1710449811`
- `yeezy-slide-pure-2022` → Pure — `https://cdn.shopify.com/s/files/1/0621/8969/9294/products/tenis-yeezy-slide-pure-2022-bege-380649.jpg?v=1710449811`

## Proposed static QA
- arrays equal: `True`
- marker count: `1`
- group index: `26`
- handles/labels/images: `7` / `7` / `7`
- handles match: `True`
- labels match: `True`
- images match: `True`
- images valid: `True`
- bad URL occurrences: `{'https:https://': 0, 'https://https://': 0, 'TenisMoldeLK': 0}`

## Public preflight
- product URLs OK: `True`
- image URLs OK: `True`

## QA plan after approval/write
- Read back Production asset and confirm proposed SHA / marker count.
- Static QA arrays, handles, labels, images and current-product exclusion simulation.
- Public PDP QA on at least `slate-marine` and `azure`, then multi-round cache-busted checks for edge propagation.
- Verify Production only; Dev already validated and no app/product/stock changes.

## Rollback
- Backup live asset first as live-before.liquid in the execution receipt; rollback restores that exact backup to Production/main after explicit approval if needed.

## Approval required
- To proceed, Lucas must explicitly approve the Production theme write with this exact scope.

## Non-actions
- No write executed while preparing this packet
- No Dev write
- No product/price/stock/app/GMC/Tiny/Klaviyo/Meta/checkout/discount/fulfillment write