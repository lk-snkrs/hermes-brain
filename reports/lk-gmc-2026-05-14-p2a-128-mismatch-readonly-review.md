# LK GMC P2A — Read-only mismatch review 2026-05-14

Status: `readonly_completed`

## Summary
- total_patched_rows: 9826
- verified_merchant_product_get: 9826
- mismatch_count: 153
- failed_count: 0

## Top mismatch patterns
- 107 × expected `Apparel & Accessories > Shoes / ['Tênis']` vs actual `Vestuário e acessórios > Sapatos / ['Tênis']`
- 43 × expected `Luggage & Bags > Handbags, Wallets & Cases / ['Bolsa/Carteira']` vs actual `None / ['Bolsa/Carteira']`
- 1 × expected `Apparel & Accessories > Clothing Accessories > Hats / ['Boné']` vs actual `3515 / ['Boné']`
- 1 × expected `Luggage & Bags > Handbags, Wallets & Cases / ['Bolsa/Carteira']` vs actual `None / ['Bolsa']`
- 1 × expected `Apparel & Accessories > Shoes / ['Tênis']` vs actual `Apparel & Accessories > Shoes / ['Tenis', 'Sneakers']`

## Not performed
- merchant_patch
- merchant_delete
- title_update
- price_update
- availability_update
- shopify_write
- tiny_write
- notion_write
- marketplace_lookup
