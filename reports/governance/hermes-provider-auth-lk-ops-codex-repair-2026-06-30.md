# LK Ops provider auth repair — openai-codex — 2026-06-30

- values_printed: false
- profile: `lk-ops`
- scope: profile-local auth + scoped gateway restart only
- external_writes: 0
- Docker/VPS/Traefik/Main touched: no

## Problema

Auditoria all-agents encontrou falha atual no `lk-ops`:

- provider/model: `openai-codex` / `gpt-5.5`
- symptom: HTTP 401 / `token_expired`
- log window: `2026-06-30 16:47–16:48 UTC`
- causa provável: `auth.json` profile-local divergente do default e bloco local `providers.openai-codex` sombreando credencial válida.

## Ação executada após aprovação de Lucas

1. Backup local criado em `/opt/data/backups/lk-ops-codex-auth-repair-20260630T170418Z/`.
2. Sincronizado somente `credential_pool.openai-codex` do default para `/opt/data/profiles/lk-ops/auth.json`.
3. Removido bloco local `providers.openai-codex` porque default não usa provider-local equivalente.
4. Validado JSON do `auth.json`.
5. Smoke profile-local antes do restart: `OK`, sem 401/token_expired/auth error; `rc=134` classificado como abort/shutdown não fatal pós-output.
6. Restart scoped somente do gateway `lk-ops`:
   - pre PID: `46223`
   - post PID: `1489108`
7. Readback runtime:
   - Telegram getMe: `ok`, username `LKOps_HermesBot`
   - API server: `false`
   - webhook: `false`
   - Telegram token present: `true` como boolean
   - allowlist present: `true` como boolean
   - `DOPPLER_TOKEN` in child: `false`
8. Smoke pós-restart: `OK`, sem 401/token_expired/auth error.

## Rollback

Restaurar:

- `/opt/data/backups/lk-ops-codex-auth-repair-20260630T170418Z/auth.json.before`
- `/opt/data/backups/lk-ops-codex-auth-repair-20260630T170418Z/config.yaml.before`

para `/opt/data/profiles/lk-ops/`, e reiniciar somente o gateway `lk-ops`.

## Resultado

`lk-ops` corrigido e funcionando no smoke local. As linhas 401 remanescentes no log são anteriores à correção (`16:47–16:48 UTC`); não houve 401/token_expired no smoke pós-reparo.
