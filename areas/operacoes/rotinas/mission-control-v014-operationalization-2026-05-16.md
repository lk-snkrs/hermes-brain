# Mission Control v0.14 operationalization — 2026-05-16

Status: implemented, validated, and deployed to Mission Control production (`https://mission.lucascimino.com`).
Generated at: 2026-05-16T12:25:33Z

## Lucas corrections applied

1. Mission Control is the operating surface. New Hermes v0.12-v0.14 rituals are represented there, not as detached notes.
2. Shopify was verified before planning: `lk-shopify-readonly` and `lk-shopify-product-upload` exist in runtime; the Brain mirror was synchronized from runtime to prevent drift.
3. Approval buttons are the standard for A3/A4: **Aprovar escopo**, **Ajustar**, **Preview only**, **Bloquear**. Approval applies only to the inline payload, risk, rollback and exclusions.
4. Autonomy increased for A0/A1/A2: read-only checks, local docs, Mission Control code, skill sync, reports, QA and silent watchers can be executed without asking when reversible and non-external.
5. Watchers expanded using the silent contract: `rc=0` + empty stdout is healthy; stdout means actionable alert.

## Mission Control changes

- Added v0.14 operating rituals: `/goal`, `/subgoal`, approval buttons, `context_from`, QA mandatory before recurring jobs.
- Added watcher registry: runtime/cron, Mission Control, Zipper OS, Mordomo, LK mandatory reports.
- Added Shopify skill state: read-only skill and product-upload skill are separate and already installed.
- Updated cron timeline to show actual/no_agent watchdogs and critical recurring jobs.
- Updated domain ledger to reflect Mission Control as the central COO board.

## Watchdog added

- Runtime executable: `/opt/data/scripts/mission_control_ops_watchdog.py`
- Brain source: `scripts/mission_control_ops_watchdog.py`
- Cron job: `feec299b99e5` — `Mission Control ops watchdog silent`, every 15 minutes, `no_agent=True`, silent on OK.
- Scope: read-only public Mission Control GET, local artifact existence, Shopify runtime-vs-Brain skill drift.
- Non-actions: no Docker, no Vercel mutation, no Shopify/Tiny/Merchant write, no email/WhatsApp/campaign, no secrets.

## Shopify verification

[
  {
    "name": "lk-shopify-readonly",
    "src_exists": true,
    "dst_exists_before": true,
    "dst_exists_after": true,
    "skill_md_bytes": 32321,
    "references": 21
  },
  {
    "name": "lk-shopify-product-upload",
    "src_exists": true,
    "dst_exists_before": true,
    "dst_exists_after": true,
    "skill_md_bytes": 13768,
    "references": 2
  }
]

## Approval model in Mission Control

Every sensitive package should surface inline:

- payload exact;
- risk/blast radius;
- rollback;
- exclusions;
- buttons: Approve scope / Adjust / Preview only / Block.

A0/A1 work should proceed autonomously when read-only/local/reversible. A3/A4 remains blocked until current explicit approval.
