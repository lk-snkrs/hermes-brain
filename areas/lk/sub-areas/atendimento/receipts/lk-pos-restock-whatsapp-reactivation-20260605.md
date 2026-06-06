# Receipt — LK POS restock WhatsApp reativado

Data UTC: 2026-06-05
Executor: LK Ops / Atendimento
Aprovação: Lucas aprovou religar LK POS restock no escopo do approval packet, com diagnóstico de secrets sem imprimir valores, correção mínima se necessária, teste não-POS sem WhatsApp/Notion e teste POS controlado no `[LK] Team`; sem Shopify/Tiny/estoque/preço, sem fornecedor/cliente, com rollback.

## Escopo executado

- Diagnóstico secret-safe Vercel/Shopify/Hermes.
- Testes via endpoint público Vercel `https://hermes-webhooks.vercel.app/webhooks/lk-shopify-pos-restock`.
- Correção local mínima no responder para preservar estado ativo da decisão quando o alerta é enviado como texto.
- Teste POS controlado no grupo interno `[LK] Team`.
- Encerramento controlado da pendência de teste com decisão `não` sintética local, sem Notion.

## Secret/env snapshot sem valores

Comparações por fingerprint não reversível/presença; nenhum valor foi impresso.

- Doppler `SHOPIFY_WEBHOOK_SECRET`: presente, len 44, fingerprint `e6dd33e6ffaa`.
- Vercel production `SHOPIFY_WEBHOOK_SECRET`: presente, len 44, fingerprint `e6dd33e6ffaa`.
- Doppler `HERMES_WEBHOOK_SECRET`: presente, len 64, fingerprint `d36bcf7450d4`.
- Vercel production `HERMES_WEBHOOK_SECRET`: presente, len 64, fingerprint `d36bcf7450d4`.
- Rota Hermes `lk-shopify-pos-restock` secret: presente, len 64, fingerprint `d36bcf7450d4`.

Resultado: secrets estavam alinhados. **Nenhum env Vercel/Shopify/Hermes foi alterado.**

## Shopify webhook read-only

Webhook Shopify confirmado:

- `id`: `1641004826846`
- `topic`: `orders/paid`
- `address`: `https://hermes-webhooks.vercel.app/webhooks/lk-shopify-pos-restock`
- `created_at`: `2026-05-23T17:52:30-03:00`
- `updated_at`: `2026-05-23T17:52:30-03:00`

Nenhuma alteração Shopify feita.

## Teste não-POS via Vercel

Payload assinado com HMAC Shopify correto, `source_name=web`, tópico `orders/paid`.

Resultado:

```json
{"status":"ignored","reason":"not_paid_active_pos_order","topic":"orders/paid","write_executed":false}
```

HTTP: `202`.

Efeito: sem WhatsApp, sem Notion, sem Shopify/Tiny.

## Bug encontrado durante teste POS

O primeiro teste POS enviou alerta, mas a fila ficou `queued`/não ativa porque `send_sale_restock_alert()` retornava `None` quando o alerta era enviado como texto. A função `register_queue_in_responder_state()` só ativava a decisão quando `message_result is not None`.

Efeito prático: o grupo recebia o alerta, mas uma resposta `sim`/`não` poderia não ser tratada como decisão ativa.

## Correção aplicada

Arquivo alterado:

- `/opt/data/scripts/lk_hermes_whatsapp_responder.py`

Mudança mínima:

```diff
-    if image_path:
-        return send_file(chat_jid, image_path, caption[:1000])
-    send_text(chat_jid, caption[:3500])
-    return None
+    if image_path:
+        result = send_file(chat_jid, image_path, caption[:1000])
+        return result or {"status": "sent_image"}
+    send_text(chat_jid, caption[:3500])
+    return {"status": "sent_text"}
```

Motivo: garantir que envio por texto também retorne resultado não-nulo, ativando a pendência `awaiting_decision`.

## Validação local pós-correção

Comando:

```bash
python3 -m py_compile /opt/data/scripts/lk_store_sale_restock_alert.py /opt/data/scripts/lk_hermes_whatsapp_responder.py && python3 /opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py
```

Resultado: `ok`.

## Teste POS controlado via Vercel

Payload sintético POS:

- `source_name`: `pos`
- `app_id`: `129785`
- `financial_status`: `paid`
- pedido: `#TESTE-POS-RESTOCK-ATIVO-NAO`
- SKU: `TESTE-HERMES-ATIVO-NAO`
- produto: `TESTE HERMES POS RESTOCK ATIVO — RESPONDER NÃO`

Resposta do endpoint:

```json
{"status":"sent","order_id":"9900000000608","queue_id":"d548f65f4c1e8116","sent_count":1,"queued_count":1,"queued_behind_active":false,"write_executed":false}
```

HTTP: `202`.

Estado verificado após envio:

```json
{"pending_count":1,"active_count":1,"status":"awaiting_decision","codigo":"TESTE-HERMES-ATIVO-NAO"}
```

## Encerramento do teste

Para não deixar pendência de teste aberta, foi enviado POST local sintético ao responder com decisão `não` para o grupo `[LK] Team`.

Resultado:

- endpoint local `127.0.0.1:8787/wacli` retornou `200 ok`;
- pendências POS restock após decisão: `pending_count=0`, `active_count=0`;
- evento registrado: `request_type=pos_sale_restock_confirmation`, `advanced_next=false`;
- não houve criação de Notion porque a decisão foi `não`.

## Estado final

- Fluxo público Vercel → Hermes aceitando HMAC Shopify correto: OK.
- Rota Hermes `lk-shopify-pos-restock`: OK.
- Processor POS local: OK.
- Alerta interno WhatsApp `[LK] Team`: OK em teste controlado.
- Estado de decisão `awaiting_decision`: OK após correção.
- Resposta `não` limpa pendência: OK.
- Shopify/Tiny/estoque/preço: sem alterações.
- Vercel env: sem alterações.
- Notion: sem card criado no teste.

## Rollback

Se precisar desfazer a correção local, reverter no arquivo `/opt/data/scripts/lk_hermes_whatsapp_responder.py` para:

```python
    if image_path:
        return send_file(chat_jid, image_path, caption[:1000])
    send_text(chat_jid, caption[:3500])
    return None
```

Depois rodar:

```bash
python3 -m py_compile /opt/data/scripts/lk_store_sale_restock_alert.py /opt/data/scripts/lk_hermes_whatsapp_responder.py && python3 /opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py
```

Backup/snapshot criado:

- Estado anterior à limpeza de teste: `/opt/data/hermes_bruno_ingest/local_sql/lk_whatsapp_hermes/state.state-before-pos-restock-test-cleanup-20260605.bak`
- Snapshot pós-fix do script: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/receipts/lk_hermes_whatsapp_responder.py.after-pos-restock-fix-20260605.bak`

## Observações

- Não houve restart de gateway/container.
- A rota de webhook carrega o script local a cada processamento, então a correção aplicada ao arquivo já foi observada no teste POS seguinte.
- O processo residente do responder continua capaz de tratar `não`/`sim`; a correção aplicada afeta principalmente o retorno do envio de alerta e a ativação de novas filas geradas pelo webhook.
