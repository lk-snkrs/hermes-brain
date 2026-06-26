# Batch 11 sync active v2 receipt

- Timestamp UTC: `20260603T121654Z`
- Approval: Lucas `Seguir aprovado`.
- Root cause: `sections/lk-pdp.liquid` renders `lk-variante-top30-visited-v2`, while Batch 11 had been promoted to canonical non-v2 snippet.
- Action: synced active v2 snippet from canonical Batch 11 source.

## Readback
- Active v2 before: `1fdaff0ba3db`
- Canonical source: `089cc730d730`
- Active v2 after: `eda8d824a952`
- Matches expected: `True`

## Live QA
- Rounds: `3`
- Bad count: `13`

## Bad samples
- round 1 `tenis-onitsuka-tiger-mexico-66-white-blue-branco` sections=[]
- round 1 `tenis-onitsuka-tiger-mexico-66-birch-rust-orange-bege` sections=[]
- round 1 `tenis-onitsuka-tiger-mexico-66-sd-cream-peacoat-navy-red-bege` sections=[]
- round 1 `tenis-onitsuka-tiger-mexico-66-sd-licorice-brown-champagne-marrom` sections=[]
- round 1 `tenis-new-balance-9060-sea-salt-concrete-branco` sections=[]
- round 1 `tenis-new-balance-9060-rose-sugar-ice-wine-rosa` sections=[]
- round 2 `tenis-onitsuka-tiger-mexico-66-white-blue-branco` sections=[]
- round 2 `tenis-new-balance-9060-rose-sugar-ice-wine-rosa` sections=[]
- round 3 `tenis-onitsuka-tiger-mexico-66-white-blue-branco` sections=[]
- round 3 `tenis-onitsuka-tiger-mexico-66-birch-rust-orange-bege` sections=[]
- round 3 `tenis-onitsuka-tiger-mexico-66-sd-cream-peacoat-navy-red-bege` sections=[]
- round 3 `tenis-new-balance-9060-sea-salt-concrete-branco` sections=[]
- round 3 `tenis-new-balance-9060-rose-sugar-ice-wine-rosa` sections=[]

## Rollback
- Reupload `active-v2.before.liquid` to active v2 snippet.