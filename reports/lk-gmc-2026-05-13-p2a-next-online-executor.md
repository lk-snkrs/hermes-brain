# LK GMC P2A Next Online Executor — 2026-05-13

Status: `dry_run_ready`

## Escopo
- Somente online ProductInputs.
- Campos: `productAttributes.googleProductCategory` + `productAttributes.productTypes`.
- DataSource: `10636492695`.

## Resultado
- Mode: dry-run
- Records: 250
- Eligible fresh: 250
- Buckets: {'Apparel & Accessories > Clothing > Shirts & Tops / Camiseta': 250}
- Execution: {}
- Verify: {}
- Match esperado: 0/0

## Approval text
`Aprovo aplicar P2A next wave piloto em 250 produtos online no GMC via Merchant API v1, apenas googleProductCategory e productTypes, com rollback e verificação.`

## Não executado
- title_update
- price_update
- availability_update
- image_or_link_update
- merchant_delete
- local_inventory_write
- shopify_write
- tiny_write
- database_write
- feed_fetch_or_upload
- campaign_or_message_send
