# Hermes v0.14 watchdog reconciliation — 2026-05-16

## Trigger
After a Lucas-approved Hermes production upgrade, a no-agent runtime watchdog alerted because it still expected v0.13 while the live runtime was healthy on v0.14.

Alert shape:
- expected version fragment: `v0.13.0`
- observed: `Hermes Agent v0.14.0 (2026.5.16)`
- probable impact text suggested drift/gateway risk

## Durable lesson
A successful Hermes runtime upgrade must include reconciliation of every monitor, helper, cron prompt, skill note, and Brain ledger that encodes the previous expected version/image. Otherwise watchdogs generate false-positive alerts even when production is healthy.

## Safe response pattern
1. Load `hermes-agent` and `lucas-hermes-continuous-improvement` before acting.
2. Verify live state read-only:
   - `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes --version`
   - `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron status`
   - local API `/health` if configured
   - Docker host observability helper when available
3. Distinguish two cases:
   - runtime unhealthy: escalate with plan/rollback; do not mask the alert
   - runtime healthy but monitor expects old version: update monitor expectations and document the reconciliation
4. Patch both active scripts and their Brain source copies:
   - `/opt/data/scripts/hermes_runtime_cron_watchdog.py`
   - `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/scripts/hermes_runtime_cron_watchdog.py`
   - `/opt/data/scripts/hermes_host_docker_observability.py`
   - `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/scripts/hermes_host_docker_observability.py`
5. Update the daily intelligence cron prompt so the new version/image is source-of-truth.
6. Run the watchdog locally and/or trigger the no-agent cron to verify the silent contract:
   - `rc=0` + empty stdout = OK/no Telegram noise
   - `rc=0` + stdout = alert
   - nonzero rc = watchdog failure
7. Document in Brain:
   - run report or reconciliation note
   - `CHANGELOG.md`
   - relevant operations routine/ledger
   - skill note if the lesson is durable

## Pitfall
Do not treat every “unexpected version” watchdog alert as an outage. First check whether the live runtime was intentionally upgraded and whether the monitor is stale. Conversely, do not silence the watchdog until runtime health has been verified read-only.

## Guardrail
This reconciliation is safe only when it updates local scripts/docs/prompts. It must not restart gateway/containers, mutate compose/Traefik/host, alter secrets, or perform a new runtime swap without explicit current approval and rollback plan.
