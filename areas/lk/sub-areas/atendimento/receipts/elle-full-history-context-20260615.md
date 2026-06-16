# Receipt — Elle full-history context correction

- Data/hora UTC: 2026-06-15T15:20Z
- Área: LK / Atendimento / Elle / Chatwoot
- Correção humana: Lucas corrigiu que Elle não deve agrupar apenas 3 mensagens; deve usar todo o histórico de conversa disponível para entender o pedido antes de responder.
- Classificação: hotfix produção aprovado no contexto da correção operacional da Elle.

## Diagnóstico

- A alteração anterior já adicionava debounce de 15s, mas ainda havia limites pequenos demais:
  - `AI_MAX_MESSAGES` default estava em 18 mensagens;
  - `customer_burst` limitava a últimas 6 mensagens consecutivas do cliente;
  - teste sintético anterior só provava 3 mensagens porque o cenário tinha 3 linhas, não provava histórico longo.

## Alteração

- `AI_MAX_MESSAGES` default alterado de 18 para 80.
- Removido corte fixo `[-6:]` do bloco consecutivo do cliente.
- `current_customer_burst` no payload do modelo ampliado para até 6000 caracteres sanitizados.
- Prompt reforçado para usar toda a conversa disponível no Chatwoot e o contexto acumulado, nunca só a última linha.

## Observação técnica

- “Todo histórico” aqui significa todo o histórico útil retornado pela API do Chatwoot dentro do teto configurável de segurança (`ELLE_AI_MAX_MESSAGES`, default 80), para evitar estouro de token/latência e proteger operação. Não há corte pequeno de 3/6 mensagens.

## Verificação

- `python3 -m py_compile app.py`: OK.
- Teste sintético com histórico longo:
  - 25 mensagens consecutivas do cliente foram agrupadas;
  - `history_message_count=26`;
  - `not_limited_to_3_or_6=true`;
  - `values_printed=false`.
- Rebuild/recreate:
  - `docker compose up -d --no-deps --build --force-recreate elle-chatwoot`: OK.
- Readback dentro do container:
  - `AI_MAX_MESSAGES=80`;
  - `current_customer_burst[:6000]`;
  - sem `[-6:]` no `customer_burst`.
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

- Backup salvo em `/opt/elle-chatwoot/backups/lucas-full-history-20260615T151929Z/app.py`.

## Segurança

- Sem teste em cliente real.
- Sem impressão de telefone, e-mail, URL de conversa, tokens, secrets ou PII.
