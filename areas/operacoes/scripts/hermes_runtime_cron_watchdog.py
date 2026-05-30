#!/usr/bin/env python3
"""
Hermes runtime + cron watchdog (read-only, no_agent-ready).

Default contract for Hermes cron no_agent:
- exit 0 + empty stdout: OK/silent
- exit 0 + non-empty stdout: operational alert
- exit non-zero: watchdog failure

This script never prints env vars, tokens, config secrets, or process environments.
It does not restart Docker, mutate cron jobs, write files, call external APIs, or send messages.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
from typing import Any

EXPECTED_VERSION_FRAGMENT = "v0.15.1"
EXPECTED_CONFIG_CWD = "/opt/data"
EXPECTED_JOB_ID = "f5a23dd6a1bd"
MAX_NEXT_RUN_DELAY_HOURS = 30
MAX_LAST_RUN_AGE_HOURS = 48
# Lucas now runs intentional isolated Telegram profiles. Multiple gateway
# processes are healthy when they map to distinct HERMES_HOME values.
# REQUIRED: must always be running; absence is an alert.
# OPTIONAL_DORMANT: prepared/configured but not necessarily running;
#   absence is informational only, not an alert.
REQUIRED_GATEWAY_HOMES = {
    "/opt/data",
    "/opt/data/profiles/mordomo",
    "/opt/data/profiles/lk-growth",
    "/opt/data/profiles/spiti",
}
OPTIONAL_DORMANT_GATEWAY_HOMES = {
    "/opt/data/profiles/lk-ops",
    "/opt/data/profiles/lk-shopify",
    "/opt/data/profiles/lk-trends",
}
# Combined for backwards compat (unknown-home checks)
EXPECTED_GATEWAY_HOMES = REQUIRED_GATEWAY_HOMES | OPTIONAL_DORMANT_GATEWAY_HOMES
SENSITIVE_RE = re.compile(
    r"(?i)(token|secret|password|passwd|api[_-]?key|authorization|bearer|shpat_|sbp_|xox[baprs]-|ghp_|github_pat_)"
)


def utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def parse_iso(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    try:
        return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except Exception:
        return None


def safe_line(text: str) -> str:
    if SENSITIVE_RE.search(text):
        return "[REDACTED-SENSITIVE-LINE]"
    return text.replace(os.environ.get("TELEGRAM_BOT_TOKEN", "__NO_TOKEN__"), "[REDACTED]")


def run(cmd: list[str], timeout: int = 20) -> tuple[int, str, str]:
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, check=False)
        stdout = "\n".join(safe_line(x) for x in (proc.stdout or "").splitlines())
        stderr = "\n".join(safe_line(x) for x in (proc.stderr or "").splitlines())
        return proc.returncode, stdout.strip(), stderr.strip()
    except FileNotFoundError:
        return 127, "", f"command not found: {cmd[0]}"
    except subprocess.TimeoutExpired:
        return 124, "", f"timeout after {timeout}s: {' '.join(cmd[:2])}"


def find_hermes_binary() -> str | None:
    candidates = [
        "/opt/hermes/.venv/bin/hermes",
        "/opt/hermes/.venv/bin/python",  # used only as fallback with -m hermes_cli.main if needed later
        shutil.which("hermes") or "",
    ]
    for c in candidates:
        if c and pathlib.Path(c).exists() and os.access(c, os.X_OK):
            return c
    return shutil.which("hermes")


def config_path() -> pathlib.Path:
    home = pathlib.Path(os.environ.get("HERMES_HOME") or "/opt/data")
    p = home / "config.yaml"
    if p.exists():
        return p
    return pathlib.Path("/opt/data/config.yaml")


def jobs_path() -> pathlib.Path:
    home = pathlib.Path(os.environ.get("HERMES_HOME") or "/opt/data")
    p = home / "cron" / "jobs.json"
    if p.exists():
        return p
    return pathlib.Path("/opt/data/cron/jobs.json")


def check_version(alerts: list[str], diag: list[str]) -> None:
    hermes = find_hermes_binary()
    if not hermes:
        alerts.append("Hermes binary não encontrado em /opt/hermes/.venv/bin/hermes nem no PATH.")
        return
    if hermes.endswith("python"):
        # Do not use bare python; this is the Docker-safe interpreter path.
        cmd = [hermes, "-m", "hermes_cli.main", "--version"]
    else:
        cmd = [hermes, "--version"]
    rc, out, err = run(cmd)
    diag.append(f"version_cmd={cmd[0]} rc={rc} out={out[:120] or err[:120]}")
    if rc != 0:
        alerts.append(f"Não consegui executar versão do Hermes (rc={rc}): {err or out}")
        return
    text = out or err
    if EXPECTED_VERSION_FRAGMENT not in text:
        alerts.append(f"Versão Hermes inesperada: esperado conter {EXPECTED_VERSION_FRAGMENT}; obtido: {text[:160]}")


def read_text_limited(path: pathlib.Path, limit: int = 200_000) -> str | None:
    try:
        if not path.exists():
            return None
        return path.read_text(encoding="utf-8", errors="replace")[:limit]
    except Exception as exc:
        return f"__READ_ERROR__ {type(exc).__name__}: {exc}"


def check_config(alerts: list[str], diag: list[str]) -> None:
    path = config_path()
    text = read_text_limited(path)
    if text is None:
        alerts.append(f"Config Hermes não encontrada em {path}.")
        return
    if text.startswith("__READ_ERROR__"):
        alerts.append(f"Falha ao ler config Hermes: {text}")
        return
    # Lightweight parse without requiring PyYAML.
    backend_ok = re.search(r"(?m)^\s*backend:\s*local\s*$", text) is not None
    cwd_match = re.search(r"(?m)^\s*cwd:\s*([^\n#]+)", text)
    cwd = cwd_match.group(1).strip().strip('"\'') if cwd_match else None
    diag.append(f"config_path={path} backend_local={backend_ok} cwd={cwd}")
    if not backend_ok:
        alerts.append("Config terminal.backend não parece ser `local`; verificar se o runtime Docker está usando backend correto.")
    if cwd != EXPECTED_CONFIG_CWD:
        alerts.append(f"Config terminal.cwd inesperado: esperado {EXPECTED_CONFIG_CWD}; obtido {cwd!r}.")


def process_env_value(pid: int, key: str) -> str | None:
    try:
        raw = pathlib.Path(f"/proc/{pid}/environ").read_bytes()
    except Exception:
        return None
    prefix = f"{key}=".encode()
    for item in raw.split(b"\0"):
        if item.startswith(prefix):
            return item[len(prefix):].decode("utf-8", errors="replace")
    return None


def process_cmdline_tokens(pid: int) -> list[str]:
    try:
        raw = pathlib.Path(f"/proc/{pid}/cmdline").read_bytes()
    except Exception:
        return []
    return [item.decode("utf-8", errors="replace") for item in raw.split(b"\0") if item]


def is_real_gateway_cmdline(tokens: list[str]) -> bool:
    """Return True only for an actual Hermes gateway process.

    Do not grep the rendered `ps args` string: cron/terminal shell wrappers can
    contain the literal text "hermes gateway run" inside a script argument and
    must not count as gateways. The real gateway command has `gateway` and `run`
    as separate argv tokens and is launched through a hermes executable/script.
    """
    if len(tokens) < 3:
        return False
    for i in range(len(tokens) - 1):
        if tokens[i] == "gateway" and tokens[i + 1] == "run":
            prefix = tokens[:i]
            return any(pathlib.Path(t).name.startswith("hermes") for t in prefix)
    return False


def check_process(alerts: list[str], diag: list[str]) -> None:
    rc, out, err = run(["ps", "-eo", "pid,ppid,comm"], timeout=10)
    if rc != 0:
        alerts.append(f"Falha ao inspecionar processos (rc={rc}): {err or out}")
        return

    rows: list[dict[str, Any]] = []
    for line in out.splitlines()[1:]:
        parts = line.strip().split(None, 2)
        if len(parts) < 3:
            continue
        pid_s, ppid_s, comm = parts
        try:
            pid = int(pid_s)
            ppid = int(ppid_s)
        except ValueError:
            continue
        tokens = process_cmdline_tokens(pid)
        if not is_real_gateway_cmdline(tokens):
            continue
        home = process_env_value(pid, "HERMES_HOME") or "[unknown]"
        rows.append({"pid": pid, "ppid": ppid, "comm": comm, "home": home})

    homes: dict[str, list[int]] = {}
    for row in rows:
        homes.setdefault(str(row["home"]), []).append(int(row["pid"]))

    diag.append(
        "gateway_processes="
        + ",".join(f"{home}:{len(pids)}" for home, pids in sorted(homes.items()))
    )
    if not rows:
        alerts.append("Nenhum processo `hermes gateway run` visível; se o Telegram ainda responde, pode ser limitação do contexto do cron, mas precisa verificação.")
        return

    unknown = sorted(home for home in homes if home not in EXPECTED_GATEWAY_HOMES)
    if unknown:
        alerts.append("Gateways com HERMES_HOME inesperado: " + ", ".join(unknown) + ".")
    missing = sorted(home for home in REQUIRED_GATEWAY_HOMES if home not in homes)
    if missing:
        alerts.append("Gateways esperados ausentes: " + ", ".join(missing) + ".")
    duplicates = {home: pids for home, pids in homes.items() if len(pids) > 1}
    if duplicates:
        alerts.append(
            "Possíveis gateways duplicados por profile: "
            + "; ".join(f"{home} ({len(pids)} processos)" for home, pids in sorted(duplicates.items()))
            + "."
        )


def load_jobs() -> Any:
    path = jobs_path()
    text = read_text_limited(path, limit=1_000_000)
    if text is None:
        raise FileNotFoundError(str(path))
    if text.startswith("__READ_ERROR__"):
        raise RuntimeError(text)
    return json.loads(text)


def iter_jobs(data: Any) -> list[dict[str, Any]]:
    if isinstance(data, list):
        return [j for j in data if isinstance(j, dict)]
    if isinstance(data, dict):
        if isinstance(data.get("jobs"), list):
            return [j for j in data["jobs"] if isinstance(j, dict)]
        # Some Hermes versions store {job_id: job_obj}
        vals = []
        for k, v in data.items():
            if isinstance(v, dict):
                v = dict(v)
                v.setdefault("job_id", k)
                vals.append(v)
        return vals
    return []


def job_value(job: dict[str, Any], *keys: str) -> Any:
    for k in keys:
        if k in job:
            return job[k]
    return None


def check_cron(alerts: list[str], diag: list[str]) -> None:
    path = jobs_path()
    try:
        data = load_jobs()
    except Exception as exc:
        alerts.append(f"Cron jobs JSON inválido/ilegível em {path}: {type(exc).__name__}: {exc}")
        return
    jobs = iter_jobs(data)
    diag.append(f"jobs_path={path} jobs_count={len(jobs)}")
    target = None
    for job in jobs:
        jid = job_value(job, "job_id", "id")
        if jid == EXPECTED_JOB_ID:
            target = job
            break
    if not target:
        alerts.append(f"Job de melhoria contínua {EXPECTED_JOB_ID} não encontrado em {path}.")
        return
    enabled = job_value(target, "enabled")
    state = job_value(target, "state")
    if enabled is False or state in {"paused", "disabled"}:
        alerts.append(f"Job {EXPECTED_JOB_ID} parece desativado: enabled={enabled}, state={state}.")
    now = utc_now()
    next_run = parse_iso(job_value(target, "next_run_at", "next_run"))
    last_run = parse_iso(job_value(target, "last_run_at", "last_run"))
    last_status = job_value(target, "last_status")
    diag.append(f"target_job enabled={enabled} state={state} next={next_run} last={last_run} status={last_status}")
    if next_run and next_run < now - dt.timedelta(hours=1):
        alerts.append(f"Job {EXPECTED_JOB_ID} está com next_run_at atrasado: {next_run.isoformat()}.")
    if next_run and next_run > now + dt.timedelta(hours=MAX_NEXT_RUN_DELAY_HOURS):
        alerts.append(f"Job {EXPECTED_JOB_ID} está com próximo run distante demais: {next_run.isoformat()}.")
    if last_run and last_run < now - dt.timedelta(hours=MAX_LAST_RUN_AGE_HOURS):
        alerts.append(f"Job {EXPECTED_JOB_ID} não roda há mais de {MAX_LAST_RUN_AGE_HOURS}h: {last_run.isoformat()}.")
    if last_status in {"error", "failed", "failure"}:
        alerts.append(f"Último status do job {EXPECTED_JOB_ID} indica falha: {last_status}.")


def format_alert(alerts: list[str]) -> str:
    now = utc_now().isoformat(timespec="seconds")
    lines = [
        "⚠️ Watchdog Hermes/LK: runtime + cron health",
        f"Horário UTC: {now}",
        "Problemas:",
    ]
    lines.extend(f"- {a}" for a in alerts)
    lines.extend([
        "Impacto provável: risco de drift do runtime Docker, gateway invisível ou rotina diária sem execução.",
        "Ação segura recomendada: inspeção read-only; não reiniciar Docker/gateway sem aprovação e rollback.",
        "Aprovação necessária: sim para qualquer alteração em Docker, containers, compose, cron real ou produção.",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Hermes v0.13 runtime/cron watchdog")
    parser.add_argument("--verbose", action="store_true", help="print OK diagnostics to stdout for manual validation")
    args = parser.parse_args()

    alerts: list[str] = []
    diag: list[str] = []
    for fn in (check_version, check_config, check_process, check_cron):
        try:
            fn(alerts, diag)
        except Exception as exc:  # keep watchdog robust; report as alert not traceback with env context
            alerts.append(f"Falha interna em {fn.__name__}: {type(exc).__name__}: {exc}")

    if alerts:
        print(format_alert(alerts))
    elif args.verbose:
        print("OK — watchdog silencioso em modo cron/no_agent.")
        for item in diag:
            print(f"- {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
