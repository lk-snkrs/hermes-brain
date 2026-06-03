---
title: lk-recovery-os Superpowers audit
created_at_utc: 2026-06-02
area: lk/atendimento
repo: https://github.com/lk-snkrs/lk-recovery-os
branch: feat/chatwoot-provider-internal
status: local_changes_verified_not_deployed
skills: [superpowers, verification-before-completion, systematic-debugging, github-code-review, executing-plans]
---

# lk-recovery-os Superpowers audit

## Scope

Lucas asked to redo the `recovery-os` audit using Superpowers discipline.

Local repo:

```text
/opt/data/lk-recovery-os
```

Branch:

```text
feat/chatwoot-provider-internal
```

## Safety

No production deploy.
No Shopify writes.
No Chatwoot live API call.
No WhatsApp/customer-visible message.
No secrets written.

## Superpowers flow applied

1. Loaded `superpowers` wrapper.
2. Loaded underlying skills:
   - `verification-before-completion`
   - `systematic-debugging`
   - `github-code-review`
   - `executing-plans`
3. Reviewed local diff/scope.
4. Checked Chatwoot API docs and LK Chatwoot skill references.
5. Investigated root-cause risks before patching.
6. Patched confirmed issues only.
7. Ran fresh verification.

## New critical finding found during Superpowers re-audit

The first Chatwoot integration created the Chatwoot contact/conversation/private note before reserving a `recovery_messages` row in Supabase.

Root cause risk:

```text
Chatwoot success
→ Supabase insert fails after success
→ no recovery_messages cap/audit row
→ next tick can create duplicate Chatwoot contexts
```

This violated the existing Crisp sender safety pattern, which reserves `recovery_messages` before external provider side effect.

## Fix applied

Updated `workers/recovery-os/src/t1.ts` so Chatwoot internal-only now follows provider-side-effect safety:

```text
ensureSequence
→ insert recovery_messages status=pending_internal_context
→ call ChatwootProvider.createInternalContext
→ patch recovery_messages to internal_context_created with conversation/contact/note ids
```

On Chatwoot failure:

```text
patch recovery_messages status=failed
write audit_log chatwoot_internal_context_failed
continue fail-closed
```

This mirrors the legacy Crisp reserve-before-send contract.

## Previous findings still covered

- Chatwoot contact create now includes required `inbox_id`.
- Chatwoot contact parser handles array/nested/top-level id responses.
- Operational context moved to `additional_attributes`, avoiding arbitrary undefined Chatwoot custom attributes.
- GitHub Action manual fallback defaults to `dry_run=true`.
- README frames legacy `LK_RECOVERY_DRY_RUN=false` as historical and not to reactivate without explicit approval.
- Worker defaults are internal-first / no customer-facing send.

## Fresh verification evidence

```bash
cd /opt/data/lk-recovery-os/workers/recovery-os && npm test && npx tsc --noEmit
```

Result:

```text
6 test files passed
45 tests passed
TypeScript typecheck exit 0
```

```bash
cd /opt/data/lk-recovery-os && uv run pytest -q
```

Result:

```text
155 passed, 1 warning
```

```bash
cd /opt/data/lk-recovery-os && git diff --check
```

Result: exit 0.

Risk scan:

```text
No hardcoded CHATWOOT_API_TOKEN.
No active LK_LIVE_SEND_ENABLED=true / LK_WHATSAPP_SEND_ENABLED=true default found in files scanned.
Only `LK_RECOVERY_DRY_RUN=false` hit is README historical note saying not to reactivate without explicit approval.
```

## Current local git status

Uncommitted local branch:

```text
feat/chatwoot-provider-internal
```

Modified/untracked files:

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

## Remaining risk / next gate

Not yet deployed or live-smoked against Chatwoot. Before any deploy, require explicit approval and verify:

- actual Cloudflare Worker vars;
- `CHATWOOT_API_TOKEN` present as secret, not config;
- Chatwoot account/inbox/team IDs still match production;
- `LK_RECOVERY_DRY_RUN` / `LK_CHATWOOT_INTERNAL_ONLY` rollout semantics are explicitly chosen;
- customer-facing sends remain disabled unless separately approved.
