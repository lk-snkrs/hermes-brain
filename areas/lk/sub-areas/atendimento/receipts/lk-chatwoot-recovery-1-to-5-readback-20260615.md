# LK Chatwoot Recovery — confirmação itens 1 a 5

Data: 2026-06-15
Agente: lk-ops
Área: LK / Atendimento / Chatwoot Recovery
Responsável: Lucas Cimino
Classificação: read-only/readback após pedido "Fazer do 1 ao 5"

## Pedido

Lucas pediu para executar/confirmar os itens 1 a 5 do fluxo de configuração do Chatwoot Recovery para carrinho abandonado e régua operacional Shopify.

## Fonte consultada

- Chatwoot Recovery API via Doppler (`lc-keys/prd`), sem imprimir valores de secrets.
- Chatwoot Rails read-only na VPS para auditoria sanitizada de mensagens recentes.

## Resultado dos itens 1 a 5

1. Inbox confirmado: `SHOPIFY_RECOVERY_INBOX_ID=2` e `KLAVIYO_RECOVERY_INBOX_ID=2`.
2. Templates disponíveis no Recovery: 12 templates LK relevantes retornados pela API, incluindo carrinho abandonado, ciclo de pedido e pós-venda.
3. Carrinho abandonado mapeado:
   - `SHOPIFY_RECOVERY_TEMPLATE_1=lk_checkout_abandonado_30min_v2`
   - `SHOPIFY_RECOVERY_TEMPLATE_2=lk_checkout_abandonado_24h_v2`
   - `SHOPIFY_RECOVERY_TEMPLATE_3=lk_checkout_abandonado_72h_v2`
   - delays ativos: `60,2880`, conforme redução/cooldown contra Meta 131049.
4. Régua de pedido mapeada:
   - `SHOPIFY_CREATED_TEMPLATE=lk_online_pedido_realizado_v1`
   - `SHOPIFY_APPROVED_TEMPLATE=lk_online_pagamento_aprovado_v1`
   - `SHOPIFY_SHIPPING_TEMPLATE=lk_online_pedido_enviado_v1`
   - `SHOPIFY_DELIVERED_TEMPLATE=lk_online_pedido_entregue_v1`
   - `SHOPIFY_FOLLOWUP_TEMPLATE=lk_pos_venda`
   - `SHOPIFY_FOLLOWUP_DELAY_MINUTES=4320`
5. Flags ativas:
   - `SHOPIFY_RECOVERY_ENABLED=true`
   - `SHOPIFY_NOTIFY_ENABLED=true`
   - `SHOPIFY_RECOVERY_131049_COOLDOWN_HOURS=24`

## Auditoria recente sanitizada

Janela read-only: últimas 24h.

- Conversas de carrinho abandonado tocadas: 12
- Mensagens públicas outbound: 18
- Sucesso/aceitas (`sent`/`delivered`/`read`): 13
- Falhadas: 5
- Notas simuladas: 0
- Última mensagem pública outbound: 2026-06-15T10:50:42Z
- Erro recorrente nas falhas: Meta `131049`

## Non-actions

- Nenhum secret impresso.
- Nenhum envio manual/canary novo executado nesta checagem.
- Nenhuma alteração em Shopify, Tiny, Klaviyo, Meta ou WhatsApp feita nesta checagem.
- Nenhuma correção de estoque/disponibilidade feita.

## Observação operacional

Os itens 1 a 5 já estavam efetivamente ativos no readback. A cadência de carrinho está reduzida para `60,2880` e cooldown `24h` por causa do erro Meta `131049`, evitando pressionar follow-up quando a Meta bloqueia entrega por saúde/engajamento.

## Próximos passos

- Continuar monitorando entrega real vs falhas `131049`.
- Não chamar o fluxo de 100% resolvido enquanto houver falhas Meta; reportar como operação ativa com bloqueios pontuais de entrega.
- Canary/envio manual novo só com pedido explícito.
