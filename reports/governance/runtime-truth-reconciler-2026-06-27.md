# Runtime Truth Reconciler — 2026-06-27

## 1. Timestamp e escopo

- Timestamp UTC: 2026-06-27 11:20 UTC.
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

- `e3279babbc4a` — LK 09h previous-day sales report external delivery — active, `deliver=local`, `last_status=error`, último run 2026-06-26T12:00:58.418039+00:00. Causa sanitizada: o script de entrega externa aprovado falhou porque o payload gerado não continha `message/html/email_meta`. Este reconciler não alterou script, cron, runtime nem executou envio externo.

## 5. Drift vs snapshot anterior

- Contagem estável vs 2026-06-26: 44 totais / 40 ativos / 4 pausados.
- Drift positivo: `bc96bb03d2b0` Hermes Memory OS daytime checker/router recuperou de `error` para `ok` na evidência viva atual.
- Drift negativo: `e3279babbc4a` passou de `ok` no snapshot de 2026-06-26 para `error`; requer correção/triagem da geração de payload da rotina LK 09h antes de considerar a entrega externa saudável.
- `00a9f839879f` segue ativo/`deliver=origin`/sem primeira execução; acompanhar até 2026-06-29T01:10 UTC e documentar owner/finalidade/critério de sucesso/contrato de alerta.
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
| `518634d5ea60` | Reminder OS — 2h open-loop watchdog | ok | 2026-06-27T09:35:43.608429+00:00 |
| `749ee30b51eb` | Mesa COO diária Telegram | ok | 2026-06-27T09:02:12.034568+00:00 |
| `98478b820720` | Relatório Hermes diário 01h+02h+02h15+02h25+02h50 + Score 0–100 — 03h Telegram | ok | 2026-06-27T06:01:26.916791+00:00 |

Pausado:

| id | nome | last_status | last_run |
|---|---|---:|---|
| `955dc769b5a6` | LK specialist Telegram gateway watchdog | ok | 2026-05-30T15:52:55.190857+00:00 |

## 8. Gaps documentais/acionáveis

1. `e3279babbc4a` está com `last_status=error`: triagem local necessária na geração de payload da rotina LK 09h external delivery. Não executar envio externo sem approval/contrato próprio.
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
- `reports/governance/runtime-truth-reconciler-2026-06-27.md`.
- `reports/brain-health-check-2026-06-27-runtime-truth-reconciler.json`.

## 11. Verificação

- Brain health check: `python3 scripts/brain_health_check.py --json reports/brain-health-check-2026-06-27-runtime-truth-reconciler.json` → `All checks passed` (`FAIL=0`, `WARN=0`).
- `git diff --check` nos artefatos tocados → sem erros.
- Secret scan escopado nos artefatos tocados → `scoped_possible_secrets 0`.
- Status escopado confirmou alterações apenas nos artefatos esperados deste reconciler; havia alterações/untracked preexistentes fora deste escopo e não foram tocados.

## 12. Apêndice — inventário sanitizado compacto

