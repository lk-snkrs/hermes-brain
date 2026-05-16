#!/usr/bin/env python3
"""Audit LK OS approval/decision artifacts for Telegram inline readiness.

Local/read-only. It scans markdown artifacts for approval/decision language and
flags items that may rely too much on local file paths or lack an inline approval
surface. No external API calls and no business-system writes.
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
LK_ROTINAS = ROOT / "areas/lk/rotinas"
OUT_JSON = REPORTS / "lk-os-telegram-approval-surface-audit-2026-05-12.json"
OUT_MD = REPORTS / "lk-os-telegram-approval-surface-audit-2026-05-12.md"
BRAIN_DOC = LK_ROTINAS / "lk-os-telegram-approval-surface-audit-2026-05-12.md"
INDEX = ROOT / "empresa/rotinas/_index.md"
CONTROL = ROOT / "areas/lk/projetos/lk-os-implementation-control.md"

APPROVAL_RE = re.compile(r"aprova|approval|preciso de resposta|próximo gate|next gate|autoriza", re.I)
PATH_RE = re.compile(r"/opt/data/|reports/|areas/lk/|\.json|\.csv|\.md")
INLINE_RE = re.compile(r"```|texto inline|frase de aprovação|approval wording|Preciso de resposta|Resumo inline", re.I)
SUPERSEDED_RE = re.compile(r"SUPERCEDED|SUPERSEDED|NÃO USAR|invalidado", re.I)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def classify(path: Path, text: str) -> dict:
    approval = bool(APPROVAL_RE.search(text))
    paths = len(PATH_RE.findall(text))
    inline = bool(INLINE_RE.search(text))
    superseded = bool(SUPERSEDED_RE.search(text))
    if not approval:
        state = "no_approval_surface_detected"
        priority = "monitor"
    elif superseded:
        state = "superseded_do_not_use"
        priority = "none"
    elif inline:
        state = "telegram_inline_ok"
        priority = "ok"
    elif paths:
        state = "needs_inline_telegram_surface"
        priority = "P1"
    else:
        state = "review_inline_clarity"
        priority = "P2"
    return {
        "path": str(path.relative_to(ROOT)),
        "state": state,
        "priority": priority,
        "approval_language_detected": approval,
        "local_path_references": paths,
        "inline_surface_detected": inline,
        "superseded_detected": superseded,
    }


def main() -> None:
    candidates: list[Path] = []
    for base in (REPORTS, LK_ROTINAS):
        if not base.exists():
            continue
        candidates.extend(sorted(base.glob("*.md")))
    # Keep audit bounded to current LK OS/GMC/LK reports, with recent naming.
    scoped = [p for p in candidates if any(k in p.name.lower() for k in ["lk-", "gmc", "merchant", "mission-control", "decision", "approval", "sourcing", "klaviyo"])]
    rows = []
    for p in scoped:
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        rows.append(classify(p, text))
    counts = {}
    for r in rows:
        counts[r["state"]] = counts.get(r["state"], 0) + 1
    needs = [r for r in rows if r["state"] == "needs_inline_telegram_surface"]
    review = [r for r in rows if r["state"] == "review_inline_clarity"]
    superseded = [r for r in rows if r["state"] == "superseded_do_not_use"]
    payload = {
        "generated_at": utc_now(),
        "status": "lk_os_telegram_approval_surface_audit_ready_no_write",
        "scope": "Local audit of LK OS approval artifacts for Telegram inline approval readiness; no external calls/writes.",
        "summary": {
            "scanned_markdown_artifacts": len(rows),
            "telegram_inline_ok": counts.get("telegram_inline_ok", 0),
            "needs_inline_telegram_surface": len(needs),
            "review_inline_clarity": len(review),
            "superseded_do_not_use": len(superseded),
            "no_approval_surface_detected": counts.get("no_approval_surface_detected", 0),
        },
        "p1_needs_inline": needs[:30],
        "p2_review_inline_clarity": review[:30],
        "superseded": superseded[:30],
        "not_performed": ["external_send", "business_system_write", "tiny_call", "shopify_call", "merchant_call", "notion_or_n8n_change", "supplier_contact"],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# LK OS — Telegram Approval Surface Audit, 2026-05-12",
        "",
        f"Generated at: `{payload['generated_at']}`",
        "",
        "## Veredito",
        "",
        "Auditoria local concluída para evitar o erro de pedir aprovação apenas por caminho de arquivo. Nada externo foi executado.",
        "",
        "## Resumo inline",
        "",
        f"- Artefatos markdown escaneados: {payload['summary']['scanned_markdown_artifacts']}",
        f"- Já parecem OK para Telegram inline: {payload['summary']['telegram_inline_ok']}",
        f"- P1 precisam de texto inline antes de qualquer aprovação: {payload['summary']['needs_inline_telegram_surface']}",
        f"- P2 revisar clareza inline: {payload['summary']['review_inline_clarity']}",
        f"- Supercedidos/não usar: {payload['summary']['superseded_do_not_use']}",
        "",
        "## P1 — não pedir aprovação sem reescrever inline no Telegram",
        "",
    ]
    if needs:
        for r in needs[:12]:
            lines.append(f"- `{r['path']}` — tem linguagem de aprovação/decisão, mas não detectei superfície inline suficiente; usar só como auditoria e colar o conteúdo no Telegram.")
    else:
        lines.append("- Nenhum P1 detectado neste scan.")
    lines.extend([
        "",
        "## Regra operacional aplicada",
        "",
        "Sempre que houver aprovação: mandar no Telegram o texto exato, escopo, riscos, o que autoriza e o que não autoriza. Caminho de JSON/CSV/MD é só trilha de auditoria.",
        "",
        "## Não executado",
        "",
    ])
    for item in payload["not_performed"]:
        lines.append(f"- {item}")
    text = "\n".join(lines) + "\n"
    OUT_MD.write_text(text, encoding="utf-8")
    BRAIN_DOC.write_text(text, encoding="utf-8")

    if INDEX.exists():
        line = "| LK OS Telegram Approval Surface Audit 2026-05-12 | `areas/lk/rotinas/lk-os-telegram-approval-surface-audit-2026-05-12.md` | Auditoria local para garantir que aprovações no Telegram tragam texto inline, não só caminhos JSON/CSV/MD |"
        idx = INDEX.read_text(encoding="utf-8")
        if line not in idx:
            INDEX.write_text(idx.rstrip() + "\n" + line + "\n", encoding="utf-8")
    if CONTROL.exists():
        marker = "### 2026-05-12 — LK OS Telegram approval surface audit"
        ctl = CONTROL.read_text(encoding="utf-8")
        block = (
            f"\n{marker}\n\n"
            f"- Status: `{payload['status']}`.\n"
            f"- Escaneados {payload['summary']['scanned_markdown_artifacts']} artefatos; {len(needs)} P1 precisam de reescrita inline antes de aprovação; {payload['summary']['telegram_inline_ok']} já parecem OK.\n"
            "- Regra Lucas aplicada: caminhos JSON/CSV/MD são auditoria; Telegram precisa carregar o conteúdo de aprovação no próprio texto.\n"
            "- Nenhum Tiny/Shopify/Merchant/Notion/fornecedor/write executado.\n"
        )
        if marker not in ctl:
            CONTROL.write_text(ctl.rstrip() + block + "\n", encoding="utf-8")
    print(json.dumps({"status": payload["status"], "summary": payload["summary"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
