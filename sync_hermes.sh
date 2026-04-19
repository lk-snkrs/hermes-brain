#!/bin/bash
# Hermes Brain Sync — Bidirectional sync between VPS brain and local
# Rodar diariamente via cron (6h BRT)
#
# Fluxo:
#   1. Pull from VPS (brain mais novo da VPS)
#   2. Push local changes (pending.md, lessons.md, etc.)
#   3. Auto-commit se mudou
#
# IMPORTANT: Cron MiniMax não tem SSH key — usa sshpass

set -e

SSH_HOST="root@72.60.150.124"
SSH_PORT="22"
SSH_PASS='+gryuk#TGk9JQF)q'

ssh_cmd() {
    sshpass -p "$SSH_PASS" ssh -o ConnectTimeout=15 -o StrictHostKeyChecking=no -p "$SSH_PORT" "$SSH_HOST" "$1"
}

CEREBRO="/root/cerebro-cimino"
HERMES_BRAIN="/root/hermes-brain"
LOCAL_BRAIN="$HOME/.hermes"
GIT_DIR="$LOCAL_BRAIN/hermes-brain-git"
STATE_FILE="$HERMES_BRAIN/.sync-state.json"

# ── Bidirectional sync of key memory files ────────────────────────────────

SYNC_FILES=(
    "memories/pending.md"
    "memories/lessons.md"
    "memories/decisions.md"
    "memories/lk.md"
    "memories/zipper.md"
    "memories/spiti.md"
    "HEARTBEAT.md"
    "PROTOCOLS.md"
)

echo "[Brain Sync] Starting — $(date)"

# ── Pull from VPS ───────────────────────────────────────────────────────
echo "[Brain Sync] Pulling from VPS..."
for file in "${SYNC_FILES[@]}"; do
    remote_path="$CEREBRO/$file"
    local_dest="$HERMES_BRAIN/$file"
    mkdir -p "$(dirname "$local_dest")"
    if ssh_cmd "test -f $remote_path"; then
        sshpass -p "$SSH_PASS" scp -o ConnectTimeout=15 -o StrictHostKeyChecking=no -P "$SSH_PORT" "$SSH_HOST:$remote_path" "$local_dest" 2>/dev/null && echo "  ✓ $file" || echo "  ✗ $file"
    fi
done

# ── Push local pending.md and lessons.md to VPS ──────────────────────────
echo "[Brain Sync] Pushing local updates to VPS..."
LOCAL_FILES=(
    "$LOCAL_BRAIN/memories/pending.md:memories/pending.md"
    "$LOCAL_BRAIN/memories/lessons.md:memories/lessons.md"
)

for pair in "${LOCAL_FILES[@]}"; do
    local_path="${pair%%:*}"
    remote_rel="${pair##*:}"
    remote_path="$CEREBRO/$remote_rel"
    if [ -f "$local_path" ]; then
        sshpass -p "$SSH_PASS" scp -o ConnectTimeout=15 -o StrictHostKeyChecking=no -P "$SSH_PORT" "$local_path" "$SSH_HOST:$remote_path" 2>/dev/null && echo "  ✓ $remote_rel" || echo "  ✗ $remote_rel"
    fi
done

# ── Auto-commit local changes ─────────────────────────────────────────────
if [ -d "$GIT_DIR" ]; then
    cd "$GIT_DIR"
    git add -A
    if ! git diff --cached --quiet; then
        TIMESTAMP=$(date '+%Y-%m-%d %H:%M')
        git commit -m "brain sync $TIMESTAMP" && git push origin main || echo "[Brain Sync] Push failed"
        echo "  ✓ Committed: $TIMESTAMP"
    else
        echo "  — No changes"
    fi
fi

# ── Sync state ──────────────────────────────────────────────────────────
mkdir -p "$HERMES_BRAIN"
echo "{\"lastSync\": \"$(date -Iseconds)\", \"status\": \"ok\"}" > "$STATE_FILE"
echo "[Brain Sync] Done — $(date)"
