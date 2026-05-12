# LK GMC Required Attributes Datafeed Refresh, 2026-05-12

Status: `gmc_required_attrs_revision_fetch_triggered`

## Resumo

- gist_revision_raw_url_detected: True/raw/[revision]/lk_sneakers_gmc_color_feed.csv
- gist_content_has_required_headers: True
- previous_fetch_url: https://gist.githubusercontent.com/lk-snkrs/8eb7f7fb61a46fa8d5a4d64fa7f21b2f/raw/[revision]/lk_sneakers_gmc_color_feed.csv
- new_fetch_url: https://gist.githubusercontent.com/lk-snkrs/8eb7f7fb61a46fa8d5a4d64fa7f21b2f/raw/[revision]/lk_sneakers_gmc_color_feed.csv
- datafeed_fetch_url_updated: True/raw/[revision]/lk_sneakers_gmc_color_feed.csv
- merchant_fetch_now_called: True
- merchant_fetch_now_response_keys: ['kind']
- production_writes: 1
- merchant_datafeed_config_write: 1
- shopify_writes: 0
- gsc_writes: 0
- campaign_sends: 0
- external_contacts: 0
- purchases_or_pos: 0
- marketplace_calls: 0
- n8n_flows_created: 0

## Rollback
- Backup: `reports/lk-gmc-datafeed-before-required-attrs-refresh-2026-05-12.json`
- Instrução: PUT the saved datafeed JSON back to Content API datafeeds/{id}, then trigger fetchNow.

## Não executado
- shopify_write
- gsc_write
- checkout_or_theme_write
- campaign_send
- supplier_or_customer_contact
- purchase_or_po
- external_marketplace_call
- n8n_flow_creation
