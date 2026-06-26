# Receipt — LK Content Klaviyo + Calendar config prepared — 2026-06-07

Data/hora BRT: 2026-06-07 09:13

## Escopo executado

Preparação local/documental para configuração de Klaviyo e Google Calendar no perfil `lk-content`.

## Arquivos criados

Integrações:

- `/opt/data/profiles/lk-content/integrations/klaviyo.md`
- `/opt/data/profiles/lk-content/integrations/google-calendar.md`

Scripts de smoke read-only:

- `/opt/data/profiles/lk-content/scripts/klaviyo_readonly_smoke.py`
- `/opt/data/profiles/lk-content/scripts/google_calendar_readonly_smoke.py`

Templates:

- `/opt/data/profiles/lk-content/templates/klaviyo-newsletter-preview.md`
- `/opt/data/profiles/lk-content/templates/klaviyo-double-confirmation.md`
- `/opt/data/profiles/lk-content/templates/calendar-event-preview.md`
- `/opt/data/profiles/lk-content/templates/smoke-report-klaviyo-calendar.md`

## Contrato de secrets esperado

Klaviyo:

- `KLAVIYO_API_KEY`

Google Calendar:

- `GOOGLE_CLIENT_ID`
- `GOOGLE_CLIENT_SECRET`
- `GOOGLE_REFRESH_TOKEN_LK_CONTENT` ou `GOOGLE_REFRESH_TOKEN`
- `LK_CONTENT_CALENDAR_ID`

Nenhum valor de secret foi lido, impresso ou salvo.

## Guardrails configurados

Klaviyo:

- Smoke inicial é read-only: campaigns, lists, segments, flows e metrics.
- Draft/template/campaign write exige aprovação explícita atual.
- Envio/agendamento/flow activation exige dupla confirmação Telegram.
- Deleção fica bloqueada sem aprovação específica.
- Readback obrigatório: status Draft, `scheduled_at` null, `send_time` null, audience/copy/template corretos.

Google Calendar:

- Smoke inicial é read-only: calendarList e próximos eventos.
- Evento teste `LK Content Smoke Test` é write externo e exige aprovação explícita atual com calendário/data/hora.
- Delete fica bloqueado sem confirmação específica.
- Não mexer em calendário pessoal/fora do escopo.

## Verificação feita

- `write_file` aplicou lint Python nos dois scripts e retornou `status: ok`.
- Arquivos foram relidos/inspecionados; os scripts retornam `blocked_missing_env` com `writes_performed: 0` quando secrets não estão presentes.
- Delegação tentou executar comandos reais, mas não tinha terminal disponível; não houve saída de execução shell fabricada.

## Não executado

- Nenhum acesso a `.env` ou Doppler.
- Nenhuma chamada Klaviyo autenticada.
- Nenhuma chamada Google Calendar autenticada.
- Nenhum envio, agendamento, draft, template, segmento, flow, evento ou cron real.
- Nenhum write externo.

## Próximo gate

Para rodar smoke real read-only, é necessário disponibilizar as credenciais no ambiente do perfil `lk-content` e autorizar apenas leitura/smoke. Depois disso, os scripts podem gerar receipt sanitizado.

Para writes de teste:

- Klaviyo draft/template teste: precisa aprovação explícita atual para criar rascunho, sem envio/agendamento.
- Calendar event teste: precisa aprovação explícita atual para criar evento `LK Content Smoke Test` no calendário alvo.
