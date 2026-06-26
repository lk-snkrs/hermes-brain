# Receipt — Chatwoot Shopify app config appears enabled

- Data UTC: 2026-06-02T15:29:00Z
- Sistema alvo: Chatwoot `https://chat.lkskrs.online`
- Account: `LK Sneakers` / ID `1`
- Shopify store alvo: `lk-sneakerss.myshopify.com`

## Evento

Lucas informou que a configuração Shopify foi concluída no Chatwoot Super Admin e enviou evidência visual mostrando o card `Shopify` disponível com indicador verde em `Configuration for setting up Shopify Integration`.

Lucas também enviou um token de automação de app em chat. O valor não foi registrado aqui e não deve ser repetido. Até o momento, esse token não foi usado para writes nem para conectar ações produtivas.

## Status operacional

- Integração Shopify parece habilitada na configuração global do Chatwoot.
- Próximo passo: conectar a loja pelo fluxo OAuth no Chatwoot usando domínio `lk-sneakerss.myshopify.com`.

## Guardrails

- Nenhum write Shopify executado por Hermes.
- Nenhum produto, pedido, estoque, preço, tema, webhook, campanha ou WhatsApp alterado.
- Shopify no Chatwoot deve ser usada como contexto de atendimento/pedido/cliente.
- Tiny permanece fonte oficial para estoque/disponibilidade.

## Próxima validação esperada

Após OAuth:

1. Verificar se Shopify aparece em `Settings > Integrations` como conectada.
2. Validar contexto de pedido/cliente no Chatwoot sem alterar dados Shopify.
3. Se possível, reconsultar `/api/v1/accounts/1/integrations/apps` com API token Chatwoot para confirmar status.
