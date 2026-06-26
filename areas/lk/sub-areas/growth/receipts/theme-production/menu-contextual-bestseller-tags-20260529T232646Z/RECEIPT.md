# LK menu contextual best-seller tag sync

Generated: 20260529T232646Z

## Scope
- Source: public storefront collection links present on the homepage/menu/discovery surface at run time.
- Write: add `best-seller--<collection_handle>` only to products that already had `best-seller`, `bestseller`, or another `best-seller--*` tag.
- No price, stock, discount, campaign, or customer-facing send changes.

## Results
- Menu/discovery collection handles found: `83`
- Collections with tag updates: `28`
- Product tag additions planned: `471`
- Product tag additions applied: `471`
- Errors: `0`
- Readback missing after: `0`

## Changed collections
- `sale` — 77 products — `best-seller--sale`
- `sneakers` — 69 products — `best-seller--sneakers`
- `onitsuka-tiger-todos-os-modelos` — 9 products — `best-seller--onitsuka-tiger-todos-os-modelos`
- `onitsuka-tiger-mexico-66` — 1 products — `best-seller--onitsuka-tiger-mexico-66`
- `new-balance-todos-os-modelos` — 7 products — `best-seller--new-balance-todos-os-modelos`
- `new-balance-9060` — 1 products — `best-seller--new-balance-9060`
- `new-balance-204l` — 5 products — `best-seller--new-balance-204l`
- `adidas-todos-os-modelos` — 8 products — `best-seller--adidas-todos-os-modelos`
- `samba` — 3 products — `best-seller--samba`
- `adidas-samba-jane` — 3 products — `best-seller--adidas-samba-jane`
- `adidas-taekwondo` — 3 products — `best-seller--adidas-taekwondo`
- `air-jordan` — 8 products — `best-seller--air-jordan`
- `nike-todos-os-modelos` — 54 products — `best-seller--nike-todos-os-modelos`
- `nike-dunk` — 7 products — `best-seller--nike-dunk`
- `roupas` — 105 products — `best-seller--roupas`
- `collab-com-artistas` — 11 products — `best-seller--collab-com-artistas`
- `aphase` — 1 products — `best-seller--aphase`
- `dane-se` — 6 products — `best-seller--dane-se`
- `saint-studio` — 2 products — `best-seller--saint-studio`
- `slyce` — 1 products — `best-seller--slyce`
- `camiseta-1` — 55 products — `best-seller--camiseta-1`
- `eyewear` — 5 products — `best-seller--eyewear`
- `moletom-1` — 3 products — `best-seller--moletom-1`
- `athleisure` — 12 products — `best-seller--athleisure`
- `alo-yoga-1` — 4 products — `best-seller--alo-yoga-1`
- `collectibles` — 9 products — `best-seller--collectibles`
- `pop-mart` — 1 products — `best-seller--pop-mart`
- `yeezy` — 1 products — `best-seller--yeezy`

## Public HTML spot checks
- `sale` — HTTP 200 — badge HTML count `1`
- `sneakers` — HTTP 200 — badge HTML count `8`
- `onitsuka-tiger-todos-os-modelos` — HTTP 200 — badge HTML count `1`
- `onitsuka-tiger-mexico-66` — HTTP 200 — badge HTML count `1`
- `new-balance-todos-os-modelos` — HTTP 200 — badge HTML count `0`
- `new-balance-9060` — HTTP 200 — badge HTML count `1`
- `new-balance-204l` — HTTP 200 — badge HTML count `2`
- `adidas-todos-os-modelos` — HTTP 200 — badge HTML count `0`
- `samba` — HTTP 200 — badge HTML count `3`
- `adidas-samba-jane` — HTTP 200 — badge HTML count `0`
- `adidas-taekwondo` — HTTP 200 — badge HTML count `3`
- `air-jordan` — HTTP 200 — badge HTML count `7`
- `nike-todos-os-modelos` — HTTP 200 — badge HTML count `0`
- `nike-dunk` — HTTP 200 — badge HTML count `9`
- `roupas` — HTTP 200 — badge HTML count `12`
- `collab-com-artistas` — HTTP 200 — badge HTML count `11`
- `aphase` — HTTP 200 — badge HTML count `9`
- `dane-se` — HTTP 200 — badge HTML count `14`
- `saint-studio` — HTTP 200 — badge HTML count `5`
- `slyce` — HTTP 200 — badge HTML count `9`
- `camiseta-1` — HTTP 200 — badge HTML count `13`
- `eyewear` — HTTP 200 — badge HTML count `13`
- `moletom-1` — HTTP 200 — badge HTML count `10`
- `athleisure` — HTTP 200 — badge HTML count `8`
- `alo-yoga-1` — HTTP 200 — badge HTML count `8`

## Rollback
- Use `products-tags-before-by-menu-collection.json` to compare prior product tags and remove added exact contextual tags if needed.
- No theme asset writes were performed by this run.