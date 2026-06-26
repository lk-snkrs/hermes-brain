# Plano de correção — Shopify POS restock → LK Team WhatsApp

Data: 2026-06-07

## Arquitetura correta

Usar o Hermes webhook público no Vercel como borda:

```text
Shopify orders/paid POS
  -> https://hermes-webhooks.vercel.app/webhooks/lk-shopify-pos-restock
  -> Hermes Gateway público /webhooks/lk-shopify-pos-restock
  -> handler determinístico lk_shopify_pos_restock
  -> /opt/data/scripts/lk_store_sale_restock_alert.py
  -> WhatsApp grupo LK Team
```

Não usar n8n para este fluxo.

## Evidência atual

- `https://hermes-webhooks.vercel.app/webhooks/lk-shopify-pos-restock` existe e valida assinatura Shopify. Sem assinatura retorna `401 missing_shopify_signature`.
- Um POST sintético Shopify-assinado e não-POS para o Vercel foi aceito e encaminhado, mas o upstream Hermes respondeu `202 {"status":"accepted"...}`.
- Esse retorno é negativo para o objetivo: indica caminho genérico/LLM no gateway vivo, não o handler determinístico.
- O endpoint custom `https://hermes-webhooks.lucascimino.com/webhooks/lk-shopify-pos-restock` não se comportou como o Vercel proxy no teste sem assinatura; retornou `401 Invalid signature` via Cloudflare/upstream, então não deve ser tratado como URL canônica até DNS/proxy ser verificado.

## Correção necessária

1. Manter/usar URL canônica Vercel: `https://hermes-webhooks.vercel.app/webhooks/lk-shopify-pos-restock`.
2. Fazer reload/restart controlado do Hermes Gateway público que atende a porta 8644 / domínio `crisp-hooks.srv1331756.hstgr.cloud`, pois o código instalado já contém o branch `lk_shopify_pos_restock`, mas o processo vivo ainda responde pelo caminho genérico.
3. Repetir probe Shopify-assinado com payload não-POS/sem envio real.
4. Critério de aceite: retorno HTTP 200 com campos determinísticos (`status`, `sent_count`, `queued_count`, `order_id`, `queue_id`, `reason`) e não `202 accepted`.
5. Só depois validar/ajustar o webhook Shopify para apontar para o Vercel canônico, se necessário, e sem backfill histórico salvo aprovação explícita.

## Aprovação necessária

Restart/reload do gateway público e qualquer ajuste em Shopify/Vercel são ações de produção. Pedir aprovação escopada antes de executar.
