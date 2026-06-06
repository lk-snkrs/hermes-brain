# Approval packet — ativação live LK POS pós-venda 30min via Evolution / LK Flagship

Data UTC: 2026-06-05

## Estado atual confirmado

- Shopify já possui webhook `orders/paid` ativo para `https://hermes-webhooks.vercel.app/webhooks/lk-shopify-pos-restock`.
- Esse webhook foi criado em `2026-05-23T17:52:30-03:00` e não foi criado/alterado nesta etapa.
- O código local do processador Hermes foi alterado para criar fila dry-run local `pos_thankyou_queue.json` para pedidos POS pagos/não cancelados.
- Teste real manual pela Evolution API / instância `LK Flagship` funcionou após correção de formatação.

## O que ainda NÃO está live

- Envio automático para clientes ainda não está ativo.
- Não existe scheduler/worker aprovado rodando para consumir a fila e enviar mensagens reais.
- O job atual registra preview/dry-run com `send_executed: false`.
- Nenhum webhook Shopify novo foi criado.
- n8n não foi desabilitado por Hermes.

## Por que Evolution retornou PENDING

O endpoint `/message/sendText/{instance}` retorna status inicial/assíncrono. `PENDING` no HTTP 201 não significa necessariamente falha; Lucas recebeu a mensagem, então o teste prático de entrega foi OK. Para produção, o ideal é registrar status inicial e, se houver webhook/status update da Evolution, reconciliar depois.

## Ativação segura recomendada

Fase 1 — canary live limitado:

- Alterar processador para permitir `dry_run=false` apenas quando `LK_POS_POSTPURCHASE_LIVE_SEND=1`.
- Consumir somente jobs vencidos (`send_after <= now`).
- Enviar via Evolution API, instância `LK Flagship`.
- Dedupe por `order_id` e `phone_e164`.
- Respeitar bloqueios: sem telefone => não envia; pedido não POS/pago/cancelado => não envia.
- Kill switch: remover/desativar `LK_POS_POSTPURCHASE_LIVE_SEND` volta para dry-run.
- Primeiro canary: no máximo 1–3 envios reais, depois auditoria.

## Aprovação necessária para executar live

Frase sugerida:

```text
Aprovo ativar canary live do pós-venda POS 30min via Evolution API / LK Flagship, usando o webhook Shopify orders/paid já existente, com limite inicial de 3 envios reais, kill switch, dedupe por pedido/telefone, sem n8n e sem alterar Shopify/Tiny/Chatwoot.
```

## Sobre desabilitar n8n

Recomendação: não desabilitar n8n antes de observar pelo menos 1 venda POS real entrando no ledger Hermes e 1 canary real enviado com sucesso pela Evolution/LK Flagship. Depois disso, pode desabilitar o workflow n8n antigo com rollback claro.
