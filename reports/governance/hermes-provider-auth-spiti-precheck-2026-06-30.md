# SPITI provider auth precheck — 2026-06-30

- generated_at_utc: `2026-06-30T19:47:49Z`
- profile: `spiti`
- bot: `SPITI_HermesBot`
- values_printed: false
- scope: read-only precheck; no auth copy/restart executed

## Evidence

Runtime:
- live gateway PID: `249`
- Telegram getMe: `ok`, username `SPITI_HermesBot`
- API server: `false`
- webhook: `false`
- Telegram token present: `true` as boolean
- allowlist present: `true` as boolean
- `DOPPLER_TOKEN` in child: `false`

Current auth failure:
- log files: `/opt/data/profiles/spiti/logs/agent.log`, `/opt/data/profiles/spiti/logs/errors.log`, watchdog `spiti.stdout.log`
- timestamp observed: `2026-06-30 19:45:20–19:45:21 UTC`
- provider/model: `openai-codex` / `gpt-5.5`
- error class: `AuthenticationError`, HTTP 401, `token_expired`
- fallback: `No Codex OAuth token found` / `provider not configured`

Auth structure:
- default `credential_pool.openai-codex` hash: `51e2e5091ab2`
- spiti `credential_pool.openai-codex` hash: `48131cdf6207`
- spiti has local `providers.openai-codex` block hash: `60136663bc52`
- conclusion: profile-local stale/divergent Codex auth is likely shadowing valid default pool.

Smoke:
- `HERMES_HOME=/opt/data/profiles/spiti hermes -z 'Reply exactly OK'`
- result: no final response; logs show current 401/token_expired.

## Proposed correction

Use the same bounded pattern as `lk-ops`:
1. backup `/opt/data/profiles/spiti/auth.json` and `config.yaml`;
2. copy only default `credential_pool.openai-codex` into spiti auth;
3. remove stale local `providers.openai-codex` if default has no equivalent;
4. smoke profile-local;
5. restart only `spiti` gateway by exact `HERMES_HOME`;
6. readback Telegram/API/Webhook/env booleans and smoke;
7. receipt.
