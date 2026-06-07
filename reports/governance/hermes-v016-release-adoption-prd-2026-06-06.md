# PRD — Hermes v0.16 Release Adoption

- Date: 2026-06-06
- Owner: Hermes Geral / Lucas Cimino runtime governance
- Runtime baseline after cutover: Hermes Agent v0.16.0 (`v2026.6.5`) on mounted venv `/opt/data/hermes-0.15.1-venv`
- Release source: GitHub release `NousResearch/hermes-agent@v2026.6.5`, “The Surface Release”, published 2026-06-06T00:55:58Z
- Previous live version: Hermes Agent v0.15.2 (`v2026.5.29.2`)
- Scope of this PRD: understand, document, prioritize, and adopt relevant v0.16 capabilities for Lucas/Cimino Hermes without creating unsafe production exposure.

## 1. Problem / correction

The v0.16 runtime upgrade was executed and validated, but the release-adoption obligation was incomplete: updating the binary/config is not enough. For every Hermes version upgrade, the operating agreement is:

1. Read the official release notes/changelog for the exact target release.
2. Map new capabilities, fixes, breaking changes, config migrations, and security items against the Lucas/Cimino runtime.
3. Classify what is already active, what needs safe local configuration, what needs PRD/spike, and what is blocked by production/external-surface approval.
4. Implement/adopt the relevant safe items, or create explicit approval packets for riskier ones.
5. Record evidence, verification, and rollback/guardrails.

This PRD closes the documentation gap and becomes the adoption backlog for v0.16.

## 2. Release summary

Official release headline:

- Hermes Agent v0.16.0 (`v2026.6.5`) — “The Surface Release”.
- Since v0.15.2: 874 commits, 542 merged PRs, 1,962 files changed, 399 issues closed, 16 security-tagged.

Primary themes:

1. Native Hermes Desktop app.
2. Remote Hermes gateway connection from Desktop with OAuth or username/password.
3. Web dashboard promoted into full admin panel.
4. Fuzzy model picker everywhere; hourly model catalog refresh.
5. `/undo [N]` across CLI/TUI/messaging.
6. Leaner skills surface and trusted NVIDIA skills tap.
7. Core agent/session/performance/reliability improvements.
8. Gateway streaming/messaging improvements.
9. Setup and TUI improvements.
10. Docker/deployment hardening.
11. Security fixes and dependency pins.

## 3. Lucas/Cimino product goals for v0.16 adoption

### Goal A — Safer Hermes upgrade governance

Every future Hermes update must produce a release-adoption packet before being called complete.

Success criteria:

- Release notes saved or linked in Brain.
- “Already active / needs local adoption / needs approval / skip” matrix exists.
- User-facing summary says honestly which novelty was adopted vs only available.

### Goal B — Use v0.16 improvements that improve current Telegram/Multi-profile operations

Priority is not “turn on every feature”; priority is adopt improvements that reduce noise, improve control, and preserve safety.

Success criteria:

- `/undo [N]` validated in Telegram-safe or CLI-safe manner.
- Model catalog refresh/fuzzy picker impact documented and, if safe, verified via CLI/dashboard read-only commands.
- Inline-button decision UX uses native buttons and no leaked wrappers.
- Skills surface remains explicit: local custom skills are preserved; upstream pruning does not delete Lucas-specific skills.

### Goal C — Evaluate new control surfaces without unsafe exposure

Desktop and dashboard are major v0.16 surfaces, but they are high-privilege. They must be evaluated through read-only/local/preview stages before any public exposure.

Success criteria:

- Desktop remote-backend plan exists with local/SSH-tunnel preference.
- Dashboard admin panel is audited for current exposure before use.
- No public dashboard/API/credential surface is opened without explicit scoped approval, backup, rollback, and verification.

## 4. New capabilities and adoption classification

### 4.1 Hermes Desktop app

Release novelty:

