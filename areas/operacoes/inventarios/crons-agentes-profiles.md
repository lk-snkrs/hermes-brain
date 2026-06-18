# Inventário vivo — crons, agentes, profiles e projetos

Data-base: 2026-06-17 11:20 UTC
Status: **Fase 1A aprovada por Lucas — inventário inicial + Fechamento recorrente ativo; última evidência runtime via fallback Hermes CLI em 2026-06-17**

---

### Atualização 2026-06-17 11:20 UTC

**Fonte:** `cronjob list` solicitado; `cronjob` não disponível no PATH deste runtime. Fallback canônico usado: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.

**Contagem:** 40 jobs totais — 36 ativos, 4 pausados.

**`last_status` não-ok:** 0. Todos os jobs com execução registrada constam `ok` na evidência viva desta execução.

**Erros explícitos de delivery do scheduler:** 0 na listagem. **Falhas em stdout de job:** 0 observadas pela listagem resumida.

**Jobs ativos sem primeira execução registrada:** 1.
- `7ef586b9ec1a` Reanalisar backlog Auto-Remediation em 72h — job one-shot ativo, `deliver=origin`, sem `Last run` ainda; próxima execução prevista para 2026-06-17T13:31 UTC.

**Jobs pausados na evidência viva:**
- `ac0b440e2643` Mordomo Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `876d54c62ccd` LK Growth Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `663e3e6a148c` SPITI Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `955dc769b5a6` LK specialist Telegram gateway watchdog — pausado, `deliver=origin`, último status ok em 2026-05-30T15:52.

**Drift/notable reconciliation:**
- Contagem estável vs 2026-06-16: 40 totais / 36 ativos / 4 pausados.
- Nenhum novo job vivo, job removido, `last_status` não-ok ou erro explícito de delivery na evidência atual.
- `7ef586b9ec1a` segue como o único job ativo sem primeira execução registrada; acompanhar até a primeira execução prevista.
- Jobs recentes `7ef586b9ec1a` e `2e5bc91d27d6` continuam vivos e ainda merecem reconciliação documental de owner/finalidade/critério de sucesso em rodada própria.
- Rotinas previamente problemáticas (`d03fa04e1188`, `c3bb587519d2`, `e3279babbc4a`, `a2ead305eab2`, `357d40a5863e`, `787134d4ac5c`, `a1d1e36f8075`) seguem `ok`; não manter como falha ativa sem nova evidência.
- Documentação que descreve Mordomo/LK Growth/SPITI gateway watchdogs como ativos deve permanecer marcada como histórica até nova evidência viva mostrar reativação.

**Jobs deliver=origin (saídas intencionais/condicionais):** Mesa COO diária (`749ee30b51eb`), Relatório Hermes 01h+02h+02h15+02h25+02h50 + Score 0–100 — 03h Telegram (`98478b820720`), Reminder OS — 2h open-loop watchdog (`518634d5ea60`) e Reanalisar backlog Auto-Remediation em 72h (`7ef586b9ec1a`). `LK specialist Telegram gateway watchdog` (`955dc769b5a6`) também está configurado como `origin`, mas está pausado.

**Relatório completo:** `reports/governance/runtime-truth-reconciler-2026-06-17.md`

---

### Atualização 2026-06-16 11:20 UTC

**Fonte:** `cronjob list` solicitado; `cronjob` não disponível no PATH deste runtime. Fallback canônico usado: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.

**Contagem:** 40 jobs totais — 36 ativos, 4 pausados.

**`last_status` não-ok:** 0. Todos os jobs com execução registrada constam `ok` na evidência viva desta execução.

**Erros explícitos de delivery do scheduler:** 0 na listagem. **Falhas em stdout de job:** 0 observadas pela listagem resumida.

**Jobs ativos sem primeira execução registrada:** 1.
- `7ef586b9ec1a` Reanalisar backlog Auto-Remediation em 72h — job one-shot ativo, `deliver=origin`, sem `Last run` ainda; próxima execução prevista para 2026-06-17T13:31 UTC.

**Jobs pausados na evidência viva:**
- `ac0b440e2643` Mordomo Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `876d54c62ccd` LK Growth Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `663e3e6a148c` SPITI Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `955dc769b5a6` LK specialist Telegram gateway watchdog — pausado, `deliver=origin`, último status ok em 2026-05-30T15:52.

**Drift/notable reconciliation:**
- Contagem estável vs 2026-06-15: 40 totais / 36 ativos / 4 pausados.
- Nenhum novo job vivo, job removido, `last_status` não-ok ou erro explícito de delivery na evidência atual.
- `7ef586b9ec1a` segue como o único job ativo sem primeira execução registrada; acompanhar até a primeira execução prevista.
- Jobs recentes `7ef586b9ec1a` e `2e5bc91d27d6` continuam vivos e ainda merecem reconciliação documental de owner/finalidade/critério de sucesso em rodada própria.
- Rotinas previamente problemáticas (`d03fa04e1188`, `c3bb587519d2`, `e3279babbc4a`, `a2ead305eab2`, `357d40a5863e`, `787134d4ac5c`, `a1d1e36f8075`) seguem `ok`; não manter como falha ativa sem nova evidência.
- Documentação que descreve Mordomo/LK Growth/SPITI gateway watchdogs como ativos deve permanecer marcada como histórica até nova evidência viva mostrar reativação.

**Jobs deliver=origin (saídas intencionais/condicionais):** Mesa COO diária (`749ee30b51eb`), Relatório Hermes 01h+02h+02h15+02h25+02h50 + Score 0–100 — 03h Telegram (`98478b820720`), Reminder OS — 2h open-loop watchdog (`518634d5ea60`) e Reanalisar backlog Auto-Remediation em 72h (`7ef586b9ec1a`). `LK specialist Telegram gateway watchdog` (`955dc769b5a6`) também está configurado como `origin`, mas está pausado.

**Relatório completo:** `reports/governance/runtime-truth-reconciler-2026-06-16.md`

---

### Atualização 2026-06-15 11:20 UTC

**Fonte:** `cronjob list` solicitado; `cronjob` não disponível no PATH deste runtime. Fallback canônico usado: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.

**Contagem:** 40 jobs totais — 36 ativos, 4 pausados.

**`last_status` não-ok:** 0. Todos os jobs com execução registrada constam `ok` na evidência viva desta execução.

**Erros explícitos de delivery do scheduler:** 0 na listagem. **Falhas em stdout de job:** 0 observadas pela listagem resumida.

**Jobs ativos sem primeira execução registrada:** 1.
- `7ef586b9ec1a` Reanalisar backlog Auto-Remediation em 72h — job one-shot ativo, `deliver=origin`, sem `Last run` ainda; próxima execução prevista para 2026-06-17T13:31 UTC.

**Jobs pausados na evidência viva:**
- `ac0b440e2643` Mordomo Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `876d54c62ccd` LK Growth Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `663e3e6a148c` SPITI Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `955dc769b5a6` LK specialist Telegram gateway watchdog — pausado, `deliver=origin`, último status ok em 2026-05-30T15:52.

**Drift/notable reconciliation:**
- Contagem mudou vs 2026-06-14: 38 → 40 totais; 34 → 36 ativos; 4 pausados estável.
- Novos jobs vivos na evidência: `7ef586b9ec1a` Reanalisar backlog Auto-Remediation em 72h — one-shot ativo/sem primeira execução; `2e5bc91d27d6` Hermes Nightly Operations Audit OS — 02h50 BRT — ativo/local/ok.
- Alguns jobs antes listados como `deliver=origin` aparecem agora como `deliver=local`: `c1ce34b4449a` Hermes multi-profile latency watchdog, `b78ae7ac81d0` Hermes all Telegram gateways watchdog, `7b7ae67655c5` wacli pessoal sync watchdog, `bc96bb03d2b0` Hermes Memory OS daytime checker/router e `23143847316e` Brain OS silent-OK health/scanner watchdog. Tratar como drift documental/operacional benigno até confirmação por histórico/decisão; não alterar cron sem aprovação.
- Nenhum `last_status` não-ok ou erro explícito de delivery na evidência atual.
- Rotinas previamente problemáticas (`d03fa04e1188`, `c3bb587519d2`, `e3279babbc4a`, `a2ead305eab2`, `357d40a5863e`, `787134d4ac5c`, `a1d1e36f8075`) seguem `ok`; não manter como falha ativa sem nova evidência.
- Documentação que descreve Mordomo/LK Growth/SPITI gateway watchdogs como ativos deve permanecer marcada como histórica até nova evidência viva mostrar reativação.

**Jobs deliver=origin (saídas intencionais/condicionais):** Mesa COO diária (`749ee30b51eb`), Relatório Hermes 01h+02h+02h15+02h25+02h50 + Score 0–100 — 03h Telegram (`98478b820720`), Reminder OS — 2h open-loop watchdog (`518634d5ea60`) e Reanalisar backlog Auto-Remediation em 72h (`7ef586b9ec1a`). `LK specialist Telegram gateway watchdog` (`955dc769b5a6`) também está configurado como `origin`, mas está pausado.

**Relatório completo:** `reports/governance/runtime-truth-reconciler-2026-06-15.md`

---

### Atualização 2026-06-14 11:20 UTC

**Fonte:** `cronjob list` solicitado; `cronjob` não disponível no PATH deste runtime. Fallback canônico usado: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.

**Contagem:** 38 jobs totais — 34 ativos, 4 pausados.

**`last_status` não-ok:** 0. Todos os jobs listados constam `ok` na evidência viva desta execução.

**Erros explícitos de delivery do scheduler:** 0 na listagem. **Falhas em stdout de job:** 0 observadas pela listagem resumida.

**Jobs ativos sem primeira execução registrada:** 0.

**Jobs pausados na evidência viva:**
- `ac0b440e2643` Mordomo Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `876d54c62ccd` LK Growth Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `663e3e6a148c` SPITI Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `955dc769b5a6` LK specialist Telegram gateway watchdog — pausado, `deliver=origin`, último status ok em 2026-05-30T15:52.

