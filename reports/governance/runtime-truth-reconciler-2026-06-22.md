# Runtime Truth Reconciler — 2026-06-22

## 1. Timestamp e escopo

- Timestamp da execução: 2026-06-22 11:23 UTC.
- Escopo: reconciliação read-only/local entre evidência viva de crons Hermes e documentação do Hermes Brain.
- Workdir: `/opt/data/hermes_bruno_ingest/hermes-brain`.

## 2. Fonte viva

- Comando solicitado: `cronjob list`.
- Resultado: indisponível neste runtime (`cronjob: command not found`).
- Fallback canônico usado: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.
- Fonte estruturada sanitizada para contagem: `/opt/data/cron/jobs.json` (campos seguros: id, nome, estado, deliver, last_status, last_run_at; prompts e stdout não versionados).

## 3. Resumo da evidência viva

- Total: 43 jobs.
- Ativos: 39 jobs.
- Pausados: 4 jobs.
- `last_status` não-ok: 0.
- Erros explícitos de delivery do scheduler na listagem/estado: 0.
- Jobs ativos sem primeira execução registrada: 1.

## 4. Anomalias atuais

Nenhum job com `last_status` não-ok e nenhum erro explícito de delivery foi encontrado. Há, porém, 1 job ativo sem primeira execução registrada: `00a9f839879f` Honcho utility go/no-go review one-shot, agendado para 2026-06-29T01:10 UTC, `deliver=origin`.

## 5. Drift vs snapshot anterior

- Contagem mudou vs 2026-06-21: 42 → 43 totais; 38 → 39 ativos; 4 pausados estável.
- Novo job vivo identificado:
- `00a9f839879f` Honcho utility go/no-go review one-shot — active, `deliver=origin`, sem Last run / sem Last run
- Jobs Honcho observados em 2026-06-20 continuam vivos/ok, mas agora aparecem como `deliver=local` na evidência viva desta execução; em 2026-06-21 estavam documentados como `deliver=origin`. Tratar como drift positivo de ruído/entrega, não como falha:
- `7d32b8b77317` Honcho Hermes memory watchdog silent-OK — active, `deliver=local`, ok / 2026-06-22T11:16:29.151844+00:00
- `39b176e08174` Honcho memory quality auditor silent-OK — active, `deliver=local`, ok / 2026-06-22T07:20:44.477263+00:00
- `16dfc4d14c85` Honcho Intelligence Layer v1 weekly silent-OK — active, `deliver=local`, ok / 2026-06-22T07:35:48.811949+00:00
- `2e5bc91d27d6` Hermes Nightly Operations Audit OS — 02h50 BRT segue ativo/local/ok e ainda merece reconciliação documental de owner/finalidade/critério de sucesso em rodada própria.
- Documentação que descreve Mordomo/LK Growth/SPITI gateway watchdogs como ativos deve permanecer marcada como histórica até nova evidência viva mostrar reativação.

## 6. Jobs pausados

- `ac0b440e2643` Mordomo Telegram gateway watchdog — paused, `deliver=local`, ok / 2026-05-30T15:52:55.213145+00:00
- `876d54c62ccd` LK Growth Telegram gateway watchdog — paused, `deliver=local`, ok / 2026-05-30T15:52:55.226608+00:00
- `663e3e6a148c` SPITI Telegram gateway watchdog — paused, `deliver=local`, ok / 2026-05-30T15:52:55.201503+00:00
- `955dc769b5a6` LK specialist Telegram gateway watchdog — paused, `deliver=origin`, ok / 2026-05-30T15:52:55.190857+00:00

## 7. Jobs `deliver=origin`

`deliver=origin` não é falha por si só; é saída intencional/condicional quando documentada.

Ativos: Mesa COO diária Telegram (`749ee30b51eb`), Relatório Hermes diário 01h+02h+02h15+02h25+02h50 + Score 0–100 — 03h Telegram (`98478b820720`), Reminder OS — 2h open-loop watchdog (`518634d5ea60`), Honcho utility go/no-go review one-shot (`00a9f839879f`).

Pausado: `955dc769b5a6` LK specialist Telegram gateway watchdog — pausado/ok histórico.

## 8. Gaps documentais/acionáveis

