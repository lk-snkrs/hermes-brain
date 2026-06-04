# Batch 11 Curadoria LK — Production promotion receipt

- Timestamp UTC: `20260603T114859Z`
- Approval: Lucas respondeu `Aprovo` após o pacote de promoção Production.
- Scope: somente `snippets/lk-variante-top30-visited.liquid` no theme Production.
- Não alterado: produtos, preço, estoque, apps, checkout, GMC, Klaviyo, campanhas.

## Themes
- Dev: `{'id': 155065450718, 'name': 'lk-new-theme/dev', 'role': 'unpublished'}`
- Production: `{'id': 155065417950, 'name': 'lk-new-theme/production', 'role': 'main'}`

## Readback
- Production before SHA12: `6e36b5761ff3`
- Dev promoted SHA12: `13133993edf5`
- Production after SHA12: `13133993edf5`
- Production matches Dev promoted: `True`
- Already present before/idempotent handles: `['tenis-onitsuka-tiger-mexico-66-white-blue-branco', 'tenis-onitsuka-tiger-mexico-66-black-and-white-preto', 'tenis-new-balance-9060-sea-salt-concrete-branco']`
- Newly present after promotion: `['tenis-onitsuka-tiger-mexico-66-birch-rust-orange-bege', 'tenis-onitsuka-tiger-mexico-66-sd-cream-peacoat-navy-red-bege', 'tenis-onitsuka-tiger-mexico-66-sd-licorice-brown-champagne-marrom', 'tenis-new-balance-9060-rose-sugar-ice-wine-rosa']`

## Handles promoted
- `tenis-onitsuka-tiger-mexico-66-white-blue-branco` — White Blue
- `tenis-onitsuka-tiger-mexico-66-black-and-white-preto` — Black White
- `tenis-onitsuka-tiger-mexico-66-birch-rust-orange-bege` — Birch Rust
- `tenis-onitsuka-tiger-mexico-66-sd-cream-peacoat-navy-red-bege` — Cream Peacoat
- `tenis-onitsuka-tiger-mexico-66-sd-licorice-brown-champagne-marrom` — Licorice Champagne
- `tenis-new-balance-9060-sea-salt-concrete-branco` — Sea Salt Concrete
- `tenis-new-balance-9060-rose-sugar-ice-wine-rosa` — Rose Sugar

## QA
- Static errors: `[]`
- Public `.js` all OK: `True`
- Public `.js` all available: `True`
- Live bad status/Liquid error count across 3 rounds: `0`
- Live section anomaly count: `0`

## Links for review
- [tenis-onitsuka-tiger-mexico-66-white-blue-branco](https://www.lksneakers.com.br/products/tenis-onitsuka-tiger-mexico-66-white-blue-branco)
- [tenis-onitsuka-tiger-mexico-66-black-and-white-preto](https://www.lksneakers.com.br/products/tenis-onitsuka-tiger-mexico-66-black-and-white-preto)
- [tenis-onitsuka-tiger-mexico-66-birch-rust-orange-bege](https://www.lksneakers.com.br/products/tenis-onitsuka-tiger-mexico-66-birch-rust-orange-bege)
- [tenis-onitsuka-tiger-mexico-66-sd-cream-peacoat-navy-red-bege](https://www.lksneakers.com.br/products/tenis-onitsuka-tiger-mexico-66-sd-cream-peacoat-navy-red-bege)
- [tenis-onitsuka-tiger-mexico-66-sd-licorice-brown-champagne-marrom](https://www.lksneakers.com.br/products/tenis-onitsuka-tiger-mexico-66-sd-licorice-brown-champagne-marrom)
- [tenis-new-balance-9060-sea-salt-concrete-branco](https://www.lksneakers.com.br/products/tenis-new-balance-9060-sea-salt-concrete-branco)
- [tenis-new-balance-9060-rose-sugar-ice-wine-rosa](https://www.lksneakers.com.br/products/tenis-new-balance-9060-rose-sugar-ice-wine-rosa)

## Rollback
- Reupload `production-before.liquid` from this folder to Production asset `snippets/lk-variante-top30-visited.liquid`, then readback and live QA.