**Drift/notable reconciliation:**
- Contagem estável vs 2026-06-13: 38 totais / 34 ativos / 4 pausados.
- Nenhum novo job vivo, job removido, `last_status` não-ok, erro explícito de delivery ou job ativo sem primeira execução registrada na evidência atual.
- Jobs adicionados à evidência em 2026-06-10 (`bc96bb03d2b0`, `6792657c0be7`, `e4c6b7c9b6dc`, `e2f169cc046a`), 2026-06-12 (`23143847316e`) e 2026-06-13 (`518634d5ea60`) seguem ativos/ok e ainda merecem reconciliação documental em rodada própria quando relevante.
- Rotinas previamente problemáticas (`d03fa04e1188`, `c3bb587519d2`, `e3279babbc4a`, `a2ead305eab2`, `357d40a5863e`, `787134d4ac5c`, `a1d1e36f8075`) seguem `ok`; não manter como falha ativa sem nova evidência.
- Documentação que descreve Mordomo/LK Growth/SPITI gateway watchdogs como ativos deve permanecer marcada como histórica até nova evidência viva mostrar reativação.

**Jobs deliver=origin (saídas intencionais/condicionais):** Mesa COO diária (`749ee30b51eb`), Relatório Hermes 01h+02h+02h15 (`98478b820720`), Hermes multi-profile latency watchdog (`c1ce34b4449a`), Hermes all Telegram gateways watchdog (`b78ae7ac81d0`), wacli pessoal sync watchdog (`7b7ae67655c5`), Hermes Memory OS daytime checker/router (`bc96bb03d2b0`), Brain OS silent-OK health/scanner watchdog (`23143847316e`) e Reminder OS — 2h open-loop watchdog (`518634d5ea60`). `LK specialist Telegram gateway watchdog` (`955dc769b5a6`) também está configurado como `origin`, mas está pausado.

**Relatório completo:** `reports/governance/runtime-truth-reconciler-2026-06-14.md`

---

### Atualização 2026-06-13 11:21 UTC

**Fonte:** `cronjob list` solicitado; `cronjob` não disponível no PATH deste runtime. Fallback canônico usado: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.

**Contagem:** 38 jobs totais — 34 ativos, 4 pausados.

**`last_status` não-ok:** 0. Todos os jobs listados constam `ok` na evidência viva desta execução.

**Erros explícitos de delivery do scheduler:** 0 na listagem. **Falhas em stdout de job:** 0 observadas pela listagem resumida.

**Jobs ativos sem primeira execução registrada:** 0.

**Jobs pausados na evidência viva:**
- `ac0b440e2643` Mordomo Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `876d54c62ccd` LK Growth Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `663e3e6a148c` SPITI Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `955dc769b5a6` LK specialist Telegram gateway watchdog — pausado, `deliver=origin`, último status ok em 2026-05-30T15:52.

**Drift/notable reconciliation:**
- Contagem mudou vs 2026-06-12: 37 → 38 totais; 33 → 34 ativos; 4 pausados estável.
- Novo job ativo/ok na evidência viva: `518634d5ea60` Reminder OS — 2h open-loop watchdog — `origin`, script `reminder_os_watchdog.py`, último status `ok` em 2026-06-13T09:35.
- Nenhum job removido, `last_status` não-ok, erro explícito de delivery ou job ativo sem primeira execução registrada na evidência atual.
- Jobs adicionados à evidência em 2026-06-10 (`bc96bb03d2b0`, `6792657c0be7`, `e4c6b7c9b6dc`, `e2f169cc046a`) e 2026-06-12 (`23143847316e`) seguem ativos/ok e ainda merecem reconciliação documental em rodada própria quando relevante.
- Rotinas previamente problemáticas (`d03fa04e1188`, `c3bb587519d2`, `e3279babbc4a`, `a2ead305eab2`, `357d40a5863e`, `787134d4ac5c`, `a1d1e36f8075`) seguem `ok`; não manter como falha ativa sem nova evidência.
- Documentação que descreve Mordomo/LK Growth/SPITI gateway watchdogs como ativos deve permanecer marcada como histórica até nova evidência viva mostrar reativação.

**Jobs deliver=origin (saídas intencionais/condicionais):** Mesa COO diária (`749ee30b51eb`), Relatório Hermes 01h+02h+02h15 (`98478b820720`), Hermes multi-profile latency watchdog (`c1ce34b4449a`), Hermes all Telegram gateways watchdog (`b78ae7ac81d0`), wacli pessoal sync watchdog (`7b7ae67655c5`), Hermes Memory OS daytime checker/router (`bc96bb03d2b0`), Brain OS silent-OK health/scanner watchdog (`23143847316e`) e Reminder OS — 2h open-loop watchdog (`518634d5ea60`). `LK specialist Telegram gateway watchdog` (`955dc769b5a6`) também está configurado como `origin`, mas está pausado.

**Relatório completo:** `reports/governance/runtime-truth-reconciler-2026-06-13.md`

---

### Atualização 2026-06-12 11:20 UTC

**Fonte:** `cronjob list` solicitado; `cronjob` não disponível no PATH deste runtime. Fallback canônico usado: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.

**Contagem:** 37 jobs totais — 33 ativos, 4 pausados.

**`last_status` não-ok:** 0. Todos os jobs listados constam `ok` na evidência viva desta execução.

**Erros explícitos de delivery do scheduler:** 0 na listagem. **Falhas em stdout de job:** 0 observadas pela listagem resumida.

**Jobs ativos sem primeira execução registrada:** 0.

**Jobs pausados na evidência viva:**
- `ac0b440e2643` Mordomo Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `876d54c62ccd` LK Growth Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `663e3e6a148c` SPITI Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `955dc769b5a6` LK specialist Telegram gateway watchdog — pausado, `deliver=origin`, último status ok em 2026-05-30T15:52.

**Drift/notable reconciliation:**
- Contagem mudou vs 2026-06-11: 36 → 37 totais; 32 → 33 ativos; 4 pausados estável.
- Novo job ativo/ok na evidência viva: `23143847316e` Brain OS silent-OK health/scanner watchdog — `origin`, script `brain_os_silent_ok_watchdog.py`, último status `ok` em 2026-06-12T10:30.
- Nenhum job removido, `last_status` não-ok, erro explícito de delivery ou job ativo sem primeira execução registrada na evidência atual.
- Jobs adicionados à evidência em 2026-06-10 (`bc96bb03d2b0`, `6792657c0be7`, `e4c6b7c9b6dc`, `e2f169cc046a`) seguem ativos/ok e ainda merecem reconciliação documental em rodada própria quando relevante.
- Rotinas previamente problemáticas (`d03fa04e1188`, `c3bb587519d2`, `e3279babbc4a`, `a2ead305eab2`, `357d40a5863e`, `787134d4ac5c`, `a1d1e36f8075`) seguem `ok`; não manter como falha ativa sem nova evidência.
- Documentação que descreve Mordomo/LK Growth/SPITI gateway watchdogs como ativos deve permanecer marcada como histórica até nova evidência viva mostrar reativação.

**Jobs deliver=origin (saídas intencionais/condicionais):** Mesa COO diária (`749ee30b51eb`), Relatório Hermes 01h+02h+02h15 (`98478b820720`), Hermes multi-profile latency watchdog (`c1ce34b4449a`), Hermes all Telegram gateways watchdog (`b78ae7ac81d0`), wacli pessoal sync watchdog (`7b7ae67655c5`), Hermes Memory OS daytime checker/router (`bc96bb03d2b0`) e Brain OS silent-OK health/scanner watchdog (`23143847316e`). `LK specialist Telegram gateway watchdog` (`955dc769b5a6`) também está configurado como `origin`, mas está pausado.

**Relatório completo:** `reports/governance/runtime-truth-reconciler-2026-06-12.md`

---

### Atualização 2026-06-11 11:20 UTC

**Fonte:** `cronjob list` solicitado; `cronjob` não disponível no PATH deste runtime. Fallback canônico usado: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.

**Contagem:** 36 jobs totais — 32 ativos, 4 pausados.

**`last_status` não-ok:** 0. Todos os jobs listados constam `ok` na evidência viva desta execução.

**Erros explícitos de delivery do scheduler:** 0 na listagem. **Falhas em stdout de job:** 0 observadas pela listagem resumida.

**Jobs ativos sem primeira execução registrada:** 0.

**Jobs pausados na evidência viva:**
- `ac0b440e2643` Mordomo Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `876d54c62ccd` LK Growth Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `663e3e6a148c` SPITI Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `955dc769b5a6` LK specialist Telegram gateway watchdog — pausado, `deliver=origin`, último status ok em 2026-05-30T15:52.

**Drift/notable reconciliation:**
- Contagem estável vs 2026-06-10: 36 totais / 32 ativos / 4 pausados.
- Nenhum novo job vivo, job removido, `last_status` não-ok, erro explícito de delivery ou job ativo sem primeira execução registrada na evidência atual.
- Jobs adicionados à evidência em 2026-06-10 (`bc96bb03d2b0`, `6792657c0be7`, `e4c6b7c9b6dc`, `e2f169cc046a`) seguem ativos/ok e ainda merecem reconciliação documental em rodada própria quando relevante.
- Rotinas previamente problemáticas (`d03fa04e1188`, `c3bb587519d2`, `e3279babbc4a`, `a2ead305eab2`, `357d40a5863e`, `787134d4ac5c`, `a1d1e36f8075`) seguem `ok`; não manter como falha ativa sem nova evidência.
- Documentação que descreve Mordomo/LK Growth/SPITI gateway watchdogs como ativos deve permanecer marcada como histórica até nova evidência viva mostrar reativação.

**Jobs deliver=origin (saídas intencionais/condicionais):** Mesa COO diária (`749ee30b51eb`), Relatório Hermes 01h+02h+02h15 (`98478b820720`), Hermes multi-profile latency watchdog (`c1ce34b4449a`), Hermes all Telegram gateways watchdog (`b78ae7ac81d0`), Hermes Memory OS daytime checker/router (`bc96bb03d2b0`). `LK specialist Telegram gateway watchdog` (`955dc769b5a6`) também está configurado como `origin`, mas está pausado.

**Relatório completo:** `reports/governance/runtime-truth-reconciler-2026-06-11.md`

---

### Atualização 2026-06-10 11:20 UTC

**Fonte:** `cronjob list` solicitado; `cronjob` não disponível no PATH deste runtime. Fallback canônico usado: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.

**Contagem:** 36 jobs totais — 32 ativos, 4 pausados.

**`last_status` não-ok:** 0. Todos os jobs listados constam `ok` na evidência viva desta execução.

**Erros explícitos de delivery do scheduler:** 0 na listagem. **Falhas em stdout de job:** 0 observadas pela listagem resumida.

**Jobs ativos sem primeira execução registrada:** 0.

**Jobs pausados na evidência viva:**
- `ac0b440e2643` Mordomo Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `876d54c62ccd` LK Growth Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `663e3e6a148c` SPITI Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `955dc769b5a6` LK specialist Telegram gateway watchdog — pausado, `deliver=origin`, último status ok em 2026-05-30T15:52.

