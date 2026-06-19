# Receipt — P1A Shopify-first Category + identifier_exists — 2026-06-18

Status: executed with Lucas approval.

Scope:

- First 50 high-confidence rows from P1 packet.
- Excluded manual review rows.
- Fields only: Shopify category + `mm-google-shopping.identifier_exists`.
- No price, stock, availability, campaign, Simprosys or direct GMC writes.

Results:

- Items processed: 50.
- Category updates attempted: 50.
- Initial identifier updates attempted: 27.
- Initial receipt all checks: False.
- Retry reason: initial metafieldsSet mutation had a GraphQL selection error in readback payload (`owner.id` selection), so identifier writes were retried with corrected mutation.
- Identifier updates retried: 27.
- Final Shopify readback all checks passed: True.

Files:

- Rollback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/p1a-shopify-category-identifier-20260618/rollback-before-p1a-category-identifier.json`
- Initial receipt: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/p1a-shopify-category-identifier-20260618/receipt-p1a-category-identifier-readback.json`
- Retry/final readback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/p1a-shopify-category-identifier-20260618/receipt-p1a-identifier-retry-readback.json`
- Final summary: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/p1a-shopify-category-identifier-20260618/summary-final.json`

Next readback:

- Wait for Simprosys sync and GMC processing.
- Then re-check affected issue counts for category/product data and `identifier_exists` related diagnostics.
- This P1A does not address the local feed drop (`store_code`, local inventory, `link_template`) directly.
