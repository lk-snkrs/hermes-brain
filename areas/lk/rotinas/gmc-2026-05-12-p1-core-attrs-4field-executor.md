# LK GMC P1 Core Attrs 4-Field Executor Dry-Run, 2026-05-12

Status: `gmc_p1_core_attrs_4field_executor_apply_finished_or_stopped`

## Escopo
- Exact online Merchant product IDs only.
- Campos alvo: `title`, `link`, `imageLink`, `price`.
- Campo excluído: `availability`.
- Motivo da exclusão: Tiny continua sendo verdade de estoque da LK.

## Resumo executivo
- Modo: `apply`
- Candidatos de entrada: 1627
- Prontos para apply futuro: 1627
- Bloqueados/skipped: 0
- Writes executados neste dry-run: ver execution_results

## Risco técnico antes do apply
- Como `availability` continua fora do escopo, a Content API pode rejeitar um `products.update` direto ou manter o diagnóstico parcialmente aberto. O executor é fail-fast e cria rollback antes de qualquer write em `--apply`.

## Não executado no dry-run
- Ver JSON para execution_results; rollback privado foi criado antes dos writes.

## Arquivos
- JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-p1-core-attrs-4field-executor.json`
- CSV: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-p1-core-attrs-4field-executor.csv`
- Rollback privado: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-12-p1-core-attrs-4field-executor-rollback-20260512T184539Z.json`
