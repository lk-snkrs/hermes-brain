# LK OS current GMC monitor — 2026-05-14

Generated: `2026-05-14T21:31:25.019670+00:00`

Productstatuses read: `23277`

## Target issue instances
- landing_page_error: `3` instances / `1` products
- price_updated: `921` instances / `307` products
- strikethrough_price_updated: `228` instances / `76` products

## Latest execution readout
- Resume status: `completed_with_verify_mismatches`
- Price repair status: `completed_with_review`
- Price repair summary: `{'input_targets': 152, 'triage_counts': {'needs_content_upsert_price': 62, 'no_action_current_matches_shopify': 43, 'needs_content_upsert_sale': 42, 'needs_content_upsert_clear_sale': 5}, 'actions_count': 109, 'execution_counts': {'content_upserted': 109}, 'verify_matches': 0, 'verify_mismatches': 109}`

## Não executado
- Shopify write
- Tiny write
- feed fetch/upload
- campaign/message/send
- bulk reapply after non-persisting price writes
