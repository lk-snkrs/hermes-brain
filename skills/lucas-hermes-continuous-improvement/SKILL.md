---
name: lucas-hermes-continuous-improvement
version: 1.0.0
description: Daily 02:00 BRT protocol for safely tracking Hermes releases and implementing low-risk LK/Hermes Brain improvements.
---

# Lucas Hermes Continuous Improvement Protocol

## Trigger
Use when Lucas asks to keep Hermes/LK continuously updated, check Hermes releases, or implement improvements from Hermes Agent into the LK ecosystem.

## Principles
1. **Improve daily, but do not break production.** Prefer read-only discovery, previews, branches, PRs, docs, skills, and dry-runs before runtime changes.
2. **Low-risk autonomous changes are allowed — and must become operational.** Brain docs, skills, analysis scripts, preview templates, non-production artifacts, workflow improvements, read-only API checks, Doppler-backed secret use in-process, and read-only SSH/host/Docker observability may be executed autonomously when non-mutating and sanitized. Do not stop at “implemented”: connect the improvement to Lucas's day-to-day process, cron, checklist, dashboard, report, or reusable skill so it actually gets used.
3. **Use the autonomy ladder.** A0/A1 safe actions execute without asking; A2 scoped previewed/approved packages execute without new approval; A3 prepares plan/rollback but waits before production/source-of-truth write; A4 external/money/customer/secret/destructive actions are blocked until current explicit approval.
4. **Manual steps must be taught clearly.** If a useful feature requires Lucas to act manually, explain exactly what to do, when to use it, and why it matters.
5. **Medium-risk and high-risk writes need explicit approval.** Production runtime, Docker/container swaps, gateway restart, root/host/Traefik/network mutations, secrets changes, databases, Shopify writes, Meta/Google campaign changes, external sends, destructive operations, or anything with unclear blast radius require a clear plan, backup/rollback, and explicit Lucas approval.
6. **Never expose secrets.** Use Doppler/env safely; never print tokens, connection strings, passwords, or API keys.
7. **Every improvement should teach the system.** Update Brain docs, skills, changelog, or memory when a durable lesson emerges.

## Daily 02:00 BRT routine
1. Check current Hermes version with `hermes --version`.
2. Query GitHub releases for NousResearch/hermes-agent.
3. Compare current version/tag against latest release **and review recent historical releases, not only the newest one**. When catching up, inspect at least the current major catch-up window (e.g. v0.10, v0.11, v0.12, v0.13) because features often become useful only after later workflow context exists. If `web_search` is unavailable or unauthorized in a cron context, query GitHub Releases directly with `curl`/Python (`https://api.github.com/repos/NousResearch/hermes-agent/releases?per_page=10`) and record the source URL; do not skip release comparison because the web-search tool failed.
4. Read release notes and classify changes:
   - must-adopt for LK/Hermes Brain now;
   - useful but later;
   - useful only if Lucas changes a workflow;
   - irrelevant;
   - medium/high-risk or breaking.
5. Inspect local environment constraints: config path, gateway status, cron jobs, Docker/update mechanism if read-only.
6. Implement and operationalize low-risk improvements automatically:
   - skills/docs updates;
   - Brain/Mission Control documentation;
   - local preview/prototype scripts;
   - cron/watchdog proposals or non-invasive checks;
   - PRs for documentation/scripts when tests pass;
   - integration into daily workflow, reports, checklists, or reusable commands.
