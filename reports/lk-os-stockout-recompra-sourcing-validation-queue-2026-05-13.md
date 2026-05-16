# LK OS — Stockout/Recompra/Sourcing Validation Queue, 2026-05-13

Generated at: `2026-05-14T04:26:59.600249+00:00`

## Step 1 — GMC P2A

- Status report: `apply_in_progress`
- Completion reason: `monitor_timeout`
- Progress counts: `{'patched_p2a_finalize_v1': 9826}`

## Step 2 — Fila curta de validação

Esta fila usa dados locais Shopify/Data Spine e snapshot Tiny quando existe. Não consulta Droper/StockX/GOAT e não cria tarefa Notion. É a fila segura para decidir o que validar/acionar depois.

### 1. Tênis Nike Air Jordan 1 Low Og Sp x Travis Scott Mocha — 40
- SKU: `CQ4277001`
- Última venda/pedido: `2026-02-20T22:35:33+00:00`
- 120d Shopify: 6 un · R$ 131999.94
- Sinal Shopify estoque: `0`
- Tiny snapshot: `None`
- Status: `candidate_stockout_signal_shopify_inventory_needs_tiny_live_confirmation`
- Próximo seguro: `tiny_live_stock_confirmation_before_any_marketplace_or_supplier_step`

### 2. Tênis Onitsuka Tiger Mexico 66 SD Cream Birch Bege — 38
- SKU: `1183C015101`
- Última venda/pedido: `2026-04-01T21:28:22+00:00`
- 120d Shopify: 48 un · R$ 119999.52
- Sinal Shopify estoque: `-1`
- Tiny snapshot: `0.0`
- Status: `candidate_stockout_confirmed_by_local_tiny_anchor_snapshot`
- Próximo seguro: `prepare_droper_first_lookup_preview_only_if_lucas_approves_external_marketplace_lookup`

### 3. Tênis Onitsuka Tiger Mexico 66 SD Cream Birch Bege — 37
- SKU: `1183C015101`
- Última venda/pedido: `2026-03-10T18:14:29+00:00`
- 120d Shopify: 48 un · R$ 119999.52
- Sinal Shopify estoque: `0`
- Tiny snapshot: `0.0`
- Status: `candidate_stockout_confirmed_by_local_tiny_anchor_snapshot`
- Próximo seguro: `prepare_droper_first_lookup_preview_only_if_lucas_approves_external_marketplace_lookup`

### 4. Tênis Nike Air Jordan 1 Low SE Gs "Gold Toe" Preto — 37
- SKU: `DR6970071`
- Última venda/pedido: `2026-02-11T13:25:46+00:00`
- 120d Shopify: 42 un · R$ 83999.58
- Sinal Shopify estoque: `-7`
- Tiny snapshot: `None`
- Status: `candidate_stockout_signal_shopify_inventory_needs_tiny_live_confirmation`
- Próximo seguro: `tiny_live_stock_confirmation_before_any_marketplace_or_supplier_step`

### 5. Tênis Onitsuka Tiger Mexico 66 SD Cream Birch Bege — 35
- SKU: `1183C015101`
- Última venda/pedido: `2026-04-02T15:13:54+00:00`
- 120d Shopify: 30 un · R$ 74999.7
- Sinal Shopify estoque: `0`
- Tiny snapshot: `0.0`
- Status: `candidate_stockout_confirmed_by_local_tiny_anchor_snapshot`
- Próximo seguro: `prepare_droper_first_lookup_preview_only_if_lucas_approves_external_marketplace_lookup`

### 6. Tênis Nike Air Jordan 1 Retro High OG 'UNC Reimagined' Azul — 43
- SKU: `dz5485-402`
- Última venda/pedido: `2026-03-07T18:21:06+00:00`
- 120d Shopify: 12 un · R$ 32399.88
- Sinal Shopify estoque: `0`
- Tiny snapshot: `None`
- Status: `candidate_stockout_signal_shopify_inventory_needs_tiny_live_confirmation`
- Próximo seguro: `tiny_live_stock_confirmation_before_any_marketplace_or_supplier_step`

### 7. Tênis New Balance 204L Mushroom Arid Stone Marrom — 38
- SKU: `U204LMMA-5`
- Última venda/pedido: `2026-04-16T01:29:58+00:00`
- 120d Shopify: 11 un · R$ 30799.89
- Sinal Shopify estoque: `0`
- Tiny snapshot: `4.0`
- Status: `candidate_stockout_signal_shopify_inventory_needs_tiny_live_confirmation`
- Próximo seguro: `tiny_live_stock_confirmation_before_any_marketplace_or_supplier_step`

### 8. Tênis Onitsuka Tiger Mexico 66 SD Cream Birch Bege — 34
- SKU: `1183C015101`
- Última venda/pedido: `2026-03-04T19:00:53+00:00`
- 120d Shopify: 12 un · R$ 29999.88
- Sinal Shopify estoque: `-1`
- Tiny snapshot: `0.0`
- Status: `candidate_stockout_confirmed_by_local_tiny_anchor_snapshot`
- Próximo seguro: `prepare_droper_first_lookup_preview_only_if_lucas_approves_external_marketplace_lookup`

### 9. Tênis Onitsuka Tiger Mexico 66 SD Cream Birch Bege — 36
- SKU: `1183C015101`
- Última venda/pedido: `2026-01-31T18:20:58+00:00`
- 120d Shopify: 12 un · R$ 29999.88
- Sinal Shopify estoque: `-1`
- Tiny snapshot: `0.0`
- Status: `candidate_stockout_confirmed_by_local_tiny_anchor_snapshot`
- Próximo seguro: `prepare_droper_first_lookup_preview_only_if_lucas_approves_external_marketplace_lookup`

### 10. Tênis New Balance 530 Silver White Branco — 38
- SKU: `MR530EMA`
- Última venda/pedido: `2026-02-18T11:48:06+00:00`
- 120d Shopify: 15 un · R$ 29999.85
- Sinal Shopify estoque: `-4`
- Tiny snapshot: `None`
- Status: `candidate_stockout_signal_shopify_inventory_needs_tiny_live_confirmation`
- Próximo seguro: `tiny_live_stock_confirmation_before_any_marketplace_or_supplier_step`

## Não executado

- whatsapp_message_read
- whatsapp_send
- supplier_contact
- purchase
- reservation
- notion_write
- shopify_write
- tiny_write
- merchant_write_beyond_existing_p2a_process
- droper_lookup
- stockx_lookup
- goat_lookup
- klaviyo_send_or_schedule
- customer_contact
