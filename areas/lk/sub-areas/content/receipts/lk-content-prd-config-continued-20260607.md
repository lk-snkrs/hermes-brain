# Receipt — LK Content PRD/prd config continued — 2026-06-07

Data/hora BRT: 2026-06-07 16:52

## Escopo executado

Continuação segura da configuração do LK Content a partir do PRD/checklist e do estado atual do perfil `lk-content`, com foco em alinhar a configuração PRD/Doppler e consolidar próximo gate.

## Fontes consultadas

- PRD/checklist: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/content/plans/lk-content-implementation-checklist-20260607.md`
- Receipts de runtime, Telegram, Klaviyo, calendário editorial e gateway.
- Integrações locais:
  - `/opt/data/profiles/lk-content/integrations/klaviyo.md`
  - `/opt/data/profiles/lk-content/integrations/google-calendar.md`
- Scripts locais:
  - `/opt/data/profiles/lk-content/scripts/doppler_lk_content_secret_inventory.py`
  - `/opt/data/profiles/lk-content/scripts/doppler_lk_content_env.py`
  - `/opt/data/profiles/lk-content/scripts/klaviyo_readonly_smoke.py`
  - `/opt/data/profiles/lk-content/scripts/klaviyo_readonly_audit.py`
  - `/opt/data/profiles/lk-content/scripts/google_calendar_readonly_smoke.py`
- Helper central Doppler:
  - `/opt/data/scripts/hermes_doppler.py`

## Ação aplicada

Atualizado o mapa sanitizado do helper central `/opt/data/scripts/hermes_doppler.py` para que o profile `lk-content` também espere os secrets atuais de Google Calendar/OAuth usados pelo PRD:

- `GOOGLE_CLIENT_ID`
- `GOOGLE_CLIENT_SECRET`
- `GOOGLE_REFRESH_TOKEN_LK_CONTENT`
- `GOOGLE_REFRESH_TOKEN`
- `LK_CONTENT_CALENDAR_ID`

Foram preservados os nomes legados/relacionados já existentes:

- `KLAVIYO_API_KEY`
- `KLAVIYO_PUBLIC_KEY`
- `GOOGLE_CALENDAR_CREDENTIALS_JSON`
- `GMAIL_REFRESH_TOKEN_LK`
- `SHOPIFY_ACCESS_TOKEN`
- `SHOPIFY_STORE`

## Verificação feita

- `patch` retornou lint `status: ok` para `/opt/data/scripts/hermes_doppler.py`.
- Readback confirmou o bloco `PROFILE_SECRET_MAP["lk-content"]` atualizado com os nomes novos.
- `cronjob list` retornou `count: 0`; não há cron ativo neste perfil no momento desta checagem.
- Auditoria delegada/estática confirmou que os scripts locais do perfil existem e declaram `writes_performed: 0` nos smokes read-only.

## Status por gate do checklist

- Gate 1 — Perfil isolado: OK por receipts anteriores.
- Gate 2 — Identidade/toolsets: OK documental/local; ajustes finos de config podem depender de comando Hermes aprovado.
- Gate 3 — Telegram: OK para Lucas/grupo, validado por round-trip atual; Renan ainda depende de autorização/teste próprio se for operar.
- Gate 4 — Brain package: OK instalado.
- Gate 5 — Klaviyo: OK para read-only; smoke corrigido retornou HTTP 200 em campaigns/lists/segments/flows/metrics. Draft/template/write seguem bloqueados sem aprovação explícita.
- Gate 6 — Google Calendar: inconclusivo/bloqueado para smoke real; precisa validar presence/access dos secrets e rodar smoke read-only. Criar evento teste continua write externo e exige aprovação específica.
- Gate 7 — Shopify/Tiny: pendente; apenas guardrails documentais por enquanto.
- Gate 8 — LK Growth/LK Trends: pendente; precisa protocolo de handoff/consulta.
- Gate 9 — Brand/Content Guide vivo: pendente.
- Gate 10 — Crons próprios: bloqueado sem cadência/kill criteria aprovados; nenhum cron ativo no perfil agora.
- Gate 11 — Smoke ponta a ponta de campanha: pendente; pode começar por preview local sem external write.
- Gate 12 — Verificação final: parcial; falta Renan, Calendar, Shopify/Tiny, protocolos e guia vivo.

## Segurança

- `values_printed=false`
- Nenhum valor de secret foi lido, impresso ou salvo.
- Nenhum `.env` foi aberto.
- Nenhum write externo foi executado.
- Nenhum Klaviyo draft/template/campaign foi criado.
- Nenhum envio, agendamento ou flow activation foi realizado.
- Nenhum evento Google Calendar foi criado/alterado/deletado.
- Nenhum cron real foi criado.

## Bloqueio/inconclusivo

A verificação runtime de Doppler/Calendar não foi concluída nesta rodada porque as ferramentas disponíveis neste turno não forneceram execução shell direta ao subagente para rodar `doctor`, `inventory` e `py_compile` reais. O helper e os scripts foram inspecionados e alinhados, mas a presença real de secrets no Doppler ainda precisa de execução do helper.

## Próximo gate recomendado

Rodar, em execução local segura, os checks sanitizados abaixo — sem imprimir valores — para fechar o Gate 6 read-only:

1. `python3 /opt/data/scripts/hermes_doppler.py doctor`
2. `python3 /opt/data/scripts/hermes_doppler.py inventory --profile lk-content --verbose`
3. `python3 /opt/data/scripts/hermes_doppler.py exists KLAVIYO_API_KEY GOOGLE_CLIENT_ID GOOGLE_CLIENT_SECRET GOOGLE_REFRESH_TOKEN_LK_CONTENT GOOGLE_REFRESH_TOKEN LK_CONTENT_CALENDAR_ID --json`
4. `python3 /opt/data/profiles/lk-content/scripts/google_calendar_readonly_smoke.py`

Se Calendar passar read-only, o próximo write opcional seria criar evento teste `LK Content Smoke Test`, mas isso exige aprovação explícita de calendário/data/hora antes de executar.