7. Include a daily **Hermes mechanism improvement** review, not only Brain/business structure: did the agent ask for approval too often or too little, stop early, require repeated “seguir”, produce overly technical reports, leave context only in chat, use an outdated prompt/skill, miss a safer tool pattern, create unnecessary noise, or fail to document an action? Convert findings into Brain docs, skill patches, prompt improvements, or approval-needed briefs.
8. For manual improvements, teach Lucas the exact usage pattern: command, when to use, expected result, and failure signs.
9. For release-window reviews, do not stop at summarizing release notes. Translate features into Lucas operating habits and classify them as: already adopted, P0 habit now, P1 workflow/Brain improvement, P2 exploratory/approval-needed, or irrelevant. For the v0.12–v0.14 pattern, prioritize `/goal` + `/subgoal`, structured approval buttons, silent `no_agent` watchers, Kanban as a manual executive board before workers, cron `context_from`, and read-only `x_search`/browser intelligence. See `references/v012-v014-opportunity-review-20260516.md`.
10. After any approved Hermes runtime update, do not stop at “it is back/healthy.” Complete the post-update adoption cycle: verify runtime/gateway/API/Telegram; reconcile watchdog/helper expectations; update the daily cron prompt, Brain, changelog, skills, and durable memory; create or update Lucas-facing usage guidance for new features; re-run the `Lucas Brain daily intelligence loop`; then report both what was implemented and what Lucas should learn.
11. Standardize watchers with the silent contract: `rc=0` + empty stdout means healthy; `rc=0` + stdout means actionable alert; `rc!=0` means watchdog failure. Watchers must be read-only/sanitized unless explicitly approved otherwise, and should avoid cron sprawl by inventorying existing checks before creating new jobs.
11. For medium/high-risk improvements, ask Lucas with a short decision brief: benefit, risk, blast radius, backup/rollback, and recommendation. When supported, use `clarify` buttons with options like Approve scope / Adjust / Preview only / Block, but only after the exact scope, payload, risk, rollback, and exclusions are shown inline. Button/text approval applies only to the inline scope and never silently expands to Docker/host, source-of-truth data writes, external sends, money, customers, secrets, destructive actions, or new items not shown inline. For A3/A4, restate the exact scope/payload/rollback inline before write if the prior surface was incomplete or file-path-only.
12. For runtime updates:
   - prepare in parallel first;
   - preserve local patches such as context-compression retry;
   - run smoke tests;
   - produce rollback plan;
   - request explicit approval before swapping containers/restarting gateway.
13. Deliver a concise report to Lucas: what changed, what was implemented into day-to-day, what Lucas needs to learn/do manually, what is recommended next, what needs approval. If the run produced LK approval packets or decision artifacts, do not ask for approval by pointing to local files only; include the actual decision text/options inline in Telegram, and audit/supersede stale approval surfaces first when many artifacts exist.

## LK-specific priorities
- `/goal` for long tasks that previously required repeated “seguir”. Teach Lucas when/manual use after the runtime supports it.
- Multi-Agent Kanban board for LK Growth Ops / Mission Control, starting with statuses: Backlog, Doing, Waiting Lucas, Waiting External, QA, Done.
- Shopify Admin + Storefront GraphQL optional skill, initially read-only.
- `no_agent` cron watchdogs for APIs, reports, Cloudflare email delivery, and attribution gaps.
- Dashboard only local/SSH first; no public exposure without hardening approval.
- Cloudflare Email Sending with real LK/Klaviyo visual layout after visual approval.
- Release catch-up is not limited to the latest release: while catching up, review v0.10, v0.11, v0.12, v0.13, and latest for delayed-use features.

## Manual teaching backlog
When these features become available in the active runtime, teach Lucas:
- `/goal`: use for long missions that should persist across turns; expected output is a durable objective/checklist; failure sign is generic state or repeated context requests.
- Kanban: use for LK Growth Ops tasks with explicit owner/status/next step; failure sign is loose chat-only task tracking.
- `/background` or `/btw`: use for long research/audit/review while the main conversation continues.

## Approval backlog
Ask Lucas before executing:
- Any future Hermes runtime swap/restart/container/compose/image change after v0.13.
- Public dashboard exposure.
- Shopify writes or permission expansion beyond read-only.
- Cloudflare weekly report migration that sends real external email or changes the live cron.

