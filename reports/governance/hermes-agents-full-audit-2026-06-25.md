# Hermes agents full audit — 2026-06-25

Generated at: `2026-06-25T19:08:15.094413+00:00`

## Executive verdict

**Não está 100% OK.** A base dos agentes está majoritariamente saudável, mas o audit encontrou **2 problemas reais** e **1 hardening recomendado**:

1. **P1 — Cron ativo com falha atual:** `Zipper post-PDF follow-up watchdog` (`a97a6317b197`) está ativo, roda a cada 30m e o último run falhou tentando envio WhatsApp com `server returned error 463`.
2. **P2 — `brain-process` dormant com auth expirado:** smoke read-only falhou com `HTTP 401 token_expired`. Não afeta gateways ativos, mas afeta esse worker quando chamado.
3. **P2 hardening — secondary gateways têm API/webhook desligados, mas herdaram `HERMES_WEBHOOK_SECRET` no env.** Não há superfície exposta (`WEBHOOK_ENABLED=false`, `API_SERVER_KEY=false`), mas vale limpar herança em launchers/watchdogs para reduzir exposição em `/proc`.

## What is OK

| Area | Result |
|---|---:|
| Profiles audited | 17 |
| `AGENTS.md` with Task OS marker | 17/17 |
| `SOUL.md` with Task OS marker | 16/16 non-default profiles |
| Document/identity issue count | 0 |
| Real gateway processes | 12 across 12 homes |
| Brain health | PASS (`FAIL=0 WARN=0`) |
| Kanban diagnostics | `[]` |
| Kanban running tasks | `[]` |
| Secret scan on audit/profile identity artifacts | 0 high-confidence hits |
| Support identity smokes | 3/4 OK |

## Runtime gateways

Real live gateways detected by exact Python/Hermes process + `HERMES_HOME`:

| Home/Profile | PID | API enabled | API key | Webhook enabled | Webhook secret in env | Telegram token | Max iter |
|---|---:|---|---:|---|---:|---:|---:|
| `default` | 1 | true | True | true | True | True | 90 |
| `mordomo` | 208 | false | False | false | True | True | 60 |
| `spiti` | 227 | false | False | false | True | True | 60 |
| `spiti-atendimento` | 302 | false | False | false | True | True | 55 |
| `lk-growth` | 66782 | false | False | false | True | True | 60 |
| `lk-ops` | 66825 | false | False | false | True | True | 40 |
| `lk-shopify` | 66830 | false | False | false | True | True | 50 |
| `lk-trends` | 66920 | false | False | false | True | True | 45 |
| `lk-collection-optimizer` | 67045 | false | False | false | True | True | 50 |
| `lk-stock` | 67157 | false | False | false | True | True | 50 |
| `lk-finance` | 67362 | false | False | false | True | True | 50 |
| `lk-content` | 67495 | false | False | false | True | True | 60 |


Interpretation:

- `default` is the only public API/webhook surface expected here.
- Specialist gateways are live with API/webhook disabled.
- The env still contains webhook secret material in secondary processes; not exposed, but should be cleaned in a hardening pass.

## LK identity / LKGOC status

The profile documentation audit found `issue_count=0` for LK identity files.

Critical check:

- `lk-collection-optimizer/SOUL.md` heading is `[LK] Otimização de Coleções / LKGOC — Hermes Specialist`.
- No LKGOC→Growth heading contamination was detected.
- LK support smokes confirmed:
  - `lk-analyst-readonly`: OK, identity = LK Analyst Readonly.
  - `lk-content-reviewer`: OK, identity = LK Content Reviewer.

## Support smoke results

| Profile | Status | Return code | Note |
|---|---:|---:|---|
| `lk-analyst-readonly` | ok | 0 | session_id: 20260625_190249_4a1c9b |
| `lk-content-reviewer` | ok | 0 | session_id: 20260625_190305_5518dc |
| `hermes-ops-readonly` | ok | 0 | session_id: 20260625_190322_61a0f2 |
| `brain-process` | error | 1 | Error: HTTP 401: Provided authentication token is expired. Please try signing in again.  session_id: 20260625_190339_8a0ade |


`brain-process` failed because its profile auth is expired. I did **not** copy credentials into it during this audit because that touches auth secrets and should be approved separately.

## Kanban / Task OS

From `hermes kanban --board hermes-task-os`:

```json
{
  "by_status": {
    "blocked": 3,
    "done": 5
  },
  "by_assignee": {
    "hermes-ops-readonly": {
      "done": 1
    }
  },
  "oldest_ready_age_seconds": null,
  "now": 1782414163
}
```

Status:

- Diagnostics: empty.
- Running cards: empty.
- Notify subscriptions: none.
- Backlog remains blocked/unassigned as expected.

## Cron/runtime finding

Cron registry summary:

```json
{
  "total": 44,
  "active": 40,
  "paused": 4,
  "other_statuses": {},
  "last_non_ok": [
    {
      "id": "a97a6317b197",
      "status": "active",
      "last_status": "1",
      "name": "Zipper post-PDF follow-up watchdog",
      "last_run": "2026-06-25T18:58:15.164169+00:00  error: Script exited with code 1"
    }
  ],
  "values_printed": false
}
```

The non-ok job is current and actionable:

```text
Zipper post-PDF follow-up watchdog — a97a6317b197
Last run: 2026-06-25T18:58:15Z error: Script exited with code 1
stdout showed send_failed with server returned error 463 for two WhatsApp follow-up candidates.
```

Output evidence:

```text
/opt/data/cron/output/a97a6317b197/2026-06-25_18-58-15.md
```

This is the main reason the answer is **not fully OK**.

## Recommended next actions

1. **P1: decide what to do with `a97a6317b197`.** Options:
   - pause the cron until WhatsApp send path is fixed; or
   - convert it to preview/dry-run only; or
   - repair the sender error 463 with a scoped Zipper/Mordomo approval packet.
2. **P2: repair `brain-process` auth** using the same backed-up credential-pool sync pattern used for LK support profiles.
3. **P2 hardening: patch secondary gateway launchers/watchdogs** to clear `WEBHOOK_SECRET/HERMES_WEBHOOK_SECRET` from specialist envs when `WEBHOOK_ENABLED=false`, then restart only affected profiles after scoped approval.

## Evidence artifacts

- Raw audit dir: `/opt/data/backups/hermes-agents-audit-20260625T190037Z`
- Profiles audit: `/opt/data/backups/hermes-agents-audit-20260625T190037Z/profiles_audit.json`
- Real gateway processes: `/opt/data/backups/hermes-agents-audit-20260625T190037Z/real_gateway_processes.json`
- Support smokes: `/opt/data/backups/hermes-agents-audit-20260625T190037Z/support_identity_smokes.json`
- Cron summary: `/opt/data/backups/hermes-agents-audit-20260625T190037Z/cron_summary.json`
- Brain health: `/opt/data/backups/hermes-agents-audit-20260625T190037Z/brain_health.txt`
- Secret scan summary: `/opt/data/backups/hermes-agents-audit-20260625T190037Z/secret_scan_summary.json`

## Conclusion

The core agent system, Task OS propagation, LK identity alignment, active gateways, Brain health and Kanban are OK. But the system is **not clean-green** because one active cron is failing on a real external-send path, and one dormant support profile has expired auth.
