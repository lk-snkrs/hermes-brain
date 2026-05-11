# Hermes Ops — watchdogs no_agent e release watch

Data/hora da coleta: 2026-05-11T00:01–00:08 UTC
Escopo: read-only. Nenhum container, cron, compose, gateway, secret, Docker, Traefik, SSH/root, firewall, banco ou envio externo foi alterado.

## Veredito curto

OK operacional para os checks principais:
- Runtime está em Docker (`/.dockerenv` presente; PID 1 `tini`).
- Hermes ativo esperado: `Hermes Agent v0.13.0 (2026.5.7)` via `/opt/hermes/.venv/bin/hermes --version`.
- Gateway visível: 1 processo `hermes gateway run` (`/opt/hermes/.venv/bin/python3 /opt/hermes/.venv/bin/hermes gateway run`).
- `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron status`: gateway running, 4 jobs ativos, próximo run 2026-05-11T00:30:00Z.
- Watchdog `edd06fe19397` rodou OK em 2026-05-11T00:00:41Z; próxima execução 00:30Z.
- Watchdog freshness `e7a61e275c37` rodou OK em 2026-05-10T23:14:38Z; próxima execução 12:00Z.
- Os dois scripts no `/opt/data/scripts/` obedeceram ao contrato `no_agent`: `rc=0`, stdout vazio e stderr vazio em modo normal.

## Cron jobs observados

- `c214051f7780` — LK weekly influencer sales email — ativo — `0 13 * * 3` — próxima 2026-05-13T13:00:00Z.
- `f5a23dd6a1bd` — Hermes/LK daily continuous improvement scan — ativo — `0 5 * * *` — próxima 2026-05-11T05:00:00Z — skills: hermes-agent, lucas-hermes-continuous-improvement, multiempresa-routing-lucas, lucas-chief-of-staff.
- `edd06fe19397` — Hermes runtime + cron watchdog no_agent — ativo — `*/30 * * * *` — script `hermes_runtime_cron_watchdog.py` — `no_agent` — último run OK.
- `e7a61e275c37` — Hermes v0.13 artifacts freshness watchdog no_agent — ativo — `0 12 * * *` — script `hermes_artifacts_freshness_watchdog.py` — `no_agent` — último run OK.

## Evidência dos scripts

`python3 /opt/data/scripts/hermes_runtime_cron_watchdog.py`:
- rc=0
- stdout_bytes=0
- stderr_bytes=0

`python3 /opt/data/scripts/hermes_runtime_cron_watchdog.py --verbose`:
- versão: `Hermes Agent v0.13.0 (2026.5.7)`
- config observada no contexto do worker: `/opt/data/profiles/hermes-ops-readonly/config.yaml`, `backend_local=True`, `cwd=/opt/data`
- config de produção também validada separadamente: `/opt/data/config.yaml`, `backend_local=True`, `cwd=/opt/data`, `approvals.mode=off`
- gateway_process_count=1
- jobs_path=/opt/data/cron/jobs.json, jobs_count=4
- target_job `f5a23dd6a1bd` enabled=True, state=scheduled, next=2026-05-11T05:00:00Z

`python3 /opt/data/scripts/hermes_artifacts_freshness_watchdog.py`:
- rc=0
- stdout_bytes=0
- stderr_bytes=0

`python3 /opt/data/scripts/hermes_artifacts_freshness_watchdog.py --verbose`:
- latest_weekly_report: `/opt/data/lk_weekly_influencer_sales_reports/lk-weekly-influencer-sales-2026-05-09.json`
- latest_weekly_report_age_days=0
- kanban_counts: done=2, ready=5, running=1
- required_cron_jobs: `edd06fe19397`, `f5a23dd6a1bd`

## Integridade dos artefatos

Checksums confirmaram que as cópias executáveis e as cópias fonte no Hermes Brain estão sincronizadas:
- `hermes_runtime_cron_watchdog.py`: `be8902a2dc35a707988a11350c92cb2151c2c33012474c2094f06212a4970479`
- `hermes_artifacts_freshness_watchdog.py`: `3cc0092d1e6a6558b51a5f0d3f26e6d66dbeb7fd58e239b805b4b1d1a2d94fa9`

Permissões dos executáveis:
- `/opt/data/scripts/hermes_runtime_cron_watchdog.py`: mode 755, size 10243
- `/opt/data/scripts/hermes_artifacts_freshness_watchdog.py`: mode 755, size 4327

Docs Brain conferidos:
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/rotinas/hermes-v013-watchdogs-no-agent.md`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/rotinas/hermes-v013-operacionalizacao.md`
- `/opt/data/hermes_bruno_ingest/hermes-brain/reports/hermes-release-catchup-2026-05-10/action-matrix.md`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/rotinas/hermes-release-watch.md`

## Drift/risco encontrado

1. `hermes` não está no PATH do worker (`command not found`). O runtime correto existe em `/opt/hermes/.venv/bin/hermes`. Isso não quebra o cron quando o scheduler usa o runtime/ambiente certo, mas scripts/manuais devem continuar chamando o binário absoluto ou setar PATH explicitamente.

2. O doc `hermes-release-watch.md` ainda menciona um one-shot `Hermes release watch post-check` (`1f60e374d0ba`) agendado para 2026-05-11T09:15Z. Esse job não aparece no `jobs.json` atual. Pode ser drift de documentação pós-migração para o cron diário `f5a23dd6a1bd`, ou perda do one-shot. Correção exige decisão: atualizar doc/cron com plano; não alterei nada.

3. O `f5a23dd6a1bd` ainda não tem `last_run_at` porque a próxima primeira execução observável é 2026-05-11T05:00Z. Isso é esperado neste horário, mas deve ser rechecado depois de 05:00Z/02:00 BRT.

4. O `hermes_runtime_cron_watchdog.py --verbose` sob este worker usa `HERMES_HOME` do perfil (`/opt/data/profiles/hermes-ops-readonly`), não `/opt/data`. Validei `/opt/data/config.yaml` separadamente. Para reproduções manuais fiéis ao cron, preferir `HERMES_HOME=/opt/data python3 /opt/data/scripts/hermes_runtime_cron_watchdog.py --verbose`.

5. Logs recentes do gateway mostram apenas um evento de rede Telegram em 2026-05-10 19:42 UTC com retomada automática no attempt 1; sem traceback/erro crítico recente nos últimos 300 registros inspecionados com filtro redigido.

## Recomendações seguras

- Depois de 2026-05-11T05:00Z, revalidar `f5a23dd6a1bd.last_run_at` e `last_status` em modo read-only. Mitigação criada após o relatório: cron one-shot `635d6bceab80`, `no_agent=True`, script `/opt/data/scripts/hermes_daily_ci_recheck_after_first_run.py`, agendado para 2026-05-11T05:30Z; fica silencioso se saudável e alerta apenas se o job diário não tiver rodado/estiver ruim.
- Decidir se o post-check `1f60e374d0ba` deve existir ou se o doc deve ser atualizado para apontar somente para `f5a23dd6a1bd` como release watch diário. Qualquer alteração em cron real deve ter plano + rollback + aprovação.
- Não reiniciar gateway/Docker nem alterar compose/imagem/cron nesta etapa; não há alerta crítico que justifique ação emergencial.
