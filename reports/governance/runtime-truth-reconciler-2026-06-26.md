# Runtime Truth Reconciler — 2026-06-26

## 1. Timestamp e escopo

- Timestamp UTC: 2026-06-26 11:21 UTC.
- Escopo: reconciliação read-only/local da evidência viva de crons Hermes com documentação do Brain.
- Workdir: `/opt/data/hermes_bruno_ingest/hermes-brain`.
- Não houve alteração em cron, gateway, Docker, VPS, Traefik, redes, containers, integrações externas, campanhas, Shopify, GMC, Notion, WhatsApp, email, bancos ou secrets.

## 2. Fonte de evidência viva

- Comando primário solicitado: `cronjob list`.
- Resultado: `cronjob` não disponível no PATH deste runtime.
- Fallback canônico usado: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.
- Fonte estruturada sanitizada para contagem: `/opt/data/cron/jobs.json`.
- Campos usados: `id`, `name`, estado active/paused, `deliver`, `last_status`, `last_run_at`, `last_delivery_error`, `next_run_at`.
- Campos não versionados: prompts, stdout bruto, stderr bruto, env vars, process args, tokens e valores de secrets.

## 3. Sumário da evidência viva

- Total: 44 jobs.
- Ativos: 40 jobs.
- Pausados: 4 jobs.
- `last_status` não-ok: 1 job.
- Erros explícitos de delivery do scheduler: 0.
- Jobs ativos sem primeira execução registrada: 1.
- Jobs com `deliver=origin`: 4 ativos + 1 pausado.

## 4. Anomalias atuais

- `bc96bb03d2b0` — Hermes Memory OS daytime checker/router — 30min alert-only — active, `deliver=local`, `last_status=error`, último run 2026-06-26T11:01:52.486192+00:00. Causa sanitizada: o watchdog excedeu timeout interno de 240s ao rodar o checker Memory OS diurno. Requer triagem local do tempo de execução/limites do checker; este reconciler não alterou script, cron ou runtime.

## 5. Drift vs snapshot anterior

- Contagem estável vs 2026-06-25: 44 totais / 40 ativos / 4 pausados.
- Drift negativo de runtime: `bc96bb03d2b0` passou de `ok` no snapshot de 2026-06-25 para `error` nesta execução.
- `00a9f839879f` segue ativo/`deliver=origin`/sem primeira execução; acompanhar até 2026-06-29T01:10 UTC e documentar owner/finalidade/critério de sucesso/contrato de alerta.
- Jobs Honcho `7d32b8b77317`, `39b176e08174` e `16dfc4d14c85` seguem vivos/ok com `deliver=local`; manter reconciliação documental da mudança de entrega para evitar falso gap de ruído.
- `2e5bc91d27d6` Hermes Nightly Operations Audit OS — 02h50 BRT segue ativo/local/ok e ainda merece reconciliação documental de owner/finalidade/critério de sucesso em rodada própria.
- Documentação que descreve Mordomo/LK Growth/SPITI gateway watchdogs como ativos deve permanecer marcada como histórica até nova evidência viva mostrar reativação.

## 6. Jobs pausados na evidência viva

| id | nome | deliver | last_status | last_run |
|---|---|---:|---:|---|
| `663e3e6a148c` | SPITI Telegram gateway watchdog | local | ok | 2026-05-30T15:52:55.201503+00:00 |
| `876d54c62ccd` | LK Growth Telegram gateway watchdog | local | ok | 2026-05-30T15:52:55.226608+00:00 |
| `955dc769b5a6` | LK specialist Telegram gateway watchdog | origin | ok | 2026-05-30T15:52:55.190857+00:00 |
| `ac0b440e2643` | Mordomo Telegram gateway watchdog | local | ok | 2026-05-30T15:52:55.213145+00:00 |

## 7. Jobs `deliver=origin`

Ativos:

| id | nome | last_status | last_run |
|---|---|---:|---|
| `00a9f839879f` | Honcho utility go/no-go review one-shot | sem primeira execução | sem Last run |
| `518634d5ea60` | Reminder OS — 2h open-loop watchdog | ok | 2026-06-26T09:27:03.466522+00:00 |
| `749ee30b51eb` | Mesa COO diária Telegram | ok | 2026-06-26T09:02:10.077213+00:00 |
| `98478b820720` | Relatório Hermes diário 01h+02h+02h15+02h25+02h50 + Score 0–100 — 03h Telegram | ok | 2026-06-26T06:02:43.760572+00:00 |

Pausado:

