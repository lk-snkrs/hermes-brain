# LK OS — Ranking stockout/recompra + preflight Notion/Júlio

Generated at: `2026-05-14T00:59:03.567846+00:00`
Status: `ranking_and_notion_pattern_preflight_ready_v2_deduped`

## Veredito

Preflight paralelo concluído em modo local/read-only. A janela usada é 120 dias (~4 meses), como Lucas aprovou. O item 2 foi ajustado para espelhar o padrão existente LK Compras → Júlio/Notion, sem inventar fluxo novo.

Correção de qualidade aplicada: vendas foram agregadas antes de cruzar com Tiny/variants para não duplicar receita/unidades quando um SKU de modelo aparece em múltiplos tamanhos.

## Padrão aprendido para item 2

- Pedido de compra / recompra nasce de demanda concreta e stockout.
- Coleta respostas/disponibilidade/preço/logística.
- Decisão humana escolhe menor preço viável ou fonte mais perto de São Paulo quando a diferença for pequena.
- Compra/logística continuam humanas.
- Notion é log/registro da compra depois; Hermes não escreve sem aprovação.

## Sanity check Tiny/local

- sales_groups_120d_with_sku: 872
- candidate_rows: 647
- tiny_confirmed_zero_any_size: 38
- tiny_exact_size_zero: 18
- tiny_zero_but_size_ambiguous_or_mismatch: 20
- shopify_zero_needs_tiny_confirmation: 609
- shared_sku_across_multiple_shopify_variants: 35
- active_products: 610

## Top candidatos — preview sem PII

### 1. Tênis New Balance 204L Arid Timberwolf Bege — 37
- SKU: `U204LMMC-4` · sku_variant_count: `1`
- Score: `126.0`
- Última venda: `2026-04-01T17:57:20+00:00`
- Demanda 4 meses Shopify: 8 un · R$ 22399.92
- Estoque Shopify sinal: `0`
- Tiny snapshot: `0.0` · tiny_size `37` · tiny_match_count_sku `1` · status `zero_stock`
- Sanity: `tiny_zero_exact_size_ready_for_droper_preview_after_gmc`
- Preview Júlio/Notion padrão: `pedido_de_recompra_por_stockout` → Droper primeiro → StockX/GOAT fallback → decisão humana preço/logística → log Notion.

### 2. Tênis Onitsuka Tiger Mexico 66 White Black Branco — 38
- SKU: `1183A201-126-5` · sku_variant_count: `1`
- Score: `122.0`
- Última venda: `2026-03-30T17:54:03+00:00`
- Demanda 4 meses Shopify: 6 un · R$ 14399.94
- Estoque Shopify sinal: `-1`
- Tiny snapshot: `0.0` · tiny_size `38` · tiny_match_count_sku `1` · status `zero_stock`
- Sanity: `tiny_zero_exact_size_ready_for_droper_preview_after_gmc`
- Preview Júlio/Notion padrão: `pedido_de_recompra_por_stockout` → Droper primeiro → StockX/GOAT fallback → decisão humana preço/logística → log Notion.

### 3. Tênis Onitsuka Tiger Mexico 66 White Black Branco — 37
- SKU: `1183A201-126-4` · sku_variant_count: `1`
- Score: `120.0`
- Última venda: `2026-04-08T00:41:47+00:00`
- Demanda 4 meses Shopify: 5 un · R$ 11999.95
- Estoque Shopify sinal: `-2`
- Tiny snapshot: `0.0` · tiny_size `37` · tiny_match_count_sku `1` · status `zero_stock`
- Sanity: `tiny_zero_exact_size_ready_for_droper_preview_after_gmc`
- Preview Júlio/Notion padrão: `pedido_de_recompra_por_stockout` → Droper primeiro → StockX/GOAT fallback → decisão humana preço/logística → log Notion.

### 4. Tênis New Balance 204L Arid Timberwolf Bege — 39
- SKU: `U204LMMC-6` · sku_variant_count: `1`
- Score: `116.0`
- Última venda: `2026-03-12T16:36:11+00:00`
- Demanda 4 meses Shopify: 7 un · R$ 19599.93
- Estoque Shopify sinal: `3`
- Tiny snapshot: `0.0` · tiny_size `39` · tiny_match_count_sku `1` · status `not_mapped`
- Sanity: `tiny_zero_exact_size_ready_for_droper_preview_after_gmc`
- Preview Júlio/Notion padrão: `pedido_de_recompra_por_stockout` → Droper primeiro → StockX/GOAT fallback → decisão humana preço/logística → log Notion.

### 5. Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo — 41.5
- SKU: `1183C102.751` · sku_variant_count: `0`
- Score: `112.82`
- Última venda: `2026-04-05T19:03:35+00:00`
- Demanda 4 meses Shopify: 4 un · R$ 9599.96
- Estoque Shopify sinal: `-1`
- Tiny snapshot: `0.0` · tiny_size `41.5` · tiny_match_count_sku `1` · status `not_mapped`
- Sanity: `tiny_zero_exact_size_ready_for_droper_preview_after_gmc`
- Preview Júlio/Notion padrão: `pedido_de_recompra_por_stockout` → Droper primeiro → StockX/GOAT fallback → decisão humana preço/logística → log Notion.

