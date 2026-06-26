# Receipt — correção de status pós-venda POS #147693

Data: 2026-06-06

## Sinal recebido

Lucas informou no Telegram: “não enviou a mensagem”.

## Diagnóstico executado

- Li a fila local `pos_thankyou_queue.json`.
- Verifiquei Evolution API read-only:
  - instância `LK Flagship`: `open`;
  - número do pedido validou como WhatsApp existente (`exists=true`), sem registrar telefone no Brain;
  - busca em `findMessages` encontrou 2 registros `fromMe=true` tipo `conversation` para o JID do cliente, correspondentes às duas tentativas.

## Causa operacional identificada

O código estava interpretando HTTP 201 + `status=PENDING` da Evolution como “sent”. Isso era otimista demais. `PENDING` significa aceito/registrado pela API, mas não comprova entrega/saída visível no WhatsApp do cliente.

## Ações tomadas

1. Fiz um retry único após Lucas reportar que não chegou, com payload oficial:
   - `number`
   - `text`
   - `delay=1000`
   - `linkPreview=false`
2. A Evolution respondeu novamente:
   - HTTP 201
   - status `PENDING`
   - message id presente
3. Atualizei o job local para `pending_delivery_confirmation`, não `sent`.
4. Corrigi `/opt/data/scripts/lk_store_sale_restock_alert.py` para tratar `PENDING` como pendente de confirmação, não como envio confirmado.
5. Atualizei teste para cobrir esse comportamento.

## Verificação

Comandos:

```bash
python3 /opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py
python3 -m py_compile /opt/data/scripts/lk_store_sale_restock_alert.py /opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py /opt/data/profiles/lk-ops/scripts/lk_pos_postpurchase_canary_worker.py
```

Resultado:

- Testes: `ok`
- Compile: exit 0

## Estado final

- Pedido #147693 tem duas tentativas registradas na Evolution como outgoing/conversation, mas sem confirmação final de entrega.
- Não farei novos reenvios automáticos para evitar spam/duplicidade.
- Shopify/Tiny/Chatwoot/n8n não foram alterados.

## Próxima decisão recomendada

Antes de ativar o canary como “funcionando”, precisamos decidir uma validação mais forte:

1. testar envio para um número interno controlado via `LK Flagship` e confirmar visualmente no WhatsApp;
2. revisar no painel/logs da Evolution por que mensagens ficam em `PENDING`;
3. só depois retomar envios a clientes.
