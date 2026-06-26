# Receipt — LK IA Bot ack before slow customer lookups

Data: 2026-06-26
Owner: lk-ops / atendimento
Status: done

## Pedido

Lucas pediu que, ao receber mensagens como:

`@Hermes me manda a lista de clientes que compraram Roupas da Essentials no tamanho G nos últimos 6 meses`

Hermes responda imediatamente com algum feedback do tipo “recebi, estou procurando”, antes de terminar a consulta.

## Executado

- Adicionado ack best-effort antes de queries lentas classificadas como `customers`.
- Mensagem de ack:
  - `Claro — recebi. Um minuto enquanto consulto a base com segurança.`
- O ack só roda depois do gate de menção/reply-to-Hermes e grupo allowlistado.
- Se o ack falhar, a resposta final continua; erro fica em log sanitizado.

## Arquivos

- `/opt/data/scripts/lk_hermes_whatsapp_responder.py`
- `/opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py`
- Skill reference atualizada: `wacli-whatsapp-cli/references/lk-ia-bot-employee-responder-20260626.md`

Backup:

- `/opt/data/backups/lk-ia-bot-ack-before-slow-query-20260626T085734Z/lk_hermes_whatsapp_responder.py`

## Verificação

- `python3 -m py_compile /opt/data/scripts/lk_hermes_whatsapp_responder.py` → OK.
- `/opt/hermes/.venv/bin/python -m pytest /opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py -q` → `21 passed`.
- Probe local confirmou:
  - `kind=customers`
  - `ack=Claro — recebi. Um minuto enquanto consulto a base com segurança.`
- Teste unitário confirmou ordem: ack primeiro, resposta final depois.
- Responder e `wacli sync` reiniciados; porta 8787 aberta; `[LK] IA Bot` ativo no state.

## Guardrails

- Sem Shopify/Tiny/Notion/Chatwoot/Klaviyo writes.
- Sem envio proativo: ack só responde mensagem marcada com `@Hermes`/reply em grupo allowlistado.
- Sem telefone/e-mail/endereço no grupo.
- values_printed=false.

## Rollback

Restaurar backup acima, reiniciar somente responder local + `wacli sync`, e rodar testes.
