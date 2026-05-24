# Hermes Skills Legacy/Safety Audit — 2026-05-22

## Summary
- Skill/runtime-support files scanned: `1361`.
- Findings requiring review after P2 patches: `0`.
- Rules: `{}`.

## Interpretation
- Findings are review flags, not proof of live unsafe behavior.
- Lines with explicit legacy/dry-run/approval/blocking/spike/bootstrap context are ignored.
- Brain strict-runtime guard is the enforcement gate for Brain-local skills; this report covers broader `/opt/data/skills` too.

## P2 patches applied
- `skills/lk-crosssell/SKILL.md`: replaced legacy `cerebro-cimino` wording with Hermes Brain/Cérebro Cimino canonical wording.
- `hermes-agent` workspace spike/cleanup references: added isolated-spike / not-production banners.
- `hostinger-vps-api-ssh-access` SSH bootstrap reference: added root-bootstrap approval banner.
- `lucas-hermes-continuous-improvement` workspace handoff: added isolated-spike banner.

## Remaining review findings

No uncontextualized legacy/safety findings remain under scanned skill paths after P2 contextual patches.

## Recommended policy
- Keep skills procedural and current; move historical receipts to Brain reports with `HISTÓRICO / NÃO EXECUTAR` banners.
- Any skill that authorizes Docker/VPS/external writes must require plan, rollback, and explicit Lucas approval.
- Re-run this audit after installing/updating high-privilege skills.
