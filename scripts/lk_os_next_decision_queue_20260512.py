#!/usr/bin/env python3
"""Build LK OS next-decision queue from existing read-only artifacts.

No external API calls. No writes outside local Brain reports/docs. This turns the
current Mission Control + approval ledger into a concise Lucas decision artifact
while long-running GMC/Tiny availability work continues separately.
"""
from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
OUT_JSON = REPORTS / "lk-os-next-decision-queue-2026-05-12.json"
OUT_CSV = REPORTS / "lk-os-next-decision-queue-2026-05-12.csv"
OUT_MD = REPORTS / "lk-os-next-decision-queue-2026-05-12.md"
BRAIN_DOC = ROOT / "areas/lk/rotinas/lk-os-next-decision-queue-2026-05-12.md"
CONTROL = ROOT / "areas/lk/projetos/lk-os-implementation-control.md"
MISSION_JSON = REPORTS / "lk-mission-control-snapshot-2026-05-12.json"
APPROVAL_JSON = REPORTS / "lk-os-approval-decision-log-router-2026-05-04_2026-05-10.json"
P1B_STATUS = REPORTS / "lk-gmc-2026-05-12-p1-availability-tiny-packet-running-status-2039.md"


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def brl(value) -> str:
    try:
        return f"R$ {float(value):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except Exception:
        return "R$ 0,00"


def build_rows() -> list[dict]:
    mission = load_json(MISSION_JSON)
    approval = load_json(APPROVAL_JSON)
    rows: list[dict] = []

    # 1) Supplier quote approvals: decision-only, no supplier contact yet.
    for item in approval.get("decision_log", []):
        status = item.get("current_status")
        route = item.get("route")
        if status != "needs_approval":
            continue
        priority = "P1"
        if item.get("default_safe_choice") == "hold_or_bundle_with_p0":
            priority = "P2"
        rows.append({
            "queue_id": item.get("decision_id"),
            "lane": "sourcing_quote_approval",
            "priority": priority,
            "title": item.get("family"),
            "decision_needed": item.get("recommended_decision"),
            "recommended_option": item.get("default_safe_choice"),
            "reference_qty_not_purchase_qty": item.get("reference_quote_qty_not_purchase_qty"),
            "evidence_value": item.get("revenue_signal_fact_shopify"),
            "source_label": "+".join(item.get("source_labels") or []),
            "owner": item.get("next_actor") or "Lucas/Júlio",
            "next_safe_action": item.get("if_approved_next_step"),
            "blocked_until_approval": ", ".join(item.get("separate_approval_required_after_quote") or []),
            "source_file": item.get("source_packet"),
            "write_allowed_now": False,
        })

    # 2) Internal hygiene / monitor rows from Mission Control, safe local/read-only only.
    for item in mission.get("open_items", []):
        lane = item.get("lane")
        if lane not in {"internal_code_hygiene", "data_resolved_monitor"}:
            continue
        rows.append({
            "queue_id": f"MC-{lane}-{item.get('title','').lower().replace(' ', '-')[:40]}",
            "lane": lane,
            "priority": item.get("priority") or "P1",
            "title": item.get("title"),
            "decision_needed": "Nenhuma ação externa; manter higiene/monitoramento local conforme evidência.",
            "recommended_option": "local_readonly_or_monitor",
            "reference_qty_not_purchase_qty": "",
            "evidence_value": "",
            "source_label": "derived_reconciliation",
            "owner": item.get("owner") or "Hermes/LK data spine",
            "next_safe_action": item.get("next_safe_action"),
            "blocked_until_approval": item.get("blocked"),
            "source_file": item.get("source"),
            "write_allowed_now": False,
        })

    # 3) CRM/Klaviyo and GMC gates: visible, but not executable without explicit approval / completion.
    crm = mission.get("crm_gate") or {}
    if crm:
        rows.append({
            "queue_id": "LK-CRM-P1-KLAVIYO-DRAFT",
            "lane": "crm_gate",
            "priority": crm.get("priority") or "P1",
            "title": crm.get("title"),
            "decision_needed": "Revisar campanha Draft; envio/agendamento/flow continuam bloqueados.",
            "recommended_option": "review_only_no_send",
            "reference_qty_not_purchase_qty": "",
            "evidence_value": "",
            "source_label": "fact_klaviyo_draft+manual_approval_required",
            "owner": "Lucas",
            "next_safe_action": crm.get("next_safe_action"),
            "blocked_until_approval": crm.get("blocked"),
            "source_file": "reports/lk-phase5-p1-klaviyo-klaviyo-objects-2026-05-11.md",
            "write_allowed_now": False,
        })

    gmc = mission.get("gmc_gate") or {}
    if gmc:
        rows.append({
            "queue_id": "LK-GMC-P1B-AVAILABILITY-TINY",
            "lane": "google_feed_availability",
            "priority": "P1",
            "title": "GMC P1-B availability via Tiny",
            "decision_needed": "Aguardar packet Tiny read-only finalizar; só aprovar availability para IDs ready com Tiny OK.",
            "recommended_option": "wait_packet_completion",
            "reference_qty_not_purchase_qty": "",
            "evidence_value": "",
            "source_label": "fact_tiny_stock_pending+manual_approval_required",
            "owner": "Hermes/LK data spine",
            "next_safe_action": "Monitorar processo P1-B; preparar approval packet final quando houver contadores finais.",
            "blocked_until_approval": "Merchant availability write; Tiny/Shopify/feed/DB/POS/campaign writes",
            "source_file": str(P1B_STATUS.relative_to(ROOT)) if P1B_STATUS.exists() else "running_process_proc_3ffabd6b94b9",
            "write_allowed_now": False,
        })

    lane_order = {
        "google_feed_availability": 0,
        "sourcing_quote_approval": 1,
        "crm_gate": 2,
        "internal_code_hygiene": 3,
        "data_resolved_monitor": 4,
    }
    prio_order = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
    rows.sort(key=lambda r: (prio_order.get(r.get("priority"), 9), lane_order.get(r.get("lane"), 9), -(float(r.get("evidence_value") or 0) if str(r.get("evidence_value") or "").replace('.', '', 1).isdigit() else 0)))
    return rows


