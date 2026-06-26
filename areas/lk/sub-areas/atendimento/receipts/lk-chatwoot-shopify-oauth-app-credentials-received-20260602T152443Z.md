# Receipt — Chatwoot Shopify OAuth app credentials received

- Data UTC: 2026-06-02T15:24:43Z
- Sistema alvo: Chatwoot `https://chat.lkskrs.online`
- Shopify store: `lk-sneakerss.myshopify.com`

## Status

Lucas criou/configurou um app Shopify para integrar com Chatwoot e forneceu Client ID e Client Secret em chat.

## Dados sensíveis

- O Client Secret não foi registrado neste receipt.
- O token/secret foi tratado como sensível por ter sido colado no Telegram.

## Requisitos técnicos confirmados no código do Chatwoot

- Configs globais necessárias no Chatwoot Super Admin:
  - `SHOPIFY_CLIENT_ID`
  - `SHOPIFY_CLIENT_SECRET`
- Feature account-level necessária:
  - `shopify_integration`
- Scopes exigidos pela integração Chatwoot Shopify:
  - `read_customers`
  - `read_orders`
  - `read_fulfillments`
- Redirect URL:
  - `https://chat.lkskrs.online/shopify/callback`

## Bloqueio atual

O token de usuário Chatwoot disponível é Application API e não autentica no `/super_admin/app_config?config=shopify`; a rota redireciona para `/super_admin/sign_in`. Para concluir, é necessário:

1. Lucas preencher via UI Super Admin; ou
2. Lucas autorizar acesso SSH/rails runner no VPS para setar `InstallationConfig` e habilitar a feature no Account ID 1.

## Guardrails

- Nenhum write Shopify foi executado.
- Nenhuma alteração em produto, estoque, preço, tema ou pedido.
- Shopify no Chatwoot será contexto de pedido/cliente; Tiny permanece fonte de verdade para estoque/disponibilidade.
