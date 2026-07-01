# Runtime Truth Reconciler — 2026-07-01

## 1. Timestamp e escopo

- Timestamp UTC: 2026-07-01 11:21 UTC.
- Escopo: reconciliação read-only/local da evidência viva de crons Hermes com documentação do Brain.
- Workdir: `/opt/data/hermes_bruno_ingest/hermes-brain`.
- Honcho: ferramentas `honcho_context/search/reasoning` não estão expostas neste cron; usei Brain/skills já carregadas e evidência viva de cron. Estados Honcho tratados apenas como evidência de scheduler: configured/active/runtime job, não como prova isolada de utility sem auditoria dedicada.
- Não houve alteração em cron, gateway, Docker, VPS, Traefik, redes, containers, integrações externas, campanhas, Shopify, GMC, Notion, WhatsApp, email, bancos ou secrets.

## 2. Fonte de evidência viva

- Comando primário solicitado: `cronjob list`.
- Resultado: `cronjob` não disponível no PATH deste runtime.
- Fallback canônico usado: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.
- Fonte estruturada sanitizada para contagem: `/opt/data/cron/jobs.json`.
- Campos usados: `id`, `name`, estado active/paused, `deliver`, `last_status`, `last_run_at`, `last_delivery_error`, `next_run_at`.
- Campos não versionados: prompts, stdout bruto, stderr bruto, env vars, process args, tokens e valores de secrets.

## 3. Sumário da evidência viva

- Total: 50 jobs.
- Ativos: 46 jobs.
- Pausados: 4 jobs.
- `last_status` não-ok: 1.
- Erros explícitos de delivery do scheduler: 0.
- Jobs ativos sem primeira execução registrada: 1.
- Jobs com `deliver=origin`: 7 ativos + 1 pausado.

## 4. Anomalias atuais

- `ec0473a3a010` Hermes Brain safe GitHub checkpoint 30min — active, `deliver=local`, `last_status=error` em 2026-07-01T11:00:55.547030+00:00; stdout sanitizado do scheduler indica bloqueio por `git diff --check failed`.
- `git diff --check` manual confirmou duas falhas locais de linha em branco final em `areas/operacoes/approval-packets/webhook-secret-secondary-gateways-cleanup-20260630.md` e `reports/daily-consolidation/2026-07-01.md`.
- Auto-remediation A1 aplicada: removidas apenas as linhas em branco finais nesses dois docs locais. Nenhuma mutação de cron/runtime/externos foi feita. O próximo tick/readback do checkpoint deve confirmar se o job recupera para `ok`.
- Jobs ativos sem primeira execução registrada: `dbafe9b8bfca` Skill Surface Diet weekly supervised review prompt.
- Nenhum erro explícito de delivery do scheduler na evidência estruturada atual.

## 5. Drift vs snapshot anterior

- Contagem estável vs 2026-06-30: 50 totais / 46 ativos / 4 pausados.
- Drift negativo: `ec0473a3a010` passou de `ok` para `error` por `git diff --check failed`.
- Drift positivo: `27916e815136` Skill Surface Diet monthly heavy-skill curation audit agora tem primeira execução registrada e `ok` em 2026-07-01T06:15:50.528302+00:00.
- `dbafe9b8bfca` segue active/`deliver=origin`/sem primeira execução; acompanhar até 2026-07-06T05:45 UTC e documentar owner/finalidade/critério de sucesso/contrato de alerta.
- `fac3e13782c4` Honcho quality watchdog — silent OK segue active/`deliver=origin`/ok e ainda precisa de contrato documental de alerta/ruído.
- `2e5bc91d27d6` Hermes Nightly Operations Audit OS — 02h50 BRT segue ativo/local/ok e ainda merece reconciliação documental de owner/finalidade/critério de sucesso em rodada própria.
- Documentação que descreve Mordomo/LK Growth/SPITI gateway watchdogs como ativos deve permanecer marcada como histórica até nova evidência viva mostrar reativação.

## 6. Jobs pausados na evidência viva