**Drift/notable reconciliation:**
- Contagem mudou vs 2026-06-09: 32 → 36 totais; 28 → 32 ativos; 4 pausados estável.
- Novos jobs ativos/ok na evidência viva: `bc96bb03d2b0` Hermes Memory OS daytime checker/router — 30min alert-only (`origin`), `6792657c0be7` LK POS pós-compra WhatsApp auto-worker (`local`), `e4c6b7c9b6dc` Hermes Memory OS weekly observability local/silent (`local`) e `e2f169cc046a` LK POS Shopify→fila reconciliador (`local`).
- Nenhum job removido, `last_status` não-ok, erro explícito de delivery ou job ativo sem primeira execução registrada na evidência atual.
- Rotinas previamente problemáticas (`d03fa04e1188`, `c3bb587519d2`, `e3279babbc4a`, `a2ead305eab2`, `357d40a5863e`, `787134d4ac5c`, `a1d1e36f8075`) seguem `ok`; não manter como falha ativa sem nova evidência.
- Documentação que descreve Mordomo/LK Growth/SPITI gateway watchdogs como ativos deve permanecer marcada como histórica até nova evidência viva mostrar reativação.

**Jobs deliver=origin (saídas intencionais/condicionais):** Mesa COO diária (`749ee30b51eb`), Relatório Hermes 01h+02h+02h15 (`98478b820720`), Hermes multi-profile latency watchdog (`c1ce34b4449a`), Hermes all Telegram gateways watchdog (`b78ae7ac81d0`), Hermes Memory OS daytime checker/router (`bc96bb03d2b0`). `LK specialist Telegram gateway watchdog` (`955dc769b5a6`) também está configurado como `origin`, mas está pausado.

**Relatório completo:** `reports/governance/runtime-truth-reconciler-2026-06-10.md`

---

### Atualização 2026-06-09 11:20 UTC

**Fonte:** `cronjob list` solicitado; `cronjob` não disponível no PATH deste runtime. Fallback canônico usado: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.

**Contagem:** 32 jobs totais — 28 ativos, 4 pausados.

**`last_status` não-ok:** 0. Todos os jobs listados constam `ok` na evidência viva desta execução.

**Erros explícitos de delivery do scheduler:** 0 na listagem. **Falhas em stdout de job:** 0 observadas pela listagem resumida.

**Jobs ativos sem primeira execução registrada:** 0.

**Jobs pausados na evidência viva:**
- `ac0b440e2643` Mordomo Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `876d54c62ccd` LK Growth Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `663e3e6a148c` SPITI Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `955dc769b5a6` LK specialist Telegram gateway watchdog — pausado, `deliver=origin`, último status ok em 2026-05-30T15:52.

**Drift/notable reconciliation:**
- Contagem estável vs 2026-06-08: 32 totais / 28 ativos / 4 pausados.
- Nenhum novo job vivo, job removido, `last_status` não-ok, erro explícito de delivery ou job ativo sem primeira execução registrada na evidência atual.
- Rotinas previamente problemáticas (`d03fa04e1188`, `c3bb587519d2`, `e3279babbc4a`, `a2ead305eab2`, `357d40a5863e`, `787134d4ac5c`, `a1d1e36f8075`) seguem `ok`; não manter como falha ativa sem nova evidência.
- Documentação que descreve Mordomo/LK Growth/SPITI gateway watchdogs como ativos deve permanecer marcada como histórica até nova evidência viva mostrar reativação.

**Jobs deliver=origin (saídas intencionais/condicionais):** Mesa COO diária (`749ee30b51eb`), Relatório Hermes 01h+02h+02h15 (`98478b820720`), Hermes multi-profile latency watchdog (`c1ce34b4449a`), Hermes all Telegram gateways watchdog (`b78ae7ac81d0`). `LK specialist Telegram gateway watchdog` (`955dc769b5a6`) também está configurado como `origin`, mas está pausado.

**Relatório completo:** `reports/governance/runtime-truth-reconciler-2026-06-09.md`

---

### Atualização 2026-06-08 11:20 UTC

**Fonte:** `cronjob list` solicitado; `cronjob` não disponível no PATH deste runtime. Fallback canônico usado: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.

**Contagem:** 32 jobs totais — 28 ativos, 4 pausados.

**`last_status` não-ok:** 0. Todos os jobs listados constam `ok` na evidência viva desta execução.

**Erros explícitos de delivery do scheduler:** 0 na listagem. **Falhas em stdout de job:** 0 observadas pela listagem resumida.

**Jobs ativos sem primeira execução registrada:** 0.

**Jobs pausados na evidência viva:**
- `ac0b440e2643` Mordomo Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `876d54c62ccd` LK Growth Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `663e3e6a148c` SPITI Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `955dc769b5a6` LK specialist Telegram gateway watchdog — pausado, `deliver=origin`, último status ok em 2026-05-30T15:52.

**Drift/notable reconciliation:**
- Contagem mudou vs 2026-06-07: 31 → 32 totais; 27 → 28 ativos; 4 pausados estável.
- Novo job ativo/ok na evidência viva: `edd06fe19397` Hermes runtime + cron watchdog no_agent — `local`, script `hermes_runtime_cron_watchdog.py`, último status `ok` em 2026-06-08T11:00.
- Rotinas previamente problemáticas (`d03fa04e1188`, `c3bb587519d2`, `e3279babbc4a`, `a2ead305eab2`, `357d40a5863e`, `787134d4ac5c`, `a1d1e36f8075`) seguem `ok`; não manter como falha ativa sem nova evidência.
- Documentação que descreve Mordomo/LK Growth/SPITI gateway watchdogs como ativos deve permanecer marcada como histórica até nova evidência viva mostrar reativação.

**Jobs deliver=origin (saídas intencionais/condicionais):** Mesa COO diária (`749ee30b51eb`), Relatório Hermes 01h+02h+02h15 (`98478b820720`), Hermes multi-profile latency watchdog (`c1ce34b4449a`), Hermes all Telegram gateways watchdog (`b78ae7ac81d0`). `LK specialist Telegram gateway watchdog` (`955dc769b5a6`) também está configurado como `origin`, mas está pausado.

**Relatório completo:** `reports/governance/runtime-truth-reconciler-2026-06-08.md`

---

### Atualização 2026-06-07 11:21 UTC

**Fonte:** `cronjob list` solicitado; `cronjob` não disponível no PATH deste runtime. Fallback canônico usado: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.

**Contagem:** 31 jobs totais — 27 ativos, 4 pausados.

**`last_status` não-ok:** 0. Todos os jobs com execução registrada constam `ok` na evidência viva desta execução.

**Erros explícitos de delivery do scheduler:** 0 na listagem. **Falhas em stdout de job:** 0 observadas pela listagem resumida.

**Jobs ativos sem primeira execução registrada:** 0.

**Jobs pausados na evidência viva:**
- `ac0b440e2643` Mordomo Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `876d54c62ccd` LK Growth Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `663e3e6a148c` SPITI Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `955dc769b5a6` LK specialist Telegram gateway watchdog — pausado, `deliver=origin`, último status ok em 2026-05-30T15:52.

**Drift/notable reconciliation:**
- Contagem estável vs 2026-06-06: 31 totais / 27 ativos / 4 pausados.
- A anomalia de 2026-06-06 (`d03fa04e1188` Hermes Brain Operating Layer structural watchdog por `memories/hot.md stale >3 days`) não aparece mais como falha ativa; o job consta `ok` em 2026-06-07T11:10.
- Rotinas externas LK/Zipper previamente problemáticas (`c3bb587519d2`, `e3279babbc4a`, `a2ead305eab2`, `357d40a5863e`) seguem `ok` na evidência viva; não manter como falha ativa sem nova evidência.
- `LK Weekly Collection Sort Rule B` (`787134d4ac5c`) segue `ok`; não há timeout ativo na evidência atual.
- `LK Weekly Catalog Badges BEST SELLER sync` (`a1d1e36f8075`) segue com primeira execução registrada e `ok`.
- Jobs ativos/ok que merecem incorporação documental em rodada própria quando relevante: `f5a23dd6a1bd` LC Hermes daily intelligence loop, `7c688553e293` LK Daily Sales Brief obrigatório, `953b9055458e` LK Weekly CEO Review obrigatório, `71b147362ec1` Zipper Gmail style learning refresh, `5bacaa61bb12`/`3cd1011edf33` watchdogs Claude proxy, `a97a6317b197` Zipper post-PDF follow-up, `7b7ae67655c5` wacli pessoal sync watchdog, `810c0d2bf65a` LC Mordomo OS real local no-agent watcher.
- Documentação que descreve Mordomo/LK Growth/SPITI gateway watchdogs como ativos deve permanecer marcada como histórica até nova evidência viva mostrar reativação.

**Jobs deliver=origin (saídas intencionais/condicionais):** Mesa COO diária (`749ee30b51eb`), Relatório Hermes 01h+02h+02h15 (`98478b820720`), Hermes multi-profile latency watchdog (`c1ce34b4449a`), Hermes all Telegram gateways watchdog (`b78ae7ac81d0`). `LK specialist Telegram gateway watchdog` (`955dc769b5a6`) também está configurado como `origin`, mas está pausado.

**Relatório completo:** `reports/governance/runtime-truth-reconciler-2026-06-07.md`

---

### Atualização 2026-06-06 11:20 UTC

**Fonte:** `cronjob list` solicitado; `cronjob` não disponível no PATH deste runtime. Fallback canônico usado: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.

**Contagem:** 31 jobs totais — 27 ativos, 4 pausados.

**`last_status` não-ok:** 1 — `Hermes Brain Operating Layer structural watchdog` (`d03fa04e1188`) falhou em 2026-06-06T11:10 com `Script exited with code 1`. O stdout informa auto-heal documental criando `memories/daily/2026-06-06.md`, mas ainda aponta `memories/hot.md stale >3 days`. Sem alteração de runtime/cron/Docker/VPS neste reconciler.

**Erros explícitos de delivery do scheduler:** 0 na listagem. **Falhas em stdout de job:** 1, no próprio watchdog `d03fa04e1188`.

**Jobs ativos sem primeira execução registrada:** 0.

**Jobs pausados na evidência viva:**
- `ac0b440e2643` Mordomo Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `876d54c62ccd` LK Growth Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `663e3e6a148c` SPITI Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `955dc769b5a6` LK specialist Telegram gateway watchdog — pausado, `deliver=origin`, último status ok em 2026-05-30T15:52.

