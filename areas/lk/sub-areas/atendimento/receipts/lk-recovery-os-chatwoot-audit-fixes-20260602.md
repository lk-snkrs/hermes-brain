---
title: lk-recovery-os Chatwoot provider audit and local fixes
created_at_utc: 2026-06-02
area: lk/atendimento
repo: https://github.com/lk-snkrs/lk-recovery-os
branch: feat/chatwoot-provider-internal
status: local_changes_verified_not_deployed
---

# lk-recovery-os Chatwoot provider audit and local fixes

## Scope

Audit the local `lk-recovery-os` migration from Crisp-centric abandoned cart recovery to Chatwoot internal-first recovery context.

Local repo:

```text
/opt/data/lk-recovery-os
```

Branch:

```text
feat/chatwoot-provider-internal
```

## Safety boundaries

No production deploy performed.
No Shopify webhook created/changed.
No customer-visible message sent.
No Chatwoot production API call performed during this audit.
No secrets written to repo, Brain, or logs.

## Findings corrected

1. Chatwoot contact create was missing required `inbox_id` from official API docs.
   - Fixed in `workers/recovery-os/src/chatwoot.ts`.
   - Test updated to assert `inbox_id` is sent.

2. Chatwoot contact response parser was too narrow.
   - Official docs describe `payload` as an array shape for create contact.
   - Parser now handles array payload, nested contact payload, and top-level id.

3. Arbitrary context was being sent under `custom_attributes`.
   - Chatwoot docs warn custom attributes should correspond to valid definitions.
   - Moved arbitrary operational context to `additional_attributes` for contact/conversation.

4. Manual legacy GitHub Action defaulted `dry_run` to `false` even though paused.
   - Changed workflow dispatch default and env fallback to `true`.
   - Preserves legacy fallback while making accidental send less likely.

5. README still documented legacy live wrapper vars with `LK_RECOVERY_DRY_RUN=false` as an operational-looking state.
   - Reframed as historical legacy state not to reactivate without explicit approval.
   - Added Chatwoot internal-first migration section.

## Files changed

```text
.github/workflows/t1-runner.yml
README.md
workers/recovery-os/package.json
workers/recovery-os/src/chatwoot.ts
workers/recovery-os/src/support_provider.ts
workers/recovery-os/src/t1.ts
workers/recovery-os/src/types.ts
workers/recovery-os/tests/chatwoot.test.ts
workers/recovery-os/tests/t1_chatwoot.test.ts
workers/recovery-os/wrangler.toml
```

## Verification

Commands run successfully:

```bash
cd /opt/data/lk-recovery-os/workers/recovery-os && npm test && npx tsc --noEmit
```

Observed:

```text
6 test files passed
45 tests passed
TypeScript typecheck exit 0
```

```bash
cd /opt/data/lk-recovery-os && uv run pytest -q
```

Observed:

```text
155 passed, 1 warning
```

```bash
cd /opt/data/lk-recovery-os && git diff --check
```

Observed: exit 0.

Risk scan for active live-send defaults and token literals found only the README historical note containing `LK_RECOVERY_DRY_RUN=false`; no hardcoded `CHATWOOT_API_TOKEN` value found.

## Current local status

Changes are local only and uncommitted as of this receipt. Next recommended step: review diff, then commit and open PR if Lucas approves pushing to GitHub.
