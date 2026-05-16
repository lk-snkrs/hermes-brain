# LK OS — Next Decision Queue, 2026-05-12

Generated at: `2026-05-13T06:33:15.022953+00:00`

## Veredito

Fila executiva pronta em modo local/read-only. Ela consolida o próximo bloco do LK OS sem tocar em Merchant, Tiny, Shopify, Klaviyo, fornecedor, cliente, compra, marketplace, banco, POS ou n8n.

## Resumo

- Itens na fila: 10
- Itens que exigem aprovação atual antes de execução externa/write: 7
- Sourcing/cotação P1 aprováveis: 4
- Contagens por lane: `{'google_feed_availability': 1, 'sourcing_quote_approval': 5, 'crm_gate': 1, 'internal_code_hygiene': 1, 'data_resolved_monitor': 2}`
- Contagens por prioridade: `{'P1': 9, 'P2': 1}`

## Top fila

### 1. P1 · google_feed_availability · GMC P1-B availability via Tiny
- Decisão: Aguardar packet Tiny read-only finalizar; só aprovar availability para IDs ready com Tiny OK.
- Recomendado: `wait_packet_completion`
- Fonte/valor: fact_tiny_stock_pending+manual_approval_required · —
- Próximo seguro: Monitorar processo P1-B; preparar approval packet final quando houver contadores finais.
- Bloqueado até aprovação: Merchant availability write; Tiny/Shopify/feed/DB/POS/campaign writes
- Source: `reports/lk-gmc-2026-05-12-p1-availability-tiny-packet-running-status-2039.md`

### 2. P1 · sourcing_quote_approval · Nike Moon Shoe SP Jacquemus
- Decisão: Aprovar envio de cotação apenas para disponibilidade, custo e lead time; compra separada depois.
- Recomendado: `approve_quote_only`
- Fonte/valor: fact_shopify+fact_tiny_stock+derived_reconciliation+manual_approval_pending · R$ 48.999,92
- Próximo seguro: prepare_supplier_send_preview_with_named_destination
- Bloqueado até aprovação: purchase, purchase_order, reservation, shopify_write, tiny_write, price_or_stock_change, campaign_or_external_send
- Source: `reports/lk-os-supplier-quote-approval-packet-2026-05-04_2026-05-10.json`

### 3. P1 · sourcing_quote_approval · New Balance 9060
- Decisão: Aprovar envio de cotação apenas para disponibilidade, custo e lead time; compra separada depois.
- Recomendado: `approve_quote_only`
- Fonte/valor: fact_shopify+fact_tiny_stock+derived_reconciliation+manual_approval_pending · R$ 18.799,93
- Próximo seguro: prepare_supplier_send_preview_with_named_destination
- Bloqueado até aprovação: purchase, purchase_order, reservation, shopify_write, tiny_write, price_or_stock_change, campaign_or_external_send
- Source: `reports/lk-os-supplier-quote-approval-packet-2026-05-04_2026-05-10.json`

### 4. P1 · sourcing_quote_approval · Nike Mind 002
- Decisão: Aprovar envio de cotação apenas para disponibilidade, custo e lead time; compra separada depois.
- Recomendado: `approve_quote_only`
- Fonte/valor: fact_shopify+fact_tiny_stock+derived_reconciliation+manual_approval_pending · R$ 6.399,98
- Próximo seguro: prepare_supplier_send_preview_with_named_destination
- Bloqueado até aprovação: purchase, purchase_order, reservation, shopify_write, tiny_write, price_or_stock_change, campaign_or_external_send
- Source: `reports/lk-os-supplier-quote-approval-packet-2026-05-04_2026-05-10.json`

### 5. P1 · sourcing_quote_approval · Comme des Garçons PLAY Polo
- Decisão: Aprovar envio de cotação apenas para disponibilidade, custo e lead time; compra separada depois.
- Recomendado: `approve_quote_only`
- Fonte/valor: fact_shopify+fact_tiny_stock+derived_reconciliation+manual_approval_pending · R$ 3.599,98
- Próximo seguro: prepare_supplier_send_preview_with_named_destination
- Bloqueado até aprovação: purchase, purchase_order, reservation, shopify_write, tiny_write, price_or_stock_change, campaign_or_external_send
- Source: `reports/lk-os-supplier-quote-approval-packet-2026-05-04_2026-05-10.json`

