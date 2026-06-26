#!/usr/bin/env python3
"""
Read-only host Docker observability for Lucas/Cimino Hermes production.

Runs from the Hermes container, fetches lc.vps SSH credentials from Doppler at runtime,
and executes only read-only Docker/Hermes inspection commands on the host. It never
prints secrets, does not mutate Docker, and does not restart anything.

Default behavior prints a sanitized JSON report. With --watchdog, prints only alerts;
empty stdout means OK.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import pathlib
import re
import subprocess
import sys
import tempfile
import textwrap
import time
import urllib.request
from datetime import datetime, timezone

TOKEN_FILE = pathlib.Path("/opt/data/hermes_bruno_ingest/.secrets/doppler_token")
PROJECT = "lc-keys"
CONFIG = "prd"
EXPECTED_CONTAINERS = [
    "hermes-agent-5ajw-hermes-agent-1",
    "hermes-agent-5ajw-hermes-telegram-1",
]
EXPECTED_VERSION = "Hermes Agent v0.14.0 (2026.5.16)"
EXPECTED_IMAGE_FRAGMENT = "hermes-agent-custom:v0.14.0-20260516"
DEFAULT_OUTPUT = pathlib.Path("/opt/data/hermes_bruno_ingest/hermes-brain/reports/hermes-host-docker-observability-latest.json")

SECRET_PATTERNS = [
    re.compile(r'(token|api[_-]?key|secret|password|passwd|pwd|authorization|client_secret|access_token)([=:\\s]+)([^\\s\'\"`]+)', re.I),
    re.compile(r'(ttyd\\s+-c\\s+[^:\\s]+:)([^\\s]+)', re.I),
    re.compile(r'(https?://[^\\s]*?(?:token|key|secret|password|access_token)=)([^&\\s]+)', re.I),
    re.compile(r'(Bearer\\s+)([^\\s]+)', re.I),
]


def scrub(text: str) -> str:
    if not text:
        return ""
    out = text
    for pat in SECRET_PATTERNS:
        out = pat.sub(lambda m: m.group(1) + (m.group(2) if len(m.groups()) > 2 else "") + "[REDACTED]", out)
    return out


def doppler_secrets(names: list[str]) -> dict[str, str]:
    token = os.getenv("DOPPLER_TOKEN")
    if not token and TOKEN_FILE.exists():
        token = TOKEN_FILE.read_text().strip()
    if not token:
        raise RuntimeError("Doppler token unavailable")
    url = f"https://api.doppler.com/v3/configs/config/secrets?project={PROJECT}&config={CONFIG}"
    auth = base64.b64encode((token + ":").encode()).decode()
    req = urllib.request.Request(url, headers={"Authorization": "Basic " + auth})
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = json.load(resp).get("secrets", {})
    result: dict[str, str] = {}
    for name in names:
        item = data.get(name, {})
        value = item.get("computed") or item.get("raw") or ""
        if value:
            result[name] = value
    return result


def run_ssh(host: str, password: str, remote_script: str, timeout: int = 35) -> subprocess.CompletedProcess[str]:
    with tempfile.TemporaryDirectory(prefix="hermes-host-observability-") as td:
        askpass = pathlib.Path(td) / "askpass.sh"
        askpass.write_text("#!/bin/sh\nprintf '%s' \"$HERMES_SSH_PASSWORD\"\n")
        askpass.chmod(0o700)
        env = os.environ.copy()
        env.update({
            "SSH_ASKPASS": str(askpass),
            "SSH_ASKPASS_REQUIRE": "force",
            "DISPLAY": ":0",
            "HERMES_SSH_PASSWORD": password,
        })
        cmd = [
            "ssh",
            "-o", "PubkeyAuthentication=no",
            "-o", "PreferredAuthentications=password",
            "-o", "NumberOfPasswordPrompts=1",
            "-o", "BatchMode=no",
            "-o", "ConnectTimeout=8",
            "-o", "StrictHostKeyChecking=accept-new",
            f"root@{host}",
            "bash -s",
        ]
        return subprocess.run(cmd, input=remote_script, text=True, capture_output=True, timeout=timeout, env=env)


def build_remote_script(log_tail: int) -> str:
    containers = " ".join(EXPECTED_CONTAINERS)
    return textwrap.dedent(f"""
        set -uo pipefail
        echo '__HOST__'
        hostname || true
        date -Is || true
        echo '__DOCKER_PS__'
        for c in {containers}; do
          docker ps -a --filter "name=$c" --format '{{{{json .}}}}' || true
        done
        echo '__VERSIONS__'
        for c in {containers}; do
          echo "### $c"
          docker exec "$c" /opt/hermes/.venv/bin/hermes --version 2>&1 || docker exec "$c" hermes --version 2>&1 || true
        done
        echo '__CRON_STATUS__'
        docker exec hermes-agent-5ajw-hermes-telegram-1 /opt/hermes/.venv/bin/hermes cron status 2>&1 || true
        echo '__CRON_LIST__'
        docker exec hermes-agent-5ajw-hermes-telegram-1 /opt/hermes/.venv/bin/hermes cron list --all 2>&1 || true
        echo '__RECENT_LOGS_TELEGRAM__'
        docker logs --tail {int(log_tail)} hermes-agent-5ajw-hermes-telegram-1 2>&1 || true
    """).strip() + "\n"


def section(raw: str, name: str) -> str:
    marker = f"__{name}__"
    m = re.search(rf"^{re.escape(marker)}\n(.*?)(?=^__[A-Z_]+__\n|\Z)", raw, re.M | re.S)
    return m.group(1).strip() if m else ""


def parse_report(raw: str, stderr: str) -> dict:
    clean_raw = scrub(raw)
    logs = section(clean_raw, "RECENT_LOGS_TELEGRAM")
    docker_lines = [ln for ln in section(clean_raw, "DOCKER_PS").splitlines() if ln.strip()]
    containers = []
    alerts = []
    for ln in docker_lines:
        try:
            item = json.loads(ln)
        except Exception:
            continue
        containers.append({
            "name": item.get("Names") or item.get("Names"),
            "image": item.get("Image"),
            "status": item.get("Status"),
            "state": item.get("State"),
        })
    found = {c.get("name") for c in containers}
    for expected in EXPECTED_CONTAINERS:
        if expected not in found:
            alerts.append(f"Container esperado não encontrado: {expected}")
    for c in containers:
        if c.get("state") != "running":
            alerts.append(f"Container não está running: {c.get('name')} state={c.get('state')} status={c.get('status')}")
        image = c.get("image") or ""
        if EXPECTED_IMAGE_FRAGMENT not in image:
            alerts.append(f"Imagem inesperada em {c.get('name')}: {image}")
    versions = section(clean_raw, "VERSIONS")
    for expected in EXPECTED_CONTAINERS:
        block_match = re.search(rf"### {re.escape(expected)}\n(.*?)(?=^### |\Z)", versions, re.M | re.S)
        block = block_match.group(1).strip() if block_match else ""
        if EXPECTED_VERSION not in block:
            alerts.append(f"Versão esperada não confirmada em {expected}")
    cron_status = section(clean_raw, "CRON_STATUS")
    if "Gateway is not running" in cron_status:
        # Known detector discrepancy: report as warning, not production-down by itself.
        alerts.append("Detector `hermes cron status` ainda reporta gateway parado; verificar junto com logs/processo antes de ação.")
    bad_log_lines = []
    for ln in logs.splitlines():
        if re.search(r"traceback|fatal|error|exception|polling conflict|failed", ln, re.I):
            bad_log_lines.append(ln[-500:])
    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "host": section(clean_raw, "HOST").splitlines()[:2],
        "containers": containers,
        "versions_sanitized": versions.splitlines()[:20],
        "cron_status_sanitized": cron_status.splitlines()[:40],
        "cron_list_sanitized": section(clean_raw, "CRON_LIST").splitlines()[:80],
        "recent_log_alert_lines_sanitized": bad_log_lines[-25:],
        "alerts": alerts,
        "stderr_sanitized": scrub(stderr)[-1000:],
        "mode": "read-only; no Docker/container/restart/write action executed",
    }
    return report


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--watchdog", action="store_true", help="silent on OK; print alerts only")
    ap.add_argument("--output", default=str(DEFAULT_OUTPUT), help="write sanitized JSON report here")
    ap.add_argument("--log-tail", type=int, default=80)
    args = ap.parse_args()

    try:
        secrets = doppler_secrets(["VPS_IP", "VPS_ROOT_PASSWORD"])
        host = secrets.get("VPS_IP") or "72.60.150.124"
        password = secrets.get("VPS_ROOT_PASSWORD")
        if not password:
            raise RuntimeError("VPS_ROOT_PASSWORD unavailable")
        proc = run_ssh(host, password, build_remote_script(args.log_tail))
        if proc.returncode != 0:
            report = {
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "alerts": [f"SSH read-only observability failed rc={proc.returncode}"],
                "stdout_sanitized": scrub(proc.stdout)[-1200:],
                "stderr_sanitized": scrub(proc.stderr)[-1200:],
                "mode": "read-only; no Docker/container/restart/write action executed",
            }
        else:
            report = parse_report(proc.stdout, proc.stderr)
        out = pathlib.Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
        alerts = report.get("alerts") or []
        if args.watchdog:
            if alerts:
                print("Hermes host Docker observability alert")
                for a in alerts:
                    print(f"- {a}")
                print(f"Relatório sanitizado: {out}")
        else:
            print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0
    except Exception as e:
        msg = f"Hermes host Docker observability failed: {type(e).__name__}: {scrub(str(e))}"
        if args.watchdog:
            print(msg)
        else:
            print(json.dumps({"generated_at": datetime.now(timezone.utc).isoformat(), "alerts": [msg]}, ensure_ascii=False, indent=2))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
