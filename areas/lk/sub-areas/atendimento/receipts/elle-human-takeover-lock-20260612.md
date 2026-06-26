# Receipt — Elle Human Takeover Lock aplicado

Data: 2026-06-12T15:08Z
Área: LK / Atendimento / Chatwoot / Elle
Executor: Hermes lk-ops

## Escopo aprovado

Lucas aprovou explicitamente:

> Aplicar o Human Takeover Lock na Elle no VPS, com backup, sem ativar resposta pública, reiniciar apenas o serviço elle-chatwoot e testar em dry-run.

## Mudanças realizadas

### Código

Arquivo alterado no VPS:

- `/opt/elle-chatwoot/app.py`

Backup criado antes do patch:

- `/opt/elle-chatwoot/app.py.backup-human-lock-20260612T150324Z`
- SHA256: `4ca88916ce11bed5b633c4eca4105786f47b21aba04afe72f5992f5341547ba2`

Novo SHA256 do app.py após patch:

- `94e48fa04aa8381652db729aab17bc755c84f3eeb986250fb892fa64c0460484`

### Configuração de segurança

Durante a verificação, o healthcheck indicou flags mais abertas do que o escopo seguro. Para cumprir o escopo aprovado de "sem ativar resposta pública", o `.env` foi ajustado para:

- `ELLE_DRY_RUN=true`
- `CHATWOOT_WRITE_ENABLED=false`
- `ELLE_KILL_SWITCH=true`
- `ELLE_PUBLIC_REPLY_ENABLED=false`

Backup do `.env`:

- `/opt/elle-chatwoot/.env.backup-human-lock-safe-flags-20260612T150532Z`

### Deploy

- Primeiro `docker restart elle-chatwoot` não carregou o código novo porque a imagem contém `COPY app.py /app/app.py`.
- Foi necessário executar rebuild/recreate apenas do serviço `elle-chatwoot`:
  - `docker compose up -d --no-deps --build --force-recreate elle-chatwoot`
- Nenhum outro serviço/container foi recriado.

## Human Takeover Lock implementado

A Elle agora cria lock por `conversation_id` quando detecta:

1. `conversation_typing_on` de agente humano
   - lock reason: `human_typing_on`
   - TTL: 10 minutos

2. `message_created`/`message_updated` com mensagem pública de agente humano
   - lock reason: `human_outgoing_message`
   - TTL: 24 horas

3. `conversation_updated` com assignee humano
   - lock reason: `human_assignee`
   - TTL: 24 horas

Antes de processar um inbound, a Elle verifica lock ativo. Se existir, retorna/loga:

- `blocked_by_human_takeover` / `human_takeover_lock`

Antes de qualquer ação externa, `apply_actions()` também revalida o lock como proteção adicional.

## Verificação

Healthcheck pós-deploy:

```json
{
  "ok": true,
  "mode": "agentbot_ready",
  "dry_run": true,
  "write_enabled": false,
  "kill_switch": true,
  "public_reply_enabled": false,
  "hmac_secret_present": false
}
```

Testes sintéticos internos, sem imprimir segredo:

- `typing_lock` → HTTP 202 / `human_lock_set`
- `incoming_after_typing_lock` → HTTP 202 / `blocked_by_human_takeover`, `lock_reason=human_typing_on`
- `outgoing_lock` → HTTP 202 / `human_lock_set`
- `incoming_after_outgoing_lock` → HTTP 202 / `blocked_by_human_takeover`, `lock_reason=human_outgoing_message`
- `assignee_lock` → HTTP 202 / `human_lock_set`
- `incoming_after_assignee_lock` → HTTP 202 / `blocked_by_human_takeover`, `lock_reason=human_assignee`
- `clean_incoming_dry_run` → HTTP 200 / `processed`, `dry_run=true`, `write_enabled=false`, `kill_switch=true`

Locks sintéticos de teste foram removidos após validação.

## Observação de produção

Após o rebuild, logs internos já mostraram locks criados para conversas reais quando houve mensagem/atualização de agente humano, confirmando que a proteção está ativa.

## Rollback

Se precisar reverter:

1. Restaurar `/opt/elle-chatwoot/app.py.backup-human-lock-20260612T150324Z` para `/opt/elle-chatwoot/app.py`.
2. Opcionalmente restaurar `.env.backup-human-lock-safe-flags-20260612T150532Z` se o objetivo for voltar ao estado anterior de flags.
3. Rodar `docker compose up -d --no-deps --build --force-recreate elle-chatwoot`.
4. Verificar `/healthz`.

## Estado final

- Human Takeover Lock: ativo.
- Resposta pública: desligada.
- Escrita Chatwoot: desligada.
- Dry-run: ligado.
- Kill switch: ligado.
