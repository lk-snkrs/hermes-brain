#!/bin/bash
# Brain Sync — Bidirectional sync entre local e VPS
# Uso: bash /root/.hermes/scripts/brain_sync.sh

set -e

SSH_HOST="root@72.60.150.124"
SSH_PORT="22"
SSH_PASS='+gryuk#TGk9JQF)q'
CEREBRO="/root/hermes-brain"
LOCAL="$HOME/.hermes"

echo "🧠 Hermes Brain Sync — $(date '+%Y-%m-%d %H:%M')"
echo "=================================================="

# ── 1. Push local → VPS ────────────────────────────────────────────────
echo ""
echo "📤 Push local → VPS..."
for file in memories/pending.md memories/lessons.md memories/decisions.md memories/lk.md memories/zipper.md memories/spiti.md; do
    local_path="$LOCAL/$file"
    if [ -f "$local_path" ]; then
        sshpass -p "$SSH_PASS" scp -o ConnectTimeout=10 -o StrictHostKeyChecking=no -P "$SSH_PORT" \
            "$local_path" "$SSH_HOST:$CEREBRO/$file" 2>/dev/null \
            && echo "  ✅ $file" || echo "  ❌ $file"
    fi
done

# ── 2. Pull VPS → local ────────────────────────────────────────────────
echo ""
echo "📥 Pull VPS → local..."

# Pull memories/
for file in pending.md lessons.md decisions.md lk.md zipper.md spiti.md; do
    remote_path="$CEREBRO/memories/$file"
    local_dest="$LOCAL/memories/$file"
    mkdir -p "$(dirname "$local_dest")"
    sshpass -p "$SSH_PASS" ssh -o ConnectTimeout=10 -o StrictHostKeyChecking=no -p "$SSH_PORT" "$SSH_HOST" \
        "test -f $remote_path && cat $remote_path" 2>/dev/null > "$local_dest" \
        && echo "  ✅ memories/$file" || echo "  ⚠️  memories/$file (not found)"
done

# Pull root files
for file in HEARTBEAT.md PROTOCOLS.md; do
    remote_path="$CEREBRO/$file"
    local_dest="$LOCAL/$file"
    sshpass -p "$SSH_PASS" ssh -o ConnectTimeout=10 -o StrictHostKeyChecking=no -p "$SSH_PORT" "$SSH_HOST" \
        "test -f $remote_path && cat $remote_path" 2>/dev/null > "$local_dest" \
        && echo "  ✅ $file" || echo "  ⚠️  $file (not found)"
done

# ── 3. Diff summary ────────────────────────────────────────────────────
echo ""
echo "📊 Sync status:"
for file in memories/pending.md memories/lessons.md; do
    local_ts=$(stat -c %Y "$LOCAL/$file" 2>/dev/null || echo "0")
    remote_ts=$(sshpass -p "$SSH_PASS" ssh -o ConnectTimeout=10 -o StrictHostKeyChecking=no -p "$SSH_PORT" "$SSH_HOST" \
        "stat -c %Y $CEREBRO/$file 2>/dev/null" 2>/dev/null || echo "0")
    if [ "$local_ts" -gt "$remote_ts" ]; then
        echo "  ↗️  $file: local newer"
    elif [ "$remote_ts" -gt "$local_ts" ]; then
        echo "  ↘️  $file: VPS newer"
    else
        echo "  ✅ $file: synced"
    fi
done

echo ""
echo "🧠 Brain Sync — Done — $(date '+%H:%M')"
