# Runtime Truth Reconciler — 2026-06-29

## 1. Timestamp e escopo

- Timestamp UTC: 2026-06-29 11:20 UTC.
- Escopo: reconciliação read-only/local da evidência viva de crons Hermes com documentação do Brain.
- Workdir: `/opt/data/hermes_bruno_ingest/hermes-brain`.
- Honcho: não houve ferramenta `honcho_context/search/reasoning` exposta neste cron; usei a camada Brain/skills já carregada e evidência viva de cron. Estados Honcho tratados apenas como evidência de scheduler: configured/active/runtime job, não como prova isolada de utilidade sem auditoria dedicada.
- Não houve alteração em cron, gateway, Docker, VPS, Traefik, redes, containers, integrações externas, campanhas, Shopify, GMC, Notion, WhatsApp, email, bancos ou secrets.

## 2. Fonte de evidência viva

- Comando primário solicitado: `cronjob list`.
- Resultado: `cronjob` não disponível no PATH deste runtime.
- Fallback canônico usado: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.
- Fonte estruturada sanitizada para contagem: `/opt/data/cron/jobs.json`.
- Campos usados: `id`, `name`, estado active/paused, `deliver`, `last_status`, `last_run_at`, `last_delivery_error`, `next_run_at`.
- Campos não versionados: prompts, stdout bruto, stderr bruto, env vars, process args, tokens e valores de secrets.

## 3. Sumário da evidência viva

- Total: 46 jobs.
- Ativos: 42 jobs.
- Pausados: 4 jobs.
- `last_status` não-ok: 0.
- Erros explícitos de delivery do scheduler: 0.
- Jobs ativos sem primeira execução registrada: 0.
- Jobs com `deliver=origin`: 4 ativos + 1 pausado.

## 4. Anomalias atuais

- Nenhum job com `last_status` não-ok na evidência viva atual.
- Nenhum erro explícito de delivery do scheduler na evidência estruturada atual.
- Nenhum job ativo sem primeira execução registrada.

## 5. Drift vs snapshot anterior

- Contagem mudou vs 2026-06-28: 44 → 46 totais; 40 → 42 ativos; 4 pausados estável.
- Novo/observado vs snapshot anterior: `e3af978c6af6` Honcho Nightly Intelligence Enforcement Audit — 02h35 BRT, active/local/ok, primeiro run observado 2026-06-29T05:41:31+00:00.
- Novo/observado vs snapshot anterior: `ba8ca37bfebd` Honcho semantic contamination audit — daily local, active/local/ok, primeiro run observado 2026-06-29T09:13:13+00:00.
- Novo/observado vs snapshot anterior: `fac3e13782c4` Honcho quality watchdog — silent OK, active/`deliver=origin`/ok, primeiro run observado 2026-06-29T10:44:11+00:00.
- Job futuro anterior removido/ausente na evidência atual: `00a9f839879f` Honcho utility go/no-go review one-shot não aparece mais em `/opt/data/cron/jobs.json`; tratar como histórico/removido ou executado/limpo fora deste snapshot, sem manter como ativo sem evidência viva.
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
| `518634d5ea60` | Reminder OS — 2h open-loop watchdog | ok | 2026-06-29T09:55:10.930670+00:00 |
| `749ee30b51eb` | Mesa COO diária Telegram | ok | 2026-06-29T09:01:47.443982+00:00 |
| `98478b820720` | Relatório Hermes diário 01h+02h+02h15+02h25+02h50 + Score 0–100 — 03h Telegram | ok | 2026-06-29T06:02:35.668251+00:00 |
| `fac3e13782c4` | Honcho quality watchdog — silent OK | ok | 2026-06-29T10:44:11.285164+00:00 |

Pausado:

| id | nome | last_status | last_run |
|---|---|---:|---|
| `955dc769b5a6` | LK specialist Telegram gateway watchdog | ok | 2026-05-30T15:52:55.190857+00:00 |

## 8. Gaps documentais/acionáveis

1. Novos/observados jobs Honcho de 2026-06-29 precisam ser reconciliados em documentação operacional: owner, finalidade, critério de sucesso, contrato de alerta e por que `fac3e13782c4` usa `deliver=origin` apesar de declarar silent-OK.
2. `00a9f839879f` saiu da evidência viva; documentar como histórico/removido/executado quando houver fonte canônica, mas não tratá-lo como ativo sem live evidence.
3. `2e5bc91d27d6` ainda precisa de documentação de owner/finalidade/critério de sucesso em rodada própria.
4. Watchdogs pausados de gateways especialistas devem continuar documentados como históricos/pausados até evidência viva de reativação.

