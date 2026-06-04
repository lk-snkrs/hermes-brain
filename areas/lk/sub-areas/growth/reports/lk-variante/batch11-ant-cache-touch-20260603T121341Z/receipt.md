# Batch 11 anti-cache touch receipt

- Timestamp UTC: `20260603T121341Z`
- Approval: Lucas `Seguir aprovado`.
- Assets touched with no logic change:
  - `snippets/lk-variante-top30-visited.liquid`
  - `sections/lk-pdp.liquid`

## Readback
- `snippets/lk-variante-top30-visited.liquid`: before `13133993edf5` after `089cc730d730` matches expected `True` marker `True`
- `sections/lk-pdp.liquid`: before `f2f11b1df561` after `a273d8d03729` matches expected `True` marker `True`

## Live QA
- Rounds: `3`
- Bad count: `21`

## Bad
- round 1 `tenis-onitsuka-tiger-mexico-66-white-blue-branco` ok=False sections=[]
- round 1 `tenis-onitsuka-tiger-mexico-66-black-and-white-preto` ok=False sections=[]
- round 1 `tenis-onitsuka-tiger-mexico-66-birch-rust-orange-bege` ok=False sections=[]
- round 1 `tenis-onitsuka-tiger-mexico-66-sd-cream-peacoat-navy-red-bege` ok=False sections=[]
- round 1 `tenis-onitsuka-tiger-mexico-66-sd-licorice-brown-champagne-marrom` ok=False sections=[]
- round 1 `tenis-new-balance-9060-sea-salt-concrete-branco` ok=False sections=[]
- round 1 `tenis-new-balance-9060-rose-sugar-ice-wine-rosa` ok=False sections=[]
- round 2 `tenis-onitsuka-tiger-mexico-66-white-blue-branco` ok=False sections=[]
- round 2 `tenis-onitsuka-tiger-mexico-66-black-and-white-preto` ok=False sections=[]
- round 2 `tenis-onitsuka-tiger-mexico-66-birch-rust-orange-bege` ok=False sections=[]
- round 2 `tenis-onitsuka-tiger-mexico-66-sd-cream-peacoat-navy-red-bege` ok=False sections=[]
- round 2 `tenis-onitsuka-tiger-mexico-66-sd-licorice-brown-champagne-marrom` ok=False sections=[]
- round 2 `tenis-new-balance-9060-sea-salt-concrete-branco` ok=False sections=[]
- round 2 `tenis-new-balance-9060-rose-sugar-ice-wine-rosa` ok=False sections=[]
- round 3 `tenis-onitsuka-tiger-mexico-66-white-blue-branco` ok=False sections=[]
- round 3 `tenis-onitsuka-tiger-mexico-66-black-and-white-preto` ok=False sections=[]
- round 3 `tenis-onitsuka-tiger-mexico-66-birch-rust-orange-bege` ok=False sections=[]
- round 3 `tenis-onitsuka-tiger-mexico-66-sd-cream-peacoat-navy-red-bege` ok=False sections=[]
- round 3 `tenis-onitsuka-tiger-mexico-66-sd-licorice-brown-champagne-marrom` ok=False sections=[]
- round 3 `tenis-new-balance-9060-sea-salt-concrete-branco` ok=False sections=[]

## Rollback
- Reupload `.before` files for snippet and section.