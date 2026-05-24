# Hermes v0.12–v0.14 opportunity review for Lucas/Cimino

Session date: 2026-05-16
Source: GitHub Releases for NousResearch/hermes-agent plus local production state.

## Durable lesson

After a runtime catch-up/update, the highest-value work is often not another deploy. It is converting new Hermes mechanisms into Lucas's operating layer: rituals, approval surfaces, watchers, boards, and cron context flows.

## Release window recap

### v0.12 — Curator / self-improvement / skills / cron chaining

Useful features:
- Autonomous Curator for skill grading, consolidation, pruning, and reports.
- Improved self-improvement fork: class-first rubric, active-skill update bias, support for `references/` and `templates/`, scoped to memory/skills.
- Cron `workdir` and `context_from` for project-aware and chained scheduled jobs.
- Skill ecosystem additions: Humanizer, claude-design, design-md, Airtable, ComfyUI, TouchDesigner.
- Prompt-cache and cold-start improvements.

Adoption pattern for Lucas:
- Treat Curator status as a hygiene signal, not a substitute for active skill patching during the session.
- Use `context_from` where one scheduled output is a clear input to another; avoid propagating stale context blindly.
- For Lucas-facing copy/visual artifacts, consider Humanizer/design skills in preview-only workflows.

### v0.13 — Tenacity / Kanban / goal / no_agent / security

Useful features:
- Durable multi-agent Kanban with heartbeat, reclaim, zombie detection, retries.
- `/goal` for persistent long-running objectives.
- `no_agent` cron mode for script-only watchdogs; stdout empty means silent OK.
- Checkpoints v2 and auto-resume after gateway restart.
- Post-write lint for `write_file`/`patch`.
- Security wave: redaction default in the release, allowlists, WhatsApp stranger rejection, prompt-injection scan in cron.
- Optional Shopify skill.

Adoption pattern for Lucas:
- Use `/goal` for long missions that otherwise lead to repeated “seguir”.
- Start Kanban as an executive/manual board first; workers/daemon/public dashboard need separate approval.
- Convert mechanical checks to `no_agent` watchdogs instead of LLM cron jobs.
- Shopify skill should start read-only; any write scope is A3/A4.

### v0.14 — Foundation / handoff / subgoal / buttons / verifier / watchers

Useful features:
- `/handoff` transfers a live session to another model/persona/profile.
- `/subgoal` adds success criteria to an active `/goal`.
- `clarify` renders native buttons on Telegram/Discord.
- Per-turn file-mutation verifier and LSP semantic diagnostics on writes.
- Watchers skill for RSS/HTTP JSON/GitHub polling via `no_agent`.
- Browser/CDP speedup, `vision_analyze` pixel passthrough, `x_search`, API approval events.
- OpenAI-compatible local proxy and Microsoft Graph/Teams foundation.

Adoption pattern for Lucas:
- Use `/goal` + `/subgoal` as the default for broad missions.
- Use structured buttons only with inline scope, payload, risk, rollback, and exclusions.
- Keep expanding silent watchers where checks are objective/read-only.
- Use `x_search`/fast browser for read-only social, market, SERP, artist/fair, and competitor intelligence.
- Treat local proxy, public API exposure, Graph/Teams productive wiring, and Shopify writes as separate approval-needed plans.

## Priority matrix

P0 — should become operating habit:
1. `/goal` + `/subgoal` for long missions.
2. Structured Telegram approvals with buttons and full inline decision packet.
3. Silent `no_agent` watchers for objective health/change checks.

P1 — implement as Brain/Ops workflows:
1. Lucas Ops Board: multiempresa Kanban without automatic workers initially.
2. Cron context chaining with `context_from` for related daily/weekly loops.
3. Read-only social/listening/research using `x_search` and faster browser tools.
4. QA discipline for scripts promoted to cron: syntax/lint/smoke, silent-OK contract, no secrets.

P2 — explore only with separate scoped approval:
1. Shopify skill read-only first.
2. Teams/Graph meeting pipeline only if Teams is a real source.
3. OpenAI-compatible local proxy only local/SSH first; no public exposure without hardening/rollback.

## Recommended response pattern for future release reviews

When Lucas asks “what can we improve from recent Hermes releases?”, do not only summarize release notes. Produce:
- what changed by release;
- what is already adopted locally;
- what is missing operationally;
- P0/P1/P2 opportunity matrix;
- what is safe to apply now vs what needs approval;
- Brain/skill updates if a durable workflow emerged.
