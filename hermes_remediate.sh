#!/usr/bin/env bash
# =============================================================================
# hermes_remediate.sh - Auto-remediation script for Hermes Monitor Alerts
# Called by alert_system.py before sending notifications when issues are detected.
# Usage: hermes_remediate.sh METRIC VALUE THRESHOLD
# Returns: 0 = remediated/ok, 1 = could not remediate, 2 = no action needed
# =============================================================================
set -euo pipefail

# Args: METRIC VALUE THRESHOLD
METRIC="${1:-}"
VALUE="${2:-}"
THRESHOLD="${3:-}"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] REMEDIATE: $*"; }
warn() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] REMEDIATE WARNING: $*" >&2; }
die() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] REMEDIATE ERROR: $*" >&2; exit 1; }

HERMES_DIR="/root/.hermes/hermes-agent"
STATE_FILE="${HERMES_DIR}/monitor-state.json"

# Load Telegram config if available
load_telegram_config() {
    if [[ -f "${HERMES_DIR}/gateway_config.json" ]]; then
        TELEGRAM_BOT_TOKEN=$(python3 -c "import json; d=json.load(open('${HERMES_DIR}/gateway_config.json')); print(d.get('platforms',{}).get('telegram',{}).get('token',''))" 2>/dev/null || echo "")
        TELEGRAM_CHAT_ID=$(python3 -c "import json; d=json.load(open('${HERMES_DIR}/gateway_config.json')); print(d.get('platforms',{}).get('telegram',{}).get('home_channel',{}).get('chat_id',''))" 2>/dev/null || echo "")
    fi
    # Fallback to env vars
    : "${TELEGRAM_BOT_TOKEN:=${TELEGRAM_BOT_TOKEN:-}}"
    : "${TELEGRAM_CHAT_ID:=${TELEGRAM_HOME_CHANNEL:-}}"
}

send_telegram() {
    local msg="$1"
    load_telegram_config
    if [[ -n "${TELEGRAM_BOT_TOKEN:-}" && -n "${TELEGRAM_CHAT_ID:-}" ]]; then
        curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
            -d "chat_id=${TELEGRAM_CHAT_ID}" \
            -d "text=${msg}" \
            -d "parse_mode=HTML" \
            > /dev/null 2>&1 || true
    fi
}

compare() {
    local op="$1"
    local val1="$2"
    local val2="$3"
    local result
    result=$(echo "${val1} ${op} ${val2}" | bc -l 2>/dev/null || echo "0")
    [[ "$result" == "1" ]]
}