- New Electron desktop app for macOS/Linux/Windows.
- Native chat, streaming, session list/search/archive, drag-and-drop files, clipboard image paste, command palette, model picker, settings UI, Simplified Chinese translation.
- Can connect to remote Hermes gateway via OAuth or username/password.

Lucas/Cimino relevance:

- High potential for Mission Control / cockpit UX.
- Could reduce dependency on Telegram for deep operations.
- Could be useful for Lucas on Mac as a GUI for the existing remote Hermes.

Current status:

- Available in v0.16 codebase.
- Not installed or connected for Lucas yet.
- Remote connection requires API/dashboard/auth surface review.

Adoption classification:

- PRD/spike required before implementation.
- No production exposure by default.
- Preferred first stage: local Desktop install on Lucas machine connecting through safe local/SSH tunnel or explicitly approved remote backend.

Risks:

- Remote Desktop connection can expose a high-privilege agent surface.
- OAuth/username-password setup may require dashboard/API config and gateway restart.
- Public endpoints require Traefik/VPS/Docker approval, currently not included in v0.16 cutover scope.

Recommended adoption:

- Create separate “Hermes Desktop Remote Backend PRD” before activation.
- Audit current API/dashboard exposure read-only.
- Prefer local-only API or SSH tunnel; do not expose public dashboard/API without explicit approval.

### 4.2 Web dashboard full admin panel

Release novelty:

- Dashboard now supports admin surfaces for MCP catalog, messaging channels, credentials, webhooks, memory, gateway controls, hooks, system settings, check-before-update, Debug Share.
- Adds authentication capabilities including username/password and generic self-hosted OIDC.

Lucas/Cimino relevance:

- Could become operational cockpit for configuring channels/tools/MCP without SSH.
- Also becomes a high-risk control plane if public or weakly authenticated.

Current status:

- Runtime contains v0.16 dashboard code.
- This PRD does not verify that dashboard is enabled/exposed.

Adoption classification:

- Read-only exposure audit first.
- Public or write-enabled use requires explicit approval.

Recommended adoption:

- Stage 0: classify current dashboard/API exposure locally: listeners, auth, public hostnames, `/health`, `/docs`, `/openapi.json`, public frontend token leakage, `/api/config` access behavior.
- Stage 1: if safe/local-only, create a preview capability card for dashboard admin panel.
- Stage 2: only after approval, enable specific cockpit use cases.

### 4.3 `/undo [N]`

Release novelty:

- `/undo [N]` backs up N user turns, pre-fills the last message, soft-deletes the turns in between.
- Works across CLI, TUI, and messaging platforms including Telegram/Discord.

Lucas/Cimino relevance:

- Very relevant for Telegram mistakes and runaway turns.
- Low-risk capability if used manually.

Current status:

- Available in v0.16.
- Not yet smoke-tested in Lucas production Telegram because it affects session history.

Adoption classification:

- Safe to document immediately.
- Smoke test should be done in a disposable/fresh session or CLI, not in the middle of critical work.

Recommended adoption:

- Add to Lucas Hermes operating guide: use `/undo 1` to retract the last user turn when a wrong instruction was sent.
- Test in local CLI or a new Telegram thread/session.

### 4.4 Fuzzy model picker + hourly model catalog refresh

Release novelty:

- Model picker fuzzy search across Desktop/Web/TUI/CLI.
- Multi-endpoint providers grouped under one row.
- Catalog refresh lowered from daily to hourly.
- New models: `deepseek-v4-flash`, MiniMax-M3 with 1M context, `qwen3.7-plus`, Gemini 3.5 Flash in relevant pickers.

Lucas/Cimino relevance:

- Relevant for model routing and availability.
- Hourly catalog refresh can improve adoption of new models.
- New models must not be auto-adopted for production-critical profiles without smoke tests.

Current status:

- Config migration v24→v27 already lowered `model_catalog.ttl_hours` to 1.
- Runtime v0.16 is active.

Adoption classification:

- Already partially adopted by config migration.
- Need read-only verification of model catalog/picker behavior and model availability.
- Any default-model changes require separate scoped approval and smoke tests.

