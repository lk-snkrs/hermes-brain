# Hermes v0.16.0 A3 upgrade approval packet — 2026-06-06

## Scope approved by Mesa item 1/4

Prepare a read-only A3 approval packet for the Hermes v0.16.0 update evaluation. This packet does **not** execute a runtime swap, Docker pull/build, gateway restart, Traefik/host change, config migration, or production mutation.

## Current verified state

- Checked at: 2026-06-06T13:37:21+00:00
- Active Hermes runtime: `Hermes Agent v0.15.2 (2026.5.29.2)`
- Runtime project path reported by CLI: `/opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages`
- Active config path: `/opt/data/config.yaml`
- Config check: `Config version: 24 ✓`
- CLI update notice: `Update available: 1 commit behind — run 'docker pull nousresearch/hermes-agent:latest'`
- Latest GitHub release: `v2026.6.5` / `Hermes Agent v0.16.0 (2026.6.5) — The Surface Release`
- Release URL: https://github.com/NousResearch/hermes-agent/releases/tag/v2026.6.5
- Release published: 2026-06-06T00:55:58Z

## Release signal

The v0.16.0 release notes describe a large jump since v0.15.2:

- 874 commits;
- 542 merged PRs;
- 1,962 files changed;
- 2 P0 closures;
- 62 P1 closures;
- 16 security-tagged items;
- major Desktop app surface;
- expanded web dashboard/admin panel;
- gateway/channel/MCP/credential/webhook/memory administration improvements;
- first-time setup improvements;
- model picker improvements;
- `/undo` improvements;
- security round including Starlette CVE pin, SSRF off-loop hardening, and subprocess credential stripping.

## Why this matters for Lucas/Cimino

Potential value:

1. Better operational surface for Hermes: Desktop + web dashboard/admin features may reduce Telegram-only operational friction.
2. Better profile/channel/MCP/credential visibility: useful for the current multi-profile LK/Mordomo/SPITI architecture.
3. Security fixes: likely important because Lucas runs messaging gateways, API/webhook surfaces, tools, and multi-profile specialist agents.
4. UX improvements: model picker and `/undo` can reduce operational mistakes.

Main risks:

1. Large release surface: 1,962 changed files means high regression risk.
2. Production is Docker-first with launcher-selected runtime; image tag alone is not source of truth.
3. Current runtime has custom/learned patches and guardrails around Telegram clean delivery, Mesa buttons, context compression, model fallback, specialist profiles, watchdogs, and Brain governance.
4. Dashboard/admin surface may expose powerful controls and must be classified before use.
5. Gateway restart can interrupt active Telegram sessions and specialist bots.

## Explicitly not approved in this packet

- No Docker pull/build/recreate.
- No production container swap.
- No gateway restart/reload.
- No Traefik/VPS/host/network mutation.
- No config migration applied to live runtime.
- No token/secret changes.
- No Shopify/Tiny/GMC/Ads/WhatsApp/e-mail/customer/supplier writes.
- No public dashboard/API exposure change.

## Recommended staged procedure before any runtime action

### Stage 0 — Read-only discovery, done for this packet

- Verify current runtime version/config path/config version.
- Verify latest release from GitHub Releases API.
- Record release URL and high-level change/risk class.

### Stage 1 — Parallel preparation, still no production mutation

1. Create or update a separate v0.16 install/runtime directory rather than mutating the live v0.15.2 runtime in place.
2. Preserve and diff local patches/guardrails:
   - Telegram clean delivery and inline buttons;
   - Mesa COO button/callback path;
   - context-compression retry/self-heal;
   - model fallback/nonresponse watchdog behavior;
   - specialist profile activation/watchdog logic;
   - Brain health/safe-sync validators.
3. Run targeted unit/smoke tests from the candidate runtime.
4. Run candidate `hermes --version`, `hermes config check`, and config migration preview/backup plan.
5. Produce a rollback plan pointing the launcher back to the current v0.15.2 runtime.

### Stage 2 — Approval required before activation

Before any live swap/restart, Lucas must approve a second scoped packet that includes:

- exact runtime path/image to activate;
- backup locations;
- rollback command/path;
- expected downtime/interruption;
- profiles affected;
- verification checklist;
- explicit exclusions.

### Stage 3 — If separately approved later

1. Backup live config/auth/session/cron references as needed without printing secrets.
2. Switch only the approved runtime surface.
3. Restart/reload only the affected gateway/runtime surface.
4. Verify exact live process via `/proc/<pid>/environ` and `cmdline`.
5. Verify API/webhook/Telegram health and specialist profile behavior.
6. Run post-upgrade adoption cycle: config migrate/check, Brain docs, watchdog expected version update, smoke tests, targeted secret scan, and daily loop prompt/skill updates if needed.

## Recommendation

Proceed with Stage 1 parallel preparation only. Do not update production live runtime yet.

Reason: v0.16.0 has material security/UX/admin value, but the release surface is large and the current Lucas/Cimino runtime has multiple custom operational guardrails that must be preserved and smoke-tested before any live swap.

## Next approval needed

Approval needed only if Lucas wants Hermes to prepare the v0.16 candidate runtime locally and run the Stage 1 test matrix. That approval would still exclude Docker/gateway restart/production swap unless explicitly included in a later packet.
