# Receipt — LK POS pós-venda WhatsApp 30min dry-run sem n8n

Data UTC: 2026-06-05T18:28:49Z

## Pedido aprovado por Lucas

Implementar em modo dry-run/local o pós-venda POS 30min sem n8n, reaproveitando o webhook Hermes de venda Shopify existente, sem envio WhatsApp real, sem alterar Shopify/Tiny/Chatwoot/n8n, apenas criando fila local/dedupe/preview de mensagem e receipts no Brain.

## Escopo executado

- Arquivo alterado: `/opt/data/scripts/lk_store_sale_restock_alert.py`.
- Teste alterado: `/opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py`.
- Integração: no fluxo existente `process_shopify_order_webhook(...)`, após validação de pedido Shopify POS pago/não cancelado, cria job local dry-run para pós-venda.
- Persistência local: `STATE_DIR / 'pos_thankyou_queue.json'`, atualmente resolvendo para `/opt/data/hermes_bruno_ingest/local_sql/lk_store_sale_restock/pos_thankyou_queue.json` em runtime normal.

## Comportamento implementado

- Agenda preview para `created_at/processed_at + 30 minutos`.
- Extrai primeiro nome do cliente.
- Extrai vendedor por tag Shopify case-insensitive no formato `vendedor:NOME` / `Vendedor: NOME`.
- Normaliza telefone brasileiro básico para dígitos com prefixo `55` quando aplicável.
- Gera `message_preview` com a copy aprovada do antigo fluxo.
- Faz dedupe por `order_id` no ledger local.
- Registra `missing_phone` quando não houver telefone, sem agendar envio real.
- Marca explicitamente `dry_run: true`, `send_executed: false`, `external_write_executed: false`.

## Guardrails

- Nenhum write em Shopify/Tiny/Chatwoot/n8n.
- Nenhum envio WhatsApp para cliente.
- Não recriou webhook Shopify.
- Não religou n8n.
- O alerta interno de reposição POS existente não foi removido nem substituído; a alteração apenas adiciona ledger/preview local do pós-venda no mesmo evento já existente.

## Verificação

RED observado:

```text
python3 - <<'PY'
import importlib.util, pathlib
p=pathlib.Path('/opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py')
spec=importlib.util.spec_from_file_location('t', p)
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
mod.test_webhook_enqueues_pos_thankyou_dry_run_preview_without_customer_send()
PY
```

Falhou antes da implementação com:

```text
KeyError: 'postpurchase_thankyou'
```

GREEN/final:

```text
python3 /opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py
# ok
```

Syntax:

```text
python3 -m py_compile /opt/data/scripts/lk_store_sale_restock_alert.py /opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py
# exit 0
```

## Próxima etapa recomendada

Rodar em observação por 1–3 vendas POS reais e conferir apenas o arquivo local `pos_thankyou_queue.json` antes de aprovar qualquer envio real. Para envio real, preparar novo approval packet com canal/remetente, canary de 1 cliente, kill switch e rollback.
