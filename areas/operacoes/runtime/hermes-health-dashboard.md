# Hermes Health Dashboard — Runtime / Brain

Atualizado em: 2026-05-22 14:22 UTC

## Objetivo

Dar a qualquer agente futuro uma visão de 30 segundos do estado operacional do Hermes sem depender de memória de chat.

## Veredito atual

- Estado geral: **operacional**.
- Brain health: último pacote P2 deve manter `FAIL=0/WARN=0` como gate obrigatório antes de conclusão.
- Cron registry: **23 jobs ativos / 0 pausados** após criação do strict-runtime watchdog.
- Telegram: canal de decisão/exceção; sucesso técnico normal deve ser silencioso.
- GMC/LK nesta frente: read-only/governado; nenhum write externo aprovado por este dashboard.

## Superfícies vivas

### Scheduler Hermes

Fonte viva: `cronjob(action='list')` ou `hermes cron list` no runtime correto.

Resumo governado:

- `areas/operacoes/rotinas/cron-control-plane.md`
- `areas/operacoes/intelligence-map.md`

Mudanças P2 executadas:

- Criado `d9badcd83411` — Hermes Brain strict-runtime guard watchdog (`0 10 * * *`, `local`, `no_agent`, silent-OK).
- `98478b820720` movido de `origin` para `local` para reduzir duplicidade com Mesa COO.
- Rollback do 02h30 Telegram, se Lucas pedir: `cronjob update 98478b820720 deliver=origin`.

### Watchdogs técnicos principais

- Runtime + cron watchdog: `edd06fe19397`, `local`.
- Compression self-heal: `4bb4e2223fd3`, `local`.
- Strict-runtime guard: `d9badcd83411`, `local`.
- Brain Operating Layer audit: `d03fa04e1188`, `local`.
- Runtime Truth Reconciler: `2404c0766d33`, `local`.
- Gateway/profile watchdogs: Mordomo, LK Growth, SPITI, LK WhatsApp, todos silent-OK/local.

### Executive Telegram surface

Mantidos em `origin` por intenção explícita/valor executivo:

- Mesa COO diária: `749ee30b51eb`.
- Lucas Brain weekly Learning Loop: `f4c499e85eac`.
- LK Daily Sales Brief: `7c688553e293`.
- LK Weekly CEO Review: `953b9055458e`.
- LK GMC Review: `d4c26da4cd48`.

Reduzido para `local`:

- Relatório Hermes diário 23h + 02h: `98478b820720`.

## Health gates obrigatórios antes de declarar “tudo certo”

Rodar a partir de `/opt/data/hermes_bruno_ingest/hermes-brain`:

```bash
python3 scripts/brain_health_check.py
python3 scripts/operational_docs_guard.py --json
python3 scripts/operational_docs_guard.py --strict-runtime --json
python3 /opt/data/scripts/brain_sync_safe.py --dry-run --verbose
/opt/data/scripts/hermes_brain_strict_runtime_guard_watchdog.py
```

Critério esperado:

- Brain health: `FAIL=0/WARN=0`.
- Default docs guard: `fail_count=0`.
- Strict-runtime guard: `fail_count=0`.
- Strict watchdog manual: `rc=0` e stdout vazio.
- Brain sync: dry-run apenas salvo aprovação explícita; confirmar allowed/skipped.

## Riscos conhecidos e controle

- Scripts locais continuam fora do Brain Sync por design; documentar comportamento em `.md` quando for conhecimento durável.
- Relatórios/raw JSON/receipts podem permanecer locais; promover só resumo durável.
- Docker/VPS/Traefik/volumes/redes continuam fora de escopo sem aprovação explícita + backup/rollback.
- Qualquer recriação de cron removido exige rotina `.md`, owner, fonte, delivery, kill criteria e approval packet novo.

## Próximas melhorias recomendadas

1. Auditar skills críticas mensalmente contra paths legados e instruções perigosas.
2. Se a Mesa COO não absorver bem o resumo 02h30, fundir prompts ou restaurar `origin` do job `98478b820720`.
3. Promover para allowlist apenas dashboards/relatórios de governança que reduzem contexto futuro.
4. Manter este dashboard curto; detalhes pertencem aos reports em `reports/governance/`.
