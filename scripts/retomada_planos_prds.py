#!/usr/bin/env python3
"""Gera relatório local/read-only de retomada de planos, PRDs e pendências.

Este script lê apenas arquivos versionados do Hermes Brain e metadados git locais.
Não consulta APIs, VPS, Docker, bancos, crons reais ou serviços externos.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

SOURCES = {
    "pendencias": ROOT / "empresa" / "gestao" / "pendencias.md",
    "pending": ROOT / "memories" / "pending.md",
    "roadmap": ROOT / "ROADMAP-30-DIAS-HERMES.md",
    "changelog": ROOT / "CHANGELOG.md",
}

APPROVAL_KEYWORDS = [
    "aprovação",
    "aprovar",
    "bloqueio",
    "bloqueado",
    "produção",
    "VPS",
    "Docker",
    "cron",
    "UI",
    "Telegram",
    "campanha",
    "WhatsApp",
    "email",
    "cliente",
    "externo",
    "secret",
    "senha",
    "SSH",
]

SAFE_DEFAULT = "Ação documental/local read-only; não mexe em produção."


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def run_git(args: list[str]) -> str:
    try:
        result = subprocess.run(
            ["git", "-C", str(ROOT), *args],
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        )
    except FileNotFoundError:
        return ""
    return result.stdout.strip()


def extract_section(text: str, heading: str) -> str:
    pattern = re.compile(rf"^##\s+{re.escape(heading)}\s*$", re.M)
    match = pattern.search(text)
    if not match:
        return ""
    start = match.end()
    next_heading = re.search(r"^##\s+", text[start:], re.M)
    end = start + next_heading.start() if next_heading else len(text)
    return text[start:end].strip()


def extract_checkboxes(section: str) -> list[str]:
    items: list[str] = []
    current: list[str] = []
    for line in section.splitlines():
        if re.match(r"^- \[[ xX]\]", line):
            if current:
                items.append(" ".join(current).strip())
            current = [line.strip()]
        elif current and line.startswith("  "):
            current.append(line.strip())
    if current:
        items.append(" ".join(current).strip())
    return items


def clean_item(item: str) -> str:
    item = re.sub(r"^- \[[ xX]\]\s*", "", item).strip()
    item = re.sub(r"\s+", " ", item)
    return item


def title_from_item(item: str) -> str:
    bold = re.match(r"\*\*(.+?)\*\*", item)
    if bold:
        return bold.group(1).strip()
    return item.split("—", 1)[0].strip().rstrip(".")


def requires_approval(text: str) -> bool:
    lowered = text.lower()
    if "somente quando houver necessidade operacional concreta" in lowered:
        return False
    return any(re.search(rf"(?<![\w.]){re.escape(k.lower())}(?![\w.])", lowered) for k in APPROVAL_KEYWORDS)


def classify_items(pendencias: str) -> list[dict[str, str]]:
    sections = {
        "Ativo": extract_section(pendencias, "Ativos"),
        "Bloqueado": extract_section(pendencias, "Bloqueados — exigem decisão/aprovação Lucas"),
        "Aguardando data/evento": extract_section(pendencias, "Aguardando data/evento"),
    }
    rows: list[dict[str, str]] = []
    for state, section in sections.items():
        for raw in extract_checkboxes(section):
            item = clean_item(raw)
            title = title_from_item(item)
            approval = "sim" if state == "Bloqueado" or requires_approval(item) else "não"
            next_action = ""
            next_match = re.search(r"próxima ação:\s*(.+?)(?:\s+Evidência|$)", item, re.I)
            if next_match:
                next_action = next_match.group(1).strip().rstrip(".;")
            elif state == "Bloqueado":
                next_action = "Preparar escopo, risco e rollback; executar só após aprovação explícita."
            elif state == "Aguardando data/evento":
                next_action = "Aguardar evento/data e revisar evidência antes de agir."
            else:
                next_action = "Executar quando virar fluxo recorrente real ou houver pedido operacional concreto."
            block = ""
            block_match = re.search(r"bloqueio:\s*([^.;]+)", item, re.I)
            if block_match:
                block = block_match.group(1).strip()
            elif state == "Bloqueado":
                block = "Exige decisão/aprovação Lucas."
            elif state == "Aguardando data/evento":
                block = "Sem ação imediata; depende de data/evento."
            else:
                block = "Sem bloqueio técnico; evitar burocracia antes de fluxo real."
            evidence = ""
            ev_match = re.search(r"Evidência(?:/base)?:\s*(.+)$", item, re.I)
            if ev_match:
                evidence = ev_match.group(1).strip()
            rows.append(
                {
                    "item": title,
                    "estado": state,
                    "ultimo_artefato": evidence or "Hermes Brain / pendências executivas.",
                    "bloqueio": block,
                    "proxima_acao_segura": next_action,
                    "precisa_aprovacao_lucas": approval,
                }
            )
    return rows


def latest_commits(limit: int = 5) -> list[str]:
    out = run_git(["log", "--oneline", f"-{limit}"])
    return [line for line in out.splitlines() if line.strip()]


def markdown_report(date: str, rows: list[dict[str, str]], git_status: str, commits: list[str]) -> str:
    active = [r for r in rows if r["estado"] == "Ativo"]
    blocked = [r for r in rows if r["estado"] == "Bloqueado"]
    waiting = [r for r in rows if r["estado"] == "Aguardando data/evento"]

    lines = [
        f"# Retomada de planos e PRDs — {date}",
        "",
        "## Leitura executiva",
        "",
        "Relatório gerado por script local/read-only. Ele resume a fila documentada do Hermes Brain e o estado git local; não consulta produção, VPS, Docker, bancos, APIs, Telegram ou crons reais.",
        "",
        f"- Ativos: {len(active)}",
        f"- Bloqueados por aprovação/decisão: {len(blocked)}",
        f"- Aguardando data/evento: {len(waiting)}",
        f"- Git status local: {'limpo' if not git_status else 'com alterações no worktree'}",
        "",
        "## Próxima ação recomendada",
        "",
    ]
    if active:
        lines.append("A próxima ação segura é manter documentação/índices e só completar subdocs de integrações quando virarem fluxo real. Não há justificativa para cron semanal recorrente de retomada agora: a fila ativa está pequena e os itens sensíveis estão corretamente bloqueados.")
    else:
        lines.append("Não há item ativo acionável. Manter apenas revisão sob demanda ou por evento.")
    lines += [
        "",
        "## Itens retomados",
        "",
    ]
    for row in rows:
        lines += [
            f"### {row['item']}",
            "",
            f"- Estado: {row['estado']}",
            f"- Último artefato/evidência: {row['ultimo_artefato']}",
            f"- Bloqueio real: {row['bloqueio']}",
            f"- Próxima ação segura: {row['proxima_acao_segura']}",
            f"- Precisa aprovação Lucas: {row['precisa_aprovacao_lucas']}",
            "",
        ]
    lines += [
        "## Git local",
        "",
        "Status:",
        "",
        "```text",
        git_status or "clean",
        "```",
        "",
        "Últimos commits:",
        "",
    ]
    for commit in commits:
        lines.append(f"- `{commit}`")
    lines += [
        "",
        "## Não alterado",
        "",
        "- Nenhum cron foi criado, pausado ou alterado.",
        "- Nenhuma UI/Mission Control visual foi criada.",
        "- Nenhum serviço de produção, VPS, Docker, Traefik, volume ou rede foi tocado.",
        "- Nenhum banco, API, secret, campanha, WhatsApp, email, post ou contato externo foi tocado.",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Gera relatório de retomada de planos e PRDs.")
    parser.add_argument("--date", default=dt.date.today().isoformat())
    parser.add_argument("--output", default="")
    parser.add_argument("--json-output", default="")
    args = parser.parse_args()

    pendencias = read_text(SOURCES["pendencias"])
    rows = classify_items(pendencias)
    git_status = run_git(["status", "--short"])
    commits = latest_commits()

    report = markdown_report(args.date, rows, git_status, commits)
    data: dict[str, Any] = {
        "date": args.date,
        "source_files": {k: str(v.relative_to(ROOT)) for k, v in SOURCES.items()},
        "counts": {
            "active": sum(1 for r in rows if r["estado"] == "Ativo"),
            "blocked": sum(1 for r in rows if r["estado"] == "Bloqueado"),
            "waiting": sum(1 for r in rows if r["estado"] == "Aguardando data/evento"),
        },
        "items": rows,
        "git_status": git_status,
        "latest_commits": commits,
        "limits": [
            "read-only local repo files only",
            "does not check production/runtime/VPS/APIs/databases/crons",
            "does not create recurring jobs or send Telegram messages",
        ],
    }

    if args.output:
        out = ROOT / args.output
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(report, encoding="utf-8")
    else:
        print(report)

    if args.json_output:
        jout = ROOT / args.json_output
        jout.parent.mkdir(parents=True, exist_ok=True)
        jout.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
