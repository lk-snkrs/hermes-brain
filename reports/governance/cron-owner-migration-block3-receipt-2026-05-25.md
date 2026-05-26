# Receipt — Cron owner migration Bloco 3

Data: 2026-05-25T11:33:21.442090+00:00

## Migrados

- `d4c26da4cd48` — LK GMC Review read-only mandatory delivery — `main` → `lk-growth` — script `lk_gmc_review_watchdog.py`
- `71b2636add5d` — LK WhatsApp Hermes responder watchdog — `main` → `mordomo` — script `lk_hermes_whatsapp_watchdog.sh`
- `a5d7a392eed9` — LK WhatsApp Hermes responder regression watchdog — `main` → `mordomo` — script `lk_hermes_whatsapp_responder_selftest.sh`

## Scripts copiados para manter compatibilidade do profile

- `/opt/data/profiles/lk-growth/scripts/lk_gmc_review_watchdog.py`
- `/opt/data/profiles/mordomo/scripts/lk_hermes_whatsapp_watchdog.sh`
- `/opt/data/profiles/mordomo/scripts/lk_hermes_whatsapp_responder_selftest.sh`

## Totais após migração

- main: total=23; ativos=23; pausados=0; targets_present=['d4c26da4cd48', '71b2636add5d', 'a5d7a392eed9']
- lk-growth: total=23; ativos=23; pausados=0; targets_present=['d4c26da4cd48']
- mordomo: total=13; ativos=13; pausados=0; targets_present=['71b2636add5d', 'a5d7a392eed9']

## Backups / rollback

- main: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/cron-registry-backups/2026-05-25-block3-owner-migration/main-jobs.before.json` → registry `/opt/data/cron/jobs.json`
- lk-growth: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/cron-registry-backups/2026-05-25-block3-owner-migration/lk-growth-jobs.before.json` → registry `/opt/data/profiles/lk-growth/cron/jobs.json`
- mordomo: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/cron-registry-backups/2026-05-25-block3-owner-migration/mordomo-jobs.before.json` → registry `/opt/data/profiles/mordomo/cron/jobs.json`

## Guardrails preservados

- Nenhum gateway/Docker/VPS foi reiniciado.
- Nenhuma integração externa foi tocada.
- Schedules/prompts/deliver dos jobs migrados foram preservados.
- Main perdeu apenas os 3 jobs migrados; destinos receberam exatamente esses IDs.