**Drift/notable reconciliation:**
- Contagem mudou vs 2026-06-05: de 29 para 31 totais; de 25 para 27 ativos; 4 pausados estável.
- A anomalia atual mudou: `c3bb587519d2` consta `ok`, e o único não-ok vivo é `d03fa04e1188` por `memories/hot.md stale >3 days`.
- Rotinas externas LK/Zipper previamente problemáticas (`c3bb587519d2`, `e3279babbc4a`, `a2ead305eab2`, `357d40a5863e`) constam `ok` na evidência viva; não manter como falha ativa sem nova evidência.
- `LK Weekly Collection Sort Rule B` (`787134d4ac5c`) segue `ok`; não há timeout ativo na evidência atual.
- `LK Weekly Catalog Badges BEST SELLER sync` (`a1d1e36f8075`) segue com primeira execução registrada e `ok`.
- Jobs ativos/ok que merecem incorporação documental em rodada própria quando relevante: `f5a23dd6a1bd` LC Hermes daily intelligence loop, `7c688553e293` LK Daily Sales Brief obrigatório, `953b9055458e` LK Weekly CEO Review obrigatório, `71b147362ec1` Zipper Gmail style learning refresh, `5bacaa61bb12`/`3cd1011edf33` watchdogs Claude proxy, `a97a6317b197` Zipper post-PDF follow-up, `7b7ae67655c5` wacli pessoal sync watchdog.
- Documentação que descreve Mordomo/LK Growth/SPITI gateway watchdogs como ativos deve permanecer marcada como histórica até nova evidência viva mostrar reativação.

**Jobs deliver=origin (saídas intencionais/condicionais):** Mesa COO diária (`749ee30b51eb`), Relatório Hermes 01h+02h+02h15 (`98478b820720`), Hermes multi-profile latency watchdog (`c1ce34b4449a`), Hermes all Telegram gateways watchdog (`b78ae7ac81d0`). `LK specialist Telegram gateway watchdog` (`955dc769b5a6`) também está configurado como `origin`, mas está pausado.

**Relatório completo:** `reports/governance/runtime-truth-reconciler-2026-06-06.md`

---

### Atualização 2026-06-05 11:20 UTC

**Fonte:** `cronjob list` solicitado; `cronjob` não disponível no PATH deste runtime. Fallback canônico usado: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.

**Contagem:** 29 jobs totais — 25 ativos, 4 pausados.

**`last_status` não-ok:** 1 — `LK Pulso Comercial 16h read-only delivery` (`c3bb587519d2`) falhou em 2026-06-04T19:00 com `Script exited with code 1` durante envio externo aprovado via WACLI/parser JSON. Sem reautenticação, retry externo ou alteração de runtime neste reconciler.

**Erros explícitos de delivery do scheduler:** 0 na listagem. **Falhas de envio externo em stdout:** 1, no job `c3bb587519d2`.

**Jobs ativos sem primeira execução registrada:** 0. O job `a1d1e36f8075` LK Weekly Catalog Badges BEST SELLER sync executou em 2026-06-05T09:39 com status `ok`.

**Jobs pausados na evidência viva:**
- `ac0b440e2643` Mordomo Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `876d54c62ccd` LK Growth Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `663e3e6a148c` SPITI Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `955dc769b5a6` LK specialist Telegram gateway watchdog — pausado, `deliver=origin`, último status ok em 2026-05-30T15:52.

**Drift/notable reconciliation:**
- Contagem estável vs 2026-06-04: 29 totais / 25 ativos / 4 pausados.
- Anomalias reduziram de 4 para 1: `e3279babbc4a`, `a2ead305eab2` e `357d40a5863e` constam `ok` na evidência viva; docs/pendências que ainda os tratam como falha atual devem ser reconciliados.
- `a1d1e36f8075` deixou de ser job ativo sem primeira execução e agora deve ser documentado como executado/ok.
- `LK Weekly Collection Sort Rule B` (`787134d4ac5c`) segue ok após execução de 2026-06-05T09:01; não há timeout ativo na evidência atual.
- Documentação que descreve Mordomo/LK Growth/SPITI gateway watchdogs como ativos deve permanecer marcada como histórica até nova evidência viva mostrar reativação.

**Jobs deliver=origin (saídas intencionais/condicionais):** Mesa COO diária (`749ee30b51eb`), Relatório Hermes 01h+02h+02h15 (`98478b820720`), Hermes multi-profile latency watchdog (`c1ce34b4449a`), Hermes all Telegram gateways watchdog (`b78ae7ac81d0`). `LK specialist Telegram gateway watchdog` (`955dc769b5a6`) também está configurado como `origin`, mas está pausado.

**Relatório completo:** `reports/governance/runtime-truth-reconciler-2026-06-05.md`

---

### Atualização 2026-06-04 11:20 UTC

**Fonte:** `cronjob list` solicitado; `cronjob` não disponível no PATH deste runtime. Fallback canônico usado: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.

**Contagem:** 29 jobs totais — 25 ativos, 4 pausados.

**`last_status` não-ok:** 4 — falhas WACLI em `LK Pulso Comercial 16h read-only delivery` (`c3bb587519d2`), `LK 09h previous-day sales report external delivery` (`e3279babbc4a`), `LK 19h30 physical store close external delivery` (`a2ead305eab2`) e `Zipper OS vendas 09h WhatsApp/email` (`357d40a5863e`).

**Erros explícitos de delivery do scheduler:** 0 na listagem. **Falhas de envio externo em stdout:** 4 por WACLI `hermes` não autenticado.

**Jobs ativos sem primeira execução registrada:**
- `a1d1e36f8075` LK Weekly Catalog Badges BEST SELLER sync — ativo, `local`, próxima execução prevista para 2026-06-05T09:30.

**Jobs pausados na evidência viva:**
- `ac0b440e2643` Mordomo Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `876d54c62ccd` LK Growth Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `663e3e6a148c` SPITI Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `955dc769b5a6` LK specialist Telegram gateway watchdog — pausado, `deliver=origin`, último status ok em 2026-05-30T15:52.

**Drift/notable reconciliation:**
- Contagem estável vs 2026-06-03: 29 totais / 25 ativos / 4 pausados.
- Quatro rotinas de entrega externa aprovada seguem falhando por WACLI não autenticado; não foi feita nenhuma reautenticação ou write externo neste reconciler.
- `LK Weekly Collection Sort Rule B` (`787134d4ac5c`) deixou de aparecer como timeout persistente e agora consta `ok` em 2026-06-03T12:14; acompanhar regressão em vez de manter a classificação de timeout ativo.
- `LK Tiny stock local DB daily fullsync` (`c64a0c63b881`) e `Hermes memory hygiene watchdog 02h15 BRT` (`f9a1d43caf48`) continuam vivos e ok; devem entrar na documentação operacional quando houver rodada própria.
- Documentação que ainda descreve Mordomo/LK Growth/SPITI gateway watchdogs como ativos deve permanecer marcada como histórica até nova evidência viva mostrar reativação.
- Fechamento Ágil aparece na evidência viva como `Hermes Brain Fechamento Ágil 01h + Brain Sync` (`0 4 * * *`) e o relatório executivo como `Relatório Hermes diário 01h + 02h + 02h15 para Lucas` (`30 5 * * *`); docs antigas devem reconciliar o nome/schedule sem inferir intenção além da evidência runtime.

**Jobs deliver=origin (saídas intencionais/condicionais):** Mesa COO diária (`749ee30b51eb`), Relatório Hermes 01h+02h+02h15 (`98478b820720`), Hermes multi-profile latency watchdog (`c1ce34b4449a`), Hermes all Telegram gateways watchdog (`b78ae7ac81d0`). `LK specialist Telegram gateway watchdog` (`955dc769b5a6`) também está configurado como `origin`, mas está pausado.

**Relatório completo:** `reports/governance/runtime-truth-reconciler-2026-06-04.md`

---

### Atualização 2026-06-03 11:20 UTC

**Fonte:** `cronjob list` solicitado; `cronjob` não disponível no PATH deste runtime. Fallback canônico usado: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.

**Contagem:** 29 jobs totais — 25 ativos, 4 pausados.

**`last_status` não-ok:** 5 — falhas WACLI em `LK Pulso Comercial 16h read-only delivery` (`c3bb587519d2`), `LK 09h previous-day sales report external delivery` (`e3279babbc4a`), `LK 19h30 physical store close external delivery` (`a2ead305eab2`), `Zipper OS vendas 09h WhatsApp/email` (`357d40a5863e`), além do timeout persistente de `LK Weekly Collection Sort Rule B` (`787134d4ac5c`).

**Erros explícitos de delivery do scheduler:** 0 na listagem. **Falhas de envio externo em stdout:** 4 por WACLI `hermes` não autenticado.

**Jobs ativos sem primeira execução registrada:**
- `a1d1e36f8075` LK Weekly Catalog Badges BEST SELLER sync — ativo, `local`, próxima execução prevista para 2026-06-05T09:30.

**Jobs pausados na evidência viva:**
- `ac0b440e2643` Mordomo Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `876d54c62ccd` LK Growth Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `663e3e6a148c` SPITI Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `955dc769b5a6` LK specialist Telegram gateway watchdog — pausado, `deliver=origin`, último status ok em 2026-05-30T15:52.

**Drift/notable reconciliation:**
- Contagem estável vs 2026-06-02: 29 totais / 25 ativos / 4 pausados.
- Quatro rotinas de entrega externa aprovada seguem falhando por WACLI não autenticado; não foi feita nenhuma reautenticação ou write externo neste reconciler.
- `LK Weekly Collection Sort Rule B` segue como timeout persistente desde 2026-05-29; precisa frente própria para timeout/runner, não mudança automática neste reconciler.
- `LK Tiny stock local DB daily fullsync` (`c64a0c63b881`) e `Hermes memory hygiene watchdog 02h15 BRT` (`f9a1d43caf48`) continuam vivos e ok; devem entrar na documentação operacional quando houver rodada própria.
- Documentação que ainda descreve Mordomo/LK Growth/SPITI gateway watchdogs como ativos deve permanecer marcada como histórica até nova evidência viva mostrar reativação.
- Fechamento Ágil aparece na evidência viva como `Hermes Brain Fechamento Ágil 01h + Brain Sync` (`0 4 * * *`) e o relatório executivo como `Relatório Hermes diário 01h + 02h + 02h15 para Lucas` (`30 5 * * *`); docs antigas devem reconciliar o nome/schedule sem inferir intenção além da evidência runtime.

