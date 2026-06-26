# Receipt — Chatwoot Shopify feature flag missing

- Data UTC: 2026-06-02T15:46:00Z
- Sistema: Chatwoot `https://chat.lkskrs.online`
- Account: `LK Sneakers` / ID `1`
- Shopify store: `lk-sneakerss.myshopify.com`

## Verificação recebida

Lucas executou Rails runner read-only e obteve:

```json
{
  "feature_shopify": false,
  "client_id_present": true,
  "hook_count": 1,
  "app_active": false,
  "app_enabled": true,
  "hooks": [
    {
      "id": 1,
      "status": "enabled",
      "reference_id": "lk-sneakerss.myshopify.com",
      "created_at": "2026-06-02T15:35:17.430Z",
      "updated_at": "2026-06-02T15:35:17.430Z"
    }
  ]
}
```

## Interpretação

- O hook Shopify existe e está enabled.
- O Client ID global existe.
- A tela/API pode não listar Shopify como ativo porque a feature account-level `shopify_integration` está desabilitada (`feature_shopify=false`, `app_active=false`).

## Código verificado

`app/models/concerns/featurable.rb` confirma método:

```ruby
enable_features!("shopify_integration")
```

## Próxima ação recomendada

Habilitar somente a feature da conta 1:

```bash
cd /opt/chatwoot
docker compose exec rails bundle exec rails runner 'account = Account.find(1); account.enable_features!("shopify_integration"); puts({feature_shopify: account.reload.feature_enabled?("shopify_integration"), app_active: Integrations::App.find(id: "shopify").active?(account), app_enabled: Integrations::App.find(id: "shopify").enabled?(account), hook_count: account.hooks.where(app_id: "shopify").count}.to_json)'
```

Essa alteração não toca Shopify, produtos, pedidos, estoque, preço, tema, WhatsApp, campanhas ou automações.

## Guardrails

- Não registrar access_token do hook.
- Tiny segue fonte oficial de estoque/disponibilidade.
