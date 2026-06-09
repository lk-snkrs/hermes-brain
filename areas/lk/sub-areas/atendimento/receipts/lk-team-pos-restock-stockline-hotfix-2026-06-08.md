# Receipt — hotfix estoque atual em alertas POS restock

Data: 2026-06-08

## Pedido do Lucas
Adicionar ao alerta de reposição POS a quantidade atual em estoque, usando Tiny / `LK | CONTROLE ESTOQUE` como fonte de verdade.

## Ações executadas
- Patch em `/opt/data/scripts/lk_hermes_whatsapp_responder.py`:
  - adicionada linha `📦 Estoque atual (Tiny — LK | CONTROLE ESTOQUE): ... un.` em `sale_restock_alert_message()`;
  - leitura live/bounded por SKU exato no Tiny para itens POS/backfill;
  - fallback explícito quando não for possível validar, sem inventar saldo.
- Patch em `/opt/data/scripts/lk_store_sale_restock_alert.py`:
  - mesma linha de estoque atual no primeiro alerta enviado pelo webhook/backfill.
- Patch em `/opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py`:
  - asserts para garantir presença da linha de estoque;
  - teste explícito com `current_stock=4`.
- Verificação executada:
  - `python3 -m py_compile /opt/data/scripts/lk_hermes_whatsapp_responder.py /opt/data/scripts/lk_store_sale_restock_alert.py /opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py`
  - `python3 /opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py`
  - saída: `ok`

## Operação WhatsApp
- Responder foi reiniciado com a versão corrigida.
- Reenvio do item ativo com linha de estoque atual foi feito para o grupo LK Team.
- Após mensagens de divergência no grupo, responder/sync foram pausados para evitar novas decisões automáticas fora de contexto.

## Estado observado ao pausar
- Item ativo no estado local: `13/14`, SKU `LIP`, status `awaiting_decision`.
- Item pendente restante: `14/14`, SKU `sem código interno`.
- Processos `lk_hermes_whatsapp_responder.py --port 8787` e `wacli --account hermes sync --follow` foram interrompidos localmente.

## Guardrails
- Nenhum write em Tiny/Shopify foi executado.
- Secrets não foram registrados.
