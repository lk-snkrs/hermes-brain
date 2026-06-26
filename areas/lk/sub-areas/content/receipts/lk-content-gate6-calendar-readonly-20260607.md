# Receipt — LK Content Gate 6 Google Calendar read-only — 2026-06-07

Data/hora BRT: 2026-06-07 17:01

## Escopo executado

Lucas aprovou seguir com o Gate 6. Foi executado um one-shot local/script-only para checar Google Calendar read-only no perfil `lk-content`, usando Doppler-first e sem external writes.

## Execução real

- Job one-shot: `dccf797d99da`
- Modo: `no_agent` / script local
- Output local: `/opt/data/profiles/lk-content/cron/output/dccf797d99da/2026-06-07_20-01-26.md`
- Script: `/opt/data/profiles/lk-content/scripts/gate6_calendar_readonly_check.py`
- Jobs ativos após execução: `0`

## Resultado

Status geral: `partial_or_blocked`

Motivo: Doppler está acessível, mas os secrets OAuth/Calendar esperados para LK Content não existem no projeto/config `lc-keys/prd`.

## Evidência sanitizada

### Compilação

`py_compile`: OK para:

- `/opt/data/scripts/hermes_doppler.py`
- `/opt/data/profiles/lk-content/scripts/doppler_lk_content_env.py`
- `/opt/data/profiles/lk-content/scripts/doppler_lk_content_secret_inventory.py`
- `/opt/data/profiles/lk-content/scripts/gate6_calendar_readonly_check.py`
- `/opt/data/profiles/lk-content/scripts/google_calendar_readonly_smoke.py`
- `/opt/data/profiles/lk-content/scripts/klaviyo_readonly_audit.py`
- `/opt/data/profiles/lk-content/scripts/klaviyo_readonly_smoke.py`

### Doppler doctor

- `returncode`: 0
- `token_source`: file
- `token_file_mode_ok`: true
- `doppler_cli_available`: true
- `doppler_cli_version`: v3.76.0
- `api_download_ok`: true
- `secret_count`: 272
- `values_printed`: false

### Secrets Gate 6

Presentes:

- `KLAVIYO_API_KEY`

Ausentes:

- `GOOGLE_CLIENT_ID`
- `GOOGLE_CLIENT_SECRET`
- `GOOGLE_REFRESH_TOKEN_LK_CONTENT`
- `GOOGLE_REFRESH_TOKEN`
- `LK_CONTENT_CALENDAR_ID`

### Google Calendar smoke

- Status: `blocked_missing_env`
- Falta: `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, `GOOGLE_REFRESH_TOKEN_LK_CONTENT or GOOGLE_REFRESH_TOKEN`
- Calendar list: não executado por falta de credencial
- Eventos próximos: não executado por falta de credencial
- `writes_performed`: 0
- `event_create_update_delete_performed`: false/null no read-only blocked output

## Segurança

- `values_printed=false`
- Nenhum valor de secret foi impresso.
- Nenhum `.env` foi lido.
- Nenhum evento Calendar foi criado, alterado ou deletado.
- Nenhum Klaviyo/Shopify/Tiny/WhatsApp/email/ads write.
- O one-shot foi removido automaticamente; `cronjob list` retornou `count: 0` após execução.

## Ações locais/documentais

- Criado script sanitizado de Gate 6: `/opt/data/profiles/lk-content/scripts/gate6_calendar_readonly_check.py`
- Atualizado status em `/opt/data/profiles/lk-content/integrations/google-calendar.md` para refletir bloqueio por secrets ausentes.

## Próximo gate

Para concluir Gate 6, é necessário provisionar no Doppler `lc-keys/prd` uma das opções:

Opção recomendada LK Content OAuth:

- `GOOGLE_CLIENT_ID`
- `GOOGLE_CLIENT_SECRET`
- `GOOGLE_REFRESH_TOKEN_LK_CONTENT`
- `LK_CONTENT_CALENDAR_ID`

Fallback aceitável só se aprovado:

- `GOOGLE_REFRESH_TOKEN`
- `LK_CONTENT_CALENDAR_ID`

Depois de provisionar, reexecutar o one-shot read-only. Criar evento teste `LK Content Smoke Test` continua sendo write externo e exigirá aprovação específica de título/calendário/data/hora.