| id | estado | nome | deliver | last_status | last_run |
|---|---|---|---:|---:|---|
| `00a9f839879f` | active | Honcho utility go/no-go review one-shot | origin | sem primeira execução | sem Last run |
| `16dfc4d14c85` | active | Honcho Intelligence Layer v1 weekly silent-OK | local | ok | 2026-06-22T07:35:48.811949+00:00 |
| `23143847316e` | active | Brain OS silent-OK health/scanner watchdog — 02h25 BRT local | local | ok | 2026-06-27T05:25:42.898681+00:00 |
| `2404c0766d33` | active | Hermes Brain Runtime Truth Reconciler | local | ok | 2026-06-26T11:24:19.049967+00:00 |
| `2e5bc91d27d6` | active | Hermes Nightly Operations Audit OS — 02h50 BRT | local | ok | 2026-06-27T05:50:34.975865+00:00 |
| `357d40a5863e` | active | Zipper OS vendas 09h WhatsApp/email | local | ok | 2026-06-26T12:01:03.463326+00:00 |
| `39b176e08174` | active | Honcho memory quality auditor silent-OK | local | ok | 2026-06-27T07:20:46.359009+00:00 |
| `3cd1011edf33` | active | claude-max-proxy watchdog | local | ok | 2026-06-27T11:15:44.816757+00:00 |
| `3fc45b0830c6` | active | Hermes Brain Fechamento Ágil 01h + Brain Sync | local | ok | 2026-06-27T04:08:10.663594+00:00 |
| `4bb4e2223fd3` | active | Hermes compression failure self-heal watchdog | local | ok | 2026-06-27T11:20:43.032338+00:00 |
| `518634d5ea60` | active | Reminder OS — 2h open-loop watchdog | origin | ok | 2026-06-27T09:35:43.608429+00:00 |
| `5bacaa61bb12` | active | claude-proxy-watchdog | local | ok | 2026-06-27T11:19:42.870306+00:00 |
| `6792657c0be7` | active | LK POS pós-compra WhatsApp auto-worker | local | ok | 2026-06-27T11:15:42.889272+00:00 |
| `71b147362ec1` | active | Zipper Gmail style learning refresh | local | ok | 2026-06-27T06:21:44.417623+00:00 |
| `749ee30b51eb` | active | Mesa COO diária Telegram | origin | ok | 2026-06-27T09:02:12.034568+00:00 |
| `787134d4ac5c` | active | LK Weekly Collection Sort Rule B | local | ok | 2026-06-26T09:00:49.092438+00:00 |
| `7b7ae67655c5` | active | wacli pessoal sync watchdog | local | ok | 2026-06-27T11:15:43.077436+00:00 |
| `7c688553e293` | active | LK Daily Sales Brief read-only mandatory delivery | local | ok | 2026-06-27T11:01:35.083200+00:00 |
| `7d32b8b77317` | active | Honcho Hermes memory watchdog silent-OK | local | ok | 2026-06-27T11:08:42.867102+00:00 |
| `810c0d2bf65a` | active | LC Mordomo OS real local no-agent watcher | local | ok | 2026-06-27T11:17:42.933864+00:00 |
| `953b9055458e` | active | LK Weekly CEO Review read-only mandatory delivery | local | ok | 2026-06-22T12:01:34.320459+00:00 |
| `98478b820720` | active | Relatório Hermes diário 01h+02h+02h15+02h25+02h50 + Score 0–100 — 03h Telegram | origin | ok | 2026-06-27T06:01:26.916791+00:00 |
| `a1d1e36f8075` | active | LK Weekly Catalog Badges BEST SELLER sync | local | ok | 2026-06-26T09:41:24.509401+00:00 |
| `a2ead305eab2` | active | LK 19h30 physical store close external delivery | local | ok | 2026-06-26T22:30:33.118679+00:00 |
| `a97a6317b197` | active | Zipper post-PDF follow-up watchdog | local | ok | 2026-06-27T11:15:45.660790+00:00 |
| `b78ae7ac81d0` | active | Hermes all Telegram gateways watchdog | local | ok | 2026-06-27T11:19:49.015089+00:00 |
| `bc96bb03d2b0` | active | Hermes Memory OS daytime checker/router — 30min alert-only | local | ok | 2026-06-27T11:19:45.962506+00:00 |
| `c1ce34b4449a` | active | Hermes multi-profile latency watchdog | local | ok | 2026-06-27T11:08:43.578476+00:00 |
| `c3bb587519d2` | active | LK Pulso Comercial 16h read-only delivery | local | ok | 2026-06-26T19:00:26.542585+00:00 |
| `c64a0c63b881` | active | LK Tiny stock local DB daily fullsync | local | ok | 2026-06-27T10:45:41.841233+00:00 |
| `c933dd2e30ec` | active | WACLI health read-only pre-Zipper 08h50 BRT | local | ok | 2026-06-26T11:50:54.489920+00:00 |
| `d03fa04e1188` | active | Hermes Brain Operating Layer structural watchdog | local | ok | 2026-06-27T11:10:42.712369+00:00 |
| `d9badcd83411` | active | Hermes Brain strict-runtime guard watchdog | local | ok | 2026-06-27T10:00:45.952085+00:00 |
| `e2f169cc046a` | active | LK POS Shopify→fila reconciliador | local | ok | 2026-06-27T11:20:43.713346+00:00 |
| `e3279babbc4a` | active | LK 09h previous-day sales report external delivery | local | error | 2026-06-26T12:00:58.418039+00:00 |
| `e4c6b7c9b6dc` | active | Hermes Memory OS weekly observability local/silent | local | ok | 2026-06-22T12:45:35.355233+00:00 |
| `edd06fe19397` | active | Hermes runtime + cron watchdog no_agent | local | ok | 2026-06-27T11:00:43.389905+00:00 |
| `f4c499e85eac` | active | Lucas Brain weekly Learning Loop report | local | ok | 2026-06-22T12:20:44.318435+00:00 |
| `f5a23dd6a1bd` | active | LC Hermes daily intelligence loop — systemwide audit + self-improvement | local | ok | 2026-06-27T05:08:55.006548+00:00 |
| `f9a1d43caf48` | active | Hermes memory hygiene watchdog 02h15 BRT | local | ok | 2026-06-27T05:15:34.708136+00:00 |
| `663e3e6a148c` | paused | SPITI Telegram gateway watchdog | local | ok | 2026-05-30T15:52:55.201503+00:00 |
| `876d54c62ccd` | paused | LK Growth Telegram gateway watchdog | local | ok | 2026-05-30T15:52:55.226608+00:00 |
| `955dc769b5a6` | paused | LK specialist Telegram gateway watchdog | origin | ok | 2026-05-30T15:52:55.190857+00:00 |
| `ac0b440e2643` | paused | Mordomo Telegram gateway watchdog | local | ok | 2026-05-30T15:52:55.213145+00:00 |