**Jobs deliver=origin (saídas intencionais/condicionais):** Mesa COO diária (`749ee30b51eb`), Relatório Hermes 01h+02h+02h15 (`98478b820720`), Hermes multi-profile latency watchdog (`c1ce34b4449a`), Hermes all Telegram gateways watchdog (`b78ae7ac81d0`). `LK specialist Telegram gateway watchdog` (`955dc769b5a6`) também está configurado como `origin`, mas está pausado.

**Relatório completo:** `reports/governance/runtime-truth-reconciler-2026-06-03.md`

---

### Atualização 2026-06-02 11:21 UTC

**Fonte:** `cronjob list` solicitado; `cronjob` não disponível no PATH deste runtime. Fallback canônico usado: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.

**Contagem:** 29 jobs totais — 25 ativos, 4 pausados.

**`last_status` não-ok:** 5 — falhas WACLI em `LK Pulso Comercial 16h read-only delivery` (`c3bb587519d2`), `LK 09h previous-day sales report external delivery` (`e3279babbc4a`), `LK 19h30 physical store close external delivery` (`a2ead305eab2`), `Zipper OS vendas 09h WhatsApp/email` (`357d40a5863e`), além do timeout persistente de `LK Weekly Collection Sort Rule B` (`787134d4ac5c`).

**Erros explícitos de delivery do scheduler:** 0 na listagem. **Falhas de envio externo em stdout:** 4 por WACLI `hermes` não autenticado.

**Jobs ativos sem primeira execução registrada:**
- `a1d1e36f8075` LK Weekly Catalog Badges BEST SELLER sync — ativo, `local`, próxima execução prevista para 2026-06-05T09:30.

**Jobs pausados na evidência viva:**
- `ac0b440e2643` Mordomo Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `876d54c62ccd` LK Growth Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `663e3e6a148c` SPITI Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `955dc769b5a6` LK specialist Telegram gateway watchdog — pausado, `deliver=origin`, último status ok em 2026-05-30T15:52.

**Drift/notable reconciliation:**
- Contagem subiu vs 2026-06-01: 27 → 29 totais / 23 → 25 ativos / 4 pausados estável.
- Novos jobs vivos a documentar em rodada própria: `c64a0c63b881` LK Tiny stock local DB daily fullsync e `f9a1d43caf48` Hermes memory hygiene watchdog 02h15 BRT.
- Quatro rotinas de entrega externa aprovada falharam por WACLI não autenticado; não foi feita nenhuma reautenticação ou write externo neste reconciler.
- `LK Weekly Collection Sort Rule B` segue como timeout persistente desde 2026-05-29; precisa frente própria para timeout/runner, não mudança automática neste reconciler.
- Documentação que ainda descreve Mordomo/LK Growth/SPITI gateway watchdogs como ativos deve permanecer marcada como histórica até nova evidência viva mostrar reativação.
- Fechamento Ágil aparece na evidência viva como `Hermes Brain Fechamento Ágil 01h + Brain Sync` (`0 4 * * *`) e o relatório executivo como `Relatório Hermes diário 01h + 02h + 02h15 para Lucas` (`30 5 * * *`); docs antigas devem reconciliar o nome/schedule sem inferir intenção além da evidência runtime.

**Jobs deliver=origin (saídas intencionais/condicionais):** Mesa COO diária (`749ee30b51eb`), Relatório Hermes 01h+02h+02h15 (`98478b820720`), Hermes multi-profile latency watchdog (`c1ce34b4449a`), Hermes all Telegram gateways watchdog (`b78ae7ac81d0`). `LK specialist Telegram gateway watchdog` (`955dc769b5a6`) também está configurado como `origin`, mas está pausado.

**Relatório completo:** `reports/governance/runtime-truth-reconciler-2026-06-02.md`

---

### Atualização 2026-06-01 11:20 UTC

**Fonte:** `cronjob list` solicitado; `cronjob` não disponível no PATH deste runtime. Fallback canônico usado: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.

**Contagem:** 27 jobs totais — 23 ativos, 4 pausados.

**`last_status` não-ok:** 1 — `LK Weekly Collection Sort Rule B` (`787134d4ac5c`) — timeout persistente (120s) desde 2026-05-29. Próximo run: 2026-06-05T09:00.

**Erros explícitos de delivery:** 0.

**Jobs ativos sem primeira execução registrada:**
- `a1d1e36f8075` LK Weekly Catalog Badges BEST SELLER sync — ativo, `local`, próxima execução prevista para 2026-06-05T09:30.

**Jobs pausados na evidência viva:**
- `ac0b440e2643` Mordomo Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `876d54c62ccd` LK Growth Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `663e3e6a148c` SPITI Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `955dc769b5a6` LK specialist Telegram gateway watchdog — pausado, `deliver=origin`, último status ok em 2026-05-30T15:52.

**Drift/notable reconciliation:**
- Contagem estável vs 2026-05-31: 27 totais / 23 ativos / 4 pausados.
- `LK Weekly Collection Sort Rule B` segue como único `last_status` não-ok; precisa frente própria para timeout/runner, não mudança automática neste reconciler.
- Documentação que ainda descreve Mordomo/LK Growth/SPITI gateway watchdogs como ativos deve permanecer marcada como histórica até nova evidência viva mostrar reativação.
- `claude-proxy-watchdog`, `claude-max-proxy watchdog` e `Hermes all Telegram gateways watchdog` continuam ativos e devem seguir no inventário documental de runtime/modelos.

**Jobs deliver=origin (saídas intencionais/condicionais):** Mesa COO diária (`749ee30b51eb`), Relatório Hermes 23h+02h (`98478b820720`), Hermes multi-profile latency watchdog (`c1ce34b4449a`), Hermes all Telegram gateways watchdog (`b78ae7ac81d0`). `LK specialist Telegram gateway watchdog` (`955dc769b5a6`) também está configurado como `origin`, mas está pausado.

**Relatório completo:** `reports/governance/runtime-truth-reconciler-2026-06-01.md`

---

### Atualização 2026-05-31 11:20 UTC

**Fonte:** `cronjob list` solicitado; `cronjob` não disponível no PATH deste runtime. Fallback canônico usado: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.

**Contagem:** 27 jobs totais — 23 ativos, 4 pausados.

**`last_status` não-ok:** 1 — `LK Weekly Collection Sort Rule B` (`787134d4ac5c`) — timeout persistente (120s) desde 2026-05-29. Próximo run: 2026-06-05T09:00.

**Erros explícitos de delivery:** 0.

**Jobs pausados na evidência viva:**
- `ac0b440e2643` Mordomo Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `876d54c62ccd` LK Growth Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `663e3e6a148c` SPITI Telegram gateway watchdog — pausado, último status ok em 2026-05-30T15:52.
- `955dc769b5a6` LK specialist Telegram gateway watchdog — pausado, `deliver=origin`, último status ok em 2026-05-30T15:52.

**Drift/notable reconciliation:**
- `claude-proxy-watchdog` (`5bacaa61bb12`) e `claude-max-proxy watchdog` (`3cd1011edf33`) estão ativos e precisam entrar no inventário documental de runtime/modelos.
- `Hermes all Telegram gateways watchdog` (`b78ae7ac81d0`) está ativo com `deliver=origin` e deve ser documentado como alerta condicional.
- `LK Weekly Catalog Badges BEST SELLER sync` (`a1d1e36f8075`) segue ativo, sem primeira execução registrada; próxima execução prevista para 2026-06-05T09:30.
- Documentação que ainda descreve Mordomo/LK Growth/SPITI gateway watchdogs como ativos deve ser reconciliada com o estado vivo atual: crons pausados.

**Jobs deliver=origin (saídas intencionais/condicionais):** Mesa COO diária (`749ee30b51eb`), Relatório Hermes 23h+02h (`98478b820720`), Hermes multi-profile latency watchdog (`c1ce34b4449a`), Hermes all Telegram gateways watchdog (`b78ae7ac81d0`). `LK specialist Telegram gateway watchdog` (`955dc769b5a6`) também está configurado como `origin`, mas está pausado.

**Relatório completo:** `reports/governance/runtime-truth-reconciler-2026-05-31.md`

---

### Atualização 2026-05-30 11:20 UTC

**Fonte:** `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`

**Contagem:** 23 jobs ativos, 0 pausados.

**`last_status` não-ok:** 1 — `LK Weekly Collection Sort Rule B` (`787134d4ac5c`) — timeout persistente (120s) desde 2026-05-29. Próximo run: 2026-06-05T09:00.

**Novos jobs vs evidência anterior (2026-05-29):**
- `d03fa04e1188` Hermes Brain Operating Layer structural watchdog — ok (2026-05-30T11:10)
- `d9badcd83411` Hermes Brain strict-runtime guard watchdog — ok (2026-05-30T10:01)
- `2404c0766d33` Hermes Brain Runtime Truth Reconciler — ok (2026-05-29T11:22)
- `a1d1e36f8075` LK Weekly Catalog Badges BEST SELLER sync — novo job, sem last run ainda, next 2026-06-05T09:30

**Jobs deliver=origin (saídas intencionais):** Mesa COO diária (749ee30b51eb), Relatório Hermes 23h+02h (98478b820720), Hermes multi-profile latency watchdog (c1ce34b4449a) — todos ok.

**Relatório completo:** `reports/governance/runtime-truth-reconciler-2026-05-30.md`

---
Escopo: Hermes Brain / Grande Mente / profiles especialistas / crons Hermes.

## 1. Princípio

Este inventário existe para garantir que o **Fechamento Ágil 23h** não consolide apenas “agentes” em abstrato. Ele deve cobrir também:

- profiles/bots reais em runtime;
- canais de conversa;
- crons e watchdogs script-only;
- projetos/rotinas associados;
- destino do handoff no Brain;
- gaps de documentação ou cobertura.

Regra curta:

> Especialista executa. Grande Mente consolida. Conversa relevante vira decisão, pendência, receipt, handoff, rotina, skill, PRD/BRD ou relatório no Brain.

## 2. Critério de entrada no Fechamento 23h

Uma conversa, cron ou entrega entra no fechamento se gerar pelo menos um destes sinais:

- decisão de Lucas ou responsável autorizado;
- pendência ou follow-up;
- aprovação;
- bloqueio/risco;
- entrega/relatório/receipt;
- write externo aprovado;
- correção de Lucas;
- aprendizado durável;
- mudança em projeto/rotina;
- exceção/falha operacional.

O fechamento **não** deve virar transcrição de chat.

## 3. Cobertura por agente/profile/bot

### 3.1 Hermes Geral / Grande Mente

