# Host Docker observability helper — 2026-05-12

## Context

The daily Hermes/LK continuous-improvement cron (`f5a23dd6a1bd`) ran inside the Hermes container and could not access `/var/run/docker.sock`, so it could not verify Hostinger Docker container images/logs directly. Lucas approved correcting the gap with “Corrigir o que deve ser corrigido está aprovado”.

## Approved scope

Allowed:
- read-only SSH to `lc.vps` using Doppler-sourced credentials;
- read-only Docker/Hermes inspection commands;
- sanitized JSON report files under Hermes Brain reports;
- daily cron prompt integration so future runs use the helper first.

Not allowed without a fresh plan + approval:
- Docker/container/compose/gateway restart or mutation;
- root/SSH/permission/socket changes;
- installing packages on the VPS;
- printing secrets or raw logs.

## Implemented helper

Active path:

```bash
/opt/data/scripts/hermes_host_docker_observability.py
```

Brain source copy:

```bash
/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/scripts/hermes_host_docker_observability.py
```

Typical daily-run command:

```bash
/opt/data/scripts/hermes_host_docker_observability.py \
  --output /opt/data/hermes_bruno_ingest/hermes-brain/reports/hermes-host-docker-observability-$(date -u +%F).json
```

Silent watchdog contract:

```bash
/opt/data/scripts/hermes_host_docker_observability.py \
  --watchdog \
  --output /opt/data/hermes_bruno_ingest/hermes-brain/reports/hermes-host-docker-observability-latest.json
```

- stdout empty means OK;
- stdout with alerts means investigate;
- nonzero rc means helper failure.

## Technique

The helper:
1. Reads the local Doppler token file only to call Doppler API, never printing it.
2. Fetches `VPS_IP` and `VPS_ROOT_PASSWORD` at runtime.
3. Creates a temporary `SSH_ASKPASS` script in a tempdir, mode `0700`.
4. Runs SSH to `root@<VPS_IP>` with password auth and a remote `bash -s` script.
5. Executes only read-only commands:
   - `docker ps -a --filter name=... --format '{{json .}}'`
   - `docker exec <container> /opt/hermes/.venv/bin/hermes --version`
   - `docker exec <telegram-container> /opt/hermes/.venv/bin/hermes cron status`
   - `docker exec <telegram-container> /opt/hermes/.venv/bin/hermes cron list --all`
   - `docker logs --tail N <telegram-container>`
6. Scrubs token/password/authorization-like strings before writing output.
7. Writes a sanitized JSON report only.

## Verification from first run

Observed OK:
- `hermes-agent-5ajw-hermes-agent-1`: `running`, image `hermes-agent-custom:v0.13.0-20260510`;
- `hermes-agent-5ajw-hermes-telegram-1`: `running`, image `hermes-agent-custom:v0.13.0-20260510`;
- both containers reported `Hermes Agent v0.13.0 (2026.5.7)`;
- `hermes cron status` inside Telegram container reported `Gateway is running — cron jobs will fire automatically`;
- helper alerts: `0`;
- `--watchdog` stdout length: `0` when OK.

## Pitfalls

- Do not over-redact structural identifiers like container names. A blanket 32+ char redactor hid expected container names and caused false missing-container alerts. Prefer targeted redaction for `token`, `password`, `secret`, `authorization`, bearer tokens, and URLs containing token-like params.
- If helper fails, do not “fix” by changing root/SSH/Docker/socket permissions. Report the failure and request a fresh plan if access/infra changes are needed.
- Keep source copy and active copy synced after edits:

```bash
install -m 700 /opt/data/scripts/hermes_host_docker_observability.py \
  /opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/scripts/hermes_host_docker_observability.py
python3 -m py_compile /opt/data/scripts/hermes_host_docker_observability.py \
  /opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/scripts/hermes_host_docker_observability.py
```
