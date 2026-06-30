# SPITI provider auth repair — openai-codex — 2026-06-30

- values_printed: false
- profile: `spiti`
- bot: `SPITI_HermesBot`
- scope: profile-local auth + scoped gateway restart only
- external_writes: 0
- Docker/VPS/Traefik/Main touched: no

## Problema

Lucas reportou `@SPITI_HermesBot` com `Provider authentication failed`.

Precheck confirmou falha atual:

- provider/model: `openai-codex` / `gpt-5.5`
- symptom: HTTP 401 / `token_expired`
- log window: `2026-06-30 19:45:20–19:45:21 UTC`
- causa provável: `auth.json` profile-local divergente do default e bloco local `providers.openai-codex` sombreando credencial válida.

## Ação executada após aprovação de Lucas

1. Backup local criado em `/opt/data/backups/spiti-codex-auth-repair-20260630T195453Z/`.
2. Sincronizado somente `credential_pool.openai-codex` do default para `/opt/data/profiles/spiti/auth.json`.
3. Removido bloco local `providers.openai-codex` porque default não usa provider-local equivalente.
4. Validado JSON do `auth.json`.
5. Smoke profile-local antes do restart: `OK`, sem 401/token_expired/auth error; `rc=134` classificado como abort/shutdown não fatal pós-output.
6. Restart scoped somente do gateway `spiti`:
   - pre PIDs: `249`, `870871`
   - post PID: `1726820`
7. Readback runtime:
   - Telegram getMe: `ok`, username `SPITI_HermesBot`
   - API server: `false`
   - webhook: `false`
   - Telegram token present: `true` como boolean
   - allowlist present: `true` como boolean
   - `DOPPLER_TOKEN` in child: `false`
8. Smoke pós-restart: `OK`, sem 401/token_expired/auth error.

## Rollback

Restaurar:

- `/opt/data/backups/spiti-codex-auth-repair-20260630T195453Z/auth.json.before`
- `/opt/data/backups/spiti-codex-auth-repair-20260630T195453Z/config.yaml.before`

para `/opt/data/profiles/spiti/`, e reiniciar somente o gateway `spiti`.

## Resultado

`spiti` corrigido e funcionando no smoke local. As linhas 401 remanescentes no log são anteriores à correção (`19:45:20–19:45:21 UTC`); não houve 401/token_expired no smoke pós-reparo.