### 6. Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo — 36
- SKU: `HV8547-700-3` · sku_variant_count: `1`
- Score: `112.0`
- Última venda: `2026-03-23T15:39:21+00:00`
- Demanda 4 meses Shopify: 3 un · R$ 15999.97
- Estoque Shopify sinal: `0`
- Tiny snapshot: `0.0` · tiny_size `36` · tiny_match_count_sku `1` · status `not_mapped`
- Sanity: `tiny_zero_exact_size_ready_for_droper_preview_after_gmc`
- Preview Júlio/Notion padrão: `pedido_de_recompra_por_stockout` → Droper primeiro → StockX/GOAT fallback → decisão humana preço/logística → log Notion.

### 7. Tênis Onitsuka Tiger Mexico 66 White Black Branco — 36
- SKU: `1183A201-126-3` · sku_variant_count: `1`
- Score: `110.57`
- Última venda: `2026-02-24T18:56:34+00:00`
- Demanda 4 meses Shopify: 3 un · R$ 7199.97
- Estoque Shopify sinal: `0`
- Tiny snapshot: `0.0` · tiny_size `36` · tiny_match_count_sku `1` · status `not_mapped`
- Sanity: `tiny_zero_exact_size_ready_for_droper_preview_after_gmc`
- Preview Júlio/Notion padrão: `pedido_de_recompra_por_stockout` → Droper primeiro → StockX/GOAT fallback → decisão humana preço/logística → log Notion.

### 8. Tênis Onitsuka Tiger Mexico 66 White Black Branco — 40
- SKU: `1183A201-126-7` · sku_variant_count: `1`
- Score: `110.57`
- Última venda: `2026-04-07T09:47:14+00:00`
- Demanda 4 meses Shopify: 3 un · R$ 7199.97
- Estoque Shopify sinal: `-2`
- Tiny snapshot: `0.0` · tiny_size `40` · tiny_match_count_sku `1` · status `zero_stock`
- Sanity: `tiny_zero_exact_size_ready_for_droper_preview_after_gmc`
- Preview Júlio/Notion padrão: `pedido_de_recompra_por_stockout` → Droper primeiro → StockX/GOAT fallback → decisão humana preço/logística → log Notion.

### 9. Tênis Adidas Samba OG Crochet Pack Sand Strata Bege — 36
- SKU: `JR9446-3` · sku_variant_count: `1`
- Score: `110.2`
- Última venda: `2026-03-18T18:55:27+00:00`
- Demanda 4 meses Shopify: 3 un · R$ 6599.97
- Estoque Shopify sinal: `-1`
- Tiny snapshot: `0.0` · tiny_size `36` · tiny_match_count_sku `1` · status `zero_stock`
- Sanity: `tiny_zero_exact_size_ready_for_droper_preview_after_gmc`
- Preview Júlio/Notion padrão: `pedido_de_recompra_por_stockout` → Droper primeiro → StockX/GOAT fallback → decisão humana preço/logística → log Notion.

### 10. Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo — 38
- SKU: `HV8547-700-5` · sku_variant_count: `1`
- Score: `108.0`
- Última venda: `2026-04-11T13:36:45+00:00`
- Demanda 4 meses Shopify: 4 un · R$ 23999.96
- Estoque Shopify sinal: `3`
- Tiny snapshot: `0.0` · tiny_size `38` · tiny_match_count_sku `1` · status `not_mapped`
- Sanity: `tiny_zero_exact_size_ready_for_droper_preview_after_gmc`
- Preview Júlio/Notion padrão: `pedido_de_recompra_por_stockout` → Droper primeiro → StockX/GOAT fallback → decisão humana preço/logística → log Notion.

### 11. Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo — 37
- SKU: `HV8547-700-4` · sku_variant_count: `1`
- Score: `108.0`
- Última venda: `2026-03-04T14:35:33+00:00`
- Demanda 4 meses Shopify: 4 un · R$ 19999.96
- Estoque Shopify sinal: `2`
- Tiny snapshot: `0.0` · tiny_size `37` · tiny_match_count_sku `1` · status `not_mapped`
- Sanity: `tiny_zero_exact_size_ready_for_droper_preview_after_gmc`
- Preview Júlio/Notion padrão: `pedido_de_recompra_por_stockout` → Droper primeiro → StockX/GOAT fallback → decisão humana preço/logística → log Notion.

### 12. Tênis Onitsuka Tiger Mexico 66 SD Cream Birch Bege — 37
- SKU: `1183C015101` · sku_variant_count: `0`
- Score: `108.0`
- Última venda: `2026-03-10T18:14:29+00:00`
- Demanda 4 meses Shopify: 8 un · R$ 19999.92
- Estoque Shopify sinal: `0`
- Tiny snapshot: `0.0` · tiny_size `42.5` · tiny_match_count_sku `6` · status `zero_stock`
- Sanity: `tiny_zero_but_size_ambiguous_or_mismatch_needs_manual_sanity_before_droper`
- Preview Júlio/Notion padrão: `pedido_de_recompra_por_stockout` → Droper primeiro → StockX/GOAT fallback → decisão humana preço/logística → log Notion.

