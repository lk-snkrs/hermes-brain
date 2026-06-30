# Approval packet — reparar provider auth do `spiti` — 2026-06-30

- generated_at_utc: `2026-06-30T19:47:49Z`
- trigger: Lucas reportou `@SPITI_HermesBot` com `Provider authentication failed`.
- values_printed: false
- risk: A2 local auth/runtime scoped

## Escopo solicitado

Profile único: `/opt/data/profiles/spiti`.

Ações propostas:
1. Criar backup local de `auth.json` e `config.yaml`.
2. Sincronizar apenas `credential_pool.openai-codex` do default `/opt/data/auth.json` para `/opt/data/profiles/spiti/auth.json`.
3. Remover bloco local `providers.openai-codex` do `spiti` se estiver sombreando o pool.
4. Validar JSON e smoke `HERMES_HOME=/opt/data/profiles/spiti hermes -z 'Reply exactly OK'`.
5. Reiniciar somente o gateway `spiti` via PID exato por `HERMES_HOME` e watchdog gerenciado.
6. Readback: um PID vivo, Telegram `SPITI_HermesBot`, API/Webhook false, `DOPPLER_TOKEN` ausente, sem novo 401/token_expired.
7. Receipt Memory OS com rollback.

## Fora de escopo

- Main/default, Docker, VPS, Traefik, crons, gateway global.
- Outros profiles.
- Copiar tokens para `.env` ou Brain.
- Reautenticação interativa.
- Writes externos SPITI/Hub/GitHub/Vercel/Supabase.

## Rollback

Restaurar os arquivos do backup e reiniciar somente `spiti`.

## Evidence

Ver relatório: `reports/governance/hermes-provider-auth-spiti-precheck-2026-06-30.md`.
