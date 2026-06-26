# LK GMC P1 Attribute Completion — Wave4 Aggressive Non-Price Executor, 2026-05-13

Status: `gmc_p1_attribute_wave4_aggressive_nonprice_dry_run_ready`

## Escopo
- Modo: `dry-run`
- Campos permitidos: `color`, `sizes`, `ageGroup`, `gender`.
- Excluído: `price` mesmo quando o produto também tem issue de preço.
- Critério Lucas: completude para ranking > fidelidade perfeita em atributos não críticos.

## Resultado
- Required rows pré-execução: 232
- Required instances pré-execução: 363
- Ready: 228
- Selecionados/aplicados: 228
- Suggested fields: {'color': 183, 'sizes': 51, 'ageGroup': 31, 'gender': 31}

## Estados
- blocked_price_only_no_nonprice_update: 4
- ready_for_wave4_aggressive_nonprice_apply: 228

## Execução/verificação
- Execution: {}
- Verify: {}
- Match esperado: 0/0

## Rollback privado
- Não criado no dry-run.

## Não executado
- merchant_price_update
- merchant_delete
- merchant_title_link_image_availability_update
- feed_update_or_fetch
- shopify_write
- tiny_call_or_write
- database_write
- pos_or_local_inventory_write
- klaviyo_or_whatsapp_send
- notion_or_n8n_write
- loyalty_or_judgeme_action
