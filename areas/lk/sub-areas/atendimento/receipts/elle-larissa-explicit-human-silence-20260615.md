# Receipt — Elle silêncio quando cliente chama Larissa/atendente

- Data/hora UTC: 2026-06-15T15:26Z
- Área: LK / Atendimento / Elle / Chatwoot
- Correção humana: Lucas mostrou conversa onde a cliente chamou “Larissa” diretamente e Elle respondeu publicamente. Regra correta: se cliente chama Larissa ou pede humano/atendente, Elle não deve responder publicamente.
- Classificação: hotfix produção aprovado no contexto de correção operacional da Elle.

## Diagnóstico

- O código tinha handoff para casos sensíveis, mas ainda podia produzir resposta pública de `human_handoff`.
- Não havia guard determinístico forte para: `Larissa ...` / `falar com Larissa` / `falar com atendente` / `chamar humano`.
- O print também mostrava conversa atribuída a Giselia; se o webhook de assignment for perdido ou o container reiniciar, a Elle precisava revalidar `assignee_id` no inbound e ficar em silêncio.

## Alteração

- Adicionado `is_explicit_human_or_larissa_request(text)`.
- Adicionado `explicit_human_or_larissa_result(flat)` com:
  - `handoff=true`;
  - `category=human_handoff`;
  - `reply=''`;
  - `blocked_reasons=['explicit_larissa_or_human_request_no_public_reply']`;
  - labels `humano` e `explicit_human_request`.
- `classify()` agora checa esse caso antes do Gemini e antes de qualquer regra que gere resposta pública.
- `process_incoming_flat()` agora bloqueia automaticamente se o inbound já vier com `assignee_id`, criando lock `human_assignee_existing` e sem enviar resposta pública.

## Verificação

- `python3 -m py_compile app.py`: OK.
- Teste sintético local:
  - mensagem “Larissa vc iniciou...” => `handoff=true`, `reply=''`, motivo explícito presente;
  - mensagem “quero falar com uma atendente...” => `handoff=true`, `reply=''`, motivo explícito presente;
  - inbound com `assignee_id=2` => bloqueado por `human_assignee_existing` antes de responder;
  - saudação normal não aciona o novo guard explícito.
- Rebuild/recreate:
  - `docker compose up -d --no-deps --build --force-recreate elle-chatwoot`: OK.
- Readback no container novo:
  - `is_explicit_human_or_larissa_request` presente;
  - motivo `explicit_larissa_or_human_request_no_public_reply` presente;
  - guard `human_assignee_existing` presente.
- Smoke dentro do container em produção:
  - `larissa_reply_blank=true`;
  - `larissa_handoff=true`;
  - `explicit_reason=true`;
  - `assigned_blocks=human_assignee_existing`;
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

- Backup salvo em `/opt/elle-chatwoot/backups/lucas-larissa-silence-20260615T152412Z/app.py`.

## Segurança

- Sem envio de teste para cliente real.
- Sem impressão de telefone, e-mail, URL de conversa, tokens, secrets ou PII.
