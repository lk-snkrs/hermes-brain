# LK POS restock missed alert — root cause

Data: 2026-06-08

## Pergunta
Lucas perguntou por que os alertas de reposição das vendas POS de hoje não foram enviados.

## Diagnóstico read-only

- Shopify Admin contém webhook `orders/paid` apontando para `https://hermes-webhooks.vercel.app/webhooks/lk-shopify-pos-restock`.
- Endpoint público responde `401 missing_shopify_signature` quando sem assinatura, provando rota pública ativa.
- Teste seguro/non-POS assinado com `SHOPIFY_WEBHOOK_SECRET` do Doppler `lc-keys/prd` via profile `lk-shopify` retornou `401 Invalid signature` no Vercel.
- Logs locais do Hermes Gateway em 2026-06-08 não mostram evento `lk-shopify-pos-restock` para os pedidos POS de hoje; aparecem eventos de Evolution e rotas stock, o que indica que o POST não chegou ao Hermes local nessa rota.

## Conclusão
Causa provável: divergência de secret de HMAC entre Shopify/Vercel/Hermes. O Vercel está rejeitando a assinatura antes de encaminhar ao Hermes, então o fluxo de WhatsApp não roda e nada entra na fila.

## Próximo passo seguro
Approval packet necessário para alinhar `SHOPIFY_WEBHOOK_SECRET` no Vercel/Hermes com a fonte correta, redeploy/reload do Vercel se necessário, repetir probe seguro assinado e só então backfill dos itens POS de 2026-06-08 se Lucas aprovar.

## Segurança
Nenhum valor de secret foi registrado.
