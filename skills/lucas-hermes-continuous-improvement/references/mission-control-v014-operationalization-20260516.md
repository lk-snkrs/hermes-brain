# Mission Control v0.14 Operationalization (2026-05-16)

Use this reference when Lucas asks to "corrigir o que deve ser corrigido", expand Hermes autonomy, or adopt Hermes v0.12-v0.14 habits into the Lucas OS.

## Core correction

- Mission Control already exists and is the operating surface. Implement new rituals there first; do not create a detached cockpit or parallel dashboard unless explicitly requested.
- Verify skills before planning. Shopify is not a TODO from scratch: `lk-shopify-readonly` and `lk-shopify-product-upload` already exist in runtime and should be mirrored into the Brain when drift is found.

## Current implementation

- Mission Control production URL: `https://mission.lucascimino.com`.
- Mission Control local repo: `/opt/data/hermes_bruno_ingest/mission-control-cimino-hermes`.
- Brain operational doc: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/rotinas/mission-control-v014-operationalization-2026-05-16.md`.
- Runtime watchdog: `/opt/data/scripts/mission_control_ops_watchdog.py`.
- Source watchdog mirror: `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/mission_control_ops_watchdog.py`.
- Cron: `feec299b99e5` — Mission Control ops watchdog silent, every 15 minutes, `no_agent=True`, deliver origin only on stdout/nonzero failure.

## UI/operating model added to Mission Control

- `/goal` for long missions with scope, evidence, checklist and ready criteria.
- `/subgoal` for execution packets: research, implementation, QA, deploy, learning.
- Approval buttons language: `Aprovar escopo`, `Ajustar`, `Preview only`, `Bloquear`.
- Executive board lanes: Backlog, Doing, Waiting Lucas, Waiting External, QA, Done.
- Watcher registry: runtime/cron, Mission Control, Zipper OS, Mordomo, LK mandatory reports.
- Shopify skill state: read-only and product-upload skills are separate; no Shopify/Tiny/Merchant writes without current approval.
- QA guidance: every script promoted to cron needs smoke test, silent-OK contract, secret scan and Mission Control registration.

## Safety boundary

Autonomous: A0/A1/A2 read-only, local/reversible docs, skill mirrors, reports, previews, QA, Vercel Mission Control publish with validation/rollback.

Requires current explicit approval: Docker/host/Traefik/container restart, database/source-of-truth writes, Shopify/Tiny/Merchant writes, email/WhatsApp/client sends, money/campaigns, secrets, destructive actions, public proxy/API exposure.

## Verification pattern

1. `npm run lint` in Mission Control repo.
2. `npm run build` in Mission Control repo.
3. `npx vercel build --prod --scope lk-snkrs-projects` before prebuilt deploy.
4. `npx vercel deploy --prebuilt --prod --yes --scope lk-snkrs-projects` using a Vercel token from Doppler without printing the token.
5. GET `https://mission.lucascimino.com` and verify markers for `Rituais Hermes v0.14`, `Shopify Skill`, `Aprovar escopo`, `lk-shopify-product-upload`.
6. Run `/opt/data/scripts/mission_control_ops_watchdog.py`; healthy output is empty stdout and rc=0.
7. Run cron `feec299b99e5`; healthy status is `last_status=ok` and no alert content.
