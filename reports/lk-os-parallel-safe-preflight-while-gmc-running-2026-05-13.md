# LK OS — Preflight paralelo seguro enquanto GMC roda

Generated at: `2026-05-14T00:39:50.922834+00:00`

## Veredito
Sim: dá para preparar o Step 2 em modo local/read-only sem concorrer com o GMC. Este relatório não consulta Droper/StockX/GOAT e não executa contato/compra/write.

## Prontidão das tabelas
- lk_orders: exists=True; rows=6059
- lk_order_items: exists=True; rows=8166
- lk_product_variants: exists=True; rows=14466
- lk_products: exists=True; rows=2241
- tiny_anchor_stock: exists=True; rows=49

## Contagens úteis
- recent_paid_items_120d_with_sku: 1446
- distinct_skus_recent_120d: 752
- recent_skus_shopify_zero_signal: 553
- recent_skus_tiny_zero_snapshot: 18

## Amostra provisória sem PII — top candidatos para validação após GMC
### 1. Tênis Nike Air Jordan 1 Low Og Sp x Travis Scott Mocha — 40
- SKU: `CQ4277001`
- Última venda: `2026-02-20T22:35:33+00:00`
- 120d: 6 un · R$ 131999.94
- Shopify estoque sinal: `0`
- Tiny snapshot: `None`
- Status provisório: `needs_tiny_confirmation_after_gmc_final`

### 2. Tênis Onitsuka Tiger Mexico 66 SD Cream Birch Bege — 38
- SKU: `1183C015101`
- Última venda: `2026-04-01T21:28:22+00:00`
- 120d: 48 un · R$ 119999.52
- Shopify estoque sinal: `-1`
- Tiny snapshot: `0.0`
- Status provisório: `ready_for_step2_after_gmc_final`

### 3. Tênis Onitsuka Tiger Mexico 66 SD Cream Birch Bege — 37
- SKU: `1183C015101`
- Última venda: `2026-03-10T18:14:29+00:00`
- 120d: 48 un · R$ 119999.52
- Shopify estoque sinal: `0`
- Tiny snapshot: `0.0`
- Status provisório: `ready_for_step2_after_gmc_final`

### 4. Tênis Nike Air Jordan 1 Low SE Gs "Gold Toe" Preto — 37
- SKU: `DR6970071`
- Última venda: `2026-02-11T13:25:46+00:00`
- 120d: 42 un · R$ 83999.58
- Shopify estoque sinal: `-7`
- Tiny snapshot: `None`
- Status provisório: `needs_tiny_confirmation_after_gmc_final`

### 5. Tênis Onitsuka Tiger Mexico 66 SD Cream Birch Bege — 35
- SKU: `1183C015101`
- Última venda: `2026-04-02T15:13:54+00:00`
- 120d: 30 un · R$ 74999.7
- Shopify estoque sinal: `0`
- Tiny snapshot: `0.0`
- Status provisório: `ready_for_step2_after_gmc_final`

### 6. Tênis Nike Air Jordan 1 Retro High OG 'UNC Reimagined' Azul — 43
- SKU: `dz5485-402`
- Última venda: `2026-03-07T18:21:06+00:00`
- 120d: 12 un · R$ 32399.88
- Shopify estoque sinal: `0`
- Tiny snapshot: `None`
- Status provisório: `needs_tiny_confirmation_after_gmc_final`

### 7. Tênis New Balance 204L Mushroom Arid Stone Marrom — 38
- SKU: `U204LMMA-5`
- Última venda: `2026-04-16T01:29:58+00:00`
- 120d: 11 un · R$ 30799.89
- Shopify estoque sinal: `0`
- Tiny snapshot: `4.0`
- Status provisório: `needs_tiny_confirmation_after_gmc_final`

### 8. Tênis Onitsuka Tiger Mexico 66 SD Cream Birch Bege — 34
- SKU: `1183C015101`
- Última venda: `2026-03-04T19:00:53+00:00`
- 120d: 12 un · R$ 29999.88
- Shopify estoque sinal: `-1`
- Tiny snapshot: `0.0`
- Status provisório: `ready_for_step2_after_gmc_final`

### 9. Tênis Onitsuka Tiger Mexico 66 SD Cream Birch Bege — 36
- SKU: `1183C015101`
- Última venda: `2026-01-31T18:20:58+00:00`
- 120d: 12 un · R$ 29999.88
- Shopify estoque sinal: `-1`
- Tiny snapshot: `0.0`
- Status provisório: `ready_for_step2_after_gmc_final`

### 10. Tênis New Balance 530 Silver White Branco — 38
- SKU: `MR530EMA`
- Última venda: `2026-02-18T11:48:06+00:00`
- 120d: 15 un · R$ 29999.85
- Shopify estoque sinal: `-4`
- Tiny snapshot: `None`
- Status provisório: `needs_tiny_confirmation_after_gmc_final`

## Não executado
- no_gmc_new_write
- no_droper_lookup
- no_stockx_lookup
- no_goat_lookup
- no_whatsapp_read_send
- no_supplier_contact
- no_purchase
- no_notion_write
- no_shopify_tiny_write
