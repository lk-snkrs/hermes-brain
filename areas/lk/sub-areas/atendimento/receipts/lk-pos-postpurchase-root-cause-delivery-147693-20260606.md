# Receipt — root cause pós-venda POS #147693 não entregue

Data: 2026-06-06

## Pedido de Lucas

Lucas informou que a mensagem não chegou e pediu para continuar/verificar onde está o erro.

## Investigação read-only / sem novo envio

Fontes consultadas:

- Fila local: `/opt/data/hermes_bruno_ingest/local_sql/lk_store_sale_restock/pos_thankyou_queue.json`
- Evolution API read-only:
  - `GET /instance/connectionState/LK Flagship`
  - `GET /settings/find/LK Flagship`
  - `GET /webhook/find/LK Flagship`
  - `POST /chat/whatsappNumbers/LK Flagship`
  - `POST /chat/findMessages/LK Flagship`
- Referências Brain do teste interno que Lucas havia recebido em 2026-06-05.

## Evidência encontrada

### Instância

- `LK Flagship`: `state=open`.
- Número do pedido: validado como WhatsApp existente (`exists=true`). Telefone não registrado neste receipt.

### Mensagens do pedido #147693

- Foram encontradas 2 mensagens outgoing para o JID do cliente.
- Ambas têm:
  - `fromMe=true`
  - `messageType=conversation`
  - `source=web`
  - texto correto iniciado por `Oi Thais...`
  - `MessageUpdate` com status `SERVER_ACK`
- Nenhuma das duas mostrou `DELIVERY_ACK`.

### Comparação com teste interno recebido por Lucas

- Mensagens internas de teste para número controlado tinham `MessageUpdate` com `DELIVERY_ACK`.
- Isso diferencia o caso que chegou do caso da cliente.

### Webhook/status reconciliation

- `GET /webhook/find/LK Flagship` retornou vazio/nulo.
- Ou seja: não há webhook Evolution configurado para receber/registrar eventos de delivery/status.

## Root cause / veredito técnico

O erro principal não está no Shopify nem na criação da fila. O webhook capturou o pedido e a API Evolution aceitou o envio.

A falha está na etapa de confirmação/entrega WhatsApp via Evolution:

- a mensagem chegou até o servidor WhatsApp (`SERVER_ACK`),
- mas não recebeu confirmação de entrega ao aparelho/conta da cliente (`DELIVERY_ACK`),
- e o sistema estava tratando `PENDING`/HTTP 201 como envio confirmado.

Portanto, o bug operacional é duplo:

1. **classificação otimista demais**: `PENDING`/`SERVER_ACK` foi reportado como “sent”; deveria ser `pending_delivery_confirmation` até `DELIVERY_ACK` ou evidência visual;
2. **canary sem reconciliação de status**: como o webhook Evolution está vazio, o fluxo não tem como atualizar automaticamente entrega/falha.

## Correções aplicadas localmente

1. `/opt/data/scripts/lk_store_sale_restock_alert.py`
   - `PENDING` agora vira `pending_delivery_confirmation`, não `sent`.
   - Teste atualizado para essa regra.
2. `/opt/data/profiles/lk-ops/scripts/lk_pos_postpurchase_canary_worker.py`
   - `LIVE_SEND_ENABLED=False` para pausar novos envios reais enquanto a entrega não está comprovada.

## Verificação

Comando:

```bash
python3 /opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py
python3 -m py_compile /opt/data/scripts/lk_store_sale_restock_alert.py /opt/data/profiles/lk-ops/scripts/lk_pos_postpurchase_canary_worker.py
python3 /opt/data/profiles/lk-ops/scripts/lk_pos_postpurchase_canary_worker.py
```

Resultado:

- Testes: `ok`
- Compile: exit 0
- Worker: `live=false`, `status=dry_run`, sem novo envio real.

## O que não fiz

- Não reenviei novamente para a cliente nesta investigação.
- Não alterei Shopify/Tiny/Chatwoot/n8n.
- Não configurei webhook Evolution nem mexi em produção externa.

## Próximos passos recomendados

1. Manter canary pausado.
2. Fazer teste controlado LK Flagship → número interno e exigir `DELIVERY_ACK`/confirmação visual.
3. Configurar reconciliação de status Evolution, via webhook ou polling seguro de `MessageUpdate`, antes de religar o canary.
4. Só voltar a cliente real depois que `SERVER_ACK` e `DELIVERY_ACK` estiverem separados no ledger.
