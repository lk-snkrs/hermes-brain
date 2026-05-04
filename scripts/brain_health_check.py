#!/usr/bin/env python3
"""Hermes Brain health check.

Checks repository hygiene for:
- token-shaped secrets
- broken relative markdown links
- required files in agent folders
- routine files missing from empresa/rotinas/_index.md
- area navigation skills that reference missing canonical skills

Run from repo root:
    python3 scripts/brain_health_check.py
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from dataclasses import dataclass

ROOT = Path(__file__).resolve().parents[1]

SECRET_PATTERNS = {
    "doppler": re.compile(r"dp\.[a-z]{2}\.[A-Za-z0-9_-]+"),
    "shopify": re.compile(r"shpat_[A-Za-z0-9_]+"),
    "supabase_pat": re.compile(r"sbp_[A-Za-z0-9_]+"),
    "github": re.compile(r"ghp_[A-Za-z0-9_]+"),
    "openai": re.compile(r"sk-[A-Za-z0-9_-]{12,}"),
    "mem0": re.compile(r"m0-[A-Za-z0-9_-]{12,}"),
    "telegram_bot": re.compile(r"\b\d{8,10}:[A-Za-z0-9_-]{25,}\b"),
    "fal_key_pair": re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}:[A-Za-z0-9_-]{20,}\b", re.I),
    "wandb": re.compile(r"wandb_[A-Za-z0-9_]{20,}"),
    "tinker": re.compile(r"tml-[A-Za-z0-9_]{20,}"),
}

REQUIRED_AGENT_FILES = ["SOUL.md", "AGENTS.md", "TOOLS.md", "USER.md", "MEMORY.md", "HEARTBEAT.md"]
IGNORE_DIRS = {".git", "__pycache__", ".pytest_cache", "node_modules", "venv", ".venv"}
MD_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")

@dataclass
class Issue:
    level: str
    kind: str
    path: str
    detail: str


def iter_files(root: Path):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        for name in filenames:
            p = Path(dirpath) / name
            if p.is_file():
                yield p


def rel(p: Path) -> str:
    return str(p.relative_to(ROOT))


def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="ignore")


def check_secrets() -> list[Issue]:
    issues = []
    for p in iter_files(ROOT):
        if p.suffix.lower() not in {".md", ".py", ".yml", ".yaml", ".json", ".txt", ".sh"}:
            continue
        txt = read_text(p)
        for name, pat in SECRET_PATTERNS.items():
            if pat.search(txt):
                issues.append(Issue("FAIL", "secret", rel(p), name))
    return issues


def normalize_link(raw: str) -> str | None:
    target = raw.strip().split("#", 1)[0]
    if not target:
        return None
    if target.startswith(("http://", "https://", "mailto:", "tel:", "#")):
        return None
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    return target.replace("%20", " ")


def check_links() -> list[Issue]:
    issues = []
    for p in iter_files(ROOT):
        if p.suffix.lower() != ".md":
            continue
        txt = read_text(p)
        for match in MD_LINK.finditer(txt):
            target = normalize_link(match.group(1))
            if not target:
                continue
            dest = (p.parent / target).resolve()
            try:
                dest.relative_to(ROOT)
            except ValueError:
                # Links outside repo are often intentional historical paths; warn only.
                issues.append(Issue("WARN", "external_relative_link", rel(p), target))
                continue
            if not dest.exists():
                issues.append(Issue("WARN", "broken_markdown_link", rel(p), target))
    return issues


def check_agent_files() -> list[Issue]:
    issues = []
    agents = ROOT / "agentes"
    if not agents.exists():
        return [Issue("FAIL", "missing_dir", "agentes", "directory missing")]
    for d in sorted(x for x in agents.iterdir() if x.is_dir()):
        for req in REQUIRED_AGENT_FILES:
            if not (d / req).exists():
                issues.append(Issue("WARN", "agent_missing_file", rel(d), req))
    return issues


def check_routines_index() -> list[Issue]:
    issues = []
    idx = ROOT / "empresa" / "rotinas" / "_index.md"
    idx_txt = read_text(idx) if idx.exists() else ""
    for p in sorted((ROOT / "areas").glob("**/rotinas/*.md")):
        if "_templates" in p.parts:
            continue
        r = rel(p)
        if r not in idx_txt:
            issues.append(Issue("WARN", "routine_not_indexed", r, "missing from empresa/rotinas/_index.md"))
    return issues


def check_skill_references() -> list[Issue]:
    issues = []
    idx = ROOT / "empresa" / "skills" / "_index.md"
    idx_txt = read_text(idx) if idx.exists() else ""
    for p in sorted((ROOT / "skills").glob("*/SKILL.md")):
        r = rel(p)
        if r not in idx_txt:
            issues.append(Issue("WARN", "canonical_skill_not_indexed", r, "missing from empresa/skills/_index.md"))
    for p in sorted((ROOT / "areas").glob("**/skills/**/SKILL.md")):
        txt = read_text(p)
        for m in re.finditer(r"`(skills/[^`]+/SKILL\.md)`", txt):
            target = ROOT / m.group(1)
            if not target.exists():
                issues.append(Issue("FAIL", "missing_canonical_skill", rel(p), m.group(1)))
    return issues


def main() -> int:
    checks = [
        ("secrets", check_secrets),
        ("links", check_links),
        ("agent_files", check_agent_files),
        ("routines_index", check_routines_index),
        ("skill_references", check_skill_references),
    ]
    all_issues: list[Issue] = []
    for name, fn in checks:
        issues = fn()
        all_issues.extend(issues)
        fail_count = sum(i.level == "FAIL" for i in issues)
        warn_count = sum(i.level == "WARN" for i in issues)
        print(f"{name}: FAIL={fail_count} WARN={warn_count}")

    if all_issues:
        print("\nIssues:")
        for i in all_issues:
            print(f"{i.level}\t{i.kind}\t{i.path}\t{i.detail}")
    else:
        print("\nAll checks passed.")

    return 1 if any(i.level == "FAIL" for i in all_issues) else 0

if __name__ == "__main__":
    sys.exit(main())
