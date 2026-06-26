# LK GMC B Remaining Shopify Live Probe, 2026-05-12

Status: `gmc_b_remaining_shopify_live_probe_readonly`

## Resumo executivo
- Linhas B restantes com variant no link: 854
- Variant IDs únicos consultados no Shopify live: 854
- Review candidates com variant ativo + SKU no Shopify live: 854

## Estados encontrados
- shopify_live_active_variant_with_sku_review_candidate: 854

## Veredito
- A causa provável dos 840 `link_variant_not_found_active` é drift/defasagem do Data Spine local contra Shopify live, não necessariamente ausência real no Shopify.
- Estes candidatos ainda não foram escritos no Merchant. O próximo passo seguro é montar um novo pacote preview com old/new product IDs exatos e rollback.
- CSV privado: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_reconciliation/lk-gmc-2026-05-12-b-remaining-shopify-live-probe.csv`

## Não tocado
- merchant_product_write_or_delete
- shopify_write
- feed
- database
- campaign_or_external_send
- local_channel
- pos_inventory
