#!/usr/bin/env python3
"""
Alert System for Hermes Monitor
Reads monitor state, evaluates alert rules, and dispatches notifications.
Supports: log, file, email (optional), and webhook notifications.
"""
import os
import sys
import json
import time
import signal
import smtplib
import logging
import urllib.request
import urllib.error
import subprocess
import asyncio
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional

# Use system Python
INTERP = "/usr/bin/python3"
if sys.executable != INTERP and os.path.exists(INTERP):
    os.execv(INTERP, [INTERP, __file__] + sys.argv[1:])

# ==============================================================================
# Configuration
# ==============================================================================
STATE_FILE = Path("/root/.hermes/hermes-agent/monitor-state.json")
ALERT_LOG = Path("/root/.hermes/hermes-agent/logs/alerts.log")
ALERT_HISTORY = Path("/root/.hermes/hermes-agent/alert_history.json")
CONFIG_FILE = Path("/root/.hermes/hermes-agent/alert_config.json")

LOG_FILE = Path("/root/.hermes/hermes-agent/logs/alert-daemon.log")

# Default thresholds (can be overridden by config)
DEFAULT_CONFIG = {
    "cpu_percent_critical": 95.0,
    "cpu_percent_warning": 85.0,
    "memory_percent_critical": 95.0,
    "memory_percent_warning": 85.0,
    "disk_percent_critical": 90.0,
    "disk_percent_warning": 80.0,
    "swap_percent_critical": 50.0,
    "alert_interval_seconds": 300,  # 5 min between repeat alerts
    "enable_log": True,
    "enable_file": True,
    "enable_webhook": False,
    "webhook_url": "",
    "enable_email": False,
    "email_to": "",
    "email_from": "",
    "smtp_host": "localhost",
    "smtp_port": 25,
    "enable_telegram": True,
    "remediate_before_notify": True,
    "remediate_script": "/root/.hermes/hermes-agent/hermes_remediate.sh",
}

# ==============================================================================
# Logging
# ==============================================================================
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [ALERT] %(levelname)s: %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("alert_system")

# ==============================================================================
# Config Management
# ==============================================================================
def load_config() -> dict:
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE) as f:
                user = json.load(f)
                config = DEFAULT_CONFIG.copy()
                config.update(user)
                return config
        except (json.JSONDecodeError, IOError) as e:
            logger.warning(f"Could not load config: {e}, using defaults")
    return DEFAULT_CONFIG.copy()

def save_config(config: dict):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)

# ==============================================================================
# Alert History
# ==============================================================================
def load_history() -> list:
    if ALERT_HISTORY.exists():
        try:
            with open(ALERT_HISTORY) as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return []

def save_history(history: list):
    # Keep last 1000 alerts
    history = history[-1000:]
    with open(ALERT_HISTORY, "w") as f:
        json.dump(history, f, indent=2)

# ==============================================================================
# Alert Evaluation
# ==============================================================================
class Alert:
    def __init__(self, level: str, metric: str, value: float, threshold: float, message: str, raw: dict = None):
        self.level = level  # INFO, WARNING, CRITICAL
        self.metric = metric
        self.value = value
        self.threshold = threshold
        self.message = message
        self.raw = raw or {}
        self.timestamp = datetime.now().isoformat()
        self.id = f"{metric}_{int(time.time())}"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "level": self.level,
            "metric": self.metric,
            "value": self.value,
            "threshold": self.threshold,
            "message": self.message,
            "timestamp": self.timestamp,
            "raw": self.raw,
        }

    def __str__(self):
        icon = {"INFO": "ℹ️", "WARNING": "⚠️", "CRITICAL": "🚨"}.get(self.level, "•")
        return f"{icon} [{self.level}] {self.metric}: {self.value:.1f} (threshold: {self.threshold}) - {self.message}"