### 6. P1 · crm_gate · Klaviyo P1 draft, loja física recompra
- Decisão: Revisar campanha Draft; envio/agendamento/flow continuam bloqueados.
- Recomendado: `review_only_no_send`
- Fonte/valor: fact_klaviyo_draft+manual_approval_required · —
- Próximo seguro: Lucas review by verified list/template/campaign IDs; prepare send packet only if explicitly requested.
- Bloqueado até aprovação: send, schedule, flow, customer contact
- Source: `reports/lk-phase5-p1-klaviyo-klaviyo-objects-2026-05-11.md`

### 7. P1 · internal_code_hygiene · Bearbrick Series 48
- Decisão: Nenhuma ação externa; manter higiene/monitoramento local conforme evidência.
- Recomendado: `local_readonly_or_monitor`
- Fonte/valor: derived_reconciliation · —
- Próximo seguro: Exact product was found with zero stock but Tiny codigo is blank; prepare internal code hygiene before external sourcing.
- Bloqueado até aprovação: external sourcing/contact/purchase still blocked; local/read-only hygiene allowed
- Source: `reports/lk-needs-data-autofix-readonly-2026-05-12.json`

### 8. P1 · data_resolved_monitor · Onitsuka Tiger Mexico 66
- Decisão: Nenhuma ação externa; manter higiene/monitoramento local conforme evidência.
- Recomendado: `local_readonly_or_monitor`
- Fonte/valor: derived_reconciliation · —
- Próximo seguro: Shopify/Tiny SKU mapping is resolved and stock exists; no quote/sourcing needed now.
- Bloqueado até aprovação: external sourcing/contact/purchase still blocked; local/read-only hygiene allowed
- Source: `reports/lk-needs-data-autofix-readonly-2026-05-12.json`

### 9. P1 · data_resolved_monitor · Camiseta Saint Studio Boxy
- Decisão: Nenhuma ação externa; manter higiene/monitoramento local conforme evidência.
- Recomendado: `local_readonly_or_monitor`
- Fonte/valor: derived_reconciliation · —
- Próximo seguro: Exact product/size was found in Tiny and stock exists; Tiny codigo remains a hygiene issue but not a sourcing blocker.
- Bloqueado até aprovação: external sourcing/contact/purchase still blocked; local/read-only hygiene allowed
- Source: `reports/lk-needs-data-autofix-readonly-2026-05-12.json`

### 10. P2 · sourcing_quote_approval · New Balance 530
- Decisão: Opcional: cotar junto se fornecedor já responder P0; caso contrário manter em observação.
- Recomendado: `hold_or_bundle_with_p0`
- Fonte/valor: fact_shopify+fact_tiny_stock+derived_reconciliation+manual_approval_pending · R$ 5.999,97
- Próximo seguro: bundle_in_existing_p0_quote_preview_only
- Bloqueado até aprovação: purchase, purchase_order, reservation, shopify_write, tiny_write, price_or_stock_change, campaign_or_external_send
- Source: `reports/lk-os-supplier-quote-approval-packet-2026-05-04_2026-05-10.json`

## Não executado

- merchant_write
- tiny_write
- shopify_write
- klaviyo_send_or_schedule
- supplier_contact
- purchase_order
- reservation
- marketplace_lookup
- database_write
- pos_write
- n8n_flow_creation

## Preciso de resposta

1. `Aprovar preparo de preview de cotação P1` — autoriza somente montar mensagens/briefs para fornecedor com destino nomeado depois; ainda não autoriza envio, compra ou reserva.
2. `Revisar Klaviyo Draft` — mantém sem envio/agendamento; só prepara checklist de revisão no painel.
3. `Aguardar GMC P1-B` — recomendada agora: deixa o packet Tiny terminar e depois decide availability com contadores finais.

Recomendado: opção 3 em paralelo com opção 1 como preview local, sem contato externo.