## 9. O que não foi alterado

- Nenhum job foi criado, editado, pausado, retomado, removido ou disparado.
- Nenhuma entrega `local`/`origin` foi alterada.
- Nenhum Docker/VPS/Traefik/container/rede/gateway foi tocado.
- Nenhuma integração externa, campanha, mensagem, banco, Shopify, GMC, Notion, WhatsApp, email ou secret foi acessado para escrita.

## 10. Artefatos atualizados

- `areas/operacoes/inventarios/crons-agentes-profiles.md`.
- `reports/governance/runtime-truth-reconciler-2026-06-29.md`.
- `reports/brain-health-check-2026-06-29-runtime-truth-reconciler.json`.

## 11. Verificação

- Brain health check: `python3 scripts/brain_health_check.py --json reports/brain-health-check-2026-06-29-runtime-truth-reconciler.json` → `All checks passed` (`FAIL=0`, `WARN=0`).
- `git diff --check` nos artefatos tocados → sem erros.
- Secret scan escopado nos artefatos tocados → `scoped_possible_secrets 0`.
- Status escopado confirmou alterações apenas nos artefatos esperados deste reconciler; havia alterações/untracked preexistentes fora deste escopo e não foram tocados.

## 12. Apêndice — inventário sanitizado compacto

| id | estado | nome | deliver | last_status | last_run |
|---|---|---|---:|---:|---|
| `16dfc4d14c85` | active | Honcho Intelligence Layer v1 weekly silent-OK | local | ok | 2026-06-29T07:35:16.159613+00:00 |
| `23143847316e` | active | Brain OS silent-OK health/scanner watchdog — 02h25 BRT local | local | ok | 2026-06-29T05:25:10.683854+00:00 |
| `2404c0766d33` | active | Hermes Brain Runtime Truth Reconciler | local | ok | 2026-06-28T11:24:03.173660+00:00 |
| `2e5bc91d27d6` | active | Hermes Nightly Operations Audit OS — 02h50 BRT | local | ok | 2026-06-29T05:50:02.486425+00:00 |
| `357d40a5863e` | active | Zipper OS vendas 09h WhatsApp/email | local | ok | 2026-06-26T12:01:03.463326+00:00 |
| `39b176e08174` | active | Honcho memory quality auditor silent-OK | local | ok | 2026-06-29T07:20:17.588733+00:00 |
| `3cd1011edf33` | active | claude-max-proxy watchdog | local | ok | 2026-06-29T11:16:12.429696+00:00 |
| `3fc45b0830c6` | active | Hermes Brain Fechamento Ágil 01h + Brain Sync | local | ok | 2026-06-29T04:07:29.042011+00:00 |
| `4bb4e2223fd3` | active | Hermes compression failure self-heal watchdog | local | ok | 2026-06-29T11:20:10.693453+00:00 |
| `518634d5ea60` | active | Reminder OS — 2h open-loop watchdog | origin | ok | 2026-06-29T09:55:10.930670+00:00 |
| `5bacaa61bb12` | active | claude-proxy-watchdog | local | ok | 2026-06-29T11:17:10.429721+00:00 |
| `663e3e6a148c` | paused | SPITI Telegram gateway watchdog | local | ok | 2026-05-30T15:52:55.201503+00:00 |
| `6792657c0be7` | active | LK POS pós-compra WhatsApp auto-worker | local | ok | 2026-06-29T11:15:10.636260+00:00 |
| `71b147362ec1` | active | Zipper Gmail style learning refresh | local | ok | 2026-06-29T06:20:24.063845+00:00 |
| `749ee30b51eb` | active | Mesa COO diária Telegram | origin | ok | 2026-06-29T09:01:47.443982+00:00 |
| `787134d4ac5c` | active | LK Weekly Collection Sort Rule B | local | ok | 2026-06-26T09:00:49.092438+00:00 |
| `7b7ae67655c5` | active | wacli pessoal sync watchdog | local | ok | 2026-06-29T11:20:10.825259+00:00 |
| `7c688553e293` | active | LK Daily Sales Brief read-only mandatory delivery | local | ok | 2026-06-29T11:00:37.170005+00:00 |
| `7d32b8b77317` | active | Honcho Hermes memory watchdog silent-OK | local | ok | 2026-06-29T11:09:10.435944+00:00 |
| `810c0d2bf65a` | active | LC Mordomo OS real local no-agent watcher | local | ok | 2026-06-29T11:15:10.518284+00:00 |
| `876d54c62ccd` | paused | LK Growth Telegram gateway watchdog | local | ok | 2026-05-30T15:52:55.226608+00:00 |
| `953b9055458e` | active | LK Weekly CEO Review read-only mandatory delivery | local | ok | 2026-06-22T12:01:34.320459+00:00 |
| `955dc769b5a6` | paused | LK specialist Telegram gateway watchdog | origin | ok | 2026-05-30T15:52:55.190857+00:00 |
| `98478b820720` | active | Relatório Hermes diário 01h+02h+02h15+02h25+02h50 + Score 0–100 — 03h Telegram | origin | ok | 2026-06-29T06:02:35.668251+00:00 |
| `a1d1e36f8075` | active | LK Weekly Catalog Badges BEST SELLER sync | local | ok | 2026-06-26T09:41:24.509401+00:00 |
| `a2ead305eab2` | active | LK 19h30 physical store close external delivery | local | ok | 2026-06-28T22:31:22.633224+00:00 |
| `a97a6317b197` | active | Zipper post-PDF follow-up watchdog | local | ok | 2026-06-29T11:19:13.421072+00:00 |
| `ac0b440e2643` | paused | Mordomo Telegram gateway watchdog | local | ok | 2026-05-30T15:52:55.213145+00:00 |
| `b78ae7ac81d0` | active | Hermes all Telegram gateways watchdog | local | ok | 2026-06-29T11:21:16.142612+00:00 |
| `ba8ca37bfebd` | active | Honcho semantic contamination audit — daily local | local | ok | 2026-06-29T09:13:13.680976+00:00 |
| `bc96bb03d2b0` | active | Hermes Memory OS daytime checker/router — 30min alert-only | local | ok | 2026-06-29T10:52:12.824679+00:00 |
| `c1ce34b4449a` | active | Hermes multi-profile latency watchdog | local | ok | 2026-06-29T11:06:11.022226+00:00 |
| `c3bb587519d2` | active | LK Pulso Comercial 16h read-only delivery | local | ok | 2026-06-28T19:00:57.980976+00:00 |
| `c64a0c63b881` | active | LK Tiny stock local DB daily fullsync | local | ok | 2026-06-29T10:45:09.523749+00:00 |
| `c933dd2e30ec` | active | WACLI health read-only pre-Zipper 08h50 BRT | local | ok | 2026-06-26T11:50:54.489920+00:00 |
| `d03fa04e1188` | active | Hermes Brain Operating Layer structural watchdog | local | ok | 2026-06-29T11:10:10.346863+00:00 |
| `d9badcd83411` | active | Hermes Brain strict-runtime guard watchdog | local | ok | 2026-06-29T10:00:12.440653+00:00 |
| `e2f169cc046a` | active | LK POS Shopify→fila reconciliador | local | ok | 2026-06-29T11:20:11.403298+00:00 |
| `e3279babbc4a` | active | LK 09h previous-day sales report external delivery | local | ok | 2026-06-28T12:00:31.532550+00:00 |
| `e3af978c6af6` | active | Honcho Nightly Intelligence Enforcement Audit — 02h35 BRT | local | ok | 2026-06-29T05:41:31.438283+00:00 |
| `e4c6b7c9b6dc` | active | Hermes Memory OS weekly observability local/silent | local | ok | 2026-06-22T12:45:35.355233+00:00 |
| `edd06fe19397` | active | Hermes runtime + cron watchdog no_agent | local | ok | 2026-06-29T11:00:11.148546+00:00 |
| `f4c499e85eac` | active | Lucas Brain weekly Learning Loop report | local | ok | 2026-06-22T12:20:44.318435+00:00 |
| `f5a23dd6a1bd` | active | LC Hermes daily intelligence loop — systemwide audit + self-improvement | local | ok | 2026-06-29T05:07:09.544212+00:00 |
| `f9a1d43caf48` | active | Hermes memory hygiene watchdog 02h15 BRT | local | ok | 2026-06-29T05:15:01.735234+00:00 |
| `fac3e13782c4` | active | Honcho quality watchdog — silent OK | origin | ok | 2026-06-29T10:44:11.285164+00:00 |