def evaluate_state(state: dict, config: dict) -> list[Alert]:
    """Evaluate current monitor state and generate alerts."""
    alerts = []
    now = datetime.now()

    # CPU
    cpu_pct = state.get("cpu", {}).get("percent", 0)
    if cpu_pct >= config["cpu_percent_critical"]:
        alerts.append(Alert("CRITICAL", "cpu_percent", cpu_pct, config["cpu_percent_critical"], "CPU usage critically high"))
    elif cpu_pct >= config["cpu_percent_warning"]:
        alerts.append(Alert("WARNING", "cpu_percent", cpu_pct, config["cpu_percent_warning"], "CPU usage elevated"))

    # Memory
    mem_pct = state.get("memory", {}).get("virtual", {}).get("percent", 0)
    if mem_pct >= config["memory_percent_critical"]:
        alerts.append(Alert("CRITICAL", "memory_percent", mem_pct, config["memory_percent_critical"], "Memory usage critically high"))
    elif mem_pct >= config["memory_percent_warning"]:
        alerts.append(Alert("WARNING", "memory_percent", mem_pct, config["memory_percent_warning"], "Memory usage elevated"))

    # Swap
    swap_pct = state.get("memory", {}).get("swap", {}).get("percent", 0)
    if swap_pct >= config["swap_percent_critical"]:
        alerts.append(Alert("CRITICAL", "swap_percent", swap_pct, config["swap_percent_critical"], "Swap usage critically high"))

    # Disk
    for part in state.get("disk", {}).get("partitions", []):
        mount = part["mountpoint"].replace("/", "_").replace(".", "")
        disk_pct = part["percent"]
        if disk_pct >= config["disk_percent_critical"]:
            alerts.append(Alert("CRITICAL", f"disk_{mount}", disk_pct, config["disk_percent_critical"], f"Disk {part['mountpoint']} nearly full"))
        elif disk_pct >= config["disk_percent_warning"]:
            alerts.append(Alert("WARNING", f"disk_{mount}", disk_pct, config["disk_percent_warning"], f"Disk {part['mountpoint']} usage high"))

    # Load average
    load_avg = state.get("cpu", {}).get("load_avg", [0, 0, 0])
    cores = state.get("cpu", {}).get("count_logical", 1)
    load_per_core = load_avg[0] / cores if cores else load_avg[0]
    if load_per_core >= 2.0:
        alerts.append(Alert("CRITICAL" if load_per_core >= 3.0 else "WARNING", "load_avg", load_avg[0], cores * 2, f"System load high: {load_avg[0]:.2f}"))

    # Process anomalies
    proc_count = state.get("processes", {}).get("count", 0)
    if proc_count >= 500:
        alerts.append(Alert("WARNING", "process_count", proc_count, 500, f"High process count: {proc_count}"))

    return alerts


# ==============================================================================
# Alert Dispatchers
# ==============================================================================
def dispatch_log(alert: Alert, config: dict):
    """Log alert to standard logger."""
    if config["enable_log"]:
        log_fn = logger.critical if alert.level == "CRITICAL" else logger.warning if alert.level == "WARNING" else logger.info
        log_fn(str(alert))


def dispatch_file(alert: Alert, config: dict):
    """Write alert to alert log file."""
    if config["enable_file"]:
        ALERT_LOG.parent.mkdir(parents=True, exist_ok=True)
        with open(ALERT_LOG, "a") as f:
            f.write(f"[{alert.timestamp}] {alert}\n")


