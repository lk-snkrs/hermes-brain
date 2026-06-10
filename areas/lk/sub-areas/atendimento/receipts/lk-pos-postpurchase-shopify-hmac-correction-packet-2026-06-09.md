# LK POS pós-compra — pacote de correção HMAC Shopify/Vercel

Data: 2026-06-09T18:54:30Z
Área: LK / Atendimento / Pós-compra / Shopify POS / Webhooks / Vercel / Doppler

## Decisão

Lucas sinalizou que a causa raiz deve ser corrigida mesmo com o reconciliador polling ativo, porque o webhook será necessário para o futuro.

## Estado verificado

Secrets atuais em Doppler `lc-keys/prd` — somente presença/tamanho/hash curto, sem valores:

```json
{
  "SHOPIFY_WEBHOOK_SECRET": {"exists": true, "len": 44},
  "SHOPIFY_ACCESS_TOKEN": {"exists": true, "len": 38},
  "SHOPIFY_STORE_URL": {"exists": true, "len": 26},
  "SHOPIFY_API_SECRET": {"exists": false},
  "SHOPIFY_API_SECRET_KEY": {"exists": false},
  "VERCEL_API_TOKEN": {"exists": true, "len": 60}
}
```

Vercel production env do projeto `hermes-webhooks` contém:

```text
HERMES_WEBHOOK_SECRET
SHOPIFY_WEBHOOK_SECRET
```

## Causa provável

O proxy Vercel valida `X-Shopify-Hmac-Sha256` usando `process.env.SHOPIFY_WEBHOOK_SECRET` e calcula HMAC-SHA256 base64 sobre o raw body.

Os POSTs reais da Shopify para `/webhooks/lk-shopify-pos-restock` chegaram ao Vercel, mas retornaram `401`, antes de Hermes. Isso é consistente com `invalid_shopify_signature`.

O valor atual de `SHOPIFY_WEBHOOK_SECRET` parece não bater com o segredo de assinatura real do app Shopify que envia os webhooks.

## Correção necessária

Atualizar `SHOPIFY_WEBHOOK_SECRET` para o **Client secret / API secret key do app Shopify** responsável pelo webhook `orders/paid`, não um segredo aleatório nem token Admin API.

Esse segredo normalmente não é exposto via Admin API; precisa ser lido no painel Shopify do app/custom app.

## Procedimento seguro recomendado

1. Obter o Client secret / API secret key correto no Shopify Admin.
2. Atualizar Doppler `lc-keys/prd` secret `SHOPIFY_WEBHOOK_SECRET` com esse valor.
3. Atualizar Vercel production env `SHOPIFY_WEBHOOK_SECRET` no projeto `hermes-webhooks`.
4. Redeploy/restart do projeto Vercel se necessário para materializar env.
5. Fazer probe assinado com o novo secret para confirmar `200/ignored` no Vercel/Hermes.
6. Monitorar próximo pedido POS real: Vercel não deve mais retornar `401`; Hermes deve registrar `queued` ou `duplicate` se polling já pegou.

## Guardrails

- Não imprimir segredo, preview, token, client secret ou hash longo em Telegram/Brain.
- Não remover o reconciliador polling; ele fica como fallback.
- Não mexer em estoque/Tiny.
- Se Lucas colar o segredo em chat, tratar como sensível e recomendar rotação se houver exposição indesejada.

## Status

Bloqueado aguardando o Client secret/API secret key correto do app Shopify ou acesso/manual step para obtê-lo no Admin.
