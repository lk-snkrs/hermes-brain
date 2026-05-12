# LK needs_data autofix read-only, 2026-05-12

Generated at: `2026-05-12T01:32:53.602897+00:00`

## Veredito

Lucas autorizou que bloqueios `needs_data` de dados sejam buscados e corrigidos autonomamente quando o trabalho for lookup/reconciliação read-only/local. Este run aplicou essa regra, sem ação externa.

## Resumo

- Itens checados: 3
- Saíram de `needs_data` para decisão/cotação interna: 0
- Saíram de `needs_data` para monitor/estoque OK: 2
- Precisam só de higiene interna de código: 1
- Permanecem em follow-up interno de dados: 0
- Shopify reads: 3
- Tiny searches/details/stock reads: 20
- Writes/envios/compras/marketplace/n8n: 0/0/0/0/0

## Resultado por item

### Bearbrick Series 48 — `MED-3410398-OS`
- Produto: MEDICOM TOY - Bearbrick Series 48 100% Toy Art Blind Box (Lacrado)
- Tamanho: sem tamanho informado
- Venda Shopify: 3 un., R$ 449,97
- Status: `resolved_out_of_stock_code_hygiene_needed`
- Rota: `internal_code_hygiene_then_decision`
- LK | CONTROLE ESTOQUE conhecido: False
- Saldo LK reconciliado: None
- Saldo Tiny total conhecido: True
- Saldo Tiny total: 0.0
- Match exato de produto: 1
- Match exato de código: 0
- Próxima quantidade de cotação segura: 0 (referência, não compra)
- Motivo: Exact product was found with zero stock but Tiny codigo is blank; prepare internal code hygiene before external sourcing.

### Onitsuka Tiger Mexico 66 — `1183C102751-3`
- Produto: Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo
- Tamanho: 36
- Venda Shopify: 2 un., R$ 4.799,98
- Status: `resolved_in_stock_no_sourcing_needed`
- Rota: `move_from_needs_data_to_monitor_or_stock_ok`
- LK | CONTROLE ESTOQUE conhecido: False
- Saldo LK reconciliado: None
- Saldo Tiny total conhecido: True
- Saldo Tiny total: 5.0
- Match exato de produto: 1
- Match exato de código: 1
- Próxima quantidade de cotação segura: 0 (referência, não compra)
- Motivo: Shopify/Tiny SKU mapping is resolved and stock exists; no quote/sourcing needed now.

### Camiseta Saint Studio Boxy — `SST-6502622-M`
- Produto: Camiseta Saint Studio Boxy Supima Breuer Preto
- Tamanho: M/M
- Venda Shopify: 2 un., R$ 619,98
- Status: `resolved_product_stock_ok_tiny_code_missing`
- Rota: `move_from_needs_data_to_monitor_or_stock_ok`
- LK | CONTROLE ESTOQUE conhecido: True
- Saldo LK reconciliado: 2.0
- Saldo Tiny total conhecido: True
- Saldo Tiny total: 2.0
- Match exato de produto: 1
- Match exato de código: 0
- Próxima quantidade de cotação segura: 0 (referência, não compra)
- Motivo: Exact product/size was found in Tiny and stock exists; Tiny codigo remains a hygiene issue but not a sourcing blocker.

## Não executado

- shopify_write
- tiny_write
- merchant_feed_write
- gsc_admin_or_indexing_submit
- klaviyo_send_or_schedule
- customer_contact
- supplier_contact
- external_marketplace_lookup
- purchase
- purchase_order
- reservation
- price_or_stock_change
- campaign_or_external_send
- n8n_flow_creation