## Current runtime note after 2026-05-16
- Production is Docker-first on Hostinger project `/docker/hermes-agent-5ajw`.
- Active image after Lucas-approved v0.14 update: `hermes-agent-custom:v0.14.0-20260516` on both dashboard and Telegram containers.
- Active version: `Hermes Agent v0.14.0 (2026.5.16)`.
- The deploy-v2 incident during the earlier v0.13 work was caused by a smoke-test script using bare `python` in the container; the correct interpreter for Docker smoke tests is `/opt/hermes/.venv/bin/python` or `python3`.
- Daily continuous-improvement cron `f5a23dd6a1bd` is now `Lucas Brain daily intelligence loop`, updated to treat v0.14 as expected production and to forbid future Docker/runtime swaps without explicit current approval.
- Reference: `references/v014-watchdog-reconciliation-20260516.md` captures the safe pattern for reconciling stale watchdog/helper expectations after an approved Hermes runtime upgrade.
- 2026-05-11/12 daily run lesson: the cron execution context may be inside the Hermes container without access to `/var/run/docker.sock`; `docker ps`/`docker logs` can fail even though the gateway runtime is healthy. In that case, do not claim container images/logs were verified. First use the approved autonomous A1 pattern: Doppler-backed, read-only SSH/host/Docker observability with sanitized output and no mutation. If that helper is unavailable or fails, fall back to `/opt/hermes/.venv/bin/hermes --version`, `hermes config path/check`, `hermes status --all`, `hermes cron status/list`, and existing `no_agent` watchdog scripts. Only host/socket/permission/compose/restart changes require approval with plan + rollback; read-only observability itself should not be treated as approval-needed.
- 2026-05-12 daily run lesson: `hermes status --all` is useful but may print API-key fragments or full values for some providers in stdout. Use it for internal diagnosis only; never paste raw output into final reports or Brain artifacts. Summarize sanitized status instead. Also treat `hermes cron status`/`hermes status --all` reporting “gateway stopped” with caution when the cron itself is running and gateway logs show recent Telegram activity — record it as a detector/runtime discrepancy until Docker/host observability confirms the real state.
- 2026-05-12 approved correction: Lucas approved fixing the Docker observability gap. Use `/opt/data/scripts/hermes_host_docker_observability.py --output /opt/data/hermes_bruno_ingest/hermes-brain/reports/hermes-host-docker-observability-YYYY-MM-DD.json` before local fallbacks in the daily run. The helper uses SSH to lc.vps, performs only read-only Docker/Hermes checks, sanitizes output, and must not restart, mutate Docker/compose/gateway, alter SSH/root, or print secrets. Prefer the installed SSH key `/opt/data/hermes_bruno_ingest/ssh_keys/hermes_lc_vps_ed25519`; Doppler/password is fallback only if the key is unavailable. If it fails, report the gap and request a fresh plan for any access/infra change. 2026-05-13 pitfall: the helper can exist and run but still fail SSH authentication with sanitized `Permission denied`/`rc=255`; in that case save/report the helper JSON, run local fallback checks (`hermes --version`, config, cron, API `/health`, watchdogs, gateway log), and classify the remaining issue as “helper auth/access gap”, not as Docker/runtime failure or permission to reset SSH/root. 2026-05-14 follow-up: the helper can later succeed without runtime changes in the cron; when it does, treat the host Docker observability gap as closed for that run and record the confirmed container names/images/versions from the sanitized JSON, while still avoiding Docker/compose/gateway mutations. 2026-05-15 pitfall: the helper JSON is intentionally sanitized and may not include generic `success`/`ok` keys; treat successful execution, populated `containers`, `versions_sanitized`, `cron_status_sanitized`, and empty `alerts` as the health signal rather than requiring a boolean field. Cron counts can legitimately increase as LK mandatory reports/other jobs are added; report the current count from live output and do not frame a changed count as drift unless a required job is missing or unexpected dangerous job appears. 2026-05-16 follow-up: when the helper confirms expected containers/images/versions, `hermes cron status` reports the gateway scheduler running, `/health` returns `200`/`ok`, and watchdog scripts return `rc=0` with empty stdout/stderr, classify transient Telegram network warnings (`TimedOut`, fallback IP, `RemoteProtocolError`) as monitor-only rather than an incident, provided the helper `alerts` array is empty and there is no persistent startup failure evidence. Also, new Mordomo/Zipper crons can raise the active job count (e.g. 14 jobs) without implying drift; enumerate critical LK/Hermes jobs and only flag missing required jobs or unexpected dangerous jobs.

Additional 2026-05-16 intraday release lesson: GitHub releases can change after the 02:00 BRT run. If a same-day re-run finds a new release (e.g. `v2026.5.16` / Hermes v0.14.0 published 09:59 UTC), update the daily report/changelog and create a decision brief, but do not update Docker/runtime/gateway automatically. For v0.14, specifically classify `/handoff`, `/subgoal`, watchers skill, clarify buttons, file-mutation verifier, LSP diagnostics, API approval events, plugin `ctx.llm`, MCP parallel calls, browser/CDP speedups, prompt cache, local OpenAI-compatible proxy, and gateway circuit breakers.

Additional 2026-05-16 same-day reconciliation lesson: a daily report can become stale within hours when Lucas approves or completes an upgrade after the morning run. In any later same-day rerun, treat the live read-only checks as current source of truth, then supersede/update earlier artifacts that still describe the old state. Specifically: re-run host Docker observability first, compare against the report/changelog/decision brief, rewrite the daily `reports/hermes-continuous-improvement/YYYY-MM-DD.md` as the live report for the day, update the top `CHANGELOG.md` entry, and mark pre-upgrade decision briefs as `histórico/superseded` instead of leaving contradictory v0.13/v0.14 claims. Do not treat this artifact reconciliation as runtime mutation; it is Brain hygiene. Still do not restart/swap Docker/gateway/host or create new productive crons without explicit approval.