- Status: **ativo**.
- Runtime/profile: `/opt/data`.
- Superfície: Telegram principal de Lucas + API/gateway principal.
- Caminho documental: `agentes/hermes-geral/`, `empresa/`, `areas/operacoes/`, `MAPA.md`.
- Projetos/rotinas associados:
  - Hermes Brain;
  - Mission Control;
  - Mesa COO;
  - Fechamento Ágil 23h;
  - governança multiempresa;
  - skills/memória/crons;
  - health checks.
- Entra no Fechamento 23h: **sim**.
- Destino de handoff: `reports/daily-consolidation/YYYY-MM-DD.md`, `empresa/gestao/pendencias.md`, `memories/`, rotinas/projetos correspondentes.
- Gap: nenhum bloqueante; deve ser a camada coordenadora.

### 3.2 Lucas pessoal / Mordomo

- Status: **ativo/parcialmente pausado conforme crons**.
- Runtime/profile conhecido: `/opt/data/profiles/mordomo`.
- Superfície: Telegram/bot Mordomo e WhatsApp pessoal via ferramentas locais quando habilitadas.
- Caminho documental atual: `areas/operacoes/` e docs de Mordomo; gap conhecido para pasta documental dedicada `agentes/mordomo/` ou `areas/lucas-pessoal/` se volume crescer.
- Projetos/rotinas associados:
  - intake pessoal;
  - follow-ups;
  - agenda/calendário;
  - WhatsApp pessoal;
  - CRM local/Mordomo;
  - drafts/previews internos.
- Crons relacionados:
  - `Mordomo Telegram gateway watchdog` — ativo, `local`, script-only.
  - `Mordomo WhatsApp pessoal resumo 17h BRT` — pausado.
  - `Mordomo WhatsApp pessoal realtime scan` — pausado, local.
  - `Mordomo: confirmar entrega com Seda Embalagens` — pausado/one-shot antigo.
- Entra no Fechamento 23h: **sim, quando houver conversa com decisão, follow-up, risco ou entrega**.
- Destino de handoff: `areas/operacoes/calendar-intake/`, `areas/operacoes/decision-inbox/`, `empresa/gestao/pendencias.md`, relatório diário.
- Gap: separar melhor Lucas pessoal/Mordomo da área Operações no Brain.

### 3.3 LK OS — LK Sneakers

- Status: **ativo**.
- Runtime/profile: Hermes Geral + scripts/crons; especialista LK Growth separado.
- Superfícies:
  - Telegram principal para decisões/exceções;
  - WhatsApp grupo LK Vendas para relatórios aprovados;
  - email `lk@...` para companions aprovados;
  - Mission Control;
  - crons LK.
- Caminho documental: `areas/lk/`, `agentes/lk/`, rotinas LK, reports LK.
- Projetos/rotinas associados:
  - Daily Sales Brief;
  - Weekly CEO Review;
  - GMC/SEO/CRO/GEO;
  - Pulso 16h;
  - relatório 09h dia anterior;
  - fechamento loja física 19h30;
  - CRM/Klaviyo;
  - stock/sourcing;
  - paid/influencer intelligence.
- Crons relacionados:
  - `LK Daily Sales Brief read-only mandatory delivery` — ativo, `local`.
  - `LK Weekly CEO Review read-only mandatory delivery` — ativo, `local`.
  - `LK GMC Review read-only mandatory delivery` — ativo na evidência viva de 2026-05-22; read-only obrigatório.
  - `LK Pulso Comercial 16h read-only delivery` — ativo, `local`.
  - `LK 09h previous-day sales report external delivery` — ativo, `local` após correção de delivery/ruído; entrega externa é feita pelo script, Telegram recebe só exceções quando aplicável.
  - `LK 19h30 physical store close external delivery` — ativo, `local` após correção de Lucas para não enviar recibo/HTML de sucesso no Telegram.
  - `LK weekly influencer sales email` — pausado.
  - `LK SEO/CRO weekly Claude SEO improvement loop` — pausado.
  - `LK SEO/CRO impact review — SEO title/meta P1 packets` — pausado.
  - `LK WhatsApp Hermes responder watchdog` — ativo, `local`.
- Entra no Fechamento 23h: **sim**.
- Destino de handoff: `areas/lk/`, `reports/`, `empresa/gestao/pendencias.md`, relatório diário.
- Gap: classificar quais crons LK devem ficar `local` por sucesso normal vs `origin` para decisões/exceções.

### 3.4 LK Growth OS

- Status: **ativo**.
- Runtime/profile conhecido: `/opt/data/profiles/lk-growth`.
- Bot conhecido: `@LKGrowth_HermesBot`.
- Caminho documental: `areas/lk/sub-areas/growth/` e referências nos mapas globais.
- Projetos/rotinas associados:
  - SEO/CRO/GEO;
  - conteúdo/newsletter;
  - Renan/Growth;
  - Klaviyo dentro do escopo de conteúdo;
  - impacto de mudanças SEO.
- Crons relacionados:
  - `LK Growth Telegram gateway watchdog` — ativo, `local`.
  - rotinas SEO/CRO pausadas no Hermes Geral, a revisar se devem migrar/rodar no profile Growth.
- Entra no Fechamento 23h: **sim, se houver output, aprovação, campanha, conteúdo, decisão ou gap de handoff**.
- Destino de handoff: `areas/lk/sub-areas/growth/`, `areas/lk/`, relatório diário.
- Gap: link global ainda precisa ficar mais explícito para não parecer agente solto.

### 3.5 Zipper OS — Zipper Galeria

- Status: **ativo**.
- Runtime/profile: ainda não mapeado como profile próprio no inventário atual; operações rodam via Hermes Geral/scripts.
- Superfícies:
  - Zipper Vendas / reports;
  - Gmail/style learning;
  - WhatsApp Zipper quando aprovado;
  - Brain Zipper.
- Caminho documental: `areas/zipper/`, `agentes/zipper/`.
- Projetos/rotinas associados:
  - vendas de obras;
  - colecionadores;
  - artistas;
  - feiras;
  - comunicação;
  - logística de obras;
  - style learning.
- Crons relacionados:
  - `Zipper OS vendas 09h WhatsApp/email` — ativo, `local` na evidência viva; entrega externa/script e Telegram apenas exceções quando aplicável.
  - `Zipper Gmail style learning refresh` — ativo, `local`.
- Entra no Fechamento 23h: **sim**.
- Destino de handoff: `areas/zipper/`, relatório diário, pendências globais se houver risco/decisão.
- Gap: confirmar se haverá profile/bot Zipper dedicado ou se continua via Hermes Geral + rotinas.

### 3.6 SPITI OS — SPITI Auction

- Status: **ativo**.
- Runtime/profile conhecido por memória operacional: `/opt/data/profiles/spiti`.
- Bot conhecido: `@SPITI_HermesBot`.
- Caminho documental: `areas/spiti/`, `agentes/spiti/`.
- Projetos/rotinas associados:
  - SPITI Hub;
  - SPITI Financial;
  - Supabase/CRM;
  - leilões/lances;
  - conteúdo/growth;
  - IA de obras;
  - public site futuro.
- Crons relacionados:
  - `SPITI Telegram gateway watchdog` — ativo, `local`.
- Entra no Fechamento 23h: **sim, quando houver atividade/decisão/output/gap**.
- Destino de handoff: `areas/spiti/`, relatório diário, pendências globais se houver risco/decisão.
- Gap: organograma documental deve explicitar melhor o runtime/profile SPITI, não apenas o agente documental.

### 3.7 ZIZ OS

- Status: **desconhecido / previsto**.
- Runtime/profile: não verificado neste inventário inicial.
- Superfícies: a validar.
- Caminho documental: a validar.
- Projetos/rotinas associados: a validar.
- Crons relacionados: nenhum identificado pelo nome no `cronjob list` atual.
- Entra no Fechamento 23h: **sim quando houver profile, projeto, rotina ou conversa ativa**.
- Destino de handoff: a definir.
- Gap: validar existência, escopo e fonte documental antes de dizer que está operacionalmente coberto.

### 3.8 Watchdogs e crons script-only

- Status: **ativos e mistos**.
- Não são agentes conversacionais, mas podem gerar fatos operacionais relevantes.
- Exemplos atuais:
  - `Hermes runtime + cron watchdog no_agent` — ativo, `local`.
  - `Hermes compression failure self-heal watchdog` — ativo, `local`.
  - gateways Mordomo/LK Growth/SPITI — ativos.
  - LK WhatsApp responder — ativo/local.
- Entra no Fechamento 23h: **sim, por exceção/falha/alerta/ação tomada; não por sucesso silencioso normal**.
- Gap: revisar quais watchdogs deveriam ser `local` ou silent-OK para reduzir ruído.

## 4. Resumo dos crons atuais por cobertura

Snapshot vivo do `/opt/hermes/.venv/bin/hermes cron list --all` em 2026-05-29 11:20 UTC: 19 jobs.

- Ativos/scheduled: 19.
- Pausados: 0.
- `last_status` não-ok: 1.
- Erros explícitos de delivery: 0 na listagem atual.
- Jobs ativos sem `Last run` ainda: 0.
- `local` confirmado para a maioria dos watchdogs e rotinas silenciosas.
- `origin` mantido apenas onde a entrega ao Telegram é intencional ou o alerta é parte da rotina executiva.

### Reconciliação Runtime Truth — 2026-05-20 18:00 UTC

Evidência runtime: tentativa de `cronjob list` neste container retornou `command not found`; fallback canônico disponível usado: `/opt/hermes/.venv/bin/hermes cron list --all`.

Relatório de governança: `reports/governance/runtime-truth-reconciler-2026-05-20.md`.

- Total de jobs: 26.
- Ativos: 19.
- Pausados: 7.
- `last_status` não-ok: 0 na listagem atual.
- Erros explícitos de delivery: 0 na listagem atual.
- Jobs ativos sem `Last run` ainda:
  - `Lucas Brain weekly Learning Loop report` (`f4c499e85eac`) — ativo, `origin`, semanal; acompanhar após primeira execução registrada.
  - `Hermes Brain Operating Layer structural watchdog` (`d03fa04e1188`) — ativo, `origin`, novo, sem primeira execução registrada.
  - `Hermes Brain Runtime Truth Reconciler` (`2404c0766d33`) — ativo, `local`, novo, sem primeira execução registrada.
- Job pausado sem `Last run`:
  - `Mordomo: confirmar entrega com Seda Embalagens` (`527ee57b3a6b`) — one-shot pausado/antigo; candidato a limpeza/arquivamento documental futuro.
