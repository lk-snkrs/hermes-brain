#!/usr/bin/env python3
"""LK OS stockout sourcing router template.

Creates a no-write, no-marketplace-call operational template for the corrected LK
sourcing flow Lucas specified on 2026-05-12.

This script does not query Droper, StockX, GOAT, Notion/n8n, Shopify, Tiny or any
external system. It only materializes the approved decision logic and Telegram
inline approval surface so future runs do not point Lucas only to local files.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
OUT_JSON = REPORTS / "lk-os-stockout-sourcing-router-template-2026-05-12.json"
OUT_MD = REPORTS / "lk-os-stockout-sourcing-router-template-2026-05-12.md"
BRAIN_DOC = ROOT / "areas/lk/rotinas/lk-os-stockout-sourcing-router-template-2026-05-12.md"
INDEX = ROOT / "empresa/rotinas/_index.md"
CONTROL = ROOT / "areas/lk/projetos/lk-os-implementation-control.md"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def main() -> None:
    REPORTS.mkdir(parents=True, exist_ok=True)
    BRAIN_DOC.parent.mkdir(parents=True, exist_ok=True)

    payload = {
        "generated_at": utc_now(),
        "status": "lk_os_stockout_sourcing_router_template_ready_no_write",
        "purpose": "Corrected LK sourcing router for sold/requested products with confirmed stockout; Telegram approval surface must be inline.",
        "trigger_required": [
            "order_or_request_context_present",
            "exact_product_sku_size_known",
            "stockout_zero_availability_confirmed",
        ],
        "routing_order": [
            "check_droper_first_for_availability_and_cost",
            "if_droper_unavailable_compare_stockx_vs_goat_after_size_normalization",
            "select_cheapest_viable_source_as_recommendation_only",
            "prepare_notion_or_julio_task_with_link_cost_context",
        ],
        "never_authorized_for_hermes": [
            "purchase",
            "reservation",
            "purchase_order",
            "supplier_or_whatsapp_compras_contact_without_explicit_approval",
            "delivery_address_choice",
            "importer_or_bring_to_brazil_supplier_choice",
            "shopify_write",
            "tiny_write",
            "merchant_write",
            "notion_or_n8n_flow_activation_without_explicit_approval",
        ],
        "telegram_inline_template": {
            "title": "Router de reposição por stockout — [produto]",
            "body": [
                "Pedido/necessidade: [pedido ou contexto]",
                "Produto/SKU/tamanho: [produto] · [SKU] · [tamanho]",
                "Status de estoque: [stockout confirmado por fonte]",
                "Droper: [tem/não tem] · [preço/link se consultado]",
                "StockX: [preço/link se Droper não tiver]",
                "GOAT: [preço/link se Droper não tiver]",
                "Recomendação para Júlio: [fonte mais barata viável]",
                "Tarefa sugerida: Júlio comprar/avaliar pelo link [link], custo [valor], observações [lead time/tamanho/risco].",
                "Não autorizado: Hermes comprar, reservar, escolher endereço/importador, acionar fornecedor/grupo ou alterar Shopify/Tiny/Merchant.",
            ],
        },
        "approval_wording_inline": "Aprovo criar tarefa para Júlio/Notion com este produto/SKU/tamanho e a fonte recomendada, apenas como orientação de compra humana; não autorizo Hermes a comprar, reservar, escolher endereço/importador, contatar fornecedor/grupo, nem alterar Shopify/Tiny/Merchant.",
        "not_performed": [
            "droper_lookup",
            "stockx_lookup",
            "goat_lookup",
            "notion_or_n8n_creation",
            "supplier_contact",
            "purchase",
            "reservation",
            "shopify_write",
            "tiny_write",
            "merchant_write",
            "database_write",
        ],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# LK OS — Stockout Sourcing Router Template, 2026-05-12",
        "",
        f"Generated at: `{payload['generated_at']}`",
        "",
        "## Veredito",
        "",
        "Template operacional pronto para substituir cotação genérica por sourcing somente quando houver venda/pedido + stockout confirmado.",
        "",
        "## Gatilho obrigatório",
        "",
        "- Existe venda/pedido/necessidade concreta.",
        "- Produto, SKU e tamanho estão definidos.",
        "- Stockout/estoque zero foi confirmado pela fonte correta antes de sourcing.",
        "",
        "## Ordem correta",
        "",
        "1. Droper primeiro: disponibilidade + custo + link.",
        "2. Se Droper não tiver: comparar StockX vs GOAT, normalizando tamanho.",
        "3. Recomendar menor fonte viável somente como orientação.",
        "4. Preparar tarefa para Júlio/Notion com contexto, link, custo e ressalvas.",
        "",
        "## Texto inline para Telegram / aprovação",
        "",
        "```text",
        "Router de reposição por stockout — [produto]",
        "",
        "Pedido/necessidade: [pedido ou contexto]",
        "Produto/SKU/tamanho: [produto] · [SKU] · [tamanho]",
        "Status de estoque: [stockout confirmado por fonte]",
        "",
        "Droper: [tem/não tem] · [preço/link se consultado]",
        "StockX: [preço/link se Droper não tiver]",
        "GOAT: [preço/link se Droper não tiver]",
        "",
        "Recomendação para Júlio: [fonte mais barata viável]",
        "Tarefa sugerida: Júlio comprar/avaliar pelo link [link], custo [valor], observações [lead time/tamanho/risco].",
        "",
        "Não autorizado: Hermes comprar, reservar, escolher endereço/importador, acionar fornecedor/grupo ou alterar Shopify/Tiny/Merchant.",
        "```",
        "",
        "## Frase de aprovação inline",
        "",
        f"`{payload['approval_wording_inline']}`",
        "",
        "## Nunca autorizado para Hermes",
        "",
    ]
    for item in payload["never_authorized_for_hermes"]:
        lines.append(f"- {item}")
    lines.extend(["", "## Não executado", ""])
    for item in payload["not_performed"]:
        lines.append(f"- {item}")
    text = "\n".join(lines) + "\n"
    OUT_MD.write_text(text, encoding="utf-8")
    BRAIN_DOC.write_text(text, encoding="utf-8")

    if INDEX.exists():
        line = "| LK OS Stockout Sourcing Router Template 2026-05-12 | `areas/lk/rotinas/lk-os-stockout-sourcing-router-template-2026-05-12.md` | Template corrigido: sourcing só por venda/pedido + stockout; Droper primeiro; StockX/GOAT fallback; tarefa Júlio/Notion; aprovação inline no Telegram |"
        idx = INDEX.read_text(encoding="utf-8")
        if line not in idx:
            INDEX.write_text(idx.rstrip() + "\n" + line + "\n", encoding="utf-8")

    if CONTROL.exists():
        marker = "### 2026-05-12 — LK OS stockout sourcing router template"
        ctl = CONTROL.read_text(encoding="utf-8")
        block = (
            f"\n{marker}\n\n"
            f"- Status: `{payload['status']}`.\n"
            "- Correção Lucas operacionalizada: sourcing/reposição só por venda/pedido + stockout confirmado; Droper primeiro; StockX/GOAT fallback; tarefa Júlio/Notion; aprovação inline no Telegram.\n"
            "- Nenhum marketplace/Notion/n8n/fornecedor/compra/reserva/Shopify/Tiny/Merchant write executado.\n"
        )
        if marker not in ctl:
            CONTROL.write_text(ctl.rstrip() + block + "\n", encoding="utf-8")

    print(json.dumps({"status": payload["status"], "report": str(OUT_MD)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