1. Novo job `00a9f839879f` Honcho utility go/no-go review one-shot está ativo/`deliver=origin` e sem `Last run`; acompanhar até a primeira execução e documentar owner, finalidade, critério de sucesso e contrato de alerta/entrega.
2. Jobs Honcho `7d32b8b77317`, `39b176e08174` e `16dfc4d14c85` mudaram de `deliver=origin` documentado para `deliver=local` vivo; reconciliar docs/receipts para refletir a entrega atual e evitar falso gap de ruído.
3. `2e5bc91d27d6` Hermes Nightly Operations Audit OS — 02h50 BRT continua vivo/local/ok e ainda merece reconciliação documental de owner/finalidade/critério de sucesso.
4. Watchdogs de gateway Mordomo/LK Growth/SPITI/LK specialist continuam pausados; manter docs como histórico/pausado até evidência viva de reativação.

## 9. O que não foi alterado

Não houve mudança em cron schedule/delivery/prompt/script, gateway/runtime, Docker, VPS, Traefik, redes, containers, sistemas externos, campanhas, Shopify, GMC, Notion, WhatsApp, email, bancos, tokens ou secrets.

## 10. Artefatos atualizados

- `areas/operacoes/inventarios/crons-agentes-profiles.md`
- `reports/governance/runtime-truth-reconciler-2026-06-22.md`
- `reports/brain-health-check-2026-06-22-runtime-truth-reconciler.json`

## 11. Verificação

- `python3 scripts/brain_health_check.py --json reports/brain-health-check-2026-06-22-runtime-truth-reconciler.json`: `All checks passed` (`FAIL=0/WARN=0`).
- `git diff --check` nos artefatos tocados: sem whitespace errors.
- Secret scan escopado dos artefatos tocados: `scoped_possible_secrets 0`.

## 12. Apêndice — inventário sanitizado vivo

Campos preservados: id, estado, deliver, último status/execução e nome. Não inclui prompt bruto, stdout bruto, env vars, tokens, process args ou secrets.

