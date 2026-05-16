# LK GMC Post A/B Package B Remaining Reconciliation, 2026-05-12

Status: `gmc_post_ab_b_remaining_reconciliation_readonly`

## Resumo executivo
- Merchant products live lidos: 23147
- Registros B do snapshot original: 954
- Old absent depois do A/B: 93
- Old presente sem target estrito: 854
- Old presente com target já existente: 7
- Candidatos estritos novos agora write-ready: 0
- Fila de revisão title-only: 0

## Principais bloqueios dos B restantes sem target estrito
- link_variant_not_found_active: 840
- gtin_not_found_in_active_shopify: 11
- gtin_duplicate_active_skus: 3

## Veredito
- Não apareceu novo B seguro para escrita automática nesta revalidação.
- Os casos title-only ajudam a revisão humana/Data Spine, mas não bastam para mudar offerId no Merchant sem confirmar tamanho/SKU.
- CSV privado de revisão: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_reconciliation/lk-gmc-2026-05-12-post-ab-b-remaining-reconciliation-review.csv`

## Não tocado
- merchant_product_write_or_delete
- local_channel
- shopify
- feed
- database
- campaign_or_external_send
- google_business_profile
- pos_inventory
