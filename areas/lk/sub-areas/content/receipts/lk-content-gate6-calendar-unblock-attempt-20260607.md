# Receipt — LK Content Gate 6 destravamento Calendar — 2026-06-07

Data/hora BRT: 2026-06-07 17:15

## Escopo executado

Lucas pediu para destravar o Gate 6. Foi feita tentativa segura de destravamento usando credencial já existente no Doppler `lc-keys/prd`, sem pedir novo secret antes de verificar alternativas.

## Ações executadas

- Atualizado `google_calendar_readonly_smoke.py` para aceitar fallback read-only via `GOOGLE_CALENDAR_CREDENTIALS_JSON` quando OAuth client/refresh token não estiver disponível.
- Reexecutado Gate 6 em one-shot local/script-only.
- Extraído hint não-secreto da service account para orientar compartilhamento do calendário.
- Atualizado status documental em `/opt/data/profiles/lk-content/integrations/google-calendar.md`.

## Resultado real

Status: parcialmente destravado / ainda bloqueado por permissão no calendário alvo.

### O que funcionou

- `GOOGLE_CALENDAR_CREDENTIALS_JSON` existe no Doppler e foi injetado no runtime do one-shot.
- Token service-account foi emitido com sucesso.
- Google Calendar API respondeu `calendarList` com HTTP 200.
- `values_printed=false`.
- `writes_performed=0`.
- Nenhum evento criado, alterado ou deletado.

### O que bloqueou

- `calendarList` retornou 0 calendários para a service account.
- Leitura do calendário alvo `lk@lksneakers.com.br` retornou HTTP 404.
- Interpretação: o calendário alvo não está compartilhado com a service account, ou a service account não tem permissão/read access nesse calendário.

## Hint não-secreto para liberar acesso

Service account client email:

- `openclaw-hst@openclaw-hst.iam.gserviceaccount.com`

Ação necessária fora do Hermes:

- Compartilhar o calendário `lk@lksneakers.com.br` com esse email, com permissão mínima de leitura para smoke read-only.

Permissão recomendada para o próximo teste:

- `Ver todos os detalhes dos eventos` / read-only.

Se depois quisermos criar evento teste, aí a permissão precisará ser elevada e o write exigirá aprovação específica.

## Secrets OAuth ainda ausentes

Continuam ausentes no Doppler:

- `GOOGLE_CLIENT_ID`
- `GOOGLE_CLIENT_SECRET`
- `GOOGLE_REFRESH_TOKEN_LK_CONTENT`
- `GOOGLE_REFRESH_TOKEN`
- `LK_CONTENT_CALENDAR_ID`

Como existe service-account JSON, a rota mais rápida agora é compartilhar o calendário com a service account. A rota OAuth continua válida, mas exige provisionar os secrets acima.

## Outputs locais

- Gate 6 service-account attempt: `/opt/data/profiles/lk-content/cron/output/74ac63f4e92e/2026-06-07_20-14-28.md`
- Service account hint: `/opt/data/profiles/lk-content/cron/output/7ebb6f5f285f/2026-06-07_20-15-24.md`

## Próximo gate

Após compartilhar o calendário com a service account, reexecutar Gate 6 read-only. Se passar:

1. Calendar list deve encontrar o calendário alvo.
2. Eventos próximos devem retornar HTTP 200.
3. Gate 6 pode ser marcado como OK read-only.
4. Evento teste permanece bloqueado até aprovação específica.
