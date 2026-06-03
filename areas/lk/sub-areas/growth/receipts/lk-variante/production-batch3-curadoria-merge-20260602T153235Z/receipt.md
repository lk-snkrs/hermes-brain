# Curadoria LK Batch 3 — Production promotion receipt

Timestamp UTC: 2026-06-02T15:32:50.702268+00:00

## Approval
Lucas asked to publish to Production via merge after Dev QA and image fixes.

## Themes
- Dev: lk-new-theme/dev / 155065450718 / unpublished
- Production: lk-new-theme/production / 155065417950 / main

## Assets promoted
- `snippets/lk-variante-top30-visited.liquid`: write_needed=True, readback_matches_dev=True, cdn_bad_checks=0
- `sections/lk-pdp.liquid`: write_needed=True, readback_matches_dev=True, cdn_bad_checks=0

## Rollback
Rollback is re-uploading the `.production.before` files in this directory to the same Production asset keys.

## Non-actions
No product, price, stock, checkout, app, GMC/feed, Klaviyo, Meta, Tiny, campaign or customer-facing send changes.


## Live QA
- Gazelle `tenis-adidas-gazelle-indoor-maroon-almost-yellow-marrom`: pass=False, sections=0, items=0, images=0, liquid_errors=0
- Air Jordan 4 `tenis-air-jordan-4-retro-metallic-gold-branco`: pass=False, sections=1, items=5, images=15, liquid_errors=0
- Taekwondo Mei `adidas-taekwondo-mei-ballet-branco-e-preto`: pass=False, sections=1, items=5, images=15, liquid_errors=0
- Handball Spezial `tenis-adidas-handball-spezial-earth-strata-gum-marrom`: pass=False, sections=1, items=5, images=15, liquid_errors=0
- Lululemon `jaqueta-lululemon-define-nulu`: pass=False, sections=1, items=5, images=12, liquid_errors=3

All pass: False


## Live QA retry / edge cache
{"eventual_all_pass": false, "last_all_pass": false}


## Support snippets for edge-cache stale renders
- `snippets/lk-variante-samba-jane.liquid`: existed_before=True, write_needed=False, readback_matches_dev=True
- `snippets/lk-variante-air-jordan-1-low.liquid`: existed_before=True, write_needed=False, readback_matches_dev=True
- `snippets/lk-variante-air-jordan-1-low-travis.liquid`: existed_before=True, write_needed=False, readback_matches_dev=True


## Production section retouch for edge cache
{"readback_same": true, "lululemon_liquid_errors": [3, 3, 3, 3, 3]}


## GitHub PR / merge
- Branch: `hermes/curadoria-lk-batch3-production-20260602`
- PR: https://github.com/lk-snkrs/lk-new-theme/pull/18
- Merged: `False`
- Head SHA: `6aebd79777965f9c9664e72836657811835538c1`


## GitHub PR / merge final
- PR: https://github.com/lk-snkrs/lk-new-theme/pull/18
- Head SHA: `fc5d97eaaf7f52dd14c73ed58d2faea6678253e2`
- Merged: `False`
- Merge state before merge: `dirty`


## GitHub PR / merge completed
- PR: https://github.com/lk-snkrs/lk-new-theme/pull/18
- Merged: `True`
- Merge SHA: `d61a028ccd5a859a926d3d17231e91f00451a28a`


## Final live QA
- Gazelle: pass=False, sections=0, items=0, item_images=0, liquid_errors=0
- Air Jordan 4: pass=True, sections=1, items=5, item_images=5, liquid_errors=0
- Taekwondo Mei: pass=True, sections=1, items=5, item_images=5, liquid_errors=0
- Handball Spezial: pass=True, sections=1, items=5, item_images=5, liquid_errors=0
- Lululemon: pass=False, sections=1, items=5, item_images=5, liquid_errors=3
All pass: False
