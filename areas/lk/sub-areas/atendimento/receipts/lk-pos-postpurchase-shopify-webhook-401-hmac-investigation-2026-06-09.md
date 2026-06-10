# LK POS pós-compra — investigação webhook Shopify 401 HMAC

Data: 2026-06-09T18:40:04Z
Área: LK / Atendimento / Pós-compra / Shopify POS / Vercel proxy / Hermes Gateway
Escopo: investigação read-only/local; sem alteração Shopify/Vercel/Doppler; sem envio adicional de WhatsApp.

## Contexto

Após ativação do worker automático, Lucas apontou nova compra POS. Shopify mostrou dois pedidos POS reais:

- `#147731`: `created_at=2026-06-09T14:56:29-03:00`, `processed_at=2026-06-09T14:56:28-03:00`
- `#147732`: `created_at=2026-06-09T14:58:19-03:00`, `processed_at=2026-06-09T14:58:19-03:00`

Ambos eram elegíveis: `financial_status=paid`, `cancelled=false`, `source_name=pos`, `app_id=129785`, cliente/telefone presentes.

O atendimento foi mitigado separadamente com backfill e limite diário por cliente; esta investigação foca o ingresso automático Shopify→Vercel→Hermes.

## Evidência Shopify webhook registrado

Shopify tem webhook registrado:

```json
{
  "id": 1641004826846,
  "topic": "orders/paid",
  "address": "https://hermes-webhooks.vercel.app/webhooks/lk-shopify-pos-restock",
  "format": "json",
  "created_at": "2026-05-23T17:52:30-03:00",
  "updated_at": "2026-05-23T17:52:30-03:00"
}
```

## Evidência Vercel

Logs Vercel mostram que chamadas reais chegaram no proxy e receberam `401`:

```text
17:56:35Z POST /webhooks/lk-shopify-pos-restock 401
17:56:36Z POST /webhooks/lk-shopify-pos-restock 401
17:57:37Z POST /webhooks/lk-shopify-pos-restock 401
17:58:24Z POST /webhooks/lk-shopify-pos-restock 401
17:58:25Z POST /webhooks/lk-shopify-pos-restock 401
17:58:50Z POST /webhooks/lk-shopify-pos-restock 401
17:59:26Z POST /webhooks/lk-shopify-pos-restock 401
17:59:37Z POST /webhooks/lk-shopify-pos-restock 401
18:01:27Z POST /webhooks/lk-shopify-pos-restock 401
18:04:39Z POST /webhooks/lk-shopify-pos-restock 401
18:06:27Z POST /webhooks/lk-shopify-pos-restock 401
```

Esses horários batem com a criação/processamento dos pedidos POS e retries da Shopify.

## Evidência Hermes local

No gateway Hermes não há processamento `queued` dos pedidos `#147731/#147732` via `lk-shopify-pos-restock`. Isso é consistente com bloqueio antes do forward Vercel→Hermes.

## Código do proxy

`/opt/data/hermes-webhooks/api/webhooks/[route].js`:

```js
function verifyShopify(req, rawBody, shopifySecret) {
  const shopifyHmac = req.headers['x-shopify-hmac-sha256'];
  if (!shopifyHmac) return { ok: false, status: 401, error: 'missing_shopify_signature' };

  const expectedShopifyHmac = crypto
    .createHmac('sha256', shopifySecret)
    .update(rawBody)
    .digest('base64');

  if (!safeEqual(shopifyHmac, expectedShopifyHmac)) {
    return { ok: false, status: 401, error: 'invalid_shopify_signature' };
  }
  return { ok: true };
}
```

Para rotas Shopify, `401` antes de forward significa assinatura Shopify ausente ou inválida. Como as chamadas vêm do webhook Shopify registrado, a hipótese principal é assinatura inválida por secret HMAC incorreto.

## Secrets observados, sem valores

Doppler contém:

- `SHOPIFY_WEBHOOK_SECRET`: presente, length `44`, hash sanitizado `e6dd33e6ffaa`
- `SHOPIFY_ACCESS_TOKEN`: presente

Não há outro candidato Shopify app secret no Doppler, como:

- `SHOPIFY_API_SECRET`
- `SHOPIFY_API_SECRET_KEY`
- `SHOPIFY_CLIENT_SECRET`
- `SHOPIFY_APP_SECRET`

Vercel lista `SHOPIFY_WEBHOOK_SECRET` como env production presente, mas a comparação de valor via `vercel env pull` não foi conclusiva porque o CLI não materializou os valores no arquivo local apesar de listar os nomes. Não imprimir/insistir em secret.

## Hipótese principal

`SHOPIFY_WEBHOOK_SECRET` configurado no proxy não corresponde ao segredo usado pela Shopify para assinar webhooks desse app.

Observação técnica: webhooks Shopify são assinados com a secret do app/custom app que criou a subscription. Se a secret em Doppler/Vercel é uma secret antiga/manual, ou não é o app client secret correto, probes manuais assinados por nós passam, mas entregas reais Shopify falham com `401`.

## O que NÃO é a causa provável

- Worker Hermes: funcionou e enviou o backfill de `#147732`.
- Rota Hermes local: probes assinados pelo secret atual chegaram e foram processados como `ignored` quando payload falso não-POS.
- Shopify webhook ausente: webhook está registrado.
- Pedido não elegível: ambos são POS/pagos/não cancelados.

## Correções possíveis

### Correção canônica

1. Obter no painel Shopify Custom App/Admin app a secret correta usada para assinar webhooks.
2. Atualizar `SHOPIFY_WEBHOOK_SECRET` no Doppler `lc-keys/prd` e no Vercel production `hermes-webhooks`.
3. Redeploy/restart do Vercel se necessário.
4. Fazer probe assinado com a secret nova e aguardar/retry real Shopify.
5. Verificar Hermes recebendo `status=sent/no_lines/queued` em vez de Vercel `401`.

Requer aprovação e manuseio de secret; não imprimir valores.

### Mitigação operacional complementar

Criar reconciliador local read-only Shopify→fila para POS paid recentes, rodando a cada 5 min, com:

- janela curta, ex.: últimos 90 min;
- idempotência por `order_id`;
- limite diário por telefone/cliente já implementado;
- sem mexer em estoque/Tiny;
- worker existente manda no máximo 1 por tick.

Isso reduz dependência de webhook, mas é polling Shopify e exige aprovação separada porque gera mensagens reais quando encontra pedidos elegíveis.

## Estado atual dos pedidos investigados

Atendimento mitigado:

- `#147732`: enviado e entregue via backfill/worker.
- `#147731`: `skipped_daily_limit` por ser mesma cliente/dia.

## Próximo passo recomendado

Pedir ao Lucas autorização para uma das opções:

1. Corrigir secret HMAC Shopify no Doppler/Vercel se ele puder fornecer/validar a secret do app Shopify; ou
2. ativar reconciliador read-only Shopify→fila como fallback operacional, mantendo limite de 1 mensagem por cliente/dia.
