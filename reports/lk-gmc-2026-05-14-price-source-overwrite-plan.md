# LK GMC price source/overwrite plan — 2026-05-14

Generated: `2026-05-14T21:11:29.842391+00:00`

## Current residual baseline
- price_updated: `921` instances / `307` products
- strikethrough_price_updated: `228` instances / `76` products
- landing_page_error: `3` instances / `1` products

## Diagnosed price cohort
- Products diagnosed: `152`
- merchant_stale_vs_shopify_and_public: `108`
- merchant_matches_shopify_admin: `44`

## Stale mismatch buckets
- regular_price_stale: `62`
- sale_price_only_stale: `30`
- price_and_sale_price_stale: `11`
- sale_price_should_be_cleared: `5`

## Data source map
- `10525577766` — lksneakers.com.br / AUTOFEED: primary crawl/autofeed; FREE_LISTINGS enabled; Shopping Ads disabled; price risk: can surface crawl-derived offer state, but no API write target
- `10636492695` — Content API / API: primary API product input; SHOPPING_ADS, FREE_LISTINGS, DISPLAY_ADS enabled; price risk: intended write target; price PATCH/upsert returned success but final Content readback did not persist for 109
- `10636384718` — Content API / API: legacyLocal/local inventory; FREE_LOCAL_LISTINGS enabled; price risk: local/LIA; not primary online price target
- `10646853947` — LK Sneakers - Color Supplemental Feed / FILE weekly fetch Mon 03:00 BRT: supplemental-looking file; Display/Free/Shopping enabled in resource; Content API feed target also excludes Shopping in legacy view; price risk: feed header has id,color,age_group,gender,size only; not direct price source

## Supplemental feed probe
- Fetch header: `id,color,age_group,gender,size`.
- No `price`/`sale_price` columns found in the fetched header/sample, so this file is not the direct price overwrite source.

## Operational conclusion
- Keep price yellow/blocked. Do not retry bulk price patches while readback does not persist.
- The most likely failure mode is source ownership / Merchant merge / auto-update/crawl behavior between API primary (`10636492695`) and autofeed/crawl (`10525577766`) or Shopify/Merchant app channel, not bad Shopify prices.
- `strikethrough_price_updated` must stay separate from regular price because it involves `salePrice`/compare-at semantics.

## Next safe gate
1. Read-only Merchant source/settings drilldown: inspect item sources/auto-update settings/UI/API evidence for price ownership and whether API primary is losing to crawl/autofeed.
2. Produce a remediation packet with one of: disable/adjust automatic price updates, refresh source ownership, or perform a tiny pilot after source ownership is fixed.
3. No source/datafeed/settings changes without explicit Lucas approval + rollback plan/screenshots/export.

## Not performed
- Merchant write
- Content API write
- Shopify write
- Tiny write
- data source delete/update
- feed fetch/upload
- campaign/message/send
