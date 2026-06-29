# Hermes Central Integration Auth Broker — Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task after Lucas approves runtime/code changes.

**Goal:** Implement a central, Doppler-first, audited integration auth broker so agents stop authenticating Shopify CLI/MCP/CLI individually.

**Architecture:** Keep Hermes profiles isolated for memory/config/skills, but route sensitive integration access through a central broker (`hermes-cli-run`) backed by Doppler and a controlled CLI auth home. Do not symlink/copy `.env`, `auth.json`, OAuth caches, or MCP tokens across profiles.

**Tech Stack:** Python 3, existing `/opt/data/scripts/hermes_cli_run.py`, `/opt/data/scripts/hermes_doppler.py`, Hermes profile policies/skills, Brain receipts, shell read-only smoke commands.

---

## Approval boundary

This plan contains runtime/code changes and must not be executed without separate scoped approval. Safe documentation already created:

- PRD: `reports/governance/hermes-central-integration-auth-broker-prd-2026-06-28.md`
- Plan: `areas/operacoes/implementation-plans/hermes-central-integration-auth-broker-2026-06-28.md`

## Task 1: Create pre-change backup and inventory

**Objective:** Capture safe rollback artifacts and current integration status.

**Files:**
- Read: `/opt/data/scripts/hermes_cli_run.py`
- Create: `/opt/data/backups/hermes-cli-run-pre-auth-broker-YYYYMMDDTHHMMSS.py`
- Create: `reports/governance/hermes-central-integration-auth-broker-inventory-YYYYMMDD.md`

**Steps:**

1. Copy `/opt/data/scripts/hermes_cli_run.py` to timestamped backup.
2. Run read-only inventory:

```bash
/opt/data/home/.local/bin/hermes-cli-integrations inventory
/opt/data/home/.local/bin/hermes-cli-integrations smoke shopify_lk github notion google_workspace klaviyo supabase
```

3. Record only status, integration names, exit codes, `values_printed=false`.
4. Secret scan the report.

**Expected:** inventory report exists; no secret values printed.

## Task 2: Add registry shape to `hermes_cli_run.py`

**Objective:** Replace ad-hoc alias-only behavior with declarative integration metadata while preserving existing behavior.

**Files:**
- Modify: `/opt/data/scripts/hermes_cli_run.py`
- Test: local smoke commands only.

**Design:**

Add a registry containing:

- env aliases;
- denied subcommands;
- write/mutation patterns;
- lock key;
- default mode read-only;
- redaction patterns.

Initial denied commands:

```text
shopify login
shopify auth
shopify store auth
hermes mcp login
```

**Expected:** existing read-only commands still work; denied commands return `policy_blocked` without executing.

## Task 3: Add lock per integration

**Objective:** Prevent concurrent CLI state/cache corruption.

**Files:**
- Modify: `/opt/data/scripts/hermes_cli_run.py`
- Create directory at runtime: `/opt/data/runtime/locks/integrations/`

**Steps:**

1. Use `fcntl.flock` around integrations marked `requires_lock=true`.
2. Lock Shopify per store key, e.g. `shopify_lk`.
3. Timeout gracefully with sanitized error.

**Expected:** concurrent calls serialize; no deadlock; lock files contain no secrets.

## Task 4: Add audit JSON output

**Objective:** Make receipts and smokes easier without leaking output.

**Files:**
- Modify: `/opt/data/scripts/hermes_cli_run.py`

**Add flag:**

```bash
hermes-cli-run --audit-json shopify store execute ...
```

**Audit fields:**

```json
{
  "integration": "shopify",
  "command_family": "store execute",
  "mode": "read_only",
  "exit_code": 0,
  "status": "ok",
  "values_printed": false,
  "secret_values_printed": false
}
```

**Expected:** stdout/stderr remain sanitized; audit contains no token previews.

## Task 5: Enforce Shopify mutation gate

**Objective:** Ensure Shopify writes cannot happen accidentally.

**Files:**
- Modify: `/opt/data/scripts/hermes_cli_run.py`

**Rules:**

- GraphQL containing `mutation` is blocked unless `--allow-mutations` is present.
- If `--allow-mutations` is present, require env/flag indicating approved approval packet ID/path.
- Even approved mutations must still redact output.

**Expected:** mutation without approval is blocked locally before network execution.

## Task 6: Detect direct-login drift in skills/scripts/crons

**Objective:** Find places that still tell agents to login individually.

**Files:**
- Search paths:
  - `/opt/data/skills/`
  - `/opt/data/hermes_bruno_ingest/hermes-brain/`
  - `/opt/data/scripts/`
  - profile cron dirs under `/opt/data/home/.hermes/profiles/` or active profile roots if applicable.

**Search patterns:**

```text
shopify login
shopify store auth
hermes mcp login
mcp login
SHOPIFY_ACCESS_TOKEN
shopify-admin-graphql
```

**Expected:** drift report with each match classified as canonical/fallback/exception/stale.

## Task 7: Update canonical policy docs/skills

**Objective:** Propagate the central broker contract.

**Files:**
- Modify: `areas/operacoes/rotinas/cli-mcp-first-integration-policy.md`
- Patch relevant Shopify/LK skills only after reading them.
- Do not patch profile-specific files outside active/default without explicit direction.

**Expected:** all docs say agents use broker, not individual login.

## Task 8: Verification suite

**Objective:** Prove behavior with real commands.

**Commands:**

```bash
/opt/data/home/.local/bin/hermes-cli-run shopify store execute --store lk-sneakerss.myshopify.com --json --query '{ shop { name myshopifyDomain } }'
/opt/data/home/.local/bin/hermes-cli-run shopify store execute --store lk-sneakerss.myshopify.com --json --query 'mutation { __typename }'
/opt/data/home/.local/bin/hermes-cli-integrations smoke shopify_lk
```

**Expected:**

- Read-only Shopify smoke OK.
- Mutation blocked without `--allow-mutations`.
- `values_printed=false`.
- No external writes.

## Task 9: Receipt and rollout gate

**Objective:** Close the implementation with evidence and decide if gateway restart is needed.

**Files:**
- Create receipt: `areas/operacoes/receipts/hermes-central-integration-auth-broker-YYYYMMDD.md`
- If prompts/runtime changed and gateway restart is required, create approval packet; do not restart without approval.

**Expected:** receipt contains rollback path, smokes, files changed, and `values_printed=false`.
