---
title: lk-recovery-os cross-platform identity sync 522 soft-fail fix
created_at_utc: 2026-06-02
area: lk/atendimento
repo: https://github.com/lk-snkrs/lk-recovery-os
pr: 23
pr_url: https://github.com/lk-snkrs/lk-recovery-os/pull/23
main_head: 37a5c055118d6c92264a22a3042ac800bc32931a
workflow_run: 26847761075
status: merged_verified
---

# Cross-platform identity sync — audit/fix

## User-reported failure

Screenshot showed GitHub Actions workflow failure:

```text
cross-platform-identity-sync: All jobs have failed
job: cross-platform-identity-sync / sync
```

Failing scheduled run inspected:

```text
run_id=26846587538
conclusion=failure
head_sha=e4b54b59818673d3a307cb0f676fd2070e9dcc17
```

## Root cause

The workflow was not failing due to code build/lint. It was failing because Supabase/PostgREST behind Cloudflare returned repeated transient origin timeouts while the job loaded `identity_links`:

```text
supabase GET identity_links returned HTTP 522 (attempt 1/4)
supabase GET identity_links returned HTTP 522 (attempt 2/4)
supabase GET identity_links returned HTTP 522 (attempt 3/4)
SupabaseApiError: Supabase REST GET identity_links failed: HTTP 522
```

The script treated exhausted transient Supabase 5xx the same as a hard code/config failure, creating noisy red scheduled workflow alerts.

Secondary audit finding: the script still enabled legacy Crisp when Crisp secrets existed. Current LK direction is Chatwoot/no-Crisp by default, so Crisp should not run unless explicitly re-enabled.

## Fix

PR:

```text
https://github.com/lk-snkrs/lk-recovery-os/pull/23
```

Merged commit:

```text
37a5c05 fix: soften transient Supabase sync outages (#23)
```

Changes:

- `SupabaseApiError` now carries `method`, `path`, `status_code`, and `retryable` metadata.
- `scripts/lk_recovery_os_cross_platform_sync.py` catches exhausted retryable Supabase errors and exits `0` with an explicit `SOFT_FAIL` log.
- Non-retryable errors such as 401/config failures still raise and fail the workflow.
- Legacy Crisp sync is disabled by default and now requires `LK_CROSS_PLATFORM_ENABLE_CRISP=true`.
- Added regression tests for soft-fail behavior and Crisp default-off behavior.

## Verification

Local after merge:

```text
git status: ## main...origin/main
head: 37a5c05 lk-snkrs <lk@lksneakers.com.br> fix: soften transient Supabase sync outages (#23)
```

Python + Ruff:

```bash
uv run pytest -q && uv run ruff check . && git diff --check
```

Result:

```text
159 passed, 1 warning
All checks passed
git diff --check exit 0
```

Worker TypeScript:

```bash
cd workers/recovery-os && npm test && npx tsc --noEmit
```

Result:

```text
6 test files passed
46 tests passed
typecheck exit 0
```

GitHub CI for PR #23:

```text
conclusion=success
```

Manual workflow dispatch after merge:

```text
run_id=26847761075
workflow=cross-platform-identity-sync
event=workflow_dispatch
conclusion=success
head_sha=37a5c055118d6c92264a22a3042ac800bc32931a
```

Workflow log confirmed the same transient 522 scenario is now safe/no-red:

```text
supabase GET identity_links returned HTTP 522 (attempt 1/4)
supabase GET identity_links returned HTTP 522 (attempt 2/4)
supabase GET identity_links returned HTTP 522 (attempt 3/4)
SOFT_FAIL: transient Supabase outage after retries; method=GET path=identity_links status=522. Skipping this scheduled sync without platform writes.
platforms enabled: {'klaviyo': True, 'shopify': True, 'crisp': False}
```

Production deployment/health:

```text
Vercel deployment dpl_CHpraQP5aCyr9FEXhppz47StwXWB
state=READY
readyState=READY
readySubstate=PROMOTED
target=production
sha=37a5c055118d6c92264a22a3042ac800bc32931a
author_email=lk@lksneakers.com.br
```

`/healthz` returned HTTP 200 in multiple probes but also had intermittent 30s timeouts during final verification. This appears separate from the GitHub Actions workflow failure fixed in PR #23 and should be monitored/audited as a Vercel runtime availability issue if it persists.

## Safety

No Shopify write performed by Hermes.
No Chatwoot live API call performed by Hermes.
No WhatsApp/customer-facing send.
No Tiny write.
No secrets printed or committed.
