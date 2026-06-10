# LK POS pós-compra / Evolution API — diagnóstico read-only

Data: 2026-06-09T15:21:53Z
Área: LK / Atendimento / Pós-compra / Evolution API LK Flagship
Modo: read-only; nenhum WhatsApp enviado; nenhuma alteração em Shopify/Evolution/cron/gateway

## Pergunta

Lucas pediu para verificar por que, quando um cliente compra na LK, Hermes/automação não está enviando a mensagem de agradecimento pela compra usando a instância Evolution API `LK Flagship Store` / `LK Flagship`.

## Fontes verificadas

- Código local: `/opt/data/scripts/lk_store_sale_restock_alert.py`
- Worker cron: `/opt/data/profiles/lk-ops/scripts/lk_pos_postpurchase_canary_worker.py`
- Cron config: `/opt/data/profiles/lk-ops/cron/jobs.json`
- Fila local: `/opt/data/hermes_bruno_ingest/local_sql/lk_store_sale_restock/pos_thankyou_queue.json`
- Estado local: `/opt/data/hermes_bruno_ingest/local_sql/lk_store_sale_restock/state.json`
- Doppler `lc-keys/prd`: presença/ausência de secrets, sem valores
- Evolution API: `GET /instance/connectionState/{instance}` via credencial geral, sem expor token
- Shopify Admin REST read-only: pedidos recentes em agregado/metadata, sem telefone/nome de cliente
- Gateway code: `/opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages/gateway/platforms/webhook.py`

## Achados

### 1. Evolution API / LK Flagship está conectada

Checagem read-only retornou:

- `base_present=true`
- `api_key_present=true`
- `instance_name_present=true`
- `instance_name_is_lk_flagship=true`
- `connection_http_status=200`
- `connection_state=open`

Conclusão: a instância Evolution não parece ser o bloqueio primário neste momento.

### 2. O worker de pós-compra está explicitamente pausado para envio real

Arquivo:

`/opt/data/profiles/lk-ops/scripts/lk_pos_postpurchase_canary_worker.py`

Linha crítica:

```python
LIVE_SEND_ENABLED = False  # Paused 2026-06-06: Evolution sends reached SERVER_ACK but not DELIVERY_ACK for first customer canary.
```

Mesmo quando o cron roda, ele chama:

```python
process_due_pos_thankyou_jobs(live=LIVE_SEND_ENABLED, canary_limit=3)
```

Com `LIVE_SEND_ENABLED=False`, o worker não deve enviar WhatsApp real.

### 3. O guardrail de live send também está ausente no Doppler

Doppler `lc-keys/prd`:

- `EVOLUTION_API_BASE_URL`: OK
- `EVOLUTION_API_URL`: OK
- `EVOLUTION_API_KEY`: OK
- `EVOLUTION_API_TOKEN`: OK
- `EVOLUTION_LK_FLAGSHIP_KEY`: OK
- `EVOLUTION_INSTANCE`: OK
- `EVOLUTION_INSTANCE_NAME`: OK
- `EVOLUTION_LK_FLAGSHIP_INSTANCE`: MISSING
- `LK_POS_POSTPURCHASE_LIVE_SEND`: MISSING

No CLI principal, envio real só passa se:

```python
args.live and os.getenv('LK_POS_POSTPURCHASE_LIVE_SEND') == '1'
```

Como `LK_POS_POSTPURCHASE_LIVE_SEND` está ausente, uma execução `--live` fora do worker também seria bloqueada.

### 4. A fila local não está recebendo pedidos POS recentes

Fila local:

- `last_updated_at`: `2026-06-06T14:52:16Z`
- `last_worker_run_at`: `2026-06-06T15:05:43Z`
- `jobs_total`: `11`
- `scheduled_due_now`: `0`
- `scheduled_total`: `0`
- `live_executed_total`: `1`
- status atuais: `pending_delivery_confirmation=6`, `delivered=5`

