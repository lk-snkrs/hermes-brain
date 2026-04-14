#!/bin/bash
# Sync hermes-brain to GitHub and local Hermes
# Run daily via cron

set -e

CEREBRO="/root/cerebro-cimino"
HERMES_BRAIN="/root/hermes-brain"
GIT_DIR="/root/.hermes-brain-git"

cd ""

# Pull latest from cerebro if exists
if [ -d "/.git" ]; then
    echo "Syncing from cerebro-cimino..."
    # Copy updated memories from cerebro if newer
    cp "/empresa/contexto/decisoes.md" "/memories/decisions.md" 2>/dev/null || true
    cp "/empresa/gestao/lessons.md" "/memories/lessons.md" 2>/dev/null || true
fi

# Commit and push
git add -A
git commit -m "hermes-brain sync 2026-04-14 08:45" 2>/dev/null || true
git push origin main 2>/dev/null || true

echo "Sync complete: Tue Apr 14 08:45:55 -03 2026"