def dispatch_webhook(alert: Alert, config: dict):
    """Send alert to webhook URL."""
    if config["enable_webhook"] and config["webhook_url"]:
        try:
            data = json.dumps(alert.to_dict()).encode("utf-8")
            req = urllib.request.Request(
                config["webhook_url"],
                data=data,
                headers={"Content-Type": "application/json"},
                method="POST"
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                logger.info(f"Webhook sent: {resp.status}")
        except Exception as e:
            logger.error(f"Webhook failed: {e}")


def dispatch_email(alert: Alert, config: dict):
    """Send alert via email."""
    if config["enable_email"] and config.get("email_to") and config.get("email_from"):
        try:
            import email.mime.text as mime_text
            import email.mime.multipart as mime_multipart

            msg = mime_multipart.MIMEMultipart()
            msg["From"] = config["email_from"]
            msg["To"] = config["email_to"]
            msg["Subject"] = f"[{alert.level}] Hermes Alert: {alert.metric}"
            body = f"Hermes System Alert\n\n{str(alert)}\n\nMetric: {alert.metric}\nValue: {alert.value}\nThreshold: {alert.threshold}\nTime: {alert.timestamp}\n\nMessage: {alert.message}"
            msg.attach(mime_text.MIMEText(body, "plain"))

            with smtplib.SMTP(config["smtp_host"], config["smtp_port"]) as server:
                server.send_message(msg)
            logger.info(f"Email sent for {alert.metric}")
        except Exception as e:
            logger.error(f"Email failed: {e}")


def dispatch_telegram(alert: Alert, config: dict):
    """Send alert via Telegram bot."""
    if not config.get("enable_telegram", False):
        return

    try:
        # Try to load Telegram config from gateway config
        import yaml
        cfg_path = Path("/root/.hermes/config.yaml")
        bot_token = None
        chat_id = None

        if cfg_path.exists():
            try:
                with open(cfg_path) as f:
                    cfg = yaml.safe_load(f) or {}
                    platforms = cfg.get("platforms", {}) or {}
                    telegram_cfg = platforms.get("telegram", {}) or {}
                    bot_token = telegram_cfg.get("bot_token") or telegram_cfg.get("token")
                    chat_id = telegram_cfg.get("home_channel") or telegram_cfg.get("chat_id")
            except Exception:
                pass

        # Fallback to env vars
        if not bot_token:
            import os
            bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
        if not chat_id:
            import os
            chat_id = os.getenv("TELEGRAM_HOME_CHANNEL")

        if not bot_token or not chat_id:
            logger.debug("Telegram not configured (no bot_token or chat_id)")
            return

        # Format message with emoji based on level
        level_emoji = {"CRITICAL": "🚨", "WARNING": "⚠️", "INFO": "ℹ️"}.get(alert.level, "•")
        message = (
            f"{level_emoji} <b>Hermes Alert: {alert.level}</b>\n"
            f"<b>Metric:</b> {alert.metric}\n"
            f"<b>Value:</b> {alert.value:.1f}\n"
            f"<b>Threshold:</b> {alert.threshold:.1f}\n"
            f"<b>Message:</b> {alert.message}\n"
            f"<b>Time:</b> {alert.timestamp}"
        )

        import urllib.request
        import urllib.error

        data = json.dumps({"chat_id": str(chat_id), "text": message, "parse_mode": "HTML"}).encode("utf-8")
        req = urllib.request.Request(
            f"https://api.telegram.org/bot{bot_token}/sendMessage",
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            if resp.status == 200:
                logger.info(f"Telegram notification sent for {alert.metric}")
            else:
                logger.warning(f"Telegram returned status {resp.status}")

    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        logger.error(f"Telegram HTTP error {e.code}: {body[:200]}")
    except Exception as e:
        logger.error(f"Telegram dispatch failed: {e}")


def attempt_remediation(alert: Alert, config: dict) -> bool:
    """Attempt to automatically remediate an alert.

    Returns True if remediation was attempted (may or may not have succeeded).
    Returns False if remediation was not attempted.
    """
    if not config.get("remediate_before_notify", True):
        return False

    script_path = config.get("remediate_script", "/root/.hermes/hermes-agent/hermes_remediate.sh")
    if not Path(script_path).exists():
        return False

    # Only remediate WARNING and CRITICAL alerts
    if alert.level == "INFO":
        return False

    try:
        metric_arg = alert.metric
        value_arg = str(alert.value)
        threshold_arg = str(alert.threshold)

        logger.info(f"Attempting remediation for {alert.metric} (value={alert.value})")

        result = subprocess.run(
            [script_path, metric_arg, value_arg, threshold_arg],
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.stdout:
            for line in result.stdout.strip().split("\n"):
                if line.strip():
                    logger.info(f"Remediation: {line}")

        return_code = result.returncode
        # Return codes: 0 = remediated, 1 = failed, 2 = no action needed
        if return_code == 0:
            logger.info(f"Remediation succeeded for {alert.metric}")
            return True
        elif return_code == 1:
            logger.warning(f"Remediation failed for {alert.metric}: {result.stderr[:200] if result.stderr else 'unknown'}")
            return True  # Attempted but failed
        else:
            logger.debug(f"No remediation action for {alert.metric}")
            return False

    except subprocess.TimeoutExpired:
        logger.error(f"Remediation timed out for {alert.metric}")
        return True
    except Exception as e:
        logger.error(f"Remediation error for {alert.metric}: {e}")
        return False


def dispatch_all(alert: Alert, config: dict):
    """Send alert through all configured channels."""
    dispatch_log(alert, config)
    dispatch_file(alert, config)
    dispatch_webhook(alert, config)
    dispatch_email(alert, config)
    dispatch_telegram(alert, config)


# ==============================================================================
# Alert Manager - Deduplication and Rate Limiting
# ==============================================================================
class AlertManager:
    def __init__(self, config: dict):
        self.config = config
        self.last_alerts = {}  # metric -> last_alert_time
        self.active_alerts = {}  # metric -> Alert

    def should_fire(self, alert: Alert) -> bool:
        """Check if alert should fire based on rate limiting.

        Key includes both metric AND severity so WARNING and CRITICAL
        are rate-limited independently (not shared bucket).
        """
        key = f"{alert.metric}:{alert.level}"
        last = self.last_alerts.get(key)
        interval = self.config["alert_interval_seconds"]

        if last is None:
            return True

        elapsed = (datetime.now() - last).total_seconds()
        return elapsed >= interval

    def process(self, alerts: list[Alert]) -> list[Alert]:
        """Process list of alerts, deduplicating and rate limiting.

        For WARNING and CRITICAL alerts, attempts auto-remediation first.
        If remediation succeeds (return code 0), skips notification.
        If remediation failed or wasn't attempted, proceeds with normal dispatch.
        """
        fired = []
        for alert in alerts:
            if self.should_fire(alert):
                self.last_alerts[alert.metric] = datetime.now()
                self.active_alerts[alert.metric] = alert

                # Attempt remediation before notifying
                remedied = attempt_remediation(alert, self.config)
                if remedied:
                    # Still dispatch but note remediation was attempted
                    logger.info(f"Alert {alert.metric} dispatched after remediation attempt")
                    dispatch_all(alert, self.config)
                else:
                    dispatch_all(alert, self.config)

                fired.append(alert)
        return fired

    def get_active(self) -> dict:
        """Return currently active (unresolved) alerts by metric."""
        return self.active_alerts.copy()


# ==============================================================================
# Main Alert Processing
# ==============================================================================
def read_state() -> Optional[dict]:
    if not STATE_FILE.exists():
        return None
    try:
        with open(STATE_FILE) as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return None


def process_once():
    """Process alerts once (for cron-based alerting)."""
    config = load_config()
    state = read_state()
    if not state:
        logger.warning("No monitor state file found, is the daemon running?")
        return []

    alerts = evaluate_state(state, config)
    manager = AlertManager(config)
    fired = manager.process(alerts)

    # Update history
    history = load_history()
    for a in fired:
        history.append(a.to_dict())
    save_history(history)

    return fired


def main():
    """Run as a daemon processing alerts periodically."""
    config = load_config()
    manager = AlertManager(config)
    history = load_history()

    logger.info("Alert system started")
    logger.info(f"Monitoring: {STATE_FILE}")
    logger.info(f"Alert interval: {config['alert_interval_seconds']}s")

    while True:
        try:
            state = read_state()
            if state:
                alerts = evaluate_state(state, config)
                fired = manager.process(alerts)
                for a in fired:
                    history.append(a.to_dict())
                if fired:
                    logger.info(f"Fired {len(fired)} alerts")
                    save_history(history)
            else:
                logger.debug("No state file yet")

        except Exception as e:
            logger.error(f"Error processing alerts: {e}", exc_info=True)

        time.sleep(config["alert_interval_seconds"])


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--once":
        fired = process_once()
        if fired:
            print(f"Fired {len(fired)} alerts:")
            for a in fired:
                print(f"  {a}")
        else:
            print("No new alerts")
    else:
        main()
