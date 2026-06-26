# Receipt — [LK] IA Bot WhatsApp employee responder

Data: 2026-06-26
Owner: lk-ops / atendimento
Status: done

## Pedido

Lucas aprovou colocar em execução uma feature do Hermes para responder mensagens dos funcionários da LK em grupo interno WhatsApp, somente quando marcarem `@Hermes`.

Exemplo de pergunta desejada: lista de clientes que compraram determinado produto/marca/tamanho nos últimos meses.

## Escopo executado

- Grupo allowlistado: `[LK] IA Bot`.
- Trigger: somente `@Hermes`, menção numérica do bot ou reply-to-Hermes conforme lógica existente.
- Conta WhatsApp: `hermes` via `wacli`.
- Respostas: read-only, PII-minimizadas, sem write externo.

## Mudanças locais

- `/opt/data/scripts/lk_hermes_whatsapp_responder.py`
  - adicionou `[LK] IA Bot` em `TARGET_CHATS`;
  - adicionou classificação `customers` para perguntas de clientes que compraram;
  - adicionou consulta Shopify read-only em pedidos pagos/cancelados fora;
  - adicionou parser de tamanho apparel `P/M/G/GG` e numeração;
  - retorno de lista PII-minimizada: nome, contagem de itens/pedidos, último pedido/data e exemplo de item; sem telefone/e-mail no grupo.
- `/opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py`
  - adicionou regressão para `[LK] IA Bot`, parser do exemplo Essentials tamanho G e match de variante `L/G`.

Backup antes da edição:

- `/opt/data/backups/lk-ia-bot-employee-responder-20260626T084534Z/lk_hermes_whatsapp_responder.py`

## Verificação

- `python3 -m py_compile /opt/data/scripts/lk_hermes_whatsapp_responder.py` → OK.
- `/opt/hermes/.venv/bin/python -m pytest /opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py -q` → `20 passed`.
- Dry-run CLI da pergunta exemplo → `kind=customers`; Shopify read-only retornou resultado sem telefone/e-mail no output do grupo.
- `@Hermes ajuda` inclui exemplo de clientes por compra.
- Runtime local reiniciado apenas para responder WhatsApp LK:
  - `lk_hermes_whatsapp_responder.py --port 8787` rodando;
  - `wacli --account hermes sync --follow ... --webhook http://127.0.0.1:8787/wacli` rodando;
  - porta `127.0.0.1:8787` aberta;
  - `state.json` inclui `[LK] IA Bot`.

## Guardrails ativos

- Sem Shopify/Tiny/Notion/Chatwoot/Klaviyo/Meta writes.
- Sem envio externo para cliente/fornecedor.
- Sem promessa de estoque, disponibilidade, reserva, preço, prazo ou desconto.
- Customer list no grupo é PII-minimizada; contatos completos exigem pedido explícito e relatório interno, não resposta aberta no grupo.
- `values_printed=false`.

## Rollback

1. Restaurar backup para `/opt/data/scripts/lk_hermes_whatsapp_responder.py`.
2. Reiniciar somente o responder local e o `wacli sync --account hermes`.
3. Verificar `TARGET_CHATS` sem `[LK] IA Bot`, porta 8787, auth status e testes.

## Reminder OS

- Reminder OS loop needed: no.
- Owner: lk-ops.
- Review trigger: erro em pergunta real no `[LK] IA Bot`, resposta com PII excessiva, trigger sem `@Hermes`, ou pedido de ampliar para grupos operacionais.
- Evidence: testes locais, dry-run CLI e readback de runtime acima.