Recommended adoption:

- Verify `model_catalog.ttl_hours: 1` in `/opt/data/config.yaml` and relevant specialist configs.
- Run safe model/provider smoke tests for configured default/fallback models.
- Do not switch business-critical defaults just because new models exist.

### 4.5 Leaner default skills + NVIDIA trusted skills tap

Release novelty:

- Bundled default skill set trimmed.
- Some skills removed/replaced; some moved to optional.
- New `environments:` relevance gate.
- Curator can prune unused built-in skills.
- NVIDIA/skills added as trusted tap.

Lucas/Cimino relevance:

- High relevance because Lucas has many custom skills and profile-specific procedures.
- Upstream pruning must not delete local business-critical skills.
- NVIDIA tap may be useful for CUDA/AIQ/cuOpt/ML tasks, but not core to current operations.

Current status:

- Local `/opt/data/skills` still contains many Lucas-specific skills.
- We have not audited whether any expected upstream skill moved/changed.

Adoption classification:

- Audit required; do not auto-prune.
- Optional skill installs require explicit need.

Recommended adoption:

- Run read-only skill inventory diff: local skills vs v0.16 bundled/optional catalog.
- Protect Lucas critical skills from accidental curator pruning.
- Update local skills where v0.16 changed semantics (e.g., release adoption agreement, inline button UX).

### 4.6 Gateway streaming/messaging improvements

Release novelty:

- Structured stream-event protocol.
- Telegram draft formatting parity.
- Per-platform streaming defaults and dashboard toggles.
- Gateway restart flow improvements and adapter cleanup fixes.

Lucas/Cimino relevance:

- Relevant for Telegram UX, live drafts, and restart reliability.
- Lucas prefers Telegram only for actionable alerts, not noise.

Current status:

- Gateway v0.16 is active and Telegram connected.
- No targeted streaming UX smoke test yet.

Adoption classification:

- Local verification can be done safely.
- Any Telegram delivery behavior changes should preserve low-noise policy.

Recommended adoption:

- Verify Telegram streaming setting from config/read-only status.
- Test one non-sensitive short response for formatting/delivery if needed.
- Ensure cron decision buttons still render cleanly without scheduler wrappers.

### 4.7 Core agent/session/performance improvements

Release novelty:

- Progressive tool disclosure for MCP/plugin tools.
- Broader Hermes self-knowledge pointer to docs + skill.
- `hermes prompt-size` diagnostic.
- `read_file` token reduction.
- Session FTS optimization commands.
- Compression/conversation-loop/auxiliary-client changes in diff.

Lucas/Cimino relevance:

- High relevance for long Telegram sessions, context compression, session search, and tool-prompt bloat.

Current status:

- Runtime active.
- Some changes are automatic; diagnostics not yet adopted into operations.

Adoption classification:

- Safe local adoption: document and add to operating runbooks.
- Potential implementation: add release-postcheck checklist to future upgrade skill.

Recommended adoption:

- Add `hermes prompt-size` to future performance/upgrade diagnostics if present.
- Run `hermes sessions optimize` only after checking help/impact; local DB maintenance but still should be done with backup.
- Keep compression self-heal watchdog aligned with v0.16 code changes.

### 4.8 Setup/TUI/CLI improvements

Release novelty:

- Configurable default interface `cli` vs `tui`.
- TUI startup no longer blocked by slow/dead MCP servers.
- Setup simplified via Nous Portal Quick Setup and `hermes portal`.
- Pickers migrated and improved.

Lucas/Cimino relevance:

- Useful for local CLI workflows and future desktop/TUI use.
- Not directly required for Telegram multi-profile runtime.

Adoption classification:

- Document; no immediate production mutation.

Recommended adoption:

- Keep Telegram runtime unchanged.
- If Lucas wants CLI/TUI as control plane, evaluate default interface separately.

### 4.9 Tool system / installer / Docker deployment hardening

Release novelty:

- Managed uv path, hardened venv rebuild, update-boundary fixes, stash/restore behavior, container labels, bounded sync cleanup, non-root container boot fixes.

Lucas/Cimino relevance:

- Relevant to future upgrades and container runtime governance.
- Current upgrade used mounted venv, not Docker image rebuild.

Current status:

- v0.16 package installed in mounted venv.
- Docker/Traefik/VPS were explicitly out of scope.

Adoption classification:

- Document for next upgrade cycle.
- Do not mutate Docker/VPS now.

Recommended adoption:

- Update Hermes upgrade runbook: release-note adoption is a required stage.
- For future image-based upgrades, evaluate new installer/update path before using mounted-venv shortcut.

### 4.10 Security & reliability

Release novelty:

- Starlette CVE-2026-48710 pinned to patched Starlette ≥1.0.1.
- SSRF checks moved off event loop in async paths.
- Bedrock token stripped from subprocess env.
- `bws_cache.json` file-safety guard.
- Mutation-verifier footer path neutralization.
- `execute_code` approval/sudo context restored.
- Dangerous patterns expanded for Docker stop/restart/kill.
- Invisible Unicode sanitization in vetted skill content.

Lucas/Cimino relevance:

- High relevance: Lucas has strict production/security guardrails.
- Security fixes are already in installed runtime if dependency pins resolved correctly.

Current status:

- v0.16 installed; `hermes --version` shows v0.16.
- Need confirm key dependency versions from live venv (`starlette`, `fastapi`, etc.) and security guard behavior if desired.

Adoption classification:

- Immediate verification item.
- No extra approval needed for read-only dependency/version checks.

Recommended adoption:

- Run read-only dependency version snapshot and store with release adoption evidence.
- Keep production guardrails stricter than upstream defaults.

## 5. Implementation backlog

### P0 — Complete release-adoption documentation and evidence

Status: in progress via this PRD.

Tasks:

1. Save official release metadata/body locally.
2. Save this PRD in Brain.
3. Run Brain Health.
4. Run targeted secret scan on PRD/evidence.
5. Create a short user-facing adoption summary.

Acceptance criteria:

- PRD file exists.
- Release source evidence exists in `/opt/data/hermes_v016_release_research_*`.
- Brain Health passes.
- Secret scan returns zero findings.

### P1 — Add future-upgrade runbook rule

Goal:

Prevent recurrence of “binary upgraded but release adoption not reviewed”.

Tasks:

1. Patch local Hermes upgrade skill/reference to include mandatory release-note adoption stage.
2. Add checklist:
   - release notes fetched;
   - feature matrix written;
   - automatic vs config vs gated adoption classified;
   - smoke tests selected;
   - PRD/receipt written.
3. Verify skill still loads.

Approval:

- Local skill/doc patch only; within safe local autonomy.

### P1 — v0.16 security/dependency verification

Goal:

Confirm security-relevant release fixes are present in live runtime.

Tasks:

1. Snapshot live versions: `starlette`, `fastapi`, `pydantic`, `openai`, `aiohttp`, `mcp`, `uvicorn`.
2. Confirm Starlette is at patched v1.0.1 per release.
3. Record result in release adoption receipt.

Approval:

- Read-only local verification; no approval needed.

### P1 — `/undo [N]` adoption

Goal:

Document and safely validate `/undo` for Lucas workflows.

Tasks:

1. Verify `/undo --help` or command registry support without mutating production session.
2. Test in disposable CLI/new session if feasible.
3. Add short Lucas-facing guidance: use `/undo 1` for bad last instruction.

Approval:

- CLI/new-session local test safe; Telegram live-session test should be explicitly approved or done in a disposable chat/thread.

### P1 — Dashboard/Desktop exposure audit packet

Goal:

Evaluate new v0.16 surfaces before enabling operational use.

Tasks:

