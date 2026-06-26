# Audit — Brain Sync e Hermes Brain

Data UTC: 2026-06-26T10:56Z–11:00Z

## Veredito

Estado geral: **parcialmente correto, com 2 erros/pendências reais ainda abertas**.

O incidente principal do Brain Sync foi corrigido: o checkout operacional está em `main`, `origin/main` e GitHub `main` estão alinhados, e o Brain Sync canônico não está mais apontando para o branch antigo.

Ainda existem problemas:

1. **Strict-runtime guard não está verde**: após restaurar o guard que ficou ausente na troca de checkout, ele encontrou 119 achados de padrões legados/perigosos em docs/scripts históricos.
2. **Há mudanças locais pós-sync não versionadas ainda**: 1 arquivo allowlisted (`areas/operacoes/crm/mordomo-crm-local-status.md`) e 20 arquivos locais não allowlisted de Memory OS/backup.

## Evidência — Brain Sync / Git

- Repo operacional: `/opt/data/hermes_bruno_ingest/hermes-brain`
- Branch operacional: `main`
- Local HEAD: `28825a9fbcdfef562f3bcf2c96d92b2d82b5799a`
- `origin/main`: `28825a9fbcdfef562f3bcf2c96d92b2d82b5799a`
- GitHub `main`: `28825a9fbcdfef562f3bcf2c96d92b2d82b5799a`
- Ahead/behind local vs origin: `0/0`
- Remote: `https://github.com/lk-snkrs/hermes-brain.git`
- Branch guard no script: presente (`--target-branch` e `--allow-noncanonical-branch`).

## Brain Sync dry-run atual

`brain_sync_safe.py --dry-run --verbose` retornou:

- branch: `main`
- allowed files: `1`
- skipped files: `20`

Arquivo allowlisted pendente:

- `areas/operacoes/crm/mordomo-crm-local-status.md`

Arquivos skipped principais:

- `reports/memory-hygiene/*.json`
- `reports/memory-hygiene/*.jsonl`
- `reports/governance/memory-backups/*before-memory-os-v120-generator-contract`

Interpretação: isso **não indica quebra do Brain Sync**; indica que houve nova escrita local depois do último sync. O próximo sync canônico pode versionar o arquivo allowlisted. Os arquivos Memory OS estão fora da allowlist por design.

## Cron vivo

Cron `Hermes Brain Fechamento Ágil 01h + Brain Sync`:

- ID: `3fc45b0830c6`
- Enabled: `true`
- Schedule: `0 4 * * *`
- Delivery: `local`
- Last status: `ok`
- Last run: `2026-06-26T04:08:30Z`
- Next run: `2026-06-27T04:00:00Z`
- Workdir: `/opt/data/hermes_bruno_ingest/hermes-brain`

## Brain Health

Antes da correção local durante este audit, `scripts/brain_health_check.py` falhava com 48 falsos positivos `openai` causados por strings como `task-router-hermes.md` contendo substring `sk-...`.

Correção local aplicada:

- regex `openai` ajustado para exigir boundary antes de `sk-`, igual ao padrão já usado no Brain Sync.

Resultado após correção:

- `brain_health_check.py`: `All checks passed`
- JSON: `fail_count=0`, `warn_count=0`

Nota: essa correção está local no checkout operacional e ainda precisa ser versionada em fluxo apropriado, pois scripts são fora da allowlist automática do Brain Sync.

## Strict-runtime guard

Erro encontrado: o watchdog `Hermes Brain strict-runtime guard watchdog` tinha `last_status=error` no cron vivo. A causa imediata era ausência de:

```text
scripts/operational_docs_guard.py
```

Esse arquivo existia no backup pré-switch e foi restaurado localmente para o checkout operacional.

Após restaurar, o script roda, mas encontrou:

- `119` issues
- `6845` arquivos escaneados

Principais clusters:

- `brain_sync.sh`: 15
- `skills/brain-sync/SKILL.md`: 9
- `alert_system.py`: 8
- `sync_hermes.sh`: 7
- `scripts/brain_sync.sh`: 6
- `skills/session-start-protocol/SKILL.md`: 5
- `hermes_remediate.sh`: 4
- `scripts/session_end_summary.py`: 4
- `scripts/git-accountability.sh`: 4
- `monitor_daemon.py`: 3

Interpretação: **isso é erro real de saneamento operacional**, não quebra do sync. O guard está detectando material legado com `/root`, `sshpass`, `Mem0`, mutações Docker/host etc. sem marcação suficiente de `DEPRECATED/DO NOT RUN` ou sem quarentena clara.

## Memory OS / untracked

`reports/memory-hygiene/latest.json` mostra estado OK:

- status recente OK
- template coverage sem missing
- profile memories sem over-limit/near-saturation crítico no trecho auditado

`cycle-maturity-latest.md`:

- Status: `ok`
- Maturidade: `mature`
- Score: `100`
- Findings acionáveis: nenhum

Os 13 JSONs untracked em `reports/memory-hygiene/` parseiam corretamente. Secret scan focado nos 20 untracked retornou `secret_literal_hits=0`.

## Correções locais aplicadas durante o audit

1. Restaurado `scripts/operational_docs_guard.py` a partir do backup:
   - `/opt/data/hermes_bruno_ingest/hermes-brain.backup-pre-main-switch-20260626T102451Z`
2. Corrigido falso positivo no `scripts/brain_health_check.py` para não tratar `task-router-*` como token `sk-*`.
3. Verificado:
   - `py_compile` OK nos dois scripts;
   - Brain health atual PASS;
   - secret scan focado dos scripts: `secret_literal_hits=0`.

Backups das alterações locais:

```text
/opt/data/backups/brain-audit-fixes-20260626T105804Z/
```

## O que não foi alterado

- Nenhum cron schedule/delivery/prompt foi modificado.
- Nenhum Docker/VPS/Traefik/runtime foi alterado.
- Nenhum Shopify/Tiny/sistema externo foi alterado.
- Nenhum secret foi impresso.
- Nenhum push GitHub foi feito durante este audit.

## Pendências recomendadas

P0/P1:

1. **Strict-runtime guard cleanup**: marcar/quarentenar arquivos legados detectados para levar o strict guard a silent-OK.
2. **Versionar correções de scripts** (`brain_health_check.py` e `operational_docs_guard.py`) via PR/fluxo seguro, porque scripts não entram no Brain Sync automático.
3. **Deixar o próximo Brain Sync ou um sync manual escopado versionar** o arquivo allowlisted pendente `areas/operacoes/crm/mordomo-crm-local-status.md` e este report.

P2:

4. Avaliar se `reports/memory-hygiene/` deve ter uma síntese `.md` allowlisted ou permanecer local-only.
5. Depois de janela de validação, remover ou arquivar o backup pré-switch do Brain operacional.
