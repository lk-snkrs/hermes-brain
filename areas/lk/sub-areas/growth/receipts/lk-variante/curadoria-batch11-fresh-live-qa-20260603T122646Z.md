# Curadoria LK Batch 11 — fresh public live QA

Timestamp UTC: 2026-06-03T12:26:46Z

Domain: `lksneakers.com.br`

Rounds: `3`

Bad count by round: `[7, 6, 3]`

All clean: `false`


## Sample

- `tenis-onitsuka-tiger-mexico-66-white-blue-branco` (new, expected `top30-mexico66-regular`): ['BAD', 'BAD', 'BAD']; last marker `None`, items `0`, images `0`, labels `[]`
- `tenis-onitsuka-tiger-mexico-66-black-and-white-preto` (new, expected `top30-mexico66-regular`): ['BAD', 'OK', 'OK']; last marker `top30-mexico66-regular`, items `5`, images `5`, labels `['Kill Bill', 'White Black', 'Beige Grass', 'Birch Peacoat', 'Paraty Birch']`
- `tenis-onitsuka-tiger-mexico-66-birch-rust-orange-bege` (new, expected `top30-mexico66-regular`): ['BAD', 'BAD', 'BAD']; last marker `None`, items `0`, images `0`, labels `[]`
- `tenis-onitsuka-tiger-mexico-66-sd-cream-peacoat-navy-red-bege` (new, expected `top30-mexico66-sd`): ['BAD', 'BAD', 'OK']; last marker `top30-mexico66-sd`, items `5`, images `5`, labels `['Beige Beet', 'Kill Bill', 'Cream Birch', 'Clay Canyon', 'Birch Metro']`
- `tenis-onitsuka-tiger-mexico-66-sd-licorice-brown-champagne-marrom` (new, expected `top30-mexico66-sd`): ['BAD', 'BAD', 'OK']; last marker `top30-mexico66-sd`, items `5`, images `5`, labels `['Beige Beet', 'Kill Bill', 'Cream Birch', 'Clay Canyon', 'Birch Metro']`
- `tenis-new-balance-9060-sea-salt-concrete-branco` (new, expected `top30-nb-9060`): ['BAD', 'BAD', 'OK']; last marker `top30-nb-9060`, items `5`, images `5`, labels `['Mushroom', 'Rich Oak', 'Angora', 'Sea Salt', 'Bisque']`
- `tenis-new-balance-9060-rose-sugar-ice-wine-rosa` (new, expected `top30-nb-9060`): ['BAD', 'BAD', 'BAD']; last marker `None`, items `0`, images `0`, labels `[]`
- `new-balance-530-white-natural-indigo-1` (control, expected `top30-nb-530`): ['OK', 'OK', 'OK']; last marker `top30-nb-530`, items `5`, images `5`, labels `['Turtledove', 'Silver Cream', 'Silver White', 'Steel Grey', 'Silver Blue']`
- `tenis-onitsuka-tiger-mexico-66-kill-bill-amarelo` (control, expected `top30-mexico66-regular`): ['OK', 'OK', 'OK']; last marker `top30-mexico66-regular`, items `5`, images `5`, labels `['White Black', 'Beige Grass', 'Birch Peacoat', 'Paraty Birch', 'Chrome Silver']`
- `tenis-new-balance-9060-bisque-sea-salt-bege` (control, expected `top30-nb-9060`): ['OK', 'OK', 'OK']; last marker `top30-nb-9060`, items `5`, images `5`, labels `['Mushroom', 'Rich Oak', 'Angora', 'Sea Salt', 'Triple White']`

## Non-actions

- no Shopify write
- no product/price/stock/app/GMC/Tiny/Klaviyo/Meta/checkout write
- public storefront GET only