1. Read-only classify API/dashboard listeners and auth gates.
2. Probe local endpoints only.
3. Check public hostname behavior only with safe GET/HEAD if already existing.
4. Produce “Desktop/Dashboard adoption packet” with recommended local/SSH-tunnel path.

Approval:

- Read-only local audit is safe.
- Any public exposure, Docker/Traefik/VPS/dashboard activation, OAuth registration, or credential write requires explicit scoped approval.

### P2 — Model catalog/fuzzy picker verification

Goal:

Confirm v0.16 model catalog improvements are active without changing production defaults.

Tasks:

1. Confirm `model_catalog.ttl_hours: 1` in default config.
2. Run read-only model catalog/list command if available.
3. Smoke current configured provider/model; do not switch defaults.

Approval:

- Read-only checks safe.
- Model default/fallback changes require scoped approval and smoke testing.

### P2 — Skills surface audit

Goal:

Ensure upstream v0.16 skill pruning does not harm Lucas local skills and evaluate NVIDIA tap.

Tasks:

1. Inventory local critical skills.
2. Identify bundled→optional/removal effects relevant to local workflows.
3. Mark Lucas critical skills as local/governed; do not prune automatically.
4. Evaluate NVIDIA tap only if an ML/CUDA workload appears.

Approval:

- Read-only inventory safe.
- Installing/removing skills should be explicit unless it is a local skill patch needed for this governance procedure.

### P2 — Gateway streaming/inline UX smoke

Goal:

Confirm v0.16 gateway UX does not regress Lucas Telegram expectations.

Tasks:

1. Verify Telegram connected and streaming config.
2. Verify cron inline-button parser path remains clean.
3. If a live cron decision is generated, inspect it for native buttons and no wrapper leakage.

Approval:

- Local parser tests safe.
- User-visible Telegram test should be purposeful and low-noise.

## 6. Non-goals

- Do not expose dashboard/API publicly as part of this PRD.
- Do not modify Docker, Traefik, VPS, public domains, or external credentials without explicit approval.
- Do not switch default models just because new models exist.
- Do not install desktop app or connect Lucas’s machine without a separate Desktop Remote Backend PRD.
- Do not prune local/custom Lucas skills automatically.

## 7. Guardrails

- External writes, production infra, Docker, Traefik, VPS, dashboard exposure, credential writes, OAuth registration, and public endpoints require explicit scoped approval with backup/rollback/verification.
- Local read-only evidence, Brain docs, local PRD, secret scan, and Brain Health can proceed autonomously.
- Telegram should receive only actionable summaries, not raw release dumps.
- Reports must redact secrets and avoid printing `.env`, `auth.json`, tokens, keys, and connection strings.

## 8. Verification plan

For this PRD:

- Targeted secret scan on PRD and release evidence summary.
- Brain Health check.

For adoption implementation:

- Dependency snapshot command for security fixes.
- `/undo` disposable-session test.
- Dashboard/API exposure audit read-only.
- Model catalog/config readback.
- Skill inventory read-only.
- Gateway/inline parser smoke tests.

## 9. Open decisions for Lucas

The immediate safe next actions do not require production approval:

1. Patch the Hermes upgrade runbook/skill so future upgrades require release-adoption PRD.
2. Run read-only v0.16 dependency/security verification.
3. Run read-only model catalog/config verification.
4. Run read-only dashboard/API exposure classification.

Actions that should wait for explicit approval:

1. Enabling or exposing dashboard/admin panel.
2. Connecting Desktop to remote Hermes.
3. Changing default models/fallbacks for live profiles.
4. Installing/removing upstream skills or pruning skills.
5. Any Docker/Traefik/VPS/public endpoint change.

## 10. Recommendation

Proceed in two tracks:

- Track 1 — Safe local adoption now: runbook patch, dependency/security snapshot, model catalog readback, `/undo` disposable test, skill inventory read-only.
- Track 2 — Separate PRD/approval packet: Desktop + Dashboard remote control surface, because this creates a new high-privilege operational interface.

This keeps v0.16 adoption real while preserving Lucas’s guardrails.
