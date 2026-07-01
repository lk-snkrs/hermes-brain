# LK Ops — GitHub Actions report-publisher fix

- date: 2026-07-01
- repo: `lucascimino/lk-ops`
- PR: https://github.com/lucascimino/lk-ops/pull/1
- merge commit: `23dec139acff5e8e5d512a32f80b7eee723d5ae3`
- affected workflows observed: `Theme and Platform Health Weekly`, `Content and SEO Strategy Biweekly`, `Competitive Intel Monthly`
- values_printed: false

## Trigger

Lucas forwarded GitHub Actions failure emails for `Theme and Platform Health Weekly` and `Content and SEO Strategy Biweekly` on branch `main`, commit `ca1f2a8`.

## Auth repair

`GITHUB_TOKEN_LUCASCIMINO` was updated in Doppler after Lucas supplied a replacement token. The value was not printed or stored in Brain.

Readback after update:

- GitHub login: `lucascimino`
- Repo access: `lucascimino/lk-ops` OK
- `values_printed=false`

Because the token was pasted in chat, later rotation is recommended after the incident is fully closed.

## Root cause

Failed run logs showed a common error during report publication:

```text
AttributeError: 'list' object has no attribute 'get'
```

The failure occurred in `scripts/lib/report-publisher.py` while updating `reports.json`. The publisher assumed every manifest entry was a dictionary and called `e.get(...)`. The live VPS manifest contained at least one malformed/non-dict list entry, causing scheduled reports to fail after generation.

## Fix applied

PR #1 changed:

- `scripts/lib/report-publisher.py`
  - added defensive `_load_manifest_entries()`;
  - returns only dict entries;
  - handles missing, invalid JSON, non-list root, and malformed list entries;
  - keeps dedupe behavior for same `type` + `date`.
- `scripts/test-report-publisher.py`
  - added focused regression for malformed manifest entries.
- `scripts/test-all.sh`
  - added syntax checks for report publisher/test and runs the regression.

## Verification

Local verification before merge:

- `python3 scripts/test-report-publisher.py` → PASS
- `python3 -m py_compile scripts/lib/report-publisher.py scripts/test-report-publisher.py` → PASS
- `bash scripts/test-all.sh` → 23 passed, 0 failed
- `git diff --check` → PASS
- Changed-file secret scan → `possible_credential_value_hits=0`

GitHub verification after merge:

- PR #1 state: `MERGED`
- Merged at: `2026-07-01T13:30:57Z`
- `main` ref SHA: `23dec139acff5e8e5d512a32f80b7eee723d5ae3`

## Guardrails

- No token/secret values printed.
- No direct push to `main`; used PR + squash merge.
- No manual workflow dispatch/rerun was executed, because workflows publish to VPS/send Telegram and should not be rerun without separate approval.
- No Docker/VPS/Traefik changes.

## Remaining validation

The next scheduled run or an explicitly approved manual dispatch should confirm the end-to-end publish path. If manual dispatch is approved, run one affected workflow and verify it no longer fails in `report-publisher.py`.
