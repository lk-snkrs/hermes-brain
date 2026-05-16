# LK GMC Required Attributes Apply, Second Batch, 2026-05-12

Status: `gmc_required_attrs_second_batch_applied_fetch_triggered`

## Resumo
- existing_rows_before: 3613
- rows_after: 3613
- approved_required_attr_rows: 72
- rows_created: 0
- rows_updated_or_completed: 72
- rows_already_matching: 0
- age_group_counts_applied: {'adult': 71, 'kids': 1}
- gender_counts_applied: {'unisex': 72}
- gist_patch_verified_by_api_content: True
- datafeed_fetch_url_updated_to_revision: True
- merchant_fetch_now_called: True
- merchant_fetch_now_response_keys: ['kind']
- production_writes: 2
- gist_feed_write: 1
- merchant_datafeed_config_write: 1
- shopify_writes: 0
- gsc_writes: 0
- campaign_sends: 0
- external_contacts: 0
- purchases_or_pos: 0
- marketplace_calls: 0
- n8n_flows_created: 0

## Rollback
- Backup CSV: `reports/lk-gmc-supplemental-feed-before-required-attrs-second-batch-2026-05-12.csv`
- Datafeed backup: `reports/lk-gmc-datafeed-before-required-attrs-second-batch-2026-05-12.json`
- Instrução: PATCH the gist file back to backup_csv; optionally PUT datafeed_backup_json back to datafeeds/{id}; then POST fetchNow.

## Não executado
- shopify_product_or_metafield_write
- gsc_admin_or_indexing_submit
- checkout_setting_change
- theme_or_pdp_write
- campaign_send_or_schedule
- supplier_contact
- purchase_or_po
- external_marketplace_call
- n8n_flow_creation
