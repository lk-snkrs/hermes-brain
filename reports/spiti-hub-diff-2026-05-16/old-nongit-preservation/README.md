# Spiti Hub old non-Git preservation

This folder preserves the useful evidence from the old non-Git `/opt/data/hermes_bruno_ingest/spiti-hub` directory before local cleanup.

## Finding

The old folder was not a Git clone. Its `.hermes_source.json` identified it as a GitHub zipball of `spiti-auction/spiti-hub` with metadata around 2026-04-30.

The canonical working repo is `/opt/data/hermes_bruno_ingest/spiti-hub-git` on branch `dev` at commit `2943614`, which already includes later PR/lint/build/performance changes.

## Preserved files

- `briefing-2026-04-30.md` — unique old briefing file.
- `hermes_source_sanitized.json` — sanitized source metadata.
- `old-spiti-hub-vs-canonical-git.diff` — full text diff excluding `.git`, `.next`, `build`, `dist`, and `node_modules`.

## Decision

Do not merge old source files back into canonical `spiti-hub-git`: the 27 differences are stale relative to later canonical `dev` work such as route lazy loading and Vite manual chunk splitting.

Safe cleanup is to remove the old non-Git directory after this preservation package is committed in the Brain.
