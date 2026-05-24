#!/usr/bin/env python3
"""Generate a read-only executive Brain Improvement Score report.

This script intentionally reads only the repository working tree plus an optional
brain_health_check JSON report. It does not call networks, databases, Docker,
VPS, crons, messaging APIs, or external integrations.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, asdict
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

AGENT_REQUIRED_FILES = ["SOUL.md", "AGENTS.md", "TOOLS.md", "USER.md", "MEMORY.md", "HEARTBEAT.md"]
ROOT_NAV_FILES = ["START-HERE.md", "README.md", "areas/MAPA.md", "empresa/MAPA.md"]
SECURITY_FILES = ["seguranca/permissoes.md", "seguranca/acoes-sensiveis.md"]
TRACKING_FILES = ["ROADMAP-30-DIAS-HERMES.md", "CHANGELOG.md", "empresa/gestao/pendencias.md", "memories/pending.md"]
EXPECTED_INTEGRATIONS = [
    "shopify.md",
    "supabase.md",
    "evolution.md",
    "n8n.md",
    "github.md",
    "hostinger.md",
    "telegram.md",
    "analytics.md",
    "klaviyo.md",
    "meta-ads.md",
]


@dataclass
class Dimension:
    key: str
    label: str
    score: int
    reason: str
    evidence: list[str]
    recommendations: list[str]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def md_files(path: Path) -> list[Path]:
    if not path.exists():
        return []
    return sorted(p for p in path.rglob("*.md") if ".git" not in p.parts)


def load_health(path: Path | None) -> dict[str, Any]:
    if not path:
        default = ROOT / "reports" / f"brain-health-check-{date.today().isoformat()}.json"
        path = default if default.exists() else ROOT / "reports" / "brain-health-check-2026-05-09.json"
    if not path.exists():
        return {"path": rel(path), "available": False, "fail_count": None, "warn_count": None, "summary": [], "issues": []}
    data = json.loads(path.read_text(encoding="utf-8"))
    data["path"] = rel(path)
    data["available"] = True
    return data


def health_check_value(health: dict[str, Any], check: str, field: str) -> int:
    for item in health.get("summary", []):
        if item.get("check") == check:
            return int(item.get(field, 0))
    return 0


def bounded(value: float) -> int:
    return max(0, min(100, round(value)))


def count_checkboxes(text: str) -> tuple[int, int]:
    open_items = len(re.findall(r"^- \[ \]", text, flags=re.M))
    done_items = len(re.findall(r"^- \[x\]", text, flags=re.M | re.I))
    return open_items, done_items


def dimension_agents(health: dict[str, Any]) -> Dimension:
    agent_dirs = sorted([p for p in (ROOT / "agentes").iterdir() if p.is_dir()]) if (ROOT / "agentes").exists() else []
    missing: list[str] = []
    for agent in agent_dirs:
        for filename in AGENT_REQUIRED_FILES:
            if not (agent / filename).exists():
                missing.append(f"{rel(agent)}/{filename}")
    base = 100 - len(missing) * 4 - health_check_value(health, "agent_files", "FAIL") * 10 - health_check_value(health, "agent_files", "WARN") * 3
    return Dimension(
        key="agents",
        label="Identidade e agentes",
        score=bounded(base),
        reason="Agentes principais têm estrutura operacional; penalização aplicada apenas para arquivos obrigatórios ausentes.",
        evidence=[f"Agentes avaliados: {len(agent_dirs)}", f"Arquivos obrigatórios faltantes: {len(missing)}"],
        recommendations=([] if not missing else ["Completar arquivos obrigatórios de agentes antes de novas especializações."]),
    )


def dimension_maps(health: dict[str, Any]) -> Dimension:
    missing_root = [p for p in ROOT_NAV_FILES if not (ROOT / p).exists()]
    subdirs = [p for base in [ROOT / "areas", ROOT / "empresa"] if base.exists() for p in base.rglob("*") if p.is_dir()]
    map_dirs = [p for p in subdirs if (p / "MAPA.md").exists()]
    base = 100 - len(missing_root) * 12 - health_check_value(health, "area_maps", "FAIL") * 10 - health_check_value(health, "area_maps", "WARN") * 3
    return Dimension(
        key="maps",
        label="MAPAs e navegação",
        score=bounded(base),
        reason="Navegação executiva depende dos arquivos de entrada e MAPAs por área/subárea.",
        evidence=[f"Arquivos de entrada ausentes: {len(missing_root)}", f"Diretórios com MAPA.md: {len(map_dirs)}"],
        recommendations=([] if not missing_root else ["Recriar arquivos de navegação ausentes antes de ampliar o Brain."]),
    )


def dimension_routines(health: dict[str, Any]) -> Dimension:
    routine_files = md_files(ROOT / "areas")
    routine_files = [p for p in routine_files if "/rotinas/" in rel(p)]
    index = read_text(ROOT / "empresa/rotinas/_index.md")
    indexed = sum(1 for p in routine_files if p.name in index)
    coverage = indexed / max(1, len(routine_files))
    base = 70 + coverage * 30 - health_check_value(health, "routines_index", "FAIL") * 8 - health_check_value(health, "routines_index", "WARN") * 2
    return Dimension(
        key="routines",
        label="Rotinas e crons",
        score=bounded(base),
        reason="Rotinas documentadas estão indexadas; o score não afirma execução real de cron.",
        evidence=[f"Rotinas documentadas: {len(routine_files)}", f"Cobertura aproximada no índice por nome de arquivo: {indexed}/{len(routine_files)}"],
        recommendations=["Manter a separação: rotina documentada não prova cron ativo; verificar runtime/VPS quando a pergunta for operacional."],
    )


def dimension_skills(health: dict[str, Any]) -> Dimension:
    skill_files = md_files(ROOT / "skills")
    index = read_text(ROOT / "empresa/skills/_index.md")
    indexed = sum(1 for p in skill_files if p.parent.name in index or p.name in index)
    coverage = indexed / max(1, len(skill_files))
    base = 72 + coverage * 28 - health_check_value(health, "skill_references", "FAIL") * 10 - health_check_value(health, "skill_references", "WARN") * 3
    return Dimension(
        key="skills",
        label="Skills e procedimentos",
        score=bounded(base),
        reason="Skills canônicas e referências de área são avaliadas por índice e health check.",
        evidence=[f"Markdowns em skills/: {len(skill_files)}", f"Cobertura aproximada no índice: {indexed}/{len(skill_files)}"],
        recommendations=["Transformar fluxos repetidos em skills apenas depois de repetição real, evitando burocracia."],
    )


def dimension_security(health: dict[str, Any]) -> Dimension:
    missing = [p for p in SECURITY_FILES if not (ROOT / p).exists()]
    secret_fail = health_check_value(health, "secrets", "FAIL")
    secret_warn = health_check_value(health, "secrets", "WARN")
    base = 100 - len(missing) * 20 - secret_fail * 20 - secret_warn * 5
    return Dimension(
        key="security",
        label="Segurança, secrets e aprovações",
        score=bounded(base),
        reason="Avalia docs de permissão e resultado do check de secrets; não consulta valores de credenciais.",
        evidence=[f"Arquivos de segurança ausentes: {len(missing)}", f"Health check secrets: FAIL={secret_fail} WARN={secret_warn}"],
        recommendations=([] if secret_fail == 0 and not missing else ["Corrigir secrets/guardrails antes de qualquer PR ou automação."]),
    )


def dimension_integrations() -> Dimension:
    base_dir = ROOT / "empresa/integracoes"
    existing = [name for name in EXPECTED_INTEGRATIONS if (base_dir / name).exists()]
    coverage = len(existing) / len(EXPECTED_INTEGRATIONS)
    base = 60 + coverage * 40
    missing = sorted(set(EXPECTED_INTEGRATIONS) - set(existing))
    return Dimension(
        key="integrations",
        label="Integrações",
        score=bounded(base),
        reason="Mede cobertura dos docs canônicos por ferramenta, não saúde das APIs ou permissões reais.",
        evidence=[f"Docs canônicos encontrados: {len(existing)}/{len(EXPECTED_INTEGRATIONS)}"],
        recommendations=([] if not missing else ["Completar docs de integrações canônicas ausentes: " + ", ".join(missing)]),
    )


def dimension_tracking() -> Dimension:
    missing = [p for p in TRACKING_FILES if not (ROOT / p).exists()]
    pending = read_text(ROOT / "memories/pending.md") + "\n" + read_text(ROOT / "empresa/gestao/pendencias.md")
    open_items, done_items = count_checkboxes(pending)
    # A few open items are normal; many open items means boot context starts to degrade.
    pending_penalty = max(0, open_items - 12) * 2
    base = 100 - len(missing) * 15 - pending_penalty
    return Dimension(
        key="tracking",
        label="Roadmap, changelog e pendências",
        score=bounded(base),
        reason="Avalia rastreabilidade executiva e fila compacta de pendências.",
        evidence=[f"Arquivos de tracking ausentes: {len(missing)}", f"Checkboxes abertos nas pendências: {open_items}", f"Checkboxes concluídos nas pendências: {done_items}"],
        recommendations=["Manter pendências como fila acionável, não log de sessão."],
    )


def dimension_consistency(health: dict[str, Any]) -> Dimension:
    fail = int(health.get("fail_count") or 0) if health.get("available") else 0
    warn = int(health.get("warn_count") or 0) if health.get("available") else 0
    base = 100 - fail * 15 - warn * 3 - (0 if health.get("available") else 15)
    return Dimension(
        key="consistency",
        label="Links, arquivos e consistência",
        score=bounded(base),
        reason="Traduz o health check técnico em leitura executiva.",
        evidence=[f"Health check usado: {health.get('path')}", f"FAIL={fail} WARN={warn}", f"Disponível: {bool(health.get('available'))}"],
        recommendations=([] if fail == 0 else ["Resolver FAILs do health check antes de mergear documentação."]),
    )


def build_report(dimensions: list[Dimension], health: dict[str, Any], report_date: str) -> dict[str, Any]:
    weights = {
        "agents": 1.0,
        "maps": 1.0,
        "routines": 1.0,
        "skills": 1.0,
        "security": 1.25,
        "integrations": 0.9,
        "tracking": 1.0,
        "consistency": 1.1,
    }
    total_weight = sum(weights[d.key] for d in dimensions)
    overall = round(sum(d.score * weights[d.key] for d in dimensions) / total_weight)
    safe_recommendations: list[str] = []
    approvals: list[str] = [
        "Cron recorrente ou entrega automática por Telegram para este score.",
        "UI/Mission Control visual ou painel operacional permanente.",
        "Qualquer alteração em produção, VPS/Docker/Traefik/volumes/redes, banco, secrets, campanhas ou mensagens externas.",
    ]
    for d in dimensions:
        safe_recommendations.extend(d.recommendations)
    # Preserve order but dedupe.
    seen = set()
    safe_recommendations = [x for x in safe_recommendations if not (x in seen or seen.add(x))]
    risk_plan = {
        "seguranca_secrets_aprovacao": [],
        "backup_rollback": [],
        "integridade_estrutural": [],
        "evidencia": [],
        "proxima_acao_segura": [],
        "nao_tocar": [
            "produção/runtime, VPS/Docker/Traefik/volumes/redes",
            "bancos, APIs, secrets e credenciais reais",
            "campanhas, WhatsApp, email, posts e contato externo",
        ],
    }
    if health.get("fail_count"):
        risk_plan["seguranca_secrets_aprovacao"].append("Resolver FAILs do health check antes de PR/merge ou qualquer automação.")
    if health_check_value(health, "secrets", "FAIL") or health_check_value(health, "secrets", "WARN"):
        risk_plan["seguranca_secrets_aprovacao"].append("Tratar achados de secrets primeiro; documentar apenas tipo/local, nunca valores.")
    low_dimensions = [d for d in dimensions if d.score < 90]
    if low_dimensions:
        risk_plan["integridade_estrutural"].extend([f"Revisar {d.label} ({d.score}/100): {d.reason}" for d in low_dimensions])
    else:
        risk_plan["integridade_estrutural"].append("Sem dimensão abaixo de 90; manter rotina de preflight antes de mexer em skills/agentes/rotinas.")
    risk_plan["backup_rollback"].append("Para mudanças documentais: branch/worktree e diff revisável bastam como rollback. Para produção/runtime: preparar backup/rollback explícito e pedir aprovação.")
    risk_plan["evidencia"].append(f"Health check usado: {health.get('path')} — disponível={health.get('available')} FAIL={health.get('fail_count')} WARN={health.get('warn_count')}.")
    risk_plan["proxima_acao_segura"].append("Executar somente correções documentais locais/PR quando health check, secret scan e diff estiverem limpos; bloquear produção/externo/credencial/runtime para aprovação Lucas.")
    return {
        "date": report_date,
        "overall_score": overall,
        "dimensions": [asdict(d) for d in dimensions],
        "health_check": {"path": health.get("path"), "available": health.get("available"), "fail_count": health.get("fail_count"), "warn_count": health.get("warn_count")},
        "safe_recommendations": safe_recommendations,
        "risk_prioritized_plan": risk_plan,
        "requires_lucas_approval": approvals,
        "non_changes": [
            "Produção",
            "VPS/Docker/Traefik/volumes/redes",
            "Bancos e dados vivos",
            "Secrets/credenciais",
            "Campanhas, WhatsApp, email, posts e contatos externos",
            "Cron, UI e runtime",
        ],
    }


def markdown(report: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append(f"# Brain Improvement Score — {report['date']}\n")
    lines.append("## Status geral\n")
    lines.append(f"Score geral: **{report['overall_score']}/100**\n")
    lines.append("Leitura executiva: relatório gerado por script local/read-only. O score traduz estrutura, health check e rastreabilidade do Brain em uma visão executiva; não prova saúde de produção, cron real, VPS, APIs ou dados vivos.\n")
    lines.append("## Resultado por dimensão\n")
    for d in report["dimensions"]:
        lines.append(f"### {d['label']} — {d['score']}/100\n")
        lines.append(f"Motivo: {d['reason']}\n")
        lines.append("Evidências:\n")
        for ev in d["evidence"]:
            lines.append(f"- {ev}\n")
        if d["recommendations"]:
            lines.append("Recomendações:\n")
            for rec in d["recommendations"]:
                lines.append(f"- {rec}\n")
        lines.append("")
    lines.append("## Correções seguras recomendadas\n")
    if report["safe_recommendations"]:
        for rec in report["safe_recommendations"]:
            lines.append(f"- {rec}\n")
    else:
        lines.append("- Nenhuma correção documental imediata detectada.\n")
    lines.append("\n## Plano priorizado por risco\n")
    labels = [
        ("seguranca_secrets_aprovacao", "Segurança/secrets/aprovação"),
        ("backup_rollback", "Backup/rollback"),
        ("integridade_estrutural", "Integridade estrutural"),
        ("evidencia", "Evidência"),
        ("proxima_acao_segura", "Próxima ação segura"),
        ("nao_tocar", "O que não será tocado"),
    ]
    for key, label in labels:
        lines.append(f"### {label}\n")
        items = report.get("risk_prioritized_plan", {}).get(key, [])
        if items:
            for item in items:
                lines.append(f"- {item}\n")
        else:
            lines.append("- Nenhum item crítico identificado nesta categoria.\n")
    lines.append("\n## Itens que exigem aprovação Lucas\n")
    for item in report["requires_lucas_approval"]:
        lines.append(f"- {item}\n")
    lines.append("\n## Evidências\n")
    hc = report["health_check"]
    lines.append(f"- Health check JSON: `{hc['path']}`; disponível={hc['available']}; FAIL={hc['fail_count']}; WARN={hc['warn_count']}.\n")
    lines.append("- Script: `scripts/brain_improvement_score.py`.\n")
    lines.append("- Fonte: arquivos versionados do Hermes Brain no working tree local.\n")
    lines.append("\n## Não alterado\n")
    for item in report["non_changes"]:
        lines.append(f"- {item}.\n")
    return "".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a read-only Hermes Brain Improvement Score report.")
    parser.add_argument("--health-json", type=Path, default=None, help="Optional brain_health_check JSON report to consume.")
    parser.add_argument("--date", default=date.today().isoformat(), help="Report date, default today.")
    parser.add_argument("--output", type=Path, default=None, help="Markdown output path.")
    parser.add_argument("--json-output", type=Path, default=None, help="JSON output path.")
    args = parser.parse_args()

    health = load_health(args.health_json)
    dimensions = [
        dimension_agents(health),
        dimension_maps(health),
        dimension_routines(health),
        dimension_skills(health),
        dimension_security(health),
        dimension_integrations(),
        dimension_tracking(),
        dimension_consistency(health),
    ]
    report = build_report(dimensions, health, args.date)

    output = args.output or ROOT / "reports" / f"brain-improvement-score-{args.date}-script.md"
    json_output = args.json_output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(markdown(report), encoding="utf-8")
    if json_output:
        json_output.parent.mkdir(parents=True, exist_ok=True)
        json_output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": rel(output), "json_output": rel(json_output) if json_output else None, "overall_score": report["overall_score"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
