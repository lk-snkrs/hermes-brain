#!/usr/bin/env python3
"""SUPERSEDED: do not use this script to prepare supplier quote sends.

Lucas corrected LK sourcing logic on 2026-05-12: replenishment sourcing must
start from a concrete sold/requested stockout SKU/size, then check Droper, then
compare StockX vs GOAT only if Droper lacks it, and prepare a Notion/Júlio task.
This old family-level generic supplier quote preview is retained only for audit.
"""
from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
SOURCE = REPORTS / "lk-os-supplier-quote-approval-packet-2026-05-04_2026-05-10.json"
OUT_JSON = REPORTS / "lk-os-supplier-quote-send-preview-2026-05-12.json"
OUT_CSV = REPORTS / "lk-os-supplier-quote-send-preview-2026-05-12.csv"
OUT_MD = REPORTS / "lk-os-supplier-quote-send-preview-2026-05-12.md"
BRAIN_DOC = ROOT / "areas/lk/rotinas/lk-os-supplier-quote-send-preview-2026-05-12.md"
CONTROL = ROOT / "areas/lk/projetos/lk-os-implementation-control.md"
INDEX = ROOT / "empresa/rotinas/_index.md"


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def brl(v) -> str:
    try:
        return "R$ " + f"{float(v):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except Exception:
        return "R$ 0,00"


def normalize_message(raw: str, family: str) -> str:
    # Keep the original operational content, add destination/approval guardrails.
    return "\n".join([
        "[DESTINO: fornecedor a confirmar por Lucas/Júlio]",
        f"[ASSUNTO/CONTEXTO: Cotação LK — {family}]",
        "",
        raw.strip(),
        "",
        "Observação interna: enviar somente após Lucas/Júlio aprovar destino e envio. Esta mensagem não autoriza compra, reserva, faturamento ou separação.",
    ])


