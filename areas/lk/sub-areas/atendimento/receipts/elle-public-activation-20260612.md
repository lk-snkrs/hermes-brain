# Receipt — Elle public reply activation (LK WhatsApp)

Data/hora UTC: 2026-06-12 18:03–18:10
Operador: Hermes LK Ops

## Aprovação recebida

Lucas aprovou explicitamente:

> “Aprovo ativar a Elle em produção no LK WhatsApp, conectando o AgentBot se necessário, ligando escrita pública apenas nas categorias aprovadas, mantendo Human Takeover Lock, com backup, rollback e teste canário.”

## Escopo executado

- Conectar/verificar AgentBot `Elle` no inbox `LK WhatsApp`.
- Ativar resposta pública controlada na Elle.
- Manter Human Takeover Lock obrigatório.
- Fazer backup, verificação e canário sintético sem exposição de secrets.

## Backups criados no VPS

Diretório: `/opt/elle-chatwoot`

- `.env.backup-public-activation-20260612T180346Z`
- `app.py.backup-public-activation-20260612T180346Z`

## Estado antes da ativação

Health de `https://elle.lkskrs.online/healthz`:

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

Secret presence local no `.env` foi verificada por booleanos, sem imprimir valores:

```json
{
  "ELLE_CHATWOOT_WEBHOOK_SECRET": true,
  "ELLE_AGENTBOT_WEBHOOK_SECRET": false,
  "ELLE_CHATWOOT_HMAC_SECRET": false,
  "ELLE_CHATWOOT_WEBHOOK_URL": false,
  "values_printed": false
}
```

Observação: `hmac_secret_present=false`; a proteção operacional confirmada é URL/path secreto já configurado no AgentBot. Nenhum valor ou path secreto foi registrado.

## Chatwoot — AgentBot conectado

Antes, a associação `AgentBotInbox` estava ausente. Foi criada/ativada a relação:

```json
{
  "connected": true,
  "agent_bot_inbox": {
    "id": 2,
    "inbox_id": 2,
    "agent_bot_id": 1,
    "account_id": 1,
    "status": "active"
  },
  "inbox_agent_bot_id": 1
}
```

Verificação posterior:

```json
{
  "inbox_id": 2,
  "bot_id": 1,
  "connected": true,
  "relation": {
    "id": 2,
    "status": "active",
    "account_id": 1
  },
  "inbox_agent_bot_id": 1
}
```

O `outgoing_url` do AgentBot foi verificado apenas por metadados redigidos:

```json
{
  "outgoing_url_present": true,
  "outgoing_scheme": "https",
  "outgoing_host": "elle.lkskrs.online",
  "outgoing_path_present": true,
  "outgoing_path_len": 83,
  "values_printed": false
}
```

## Flags ativadas

Arquivo: `/opt/elle-chatwoot/.env`

```env
ELLE_DRY_RUN=false
CHATWOOT_WRITE_ENABLED=true
ELLE_KILL_SWITCH=false
ELLE_PUBLIC_REPLY_ENABLED=true
```

Serviço recriado:

```bash
timeout 180 docker compose up -d --no-deps --force-recreate elle-chatwoot
```

## Estado após ativação

Health:

```json
{
  "ok": true,
  "mode": "agentbot_ready",
  "dry_run": false,
  "write_enabled": true,
  "kill_switch": false,
  "public_reply_enabled": true,
  "hmac_secret_present": false
}
```

Após 20s:

```json
{
  "ok": true,
  "dry_run": false,
  "write_enabled": true,
  "kill_switch": false,
  "public_reply_enabled": true
}
```

Container:

- `elle-chatwoot Up 2 minutes`
- `docker logs --tail 100`: sem `Traceback`, sem `error`.

## Canário sintético

Canário sem escrita pública em cliente real: confirmou que Human Takeover Lock continua vencendo mesmo com escrita pública ativada.

Payload sintético em conversation id `910012`:

```json
{
  "typing": [202, {"ok": true, "status": "human_lock_set"}],
  "incoming_after_typing": [202, {"ok": true, "status": "blocked_by_human_takeover", "lock_reason": "human_typing_on"}],
  "values_printed": false
}
```

Limpeza:

```json
{
  "synthetic_lock_removed": true,
  "remaining_locks": 1
}
```

Verificação posterior:

```json
{
  "total_locks": 1,
  "synthetic_910012_present": false,
  "values_printed": false
}
```

## Escopo de respostas públicas mantido

Permitido somente nas categorias já aprovadas:

- saudação / abertura;
- institucional simples;
- cupom primeira compra `ELLE5` / 5%;
- produto claro com link/contexto;
- concorrente claro com linguagem cautelosa de réplica/similar;
- pedido já enviado/em trânsito com rastreio verificado.

Transbordo/bloqueio obrigatório continua para:

- estoque/pronta entrega/tamanho disponível;
- pedido não enviado;
- atraso/problema de entrega;
- troca/devolução;
- reclamação sensível;
- reserva/desconto/negociação além de `ELLE5`;
- cancelamento/reembolso/estorno/perda;
- foto sem texto/logo/link/contexto;
- qualquer conversa com Human Takeover Lock.

## Rollback

Opção Chatwoot:

1. Settings → Inboxes → `LK WhatsApp` → Bot Configuration.
2. Remover/limpar bot `Elle`.
3. Save.

Opção VPS:

1. Restaurar `.env.backup-public-activation-20260612T180346Z`.
2. Recriar serviço:

```bash
cd /opt/elle-chatwoot
timeout 180 docker compose up -d --no-deps --force-recreate elle-chatwoot
```

Flags seguras esperadas para rollback:

```env
ELLE_DRY_RUN=true
CHATWOOT_WRITE_ENABLED=false
ELLE_KILL_SWITCH=true
ELLE_PUBLIC_REPLY_ENABLED=false
```

Se necessário, restaurar também `app.py.backup-public-activation-20260612T180346Z` e rebuild/recreate.

## Status final

Ativação concluída com sucesso operacional.

Pendente operacional recomendado: observar primeiros eventos reais no `LK WhatsApp` e confirmar que a primeira resposta pública real ocorre apenas em categoria permitida e sem Human Takeover Lock.
