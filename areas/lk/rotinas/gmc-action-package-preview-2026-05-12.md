# LK GMC Action Package Preview, 2026-05-12

Status: `gmc_action_package_preview_ready_readonly`

## Resumo executivo
- Fila P0/P1 total: 2168
- P0/P1 por prioridade: {'P0': 5, 'P1': 2163}
- Por canal: {'online': 866, 'local': 1302}
- Merchant/Shopify/feed writes: 0

## Pacotes de ação
### B_online_identifier_fix — online_identifier_mismatch
- Itens: 861
- Risco: `medium`
- Prioridades: {'P1': 861}
- Canais: {'online': 861}
- Aprovação: Lucas approval for any feed, Merchant, Shopify, or app identifier write.
- Rollback: Keep old identifier mapping and feed/resource snapshot; rollback by restoring previous identifier/feed row.
- Sequência proposta:
  - Confirm whether GTIN/product match maps to an active Shopify variant with different SKU/offer_id.
  - Prefer fixing source identifiers/feed mapping over deleting the Merchant item.
  - Generate exact before/after mapping preview for SKU/offer_id/product_id/GTIN.
  - Execute only after approval for the specific source to change: Merchant/feed/Shopify/app.

### C_local_identifier_fix — local_identifier_mismatch
- Itens: 847
- Risco: `medium_high`
- Prioridades: {'P1': 847}
- Canais: {'local': 847}
- Aprovação: Lucas approval for any local inventory/POS/Merchant mapping write.
- Rollback: Keep LIA product resource snapshot and POS/local mapping before any change; rollback by restoring mapping/resource.
- Sequência proposta:
  - Preserve local listings by default because LK uses physical store/local inventory.
  - Confirm Shopify POS/local inventory mapping for LIA_ offer_id and current SKU/GTIN/product.
  - Prepare mapping correction preview; avoid local inventory deletion unless stale is proven.
  - Execute only after approval because it can affect local free listings/local inventory visibility.

### D_local_stale_triage — local_unmatched_after_normalization
- Itens: 455
- Risco: `medium_high`
- Prioridades: {'P1': 455}
- Canais: {'local': 455}
- Aprovação: Lucas approval for local Merchant cleanup or local inventory feed/app change.
- Rollback: Keep exact local product resource snapshot; rollback by restoring/reinserting local product or source feed row.
- Sequência proposta:
  - Sample against live Shopify POS/local inventory and Tiny before treating as stale.
  - If no valid current source exists, prepare local-only cleanup preview by exact product ID.
  - Do not disable the local channel globally; act only on proven stale product IDs.
  - Execute only after approval and rollback snapshot.

### A_online_stale_triage — online_unmatched_possible_stale
- Itens: 5
- Risco: `high`
- Prioridades: {'P0': 5}
- Canais: {'online': 5}
- Aprovação: Lucas approval for Merchant product delete/suppression or feed change.
- Rollback: Reinsert or restore exact Merchant product resource/feed row from pre-action snapshot if a valid item is removed.
- Sequência proposta:
  - Verify a sample against live Shopify by offer_id, GTIN/barcode, product handle/title.
  - If no current Shopify/Data Spine match exists, prepare Merchant cleanup/delete preview for exact product IDs only.
  - Before execution, export product IDs, titles, URLs, status and current resource snapshot as rollback evidence.
  - Execute only after Lucas approval; verify Merchant count/diagnostics after reprocessing lag.

## Ordem recomendada
1. A_online_stale_triage: maior volume e menor risco sobre inventário físico.
2. B_online_identifier_fix: saneamento de ID antes de apagar.
3. D_local_stale_triage: local sensível, só produto provado como stale.
4. C_local_identifier_fix: preservar local listings e corrigir mapeamento com cuidado.

## Não executado
- merchant_product_delete
- merchant_product_update
- feed_update
- shopify_write
- database_write
- campaign_or_external_send
- local_inventory_disable
- gmb_update
- pos_inventory_write