| id | nome | deliver | last_status | last_run |
|---|---|---|---|---|
| `663e3e6a148c` | SPITI Telegram gateway watchdog | local | ok | 2026-05-30T15:52:55.201503+00:00 |
| `876d54c62ccd` | LK Growth Telegram gateway watchdog | local | ok | 2026-05-30T15:52:55.226608+00:00 |
| `955dc769b5a6` | LK specialist Telegram gateway watchdog | origin | ok | 2026-05-30T15:52:55.190857+00:00 |
| `ac0b440e2643` | Mordomo Telegram gateway watchdog | local | ok | 2026-05-30T15:52:55.213145+00:00 |

## 7. Jobs `deliver=origin`

Ativos:

| id | nome | deliver | last_status | last_run |
|---|---|---|---|---|
| `27916e815136` | Skill Surface Diet monthly heavy-skill curation audit | origin | ok | 2026-07-01T06:15:50.528302+00:00 |
| `518634d5ea60` | Reminder OS — 2h open-loop watchdog | origin | ok | 2026-07-01T10:07:59.189967+00:00 |
| `749ee30b51eb` | Mesa COO diária Telegram | origin | ok | 2026-07-01T09:03:11.332114+00:00 |
| `98478b820720` | Relatório Hermes diário 01h+02h+02h15+02h25+02h50 + Score 0–100 — 03h Telegram | origin | ok | 2026-07-01T06:02:04.619597+00:00 |
| `ce165b7246d3` | Skill Surface Diet daily drift audit read-only | origin | ok | 2026-07-01T05:30:50.576538+00:00 |
| `dbafe9b8bfca` | Skill Surface Diet weekly supervised review prompt | origin | — | — |
| `fac3e13782c4` | Honcho quality watchdog — silent OK | origin | ok | 2026-07-01T11:14:57.435668+00:00 |

Pausado:

| id | nome | deliver | last_status | last_run |
|---|---|---|---|---|
| `955dc769b5a6` | LK specialist Telegram gateway watchdog | origin | ok | 2026-05-30T15:52:55.190857+00:00 |

## 8. Gaps documentais/acionáveis

1. `ec0473a3a010` está com `last_status=error` por `git diff --check failed`; auto-remediation local já removeu as duas linhas em branco finais encontradas, mas o scheduler ainda precisa de próximo tick/readback para confirmar recuperação.
2. `dbafe9b8bfca` está ativo, `deliver=origin` e ainda sem primeira execução; acompanhar até o primeiro run/readback em 2026-07-06.
3. Jobs Skill Surface Diet com `deliver=origin` precisam explicitar owner, finalidade, critério de sucesso e contrato de alerta/ruído.
4. `fac3e13782c4` continua com nome silent-OK e `deliver=origin`; permanece gap documental de contrato de alerta/ruído, sem mutação de delivery por este reconciler.
5. `2e5bc91d27d6` ainda precisa de documentação de owner/finalidade/critério de sucesso em rodada própria.
6. Watchdogs pausados de gateways especialistas devem continuar documentados como históricos/pausados até evidência viva de reativação.

## 9. O que não foi alterado

- Nenhum job foi criado, editado, pausado, retomado, removido ou disparado.
- Nenhuma entrega `local`/`origin` foi alterada.
- Nenhum Docker/VPS/Traefik/container/rede/gateway foi tocado.
- Nenhuma integração externa, campanha, mensagem, banco, Shopify, GMC, Notion, WhatsApp, email ou secret foi acessado para escrita.
- Alteração local/documental segura aplicada fora dos artefatos do reconciler: remoção de linha em branco final em dois docs que bloqueavam `git diff --check`.

## 10. Artefatos atualizados

- `areas/operacoes/inventarios/crons-agentes-profiles.md`.
- `reports/governance/runtime-truth-reconciler-2026-07-01.md`.
- `reports/brain-health-check-2026-07-01-runtime-truth-reconciler.json`.
- Auto-remediation A1 local: `areas/operacoes/approval-packets/webhook-secret-secondary-gateways-cleanup-20260630.md` e `reports/daily-consolidation/2026-07-01.md` tiveram apenas linha em branco final removida.

## 11. Verificação

