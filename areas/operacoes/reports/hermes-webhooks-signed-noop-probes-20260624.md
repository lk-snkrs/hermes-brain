# Hermes Webhooks Vercel — signed no-op probes

- Data: 2026-06-24
- Escopo: probes assinados contra `https://hermes-webhooks.lucascimino.com/webhooks/<route>`.
- Pedido Lucas: seguir com validação Vercel após auditoria read-only.
- Secrets: usados via Doppler `lc-keys/prd`/runtime env, valores não impressos.
- Writes externos/deploy/env/provider registry: `0`
- values_printed: `false`

## Veredito

**Vercel continua sendo o caminho certo, mas a prova assinada abriu um blocker específico em Shopify.**

- Evolution: assinatura/proxy secret aceito pela Vercel e encaminhado para Hermes.
- Klaviyo: assinatura Klaviyo aceita pela Vercel e evento chegou ao Hermes.
- Shopify POS restock: payload assinado com o secret canônico do Doppler foi rejeitado pela Vercel com `401 Invalid signature`.

Isso não derruba a Vercel como arquitetura; indica drift ou divergência na camada de segredo/assinatura Shopify usada pela Production Vercel versus o secret canônico Doppler/Shopify esperado.

## Resultados dos probes

| Provider/rota | Resultado HTTP | Resultado operacional |
|---|---:|---|
| Shopify `lk-shopify-pos-restock` | `401` | `Invalid signature` mesmo com payload no-op assinado via Doppler |
| Evolution `lk-evolution-delivery-reconciliation` | `202` | `accepted`; POST `messages.update` chegou ao Hermes |
| Klaviyo `lk-content-klaviyo-events` | `202` | `accepted`; Hermes logou evento `event:klaviyo.email_opened` e respondeu no-op |

## Detalhe por provider

### Shopify

Probe usado:

- rota: `lk-shopify-pos-restock`
- topic: `orders/paid`
- payload: fake order pago, porém `source_name=web` para ser inelegível como POS e retornar `ignored/not_paid_active_pos_order` se a assinatura passasse.
- assinatura: `X-Shopify-Hmac-Sha256`, base64 HMAC-SHA256 do raw body com `SHOPIFY_WEBHOOK_SECRET` via Doppler.

Resultado:

- Vercel respondeu `401`/`Invalid signature` antes de encaminhar para Hermes.
- Não houve envio externo, WhatsApp, Shopify/Tiny/Klaviyo write ou deploy.

Interpretação:

- O secret `SHOPIFY_WEBHOOK_SECRET` existe no Doppler e aparece como env encrypted na Vercel Production.
- Mesmo assim, a assinatura canônica local foi rejeitada pela runtime Vercel.
- Hipóteses prováveis: valor de Production Vercel divergente do Doppler; Shopify app/webhook usando outro secret; env pull não permitiu comparar valor real de secret sensível; ou secret/rota Shopify precisa de rotação controlada.

### Evolution

Probe usado:

- rota: `lk-evolution-delivery-reconciliation`
- payload: `messages.update`, `fromMe=false`, status `SERVER_ACK`.
- proxy secret via Doppler no header aceito pela Vercel.

Resultado:

- HTTP `202 accepted`.
- Logs Hermes mostram POST na rota e processamento assíncrono.
- Não houve update de ledger real esperado porque `fromMe=false` é no-op/inbound.

### Klaviyo

Probe usado:

- rota: `lk-content-klaviyo-events`
- payload: fake `event:klaviyo.email_opened`, sem campaign id real.
- assinatura `klaviyo-signature` + timestamp via Doppler.

Resultado:

- HTTP `202 accepted`.
- Logs Hermes mostram evento recebido e resposta no-op.
- Não houve campaign id real nem write externo.

## Observação importante sobre o downstream Hermes

Evolution/Klaviyo retornaram `202 accepted`, não `200` determinístico, porque a rota Hermes disparou processamento assíncrono/agent run. A prova atual valida:

```text
provider signature -> Vercel auth -> Vercel -> Hermes route accepted
```

Para prova determinística completa, as rotas críticas deveriam preferir script/deliver-only quando o caso for puramente ingestão/ledger, evitando LLM para probes e eventos técnicos.

## Próxima ação recomendada

**P0: reconciliar Shopify secret antes de confiar em webhooks Shopify.**

Ação segura proposta, ainda sem deploy/write até aprovação:

1. Fazer readback da configuração Shopify Admin/API para saber qual webhook/app secret está ativo para as rotas Shopify.
2. Comparar presença/identidade por nome entre Doppler, Vercel Production e Shopify, sem imprimir valores.
3. Se confirmar drift, preparar approval packet para uma das opções:
   - atualizar Vercel Production `SHOPIFY_WEBHOOK_SECRET` para o valor canônico correto; ou
   - atualizar Doppler/registro canônico se a Vercel/Shopify estiver correta; ou
   - rotacionar secret de forma controlada com probe assinado e rollback.
4. Repetir probe `lk-shopify-pos-restock` até retornar o esperado: `200 ignored not_paid_active_pos_order`, `sent_count=0`, `queued_count=0`.

## Limites respeitados

- Sem deploy Vercel.
- Sem alteração de env/secrets.
- Sem alteração de provider webhook registry.
- Sem Shopify/Tiny/Klaviyo/Evolution writes.
- Sem WhatsApp/e-mail.
- Sem gateway/VPS/Docker/Traefik changes.
- Nenhum valor de secret foi impresso.
