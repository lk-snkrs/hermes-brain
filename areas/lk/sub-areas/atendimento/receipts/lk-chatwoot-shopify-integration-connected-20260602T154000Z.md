# Receipt — Chatwoot Shopify integration connected

- Data UTC: 2026-06-02T15:40:00Z
- Sistema: Chatwoot `https://chat.lkskrs.online`
- Account: `LK Sneakers` / Account ID `1`
- Shopify store conectada: `lk-sneakerss.myshopify.com`

## Verificação via Rails runner

Lucas executou no VPS:

```bash
cd /opt/chatwoot
docker compose exec rails bundle exec rails runner 'puts Integrations::Hook.where(account_id: 1, app_id: "shopify").select(:id,:account_id,:app_id,:status,:reference_id,:created_at,:updated_at).map(&:attributes).to_json'
```

Resultado sem access token:

```json
[
  {
    "id": 1,
    "account_id": 1,
    "app_id": "shopify",
    "status": "enabled",
    "reference_id": "lk-sneakerss.myshopify.com",
    "created_at": "2026-06-02T15:35:17.430Z",
    "updated_at": "2026-06-02T15:35:17.430Z"
  }
]
```

## Conclusão

A integração Shopify está conectada no Chatwoot para a conta `LK Sneakers`.

O erro anterior `Validation failed: App has already been taken` ocorreu porque uma segunda tentativa de OAuth tentou criar outro hook `app_id=shopify` para a mesma conta. O model `Integrations::Hook` permite apenas um hook por `app_id` e `account_id`, salvo exceções de `allow_multiple_hooks`.

## Guardrails

- Nenhum token/access_token foi registrado.
- Nenhum write Shopify feito por Hermes.
- Nenhum produto, pedido, estoque, preço, tema, webhook, WhatsApp, campanha ou automação foi alterado.
- Shopify deve ser usada como contexto de atendimento/pedidos/clientes.
- Tiny permanece fonte oficial para estoque/disponibilidade.

## Próximas validações recomendadas

1. UI: abrir `https://chat.lkskrs.online/app/accounts/1/settings/integrations/shopify` e confirmar status conectado.
2. Atendimento: testar um contato/conversa com e-mail ou telefone que exista na Shopify para ver pedidos associados.
3. Não ativar automações/IA/envios sem aprovação explícita.