- Drift reconciliado neste arquivo: seção 4 ainda dizia `24 jobs / 17 ativos / 7 pausados`; snapshot vivo agora é `26 jobs / 19 ativos / 7 pausados`.
- Nenhum schedule, delivery, prompt, script, profile, Docker/gateway, sistema externo ou secret foi alterado.

### Reconciliação Runtime Truth — 2026-05-21 11:20 UTC

Evidência runtime: tentativa de `cronjob list` neste container retornou `command not found`; fallback canônico usado com sucesso: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.

Relatório de governança: `reports/governance/runtime-truth-reconciler-2026-05-21.md`.

- Total de jobs: 28.
- Ativos: 21.
- Pausados: 7.
- `last_status` não-ok: 1 na listagem atual.
- Erros explícitos de delivery: 0 na listagem atual.
- Job ativo com `last_status` não-ok:
  - `Hermes Brain Operating Layer structural watchdog` (`d03fa04e1188`) — último run `error: Script exited with code 1`; saída indicou falta de `memories/daily/2026-05-21.md`.
- Job ativo sem `Last run` ainda:
  - `Lucas Brain weekly Learning Loop report` (`f4c499e85eac`) — ativo, `origin`, semanal.
- Job pausado sem `Last run`:
  - `Mordomo: confirmar entrega com Seda Embalagens` (`527ee57b3a6b`) — one-shot pausado/antigo; candidato a limpeza/arquivamento documental futuro.
- Drift de contagem em relação ao snapshot anterior: `26 jobs / 19 ativos / 7 pausados` → `28 jobs / 21 ativos / 7 pausados`.
- Novos jobs observados na listagem atual que não apareciam no snapshot anterior deste inventário: `LK WhatsApp Hermes responder regression watchdog` (`a5d7a392eed9`) e `Relatório Hermes diário 23h + 02h para Lucas` (`98478b820720`).
- Nenhum schedule, delivery, prompt, script, profile, Docker/gateway, sistema externo ou secret foi alterado.

### Reconciliação Runtime Truth — 2026-05-22 11:20 UTC

Evidência runtime: tentativa de `cronjob list` neste container retornou `command not found`; fallback canônico usado com sucesso: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.

Relatório de governança: `reports/governance/runtime-truth-reconciler-2026-05-22.md`.

- Total de jobs: 29.
- Ativos: 23.
- Pausados: 6.
- `last_status` não-ok: 0 na listagem atual.
- Erros explícitos de delivery: 0 na listagem atual.
- Jobs ativos sem `Last run` ainda:
  - `Lucas Brain weekly Learning Loop report` (`f4c499e85eac`) — ativo, `origin`, semanal; acompanhar após primeira execução registrada.
  - `Lembrete GMC Data Sources 10h` (`1d3a188b24f2`) — ativo, one-shot, `origin`, sem execução registrada na listagem.
- Jobs pausados sem `Last run`:
  - `Mordomo: confirmar entrega com Seda Embalagens` (`527ee57b3a6b`) — one-shot pausado/antigo; candidato a limpeza/arquivamento documental futuro.
  - `LK SEO/CRO impact review — SEO title/meta P1 packets` (`a7e883edd200`) — one-shot pausado sem execução registrada; candidato a reconciliação documental futura.
- Drift de contagem em relação ao snapshot anterior: `28 jobs / 21 ativos / 7 pausados` → `29 jobs / 23 ativos / 6 pausados`.
- Drift de status/documentação observado: `LK GMC Review read-only mandatory delivery` (`d4c26da4cd48`) aparece ativo e `ok` na evidência viva; trechos anteriores do inventário ainda o tratavam como pausado.
- Erro anterior resolvido na evidência viva: `Hermes Brain Operating Layer structural watchdog` (`d03fa04e1188`) aparece com último run `ok`.
- Delivery `origin` em watchdogs silent-OK continua como pendência de revisão de ruído: runtime/cron, compressão self-heal, gateways Mordomo/LK Growth/SPITI, Operating Layer e responder regression.
- Nenhum schedule, delivery, prompt, script, profile, Docker/gateway, VPS, Traefik, container, rede, sistema externo ou secret foi alterado.

### Reconciliação Runtime Truth — 2026-05-23 11:21 UTC

Evidência runtime: tentativa de `cronjob list` neste container retornou `command not found`; fallback canônico usado com sucesso: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.

Relatório de governança: `reports/governance/runtime-truth-reconciler-2026-05-23.md`.

- Total de jobs listados: 23.
- Ativos: 23.
- Pausados/disabled listados: 0.
- `last_status` não-ok: 0 na listagem atual.
- Erros explícitos de delivery: 0 na listagem atual.
- Jobs ativos sem `Last run` ainda:
  - `Lucas Brain weekly Learning Loop report` (`f4c499e85eac`) — ativo, `origin`, semanal; acompanhar após primeira execução registrada.
- Drift de contagem em relação ao snapshot anterior: `29 jobs / 23 ativos / 6 pausados` → `23 jobs / 23 ativos / 0 pausados listados`.
- Jobs pausados antigos citados no inventário anterior não aparecem mais na evidência viva com `--all`; tratar como histórico/arquivado até nova evidência viva.
- `Lembrete GMC Data Sources 10h` (`1d3a188b24f2`), observado como ativo/one-shot sem execução no snapshot de 2026-05-22, não aparece mais na listagem viva atual.
- Delivery `origin` observado sem erro explícito: `LK Daily Sales Brief`, `LK Weekly CEO Review`, `LK GMC Review`, `Mesa COO diária Telegram` e `Lucas Brain weekly Learning Loop report`; manter revisão futura apenas com aprovação de Lucas.
- Drift documental em seções antigas: alguns watchdogs ainda aparecem descritos como `origin`, mas a evidência viva atual mostra `local` para runtime/cron, compressão self-heal, Mordomo, LK Growth e SPITI; esta seção datada é a fonte viva mais recente sem reescrever histórico.
- Nenhum schedule, delivery, prompt, script, profile, Docker/gateway, sistema externo ou secret foi alterado.

### Reconciliação Runtime Truth — 2026-05-24 05:01 UTC

Evidência runtime: helper read-only Hostinger/Docker `hermes_host_docker_observability.py` salvo em `reports/hermes-host-docker-observability-2026-05-24.json` + fallback canônico `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron status/list --all`.

Relatório diário associado: `reports/hermes-continuous-improvement/2026-05-24.md`.

- Total de jobs ativos no cron status/list: 23.
- Pausados/disabled listados: 0.
- `last_status` não-ok: 0 na listagem atual.
- Erros explícitos de delivery: 0 na listagem atual.
- Jobs ativos sem `Last run` ainda:
  - `Lucas Brain weekly Learning Loop report` (`f4c499e85eac`) — ativo, `origin`, semanal; primeira execução esperada em 2026-05-25 12:15 UTC.
- Watchdogs críticos validados com silent-OK por contexto/live checks: runtime+cron, compression self-heal, SPITI gateway, Mordomo gateway, LK Growth gateway, LK WhatsApp responder regression e strict-runtime guard.
- Delivery `origin` observado sem erro explícito: `LK Daily Sales Brief`, `LK Weekly CEO Review`, `LK GMC Review`, `Mesa COO diária Telegram`, `Lucas Brain weekly Learning Loop report` e `Relatório Hermes diário 23h + 02h para Lucas`.
- Delivery `local` confirmado para watchdogs que antes apareciam em seções antigas como `origin`: runtime+cron, compression self-heal, Mordomo gateway, LK Growth gateway e SPITI gateway. Seções antigas permanecem históricas; esta seção datada é a fonte viva mais recente.
- Nenhum schedule, delivery, prompt, script, profile, Docker/gateway, VPS, Traefik, container, rede, sistema externo ou secret foi alterado.

### Reconciliação Runtime Truth — 2026-05-24 11:21 UTC

Evidência runtime: tentativa de `cronjob list` neste container/runtime não encontrou o comando no PATH; fallback canônico usado com sucesso: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.

Relatório de governança: `reports/governance/runtime-truth-reconciler-2026-05-24.md`.

- Total de jobs listados: 23.
- Ativos: 23.
- Pausados/disabled listados: 0.
- `last_status` não-ok: 0 na listagem atual.
- Erros explícitos de delivery: 0 na listagem atual.
- Jobs ativos sem `Last run` ainda:
  - `Lucas Brain weekly Learning Loop report` (`f4c499e85eac`) — ativo, `origin`, semanal; primeira execução esperada em 2026-05-25 12:15 UTC.
- Drift de contagem em relação ao snapshot anterior de 2026-05-24 05:01 UTC: sem mudança (`23 ativos / 0 pausados listados`).
- Seções antigas com watchdogs em `origin` permanecem históricas; evidência viva atual confirma `local` para runtime+cron, compression self-heal, Mordomo gateway, LK Growth gateway, SPITI gateway, Operating Layer, Runtime Truth Reconciler, responder regression e strict-runtime guard.
- Delivery `origin` observado sem erro explícito: `LK Daily Sales Brief`, `LK Weekly CEO Review`, `LK GMC Review`, `Mesa COO diária Telegram`, `Lucas Brain weekly Learning Loop report` e `Relatório Hermes diário 23h + 02h para Lucas`; nenhuma mudança de delivery foi feita.
- Nenhum schedule, delivery, prompt, script, profile, Docker/gateway, VPS, Traefik, container, rede, sistema externo ou secret foi alterado.

### Reconciliação Runtime Truth — 2026-05-25 11:20 UTC

Evidência runtime: tentativa de `cronjob list` neste container/runtime não encontrou o comando no PATH; fallback canônico usado com sucesso: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.

Relatório de governança: `reports/governance/runtime-truth-reconciler-2026-05-25.md`.

- Total de jobs listados: 23.
- Ativos: 23.
- Pausados/disabled listados: 0.
- `last_status` não-ok: 0 na listagem atual.
- Erros explícitos de delivery: 0 na listagem atual.
- Jobs ativos sem `Last run` ainda:
  - `Lucas Brain weekly Learning Loop report` (`f4c499e85eac`) — ativo, `origin`, semanal; próxima execução prevista em 2026-05-25 12:15 UTC.
