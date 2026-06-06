# Curadoria LK PDP — DEV Yeezy Slide readback

- timestamp UTC: `2026-06-05T18:18:17.647085+00:00`
- action result: No new PUT performed by final apply attempt because DEV asset already contained marker top30-yeezy-slide-regular before upload; treated as idempotent readback success.
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
- images valid: `True`
- bad URL occurrences: `{'https:https://': 0, 'https://https://': 0, 'TenisMoldeLK': 0}`

## Public preflight
- products OK: `True`
- images OK: `True`

## Preview HTML QA caveat
- Public preview_theme_id requests redirected/dropped preview_theme_id, so HTML QA hit live/main storefront rather than DEV preview. Source/readback/static QA are valid for DEV; visual preview still needs browser/authenticated theme preview or Shopify preview link.

## Rollback
- Because no new PUT occurred in this attempt, rollback is not needed for this execution. If reverting the existing DEV group is requested, remove marker top30-yeezy-slide-regular from the five aligned arrays in DEV only after explicit approval.

## Non-actions
- No Production/main write
- No product write
- No price/stock/app/GMC/Tiny/Klaviyo/Meta/checkout/discount/fulfillment write