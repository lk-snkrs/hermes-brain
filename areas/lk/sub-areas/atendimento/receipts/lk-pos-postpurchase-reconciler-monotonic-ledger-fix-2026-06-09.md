# LK POS pós-compra — correção local do reconciliador monotônico

Data: 2026-06-09T17:15:33Z
Área: LK / Atendimento / Pós-compra / Evolution API / ledger local
Escopo: correção local segura; sem envio WhatsApp; sem ativar cron/worker; sem writes Shopify/Tiny/Chatwoot/Vercel/Doppler.

## Contexto

Após o lote final, o gateway confirmou para `#147719`:

```text
2026-06-09 17:03:47 status=server_ack matched=1 updated=1 hash=4a4a75f42431
2026-06-09 17:03:48 status=delivered matched=1 updated=1 hash=4a4a75f42431
```

Mesmo assim, o ledger local ficou em `server_ack`. A causa provável não era apenas ordem de eventos: o código já evitava rebaixar `delivered` se lesse estado atual. A hipótese confirmada foi corrida de webhooks concorrentes com read-modify-write da fila inteira: um processo stale de `server_ack` pode salvar depois de `delivered` e sobrescrever status mais forte.

## Arquivo alterado

`/opt/data/scripts/lk_evolution_delivery_reconciler.py`

## Backup de código

`/opt/data/scripts/lk_evolution_delivery_reconciler.py.bak-20260609T171319Z`

## Mudança aplicada

Adicionado merge monotônico no salvamento da reconciliação:

- ranking de status:
  - `pending_delivery_confirmation` / `sent`
  - `server_ack`
  - `delivered`
  - `read`
  - erros terminais
- antes de salvar, o reconciliador recarrega a fila mais recente do disco;
- mescla o job reconciliado no estado mais recente;
- preserva o status mais forte;
- anexa `delivery_updates` e aliases sem duplicar;
- evita que `server_ack` stale sobrescreva `delivered`/`read`.

## Teste adicionado

`/opt/data/scripts/tests/test_lk_evolution_delivery_reconciler.py`

Casos cobertos:

- `save_pos_thankyou_queue_monotonic` não rebaixa `delivered` quando recebe fila stale com `server_ack`;
- ranking preserva `read > delivered > server_ack`.

## Verificação executada

Como `pytest` não está instalado no Python padrão, foi executado runner mínimo sem dependências para a regressão crítica.

Resultado:

```json
{
  "status": "ok",
  "saved_status": "delivered",
  "updates": [
    "delivered",
    "server_ack"
  ]
}
```

Também executado:

```text
python3 -m py_compile /opt/data/scripts/lk_evolution_delivery_reconciler.py /opt/data/scripts/tests/test_lk_evolution_delivery_reconciler.py
```

Resultado: OK.

## Reparo local do ledger `#147719`

Com base no evento entregue confirmado no gateway, o status local de `#147719` foi ajustado para `delivered` e recebeu nota de reparo sanitizada.

Backup da fila antes do reparo:

`/opt/data/hermes_bruno_ingest/local_sql/lk_store_sale_restock/backups/pos_thankyou_queue.pre-ledger-monotonic-repair-20260609T171520Z.json`

## Estado final da fila

```json
{
  "jobs_total": 21,
  "status_counts": {
    "pending_delivery_confirmation": 6,
    "delivered": 12,
    "send_error": 2,
    "read": 1
  },
  "scheduled_remaining": 0,
  "live_executed_total": 9,
  "job_147719": [
    {
      "status": "delivered",
      "has_repair_note": true
    }
  ]
}
```

## Observações

- Não houve novo envio externo.
- Não houve ativação de worker automático.
- Não houve alteração em secrets, webhook público, Shopify, Tiny ou Chatwoot.
- Antes de reativar automação recorrente, ainda falta resolver/confirmar o ingresso Shopify/Vercel que gerou 401 e exigiu reconciliação manual.
