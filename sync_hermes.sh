#!/bin/bash
# DEPRECATED / DO NOT RUN: legacy Hermes Brain script retained only for historical/reference audit. Not part of current runtime.
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

# ── Hard deprecation guard ────────────────────────────────────────────────
# This legacy script references the old /root/cerebro-cimino path and is NOT
# part of the current runtime. The canonical brain is lk-snkrs/hermes-brain
# (branch main). Refuse to run unless explicitly opted in for audit, so it can
# never silently clobber the canonical brain.
# See governance/protocols/brain-write-coordination.md.
if [ "${HERMES_ALLOW_DEPRECATED_SYNC:-0}" != "1" ]; then
    echo "[Brain Sync] DEPRECATED: sync_hermes.sh is retained for reference only and must not run."
    echo "[Brain Sync] Canonical brain = lk-snkrs/hermes-brain (main). See governance/protocols/brain-write-coordination.md."
    echo "[Brain Sync] To force-run for audit only, set HERMES_ALLOW_DEPRECATED_SYNC=1 (concurrency-safe git pattern applies)."
    exit 0
fi

SSH_HOST="root@72.60.150.124"
SSH_PORT="22"
# Senha via Doppler (lc-keys/prd) ou env var HERMES_VPS_SSH_PASS.
# Nunca commitar senha hardcoded aqui.
SSH_PASS="${HERMES_VPS_SSH_PASS:-$(doppler secrets get HERMES_VPS_SSH_PASS --plain -p lc-keys -c prd 2>/dev/null)}"
if [ -z "$SSH_PASS" ]; then
    echo "[Brain Sync] ERROR: HERMES_VPS_SSH_PASS não encontrado (Doppler nem env). Abortando."
    exit 1
fi

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

# ── Auto-commit local changes (concurrency-safe) ──────────────────────────
# Two rules that prevent clobbering a brain that another writer (HERMES VPS
# runtime or CLAUDE via PR) may have advanced:
#   1. Scope `git add` to the intended files. Never `git add -A` in a shared
#      clone — it sweeps unrelated work-in-progress and junk (e.g. .DS_Store).
#   2. Pull-before-push: rebase onto the latest main before pushing, and retry
#      once if the remote advanced mid-flight. Never force-push main.
if [ -d "$GIT_DIR" ]; then
    cd "$GIT_DIR"
    git add memories/pending.md memories/lessons.md 2>/dev/null || true
    if ! git diff --cached --quiet; then
        TIMESTAMP=$(date '+%Y-%m-%d %H:%M')
        git commit -m "brain sync $TIMESTAMP"
        for attempt in 1 2; do
            if ! git pull --rebase --autostash origin main; then
                echo "[Brain Sync] Rebase conflict — manual resolution needed; not pushing."
                break
            fi
            if git push origin main; then
                echo "  ✓ Committed & pushed: $TIMESTAMP"
                break
            fi
            echo "[Brain Sync] Push rejected (attempt $attempt) — remote advanced; rebasing and retrying."
        done
    else
        echo "  — No changes"
    fi
fi

# ── Sync state ──────────────────────────────────────────────────────────
mkdir -p "$HERMES_BRAIN"
echo "{\"lastSync\": \"$(date -Iseconds)\", \"status\": \"ok\"}" > "$STATE_FILE"
echo "[Brain Sync] Done — $(date)"
