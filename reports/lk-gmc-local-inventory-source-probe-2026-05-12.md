# LK GMC Local Inventory Source Probe, 2026-05-12

Status: `gmc_local_inventory_source_probe_ready_readonly`

## Veredito
- Fonte provável do inventário local: **Shopify POS / Shopify app via Google Content API**.
- Confiança: `high`.
- O canal local está ativo no Merchant e aponta para `shopify.com` como provedor POS/local.
- Portanto, `local` não deve ser tratado como ruído.

## Evidências
- Merchant LIA settings has inventory status active for BR.
- Merchant LIA settings reports posExternalAccountId=shopify.com.
- Merchant local products have source=api, not file/feed.
- Only listed datafeed is the supplemental color feed, not the primary local inventory source.
- Most local offer IDs use LIA_ prefix, which is characteristic of Local Inventory Ads/local channel IDs and can break naive SKU matching.

## Números principais
- Produtos Merchant lidos: 25578
- Canal `local`: 11638
- Canal `online`: 13940
- Source por canal: {'local|api': 11638, 'online|api': 10025, 'online|feed': 3613, 'online|crawl': 302}
- Prefixos local: {'LIA_': 11638}
- Match Shopify local raw: 0
- Match Shopify local após remover `LIA_`: 10336
- Sem match após normalização `LIA_`: 1302

## Interpretação
- Previous local orphan counts are too conservative because raw matching did not normalize the LIA_ prefix. After stripping LIA_, many local items may match Shopify SKUs/variants.
- Do not delete local items based on the first orphan preview. Local listings are active and backed by Shopify POS/local inventory integration.
- Próximo passo seguro: Regenerate cleanup preview with LIA_ normalization and split true stale local items from valid Shopify POS local items.

## Não executado
- merchant_product_delete
- merchant_product_update
- datafeed_update
- feed_delete_or_exclusion
- shopify_write
- database_write
- campaign_or_external_send
- local_inventory_disable
- gmb_update