def main() -> None:
    raise SystemExit(
        "SUPERSEDED_DO_NOT_RUN: Lucas corrected LK sourcing logic on 2026-05-12. "
        "Use a sold/requested stockout router: exact SKU/size + stockout -> Droper -> "
        "StockX/GOAT comparison -> Notion/Júlio task. Do not generate generic supplier quote sends."
    )
    src = json.loads(SOURCE.read_text(encoding="utf-8"))
    decisions = src.get("decisions") or []
    ready = [d for d in decisions if d.get("approval_status") == "ready_for_approval_quote_only"]
    optional = [d for d in decisions if d.get("approval_status") == "optional_quote_or_hold"]
    previews = []
    for d in ready:
        previews.append({
            "preview_id": d.get("decision_id"),
            "family": d.get("family"),
            "status": "ready_for_lucas_destination_and_send_approval",
            "priority": "P1",
            "recommended_decision": d.get("recommended_decision"),
            "supplier_destination": "pending_lucas_or_julio_selection",
            "items_count": d.get("items_count"),
            "p0_count": d.get("p0_count"),
            "p1_count": d.get("p1_count"),
            "reference_quote_qty_not_purchase_qty": d.get("reference_quote_qty_not_purchase_qty"),
            "revenue_signal_fact_shopify": d.get("revenue_signal_fact_shopify"),
            "source_labels": d.get("source_labels") or [],
            "copy_ready_message_not_sent": normalize_message(d.get("supplier_brief_preview_not_sent") or "", d.get("family") or ""),
            "approval_required_before_send": ["supplier_destination_selection", "external_send_approval"],
            "still_blocked_after_send_approval": ["purchase", "purchase_order", "reservation", "shopify_write", "tiny_write", "price_or_stock_change", "campaign_or_external_send"],
            "external_send_status": "not_sent",
            "write_allowed_now": False,
        })

    payload = {
        "generated_at": now(),
        "status": "lk_os_supplier_quote_send_preview_ready_no_send",
        "scope": "Copy-ready supplier quote previews for P1 sourcing families; local/preview only, no external send.",
        "source_packet": str(SOURCE.relative_to(ROOT)),
        "summary": {
            "preview_messages": len(previews),
            "ready_families": len(ready),
            "optional_families_not_included": len(optional),
            "reference_quote_qty_not_purchase_qty": sum(int(p.get("reference_quote_qty_not_purchase_qty") or 0) for p in previews),
            "revenue_signal_fact_shopify": round(sum(float(p.get("revenue_signal_fact_shopify") or 0) for p in previews), 2),
            "supplier_contacts": 0,
            "external_sends": 0,
            "purchases_or_pos": 0,
            "shopify_writes": 0,
            "tiny_writes": 0,
            "database_writes": 0,
            "marketplace_calls": 0,
            "n8n_flows": 0,
        },
        "previews": previews,
        "optional_not_included": [d.get("family") for d in optional],
        "approval_wording": "Aprovo enviar as 4 mensagens de cotação P1 exatamente como preview, para os fornecedores/destinos que eu indicar, apenas para disponibilidade/custo/lead time; não autorizo compra, reserva, PO, Shopify/Tiny/preço/estoque/campanha.",
        "not_performed": ["supplier_contact", "external_send", "purchase", "purchase_order", "reservation", "shopify_write", "tiny_write", "price_or_stock_change", "campaign_send", "database_write", "marketplace_lookup", "n8n_flow_creation"],
        "files": {"json": str(OUT_JSON), "csv": str(OUT_CSV), "md": str(OUT_MD), "brain_doc": str(BRAIN_DOC)},
    }

    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    fields = ["preview_id", "family", "status", "priority", "supplier_destination", "items_count", "p0_count", "p1_count", "reference_quote_qty_not_purchase_qty", "revenue_signal_fact_shopify", "external_send_status", "write_allowed_now", "copy_ready_message_not_sent"]
    with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader(); w.writerows(previews)

    lines = [
        "# LK OS — Supplier Quote Send Preview, 2026-05-12",
        "",
        f"Generated at: `{payload['generated_at']}`",
        "",
        "## Veredito",
        "",
        "Preview local pronto para 4 mensagens de cotação P1. Nada foi enviado. Destino do fornecedor ainda precisa ser indicado/aprovado por Lucas/Júlio.",
        "",
        "## Resumo",
        "",
        f"- Mensagens preview: {len(previews)}",
        f"- Quantidade referência de cotação, não compra: {payload['summary']['reference_quote_qty_not_purchase_qty']}",
        f"- Sinal de receita Shopify: {brl(payload['summary']['revenue_signal_fact_shopify'])}",
        f"- Opcionais não incluídos por padrão: {', '.join(payload['optional_not_included']) if payload['optional_not_included'] else 'nenhum'}",
        "- Supplier contact / external send / purchase / PO / reservation / writes: 0",
        "",
        "## Mensagens preview — não enviadas",
        "",
    ]
    for idx, p in enumerate(previews, 1):
        lines.extend([
            f"### {idx}. {p['family']}",
            f"- Status: `{p['status']}`",
            f"- Itens/P0/P1: {p['items_count']} / {p['p0_count']} / {p['p1_count']}",
            f"- Quantidade referência, não compra: {p['reference_quote_qty_not_purchase_qty']}",
            f"- Receita Shopify sinal: {brl(p['revenue_signal_fact_shopify'])}",
            "- Mensagem:",
            "```text",
            p["copy_ready_message_not_sent"],
            "```",
            "",
        ])
    lines.extend([
        "## Approval wording",
        "",
        f"`{payload['approval_wording']}`",
        "",
        "## Não executado",
        "",
    ])
    for item in payload["not_performed"]:
        lines.append(f"- {item}")
    lines.extend([
        "",
        "## Próximo gate",
        "",
        "Para executar envio real, Lucas/Júlio precisa indicar destino/fornecedor e aprovar envio externo explicitamente. Mesmo aprovado o envio, compra/reserva/PO continuam bloqueados até nova aprovação depois da resposta do fornecedor.",
    ])
    text = "\n".join(lines) + "\n"
    OUT_MD.write_text(text, encoding="utf-8")
    BRAIN_DOC.write_text(text, encoding="utf-8")

    if CONTROL.exists():
        marker = "### 2026-05-12 — LK OS supplier quote send preview"
        current = CONTROL.read_text(encoding="utf-8")
        block = (
            f"\n{marker}\n\n"
            f"- Status: `{payload['status']}`.\n"
            f"- Preview local de {len(previews)} mensagens P1 para cotação; quantidade referência {payload['summary']['reference_quote_qty_not_purchase_qty']} un; sinal Shopify {brl(payload['summary']['revenue_signal_fact_shopify'])}.\n"
            f"- Destinos/fornecedores continuam pendentes de Lucas/Júlio; nenhum envio/contato/compra/PO/reserva/write executado.\n"
            f"- Arquivo: `reports/lk-os-supplier-quote-send-preview-2026-05-12.md`.\n"
        )
        if marker not in current:
            CONTROL.write_text(current.rstrip() + block, encoding="utf-8")

    if INDEX.exists():
        line = "| LK Supplier Quote Send Preview 2026-05-12 | `areas/lk/rotinas/lk-os-supplier-quote-send-preview-2026-05-12.md` | Preview local de 4 mensagens P1 para cotação a fornecedor, com destino pendente e 0 envio/compra/write |"
        idx = INDEX.read_text(encoding="utf-8")
        if line not in idx:
            marker = "| LK Supplier Quote Approval Packet Read-only 2026-05-11 |"
            if marker in idx:
                idx = idx.replace(marker, line + "\n" + marker)
            else:
                idx = idx.rstrip() + "\n" + line + "\n"
            INDEX.write_text(idx, encoding="utf-8")

    print(json.dumps({"status": payload["status"], "summary": payload["summary"], "public_report": str(OUT_MD)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
