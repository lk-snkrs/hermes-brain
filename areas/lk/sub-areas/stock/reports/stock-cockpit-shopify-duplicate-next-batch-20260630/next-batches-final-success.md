# Stock Cockpit — Shopify duplicate deterministic next batches SUCCESS — 2026-06-30

- generated_at_utc: `2026-06-30T15:39:35.774881+00:00`
- values_printed: false
- writes_verified_this_step: 9
- all_verified: true
- remaining_write_ready_after_recompute: 0
- remaining_next_batch_writes: 0

## Changes verified
- `nike-sb-dunk-low-vx-1000-camcorder` variant `45341347053790` size `36`: `CV1659001` → `CV1659001-3`; live `CV1659001-3`; verified `true`
- `nike-sb-dunk-low-vx-1000-camcorder` variant `45341347119326` size `37`: `CV1659001` → `CV1659001-4`; live `CV1659001-4`; verified `true`
- `nike-dunk-low-patent-halloween` variant `45389958349022` size `37`: `DJ9955800` → `DJ9955800-2`; live `DJ9955800-2`; verified `true`
- `nike-dunk-low-patent-halloween` variant `45389958381790` size `38`: `DJ9955800` → `DJ9955800-3`; live `DJ9955800-3`; verified `true`
- `tenis-new-balance-530-silver-white-branco` variant `47119200747742` size `40`: `MR530EMA` → `MR530EMA-8`; live `MR530EMA-8`; verified `true`
- `tenis-adidas-campus-00s-crystal-white-branco` variant `46146065727710` size `38`: `GY0042` → `GY0042-4`; live `GY0042-4`; verified `true`
- `jersey-off-white-x-nike-allover-print-kelly-green-verde` variant `44750744486110` size `M`: `FQ0997-389` → `FQ0997-389-2`; live `FQ0997-389-2`; verified `true`
- `jersey-off-white-x-nike-allover-print-kelly-green-verde` variant `44750744518878` size `G/L`: `FQ0997-389` → `FQ0997-389-3`; live `FQ0997-389-3`; verified `true`
- `tenis-new-balance-1906l-khaki-bege` variant `47741944791262` size `41`: `U1906LNU` → `U1906LNU-12`; live `U1906LNU-12`; verified `true`

## Current gate
After recompute, no additional deterministic Shopify duplicate SKU-only writes remain (`write_ready=0`). Remaining duplicate groups, if any, require human/LK Shopify identity decision before write.

## Not changed
Tiny, Supabase, stock quantity, price, title, image, collection, product text and vendors were not changed.

## Rollback
Rollback is SKU-only using old_sku values in `nine_write_consolidated_readback.json` if Lucas requests it.