### 13. Tênis Onitsuka Tiger Mexico 66 SD Cream Birch Bege — 38
- SKU: `1183C015101` · sku_variant_count: `0`
- Score: `108.0`
- Última venda: `2026-04-01T21:28:22+00:00`
- Demanda 4 meses Shopify: 8 un · R$ 19999.92
- Estoque Shopify sinal: `-1`
- Tiny snapshot: `0.0` · tiny_size `42.5` · tiny_match_count_sku `6` · status `zero_stock`
- Sanity: `tiny_zero_but_size_ambiguous_or_mismatch_needs_manual_sanity_before_droper`
- Preview Júlio/Notion padrão: `pedido_de_recompra_por_stockout` → Droper primeiro → StockX/GOAT fallback → decisão humana preço/logística → log Notion.

### 14. Tênis Adidas Samba OG Crochet Pack Sand Strata Bege — 35
- SKU: `JR9446-2` · sku_variant_count: `1`
- Score: `107.44`
- Última venda: `2026-03-17T20:09:07+00:00`
- Demanda 4 meses Shopify: 4 un · R$ 8799.96
- Estoque Shopify sinal: `3`
- Tiny snapshot: `0.0` · tiny_size `35` · tiny_match_count_sku `1` · status `zero_stock`
- Sanity: `tiny_zero_exact_size_ready_for_droper_preview_after_gmc`
- Preview Júlio/Notion padrão: `pedido_de_recompra_por_stockout` → Droper primeiro → StockX/GOAT fallback → decisão humana preço/logística → log Notion.

### 15. Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo — 37
- SKU: `1183C102.751` · sku_variant_count: `0`
- Score: `104.0`
- Última venda: `2026-03-27T13:28:07+00:00`
- Demanda 4 meses Shopify: 6 un · R$ 14399.94
- Estoque Shopify sinal: `-2`
- Tiny snapshot: `0.0` · tiny_size `41.5` · tiny_match_count_sku `1` · status `not_mapped`
- Sanity: `tiny_zero_but_size_ambiguous_or_mismatch_needs_manual_sanity_before_droper`
- Preview Júlio/Notion padrão: `pedido_de_recompra_por_stockout` → Droper primeiro → StockX/GOAT fallback → decisão humana preço/logística → log Notion.

### 16. Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo — 39
- SKU: `1183C102.751` · sku_variant_count: `0`
- Score: `104.0`
- Última venda: `2026-03-27T16:18:16+00:00`
- Demanda 4 meses Shopify: 6 un · R$ 14399.94
- Estoque Shopify sinal: `0`
- Tiny snapshot: `0.0` · tiny_size `41.5` · tiny_match_count_sku `1` · status `not_mapped`
- Sanity: `tiny_zero_but_size_ambiguous_or_mismatch_needs_manual_sanity_before_droper`
- Preview Júlio/Notion padrão: `pedido_de_recompra_por_stockout` → Droper primeiro → StockX/GOAT fallback → decisão humana preço/logística → log Notion.

### 17. Tênis New Balance 204L Arid Timberwolf Bege — 38
- SKU: `U204LMMC-5` · sku_variant_count: `1`
- Score: `103.24`
- Última venda: `2026-04-06T21:13:30+00:00`
- Demanda 4 meses Shopify: 3 un · R$ 8399.97
- Estoque Shopify sinal: `1`
- Tiny snapshot: `0.0` · tiny_size `38` · tiny_match_count_sku `1` · status `not_mapped`
- Sanity: `tiny_zero_exact_size_ready_for_droper_preview_after_gmc`
- Preview Júlio/Notion padrão: `pedido_de_recompra_por_stockout` → Droper primeiro → StockX/GOAT fallback → decisão humana preço/logística → log Notion.

### 18. Tênis New Balance 204L Arid Timberwolf Bege — 40
- SKU: `U204LMMC-7` · sku_variant_count: `1`
- Score: `103.24`
- Última venda: `2026-03-21T20:42:15+00:00`
- Demanda 4 meses Shopify: 3 un · R$ 8399.97
- Estoque Shopify sinal: `1`
- Tiny snapshot: `0.0` · tiny_size `40` · tiny_match_count_sku `1` · status `not_mapped`
- Sanity: `tiny_zero_exact_size_ready_for_droper_preview_after_gmc`
- Preview Júlio/Notion padrão: `pedido_de_recompra_por_stockout` → Droper primeiro → StockX/GOAT fallback → decisão humana preço/logística → log Notion.

## Não executado

- droper_lookup
- stockx_lookup
- goat_lookup
- whatsapp_read
- whatsapp_send
- supplier_contact
- purchase
- reservation
- payment
- notion_write
- shopify_write
- tiny_write
- merchant_write
- campaign_or_customer_contact