case "${METRIC}" in
    cpu_percent)
        log "High CPU detected: ${VALUE}%"
        # Try to identify and kill runaway processes
        TOP_PROC=$(ps aux --sort=-%cpu | head -6 | tail -5 | awk '{print $2, $3"%", $11}' | head -3)
        log "Top CPU consumers: ${TOP_PROC}"

        # If load is critical, try to reduce
        if compare ">" "${VALUE}" "95"; then
            log "Critical CPU - attempting remediation..."

            # Clear page cache (requires root, may fail silently)
            sync || true
            echo 3 > /proc/sys/vm/drop_caches 2>/dev/null || true

            # Send SIGTERM to top CPU process (excluding essential)
            TOP_PID=$(ps aux --sort=-%cpu | grep -v PID | head -1 | awk '{print $2}')
            if [[ -n "${TOP_PID}" && -d "/proc/${TOP_PID}" ]]; then
                PROC_NAME=$(ps -p "${TOP_PID}" -o comm= 2>/dev/null || echo "unknown")
                # Don't kill critical system processes
                if [[ ! "${PROC_NAME}" =~ ^(systemd|kworker|init|kthreadd|runc|docker)$ ]]; then
                    log "Sending SIGTERM to runaway process ${TOP_PID} (${PROC_NAME})"
                    kill -15 "${TOP_PID}" 2>/dev/null || true
                    sleep 2
                    # If still alive, SIGKILL
                    if kill -0 "${TOP_PID}" 2>/dev/null; then
                        log "Process still alive, sending SIGKILL"
                        kill -9 "${TOP_PID}" 2>/dev/null || true
                    fi
                    send_telegram "🔥 <b>CPU Auto-Remediated</b>%0ATop process ${PROC_NAME} (PID ${TOP_PID}) terminated%0ACPU: ${VALUE}%"
                fi
            fi

            echo "0"
            exit 0
        fi
        echo "2"  # No action taken, alert will still notify
        exit 0
        ;;

    memory_percent)
        log "High Memory detected: ${VALUE}%"
        if compare ">" "${VALUE}" "90"; then
            log "Critical memory - attempting remediation..."

            # Try to free page cache
            sync || true
            echo 3 > /proc/sys/vm/drop_caches 2>/dev/null || true

            # Find and restart bloated services (common ones)
            for svc in apache2 nginx php-fpm docker; do
                if pgrep -x "${svc}" > /dev/null 2>&1; then
                    MEM_USAGE=$(ps aux | grep "${svc}" | grep -v grep | awk '{sum+=$6} END {printf "%.0f", sum/1024}')
                    if [[ -n "${MEM_USAGE}" && "${MEM_USAGE}" -gt 500 ]]; then
                        log "Restarting bloated ${svc} (using ${MEM_USAGE}MB)"
                        systemctl restart "${svc}" 2>/dev/null || true
                        send_telegram "💾 <b>Memory Auto-Remediated</b>%0A${svc} restarted (was using ${MEM_USAGE}MB)%0AMemory: ${VALUE}%"
                    fi
                fi
            done

            # Kill processes in 'D' state (uninterruptible sleep, often causing memory pressure)
            D_STATE_PIDS=$(ps aux | awk '$8 ~ /D/ {print $2}' | head -5)
            for pid in ${D_STATE_PIDS}; do
                log "Found D-state process ${pid}, attempting cleanup..."
                echo -n > /proc/"${pid}"/fd/1 2>/dev/null || true
            done

            echo "0"
            exit 0
        fi
        echo "2"
        exit 0
        ;;

    disk_*)
        log "High Disk detected: ${METRIC} = ${VALUE}%"
        # Skip snap mountpoints as they are read-only squashfs
        if [[ "${METRIC}" =~ snap_ ]]; then
            log "Skipping read-only snap mountpoint: ${METRIC}"
            echo "2"
            exit 0
        fi
        if compare ">" "${VALUE}" "85"; then
            log "Critical disk - attempting remediation..."

            # Clean common temp directories
            TEMP_DIRS="/tmp /var/tmp /root/.cache"
            for d in ${TEMP_DIRS}; do
                if [[ -d "${d}" ]]; then
                    SIZE_BEFORE=$(du -sm "${d}" 2>/dev/null | cut -f1 || echo 0)
                    # Remove files older than 7 days in tmp
                    find "${d}" -type f -mtime +7 -delete 2>/dev/null || true
                    SIZE_AFTER=$(du -sm "${d}" 2>/dev/null | cut -f1 || echo 0)
                    FREED=$((SIZE_BEFORE - SIZE_AFTER))
                    if [[ ${FREED} -gt 100 ]]; then
                        log "Cleaned ${d}: freed ${FREED}MB"
                    fi
                fi
            done

            # Clean pip cache
            pip cache purge 2>/dev/null || true

            # Clean apt cache
            apt-get clean 2>/dev/null || true

            # Clean docker dangling images
            if command -v docker &>/dev/null; then
                docker image prune -f 2>/dev/null || true
            fi

            # Clean log files if they're huge
            find "${HERMES_DIR}/logs" -name "*.log" -size +100M -exec truncate -s 50M {} \; 2>/dev/null || true

            send_telegram "💾 <b>Disk Auto-Remediated</b>%0AFreed space on ${METRIC}%0ADisk: ${VALUE}%"

            echo "0"
            exit 0
        fi
        echo "2"
        exit 0
        ;;

    swap_percent)
        log "High Swap detected: ${VALUE}%"
        if compare ">" "${VALUE}" "50"; then
            log "Critical swap - attempting remediation..."

            # Disable/clear swap temporarily and free memory
            sync || true
            echo 3 > /proc/sys/vm/drop_caches 2>/dev/null || true

            # Restart memory-heavy cron jobs
            pkill -f "lk_full_sync" 2>/dev/null || true
            pkill -f "meta_ads" 2>/dev/null || true
            pkill -f "klaviyo" 2>/dev/null || true

            send_telegram "💾 <b>Swap Auto-Remediated</b>%0ACleared caches, restarted heavy jobs%0ASwap: ${VALUE}%"

            echo "0"
            exit 0
        fi
        echo "2"
        exit 0
        ;;

    load_avg)
        log "High Load Average detected: ${VALUE}"
        if compare ">" "${VALUE}" "8"; then
            log "Critical load - attempting remediation..."

            # Find processes in uninterruptible sleep
            ps aux | awk '$8 ~ /D/ {print $2}' | while read pid; do
                log "Clearing D-state process ${pid}"
                kill -9 "${pid}" 2>/dev/null || true
            done

            # Restart docker if it's consuming resources
            if command -v docker &>/dev/null; then
                DOCKER_LOAD=$(docker stats --no-stream --format "{{.CPUPerc}}" | head -1 | tr -d '%' || echo 0)
                if compare ">" "${DOCKER_LOAD}" "80"; then
                    log "Docker high CPU at ${DOCKER_LOAD}%"
                    docker system prune -f 2>/dev/null || true
                fi
            fi

            send_telegram "📊 <b>Load Auto-Remediated</b>%0ACleaned up blocked processes%0ALoad: ${VALUE}"

            echo "0"
            exit 0
        fi
        echo "2"
        exit 0
        ;;

    process_count)
        log "High process count: ${VALUE}"
        if [[ "${VALUE}" -gt 600 ]]; then
            # Find and warn about zombie processes
            ZOMBIES=$(ps aux | awk '$8 ~ /Z/ {count++} END {print count+0}')
            if [[ "${ZOMBIES}" -gt 5 ]]; then
                log "Found ${ZOMBIES} zombie processes"
                # Try to reap zombies
                ps aux | awk '$8 ~ /Z/ {print $2}' | while read pid; do
                    parent=$(ps -o ppid= -p "${pid}" 2>/dev/null | tr -d ' ')
                    kill -9 "${pid}" 2>/dev/null || true
                    log "Killed zombie ${pid} (parent ${parent})"
                done
                send_telegram "🧟 <b>Zombie Processes Cleaned</b>%0AFound and cleared ${ZOMBIES} zombies%0AProcesses: ${VALUE}"
            fi
            echo "0"
            exit 0
        fi
        echo "2"
        exit 0
        ;;

    *)
        log "Unknown alert type: ${METRIC}"
        echo "2"
        exit 0
        ;;
esac

log "No remediation action for ${METRIC}"
echo "2"
exit 0
