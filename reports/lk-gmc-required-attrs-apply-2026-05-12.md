# LK GMC Required Attributes Apply, 2026-05-12

Generated at: `2026-05-12T02:17:44.875327+00:00`

## Veredito

Status: `gmc_required_attrs_applied_fetch_triggered`

Lucas aprovou a aplicação. O supplemental feed existente do Merchant foi atualizado no Gist e o fetchNow do datafeed foi acionado.

## Resumo

- existing_rows_before: 3613
- rows_after: 3613
- approved_required_attr_rows: 80
- rows_created: 0
- rows_updated_or_completed: 80
- rows_already_matching: 0
- columns_after: ['id', 'color', 'age_group', 'gender', 'size']
- age_group_counts_applied: {'adult': 79, 'kids': 1}
- gender_counts_applied: {'male': 7, 'unisex': 70, 'female': 3}
- gist_patch_verified_by_api_content: True
- merchant_fetch_now_called: True
- merchant_fetch_now_response_keys: ['kind']
- production_writes: 1
- merchant_feed_write: 1
- shopify_writes: 0
- gsc_writes: 0
- campaign_sends: 0
- external_contacts: 0
- purchases_or_pos: 0
- marketplace_calls: 0
- n8n_flows_created: 0

## Superfície aplicada

- type: merchant_center_supplemental_feed_csv_gist
- gist_id: 8eb7f7fb61a46fa8d5a4d64fa7f21b2f
- gist_file: lk_sneakers_gmc_color_feed.csv
- datafeed_id: 407508563
- datafeed_name: LK Sneakers - Color Supplemental Feed
- fetch_url: https://gist.githubusercontent.com/lk-snkrs/8eb7f7fb61a46fa8d5a4d64fa7f21b2f/raw/lk_sneakers_gmc_color_feed.csv

## Rollback

- Backup: `reports/lk-gmc-supplemental-feed-before-required-attrs-2026-05-12.csv`
- Instrução: PATCH the gist file back to the backup CSV content, then POST datafeeds/{datafeed_id}/fetchNow again.

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
