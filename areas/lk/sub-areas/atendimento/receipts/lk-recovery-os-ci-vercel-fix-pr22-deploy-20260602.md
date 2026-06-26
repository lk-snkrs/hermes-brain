---
title: lk-recovery-os CI/Vercel author fix and deploy
created_at_utc: 2026-06-02
area: lk/atendimento
repo: https://github.com/lk-snkrs/lk-recovery-os
pr: 22
pr_url: https://github.com/lk-snkrs/lk-recovery-os/pull/22
main_head: e4b54b59818673d3a307cb0f676fd2070e9dcc17
vercel_deployment_uid: dpl_J8aFoYrkvhjZt1omjK5QL5nv4wU6
status: deployed_verified
---

# LK Recovery OS — CI/Vercel fix after PR #21

## Why PR #21 produced alerts

Two separate things happened:

1. GitHub CI failed because the workflow runs `uv run ruff check .`, and the repo had existing Ruff failures not covered by the previous local verification.
2. Vercel blocked the feature-branch preview deployment authored as `Lucas Cimino <lucas@lkskrs.online>`, because that Git author is not accepted on the `lk-snkrs-projects` Vercel team.

## Fix applied

PR #22:

```text
https://github.com/lk-snkrs/lk-recovery-os/pull/22
```

Merged main commit:

```text
e4b54b5 fix: satisfy recovery os CI lint (#22)
```

Commit/deploy author:

```text
lk-snkrs <lk@lksneakers.com.br>
```

Vercel production deployment:

```text
dpl_J8aFoYrkvhjZt1omjK5QL5nv4wU6
```

Vercel state:

```text
READY / PROMOTED / target=production
```

Vercel metadata confirms:

```text
githubCommitAuthorEmail=lk@lksneakers.com.br
githubCommitSha=e4b54b59818673d3a307cb0f676fd2070e9dcc17
```

## CI status

GitHub Actions CI for `e4b54b59818673d3a307cb0f676fd2070e9dcc17`:

```text
run_id=26846248173
conclusion=success
job test=success
```

## Local verification after sync

Repo state:

```text
## main...origin/main
e4b54b5 lk-snkrs <lk@lksneakers.com.br> fix: satisfy recovery os CI lint (#22)
663bf27 lk-snkrs <lk@lksneakers.com.br> feat: add Chatwoot internal recovery context (#21)
```

Python + Ruff:

```bash
uv run pytest -q && uv run ruff check .
```

Result:

```text
155 passed, 1 warning
All checks passed
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

## Runtime verification

Production alias:

```text
https://lk-recovery-os.vercel.app/healthz
```

Verified response:

```text
HTTP 200
{"service":"lk-recovery-os","status":"ok"}
```

`/readyz` returned 200 on subsequent retries but had one intermittent timeout during verification; note for future monitoring.

## Branch cleanup

Feature branch deleted remotely and locally:

```text
fix/ci-ruff-lk-deploy-author
```

## Production safety

No Shopify write.
No Chatwoot live API call.
No WhatsApp/customer-facing send.
No Tiny write.
No secrets printed or committed.
