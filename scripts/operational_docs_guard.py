#!/usr/bin/env python3
# Auto-remediation contract:
# - handle A0/A1 local/read-only/script-safe failures by correcting or retrying locally,
#   then verify with sanitized evidence before alerting;
# - do not perform production/external writes, credential work, cron schedule/delivery
#   mutations, Docker/VPS/Traefik/gateway changes, or sends from this script without
#   a scoped approval packet with rollback/readback verification;
# - keep values_printed=false and never print secrets.
"""Guard operacional para docs e runtime local do Hermes Brain.

Modo default: falha quando docs operacionais vivos contêm padrões perigosos como
instrução executável sem marcador LEGACY/SUPERSEDED/DO NOT RUN/EXAMPLE/DRY-RUN.

Modo strict-runtime: amplia a superfície para root docs, skills, scripts e
executáveis locais. Use para auditorias de segurança operacional antes de dizer
que o Brain está saneado.

Uso:
  python3 scripts/operational_docs_guard.py
  python3 scripts/operational_docs_guard.py --root /opt/data/hermes_bruno_ingest/hermes-brain
  python3 scripts/operational_docs_guard.py --strict-runtime --json
"""
from __future__ import annotations

import argparse
import json
import os
import re
import stat
from pathlib import Path
from typing import Iterable

DEFAULT_SCAN_DIRS = [
    "areas/operacoes",
    "empresa",
    "memories",
]

STRICT_SCAN_DIRS = [
    ".",
    "areas",
    "empresa",
    "memories",
    "skills",
    "scripts",
]

DANGEROUS_PATTERNS = [
    ("legacy_root_path", re.compile(r"(?<![A-Za-z0-9_-])/root(?:/|\b)")),
    ("sshpass", re.compile(r"\bsshpass\b", re.I)),
    ("cerebro_cimino_legacy", re.compile(r"\bcerebro-cimino\b", re.I)),
    ("mem0_legacy", re.compile(r"\bmem0\b", re.I)),
    ("inline_password_env", re.compile(r"\b(?:SSHPASS|PASSWORD|PASS|TOKEN|SECRET)=['\"][^'\"]{6,}['\"]")),
    ("dangerous_rm", re.compile(r"\brm\s+-rf\s+(?:/|\$|~|/opt|/docker|/root)")),
    ("docker_mutation", re.compile(r"\bdocker\s+(?:compose\s+)?(?:down|up|restart|rm|rmi|system\s+prune|volume\s+rm|network\s+rm)\b", re.I)),
    # Require a shell-command boundary so prose like "shutdown race" or a
    # regex containing "passwd" is not treated as an executable mutation.
    ("host_mutation", re.compile(r"(?:^|[;&|`])\s*(?:sudo\s+)?(?:reboot|shutdown(?:\s+-[a-zA-Z]+)?|systemctl\s+restart|ufw\s+(?:allow|deny|reset)|passwd\b)", re.I)),
]

LINE_ALLOW = re.compile(
    r"LEGACY|SUPERSEDED|DEPRECATED|DO NOT RUN|NÃO EXECUTAR|NAO EXECUTAR|EXAMPLE|EXEMPLO|DRY[- ]?RUN|hist[oó]ric|não\s+|nao\s+|sem\s+tocar|sem\s+alterar|sem\s+imprimir|não é autorização|nao e autorizacao|bloquead|bloquear|proibir|proibid|guardrail|scan|scanner|token-shaped|secret scan|safe allowlist|qualquer mudança|SSH/root/firewall|risco|nenhum\s+|somente\s+|apenas\s+|removid[ao]|referência histórica|referencia historica|not runtime|não runtime|nao runtime|bloqueio|blocked|Nomenclatura|Antes:|corrigid|updated|SECRET_PATTERNS|placeholder|\*\*\*|Docker/VPS/root",
    re.I,
)
FILE_LEGACY = re.compile(r"LEGACY|SUPERSEDED|DEPRECATED|DO NOT RUN|NÃO EXECUTAR|NAO EXECUTAR|hist[oó]ric", re.I)
SKIP_PARTS = {".git", "node_modules", ".venv", "venv", "__pycache__", ".pytest_cache", "dist", "build"}
# Historical evidence artifacts can quote old commands/paths as receipts.
# They are not executable runtime instructions and should not block strict-runtime.
HISTORICAL_ARTIFACT_PARTS = {"receipts", "approval-packets", "handoffs", "reports", "impact-reviews"}
DEFAULT_TEXT_EXTS = {".md", ".txt", ".yaml", ".yml", ".json"}
STRICT_TEXT_EXTS = DEFAULT_TEXT_EXTS | {".py", ".sh", ".toml", ".env"}
ROOT_LEVEL_STRICT_NAMES = {"brain_sync.sh", "sync_hermes.sh", "hermes_remediate.sh", "monitor_daemon.py", "alert_system.py"}


