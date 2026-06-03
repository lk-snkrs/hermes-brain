# Receipt — Chatwoot Shopify UI still shows connect/error after hook exists

- Data UTC: 2026-06-02T15:45:00Z
- Sistema: Chatwoot `https://chat.lkskrs.online`
- Account: `LK Sneakers` / ID `1`
- Shopify store: `lk-sneakerss.myshopify.com`

## Evento

Lucas enviou screenshot da tela `Integrações > Shopify` no Chatwoot mostrando:

- botão `Conectar`
- mensagem: `Ocorreu um erro ao tentar conectar com o Shopify...`

## Estado backend já verificado anteriormente

Rails runner mostrou hook Shopify existente:

- `app_id`: `shopify`
- `status`: `enabled`
- `reference_id`: `lk-sneakerss.myshopify.com`
- `account_id`: `1`

## Investigação local no código Chatwoot

Arquivos verificados:

- `app/javascript/dashboard/routes/dashboard/settings/integrations/Shopify.vue`
  - A mensagem de erro é exibida quando a rota recebe prop/query `error` após callback falho.
  - A página busca a integração via `store.dispatch('integrations/get', 'shopify')`.
- `app/javascript/dashboard/routes/dashboard/settings/integrations/Integration.vue`
  - O botão `Conectar` é mostrado quando `integrationEnabled` é falso.
- `app/views/api/v1/models/_app.json.jbuilder`
  - Campo `enabled` vem de `resource.enabled?(@current_account)`.
- `app/models/integrations/app.rb`
  - `enabled?` para apps comuns consulta `account.hooks.exists?(app_id: id)`.

## Interpretação

Como o hook existe no backend, a mensagem de erro pode ser resíduo da URL `?error=true` de uma segunda tentativa de conexão. Porém, se o botão `Conectar` continua após hard refresh e sem `?error=true`, então a API/frontend está lendo `enabled=false` apesar do hook existir, exigindo nova validação via API/rails runner.

## Próximo comando recomendado

Read-only no VPS:

```bash
cd /opt/chatwoot
docker compose exec rails bundle exec rails runner 'account = Account.find(1); app = Integrations::App.find(id: "shopify"); puts({feature_shopify: account.feature_enabled?("shopify_integration"), client_id_present: GlobalConfigService.load("SHOPIFY_CLIENT_ID", nil).present?, hook_count: account.hooks.where(app_id: "shopify").count, app_active: app.active?(account), app_enabled: app.enabled?(account), hooks: account.hooks.where(app_id: "shopify").select(:id,:status,:reference_id,:created_at,:updated_at).map { |h| {id: h.id, status: h.status, reference_id: h.reference_id, created_at: h.created_at, updated_at: h.updated_at} }}.to_json)'
```

Não imprime tokens.

## Guardrails

- Não registrar access_token do hook.
- Não mexer em produtos, pedidos, estoque, preço, tema, webhooks, WhatsApp ou automações.
- Shopify é contexto de atendimento; Tiny segue estoque oficial.
