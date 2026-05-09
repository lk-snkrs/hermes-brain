#!/usr/bin/env python3
"""Hermes Brain health check.

Checks repository hygiene for:
- token-shaped secrets
- broken relative markdown links and anchors
- required root/governance files
- required files in agent folders
- area/sub-area navigation MAPA files
- routine files missing from empresa/rotinas/_index.md
- canonical skills missing from empresa/skills/_index.md
- area skill references to missing canonical skills

Run from repo root:
    python3 scripts/brain_health_check.py
    python3 scripts/brain_health_check.py --json reports/brain-health-check.json
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import unicodedata
from dataclasses import asdict, dataclass
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

SECRET_PATTERNS = {
    "doppler": re.compile(r"dp\.[a-z]{2}\.[A-Za-z0-9_-]+"),
    "shopify": re.compile(r"shpat_[A-Za-z0-9_]+"),
    "supabase_pat": re.compile(r"sbp_[A-Za-z0-9_]+"),
    "github_classic": re.compile(r"ghp_[A-Za-z0-9_]+"),
    "github_fine_grained": re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    "openai": re.compile(r"sk-[A-Za-z0-9_-]{12,}"),
    "mem0": re.compile(r"m0-[A-Za-z0-9_-]{12,}"),
    "telegram_bot": re.compile(r"\b\d{8,10}:[A-Za-z0-9_-]{25,}\b"),
    "fal_key_pair": re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}:[A-Za-z0-9_-]{20,}\b", re.I),
    "wandb": re.compile(r"wandb_[A-Za-z0-9_]{20,}"),
    "tinker": re.compile(r"tml-[A-Za-z0-9_]{20,}"),
    "google_oauth_secret": re.compile(r"GOCSPX-[A-Za-z0-9_-]{20,}"),
    "google_refresh_token": re.compile(r"1//[A-Za-z0-9_-]{20,}"),
}

REQUIRED_ROOT_FILES = [
    "README.md",
    "START-HERE.md",
    "STARTUP.md",
    "PROTOCOLS.md",
    "TOOLS.md",
    "ARCHITECTURE.md",
    "CHANGELOG.md",
    "ROADMAP-30-DIAS-HERMES.md",
    "areas/MAPA.md",
    "empresa/MAPA.md",
    "empresa/rotinas/_index.md",
    "empresa/skills/_index.md",
    "empresa/gestao/pendencias.md",
    "empresa/gestao/memory-system.md",
    "memories/pending.md",
    "memories/decisions.md",
    "memories/lessons.md",
    "seguranca/permissoes.md",
    "seguranca/acoes-sensiveis.md",
]
REQUIRED_AGENT_FILES = ["SOUL.md", "AGENTS.md", "TOOLS.md", "USER.md", "MEMORY.md", "HEARTBEAT.md"]
IGNORE_DIRS = {".git", "__pycache__", ".pytest_cache", "node_modules", "venv", ".venv", "dist", "build"}
TEXT_SUFFIXES = {".md", ".py", ".yml", ".yaml", ".json", ".txt", ".sh", ".env", ".toml"}
MD_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$")

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


def github_anchor_slug(title: str) -> str:
    # Close enough to GitHub's markdown anchor algorithm for this repo's headings.
    title = re.sub(r"<[^>]+>", "", title)
    title = title.strip().lower()
    title = unicodedata.normalize("NFKD", title)
    title = "".join(ch for ch in title if not unicodedata.combining(ch))
    title = re.sub(r"[`*_~]", "", title)
    title = re.sub(r"[^a-z0-9\s-]", "", title)
    title = re.sub(r"[\s-]+", "-", title).strip("-")
    return title


def anchors_for_file(p: Path) -> set[str]:
    anchors = {""}
    seen: dict[str, int] = {}
    for line in read_text(p).splitlines():
        m = HEADING.match(line)
        if not m:
            continue
        base = github_anchor_slug(m.group(2))
        if not base:
            continue
        count = seen.get(base, 0)
        seen[base] = count + 1
        anchors.add(base if count == 0 else f"{base}-{count}")
    return anchors


def check_secrets() -> list[Issue]:
    issues = []
    for p in iter_files(ROOT):
        if p.suffix.lower() not in TEXT_SUFFIXES:
            continue
        txt = read_text(p)
        for name, pat in SECRET_PATTERNS.items():
            if pat.search(txt):
                issues.append(Issue("FAIL", "secret", rel(p), name))
    return issues


def normalize_link(raw: str) -> tuple[str, str] | None:
    raw = raw.strip()
    if not raw or raw.startswith(("http://", "https://", "mailto:", "tel:")):
        return None
    if raw.startswith("<") and raw.endswith(">"):
        raw = raw[1:-1]
    if raw.startswith("#"):
        return "", unquote(raw[1:])
    path, _, anchor = raw.partition("#")
    return unquote(path.replace("%20", " ")), unquote(anchor)


def check_links() -> list[Issue]:
    issues = []
    anchor_cache: dict[Path, set[str]] = {}
    for p in iter_files(ROOT):
        if p.suffix.lower() != ".md":
            continue
        txt = read_text(p)
        for match in MD_LINK.finditer(txt):
            normalized = normalize_link(match.group(1))
            if not normalized:
                continue
            target, anchor = normalized
            dest = p if target == "" else (p.parent / target).resolve()
            try:
                dest.relative_to(ROOT)
            except ValueError:
                # Links outside repo are often intentional historical paths; warn only.
                issues.append(Issue("WARN", "external_relative_link", rel(p), target))
                continue
            if not dest.exists():
                issues.append(Issue("WARN", "broken_markdown_link", rel(p), target))
                continue
            if anchor and dest.suffix.lower() == ".md":
                slug = github_anchor_slug(anchor)
                anchor_cache.setdefault(dest, anchors_for_file(dest))
                if slug not in anchor_cache[dest]:
                    detail = f"{target or rel(dest)}#{anchor}"
                    issues.append(Issue("WARN", "broken_markdown_anchor", rel(p), detail))
    return issues


def check_required_files() -> list[Issue]:
    issues = []
    for path in REQUIRED_ROOT_FILES:
        if not (ROOT / path).exists():
            issues.append(Issue("FAIL", "missing_required_file", path, "required root/governance file missing"))
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


def check_area_maps() -> list[Issue]:
    issues = []
    areas = ROOT / "areas"
    if not areas.exists():
        return [Issue("FAIL", "missing_dir", "areas", "directory missing")]
    for d in sorted(x for x in areas.iterdir() if x.is_dir()):
        if not (d / "MAPA.md").exists():
            issues.append(Issue("WARN", "area_missing_mapa", rel(d), "MAPA.md"))
    for d in sorted(areas.glob("*/sub-areas/*")):
        if d.is_dir() and not (d / "MAPA.md").exists():
            issues.append(Issue("WARN", "subarea_missing_mapa", rel(d), "MAPA.md"))
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


def run_checks() -> tuple[list[dict[str, int | str]], list[Issue]]:
    checks = [
        ("secrets", check_secrets),
        ("links", check_links),
        ("required_files", check_required_files),
        ("agent_files", check_agent_files),
        ("area_maps", check_area_maps),
        ("routines_index", check_routines_index),
        ("skill_references", check_skill_references),
    ]
    summary = []
    all_issues: list[Issue] = []
    for name, fn in checks:
        issues = fn()
        all_issues.extend(issues)
        summary.append({
            "check": name,
            "FAIL": sum(i.level == "FAIL" for i in issues),
            "WARN": sum(i.level == "WARN" for i in issues),
        })
    return summary, all_issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Hermes Brain repository health check")
    parser.add_argument("--json", dest="json_path", help="Optional path to write a JSON report")
    args = parser.parse_args()

    summary, all_issues = run_checks()
    for item in summary:
        print(f"{item['check']}: FAIL={item['FAIL']} WARN={item['WARN']}")

    if all_issues:
        print("\nIssues:")
        for i in all_issues:
            print(f"{i.level}\t{i.kind}\t{i.path}\t{i.detail}")
    else:
        print("\nAll checks passed.")

    if args.json_path:
        out = ROOT / args.json_path
        out.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "summary": summary,
            "issues": [asdict(i) for i in all_issues],
            "fail_count": sum(i.level == "FAIL" for i in all_issues),
            "warn_count": sum(i.level == "WARN" for i in all_issues),
        }
        out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"\nJSON report: {args.json_path}")

    return 1 if any(i.level == "FAIL" for i in all_issues) else 0

if __name__ == "__main__":
    sys.exit(main())
