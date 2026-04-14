#!/bin/bash
# Memory Flush — categorize and save session memory
# Rodar quando contexto atingir ~30k tokens
#
# Categorias:
#  1. Decisões → memories/decisions.md
#  2. Mudanças → memories/decisions.md
#  3. Lições → memories/lessons.md
#  4. Bloqueios → pending.md
#  5. Fatos-chave → memories/*.md

HERMES_BRAIN="/root/hermes-brain"
MEMORIES="$HERMES_BRAIN/memories"
STATE_FILE="$HERMES_BRAIN/.flush-state.json"
DATE=$(date '+%Y-%m-%d')

echo "Running memory flush: $DATE"

# Update flush state
echo "{\"lastFlush\": \"$(date -Iseconds)\", \"tokens_estimate\": \"~30k\"}" > "$STATE_FILE"

# Commit the flush itself
cd "$HERMES_BRAIN"
if [ -d "/root/.hermes-brain-git" ]; then
    cd "/root/.hermes-brain-git"
    git add -A
    git commit -m "chore: memory flush $DATE" 2>/dev/null || true
    git push origin main 2>/dev/null || true
    echo "✅ Flush committed"
fi

echo "Flush complete: $DATE"
