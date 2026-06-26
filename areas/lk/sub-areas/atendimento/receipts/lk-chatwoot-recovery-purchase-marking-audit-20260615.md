# LK Chatwoot Recovery — auditoria de marcação recovered pós-compra

Data: 2026-06-15
Agente: lk-ops
Área: LK / Atendimento / Chatwoot Recovery
Tipo: read-only audit, sem PII

## Pergunta

Lucas perguntou se o motor está marcando com êxito pessoas que compraram depois do carrinho abandonado.

## Evidência consultada

- Banco Chatwoot production, read-only.
- Tabelas/modelos: `shopify_recovery_checkouts`, `recovery_event_logs`.
- Código live inspecionado no container:
  - `Shopify::CheckoutTrackingService#mark_recovered`
  - `Shopify::AbandonedCheckoutJob#purchased_after_checkout?`
  - `Webhooks::ShopifyController#record_purchase`

## Como o sistema marca recovered

Há dois caminhos:

1. No webhook de pedido Shopify (`orders/create`):
   - registra `RecoveryEventLog` com dedup `purchase:<order_id>`;
   - chama `Shopify::CheckoutTrackingService#mark_recovered`, que tenta casar por `checkout_id` ou `cart_token` e executa `record.mark_recovered!`.
2. No job futuro do carrinho abandonado:
   - antes de enviar novo toque, consulta `RecoveryEventLog` de purchase por e-mail ou telefone criado depois do checkout;
   - se encontrar compra posterior, marca o checkout como `recovered` e não envia mais mensagem.

## Resultado quantitativo sanitizado

Janela 24h:
- Checkouts considerados: 52
- Status recovered: 8
- Com compra posterior detectada por log: 8
- Compra posterior não marcada como recovered: 0
- Recovered sem compra posterior em event log: 0
- Último recovered: 2026-06-15T12:15:28Z

Janela 7d:
- Checkouts considerados: 247
- Status recovered: 45
- Com compra posterior detectada por log: 18
- Compra posterior não marcada como recovered: 0
- Recovered sem compra posterior em event log: 27
- Último recovered: 2026-06-15T12:15:28Z

Janela 30d/all:
- Checkouts totais: 627
- Status counts: pending 533, notified 4, recovered 90
- Com compra posterior detectada por log: 20
- Compra posterior não marcada como recovered: 1
- Recovered sem compra posterior em event log: 71

## Interpretação

- Para a operação recente, sim: compras posteriores estão sendo marcadas corretamente; nas últimas 24h e 7d não apareceu compra posterior não marcada.
- Existe 1 caso legado não marcado: checkout de 2026-05-07, status `notified`, compra posterior detectada em 2026-06-10, `touches_sent=0`. Isso parece anterior/fora do ciclo atual do job e não contradiz a operação recente, mas pode ser reconciliado se Lucas aprovar correção backfill.
- Muitos `recovered` sem compra posterior no `RecoveryEventLog` são esperados porque o caminho principal de `orders/create` também marca por `checkout_id`/`cart_token`; o log de purchase é uma segunda trava para parar cadência por e-mail/telefone.

## Non-actions

- Nenhum dado pessoal impresso.
- Nenhuma escrita no banco.
- Nenhum envio/canary.
- Nenhuma alteração em Shopify/Meta/Klaviyo/WhatsApp.

## Próximo passo sugerido

Se Lucas quiser precisão histórica total, preparar approval packet para backfill pontual/sanitizado do 1 caso legado `notified` com compra posterior, com backup e rollback. Não executar sem aprovação explícita porque é write em produção.
