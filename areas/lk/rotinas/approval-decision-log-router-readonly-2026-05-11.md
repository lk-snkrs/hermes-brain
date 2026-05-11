# LK OS, Approval Decision Log + Router read-only, 2026-05-11

Generated at: `2026-05-11T20:02:57.717793+00:00`
Week: `2026-05-04` to `2026-05-10`

## Escopo

Registro operacional das decisões pendentes. Serve para Lucas/Júlio aprovar, rejeitar ou pedir dados sem misturar isso com execução externa.

## Resumo

- Decisões registradas: 8
- Needs approval: 5
- Needs data: 3
- Quantidade referência cotação, não compra: 26
- Sinal receita Shopify: R$ 89.669,71

## Router

### LK-QUOTE-20260504-20260510-01 | Nike Moon Shoe SP Jacquemus
- Status atual: `needs_approval`
- Rota: `awaiting_lucas_or_julio_approval`
- Próximo ator: Lucas/Júlio
- Default seguro: `approve_quote_only`
- Ação bloqueada: `supplier_contact`
- Se aprovado: `prepare_supplier_send_preview_with_named_destination`
- Se rejeitado/segurar: `mark_rejected_keep_no_action`
- Quantidade referência cotação: 10
- Receita Shopify sinal: R$ 48.999,92

### LK-QUOTE-20260504-20260510-02 | New Balance 9060
- Status atual: `needs_approval`
- Rota: `awaiting_lucas_or_julio_approval`
- Próximo ator: Lucas/Júlio
- Default seguro: `approve_quote_only`
- Ação bloqueada: `supplier_contact`
- Se aprovado: `prepare_supplier_send_preview_with_named_destination`
- Se rejeitado/segurar: `mark_rejected_keep_no_action`
- Quantidade referência cotação: 8
- Receita Shopify sinal: R$ 18.799,93

### LK-QUOTE-20260504-20260510-03 | Nike Mind 002
- Status atual: `needs_approval`
- Rota: `awaiting_lucas_or_julio_approval`
- Próximo ator: Lucas/Júlio
- Default seguro: `approve_quote_only`
- Ação bloqueada: `supplier_contact`
- Se aprovado: `prepare_supplier_send_preview_with_named_destination`
- Se rejeitado/segurar: `mark_rejected_keep_no_action`
- Quantidade referência cotação: 3
- Receita Shopify sinal: R$ 6.399,98

### LK-QUOTE-20260504-20260510-04 | Comme des Garçons PLAY Polo
- Status atual: `needs_approval`
- Rota: `awaiting_lucas_or_julio_approval`
- Próximo ator: Lucas/Júlio
- Default seguro: `approve_quote_only`
- Ação bloqueada: `supplier_contact`
- Se aprovado: `prepare_supplier_send_preview_with_named_destination`
- Se rejeitado/segurar: `mark_rejected_keep_no_action`
- Quantidade referência cotação: 3
- Receita Shopify sinal: R$ 3.599,98

### LK-QUOTE-20260504-20260510-05 | New Balance 530
- Status atual: `needs_approval`
- Rota: `hold_or_bundle_with_p0_decision`
- Próximo ator: Lucas/Júlio
- Default seguro: `hold_or_bundle_with_p0`
- Ação bloqueada: `supplier_contact`
- Se aprovado: `bundle_in_existing_p0_quote_preview_only`
- Se rejeitado/segurar: `hold_monitor_weekly`
- Quantidade referência cotação: 2
- Receita Shopify sinal: R$ 5.999,97

### LK-QUOTE-20260504-20260510-06 | Onitsuka Tiger Mexico 66
- Status atual: `needs_data`
- Rota: `needs_data_before_approval`
- Próximo ator: Hermes/LK ops data cleanup
- Default seguro: `needs_data`
- Ação bloqueada: `supplier_contact_and_purchase`
- Se aprovado: `not_applicable_until_data_resolved`
- Se rejeitado/segurar: `keep_needs_data`
- Quantidade referência cotação: 0
- Receita Shopify sinal: R$ 4.799,98

### LK-QUOTE-20260504-20260510-07 | Camiseta Saint Studio Boxy
- Status atual: `needs_data`
- Rota: `needs_data_before_approval`
- Próximo ator: Hermes/LK ops data cleanup
- Default seguro: `needs_data`
- Ação bloqueada: `supplier_contact_and_purchase`
- Se aprovado: `not_applicable_until_data_resolved`
- Se rejeitado/segurar: `keep_needs_data`
- Quantidade referência cotação: 0
- Receita Shopify sinal: R$ 619,98

### LK-QUOTE-20260504-20260510-08 | Bearbrick Series 48
- Status atual: `needs_data`
- Rota: `needs_data_before_approval`
- Próximo ator: Hermes/LK ops data cleanup
- Default seguro: `needs_data`
- Ação bloqueada: `supplier_contact_and_purchase`
- Se aprovado: `not_applicable_until_data_resolved`
- Se rejeitado/segurar: `keep_needs_data`
- Quantidade referência cotação: 0
- Receita Shopify sinal: R$ 449,97

## O que não foi feito

- Nenhuma decisão foi marcada como aprovada pelo Lucas/Júlio.
- Nenhum fornecedor foi contatado.
- Nenhuma mensagem externa foi enviada.
- Nenhuma compra, PO, reserva, pagamento, Shopify/Tiny write, preço, estoque, campanha, cliente, banco de produção ou cron foi executado.

## Como usar depois

Quando Lucas/Júlio aprovar uma linha, registrar `manual_decision_value` e só então preparar um preview de envio com fornecedor/destino explícito. Mesmo depois da cotação, compra e PO continuam exigindo nova aprovação.
