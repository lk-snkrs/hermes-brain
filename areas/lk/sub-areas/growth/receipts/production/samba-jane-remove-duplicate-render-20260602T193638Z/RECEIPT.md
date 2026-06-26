# Receipt — Samba Jane duplicate block removed

Timestamp UTC: 2026-06-02T19:36:45Z

## What was fixed
Removed the extra explicit render of `snippets/lk-samba-jane-coll-preview.liquid` from `sections/lk-collection.liquid` for `collection.handle == 'adidas-samba-jane'`.

Reason: the collection already had the LKGOC/204L visual block rendered in the collection hero/description area; the extra render after the banner caused the duplicate block visible before the grid.

## Production target
- Theme id: 155065417950
- Asset changed: `sections/lk-collection.liquid`

## QA readback
- Removed blocks: 1
- Render count after: 0
- Samba class in section after: 0
- Section bytes: 253691
- Under 256KB: True

## Public/headless QA
- URL: https://lksneakers.com.br/collections/adidas-samba-jane?qa=20260602T193656Z
- Screenshot: `samba-jane-after-remove-duplicate.png`
- Collection title occurrences: 136
- Size selector present: 1
- Items count present: 1

Note: headless DOM did not expose the same visible editorial strings returned in Lucas' browser screenshot, but the duplicated explicit Shopify render was removed at source.

## Rollback
PUT sections__lk-collection.before.liquid back to sections/lk-collection.liquid
