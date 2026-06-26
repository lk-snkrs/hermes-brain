# LK GMC P1 Attribute Completion — Wave3 Color Tag Executor, 2026-05-13

Status: `gmc_p1_attribute_wave3_color_tag_apply_verified`

## Escopo
- Modo: `apply`
- Bucket: `candidate_wave3_color_tag_high_confidence`.
- Campo alvo: `color` apenas.
- Evidência exigida: tag Shopify explícita `color:*`.
- Apply produtivo: bloqueado até aprovação inline específica.

## Resultado do preflight
- Preview candidates: 5
- Ready: 5
- Selecionados se aprovado: 5

## Estados
- ready_for_wave3_color_tag_apply_if_lucas_approves: 5

## IDs selecionados
- `online:pt:BR:ST63` — Calça Saint Studio Jeans Baggy Risca de Giz Azul — color=Azul
- `online:pt:BR:ST64` — Calça Saint Studio Jeans Baggy Risca de Giz Azul — color=Azul
- `online:pt:BR:ST65` — Calça Saint Studio Jeans Baggy Risca de Giz Azul — color=Azul
- `online:pt:BR:ST66` — Calça Saint Studio Jeans Baggy Risca de Giz Azul — color=Azul
- `online:pt:BR:ST67` — Calça Saint Studio Jeans Baggy Risca de Giz Azul — color=Azul

## Aprovação necessária para apply futuro
- Texto exato requerido pelo executor: `Lucas approved GMC P1 Attribute Wave3 color-tag apply`
- Scope: aplicar `color` apenas nesses IDs high-confidence, com rollback privado antes do write e verificação via `products.get`.

## Rollback privado
- `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-13-p1-attribute-wave3-color-tag-executor-rollback-20260513T131621Z.json`

## Não executado
- merchant_delete
- merchant_delete
- merchant_price_title_link_image_availability_update
- feed_update_or_fetch
- shopify_write
- tiny_call_or_write
- database_write
- pos_or_local_inventory_write
- klaviyo_or_whatsapp_send
- notion_or_n8n_write
- loyalty_or_judgeme_action
