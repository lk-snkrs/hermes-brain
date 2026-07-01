#!/usr/bin/env bash
# brain-safe-push.sh — concurrency-safe commit + push for the Hermes Brain.
#
# The Brain has multiple simultaneous writers (HERMES VPS runtime + CLAUDE via
# PR). ANY automated writer that pushes directly to `main` MUST use this instead
# of a raw `git push origin main`, so it can never clobber a brain that another
# writer already advanced. See governance/protocols/brain-write-coordination.md.
#
# What it guarantees:
#   1. Scoped staging — never `git add -A` (which sweeps unrelated WIP / junk).
#   2. Pull-before-push — rebase onto latest remote before every push.
#   3. Retry on rejection — if the remote advanced mid-flight, rebase & retry.
#   4. Never force-push; stop and ask for manual resolution on real conflicts.
#
# Usage:
#   brain-safe-push.sh -m "commit message" [path ...]
#     path...  files/dirs to stage (scoped). If omitted, uses already-staged.
#
# Env overrides:
#   BRAIN_REMOTE        (default: origin)
#   BRAIN_BRANCH        (default: main)
#   BRAIN_PUSH_RETRIES  (default: 3)
#
# Exit codes: 0 ok/no-op · 2 usage · 3 rebase conflict · 4 push failed.
set -euo pipefail

REMOTE="${BRAIN_REMOTE:-origin}"
BRANCH="${BRAIN_BRANCH:-main}"
RETRIES="${BRAIN_PUSH_RETRIES:-3}"

msg=""
paths=()
while [ "$#" -gt 0 ]; do
    case "$1" in
        -m) msg="${2:-}"; shift 2 ;;
        --) shift; while [ "$#" -gt 0 ]; do paths+=("$1"); shift; done ;;
        *)  paths+=("$1"); shift ;;
    esac
done

if [ -z "$msg" ]; then
    echo "brain-safe-push: -m <message> is required" >&2
    exit 2
fi

# 1. Scoped stage (never `git add -A`).
if [ "${#paths[@]}" -gt 0 ]; then
    git add -- "${paths[@]}"
fi

# Nothing staged? no-op.
if git diff --cached --quiet; then
    echo "brain-safe-push: no staged changes — nothing to do"
    exit 0
fi

git commit -m "$msg"

# 2. Pull-before-push with retry; never --force.
attempt=1
while [ "$attempt" -le "$RETRIES" ]; do
    if ! git pull --rebase --autostash "$REMOTE" "$BRANCH"; then
        echo "brain-safe-push: rebase conflict — resolve manually; NOT pushing." >&2
        echo "brain-safe-push: inspect before overwriting; never --force to 'resolve'." >&2
        exit 3
    fi
    if git push "$REMOTE" "$BRANCH"; then
        echo "brain-safe-push: pushed to $REMOTE/$BRANCH (attempt $attempt/$RETRIES)"
        exit 0
    fi
    echo "brain-safe-push: push rejected (attempt $attempt/$RETRIES) — remote advanced; rebasing & retrying."
    attempt=$((attempt + 1))
done

echo "brain-safe-push: failed after $RETRIES attempts." >&2
exit 4
