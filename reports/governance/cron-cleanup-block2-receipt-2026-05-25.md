# Receipt — Cron cleanup Bloco 2

Data: 2026-05-25T11:31:22.755795+00:00

## Removidos

- `lk-growth` `350be0e438c7` — LK cart intent phase 2 — monitor 90min
- `lk-growth` `015cb75e8e91` — LK cart intent v2.2 cache/event monitor
- `lk-growth` `36694eae598e` — LK Recovery OS production tracker propagation monitor
- `lk-growth` `fdc9ad165daa` — LK Recovery OS cart intent controlled LIVE runner
- `mordomo` `058df00bf941` — Mordomo A2 executor scaffold

## Backups / rollback

- lk-growth: backup `/opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/cron-registry-backups/2026-05-25-block2-paused-oneshot-cleanup/lk-growth-jobs.before.json`; registry `/opt/data/profiles/lk-growth/cron/jobs.json`; removidos=4; restantes=22
- mordomo: backup `/opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/cron-registry-backups/2026-05-25-block2-paused-oneshot-cleanup/mordomo-jobs.before.json`; registry `/opt/data/profiles/mordomo/cron/jobs.json`; removidos=1; restantes=11

Rollback: copiar o respectivo `*.before.json` de volta para o registry do profile.

## Guardrails preservados

- Main registry não foi alterado neste bloco.
- SPITI registry não foi alterado/criado.
- Nenhum gateway/Docker/VPS foi reiniciado.
- Nenhuma integração externa foi tocada.
