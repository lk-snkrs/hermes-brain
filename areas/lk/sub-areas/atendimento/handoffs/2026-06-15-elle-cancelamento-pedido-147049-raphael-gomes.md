---
type: handoff
area: lk/atendimento
source: telegram_lucas
created_at_utc: 2026-06-15T13:44:32+00:00
created_at_brt: 2026-06-15 10:44:32 -03
conversation: Chatwoot #1197 / LK WhatsApp
customer_name: Raphael Gomes
order_number: "147049"
labels_observed: [financeiro, humano, troca_devolucao, whatsapp-api]
external_write: false
---

# Handoff: correção Elle — cancelamento/reembolso pedido #147049

## Contexto observado
- Cliente Raphael Gomes pediu cancelamento do pedido e reembolso.
- Elle respondeu pedindo número do pedido e motivo da troca/devolução.
- Cliente enviou `#147049`.
- Sidebar Chatwoot indica último pedido `#147049`, pago, valor R$899,99, data 2026-04-15.
- Lucas corrigiu que Elle deveria reconhecer o número recebido e transferir para Larissa.
- Produto informado por Lucas para a resposta: Camiseta Lululemon Swiftly Tech 2.0 Hip Length, Lavender Frost, tamanho S/P.

## Resposta correta sugerida
"Perfeito, Raphael. Recebi o número do seu pedido, #147049, referente à Camiseta Lululemon Swiftly Tech 2.0 Hip Length, Lavender Frost, tamanho S/P. Vou transferir sua conversa para a Larissa para ela dar sequência com o cancelamento e reembolso, ok?"

## Regra Elle a corrigir
Quando o cliente já enviou o número do pedido em continuação a um pedido sensível de cancelamento, reembolso, troca ou devolução:
1. Não pedir novamente o número do pedido.
2. Reconhecer o número recebido.
3. Se houver contexto Shopify no Chatwoot, citar produto/variante apenas como referência, sem prometer decisão financeira.
4. Encaminhar para Larissa/humano para decisão e próximos passos.
5. Aplicar/garantir labels de `financeiro`, `humano` e categoria correspondente, mas não enviar decisão final automática.

## Observação de segurança
Cancelamento/reembolso é caso sensível financeiro. Elle pode acolher e transferir, mas não deve confirmar cancelamento, prazo de estorno, aprovação de reembolso ou qualquer decisão final sem humano/fonte aprovada.
