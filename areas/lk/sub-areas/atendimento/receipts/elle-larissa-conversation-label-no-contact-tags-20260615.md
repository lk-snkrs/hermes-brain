# Receipt — Elle: tag Larissa na conversa e sem tags automáticas em clientes

- Data/hora UTC: 2026-06-15T16:03Z
- Área: LK / Atendimento / Elle / Chatwoot
- Solicitação Lucas: Elle nunca deve adicionar tag automaticamente nos clientes/contatos. Quando houver transbordo para Larissa, além de abrir/atribuir a conversa, deve adicionar uma tag na conversa para Larissa filtrar.

## Regra aplicada

- Tags/labels automáticas em cliente/contato: proibidas.
- Tags/labels automáticas em conversa: permitidas conforme fluxo operacional.
- Em qualquer `handoff=true`, Elle garante o label de conversa `larissa`.
- Larissa/Giselia poderá filtrar conversas pelo label `larissa` no Chatwoot.

## Alterações

1. Chatwoot
   - Criado label de conta/conversa `larissa`.
   - Readback: `has_larissa=true`.

2. Elle app
   - Adicionado `LARISSA_HANDOFF_LABEL = 'larissa'`.
   - Adicionada função `conversation_labels_for_result(result)`:
     - usa somente labels de conversa;
     - se `handoff=true`, adiciona `larissa` uma única vez;
     - não escreve em contato/cliente.
   - `apply_actions()` agora posta labels em `/conversations/{id}/labels` com o label `larissa` nos handoffs.
   - Comentário explícito no código: nunca escrever labels/tags no objeto de contato/cliente.

## Verificação

- `python3 -m py_compile app.py`: OK.
- Verificação local com `chatwoot` mockado:
  - handoff inclui `larissa` nos labels;
  - non-handoff não recebe `larissa` automaticamente;
  - endpoint chamado: `/conversations/<id>/labels`;
  - nenhum endpoint `/contacts` usado.
- Rebuild/recreate do container `elle-chatwoot`: OK.
- Smoke no container novo:
  - `chatwoot_has_larissa_label=true`;
  - `handoff_adds_larissa_conversation_label=true`;
  - `contact_endpoint_used=false`;
  - `values_printed=false`.
- Health público:
  - `ok=true`;
  - `write_enabled=true`;
  - `kill_switch=false`;
  - `public_reply_enabled=true`;
  - `ai_enabled=true`;
  - `ai_model=google/gemini-2.5-flash`;
  - `ai_secret_present=true`;
  - `debounce_enabled=true`;
  - `debounce_seconds=15.0`.

## Rollback

- Backup app.py: `/opt/elle-chatwoot/backups/lucas-larissa-conversation-label-no-contact-tags-20260615T160146Z/app.py`.
- Para rollback de código: restaurar backup, `python3 -m py_compile app.py`, rebuild/recreate `elle-chatwoot`.
- O label `larissa` criado no Chatwoot pode permanecer sem impacto; se Lucas quiser remover, remover manualmente/administrativamente no Chatwoot.

## Segurança

- Não foi consultado estoque.
- Não foi enviado teste em cliente real.
- Não foram impressos tokens/secrets/PII.
- Único write externo além do deploy: criação do label `larissa` no Chatwoot, conforme solicitação operacional do Lucas.
