# Receipt — Chatwoot Shopify OAuth duplicate hook diagnosis

- Data UTC: 2026-06-02T15:39:00Z
- Sistema: Chatwoot `https://chat.lkskrs.online`
- Account: `LK Sneakers` / ID `1`
- Shopify store esperada: `lk-sneakerss.myshopify.com`

## Log recebido

Lucas executou:

```bash
cd /opt/chatwoot
docker compose logs rails --tail=200 | grep -i shopify
```

O log mostrou:

- POST para `/api/v1/accounts/1/integrations/shopify/auth`.
- Uma tentativa inicial com `shop_domain = lksneakersbr.myshopify.com`.
- Callback efetivo voltou com `shop=lk-sneakerss.myshopify.com`.
- Erro do Chatwoot no callback:

```text
Shopify callback error: Validation failed: App has already been taken
```

## Interpretação

O erro vem da validação do model `Integrations::Hook`: `app_id` é único por `account_id` salvo (`validates :app_id, uniqueness: { scope: [:account_id] ... }`).

Isso significa que já existe um hook `app_id='shopify'` para a conta `1`. Pode ser:

1. integração já conectada e erro ocorreu por segunda tentativa de conexão; ou
2. hook antigo/stale que bloqueia nova conexão.

## Próxima ação recomendada

Rodar Rails runner read-only para listar o hook sem imprimir token:

```bash
cd /opt/chatwoot
docker compose exec rails bundle exec rails runner 'puts Integrations::Hook.where(account_id: 1, app_id: "shopify").select(:id,:account_id,:app_id,:status,:reference_id,:created_at,:updated_at).map(&:attributes).to_json'
```

Se o `reference_id` for `lk-sneakerss.myshopify.com` e status `enabled`, tratar como conectado e validar pela UI.

Se o hook for antigo/incorreto, remover somente esse hook após aprovação explícita/backup e refazer OAuth.

## Guardrails

- Não registrar access_token do hook.
- Não mexer em produtos, pedidos, estoque, preço, tema, webhooks, WhatsApp ou automações.
- Shopify é contexto de atendimento; Tiny segue estoque oficial.