def is_executable(path: Path) -> bool:
    try:
        return bool(path.stat().st_mode & stat.S_IXUSR)
    except OSError:
        return False


def wanted_file(path: Path, strict_runtime: bool) -> bool:
    if any(part in SKIP_PARTS for part in path.parts):
        return False
    if strict_runtime and any(part in HISTORICAL_ARTIFACT_PARTS for part in path.parts):
        return False
    suffix = path.suffix.lower()
    if strict_runtime:
        return suffix in STRICT_TEXT_EXTS or path.name in ROOT_LEVEL_STRICT_NAMES or is_executable(path)
    return suffix in DEFAULT_TEXT_EXTS


def iter_files(root: Path, strict_runtime: bool = False) -> Iterable[Path]:
    if strict_runtime:
        seen: set[Path] = set()
        # Root-level operational docs/scripts.
        for path in root.iterdir():
            if path.is_file() and wanted_file(path, True):
                resolved = path.resolve()
                if resolved not in seen:
                    seen.add(resolved)
                    yield path
        for rel in ["areas", "empresa", "memories", "skills", "scripts", "reports/governance"]:
            base = root / rel
            if not base.exists():
                continue
            for path in base.rglob("*"):
                if path.is_file() and wanted_file(path, True):
                    resolved = path.resolve()
                    if resolved not in seen:
                        seen.add(resolved)
                        yield path
        return

    for rel in DEFAULT_SCAN_DIRS:
        base = root / rel
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if path.is_file() and wanted_file(path, False):
                yield path


def is_fenced(line: str, fence_state: dict) -> bool:
    stripped = line.strip()
    if stripped.startswith("```") or stripped.startswith("~~~"):
        fence_state["in"] = not fence_state.get("in", False)
        return True
    return bool(fence_state.get("in", False))


def scan_file(path: Path, root: Path, strict_runtime: bool = False):
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    head = "\n".join(lines[:12])
    file_legacy = bool(FILE_LEGACY.search(head))
    findings = []
    fence = {"in": False}
    executable_like = path.suffix.lower() in {".py", ".sh"} or is_executable(path)

    for idx, line in enumerate(lines, 1):
        in_code = is_fenced(line, fence)
        context_window = "\n".join(lines[max(0, idx - 5):min(len(lines), idx + 3)])
        for name, pattern in DANGEROUS_PATTERNS:
            if not pattern.search(line):
                continue
            allowed = file_legacy or LINE_ALLOW.search(line) or LINE_ALLOW.search(context_window)
            scanner_definition_context = (
                path.suffix.lower() == ".py"
                and (
                    "re.compile" in line
                    or "SECRET_PATTERNS" in context_window
                    or "DANGEROUS_PATTERNS" in context_window
                    or "redact" in context_window.lower()
                    or "token-shaped" in context_window.lower()
                    or "token|secret|password" in line
                )
            )
            if scanner_definition_context:
                allowed = True
            # Markdown/documentation fenced examples are allowed; executable-like
            # files still need a top-of-file deprecation marker for legacy patterns.
            if in_code and not executable_like:
                allowed = True
            # In strict mode, executable-like files may contain legacy patterns only
            # when the file itself is explicitly deprecated at the top, unless the
            # match is inside a scanner/redaction pattern definition.
            if strict_runtime and executable_like and not file_legacy and not scanner_definition_context:
                allowed = False
            if allowed:
                continue
            findings.append({
                "file": str(path.relative_to(root)),
                "line": idx,
                "rule": name,
                "strict_runtime": strict_runtime,
                "text": line.strip()[:240],
            })
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--strict-runtime", action="store_true", help="scan scripts, skills, root docs and executable files in addition to default docs")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    findings = []
    scanned = 0
    for path in iter_files(root, strict_runtime=args.strict_runtime):
        scanned += 1
        findings.extend(scan_file(path, root, strict_runtime=args.strict_runtime))

    result = {
        "root": str(root),
        "mode": "strict-runtime" if args.strict_runtime else "default-docs",
        "scanned_files": scanned,
        "fail_count": len(findings),
        "findings": findings,
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"operational_docs_guard mode={result['mode']} scanned_files={scanned} fail_count={len(findings)}")
        for f in findings[:100]:
            print(f"FAIL {f['file']}:{f['line']} [{f['rule']}] {f['text']}")
        if len(findings) > 100:
            print(f"... {len(findings) - 100} additional findings omitted")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
