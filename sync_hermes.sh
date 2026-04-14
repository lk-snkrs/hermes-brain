#!/bin/bash
# Sync hermes-brain ↔ cerebro-cimino + auto-commit
# Rodar diariamente via cron
#
# Fluxo:
#  1. Pull do cerebro-cimino (fonte original)
#  2. Merge local (hermes edits)
#  3. Auto-commit se mudou
#  4. Push hermes-brain-git

set -e

CEREBRO="/root/cerebro-cimino"
HERMES_BRAIN="/root/hermes-brain"
GIT_DIR="/root/.hermes-brain-git"
STATE_FILE="$HERMES_BRAIN/.sync-state.json"

cd "$HERMES_BRAIN"

# --- Pull from cerebro-cimino ---
if [ -d "$CEREBRO/.git" ]; then
    echo "Pulling from cerebro-cimino..."
    # Only copy memory-relevant files (not all cerebro)
    rsync -av --files-from=- "$CEREBRO/" "$HERMES_BRAIN/" <<'RSYNC_FILES'
empresa/contexto/decisoes.md
empresa/contexto/metricas.md
empresa/contexto/geral.md
empresa/decisoes/
agentes/lk/SOUL.md
agentes/lk/AGENTS.md
agentes/zipper/SOUL.md
agentes/zipper/AGENTS.md
agentes/spiti/SOUL.md
agentes/spiti/AGENTS.md
RSYNC_FILES
fi

# --- Check if anything changed ---
if [ -d "$GIT_DIR" ]; then
    cd "$GIT_DIR"
    git fetch origin main 2>/dev/null || true
    LOCAL=$(git rev-parse HEAD 2>/dev/null)
    REMOTE=$(git rev-parse origin/main 2>/dev/null)
    
    if [ "$LOCAL" != "$REMOTE" ]; then
        echo "New commits in cerebro, pulling..."
        git pull origin main --no-edit || true
    fi
fi

# --- Auto-commit if local changes ---
cd "$HERMES_BRAIN"
if [ -d "$GIT_DIR" ]; then
    cd "$GIT_DIR"
    # Stage all changes
    git add -A
    
    # Only commit if there are actual changes
    if git diff --cached --quiet; then
        echo "No changes to commit"
    else
        TIMESTAMP=$(date '+%Y-%m-%d %H:%M')
        git commit -m "hermes sync $TIMESTAMP" || true
        git push origin main || true
        echo "✅ Committed and pushed: $TIMESTAMP"
    fi
fi

# --- Update sync state ---
echo "{\"lastSync\": \"$(date -Iseconds)\", \"status\": \"ok\"}" > "$STATE_FILE"
echo "Sync complete: $(date)"
