# Ecosystem learning propagation — 2026-06-15

## Rule

Corrections from Lucas are not complete when saved only in memory or a single agent response. Durable learning must be encoded in the execution surface that can repeat the behavior.

## Required propagation surfaces

- Runtime profile `AGENTS.md` for every agent that can repeat the error.
- Canonical Brain `AGENTS.md` / sub-area docs that govern the workflow.
- Relevant default/profile-local skills.
- Cron prompt/checklist/report template when the behavior is scheduled.
- Script, validator, test, or guard when the behavior can be mechanically checked.
- Handoff/receipt contract when another agent must continue the work.

## Verification

Every propagation must end with a count/search verification and a scoped report: what changed, where, backups, and which external/prod systems were not touched.
