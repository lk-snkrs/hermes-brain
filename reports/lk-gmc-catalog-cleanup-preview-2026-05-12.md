# LK GMC Catalog Cleanup Preview, 2026-05-12

Status: `gmc_catalog_cleanup_preview_ready_readonly`

## Resumo
- merchant_products_read: 25578
- merchant_channels: {'local': 11638, 'online': 13940}
- preview_rows_total_p1_p2: 4671
- p1_rows: 1302
- p2_rows: 3369
- action_counts: {'keep_valid_local_listing_preview_only': 10336, 'investigate_or_suppress_local_orphan_preview_only': 985, 'monitor_keep_for_now': 10571, 'investigate_online_orphan_preview_only': 3369, 'cleanup_candidate_local_duplicate_preview_only': 317}
- reason_counts: {'local_lia_prefix_matches_shopify_after_normalization': 10336, 'local_offer_id_not_found_after_lia_normalization_in_shopify_sku_or_variant_ids': 985, 'no_safe_cleanup_signal': 10571, 'online_offer_id_not_found_in_shopify_sku_or_variant_ids': 3369, 'same_offer_id_exists_as_online_and_local': 317}
- sample_rows_published: 500
- merchant_writes: 0
- shopify_writes: 0

## Melhor melhoria candidata
- A LK usa Local Listings/inventário local, então o canal `local` deve ser preservado.
- O preview agora normaliza `LIA_<sku>` para `<sku>` apenas para reconciliação contra Shopify/Data Spine.
- Alvo seguro agora: investigar somente locais que continuam sem match após essa normalização e online órfãos; execução exige aprovação específica e rollback.

## Não executado
- merchant_product_delete
- merchant_product_update
- datafeed_update
- local_inventory_feed_change
- shopify_write
- campaign_send
- external_contact
