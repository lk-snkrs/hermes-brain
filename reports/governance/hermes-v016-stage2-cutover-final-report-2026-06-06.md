# Hermes v0.16 Stage 2 Cutover — Final Report

- Date: 2026-06-06T14:20:22.626194+00:00
- Scope: default Hermes runtime only (`/opt/data`), mounted venv `/opt/data/hermes-0.15.1-venv`, config migration, inline-buttons patch, local validation.
- Explicitly out of scope: Docker, Traefik, VPS, dashboard, unrelated external mutations.
- Backup: `/opt/data/backups/hermes-v016-cutover-20260606-140851` (restricted local backup; contains sensitive snapshots, do not publish).

## Result

Stage 2 completed successfully. The default gateway restarted after the controlled stop/restart interruption, is now running from the mounted venv with Hermes Agent v0.16.0, and local Telegram/API/webhook/cron validations passed. Rollback was not needed.

## Evidence

```text
=== final evidence date ===
2026-06-06T14:20:17+00:00
=== live package version ===
Hermes Agent v0.16.0 (2026.6.5)
Project: /opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages
Python: 3.13.5
OpenAI SDK: 2.24.0
Up to date
=== inline runtime smoke ===
inline_marker_clean_delivery_ok
=== process truth ===
HERMES_HOME=/opt/data PID=1 start=2026-06-06T14:15:09+0000 PYTHONPATH=/opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages CMD=/opt/data/hermes-0.15.1-venv/bin/python /opt/data/hermes-0.15.1-venv/bin/hermes gateway run 
HERMES_HOME=/opt/data PID=2602 start=2026-06-06T14:20:17+0000 PYTHONPATH=/opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages CMD=/usr/bin/bash -c source /tmp/hermes-snap-5cdc4eeeef33.sh >/dev/null 2>&1 || true
builtin cd -- /opt/data || exit 126
eval 'set -euo pipefail
BACKUP="$(cat /tmp/hermes_stage2_backup
HERMES_HOME=/opt/data PID=2607 start=2026-06-06T14:20:17+0000 PYTHONPATH=/opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages CMD=/usr/bin/bash -c source /tmp/hermes-snap-5cdc4eeeef33.sh >/dev/null 2>&1 || true
builtin cd -- /opt/data || exit 126
eval 'set -euo pipefail
BACKUP="$(cat /tmp/hermes_stage2_backup
HERMES_HOME=/opt/data/profiles/lk-collection-optimizer PID=379 start=2026-06-06T14:15:30+0000 PYTHONPATH=/opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages CMD=/opt/hermes/.venv/bin/python3 /opt/hermes/.venv/bin/hermes gateway run 
HERMES_HOME=/opt/data/profiles/lk-growth PID=161 start=2026-06-06T14:15:25+0000 PYTHONPATH=/opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages CMD=/opt/hermes/.venv/bin/python3 /opt/hermes/.venv/bin/hermes gateway run 
HERMES_HOME=/opt/data/profiles/lk-ops PID=175 start=2026-06-06T14:15:27+0000 PYTHONPATH=/opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages CMD=/opt/hermes/.venv/bin/python3 /opt/hermes/.venv/bin/hermes gateway run 
HERMES_HOME=/opt/data/profiles/lk-shopify PID=262 start=2026-06-06T14:15:28+0000 PYTHONPATH=/opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages CMD=/opt/hermes/.venv/bin/python3 /opt/hermes/.venv/bin/hermes gateway run 
HERMES_HOME=/opt/data/profiles/lk-trends PID=286 start=2026-06-06T14:15:29+0000 PYTHONPATH=/opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages CMD=/opt/hermes/.venv/bin/python3 /opt/hermes/.venv/bin/hermes gateway run 
HERMES_HOME=/opt/data/profiles/mordomo PID=160 start=2026-06-06T14:15:24+0000 PYTHONPATH=/opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages CMD=/opt/hermes/.venv/bin/python3 /opt/hermes/.venv/bin/hermes gateway run 
HERMES_HOME=/opt/data/profiles/spiti PID=169 start=2026-06-06T14:15:26+0000 PYTHONPATH=/opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages CMD=/opt/hermes/.venv/bin/python3 /opt/hermes/.venv/bin/hermes gateway run 
=== api health ===
{"status": "ok", "platform": "hermes-agent"}
=== gateway status ===
✓ Gateway is running (PID: 1, 160, 161, 169, 175, 262, 286, 379)
  (Running manually, not as a system service)

To install as a service:
  hermes gateway install
  sudo hermes gateway install --system

Other profiles:
  ✓ lk-collection-optimizer — PID 379
  ✓ lk-growth        — PID 161
  ✓ lk-ops           — PID 175
  ✓ lk-shopify       — PID 262
  ✓ lk-trends        — PID 286
  ✓ mordomo          — PID 160
  ✓ spiti            — PID 169
=== cron status ===

✓ Gateway is running — cron jobs will fire automatically
  PID: 1, 160, 161, 169, 175, 262, 286, 379

  27 active job(s)
  Next run: 2026-06-06T14:20:00+00:00

=== webhook list ===

  3 webhook subscription(s):

  ◆ lk-shopify-tiny-stock-sync-dryrun
    LK Shopify orders/paid|orders/cancelled -> Tiny official stock dry-run ledger (no writes)
    URL:     http://localhost:8644/webhooks/lk-shopify-tiny-stock-sync-dryrun
    Events:  orders/paid, orders/cancelled
    Deliver: log

  ◆ lk-shopify-tiny-stock-sync
    LK Shopify orders/paid|orders/cancelled -> deterministic Tiny official stock local SQLite refresh (no Shopify/Tiny writes)
    URL:     http://localhost:8644/webhooks/lk-shopify-tiny-stock-sync
    Events:  orders/paid, orders/cancelled
    Deliver: log

  ◆ lk-shopify-pos-restock
    URL:     http://localhost:8644/webhooks/lk-shopify-pos-restock
    Events:  orders/paid
    Deliver: log

=== config check version line ===

📋 Configuration Status

  Config version: 27 ✓

  Required:

  Optional:
=== recent startup log proof ===
Starting Hermes Gateway: 2026-06-06 14:15:19,708 INFO gateway.run: Starting Hermes Gateway...
webhook connected: 2026-06-06 14:15:19,777 INFO gateway.run: ✓ webhook connected
Connected to Telegram: 2026-06-06 14:15:23,704 INFO gateway.platforms.telegram: [Telegram] Connected to Telegram (polling mode)
api_server connected: 2026-06-06 14:15:23,769 INFO gateway.run: ✓ api_server connected
Gateway running with 3 platform: 2026-06-06 14:15:23,773 INFO gateway.run: Gateway running with 3 platform(s)
Cron ticker started: 2026-06-06 14:15:24,794 INFO gateway.run: Cron ticker started (interval=60s)

```

## Notes

- The first `hermes gateway restart` attempt was blocked because the command inherited `_HERMES_GATEWAY=1` from the running gateway.
- Retrying without that marker initiated a planned stop; the user-visible session was interrupted during shutdown, then auto-resumed after the gateway came back.
- Logs show clean platform startup after restart: webhook, Telegram polling, API server, gateway running, and cron ticker started.
- Inline buttons marker extraction was smoke-tested in the live v0.16 runtime using the installed parser format.
- Config is now version 27.

## Rollback material

- Pre-change config/env/auth/cron/session/process snapshots are under the backup directory.
- If a later regression appears, rollback should restore `config.yaml.before-v016` and reinstall Hermes v0.15.2 in the mounted venv, then restart default gateway only.
