# LK GMC P1 Attribute Completion — Wave6 Price from Shopify Source, 2026-05-13

Status: `gmc_p1_attribute_wave6_price_apply_verified`

## Escopo
- Modo: `apply`
- Campo alterado: `price` somente.
- Fonte: preço do Shopify/Data Spine por handle/link, offer/SKU/variant ou título normalizado exato.
- Política multi-variante: menor preço positivo de variante Shopify para o produto.

## Resultado
- Price rows atuais: 35
- Ready: 35
- Selecionados/aplicados: 35
- Fontes: {'shopify_handle_from_merchant_link': 34, 'exact_normalized_title': 1}
- Execution: {'updated_wave6_price': 35}
- Verify: {'verified_product_get': 35}
- Match esperado: 0/35
- Required rows after: 35
- Required instances after: 35
- Counts after: {'price': 35}

## Rollback privado
- `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-13-p1-attribute-wave6-price-shopify-source-executor-rollback-20260513T152343Z.json`

## Não executado
- merchant_delete
- merchant_non_price_update
- feed_update_or_fetch
- shopify_write
- tiny_call_or_write
- database_write
- pos_or_local_inventory_write
- klaviyo_or_whatsapp_send
- notion_or_n8n_write
- loyalty_or_judgeme_action