- Drift de contagem em relação ao snapshot anterior de 2026-05-24 11:21 UTC: sem mudança (`23 ativos / 0 pausados listados`).
- Seções antigas com watchdogs em `origin` permanecem históricas; evidência viva atual confirma `local` para runtime+cron, compression self-heal, Mordomo gateway, LK Growth gateway, SPITI gateway, Operating Layer, Runtime Truth Reconciler, responder regression e strict-runtime guard.
- Delivery `origin` observado sem erro explícito: `LK Daily Sales Brief`, `LK Weekly CEO Review`, `LK GMC Review`, `Mesa COO diária Telegram`, `Lucas Brain weekly Learning Loop report` e `Relatório Hermes diário 23h + 02h para Lucas`; nenhuma mudança de delivery foi feita.
- Nenhum schedule, delivery, prompt, script, profile, Docker/gateway, VPS, Traefik, container, rede, sistema externo ou secret foi alterado.

### Reconciliação Runtime Truth — 2026-05-26 11:21 UTC

Evidência runtime: tentativa de localizar `cronjob list` neste container/runtime não encontrou o comando no PATH; fallback canônico usado com sucesso: `/opt/hermes/.venv/bin/hermes cron list --all` a partir de `/opt/data/hermes_bruno_ingest/hermes-brain`.

Relatório de governança: `reports/governance/runtime-truth-reconciler-2026-05-26.md`.

- Total de jobs listados: 20.
- Ativos: 20.
- Pausados/disabled listados: 0.
- `last_status` não-ok: 0 na listagem atual.
- Erros explícitos de delivery: 0 na listagem atual.
- Jobs ativos sem `Last run` ainda: 0.
- Drift de contagem em relação ao snapshot anterior de 2026-05-25 11:20 UTC: `23 ativos / 0 pausados listados` → `20 ativos / 0 pausados listados`.
- Jobs observados em 2026-05-25 que não aparecem mais na listagem viva atual: `LK GMC Review read-only mandatory delivery`, `LK WhatsApp Hermes responder regression watchdog` e um dos jobs LK/SEO-GMC previamente listados no snapshot de 23 jobs; tratar seções antigas como históricas até nova evidência viva.
- Delivery `origin` observado sem erro explícito: `Mesa COO diária Telegram` e `Relatório Hermes diário 23h + 02h para Lucas`; nenhuma mudança de delivery foi feita.
- Delivery `local` confirmado para LK Daily Sales Brief, LK Weekly CEO Review, todos os watchdogs de gateway listados, Fechamento 23h, Runtime Truth Reconciler e Operating Layer.
- Nenhum schedule, delivery, prompt, script, profile, Docker/gateway, VPS, Traefik, container, rede, sistema externo, campanha, Shopify, GMC, Notion, WhatsApp, email ou secret foi alterado.

### Reconciliação Runtime Truth — 2026-05-27 11:20 UTC

Evidência runtime: tentativa de localizar `cronjob list` neste container/runtime não encontrou o comando no PATH; fallback canônico usado com sucesso: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all` a partir de `/opt/data/hermes_bruno_ingest/hermes-brain`.

Relatório de governança: `reports/governance/runtime-truth-reconciler-2026-05-27.md`.

- Total de jobs listados: 21.
- Ativos: 21.
- Pausados/disabled listados: 0.
- `last_status` não-ok: 0 na listagem atual.
- Erros explícitos de delivery: 0 na listagem atual.
- Jobs ativos sem `Last run` ainda: 0.
- Drift de contagem em relação ao snapshot anterior de 2026-05-26 11:21 UTC: `20 ativos / 0 pausados listados` → `21 ativos / 0 pausados listados`.
- Novo job observado na listagem viva atual: `Hermes multi-profile latency watchdog` — ativo, `origin`, script `hermes_profile_latency_watchdog.py`, último status `ok`; precisa permanecer documentado como alerta/anomalia, não como recibo de sucesso silencioso.
- Delivery `origin` observado sem erro explícito: `Mesa COO diária Telegram`, `Relatório Hermes diário 23h + 02h para Lucas` e `Hermes multi-profile latency watchdog`; nenhuma mudança de delivery foi feita.
- Delivery `local` confirmado para LK Daily Sales Brief, LK Weekly CEO Review, todos os watchdogs de gateway listados, Fechamento 23h, Runtime Truth Reconciler, Operating Layer e strict-runtime guard.
- Nenhum schedule, delivery, prompt, script, profile, Docker/gateway, VPS, Traefik, container, rede, sistema externo, campanha, Shopify, GMC, Notion, WhatsApp, email ou secret foi alterado.

### Reconciliação Runtime Truth — 2026-05-28 11:20 UTC

Evidência runtime: tentativa de `cronjob list` neste container/runtime não encontrou o comando no PATH; fallback canônico usado com sucesso: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all` a partir de `/opt/data/hermes_bruno_ingest/hermes-brain`.

Relatório de governança: `reports/governance/runtime-truth-reconciler-2026-05-28.md`.

- Total de jobs listados: 21.
- Ativos: 21.
- Pausados/disabled listados: 0.
- `last_status` não-ok: 1 na listagem atual.
- Erros explícitos de delivery: 0 na listagem atual.
- Jobs ativos sem `Last run` ainda: 0.
- Drift de contagem em relação ao snapshot anterior de 2026-05-27 11:20 UTC: sem mudança (`21 ativos / 0 pausados listados`).
- Job ativo com `last_status` não-ok: `Hermes Brain Operating Layer structural watchdog` — ativo, `local`, script `brain_operating_layer_audit.py`; último run retornou `error: Script exited with code 1` após auto-heal criar `memories/daily/2026-05-28.md` e ainda detectar `memories/hot.md stale >3 days`.
- Delivery `origin` observado sem erro explícito: `Mesa COO diária Telegram`, `Relatório Hermes diário 23h + 02h para Lucas` e `Hermes multi-profile latency watchdog`; nenhuma mudança de delivery foi feita.
- Delivery `local` confirmado para LK Daily Sales Brief, LK Weekly CEO Review, todos os watchdogs de gateway listados, Fechamento 23h, Runtime Truth Reconciler, Operating Layer, strict-runtime guard e relatórios script-only listados.
- Drift documental a reconciliar sem reescrever histórico: seções antigas ainda mencionam alguns watchdogs/relatórios como `origin`, mas a evidência viva de 2026-05-28 confirma `local` para esses jobs; considerar limpeza documental em rodada própria se necessário.
- Nenhum schedule, delivery, prompt, script, profile, Docker/gateway, VPS, Traefik, container, rede, sistema externo, campanha, Shopify, GMC, Notion, WhatsApp, email ou secret foi alterado.

### Reconciliação Runtime Truth — 2026-05-29 11:20 UTC

Evidência runtime: comando solicitado `cronjob list` indisponível neste runtime (`command not found`); fallback canônico usado com sucesso: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all` a partir de `/opt/data/hermes_bruno_ingest/hermes-brain`.

Relatório de governança: `reports/governance/runtime-truth-reconciler-2026-05-29.md`.

- Total de jobs listados: 19.
- Ativos: 19.
- Pausados/disabled listados: 0.
- `last_status` não-ok: 1.
- Erros explícitos de delivery: 0.
- Jobs ativos sem `Last run` ainda: 0.
- Drift de contagem em relação ao snapshot anterior de 2026-05-28 11:20 UTC: `21 ativos / 0 pausados` → `19 ativos / 0 pausados`.
- Job ativo com `last_status` não-ok:
  - `LK Weekly Collection Sort Rule B` (`787134d4ac5c`) — ativo, `local`, script `lk_weekly_collection_sort_ruleB.sh`; último run retornou `error: Script timed out after 120s: /opt/data/scripts/lk_weekly_collection_sort_ruleB.sh`.
- Jobs ativos com `deliver=origin` que merecem reconciliação documental porque são recados/alertas e não sucesso silencioso:
  - `Mesa COO diária Telegram` (`749ee30b51eb`) — origin, ok.
  - `Relatório Hermes diário 23h + 02h para Lucas` (`98478b820720`) — origin, ok.
  - `Hermes multi-profile latency watchdog` (`c1ce34b4449a`) — origin, ok.
- Jobs/itens históricos removidos da evidência viva em relação ao snapshot anterior:
  - `Hermes Brain Operating Layer structural watchdog` não aparece mais na listagem atual.
  - `Hermes Brain strict-runtime guard watchdog` não aparece mais na listagem atual.
  - `Hermes Brain Runtime Truth Reconciler` não aparece mais na listagem atual.
- A listagem viva atual confirma `local` para os watchdogs/gateways/relatórios restantes, incluindo LK Daily Sales Brief, LK Weekly CEO Review, Zipper Gmail style learning refresh, Hermes compression failure self-heal watchdog, LK Pulso Comercial 16h, LK 09h previous-day sales report, LK 19h30 physical store close, Mordomo gateway, Zipper vendas, LK Growth gateway, SPITI gateway, Fechamento Ágil 23h + Brain Sync e Lucas Brain weekly Learning Loop report.
- Nenhum schedule, delivery, prompt, script, profile, Docker/gateway, VPS, Traefik, container, rede, sistema externo, campanha, Shopify, GMC, Notion, WhatsApp, email ou secret foi alterado.

## 5. Regras de delivery para Fechamento 23h

- Fechamento 23h: `local` por padrão.
- Telegram/origin: somente decisão, exceção, falha, risco crítico ou pedido explícito de Lucas.
- Relatórios LK com entrega externa aprovada: sucesso normal deve ficar em receipt/Brain/local, não necessariamente no Telegram.
- HTML/artefatos: não enviar no Telegram salvo pedido de revisão visual/arquivo.

## 6. Gaps para resolver antes do cron recorrente

1. Confirmar e documentar a cobertura real de ZIZ OS.
2. Decidir se Mordomo ganha `agentes/mordomo/` ou `areas/lucas-pessoal/` como pasta documental própria.
3. Atualizar organograma para explicitar SPITI runtime/profile.
4. Revisar entrega `origin` de watchdogs que só deveriam alertar exceção.
5. Decidir se SEO/CRO/LK Growth crons pausados devem continuar no Hermes Geral, migrar para profile LK Growth ou permanecer pausados.
6. Garantir que Mesa COO consuma `reports/daily-consolidation/YYYY-MM-DD.md` quando o cron 23h for ativado.

## 7. Status Fase 1A

- Inventário vivo criado: **sim**.
- Teste manual do Fechamento 23h: **concluído** em `reports/daily-consolidation/2026-05-19.md`.
- Rotina canônica criada: **sim**, `areas/operacoes/rotinas/fechamento-agil-23h.md`.
- Cron recorrente 23h criado: **sim**, delivery `local`, schedule UTC `0 2 * * *`.
