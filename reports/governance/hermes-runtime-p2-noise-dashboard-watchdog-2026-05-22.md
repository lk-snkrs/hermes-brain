# Hermes Runtime P2 — noise, dashboard, watchdog — 2026-05-22

## Veredito

Pacote P2 executado com foco em menos ruído, mais painel e mais detecção preventiva. Não houve Docker/VPS/gateway restart, nem mutação externa em GMC/Shopify/WhatsApp/email/bancos.

## Mudanças executadas

1. Dashboard único de saúde Hermes criado:
   - `areas/operacoes/runtime/hermes-health-dashboard.md`

2. Strict-runtime guard virou watchdog silent-OK:
   - Script local: `/opt/data/scripts/hermes_brain_strict_runtime_guard_watchdog.py`
   - Cron: `d9badcd83411` — Hermes Brain strict-runtime guard watchdog
   - Schedule: `0 10 * * *` UTC / 07h BRT
   - Delivery: `local`
   - no_agent: `true`
   - Contrato: stdout vazio em OK; stdout apenas em achados/erro de execução.

3. Redução de ruído Telegram:
   - Job `98478b820720` — Relatório Hermes diário 23h + 02h para Lucas — movido de `origin` para `local`.
   - Mesa COO (`749ee30b51eb`) permanece como fila executiva principal no Telegram.
   - Rollback: `cronjob update 98478b820720 deliver=origin`.

4. Control plane e mapa atualizados:
   - `areas/operacoes/rotinas/cron-control-plane.md`
   - `areas/operacoes/intelligence-map.md`

5. Skills audit executado:
   - Relatório: `reports/governance/hermes-skills-legacy-safety-audit-2026-05-22.md`
   - Arquivos de skill/references escaneados: `1361`
   - Findings restantes após patches/contextualização: `0`
   - Patches aplicados em referências com `/root` histórico para marcar isolated-spike/bootstrap e evitar uso como produção.

## Estado cron pós-P2

- Total live: `23` jobs.
- Scheduled/ativos: `23`.
- Pausados: `0`.
- Novo job: `d9badcd83411`.
- Delivery alterado: `98478b820720` de `origin` para `local`.

## Evidência de verificação

### Brain health

```text
secrets: FAIL=0 WARN=0
links: FAIL=0 WARN=0
required_files: FAIL=0 WARN=0
agent_files: FAIL=0 WARN=0
area_maps: FAIL=0 WARN=0
decisions_index: FAIL=0 WARN=0
routines_index: FAIL=0 WARN=0
skill_references: FAIL=0 WARN=0

All checks passed.
```

### Operational docs guard — default

- scanned: `181`
- fail: `0`

### Operational docs guard — strict-runtime

- scanned: `1062`
- fail: `0`

### Strict-runtime watchdog manual check

- command: `/opt/data/scripts/hermes_brain_strict_runtime_guard_watchdog.py`
- rc: `0`
- stdout length: `0` — silent OK confirmado.

### Brain Sync safe dry-run

- branch: `consolidation/brain-filesystem-git-hygiene-20260516`
- allowed files: `81`
- skipped files: `306`
- live push/sync externo: **não executado**.

## O que não foi tocado

- Docker/VPS/containers/volumes/redes/Traefik.
- Gateway restart.
- GMC/Content API writes.
- Shopify/Tiny/Crisp/WhatsApp/email writes.
- Secrets impressos em logs ou docs.

## Próximo ponto de atenção

Observar por 2–3 dias se a Mesa COO absorve bem o conteúdo que antes vinha no Telegram 02h30. Se faltar contexto, a opção segura é fundir melhor o prompt da Mesa antes de restaurar ruído no Telegram.
