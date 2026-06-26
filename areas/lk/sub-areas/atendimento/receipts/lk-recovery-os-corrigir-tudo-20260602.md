---
title: lk-recovery-os corrections after Superpowers audit
created_at_utc: 2026-06-02
area: lk/atendimento
repo: https://github.com/lk-snkrs/lk-recovery-os
branch: feat/chatwoot-provider-internal
status: local_verified_not_deployed
---

# lk-recovery-os — corrigir tudo

## Scope

Lucas asked to correct all issues found in the `lk-recovery-os` Chatwoot/internal-only migration.

Local repo:

```text
/opt/data/lk-recovery-os
```

Branch:

```text
feat/chatwoot-provider-internal
```

## Production safety

No deploy.
No push/PR.
No Cloudflare config mutation.
No Shopify write.
No Chatwoot live API call.
No WhatsApp/customer-visible message.
No secret written.

## Fixes completed

### 1. Chatwoot contact idempotency

Problem: provider always created a contact, which could duplicate contacts on replay/manual rerun if Chatwoot already had the LK identifier.

Fix:

```text
GET /contacts/search?q=<lk-recovery:checkout_id>
if exact identifier exists: PATCH /contacts/{id}
else: POST /contacts
```

File:

```text
workers/recovery-os/src/chatwoot.ts
```

Regression:

```text
workers/recovery-os/tests/chatwoot.test.ts
```

### 2. Preserve provider success if Supabase success-patch fails

Problem: Chatwoot side effect could succeed, then the success patch to `recovery_messages` could fail and be treated like Chatwoot failed. That could misreport a real internal context as failed.

Fix:

```text
reserve recovery_messages pending_internal_context
call Chatwoot
if Chatwoot fails: patch failed + audit
if Chatwoot succeeds: try success patch; if patch fails, audit patch failure but keep context in summary
```

File:

```text
workers/recovery-os/src/t1.ts
```

### 3. Failure-patch now fail-closed without aborting whole tick

Problem: in the Chatwoot failure path, if patching `recovery_messages` to failed also failed, the catch block could throw and abort the tick.

Fix: wrap failure patch in its own try/catch and write an audit breadcrumb.

### 4. Existing previous fixes retained

- Chatwoot contact create includes required `inbox_id`.
- Contact parser handles payload array / nested contact / top-level id.
- Operational metadata uses `additional_attributes`.
- GitHub Action manual default is `dry_run=true`.
- Worker defaults remain internal-first and customer-facing sends disabled.
- README documents legacy live path as historical only.

## Fresh verification

### Worker TypeScript

```bash
cd /opt/data/lk-recovery-os/workers/recovery-os && npm test && npx tsc --noEmit
```

Result:

```text
6 test files passed
46 tests passed
TypeScript typecheck exit 0
```

### Python

```bash
cd /opt/data/lk-recovery-os && uv run pytest -q
```

Result:

```text
155 passed, 1 warning
```

### Diff hygiene

```bash
git diff --check
```

Result: exit 0.

### Risk scan

Checked for:

```text
LK_RECOVERY_DRY_RUN=false
LK_LIVE_SEND_ENABLED=true
LK_WHATSAPP_SEND_ENABLED=true
CHATWOOT_API_TOKEN=
api_access_token hardcoded
merge conflict markers
```

Result: no active risky default or hardcoded Chatwoot token found. The only `LK_RECOVERY_DRY_RUN=false` match is a README historical note warning not to reactivate without explicit approval.

## Current status

Local uncommitted branch:

```text
feat/chatwoot-provider-internal
```

Touched files:

```text
.github/workflows/t1-runner.yml
README.md
workers/recovery-os/package.json
workers/recovery-os/src/t1.ts
workers/recovery-os/src/types.ts
workers/recovery-os/wrangler.toml
workers/recovery-os/src/chatwoot.ts
workers/recovery-os/src/support_provider.ts
workers/recovery-os/tests/chatwoot.test.ts
workers/recovery-os/tests/t1_chatwoot.test.ts
```

## Next safe gate

Before production deploy:

- commit branch locally;
- open PR only after Lucas approves external GitHub write;
- verify real Cloudflare secrets/vars;
- keep `LK_CHATWOOT_INTERNAL_ONLY=true`;
- keep customer-facing send disabled unless separately approved.
