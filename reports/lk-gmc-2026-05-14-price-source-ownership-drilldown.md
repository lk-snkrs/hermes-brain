# LK GMC price source ownership drilldown — 2026-05-14

Generated: `2026-05-15T20:18:49.160007+00:00`

Sample stale products probed: `12`

## Read-only findings
- Account settings probe: HTTP `200`; automaticImprovements: `returned`.
- ProductInputs source presence in sample: `{}`.
- API input vs final Merchant output: `{}`.
- Fresh final output vs Shopify target: `{'fresh_output_stale_vs_shopify_target': 12}`.
- Fresh Productstatus price issue details in sample: `{'price_updated': 36}`.

## Interpretation
- Automatic item price updates are enabled/effective at account level; productstatuses confirm Google is auto-updating mismatched prices from the online store with servability unaffected.
- ProductInputs GET returned 404 for all sampled source/dataSource combinations even though final products are readable; source ownership could not be proven at ProductInput-read level, so use final product + account auto-update + productstatus evidence.
- Some fresh final outputs remain stale vs Shopify target; those need source/feed regeneration or a tightly verified price/salePrice pilot after the ownership path is fixed.

## Probe samples
- `online:pt:BR:01424-002-2`: final `5999.90`/`None`, fresh Content `5999.90`/`None`, API input `None`/`None`, autofeed input exists `False`; Shopify target `8999.99`/`None`; status issue codes `['price_updated', 'price_updated', 'price_updated']`
- `online:pt:BR:553558140-7`: final `1499.99`/`None`, fresh Content `1499.99`/`None`, API input `None`/`None`, autofeed input exists `False`; Shopify target `1799.99`/`None`; status issue codes `['price_updated', 'price_updated', 'price_updated']`
- `online:pt:BR:AQ9129-170-5`: final `2599.99`/`None`, fresh Content `2599.99`/`None`, API input `None`/`None`, autofeed input exists `False`; Shopify target `2749.99`/`None`; status issue codes `['price_updated', 'price_updated', 'price_updated']`
- `online:pt:BR:AQ9129-170-7`: final `2599.99`/`None`, fresh Content `2599.99`/`None`, API input `None`/`None`, autofeed input exists `False`; Shopify target `3349.99`/`None`; status issue codes `['price_updated', 'price_updated', 'price_updated']`
- `online:pt:BR:AQ9129-170-9`: final `2599.99`/`None`, fresh Content `2599.99`/`None`, API input `None`/`None`, autofeed input exists `False`; Shopify target `3349.99`/`None`; status issue codes `['price_updated', 'price_updated', 'price_updated']`
- `online:pt:BR:CJ5378700-36`: final `5499.99`/`None`, fresh Content `5499.99`/`None`, API input `None`/`None`, autofeed input exists `False`; Shopify target `6099.99`/`None`; status issue codes `['price_updated', 'price_updated', 'price_updated']`

## Next safe remediation design
- Do **not** bulk-retry price writes yet.
- If API input is stale and matches final output, the next corrective route is likely source-of-truth regeneration/resync of the API feed/channel for exact rows, or a small ProductInputs v1 pilot with post-delay readback that verifies the API input itself changed and stayed changed.
- If Merchant UI confirms automatic price updates are active and overriding API, prepare a separate settings-change packet with rollback/screenshot/export before any change.

## Not performed
- Merchant write
- Content API write
- ProductInputs PATCH
- data source update/delete
- automatic item update settings change
- feed fetch/upload
- Shopify write
- Tiny write
- campaign/message/send
