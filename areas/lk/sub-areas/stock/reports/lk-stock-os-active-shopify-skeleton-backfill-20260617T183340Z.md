# LK Stock OS — active Shopify skeleton DB backfill

- Run ID: `20260617T183340Z`
- Input DB: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/data/lk_stock_os_current_variant_promotion_20260617T182527Z.db`
- Output DB: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/data/lk_stock_os_current_active_shopify_skeleton_backfill_20260617T183340Z.db`
- Active Shopify unique SKUs seen: `12031`
- Current rows before: `3799`
- Skeleton rows inserted: `8792`
- Current rows after: `12591`
- Guardrails: Tiny write `0`; Shopify write `0`; writes externos `0`; public availability `0`.

Inserted rows are not availability confirmations. They only make the local database aware of active Shopify SKUs; Tiny correspondence/stock remains pending and fail-safe until crosswalk/live readback resolves it.
