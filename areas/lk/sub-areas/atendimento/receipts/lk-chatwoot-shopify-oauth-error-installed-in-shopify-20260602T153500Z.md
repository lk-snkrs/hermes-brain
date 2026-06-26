# Receipt — Chatwoot Shopify OAuth error, app appears installed in Shopify

- Data UTC: 2026-06-02T15:35:00Z
- Sistema alvo: Chatwoot `https://chat.lkskrs.online`
- Conta Chatwoot: `LK Sneakers` / Account ID `1`
- Shopify store: `lk-sneakerss.myshopify.com`

## Evento

Lucas reportou erro no Chatwoot ao tentar conectar Shopify:

> Ocorreu um erro ao tentar conectar com o Shopify. Por favor, tente novamente ou entre em contato com o suporte se o problema persistir.

Em seguida enviou screenshot da Shopify mostrando o app `Chatwoot LK Sneakers` como instalado agora mesmo.

## Evidência visual

- Shopify mostra `Chatwoot LK Sneakers` instalado.
- Há botão `Abrir app` e `Desinstalar app`.
- Banner informa que o app não está listado na Shopify App Store.
- A tabela de permissões exibida parece ampla; escopos mínimos confirmados no código Chatwoot são `read_customers`, `read_orders`, `read_fulfillments`.

## Investigação local no código Chatwoot

Arquivos lidos em `/tmp/chatwoot-scope-check`:

- `app/controllers/api/v1/accounts/integrations/shopify_controller.rb`
  - endpoint `auth` gera URL OAuth com `redirect_uri = ENV['FRONTEND_URL'] + /shopify/callback`.
- `app/controllers/shopify/callbacks_controller.rb`
  - callback troca o code por token e cria `Integrations::Hook` com `app_id: shopify`, `access_token`, `reference_id: params[:shop]`.
  - em erro, loga `Shopify callback error: ...` e redireciona para a tela de integração com `?error=true`.
- `app/helpers/shopify/integration_helper.rb`
  - state é JWT assinado com `SHOPIFY_CLIENT_SECRET`.

## Hipóteses prováveis

1. App foi instalado na Shopify, mas o Chatwoot falhou ao gravar o hook/token da integração.
2. Possível mismatch de Client Secret/redirect/callback ou erro na troca OAuth.
3. Possível feature/config global incompleta ou permissões/escopos diferentes do esperado.
4. Necessário ler logs do container Rails para causa exata (`Shopify callback error: ...`).

## Guardrails

- Nenhuma alteração Shopify executada por Hermes.
- Nenhum produto, pedido, estoque, preço, tema, webhook, campanha ou WhatsApp alterado.
- Shopify no Chatwoot deve servir apenas como contexto de atendimento/pedidos/clientes.
- Tiny permanece fonte oficial para estoque/disponibilidade.
