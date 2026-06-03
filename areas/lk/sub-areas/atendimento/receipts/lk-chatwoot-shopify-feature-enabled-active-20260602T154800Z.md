# Receipt — Chatwoot Shopify feature enabled and integration active

- Data UTC: 2026-06-02T15:48:00Z
- Sistema: Chatwoot `https://chat.lkskrs.online`
- Account: `LK Sneakers` / ID `1`
- Shopify store: `lk-sneakerss.myshopify.com`

## Ação executada por Lucas no VPS

Lucas executou Rails runner para habilitar a feature account-level:

```bash
cd /opt/chatwoot
docker compose exec rails bundle exec rails runner 'account = Account.find(1); account.enable_features!("shopify_integration"); puts({feature_shopify: account.reload.feature_enabled?("shopify_integration"), app_active: Integrations::App.find(id: "shopify").active?(account), app_enabled: Integrations::App.find(id: "shopify").enabled?(account), hook_count: account.hooks.where(app_id: "shopify").count}.to_json)'
```

## Resultado

```json
{
  "feature_shopify": true,
  "app_active": true,
  "app_enabled": true,
  "hook_count": 1
}
```

## Conclusão

A integração Shopify está ativa no Chatwoot para a conta `LK Sneakers`.

- Config global presente: `SHOPIFY_CLIENT_ID`/secret já configurados no Super Admin.
- Hook existente: `app_id=shopify`, `status=enabled`, `reference_id=lk-sneakerss.myshopify.com`.
- Feature account-level `shopify_integration` habilitada.
- App ativo e enabled pelo código do Chatwoot.

## Avisos observados

Os avisos de Docker compose version obsolete, RubyLLM legacy API, IP lookup key ausente e Hashie::Mash default são ruído operacional já emitido pelo ambiente; não impediram a execução.

## Guardrails

- Nenhum token/access_token foi registrado.
- Nenhum write Shopify foi feito por Hermes.
- Nenhum produto, pedido, estoque, preço, tema, webhook, WhatsApp, campanha ou automação foi alterado.
- Shopify deve ser usada como contexto de atendimento/pedidos/clientes.
- Tiny permanece fonte oficial para estoque/disponibilidade.

## Próximas validações

1. Hard refresh na UI do Chatwoot: `/app/accounts/1/settings/integrations/shopify`.
2. Testar conversa/contato com e-mail/telefone existente na Shopify para visualizar pedidos.
3. WhatsApp Business API continua pendente de dados Meta e aprovação de criação de inbox.