| id | estado | deliver | último status / execução | nome |
|---|---|---:|---|---|
| `f5a23dd6a1bd` | active | local | ok / 2026-06-22T05:08:35.303588+00:00 | LC Hermes daily intelligence loop — systemwide audit + self-improvement |
| `edd06fe19397` | active | local | ok / 2026-06-22T11:00:29.271269+00:00 | Hermes runtime + cron watchdog no_agent |
| `7c688553e293` | active | local | ok / 2026-06-22T11:01:17.066858+00:00 | LK Daily Sales Brief read-only mandatory delivery |
| `953b9055458e` | active | local | ok / 2026-06-15T12:02:58.587007+00:00 | LK Weekly CEO Review read-only mandatory delivery |
| `71b147362ec1` | active | local | ok / 2026-06-22T06:21:36.381402+00:00 | Zipper Gmail style learning refresh |
| `4bb4e2223fd3` | active | local | ok / 2026-06-22T11:20:29.183763+00:00 | Hermes compression failure self-heal watchdog |
| `c3bb587519d2` | active | local | ok / 2026-06-21T19:00:27.869750+00:00 | LK Pulso Comercial 16h read-only delivery |
| `e3279babbc4a` | active | local | ok / 2026-06-21T12:00:23.035456+00:00 | LK 09h previous-day sales report external delivery |
| `a2ead305eab2` | active | local | ok / 2026-06-21T22:30:31.591694+00:00 | LK 19h30 physical store close external delivery |
| `ac0b440e2643` | paused | local | ok / 2026-05-30T15:52:55.213145+00:00 | Mordomo Telegram gateway watchdog |
| `357d40a5863e` | active | local | ok / 2026-06-19T12:00:23.031331+00:00 | Zipper OS vendas 09h WhatsApp/email |
| `876d54c62ccd` | paused | local | ok / 2026-05-30T15:52:55.226608+00:00 | LK Growth Telegram gateway watchdog |
| `749ee30b51eb` | active | origin | ok / 2026-06-22T09:02:10.679505+00:00 | Mesa COO diária Telegram |
| `663e3e6a148c` | paused | local | ok / 2026-05-30T15:52:55.201503+00:00 | SPITI Telegram gateway watchdog |
| `3fc45b0830c6` | active | local | ok / 2026-06-22T04:10:02.980307+00:00 | Hermes Brain Fechamento Ágil 01h + Brain Sync |
| `f4c499e85eac` | active | local | ok / 2026-06-15T12:19:29.987705+00:00 | Lucas Brain weekly Learning Loop report |
| `d03fa04e1188` | active | local | ok / 2026-06-22T11:10:28.931265+00:00 | Hermes Brain Operating Layer structural watchdog |
| `2404c0766d33` | active | local | ok / 2026-06-21T11:24:29.260578+00:00 | Hermes Brain Runtime Truth Reconciler |
| `98478b820720` | active | origin | ok / 2026-06-22T06:02:08.834819+00:00 | Relatório Hermes diário 01h+02h+02h15+02h25+02h50 + Score 0–100 — 03h Telegram |
| `d9badcd83411` | active | local | ok / 2026-06-22T10:02:59.515217+00:00 | Hermes Brain strict-runtime guard watchdog |
| `c1ce34b4449a` | active | local | ok / 2026-06-22T11:10:29.573120+00:00 | Hermes multi-profile latency watchdog |
| `787134d4ac5c` | active | local | ok / 2026-06-19T09:00:09.750931+00:00 | LK Weekly Collection Sort Rule B |
| `a1d1e36f8075` | active | local | ok / 2026-06-19T09:38:58.178925+00:00 | LK Weekly Catalog Badges BEST SELLER sync |
| `5bacaa61bb12` | active | local | ok / 2026-06-22T11:22:29.132398+00:00 | claude-proxy-watchdog |
| `3cd1011edf33` | active | local | ok / 2026-06-22T11:19:30.990808+00:00 | claude-max-proxy watchdog |
| `955dc769b5a6` | paused | origin | ok / 2026-05-30T15:52:55.190857+00:00 | LK specialist Telegram gateway watchdog |
| `b78ae7ac81d0` | active | local | ok / 2026-06-22T11:23:34.749736+00:00 | Hermes all Telegram gateways watchdog |
| `c64a0c63b881` | active | local | ok / 2026-06-22T10:45:27.840767+00:00 | LK Tiny stock local DB daily fullsync |
| `f9a1d43caf48` | active | local | ok / 2026-06-22T05:15:35.010525+00:00 | Hermes memory hygiene watchdog 02h15 BRT |
| `a97a6317b197` | active | local | ok / 2026-06-22T11:09:29.780904+00:00 | Zipper post-PDF follow-up watchdog |
| `7b7ae67655c5` | active | local | ok / 2026-06-22T11:19:29.220386+00:00 | wacli pessoal sync watchdog |
| `810c0d2bf65a` | active | local | ok / 2026-06-22T11:17:29.088032+00:00 | LC Mordomo OS real local no-agent watcher |
| `bc96bb03d2b0` | active | local | ok / 2026-06-22T11:23:32.369111+00:00 | Hermes Memory OS daytime checker/router — 30min alert-only |
| `6792657c0be7` | active | local | ok / 2026-06-22T11:15:29.015085+00:00 | LK POS pós-compra WhatsApp auto-worker |
| `e4c6b7c9b6dc` | active | local | ok / 2026-06-15T12:45:34.207521+00:00 | Hermes Memory OS weekly observability local/silent |
| `e2f169cc046a` | active | local | ok / 2026-06-22T11:20:30.067261+00:00 | LK POS Shopify→fila reconciliador |
| `23143847316e` | active | local | ok / 2026-06-22T05:25:43.373993+00:00 | Brain OS silent-OK health/scanner watchdog — 02h25 BRT local |
| `518634d5ea60` | active | origin | ok / 2026-06-22T10:51:31.650245+00:00 | Reminder OS — 2h open-loop watchdog |
| `2e5bc91d27d6` | active | local | ok / 2026-06-22T05:50:35.414754+00:00 | Hermes Nightly Operations Audit OS — 02h50 BRT |
| `7d32b8b77317` | active | local | ok / 2026-06-22T11:16:29.151844+00:00 | Honcho Hermes memory watchdog silent-OK |
| `39b176e08174` | active | local | ok / 2026-06-22T07:20:44.477263+00:00 | Honcho memory quality auditor silent-OK |
| `16dfc4d14c85` | active | local | ok / 2026-06-22T07:35:48.811949+00:00 | Honcho Intelligence Layer v1 weekly silent-OK |
| `00a9f839879f` | active | origin | sem Last run / sem Last run | Honcho utility go/no-go review one-shot |
