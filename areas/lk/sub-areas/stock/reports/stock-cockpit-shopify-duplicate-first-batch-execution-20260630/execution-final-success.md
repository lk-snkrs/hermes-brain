# Stock Cockpit — Shopify duplicate first batch SUCCESS — 2026-06-30

- generated_at_utc: `2026-06-30T15:33:27.617063+00:00`
- values_printed: false
- writes_attempted: 3
- writes_verified: 3
- all_verified: true
- scope: Shopify InventoryItem SKU-only, first approved batch

## Changes verified
- variant `45968993911006` / inventory `48067760488670`: `183A872` → `183A872-7`; live `183A872-7`; verified `true`
- variant `45968993943774` / inventory `48067760521438`: `183A872` → `183A872-8`; live `183A872-8`; verified `true`
- variant `47604797472990` / inventory `49719203659998`: `FJ3453-200` → `FJ3453-200-8`; live `FJ3453-200-8`; verified `true`

## OAuth / permission
- Shopify official CLI reauth completed with `write_inventory=true` and `read_inventory=true`.
- values_printed=false; OAuth code/state/token values not persisted in report.

## Not changed
Tiny, Supabase, stock quantity, price, title, image, collection, product text and vendors were not changed.

## Rollback
Rollback is SKU-only using the old SKU values listed above, via the same `inventoryItemUpdate` path, if Lucas requests it.
