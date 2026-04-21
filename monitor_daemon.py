#!/usr/bin/env python3
"""
Real-time System Monitoring Daemon
Monitors CPU, memory, disk, network, and process metrics.
Outputs to shared JSON state file for dashboard consumption.
"""
import os
import sys
import json
import time
import signal
import logging
import atexit
from pathlib import Path
from datetime import datetime

# Use system Python with psutil
INTERP = "/usr/bin/python3"
if sys.executable != INTERP and os.path.exists(INTERP):
    os.execv(INTERP, [INTERP, __file__] + sys.argv[1:])

import psutil

# ==============================================================================
# Configuration
# ==============================================================================
STATE_FILE = Path("/root/.hermes/hermes-agent/monitor-state.json")
PID_FILE = Path("/root/.hermes/hermes-agent/monitor-daemon.pid")
LOG_FILE = Path("/root/.hermes/hermes-agent/logs/monitor-daemon.log")

ALERT_THRESHOLDS = {
    "cpu_percent": 90.0,      # CPU usage %
    "memory_percent": 85.0,   # Memory usage %
    "disk_percent": 90.0,     # Disk usage %
    "swap_percent": 50.0,     # Swap usage %
    "load_avg": 4.0,          # Load average per core
    "temperature": 80.0,      # CPU temp °C
}

INTERVAL = 2  # seconds between updates

# ==============================================================================
# Logging Setup
# ==============================================================================
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [MONITOR] %(levelname)s: %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("monitor_daemon")

# ==============================================================================
# Global State
# ==============================================================================
running = True
alerts = []

def load_previous_state():
    """Load previous alert history to avoid duplicate alerts."""
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE) as f:
                data = json.load(f)
                return data.get("alerts", [])
        except (json.JSONDecodeError, IOError):
            pass
    return []

def save_state(state):
    """Atomically save state to JSON file."""
    tmp = STATE_FILE.with_suffix(".tmp")
    with open(tmp, "w") as f:
        json.dump(state, f, indent=2)
    tmp.rename(STATE_FILE)

def signal_handler(signum, frame):
    global running
    logger.info(f"Received signal {signum}, shutting down...")
    running = False

def cleanup():
    logger.info("Daemon cleanup, removing PID file")
    PID_FILE.unlink(missing_ok=True)

atexit.register(cleanup)
signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

# ==============================================================================
# Metric Collection
# ==============================================================================
def get_cpu_stats():
    """Collect CPU metrics."""
    try:
        # Initialize psutil CPU counter (first call always returns 0.0)
        psutil.cpu_percent(interval=0.1)
        return {
            "percent": psutil.cpu_percent(interval=None),
            "count": psutil.cpu_count(),
            "count_logical": psutil.cpu_count(logical=True),
            "load_avg": os.getloadavg() if hasattr(os, "getloadavg") else [0.0, 0.0, 0.0],
            "per_cpu": psutil.cpu_percent(interval=None, percpu=True),
            "freq": psutil.cpu_freq()._asdict() if psutil.cpu_freq() else None,
            "times": psutil.cpu_times()._asdict(),
        }
    except Exception as e:
        logger.error(f"Error getting CPU stats: {e}")
        return {}

def get_memory_stats():
    """Collect memory metrics."""
    try:
        vm = psutil.virtual_memory()
        swap = psutil.swap_memory()
        return {
            "virtual": vm._asdict(),
            "swap": swap._asdict(),
        }
    except Exception as e:
        logger.error(f"Error getting memory stats: {e}")
        return {}

def get_disk_stats():
    """Collect disk usage metrics."""
    try:
        partitions = []
        for part in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(part.mountpoint)
                partitions.append({
                    "device": part.device,
                    "mountpoint": part.mountpoint,
                    "fstype": part.fstype,
                    "total": usage.total,
                    "used": usage.used,
                    "free": usage.free,
                    "percent": usage.percent,
                })
            except PermissionError:
                continue
        io = psutil.disk_io_counters()
        io_data = io._asdict() if io else {}
        return {"partitions": partitions, "io": io_data}
    except Exception as e:
        logger.error(f"Error getting disk stats: {e}")
        return {}

def get_network_stats():
    """Collect network I/O metrics."""
    try:
        io = psutil.net_io_counters()
        per_nic = {}
        for iface, counters in psutil.net_io_counters(pernic=True).items():
            per_nic[iface] = counters._asdict()
        return {
            "total": io._asdict(),
            "per_nic": per_nic,
        }
    except Exception as e:
        logger.error(f"Error getting network stats: {e}")
        return {}

