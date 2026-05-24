# Mordomo PRD — implementação 1/3/5/6 + Tidio sem webhook

Atualizado: 2026-05-18

## Implementado neste ciclo

### 1. Calendar watcher global

Script: `/opt/data/profiles/mordomo/scripts/mordomo_calendar_global_watch.py`
Cron: `fe5cf7f1b228` — a cada 15 minutos

Função:
- lê calendários autorizados;
- detecta novos eventos relevantes;
- detecta conflitos;
- salva estado em `/opt/data/profiles/mordomo/state/mordomo_calendar_global_watch.json`;
- salva artefatos em `areas/operacoes/calendar-intake/`;
- contrato silent-OK.

Primeira varredura baselined eventos já existentes; próximos alertas devem ser apenas novos/conflitos.

### 3. CRM local estruturado

Script: `/opt/data/profiles/mordomo/scripts/mordomo_crm_sync_local.py`
Cron: `daf97feec481` — a cada 10 minutos, entrega local
Banco: `/opt/data/profiles/mordomo/state/mordomo_crm.sqlite`

Tabelas:
- `contacts`
- `followups`
- `signals`
- `actions`

Status local salvo em:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/crm/mordomo-crm-local-status.md`

Sem write em Supabase nesta fase.

### 5. Decision Inbox / digest

Script: `/opt/data/profiles/mordomo/scripts/mordomo_decision_digest.py`
Cron: `e46ea230f0cf` — diário 09:00 UTC

Entrega apenas se houver follow-up vencendo/vencido ou decisão/bloqueio. Sem relatório vazio.

### 6. A2 executor scaffold

Script: `/opt/data/profiles/mordomo/scripts/mordomo_a2_executor.py`
Cron: `058df00bf941` — a cada 30 minutos
Config: `/opt/data/profiles/mordomo/state/mordomo_a2_config.json`

Estado seguro inicial:
- `enabled: false`
- `kill_switch: true`
- `send_external: false`

Ou seja: prepara previews locais para subfluxos A2, mas não envia mensagem externa. Envio externo continua bloqueado sem aprovação exata de Lucas no turno atual.

## Tidio sem webhook

Plano salvo em:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/zipper/projetos/mordomo-tidio-email-fallback-2026-05-18.md`

Decisão: usar e-mails do Tidio no Gmail como fonte alternativa, já que o plano do Tidio não permite webhook.

## Verificação

- `py_compile`: OK para os 4 scripts novos.
- CRM sync: OK.
- Digest: OK / silencioso sem itens.
- A2 scaffold: OK / silencioso.
- Calendar watcher: OK; primeira baseline detectou eventos existentes relevantes.
