# LK GMC P2A Finalize Remaining Online — 2026-05-13

Status: `apply_completed_needs_review`

## Escopo
- Merchant API v1 ProductInputs PATCH.
- Somente `productAttributes.googleProductCategory` + `productAttributes.productTypes`.
- DataSource: `10636492695`.
- Exclui local inventory/LIA e candidatos ambíguos.

## Resumo
- mode: apply
- base_candidates: 10576
- selected_to_patch: 9826
- skipped_already_compliant: 750
- selected_bucket_counts: {'Apparel & Accessories > Shoes / Tênis': 8903, 'Apparel & Accessories > Clothing > Pants / Calça': 416, 'Apparel & Accessories > Clothing > Outerwear / Moletom/Jaqueta': 318, 'Apparel & Accessories > Clothing Accessories > Hats / Boné': 101, 'Apparel & Accessories > Clothing > Shorts / Shorts': 44, 'Luggage & Bags > Handbags, Wallets & Cases / Bolsa/Carteira': 44}
- execution_results_summary: {'patched_p2a_finalize_v1': 9826}
- verify_results_summary: {'verified_merchant_product_get': 9826}
- patched_count: 9826
- verified_match_expected: 9698
- verify_mismatch_count: 128
- verify_failed_count: 0

## Rollback privado
- Shards criados: 40

## Não executado
- title_update
- price_update
- availability_update
- image_or_link_update
- merchant_delete
- local_inventory_write
- shopify_write
- tiny_write
- database_write
- feed_fetch_or_upload
- campaign_or_message_send