Shopify read-only desde `2026-06-06T14:52:16Z`:

- pedidos retornados: `35`
- POS pagos elegíveis: `10`
- POS pagos recentes tinham `phone_present=true` e `tags_has_vendedor=true`

Exemplos de pedidos POS elegíveis em metadata:

- `#147727` — POS paid — `2026-06-09T12:07:58-03:00`
- `#147720` — POS paid — `2026-06-08T15:58:49-03:00`
- `#147719` — POS paid — `2026-06-08T15:44:48-03:00`
- `#147718` — POS paid — `2026-06-08T15:42:15-03:00`
- `#147712` — POS paid — `2026-06-08T10:26:52-03:00`

Conclusão: além do worker estar pausado, o caminho de ingresso/enfileiramento de compras POS recentes não está persistindo jobs novos na fila.

### 5. Cron existe e roda, mas não envia por causa do pause/no-due

Cron:

- job id: `lk-pos-postpurchase-canary`
- schedule: `*/5 * * * *`
- enabled: `true`
- last status: `ok`
- última execução observada: `2026-06-09T15:15:51Z`
- saída: `silent (wakeAgent=false)`

Isso indica que o cron acorda, mas não tem jobs due e/ou está em dry-run/pause.

### 6. Gateway atual tem handler determinístico, mas precisa validar caminho público/proxy

Código do gateway atual contém branch:

```python
if route_config.get("kind") == "lk_shopify_pos_restock":
    return await self._handle_lk_shopify_pos_restock_webhook(...)
```

E o handler chama:

```python
restock.process_shopify_order_webhook(payload, delivery_id=delivery_id, topic=event_type)
```

Porém a fila local não recebe os POS recentes. O próximo diagnóstico seguro é validar a cadeia pública completa:

Shopify webhook → Vercel/proxy `hermes-webhooks` → Hermes gateway → handler `lk_shopify_pos_restock` → `pos_thankyou_queue.json`.

Atenção: um retorno `202 accepted` do webhook não prova sucesso; ele pode indicar caminho genérico. O correto para esse handler é resposta `200` com campos como `sent_count`, `queued_count`, `order_id`, `queue_id`, `reason`.

## Veredito

A mensagem de agradecimento pós-compra não está saindo por uma combinação de bloqueios:

1. **Envio real pausado no worker** (`LIVE_SEND_ENABLED=False`).
2. **Flag de live send ausente no Doppler** (`LK_POS_POSTPURCHASE_LIVE_SEND` missing), bloqueando envio real no CLI.
3. **Fila local sem novos jobs desde 06/06**, apesar de haver POS pagos elegíveis depois disso; o ingress/enfileiramento via Shopify/webhook/proxy precisa ser verificado.
4. **Evolution LK Flagship está open**, então o problema primário não parece ser a conexão da instância.

## O que não foi feito

- Nenhum WhatsApp enviado.
- Nenhuma alteração no worker, cron, gateway, Vercel, Evolution, Shopify ou Doppler.
- Nenhum telefone/token/secret/payload bruto foi impresso ou salvo.

## Próximo passo recomendado

Preparar approval packet para reativação controlada:

1. Validar e corrigir, se necessário, o ingress Shopify/Vercel/Hermes para garantir que POS paid enfileira job novo.
2. Rodar probe assinado controlado e exigir resposta determinística `200` do handler, não `202 accepted`.
3. Manter customer send desligado até o enfileiramento estar provado.
4. Depois, só com aprovação explícita, reativar canário:
   - setar `LK_POS_POSTPURCHASE_LIVE_SEND=1` no escopo correto; e/ou
   - mudar `LIVE_SEND_ENABLED=True` no worker;
   - começar com canary limit baixo e mensagem aprovada.
5. Tratar `201/PENDING` da Evolution como aceitação de API, não entrega; exigir `DELIVERY_ACK`/confirmação forte antes de declarar entregue.
