# Receipt — Cron noise reduction Bloco 1

Data: 2026-05-25T11:27:55.349439+00:00

## Alterações executadas

- `7c688553e293` — LK Daily Sales Brief read-only mandatory delivery — deliver `origin` → `local`
- `953b9055458e` — LK Weekly CEO Review read-only mandatory delivery — deliver `origin` → `local`
- `d4c26da4cd48` — LK GMC Review read-only mandatory delivery — deliver `origin` → `local`
- `f4c499e85eac` — Lucas Brain weekly Learning Loop report — deliver `origin` → `local`
- `98478b820720` — Relatório Hermes diário 23h + 02h para Lucas — deliver `origin` → `local`

## Backup / rollback

- Backup: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/cron-registry-backups/2026-05-25-block1-noise-reduction/main-jobs.before.json`
- SHA antes: `b8c9a7df82e43f243d32009e1046d38727d28f2e08d27e9d7119479fc34c4979`
- SHA depois: `2ba6df92c12cef67dcae814d56aacb170e1147cc8663d73c4c5361c1be51aee7`
- Rollback: copiar o backup para `/opt/data/cron/jobs.json`.

## Guardrails preservados

- Mesa COO não foi alterada.
- Registries de LK Growth, Mordomo e SPITI não foram alterados.
- Nenhum gateway/Docker/VPS foi reiniciado.
- Nenhuma integração externa foi tocada.
