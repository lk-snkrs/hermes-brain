# LK GMC B3 Same-ID Root Cause, 2026-05-12

Status: `gmc_b3_same_id_root_cause_completed_readonly`

## Resumo executivo
- Linhas investigadas: 854
- Shopify live active variant with SKU: 854
- B2 old_product_id == new_product_id: 854
- B2 old_product_id != new_product_id: 0
- SKU Shopify live ausente no Data Spine local: 854
- Data Spine products max(updated_at): 2026-04-17T00:00:33.618+00:00
- Data Spine variants max(updated_at): None

## Causa raiz
- O ranker original colocou esses itens em B porque havia evidência fraca de produto/GTIN, mas o SKU exato não aparecia no Data Spine local.
- O Shopify live mostrou que os 854 variants existem, estão ativos e têm SKU.
- O B2 transformou isso em `target_already_exists`, mas não checou se o target era o próprio old ID.
- Como `old_product_id == target_product_id` nos 854 casos, B3 não era uma limpeza de duplicata; era delete do item real.

## Correção operacional
- B3 foi revertido e verificado: 854/854 presentes novamente.
- Scripts/skills devem bloquear hard qualquer delete same-ID.
- Esses 854 devem virar `same_id_noop/valid_after_shopify_live`, não pacote de delete.

## Não tocado
- merchant_product_write_or_delete
- shopify_write
- feed
- database_write
- campaign_or_external_send
- local_channel
- pos_inventory
