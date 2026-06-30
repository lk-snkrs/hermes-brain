# Approval packet — reparar provider auth do `lk-ops` — 2026-06-30

- generated_at_utc: `2026-06-30T16:59:26Z`
- trigger: Lucas reportou `Provider authentication failed`; auditoria todos agentes localizou falha atual no `lk-ops`.
- values_printed: false
- risk: A2 local auth/runtime scoped

## Escopo aprovado se Lucas disser “aprovo corrigir lk-ops”

Profile único: `/opt/data/profiles/lk-ops`.

Ações:
1. Criar backup local de `auth.json` e `config.yaml`.
2. Sincronizar apenas `credential_pool.openai-codex` do default `/opt/data/auth.json` para o `lk-ops`.
3. Remover bloco local `providers.openai-codex` do `lk-ops` se estiver sombreando o pool.
4. Validar JSON e smoke `HERMES_HOME=/opt/data/profiles/lk-ops hermes -z 'Reply exactly OK'`.
5. Reiniciar somente o gateway `lk-ops` via watchdog/kill scoped por `HERMES_HOME` exato.
6. Readback: um PID vivo, Telegram connected, API/Webhook false, `DOPPLER_TOKEN` ausente, sem novo 401/token_expired.
7. Receipt Memory OS com rollback.

## Fora de escopo

- Main/default, Docker, VPS, Traefik, crons, gateway global.
- Copiar tokens para `.env` ou Brain.
- Reautenticar provider interativamente.
- Corrigir todos os profiles por batch sem nova aprovação.

## Rollback

Restaurar os arquivos do backup e reiniciar somente `lk-ops`.

## Evidência

Ver relatório: `reports/governance/hermes-all-agents-provider-auth-audit-2026-06-30.md`.