def main() -> None:
    rows = build_rows()
    REPORTS.mkdir(parents=True, exist_ok=True)
    BRAIN_DOC.parent.mkdir(parents=True, exist_ok=True)

    lane_counts = Counter(r["lane"] for r in rows)
    priority_counts = Counter(r["priority"] for r in rows)
    approval_required = [r for r in rows if r["lane"] in {"sourcing_quote_approval", "crm_gate", "google_feed_availability"}]
    p1_sourcing = [r for r in rows if r["lane"] == "sourcing_quote_approval" and r["priority"] == "P1"]

    payload = {
        "generated_at": now(),
        "status": "lk_os_next_decision_queue_ready_no_write",
        "scope": "Consolidated LK OS next-decision queue from Mission Control + approval ledger; local/read-only artifact only.",
        "summary": {
            "rows": len(rows),
            "lane_counts": dict(lane_counts),
            "priority_counts": dict(priority_counts),
            "approval_required_items": len(approval_required),
            "p1_sourcing_quote_approval_items": len(p1_sourcing),
            "merchant_writes": 0,
            "tiny_writes": 0,
            "shopify_writes": 0,
            "klaviyo_sends_or_schedules": 0,
            "supplier_contacts": 0,
            "purchases_or_pos": 0,
            "marketplace_calls": 0,
            "n8n_flows": 0,
        },
        "rows": rows,
        "not_performed": [
            "merchant_write", "tiny_write", "shopify_write", "klaviyo_send_or_schedule",
            "supplier_contact", "purchase_order", "reservation", "marketplace_lookup",
            "database_write", "pos_write", "n8n_flow_creation"
        ],
        "files": {"json": str(OUT_JSON), "csv": str(OUT_CSV), "md": str(OUT_MD), "brain_doc": str(BRAIN_DOC)},
    }

    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    fields = ["queue_id", "lane", "priority", "title", "decision_needed", "recommended_option", "reference_qty_not_purchase_qty", "evidence_value", "source_label", "owner", "next_safe_action", "blocked_until_approval", "source_file", "write_allowed_now"]
    with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    lines = [
        "# LK OS — Next Decision Queue, 2026-05-12",
        "",
        f"Generated at: `{payload['generated_at']}`",
        "",
        "## Veredito",
        "",
        "Fila executiva pronta em modo local/read-only. Ela consolida o próximo bloco do LK OS sem tocar em Merchant, Tiny, Shopify, Klaviyo, fornecedor, cliente, compra, marketplace, banco, POS ou n8n.",
        "",
        "## Resumo",
        "",
        f"- Itens na fila: {len(rows)}",
        f"- Itens que exigem aprovação atual antes de execução externa/write: {len(approval_required)}",
        f"- Sourcing/cotação P1 aprováveis: {len(p1_sourcing)}",
        f"- Contagens por lane: `{dict(lane_counts)}`",
        f"- Contagens por prioridade: `{dict(priority_counts)}`",
        "",
        "## Top fila",
        "",
    ]
    for i, r in enumerate(rows[:10], 1):
        val = brl(r.get("evidence_value")) if r.get("evidence_value") not in (None, "") else "—"
        lines.extend([
            f"### {i}. {r.get('priority')} · {r.get('lane')} · {r.get('title')}",
            f"- Decisão: {r.get('decision_needed')}",
            f"- Recomendado: `{r.get('recommended_option')}`",
            f"- Fonte/valor: {r.get('source_label')} · {val}",
            f"- Próximo seguro: {r.get('next_safe_action')}",
            f"- Bloqueado até aprovação: {r.get('blocked_until_approval')}",
            f"- Source: `{r.get('source_file')}`",
            "",
        ])
    lines.extend([
        "## Não executado",
        "",
    ])
    for item in payload["not_performed"]:
        lines.append(f"- {item}")
    lines.extend([
        "",
        "## Preciso de resposta",
        "",
        "1. `Aprovar preparo de preview de cotação P1` — autoriza somente montar mensagens/briefs para fornecedor com destino nomeado depois; ainda não autoriza envio, compra ou reserva.",
        "2. `Revisar Klaviyo Draft` — mantém sem envio/agendamento; só prepara checklist de revisão no painel.",
        "3. `Aguardar GMC P1-B` — recomendada agora: deixa o packet Tiny terminar e depois decide availability com contadores finais.",
        "",
        "Recomendado: opção 3 em paralelo com opção 1 como preview local, sem contato externo.",
    ])
    text = "\n".join(lines) + "\n"
    OUT_MD.write_text(text, encoding="utf-8")
    BRAIN_DOC.write_text(text, encoding="utf-8")

    if CONTROL.exists():
        marker = "### 2026-05-12 — LK OS next decision queue"
        control = CONTROL.read_text(encoding="utf-8")
        block = (
            f"\n{marker}\n\n"
            f"- Status: `{payload['status']}`.\n"
            f"- Fila local/read-only consolidada: {len(rows)} itens; {len(approval_required)} exigem aprovação atual antes de execução; {len(p1_sourcing)} sourcing/cotação P1 aprováveis.\n"
            f"- Arquivos: `reports/lk-os-next-decision-queue-2026-05-12.md` e `areas/lk/rotinas/lk-os-next-decision-queue-2026-05-12.md`.\n"
            f"- Nenhum Merchant/Tiny/Shopify/Klaviyo/fornecedor/compra/marketplace/DB/POS/n8n write ou envio executado.\n"
        )
        if marker not in control:
            CONTROL.write_text(control.rstrip() + block + "\n", encoding="utf-8")

    print(json.dumps({"status": payload["status"], "summary": payload["summary"], "public_report": str(OUT_MD)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
