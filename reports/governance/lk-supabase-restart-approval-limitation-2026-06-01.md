# LK Supabase incident — restart approval / execution limitation — 2026-06-01

Generated at: `2026-06-01T19:22:24.337648+00:00`

Lucas selected option `2`, interpreted as controlled Supabase restart/recovery for project `cnjimxglpktznenpbail` (`LK Sneakers Db`).

## Verification before execution

Supabase Management OpenAPI was checked for an official project/database restart endpoint. The current OpenAPI exposes project pause/restore and backup restore operations, but no explicit database restart endpoint was found.

Because backup restore / project restore are not equivalent to a controlled restart and can be destructive or materially change state, they were not used.

## State

- `LK - Envio de Email Novo Produto` remains paused from the prior containment step.
- `LK POS → WhatsApp Thank You` must remain active per Lucas's instruction.
- No Supabase restart/restore/upgrade was executed from Hermes.

## Required operator action

Use Supabase Dashboard for the controlled recovery action:

1. Open Supabase Dashboard.
2. Project: `LK Sneakers Db` / `cnjimxglpktznenpbail`.
3. Open Database / Settings / Infrastructure / Compute area or Database Health recommendations.
4. Use the dashboard-supported Restart/Recovery action if offered.
5. Avoid backup restore/PITR unless explicitly intended as data restore.

After restart, run the read-only SQL/REST health probe and then collect `pg_stat_activity`, `pg_stat_statements`, relation sizes, and dead tuple stats.
