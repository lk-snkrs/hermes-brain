# Hermes/LK Operational Consolidation — Filesystem & Git Inventory

Timestamp: 2026-05-16T19:15:53Z
Scope: `/opt/data/hermes_bruno_ingest`
Mode: read-only inventory + low-risk cache cleanup only. No Docker/VPS/runtime/Shopify/Meta/Google/external send changes.

## Executive verdict

The environment is stable but cluttered. The biggest redundancy is not active production infrastructure; it is local filesystem/worktree sprawl from prior Brain/LK/Mission iterations.

Recommended source-of-truth posture:

- Canonical Brain: `/opt/data/hermes_bruno_ingest/hermes-brain`
- Canonical Spiti repo: `/opt/data/hermes_bruno_ingest/spiti-hub-git`
- Active LK theme work: `/opt/data/hermes_bruno_ingest/lk-new-theme`
- Production Hermes runtime: Docker/VPS, not any local Mission/Workspace checkout
- Workspace: retired; `hermes.lucascimino.com` intentionally 404

## Actions executed during this pass

- Cleaned Python cache-only dirt from three Brain worktrees:
  - `/opt/data/hermes_bruno_ingest/hermes-brain-follow-20260510/scripts/__pycache__`
  - `/opt/data/hermes_bruno_ingest/hermes-brain-lk-weekly-influencer-creatives-20260510/scripts/__pycache__`
  - `/opt/data/hermes_bruno_ingest/hermes-brain-lk-weekly-influencer-email-gmail-fix-20260510/scripts/__pycache__`
- Verified those three worktrees became clean after cleanup.
- Did not remove any project directories, Git worktrees, archives, data snapshots, secrets, or theme files.

## Inventory summary

Top-level directories inventoried: 72

Classification counts:

- Maintain secrets / do not touch: 2
- Maintain canonical dirty Brain: 1
- Maintain active LK theme work: 1
- Maintain LK theme production-sync reference: 1
- Maintain Spiti canonical Git repo: 1
- Maintain local data, review retention: 1
- Maintain Hermes patch history, review later: 2
- Clean Brain worktrees candidate for archival: 44
- Large archive candidate for removal after approval: 1
- Lightweight draft/archive candidates: 7
- Candidate duplicate Spiti directory after verification: 1
- Maintain or review miscellaneous: 9

## Highest-impact cleanup candidates

### 1. `_archived_projects` — 1.4G

Path:

```text
/opt/data/hermes_bruno_ingest/_archived_projects
```

Contents:

```text
mission-control-cimino-hermes.20260516-173247
```

Recommendation: remove only after a final explicit approval because it is the archived Mission Control project. It is not active production, but deletion is irreversible unless backed up elsewhere.

Potential benefit: frees ~1.4GB and removes the biggest source of Mission/Workspace confusion.

### 2. Brain worktree sprawl — 44 clean worktrees

There are 44 clean Brain worktrees, mostly one-commit docs/feat/fix branches from May 9–11. They are not dirty after cache cleanup.

Recommendation: do not delete blindly. Next safe step is to classify each branch into:

- already merged / redundant → remove worktree and optionally delete local branch;
- not merged but valuable → cherry-pick/squash into canonical Brain or archive as patch bundle;
- unknown → keep until reviewed.

Examples of clean worktrees:

- `hermes-brain-brain-score-worktree`
- `hermes-brain-bruno-p0-worktree`
- `hermes-brain-follow-20260510`
- `hermes-brain-lk-*`
- `hermes-brain-memory-hygiene-worktree`
- `hermes-brain-next-safe-worktree`

### 3. `spiti-hub` duplicate candidate — 224M

Paths:

```text
/opt/data/hermes_bruno_ingest/spiti-hub
/opt/data/hermes_bruno_ingest/spiti-hub-git
```

Observed:

- `spiti-hub-git` is a clean Git repo on `dev`, remote `spiti-auction/spiti-hub`, with node_modules.
- `spiti-hub` is non-Git, also has `package.json`, `README.md`, and `node_modules`.

