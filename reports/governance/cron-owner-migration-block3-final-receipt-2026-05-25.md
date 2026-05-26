# Final receipt — Cron owner migration Bloco 3

Data: 2026-05-25

## Resultado

Bloco 3 executado: 3 jobs foram migrados do Main/Hermes Geral para os profiles especialistas corretos.

## Migrados

- `d4c26da4cd48` — LK GMC Review read-only mandatory delivery — `main` → `lk-growth`
- `71b2636add5d` — LK WhatsApp Hermes responder watchdog — `main` → `mordomo`
- `a5d7a392eed9` — LK WhatsApp Hermes responder regression watchdog — `main` → `mordomo`

## Compatibilidade de scripts

Como os jobs usam `script` relativo ao profile, copiei os wrappers/scripts para os profiles destino:

- `/opt/data/profiles/lk-growth/scripts/lk_gmc_review_watchdog.py`
- `/opt/data/profiles/mordomo/scripts/lk_hermes_whatsapp_watchdog.sh`
- `/opt/data/profiles/mordomo/scripts/lk_hermes_whatsapp_responder_selftest.sh`

Os scripts preservam os paths absolutos originais para os runners em `/opt/data/scripts/`, mantendo comportamento funcional.

## Correção durante verificação

A primeira escrita copiou os jobs para os profiles destino, mas a verificação detectou que os 3 IDs ainda estavam presentes no Main. Corrigi imediatamente removendo esses IDs do Main e salvei receipt separado:

- `reports/governance/cron-owner-migration-block3-duplicate-fix-receipt-2026-05-25.json`

## Estado final verificado

- Main: total=20; ativos=20; pausados=0; nenhum dos 3 IDs migrados permanece no Main.
- LK Growth: total=23; ativos=23; pausados=0; contém `d4c26da4cd48`.
- Mordomo: total=13; ativos=13; pausados=0; contém `71b2636add5d` e `a5d7a392eed9`.

## Backups / rollback

Backups iniciais do bloco:

- `reports/governance/cron-registry-backups/2026-05-25-block3-owner-migration/main-jobs.before.json`
- `reports/governance/cron-registry-backups/2026-05-25-block3-owner-migration/lk-growth-jobs.before.json`
- `reports/governance/cron-registry-backups/2026-05-25-block3-owner-migration/mordomo-jobs.before.json`

Backup da correção de duplicidade no Main:

- `reports/governance/cron-registry-backups/2026-05-25-block3-owner-migration-fix-main-duplicate/main-jobs.before-fix.json`

Rollback: restaurar os `*.before.json` correspondentes para cada registry.

## Guardrails preservados

- Nenhum gateway/Docker/VPS foi reiniciado.
- Nenhuma integração externa foi tocada.
- Schedules, prompts e `deliver` dos jobs migrados foram preservados.
- Guard strict-runtime final: 0 falhas.
- Varredura de credenciais dos receipts: OK.