- Brain health check: `python3 scripts/brain_health_check.py --json reports/brain-health-check-2026-07-01-runtime-truth-reconciler.json` → `All checks passed` (`FAIL=0`, `WARN=0`).
- `git diff --check` nos artefatos tocados → sem erros.
- Secret scan escopado nos artefatos tocados → `scoped_possible_secrets 0`.
- Status escopado confirmou atualização do inventário, criação do report/health JSON e auto-remediation A1 em dois docs locais com linha em branco final.

## 12. Apêndice — inventário sanitizado compacto

| id | estado | nome | deliver | last_status | last_run |
|---|---|---|---|---|---|
| `16dfc4d14c85` | active | Honcho Intelligence Layer v1 weekly silent-OK | local | ok | 2026-06-29T07:35:16.159613+00:00 |
| `23143847316e` | active | Brain OS silent-OK health/scanner watchdog — 02h25 BRT local | local | ok | 2026-07-01T05:25:55.775395+00:00 |
| `2404c0766d33` | active | Hermes Brain Runtime Truth Reconciler | local | ok | 2026-06-30T11:23:40.789949+00:00 |
| `27916e815136` | active | Skill Surface Diet monthly heavy-skill curation audit | origin | ok | 2026-07-01T06:15:50.528302+00:00 |
| `2e5bc91d27d6` | active | Hermes Nightly Operations Audit OS — 02h50 BRT | local | ok | 2026-07-01T05:50:46.297185+00:00 |
| `357d40a5863e` | active | Zipper OS vendas 09h WhatsApp/email | local | ok | 2026-06-30T12:00:11.626401+00:00 |
| `39b176e08174` | active | Honcho memory quality auditor silent-OK | local | ok | 2026-07-01T07:20:57.830140+00:00 |
| `3cd1011edf33` | active | claude-max-proxy watchdog | local | ok | 2026-07-01T11:16:57.611187+00:00 |
| `3fc45b0830c6` | active | Hermes Brain Fechamento Ágil 01h + Brain Sync | local | ok | 2026-07-01T04:08:52.478472+00:00 |
| `4bb4e2223fd3` | active | Hermes compression failure self-heal watchdog | local | ok | 2026-07-01T11:20:55.931418+00:00 |
| `518634d5ea60` | active | Reminder OS — 2h open-loop watchdog | origin | ok | 2026-07-01T10:07:59.189967+00:00 |
| `5bacaa61bb12` | active | claude-proxy-watchdog | local | ok | 2026-07-01T11:16:55.583134+00:00 |
| `663e3e6a148c` | paused | SPITI Telegram gateway watchdog | local | ok | 2026-05-30T15:52:55.201503+00:00 |
| `6792657c0be7` | active | LK POS pós-compra WhatsApp auto-worker | local | ok | 2026-07-01T11:15:55.825681+00:00 |
| `71b147362ec1` | active | Zipper Gmail style learning refresh | local | ok | 2026-07-01T06:21:07.509206+00:00 |
| `749ee30b51eb` | active | Mesa COO diária Telegram | origin | ok | 2026-07-01T09:03:11.332114+00:00 |
| `787134d4ac5c` | active | LK Weekly Collection Sort Rule B | local | ok | 2026-06-26T09:00:49.092438+00:00 |
| `7b7ae67655c5` | active | wacli pessoal sync watchdog | local | ok | 2026-07-01T11:19:55.972355+00:00 |
| `7c688553e293` | active | LK Daily Sales Brief read-only mandatory delivery | local | ok | 2026-07-01T11:01:47.456296+00:00 |
| `7d32b8b77317` | active | Honcho Hermes memory watchdog silent-OK | local | ok | 2026-07-01T11:10:55.821569+00:00 |
| `810c0d2bf65a` | active | LC Mordomo OS real local no-agent watcher | local | ok | 2026-07-01T11:15:55.716306+00:00 |
| `876d54c62ccd` | paused | LK Growth Telegram gateway watchdog | local | ok | 2026-05-30T15:52:55.226608+00:00 |
| `953b9055458e` | active | LK Weekly CEO Review read-only mandatory delivery | local | ok | 2026-06-29T12:00:24.703013+00:00 |
| `955dc769b5a6` | paused | LK specialist Telegram gateway watchdog | origin | ok | 2026-05-30T15:52:55.190857+00:00 |
| `98478b820720` | active | Relatório Hermes diário 01h+02h+02h15+02h25+02h50 + Score 0–100 — 03h Telegram | origin | ok | 2026-07-01T06:02:04.619597+00:00 |
| `a1d1e36f8075` | active | LK Weekly Catalog Badges BEST SELLER sync | local | ok | 2026-06-26T09:41:24.509401+00:00 |
| `a2ead305eab2` | active | LK 19h30 physical store close external delivery | local | ok | 2026-06-30T22:30:49.467872+00:00 |
| `a97a6317b197` | active | Zipper post-PDF follow-up watchdog | local | ok | 2026-07-01T10:51:58.741539+00:00 |
| `ac0b440e2643` | paused | Mordomo Telegram gateway watchdog | local | ok | 2026-05-30T15:52:55.213145+00:00 |
| `b78ae7ac81d0` | active | Hermes all Telegram gateways watchdog | local | ok | 2026-07-01T11:20:03.207106+00:00 |
| `ba8ca37bfebd` | active | Honcho semantic contamination audit — daily local | local | ok | 2026-07-01T07:40:56.992122+00:00 |
| `bc96bb03d2b0` | active | Hermes Memory OS daytime checker/router — 30min alert-only | local | ok | 2026-07-01T10:55:58.171894+00:00 |
| `c1ce34b4449a` | active | Hermes multi-profile latency watchdog | local | ok | 2026-07-01T11:17:56.934697+00:00 |
| `c3bb587519d2` | active | LK Pulso Comercial 16h read-only delivery | local | ok | 2026-06-30T19:00:40.267080+00:00 |
| `c64a0c63b881` | active | LK Tiny stock local DB daily fullsync | local | ok | 2026-07-01T10:45:54.079550+00:00 |
| `c933dd2e30ec` | active | WACLI health read-only pre-Zipper 08h50 BRT | local | ok | 2026-06-30T11:50:04.739464+00:00 |
| `ce165b7246d3` | active | Skill Surface Diet daily drift audit read-only | origin | ok | 2026-07-01T05:30:50.576538+00:00 |
| `d03fa04e1188` | active | Hermes Brain Operating Layer structural watchdog | local | ok | 2026-07-01T11:10:55.482817+00:00 |
| `d9badcd83411` | active | Hermes Brain strict-runtime guard watchdog | local | ok | 2026-07-01T10:00:57.529468+00:00 |
| `dbafe9b8bfca` | active | Skill Surface Diet weekly supervised review prompt | origin | — | — |
| `e2f169cc046a` | active | LK POS Shopify→fila reconciliador | local | ok | 2026-07-01T11:20:56.659495+00:00 |
| `e3279babbc4a` | active | LK 09h previous-day sales report external delivery | local | ok | 2026-06-30T12:00:38.645351+00:00 |
| `e3af978c6af6` | active | Honcho Nightly Intelligence Enforcement Audit — 02h35 BRT | local | ok | 2026-07-01T05:44:48.319366+00:00 |
| `e4c6b7c9b6dc` | active | Hermes Memory OS weekly observability local/silent | local | ok | 2026-06-29T12:45:14.460362+00:00 |
| `ec0473a3a010` | active | Hermes Brain safe GitHub checkpoint 30min | local | error | 2026-07-01T11:00:55.547030+00:00 |
| `edd06fe19397` | active | Hermes runtime + cron watchdog no_agent | local | ok | 2026-07-01T11:00:55.934465+00:00 |
| `f4c499e85eac` | active | Lucas Brain weekly Learning Loop report | local | ok | 2026-06-29T12:18:48.862210+00:00 |
| `f5a23dd6a1bd` | active | LC Hermes daily intelligence loop — systemwide audit + self-improvement | local | ok | 2026-07-01T05:09:53.651948+00:00 |
| `f9a1d43caf48` | active | Hermes memory hygiene watchdog 02h15 BRT | local | ok | 2026-07-01T05:15:45.888919+00:00 |
| `fac3e13782c4` | active | Honcho quality watchdog — silent OK | origin | ok | 2026-07-01T11:14:57.435668+00:00 |
