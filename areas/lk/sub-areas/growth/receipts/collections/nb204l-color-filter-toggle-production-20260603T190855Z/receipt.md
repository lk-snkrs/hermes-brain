# Receipt — NB 204L color filter toggle Production apply

Date UTC: 20260603T190855Z

## Approval

Lucas approved promotion after Dev readback of the color-filter toggle correction.

## Scope

- Collection: `/collections/new-balance-204l`
- Asset: `sections/lk-collection.liquid`
- Production theme: `155065417950` (`lk-new-theme/production`, role `main`)
- Dev theme reference: `155065450718` (`lk-new-theme/dev`, role `unpublished`)

## Change applied

Minimal production patch only: color filter chip links now use Shopify native remove URL when the chip is active.

```liquid
href="{% if value.active %}{{ value.url_to_remove }}{% else %}{{ value.url_to_add }}{% endif %}"
```

This was applied to the two color chip render paths: desktop sidebar and mobile filter sheet.

No product, price, stock, checkout, app, collection data, GMC/feed, or campaign writes were performed.

## Readback evidence

- Production before SHA: `8744b6ea095ab34d`
- Production after SHA: `22db995cc9aa57a0`
- Dev SHA unchanged during production write: `e467d627a4ad80d9`
- Old add-only color chip anchors before: `2`
- Old add-only color chip anchors after: `0`
- `value.url_to_remove` occurrences after: `2`
- Production after bytes: `257761`
- Backup before: `production_before_sections_lk_collection.liquid`
- Planned after snapshot: `production_after_planned_sections_lk_collection.liquid`

## Live QA

Tested live cache-busted storefront HTML:

1. Unfiltered URL: `https://lksneakers.com.br/collections/new-balance-204l?cb=prodqa1909a`
   - Preto chip href: `/collections/new-balance-204l?filter.v.t.shopify.color-pattern=gid%3A%2F%2Fshopify%2FTaxonomyValue%2F1`
   - Verdict: clicking Preto adds filter.

2. Active Preto URL: `https://lksneakers.com.br/collections/new-balance-204l?filter.v.t.shopify.color-pattern=gid%3A%2F%2Fshopify%2FTaxonomyValue%2F1&cb=prodqa1909b`
   - Active Preto chip class: `flt-color-chip checked is-dark`
   - Active Preto chip href: `/collections/new-balance-204l`
   - Verdict: clicking Preto again removes filter.

## Notes

- `Marca` and `Categoria` are still visible on live production, because this production write was intentionally scoped only to the color toggle bug. The prior Dev/PR work for hiding redundant mono-value filters remains a separate promotion decision if needed.

## Rollback

Re-upload `production_before_sections_lk_collection.liquid` to production asset `sections/lk-collection.liquid`, or apply the inverse replacement:

```liquid
href="{% if value.active %}{{ value.url_to_remove }}{% else %}{{ value.url_to_add }}{% endif %}" class="flt-color-chip
```

to:

```liquid
href="{{ value.url_to_add }}" class="flt-color-chip
```

Rollback affects only the color-chip toggle behavior.