| id | nome | last_status | last_run |
|---|---|---:|---|
| `955dc769b5a6` | LK specialist Telegram gateway watchdog | ok | 2026-05-30T15:52:55.190857+00:00 |

## 8. Gaps documentais/acionáveis

1. `bc96bb03d2b0` está com `last_status=error`: triagem local necessária para timeout do Memory OS daytime checker/router.
2. `00a9f839879f` segue como one-shot futuro sem primeira execução: acompanhar até 2026-06-29T01:10 UTC e documentar owner/finalidade/critério de sucesso/contrato de alerta.
3. `2e5bc91d27d6` ainda precisa de documentação de owner/finalidade/critério de sucesso em rodada própria.
4. Watchdogs pausados de gateways especialistas devem continuar documentados como históricos/pausados até evidência viva de reativação.

## 9. O que não foi alterado

- Nenhum job foi criado, editado, pausado, retomado, removido ou disparado.
- Nenhuma entrega `local`/`origin` foi alterada.
- Nenhum Docker/VPS/Traefik/container/rede/gateway foi tocado.
- Nenhuma integração externa, campanha, mensagem, banco, Shopify, GMC, Notion, WhatsApp, email ou secret foi acessado para escrita.

## 10. Artefatos atualizados

- `areas/operacoes/inventarios/crons-agentes-profiles.md`.
- `reports/governance/runtime-truth-reconciler-2026-06-26.md`.
- `reports/brain-health-check-2026-06-26-runtime-truth-reconciler.json`.

## 11. Verificação

- Brain health check: `python3 scripts/brain_health_check.py --json reports/brain-health-check-2026-06-26-runtime-truth-reconciler.json` → `All checks passed` (`FAIL=0`, `WARN=0`).
- `git diff --check` nos artefatos tocados → sem erros.
- Secret scan escopado nos artefatos tocados → `scoped_possible_secrets 0`.
- Status escopado confirmou alterações apenas nos artefatos esperados deste reconciler; havia alterações/untracked preexistentes fora deste escopo e não foram tocados.

## 12. Apêndice — inventário sanitizado compacto

