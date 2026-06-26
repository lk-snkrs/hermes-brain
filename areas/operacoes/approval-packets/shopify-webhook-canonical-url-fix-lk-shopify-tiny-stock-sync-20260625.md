# Approval packet — corrigir URL canônica Shopify webhook `lk-shopify-tiny-stock-sync`

## Pedido
Lucas: “Vamos atacar a assinatura”.

## Diagnóstico verificado

Warnings no Main Gateway:

```text
Invalid signature for route lk-shopify-tiny-stock-sync
```

Causa confirmada por read-only Admin Shopify:

| Shopify webhook ID | Topic | URL atual | Problema |
|---|---|---|---|
| 1646886125790 | `orders/paid` | `https://crisp-hooks.srv1331756.hstgr.cloud/webhooks/lk-shopify-tiny-stock-sync` | Chama Hermes direto/host antigo; Shopify assina com `X-Shopify-Hmac-Sha256`, mas Hermes direto espera `X-Webhook-Signature` |
| 1646886158558 | `orders/cancelled` | `https://crisp-hooks.srv1331756.hstgr.cloud/webhooks/lk-shopify-tiny-stock-sync` | Mesmo problema |

Proxy canônico testado com probe Shopify assinado:

```text
https://hermes-webhooks.lucascimino.com/webhooks/lk-shopify-tiny-stock-sync
HTTP 202 accepted
values_printed=false
```

## Correção proposta

Atualizar **somente** esses dois webhook subscriptions no Shopify Admin:

```text
1646886125790 orders/paid      -> https://hermes-webhooks.lucascimino.com/webhooks/lk-shopify-tiny-stock-sync
1646886158558 orders/cancelled -> https://hermes-webhooks.lucascimino.com/webhooks/lk-shopify-tiny-stock-sync
```

## Escopo permitido se Lucas aprovar

- Shopify Admin REST `PUT /admin/api/.../webhooks/{id}.json`
- apenas campo `address`
- apenas os 2 IDs acima
- sem produtos, pedidos, estoque, Tiny, tema, preço, disponibilidade, Klaviyo ou mensagens
- secrets via Doppler, `values_printed=false`

## Rollback

Reverter os mesmos 2 IDs para:

```text
https://crisp-hooks.srv1331756.hstgr.cloud/webhooks/lk-shopify-tiny-stock-sync
```

## Verificação pós-write

1. Readback Shopify Admin dos 2 IDs confirma novo `address`.
2. Probe público Shopify-HMAC para `hermes-webhooks.lucascimino.com/.../lk-shopify-tiny-stock-sync` retorna `202 accepted`.
3. Monitorar logs do Main por 5 minutos; nenhum novo `Invalid signature for route lk-shopify-tiny-stock-sync` vindo de eventos novos.
4. Brain health + receipt.

## Risco

Baixo/médio: troca endpoint de webhook já existente para o proxy canônico. Se o proxy estiver indisponível, rollback é simples pelo campo `address`.

## Approval phrase

Aprovar exatamente:

```text
Aprovo corrigir os 2 webhooks Shopify lk-shopify-tiny-stock-sync para hermes-webhooks.lucascimino.com
```
