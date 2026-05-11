# LK Shopify read-only skill operationalization — 2026-05-11

Session learning from Lucas/Hermes Brain v0.13 operationalization.

## What mattered

Lucas asked whether the new Shopify skill was actually “100%”. The useful standard became stricter than “the SKILL.md exists”: a business/integration skill is not complete until it is installed where Hermes can load it, mirrored/versioned in Hermes Brain when relevant, indexed in Brain navigation, scanned for secrets, health-checked, and merged/synced.

## Completion standard before saying “100%”

For `lk-shopify-readonly` and similar integration/business skills, verify all of the following:

- Local runtime skill exists under `/opt/data/skills/productivity/<skill>/SKILL.md` and can be loaded with `skill_view`.
- Hermes Brain copy exists under `skills/<skill>/SKILL.md` when the Brain is the durable source of truth for the process.
- Navigation/index files point to it, especially `empresa/skills/_index.md` and the relevant area MAPAs (for LK Shopify: `areas/lk/MAPA.md` and `areas/lk/sub-areas/ecommerce/MAPA.md`).
- Guardrails are explicit: Doppler-only secrets, read-only Shopify GET/query, Tiny as stock truth, no external sends or Shopify writes without Lucas approval.
- `scripts/brain_health_check.py` returns `FAIL=0` and preferably `WARN=0` for the Brain change.
- Changed-file or whole-repo secret scan reports `possible_secrets 0`; include Shopify `shpat_`, Doppler `dp.*`, GitHub PAT, Supabase, OpenAI, Telegram and similar patterns.
- PR workflow is complete for Brain changes: branch rebased, PR opened, mergeability clean, squash-merged if low-risk docs-only, and local clone reset/synced to `origin/main`.
- If cron/watchdog state was part of the delivery, verify `cronjob list` after merge and report only job health/status, not secrets.

## Observed safe result

The v0.13 round ended with:

- Brain PR `#54` merged.
- Brain health check clean (`FAIL=0`, `WARN=0`).
- Secret scan clean (`possible_secrets 0`).
- Local Hermes Brain synced to merged `origin/main`.
- Runtime/freshness watchdog cronjobs active and last status OK.

## Response pattern Lucas preferred

When asked “está 100%?”, answer with a direct verdict and evidence bullets:

- `Fase concluída.` / `Sim, fechado.`
- What was installed/indexed/versioned.
- What was verified.
- What was explicitly not touched (Shopify writes, DB, Docker/VPS, campaigns, external sends).
- Next safe block.

Avoid vague status language or saying a skill is complete without checking the files/indexes/health/secret scan/PR state.
