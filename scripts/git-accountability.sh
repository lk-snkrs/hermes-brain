#!/bin/bash
# Auto-commit after session — git accountability para Hermes
# Rodar após toda sessão relevante
#
# Uso:
#   bash /root/hermes-brain/scripts/git-accountability.sh "resumo da tarefa"
#
# Exemplo:
#   bash /root/hermes-brain/scripts/git-accountability.sh "Atualizado TOOLS.md com 13 integrais"

SUMMARY="${1:-chore: auto-commit}"
HERMES_BRAIN="/root/hermes-brain"
GIT_DIR="/root/.hermes-brain-git"

cd "$HERMES_BRAIN"

# Check if there are changes
if [ -d "$GIT_DIR" ]; then
    cd "$GIT_DIR"
    
    # Stage all changes
    git add -A
    
    # Only commit if there are actual changes
    if git diff --cached --quiet; then
        echo "No changes to commit"
        exit 0
    fi
    
    TIMESTAMP=$(date '+%Y-%m-%d %H:%M')
    git commit -m "$SUMMARY — $TIMESTAMP"
    git push origin main 2>/dev/null || true
    echo "✅ Committed: $SUMMARY"
else
    # No git dir — create one
    cd "$HERMES_BRAIN"
    git init 2>/dev/null || true
    git add -A
    git commit -m "$SUMMARY" 2>/dev/null || true
    echo "✅ Local commit (no remote configured)"
fi
