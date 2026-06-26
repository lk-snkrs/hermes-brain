# Receipt — Chatwoot Shopify integration attempt / token validation

- Data UTC: 2026-06-02T15:12:41Z
- Sistema alvo: Chatwoot `https://chat.lkskrs.online`
- Conta Chatwoot: LK Sneakers / Account ID 1
- Shopify store: `lk-sneakerss.myshopify.com`

## Pedido

Lucas pediu para configurar Shopify no Chatwoot e forneceu um token Shopify Admin API em chat.

## Ação segura executada

- Token Shopify foi usado apenas para validação read-only em `GET /admin/api/2024-01/shop.json`.
- Resultado: token válido para a loja LK.
- Dados não sensíveis observados:
  - shop name: `LK`
  - primary domain: `lksneakers.com.br`
  - myshopify domain: `lk-sneakerss.myshopify.com`
  - timezone: `America/Sao_Paulo`
  - currency: `BRL`
  - plan: `shopify_plus`

## Bloqueio / próximo requisito

A integração nativa Shopify do Chatwoot self-hosted não usa token Admin API direto; pela documentação oficial, precisa de Shopify app OAuth com:

- Shopify Client ID
- Shopify Client Secret
- redirect URL: `https://chat.lkskrs.online/shopify/callback`
- configuração no Chatwoot Super Admin: `https://chat.lkskrs.online/super_admin/app_config?config=shopify`

A API do Chatwoot indicou que a integração Shopify ainda não aparece em `Settings -> Integrations`; apps disponíveis eram Webhooks, Dashboard Apps, OpenAI, Dialogflow, Google Translate e Dyte.

## Segurança

- Valor do token não foi registrado neste receipt.
- Recomendar salvar/rotacionar token após uso, pois foi colado no Telegram.
- Nenhum write Shopify foi executado.
- Nenhum produto, pedido, estoque, preço ou tema foi alterado.
