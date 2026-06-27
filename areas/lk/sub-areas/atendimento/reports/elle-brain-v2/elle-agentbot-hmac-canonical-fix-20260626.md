# Elle / Chatwoot AgentBot — HMAC canonical fix

Data: 2026-06-26
Status: done
values_printed=false
writes_external: Chatwoot AgentBot outgoing_url update; Doppler secret write; Elle container recreate/build

## Objetivo
Corrigir integração Elle ↔ Chatwoot AgentBot para seguir o padrão oficial Chatwoot: endpoint limpo + `X-Chatwoot-Signature`/`X-Chatwoot-Timestamp` HMAC-SHA256 sobre `{timestamp}.{raw_body}`.

## Mudanças executadas
- Secret do `AgentBot.secret` sincronizado para Doppler `lc-keys/prd` como `ELLE_AGENTBOT_WEBHOOK_SECRET` sem imprimir valor.
- `/opt/elle-chatwoot/docker-compose.yml` passou a injetar `ELLE_AGENTBOT_WEBHOOK_SECRET`.
- `/opt/elle-chatwoot/env.manifest.json` atualizado com secret obrigatório.
- `/opt/elle-chatwoot/app/app.py` endurecido:
  - `hmac_secret_present` no health;
  - `legacy_path_webhook_enabled=false` por padrão;
  - endpoint legado `/webhooks/chatwoot/<secret>` só funciona se `ELLE_LEGACY_PATH_WEBHOOK_ENABLED=true`.
- AgentBot `Elle` no Chatwoot atualizado para URL limpa: `/webhooks/chatwoot-agentbot`.
- Imagem `elle-chatwoot:canonical-20260623` rebuildada e container recriado via script Doppler-safe.

## Evidência

### Health
```json
{"ok": true, "hmac_secret_present": true, "legacy_path_webhook_enabled": false, "dry_run": false, "write_enabled": true, "public_reply_enabled": true, "elle_brain_v2_canary_enabled": true, "elle_brain_v2_canary_percent": 100}
```

### Probes HMAC sem envio a cliente
```text
signed_status=202 body={"ok": true, "status": "ignored"}
unsigned_status=401
legacy_status=404
values_printed=false
```

### Chatwoot readback
```json
{"agent_bot_id": 1, "host": "elle.lkskrs.online", "path": "/webhooks/chatwoot-agentbot", "https": true, "secret_present": true, "values_printed": false}
```

### Gates finais
```text
check_drift.sh: status=ok values_printed=false
regression: {"ok": true, "tests": 38, "values_printed": false}
learner: status=ok, lessons_total=15, v2_lessons_loaded=8, writes_external=0
OpenRouter 1h: OK, v2_errors=0, provider_errors=0
autonomy_gate: hold, eval_bad=3, eval_medium_high=1, handoff_violations=0
```

## Rollback
Backup/snapshot:
`/opt/data/backups/elle-agentbot-hmac-canonical/20260626T205157Z`

Rollback possível:
1. Restaurar `app.py`, `docker-compose.yml`, `Dockerfile`, script de recreate do backup.
2. Restaurar AgentBot outgoing_url do arquivo `agentbot_outgoing_url.rollback` no backup.
3. Rebuild/recreate Elle via `/opt/elle-chatwoot/scripts/recreate_elle_doppler_safe.sh`.

## Status remanescente
- AgentBot/HMAC agora está canônico.
- Autonomia ampla da Elle continua bloqueada: `autonomy_gate=hold`; não expandir além de 100% safe-only.