Follow-up comparison excluding `node_modules`, `.git`, `.next`, `dist`, and `build`:

- `spiti-hub`: 129 files
- `spiti-hub-git`: 127 files
- only in `spiti-hub`: `.hermes_source.json`, `docs/briefing-2026-04-30.md`
- same relative path but different size: 27 files, including `src/App.jsx`, `src/components/*`, `src/lib/*`, multiple `src/pages/*`, and `vite.config.js`

Recommendation: **do not delete `spiti-hub` yet.** It is not a pure duplicate. Next safe step is a focused diff/export of the 27 differing files and the two unique files, then decide whether to merge anything useful into `spiti-hub-git` or archive the old copy.

### 4. `local_sql` — 976M

Path:

```text
/opt/data/hermes_bruno_ingest/local_sql
```

Largest observed items:

- `lk_os_backups` — 763M
- `lk_gmc_rollback_snapshots` — 115M
- `lk_os_phase5.sqlite` — 86M

Recommendation: keep for now. This is data/rollback material, not UI clutter. Later create a retention policy, e.g. keep latest N snapshots and compress older backups.

### 5. `lk-new-theme` — 1014M, dirty

Path:

```text
/opt/data/hermes_bruno_ingest/lk-new-theme
```

Branch:

```text
cro/samba-jane-preview-v0
```

Dirty files:

```text
M layout/theme.liquid
M sections/lk-collection.liquid
M sections/lk-pdp.liquid
?? sections/lk-announcement.liquid
?? snippets/lk-popup-ab.liquid
?? snippets/lk-popup-b.liquid
?? snippets/lk-popup.liquid
?? snippets/lk-whatsapp-widget.liquid
```

Recommendation: do not clean/delete. This is active LK CRO/theme work and should be handled through dev-theme QA/PR flow only.

### 6. Hermes Agent patch history — dirty but important

Paths:

```text
/opt/data/hermes_bruno_ingest/hermes-agent-upstream
/opt/data/hermes_bruno_ingest/hermes-agent-v0.13.0
```

Observed dirty changes relate to context compression retry work:

```text
agent/context_compressor.py
tests/agent/test_context_compressor.py
```

Recommendation: keep. Do not delete or reset; these contain the compression self-heal/patch history relevant to production Hermes reliability.

## Current Git risk notes

### Canonical Brain

Path:

```text
/opt/data/hermes_bruno_ingest/hermes-brain
```

Status:

- detached at `origin/main`
- dirty: 39 modified files + 707 untracked entries at inventory time

Recommendation: next pass should not be deletion. It should be Git hygiene:

1. separate generated reports/artifacts from source docs/scripts;
2. identify which untracked entries are intended Brain records;
3. commit or archive a coherent Brain consolidation patch;
4. only then remove old worktrees.

### Weekly SEO/CRO cron workdir

Cron:

```text
15777e3416dc — LK SEO/CRO weekly Claude SEO improvement loop
```

Current workdir:

```text
/opt/data/hermes_bruno_ingest/hermes-brain-follow-20260510
```

After cache cleanup, this worktree is clean.

Recommendation: keep for the next scheduled run unless/until we validate that the canonical Brain has all required scripts/references. Changing the workdir before Monday is possible, but not necessary for runtime stability.

## Recommended next execution order

1. Git hygiene on canonical Brain: produce a concise changed/untracked map and decide what becomes a commit.
2. Compare clean Brain worktree branches against canonical Brain to identify branches already merged or obsolete.
3. Verify `spiti-hub` vs `spiti-hub-git`; remove duplicate only if byte/content differences are non-valuable.
4. Prepare explicit approval packet for deleting `_archived_projects/mission-control-cimino-hermes.20260516-173247` if Lucas wants to free 1.4GB.
5. Later: define local SQL backup retention/compression policy.

## Safety boundaries preserved

- No Docker/compose/Traefik/VPS mutation.
- No Hermes gateway/runtime restart.
- No Shopify/theme production write.
- No Meta/Google/GMC mutation.
- No external email/WhatsApp/client send.
- No secret contents printed or copied.