def get_process_stats():
    """Collect top processes by CPU and memory."""
    try:
        procs = []
        for p in psutil.process_iter(["pid", "name", "username", "cpu_percent", "memory_percent", "status"]):
            try:
                info = p.info
                procs.append(info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        # Sort by CPU
        by_cpu = sorted(procs, key=lambda x: x.get("cpu_percent", 0) or 0, reverse=True)[:10]
        by_mem = sorted(procs, key=lambda x: x.get("memory_percent", 0) or 0, reverse=True)[:10]
        return {"by_cpu": by_cpu, "by_memory": by_mem, "count": len(procs)}
    except Exception as e:
        logger.error(f"Error getting process stats: {e}")
        return {}

def get_boot_time():
    """Get system boot time."""
    try:
        return datetime.fromtimestamp(psutil.boot_time()).isoformat()
    except Exception:
        return None

# ==============================================================================
# Alerting
# ==============================================================================
def check_thresholds(state):
    """Check metrics against thresholds and generate alerts."""
    global alerts
    new_alerts = []
    timestamp = datetime.now().isoformat()

    # CPU
    cpu_pct = state.get("cpu", {}).get("percent", 0)
    if cpu_pct >= ALERT_THRESHOLDS["cpu_percent"]:
        new_alerts.append({"level": "WARNING", "metric": "cpu_percent", "value": cpu_pct, "threshold": ALERT_THRESHOLDS["cpu_percent"], "timestamp": timestamp})

    # Memory
    mem_pct = state.get("memory", {}).get("virtual", {}).get("percent", 0)
    if mem_pct >= ALERT_THRESHOLDS["memory_percent"]:
        new_alerts.append({"level": "CRITICAL" if mem_pct >= 95 else "WARNING", "metric": "memory_percent", "value": mem_pct, "threshold": ALERT_THRESHOLDS["memory_percent"], "timestamp": timestamp})

    # Disk (exclude snap/squashfs loop devices — they are read-only and expected at 100%)
    for part in state.get("disk", {}).get("partitions", []):
        mount = part.get("mountpoint", "")
        fstype = part.get("fstype", "")
        # Skip snap loop devices (squashfs read-only images)
        if "/snap/" in mount or fstype == "squashfs":
            continue
        if part["percent"] >= ALERT_THRESHOLDS["disk_percent"]:
            new_alerts.append({"level": "CRITICAL", "metric": f"disk_{mount}", "value": part["percent"], "threshold": ALERT_THRESHOLDS["disk_percent"], "timestamp": timestamp})

    # Load average
    load1 = state.get("cpu", {}).get("load_avg", [0])[0] if state.get("cpu", {}).get("load_avg") else 0
    cores = state.get("cpu", {}).get("count_logical", 1)
    if load1 >= ALERT_THRESHOLDS["load_avg"]:
        new_alerts.append({"level": "WARNING", "metric": "load_avg_1m", "value": load1, "threshold": ALERT_THRESHOLDS["load_avg"], "timestamp": timestamp})

    # Deduplicate - only alert if not same metric in last 300 seconds (5 min)
    recent = [a for a in alerts if (datetime.now() - datetime.fromisoformat(a["timestamp"])).total_seconds() < 300]
    for na in new_alerts:
        if not any(a["metric"] == na["metric"] for a in recent):
            alerts.append(na)
            logger.warning(f"ALERT: {na['metric']} = {na['value']:.1f} (threshold: {na['threshold']})")

    # Keep only last 100 alerts
    alerts = alerts[-100:]

# ==============================================================================
# Main Loop
# ==============================================================================
def main():
    global running

    logger.info("=" * 60)
    logger.info("Hermes Monitoring Daemon starting")
    logger.info(f"State file: {STATE_FILE}")
    logger.info(f"Interval: {INTERVAL}s")
    logger.info(f"Thresholds: {ALERT_THRESHOLDS}")
    logger.info("=" * 60)

    # Write PID file
    with open(PID_FILE, "w") as f:
        f.write(str(os.getpid()))

    previous_state = load_previous_state()
    start_time = datetime.now().isoformat()

    while running:
        try:
            state = {
                "timestamp": datetime.now().isoformat(),
                "uptime": start_time,
                "hostname": os.uname().nodename,
                "cpu": get_cpu_stats(),
                "memory": get_memory_stats(),
                "disk": get_disk_stats(),
                "network": get_network_stats(),
                "processes": get_process_stats(),
                "boot_time": get_boot_time(),
                "thresholds": ALERT_THRESHOLDS,
                "alerts": alerts[-20:],  # Last 20 alerts
            }

            check_thresholds(state)
            save_state(state)

        except Exception as e:
            logger.error(f"Error in main loop: {e}", exc_info=True)

        # Sleep in small increments for responsive shutdown
        for _ in range(INTERVAL * 10):
            if not running:
                break
            time.sleep(0.1)

    logger.info("Daemon stopped gracefully")

if __name__ == "__main__":
    main()
