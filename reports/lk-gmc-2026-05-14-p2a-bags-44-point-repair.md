# LK GMC P2A — Bags 44 point repair 2026-05-14

Status: `apply_completed_needs_review`

## Scope
- Merchant API v1 ProductInputs PATCH.
- Exact selected products: 44
- Target googleProductCategory: `Apparel & Accessories > Handbags, Wallets & Cases`
- Target productTypes: `['Bolsa/Carteira']`

## Summary
- mode: apply
- selected_count: 44
- source_expected_googleProductCategory: Luggage & Bags > Handbags, Wallets & Cases
- target_googleProductCategory: Apparel & Accessories > Handbags, Wallets & Cases
- still_needs_patch_preflight: 44
- preflight_current_patterns: {"None / ['Bolsa/Carteira']": 43, "None / ['Bolsa']": 1}
- execution_results_summary: {'patched_bags_44_point_repair_v1': 44}
- patched_count: 44
- verify_match_expected: 43
- verify_mismatch_count: 1
- verify_patterns: {"Apparel & Accessories > Handbags, Wallets & Cases / ['Bolsa/Carteira']": 43, "Apparel & Accessories > Handbags, Wallets & Cases / ['Bolsa']": 1}

## Not performed
- title_update
- price_update
- availability_update
- image_or_link_update
- merchant_delete
- local_inventory_write
- shopify_write
- tiny_write
- database_write
- notion_write
- feed_fetch_or_upload
- campaign_or_message_send
- marketplace_lookup
