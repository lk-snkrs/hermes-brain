# Daily Intelligence P2 — correções finais — 2026-06-08

## Pedido
Lucas pediu “corrigir tudo acima” após o status P2.

## Correções aplicadas

1. **Brain Sync allowlist**
   - `/opt/data/scripts/brain_sync_safe.py` agora permite artefatos JSON canônicos de governança P2:
     - `reports/governance/*.json`
     - `reports/hermes-alert-dedupe/*.json`
     - `reports/hermes-release-watch/*.json`
     - `reports/hermes-mistake-ledger/*.json`
   - Mantido bloqueio geral para scripts/config/secrets/HTML/cache; não usar `git add .`.

2. **Webhook secret literal**
   - Confirmado `SHOPIFY_WEBHOOK_SECRET` presente no Doppler.
   - Corrigido `/opt/data/scripts/hermes_doppler.py` para o perfil `default` injetar `SHOPIFY_WEBHOOK_SECRET` e `HERMES_DASHBOARD_BASIC_AUTH_SECRET` em runtime child env sem passar `DOPPLER_TOKEN` ao child.
   - Removido o campo literal `secret:` da rota `lk-shopify-pos-restock` em `/opt/data/config.yaml`, mantendo `secret_doppler: SHOPIFY_WEBHOOK_SECRET`.
   - Backup salvo em `/opt/data/backups/runtime/config-webhook-secret-doppler-only-20260609T003115Z/config.yaml`.

3. **LK Content Doppler false alert**
   - Verificado que os nomes OAuth antigos (`GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, refresh token dedicado e calendar id dedicado) não existem, mas o caminho operacional real existe via `GOOGLE_CALENDAR_CREDENTIALS_JSON` e `GMAIL_REFRESH_TOKEN_LK`.
   - Google Calendar smoke read-only passou em modo `service_account_json`, sem writes.
   - Ajustado o expected map em `/opt/data/scripts/hermes_doppler.py` e no preflight para refletir os secrets reais do `lk-content`.

4. **P2 infra deeper**
   - Reexecutado Host/Docker observability helper read-only/sanitizado.
   - Novo artefato: `reports/governance/host-docker-observability-p2-fixed-2026-06-08.json`.
   - Resultado sanitizado: `alerts_count=0`, `containers_count=2`, versões e cron status presentes.
   - Nenhum Docker/VPS/gateway/restart/Traefik/secret value foi mutado ou impresso.

## Limites preservados
- Sem external writes/source-of-truth.
- Sem restart de gateway/Docker/VPS/Traefik.
- Sem impressão de secrets; `values_printed=false`.
- Mudanças sensíveis limitadas a remover literal local após confirmar Doppler presence + runtime helper injection.