| id | estado | nome | deliver | last_status | last_run |
|---|---|---|---:|---:|---|
| `00a9f839879f` | active | Honcho utility go/no-go review one-shot | origin | sem primeira execução | sem Last run |
| `16dfc4d14c85` | active | Honcho Intelligence Layer v1 weekly silent-OK | local | ok | 2026-06-22T07:35:48.811949+00:00 |
| `23143847316e` | active | Brain OS silent-OK health/scanner watchdog — 02h25 BRT local | local | ok | 2026-06-26T05:25:52.246843+00:00 |
| `2404c0766d33` | active | Hermes Brain Runtime Truth Reconciler | local | ok | 2026-06-25T11:23:39.673131+00:00 |
| `2e5bc91d27d6` | active | Hermes Nightly Operations Audit OS — 02h50 BRT | local | ok | 2026-06-26T05:50:43.442602+00:00 |
| `357d40a5863e` | active | Zipper OS vendas 09h WhatsApp/email | local | ok | 2026-06-25T12:00:18.105344+00:00 |
| `39b176e08174` | active | Honcho memory quality auditor silent-OK | local | ok | 2026-06-26T07:20:58.631300+00:00 |
| `3cd1011edf33` | active | claude-max-proxy watchdog | local | ok | 2026-06-26T11:20:55.136879+00:00 |
| `3fc45b0830c6` | active | Hermes Brain Fechamento Ágil 01h + Brain Sync | local | ok | 2026-06-26T04:08:30.567084+00:00 |
| `4bb4e2223fd3` | active | Hermes compression failure self-heal watchdog | local | ok | 2026-06-26T11:20:53.458995+00:00 |
| `518634d5ea60` | active | Reminder OS — 2h open-loop watchdog | origin | ok | 2026-06-26T09:27:03.466522+00:00 |
| `5bacaa61bb12` | active | claude-proxy-watchdog | local | ok | 2026-06-26T11:16:52.958131+00:00 |
| `6792657c0be7` | active | LK POS pós-compra WhatsApp auto-worker | local | ok | 2026-06-26T11:15:53.312591+00:00 |
| `71b147362ec1` | active | Zipper Gmail style learning refresh | local | ok | 2026-06-26T06:21:52.142975+00:00 |
| `749ee30b51eb` | active | Mesa COO diária Telegram | origin | ok | 2026-06-26T09:02:10.077213+00:00 |
| `787134d4ac5c` | active | LK Weekly Collection Sort Rule B | local | ok | 2026-06-26T09:00:49.092438+00:00 |
| `7b7ae67655c5` | active | wacli pessoal sync watchdog | local | ok | 2026-06-26T11:18:53.290267+00:00 |
| `7c688553e293` | active | LK Daily Sales Brief read-only mandatory delivery | local | ok | 2026-06-26T11:01:52.974017+00:00 |
| `7d32b8b77317` | active | Honcho Hermes memory watchdog silent-OK | local | ok | 2026-06-26T11:06:52.913731+00:00 |
| `810c0d2bf65a` | active | LC Mordomo OS real local no-agent watcher | local | ok | 2026-06-26T11:15:53.200650+00:00 |
| `953b9055458e` | active | LK Weekly CEO Review read-only mandatory delivery | local | ok | 2026-06-22T12:01:34.320459+00:00 |
| `98478b820720` | active | Relatório Hermes diário 01h+02h+02h15+02h25+02h50 + Score 0–100 — 03h Telegram | origin | ok | 2026-06-26T06:02:43.760572+00:00 |
| `a1d1e36f8075` | active | LK Weekly Catalog Badges BEST SELLER sync | local | ok | 2026-06-26T09:41:24.509401+00:00 |
| `a2ead305eab2` | active | LK 19h30 physical store close external delivery | local | ok | 2026-06-25T22:30:44.074869+00:00 |
| `a97a6317b197` | active | Zipper post-PDF follow-up watchdog | local | ok | 2026-06-26T10:58:56.108074+00:00 |
| `b78ae7ac81d0` | active | Hermes all Telegram gateways watchdog | local | ok | 2026-06-26T11:20:58.955729+00:00 |
| `bc96bb03d2b0` | active | Hermes Memory OS daytime checker/router — 30min alert-only | local | error | 2026-06-26T11:01:52.486192+00:00 |
| `c1ce34b4449a` | active | Hermes multi-profile latency watchdog | local | ok | 2026-06-26T11:10:53.912597+00:00 |
| `c3bb587519d2` | active | LK Pulso Comercial 16h read-only delivery | local | ok | 2026-06-25T19:00:24.969275+00:00 |
| `c64a0c63b881` | active | LK Tiny stock local DB daily fullsync | local | ok | 2026-06-26T10:45:51.483899+00:00 |
| `c933dd2e30ec` | active | WACLI health read-only pre-Zipper 08h50 BRT | local | ok | 2026-06-25T11:50:10.805682+00:00 |
| `d03fa04e1188` | active | Hermes Brain Operating Layer structural watchdog | local | ok | 2026-06-26T11:10:52.878854+00:00 |
| `d9badcd83411` | active | Hermes Brain strict-runtime guard watchdog | local | ok | 2026-06-26T11:18:57.045082+00:00 |
| `e2f169cc046a` | active | LK POS Shopify→fila reconciliador | local | ok | 2026-06-26T11:20:54.170557+00:00 |
| `e3279babbc4a` | active | LK 09h previous-day sales report external delivery | local | ok | 2026-06-25T12:00:40.506304+00:00 |
| `e4c6b7c9b6dc` | active | Hermes Memory OS weekly observability local/silent | local | ok | 2026-06-22T12:45:35.355233+00:00 |
| `edd06fe19397` | active | Hermes runtime + cron watchdog no_agent | local | ok | 2026-06-26T11:00:53.652084+00:00 |
| `f4c499e85eac` | active | Lucas Brain weekly Learning Loop report | local | ok | 2026-06-22T12:20:44.318435+00:00 |
| `f5a23dd6a1bd` | active | LC Hermes daily intelligence loop — systemwide audit + self-improvement | local | ok | 2026-06-26T05:09:48.650808+00:00 |
| `f9a1d43caf48` | active | Hermes memory hygiene watchdog 02h15 BRT | local | ok | 2026-06-26T05:15:42.928702+00:00 |
| `663e3e6a148c` | paused | SPITI Telegram gateway watchdog | local | ok | 2026-05-30T15:52:55.201503+00:00 |
| `876d54c62ccd` | paused | LK Growth Telegram gateway watchdog | local | ok | 2026-05-30T15:52:55.226608+00:00 |
| `955dc769b5a6` | paused | LK specialist Telegram gateway watchdog | origin | ok | 2026-05-30T15:52:55.190857+00:00 |
| `ac0b440e2643` | paused | Mordomo Telegram gateway watchdog | local | ok | 2026-05-30T15:52:55.213145+00:00 |
