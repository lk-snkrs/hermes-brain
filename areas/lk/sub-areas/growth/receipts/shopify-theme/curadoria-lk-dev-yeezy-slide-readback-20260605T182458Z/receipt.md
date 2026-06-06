# Curadoria LK PDP — DEV Yeezy Slide readback

- timestamp UTC: `2026-06-05T18:25:08.818014+00:00`
- action result: Apply attempt found marker already present in DEV; no new PUT performed in this verification run. Current DEV readback matches approved Yeezy Slide packet exactly.
- DEV: `155065450718` / `lk-new-theme/dev` / role `unpublished`
- Production observed: `155065417950` / `lk-new-theme/production` / role `main`
- asset: `snippets/lk-variante-top30-visited.liquid`
- DEV sha12: `493429e95ac5`
- Production marker count: `0`

## Static QA
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
- products OK: `True`
- images OK: `True`

## Preview HTML QA
- `tenis-adidas-yeezy-slide-slate-marine-azul-escuro` status `200`, preview_id_retained `False`, block `False`, marker `False`, label_hits `1`, handle_hits `1`, current_card `False`, ok `False`
- `yeezy-slide-azure` status `200`, preview_id_retained `False`, block `False`, marker `False`, label_hits `1`, handle_hits `1`, current_card `False`, ok `False`

## Caveat
- Public preview_theme_id may redirect/drop preview_theme_id; if preview_id_retained is false, HTML QA is inconclusive for DEV storefront even when Asset API readback/static QA pass.

## Rollback
- No new PUT in this verification run. To revert the existing DEV group, remove marker top30-yeezy-slide-regular from the five aligned arrays in DEV after explicit approval.

## Non-actions
- No Production/main write
- No product write
- No price/stock/app/GMC/Tiny/Klaviyo/Meta/checkout/discount/fulfillment write