## Current catch-up artifacts
- `/opt/data/hermes_bruno_ingest/hermes-brain/reports/hermes-release-catchup-2026-05-10/action-matrix.md`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/rotinas/hermes-v013-operacionalizacao.md`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/rotinas/hermes-v013-watchdogs-no-agent.md`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/scripts/hermes_runtime_cron_watchdog.py` — source copy of the read-only `no_agent` runtime/cron watchdog. Lucas approved activation on 2026-05-10; executable copy lives at `/opt/data/scripts/hermes_runtime_cron_watchdog.py`; cron job `edd06fe19397` runs every 30 minutes with `no_agent=True`, silent on OK. Cron script paths are relative to `/opt/data/scripts/` in this runtime; absolute paths are rejected.
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/scripts/hermes_artifacts_freshness_watchdog.py` — source copy of the read-only `no_agent` freshness watchdog for v0.13 operational artifacts; executable copy lives at `/opt/data/scripts/hermes_artifacts_freshness_watchdog.py`; cron job `e7a61e275c37` runs daily at 09:00 BRT (`0 12 * * *`), silent on OK.
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/rotinas/hermes-v013-kanban-lk-growth-ops.md` — live board `lk-growth-ops` was created in safe mode with 7 unassigned cards; no workers/daemon/dashboard exposure without Lucas approval.
- `/opt/data/scripts/zipper_os_cockpit.py` — approved Zipper OS read-only/draft-only cockpit. It writes sanitized daily artifacts under `reports/zipper-os-executive-inbox-followups-YYYY-MM-DD.*`, reads Gmail/Supabase through Doppler without printing secrets, never sends externally, and has two wrappers: `zipper_os_cockpit_daily.sh` (daily summary) and `zipper_os_cockpit_watchdog.sh` (Silent OK alerts). Active crons after 2026-05-16 approval: `f00c68f5967a` daily 08:15 BRT and `af07bbc077b8` every 30 min.
- 2026-05-16 Mission Control correction: Lucas explicitly corrected that v0.12-v0.14 operating improvements must be implemented in the existing Mission Control, not as a parallel cockpit. Before proposing Shopify work, verify installed skills first; `lk-shopify-readonly` and `lk-shopify-product-upload` already exist and are mirrored into the Brain. Mission Control is now the central surface for `/goal`/`/subgoal`, structured approval buttons, executive Kanban lanes, cron/watchdog registry, `context_from`/QA guidance, and Shopify skill state. Active no_agent watchdog: `feec299b99e5` (`mission_control_ops_watchdog.py`) every 15 minutes, silent on OK. Reference: `references/mission-control-v014-operationalization-20260516.md`.
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/rotinas/hermes-approval-learning-loop.md` — learning loop for Lucas approvals/corrections: record durable approvals in decisions, lessons, pending and, when procedure changes, patch the relevant skill. Current lessons: Docker-awareness, `approvals.mode: off` does not remove guardrails, Kanban workers require restricted profiles, and manual dispatcher should use the PATH wrapper when needed.

## References
- `references/hermes-013-staged-upgrade-20260510.md` — staged-upgrade lesson from the Hermes 0.12 → 0.13 preparation: non-git runtime, parallel clone, context-compression retry preservation, targeted tests, and production-swap guardrails.
- `references/no-agent-post-run-recheck-pattern.md` — one-shot `no_agent` post-run recheck pattern for newly created/changed crons: stay silent before/when healthy, alert only on missing/stale/failed run evidence.
- `references/host-docker-observability-helper-20260512.md` — approved read-only Doppler+SSH helper pattern for daily Hostinger Docker observability when the container lacks `/var/run/docker.sock`, including pitfalls and verification.
- `references/v012-v014-opportunity-review-20260516.md` — release-window opportunity matrix for translating Hermes v0.12/v0.13/v0.14 features into Lucas operating habits: `/goal` + `/subgoal`, structured approval buttons, `no_agent` watchers, Kanban board, cron `context_from`, read-only `x_search`/browser intelligence, and approval-needed boundaries for Shopify/Teams/proxy.

## Verification checklist
- `hermes --version` captured.
- Release source URL captured.
- No secrets in outputs/artifacts.
- Low-risk changes tested or linted.
- Runtime changes have backup/rollback.
- Brain/skills updated for durable lessons.
