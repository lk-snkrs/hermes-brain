# Receipt — NB 204L color filter toggle fix on Dev theme

Date UTC: 20260603T185137Z

## Scope approved by Lucas

Lucas approved uploading the prepared color-filter toggle correction to the Shopify Dev/unpublished theme for preview QA.

## Target

- Storefront surface: collection filters on `/collections/new-balance-204l`
- Theme Dev/unpublished: `155065450718` (`lk-new-theme/dev`, role `unpublished`)
- Production theme: `155065417950` (`lk-new-theme/production`, role `main`)
- Asset: `sections/lk-collection.liquid`

## Cause

Color filter chip anchors were rendered with `value.url_to_add` even when `value.active == true`. Result: clicking an already-active color such as `Preto` did not remove the filter.

## Change applied to Dev only

For the desktop and mobile color chip anchors:

```liquid
href="{% if value.active %}{{ value.url_to_remove }}{% else %}{{ value.url_to_add }}{% endif %}"
```

This preserves add behavior for inactive colors and uses Shopify's native remove URL for active colors.

To satisfy Shopify Asset API's 256 KB PUT limit, non-rendered Liquid comments were removed from the source asset. No customer-facing copy, products, price, stock, checkout, apps, or production theme asset were changed.

## Readback evidence

- Upload status: `uploaded_dev_readback_ok`
- Dev before SHA: `9867b62f3c3bd7bf`
- Dev after SHA: `e467d627a4ad80d9`
- Local SHA: `e467d627a4ad80d9`
- Production before SHA: `8744b6ea095ab34d`
- Production after SHA: `8744b6ea095ab34d`
- Production unchanged: `true`
- `value.url_to_remove` occurrences in Dev asset: `2`
- Dev asset bytes after slimming: `260066` (under Shopify PUT limit)

## QA

Static Dev asset QA passed:

- 2 color chip toggle anchors found: desktop + mobile
- 0 old add-only color chip anchors remain
- Expected inactive color click: `value.url_to_add`
- Expected active color click: `value.url_to_remove`
- Single-value `Marca` / `Categoria` hide markers for NB 204L remain present

Public unauthenticated `preview_theme_id` fetches were not authoritative in this environment: Shopify served live/production HTML and dropped the preview marker. Therefore public browser click QA should be done from an authenticated Shopify preview/browser before any production promotion.

## Git trace

- Local branch: `fix/collection-filter-toggle-remove`
- Local commit: `5a90fdd` (`fix(collection): allow active color filter chips to remove`)
- Not pushed / no PR opened in this step.

## Rollback

Dev rollback options:

1. Re-upload prior Dev asset snapshot by restoring SHA/state `9867b62f3c3bd7bf` from local/API backup if needed.
2. Git rollback local branch: `git revert 5a90fdd`.

Production rollback not needed because production was not changed.

## Remaining blocker

Production promotion is blocked until Lucas explicitly approves a Dev → Production promotion after preview/browser QA.
