#!/usr/bin/env python3
"""Build sanitized LK Compras ranking preview from local wacli signal queue raw source.

Read-only/local only. No WhatsApp sends, no supplier contact, no purchases, no Notion writes.
Outputs sanitized ranking artifacts without names, phones, JIDs or literal message text.
"""
from __future__ import annotations

import json
import os
import re
import hashlib
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/opt/data/hermes_bruno_ingest/hermes-brain")
PRIVATE_DIR = Path("/opt/data/hermes_bruno_ingest/local_sql/wacli_lk_compras")
SIGNAL_REPORT = ROOT / "reports/lk-compras-whatsapp-signal-queue-2026-05-13.json"
OUT_JSON = ROOT / "reports/lk-compras-ranking-preview-2026-05-13.json"
OUT_MD = ROOT / "reports/lk-compras-ranking-preview-2026-05-13.md"
ROUTINE_MD = ROOT / "areas/lk/rotinas/lk-compras-ranking-preview-2026-05-13.md"

PII_RE = re.compile(r"\b\d{8,}@(?:s\.whatsapp\.net|g\.us)\b|\b\+?55?\d{10,13}\b", re.I)
URL_RE = re.compile(r"https?://\S+", re.I)
PRICE_RE = re.compile(r"(?:R\$\s*)?(?<!\d)(\d{3,5})(?:[,.](\d{2}))?(?!\d)")
SIZE_RE = re.compile(r"\b(?:BR\s*)?(3[4-9]|4[0-6])\b|\bUS\s*(?:M|W)?\s*(\d{1,2}(?:[.,]5)?)\b", re.I)

CLASSES = {
    "pedido_de_compra": ["pedido", "pedir", "cotação", "cotacao", "comprar", "compra", "preciso", "procurando", "consegue", "encomenda", "busco", "procuro"],
    "resposta_fornecedor": ["tenho", "temos", "disponível", "disponivel", "chegou", "consigo", "separar", "disponibilidade", "tem sim"],
    "negociacao_preco": ["valor", "preço", "preco", "quanto", "desconto", "pix", "boleto", "cartão", "cartao", "à vista", "avista", "menor", "fecha", "fechar"],
    "proximidade_sp_logistica": ["são paulo", "sao paulo", " sp", "entrega", "retirada", "retirar", "motoboy", "sedex", "transportadora", "envio", "prazo", "chega", "zona"],
    "fechamento_compra": ["fechado", "fechou", "vou ficar", "pode separar", "manda pix", "paguei", "pagamento", "comprado", "nota", "nf", "notion", "lançar", "lancar"],
    "produto_tamanho_estoque": ["estoque", "grade", "numeração", "numeracao", "tamanho", "unidade", "par ", "pares", "us ", "br ", "tam"],
}

BRANDS = [
    "air jordan", "jordan", "nike", "dunk", "air force", "af1", "yeezy", "adidas", "samba", "gazelle", "new balance", "nb", "asics", "gel", "puma", "mizuno", "on", "salomon", "travis", "off-white", "supreme", "bape", "fear of god", "essentials", "amiri", "stone island", "represent", "hellstar", "corteiz", "cortiez", "gallery dept", "denim tears", "sp5der", "chrome hearts", "stussy"
]
COLOR_HINTS = ["black", "white", "red", "blue", "green", "grey", "gray", "preto", "branco", "vermelho", "azul", "verde", "cinza", "bege", "cream", "brown", "marrom", "olive", "pink", "rosa", "navy"]


def clean_text(m: dict) -> str:
    text = "\n".join(str(m.get(k, "")) for k in ("Text", "DisplayText", "MediaCaption") if m.get(k))
    text = PII_RE.sub(" ", text)
    text = URL_RE.sub(" link ", text)
    return text[:5000]


def chat_hash(m: dict) -> str:
    return hashlib.sha256(str(m.get("ChatJID", "")).encode()).hexdigest()[:10]


def signal_id(m: dict) -> str:
    raw = f"{m.get('ChatJID','')}|{m.get('MsgID','')}|{m.get('Timestamp','')}"
    return hashlib.sha256(raw.encode()).hexdigest()[:12]


def classify(text: str) -> list[str]:
    low = text.lower()
    return [name for name, kws in CLASSES.items() if any(kw in low for kw in kws)]


def extract_prices(text: str) -> list[int]:
    vals = []
    for m in PRICE_RE.finditer(text):
        val = int(m.group(1))
        # avoid treating BR sizes or years as prices
        if 250 <= val <= 50000 and val not in range(34, 47):
            vals.append(val)
    return vals[:10]


def extract_sizes(text: str) -> list[str]:
    vals = []
    for m in SIZE_RE.finditer(text):
        v = m.group(1) or m.group(2)
        if v:
            vals.append(v.replace(",", "."))
    return sorted(set(vals), key=lambda x: float(x) if x.replace('.', '', 1).isdigit() else 999)[:12]


def product_tokens(text: str) -> list[str]:
    low = text.lower()
    hits = []
    for brand in BRANDS:
        if brand in low:
            hits.append(brand)
    # Capture common model-like fragments around hit brands without using full literal message.
    tokens = re.findall(r"\b(?:jordan|dunk|yeezy|samba|gazelle|air force|new balance|asics|gel|travis|amiri|essentials|represent|hellstar|sp5der|stussy|corteiz|cortiez|bape|supreme)\b(?:\s+[a-z0-9-]{2,12}){0,3}", low)
    for t in tokens:
        if t not in hits:
            hits.append(t.strip())
    colors = [c for c in COLOR_HINTS if c in low]
    # Keep product-level hints only; never include message sentences.
    return (hits[:4] + colors[:2])[:6]


def logistic_flags(text: str) -> list[str]:
    low = text.lower()
    flags = []
    if any(k in low for k in ["são paulo", "sao paulo", " sp", "zona"]):
        flags.append("proximidade_sp")
    if any(k in low for k in ["retirada", "retirar", "motoboy"]):
        flags.append("retirada/motoboy")
    if any(k in low for k in ["sedex", "transportadora", "envio", "entrega"]):
        flags.append("envio/transportadora")
    if any(k in low for k in ["prazo", "chega"]):
        flags.append("prazo")
    return flags


def band_price(prices: list[int]) -> str:
    if not prices:
        return "sem preço detectado"
    return f"R$ {min(prices):,}".replace(",", ".") if min(prices) == max(prices) else f"R$ {min(prices):,}–{max(prices):,}".replace(",", ".")


def main() -> None:
    signal = json.loads(SIGNAL_REPORT.read_text())
    raw_path = Path(signal["private_raw_path"])
    obj = json.loads(raw_path.read_text(errors="replace"), strict=False)
    messages = obj.get("messages") or []
    generated_at = datetime.now(timezone.utc).isoformat()

    clusters: dict[str, dict] = {}
    for m in messages:
        text = clean_text(m)
        classes = classify(text)
        if not classes:
            continue
        ch = chat_hash(m)
        ptoks = product_tokens(text)
        sizes = extract_sizes(text)
        prices = extract_prices(text)
        lflags = logistic_flags(text)
        # If product unknown, cluster by chat and class group; this remains a queue candidate, not a product fact.
        product_key = "+".join(ptoks[:2]) if ptoks else "produto_nao_identificado"
        size_key = "+".join(sizes[:3]) if sizes else "tam_nao_identificado"
        key = f"{ch}|{product_key}|{size_key}"
        c = clusters.setdefault(key, {
            "ranking_id": hashlib.sha256(key.encode()).hexdigest()[:12],
            "source_label": "platform_signal_wacli_local",
            "chat_hash": ch,
            "product_hint": product_key.replace("+", " / "),
            "sizes_detected": set(),
            "prices_detected": [],
            "logistic_flags": Counter(),
            "signal_classes": Counter(),
            "signal_ids": [],
            "latest_timestamp_utc": None,
            "message_count": 0,
        })
        c["message_count"] += 1
        c["signal_ids"].append(signal_id(m))
        for s in sizes: c["sizes_detected"].add(s)
        c["prices_detected"].extend(prices)
        c["logistic_flags"].update(lflags)
        c["signal_classes"].update(classes)
        ts = m.get("Timestamp")
        if ts and (not c["latest_timestamp_utc"] or ts > c["latest_timestamp_utc"]):
            c["latest_timestamp_utc"] = ts

    ranked = []
    for c in clusters.values():
        classes = c["signal_classes"]
        has_price = bool(c["prices_detected"])
        has_size = bool(c["sizes_detected"])
        has_logistics = bool(c["logistic_flags"])
        has_product = c["product_hint"] != "produto_nao_identificado"
        score = (
            c["message_count"]
            + 4 * classes.get("pedido_de_compra", 0)
            + 3 * classes.get("resposta_fornecedor", 0)
            + 3 * classes.get("negociacao_preco", 0)
            + 2 * classes.get("proximidade_sp_logistica", 0)
            + 2 * classes.get("fechamento_compra", 0)
            + 2 * int(has_price)
            + 2 * int(has_size)
            + 2 * int(has_logistics)
            + 2 * int(has_product)
        )
        if classes.get("fechamento_compra") and not classes.get("pedido_de_compra"):
            recommended_next_step = "notion_logging_preview_only_if_human_purchase_confirmed"
        elif has_price and has_logistics:
            recommended_next_step = "rank_cheapest_vs_closer_to_sp"
        elif has_price:
            recommended_next_step = "compare_price_options"
        elif has_product or has_size:
            recommended_next_step = "validate_product_size_stock_context"
        else:
            recommended_next_step = "needs_manual_context_or_ignore"
        ranked.append({
            "ranking_id": c["ranking_id"],
            "rank_score": score,
            "source_label": c["source_label"],
            "chat_hash": c["chat_hash"],
            "product_hint": c["product_hint"],
            "sizes_detected": sorted(c["sizes_detected"], key=lambda x: float(x) if x.replace('.', '', 1).isdigit() else 999),
            "price_band_detected": band_price(c["prices_detected"]),
            "min_price_detected_brl": min(c["prices_detected"]) if c["prices_detected"] else None,
            "max_price_detected_brl": max(c["prices_detected"]) if c["prices_detected"] else None,
            "logistic_flags": [k for k, _ in c["logistic_flags"].most_common()],
            "signal_classes": dict(c["signal_classes"].most_common()),
            "message_count": c["message_count"],
            "latest_timestamp_utc": c["latest_timestamp_utc"],
            "evidence_signal_ids": c["signal_ids"][:6],
            "recommended_next_step": recommended_next_step,
            "blocked_before_approval": ["whatsapp_send", "supplier_contact", "purchase", "reservation", "notion_write", "shopify_tiny_write", "cron_or_automation"],
        })

    ranked.sort(key=lambda x: (x["rank_score"], x.get("latest_timestamp_utc") or ""), reverse=True)
    top = ranked[:25]
    out = {
        "generated_at": generated_at,
        "status": "read_only_sanitized_ranking_preview_ready",
        "source_label": "platform_signal_wacli_local",
        "input_signal_report": str(SIGNAL_REPORT),
        "messages_scanned": len(messages),
        "candidate_clusters": len(ranked),
        "top_count": len(top),
        "ranking_formula": "message_count + weighted purchase/supplier/price/logistics/closing classes + evidence bonuses; not an approval to buy/contact/write",
        "top_ranked_candidates": top,
        "non_actions": ["no_whatsapp_send", "no_supplier_contact", "no_customer_contact", "no_purchase", "no_reservation", "no_notion_write", "no_shopify_tiny_merchant_db_write", "no_cron"],
    }
    OUT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=2))

    md = [
        "# LK Compras — Ranking Preview v1",
        "",
        "Status: `read_only_sanitized_ranking_preview_ready`",
        f"Data: {generated_at}",
        "Fonte: `platform_signal_wacli_local` (`lk-compras`) a partir da Signal Queue v1.",
        "",
        "## Veredito",
        "",
        "Criei um preview de ranking local/sanitizado para priorizar sinais de compra por produto/tamanho/preço/logística. Isto ainda é sinal de WhatsApp, não fato de compra, estoque ou fornecedor validado.",
        "",
        "## Resumo técnico",
        "",
        f"- Mensagens reprocessadas: {len(messages)}.",
        f"- Clusters candidatos: {len(ranked)}.",
        f"- Top candidatos no preview: {len(top)}.",
        "- Critério: volume + pedido/resposta/negociação/preço/logística/fechamento + presença de produto/tamanho.",
        "- Sem nomes, telefones, JIDs ou texto literal de mensagens.",
        "",
        "## Top candidatos sanitizados",
        "",
    ]
    for i, c in enumerate(top[:10], 1):
        md += [
            f"### {i}. Ranking `{c['ranking_id']}` — score {c['rank_score']}",
            "",
            f"- Produto/hint: `{c['product_hint']}`.",
            f"- Tamanhos detectados: {', '.join(c['sizes_detected']) if c['sizes_detected'] else 'não identificado'}.",
            f"- Preço detectado: {c['price_band_detected']}.",
            f"- Logística: {', '.join(c['logistic_flags']) if c['logistic_flags'] else 'sem sinal logístico claro'}.",
            f"- Classes: {', '.join(f'{k}={v}' for k, v in c['signal_classes'].items())}.",
            f"- Próximo passo recomendado: `{c['recommended_next_step']}`.",
            f"- Evidência: {len(c['evidence_signal_ids'])} IDs sanitizados; chat_hash `{c['chat_hash']}`; última msg `{c['latest_timestamp_utc']}`.",
            "",
        ]
    md += [
        "## Como usar operacionalmente",
        "",
        "1. Confirmar produto/tamanho exato no contexto privado antes de qualquer ação.",
        "2. Se houver preço + logística, comparar menor preço viável versus fonte mais próxima de São Paulo quando a diferença for pequena.",
        "3. Se virar compra humana, preparar somente um preview de lançamento Notion; write no Notion exige aprovação separada.",
        "",
        "## Não executado",
        "",
        "- Nenhum WhatsApp enviado.",
        "- Nenhum contato com fornecedor/grupo/cliente.",
        "- Nenhuma compra, reserva, pagamento ou escolha final de fornecedor.",
        "- Nenhum write em Notion, Shopify, Tiny, banco, Klaviyo, Meta, Google ou n8n.",
        "- Nenhum cron/automação recorrente criado.",
        "",
        "## Próximo seguro",
        "",
        "A próxima evolução é uma calibragem read-only mais precisa por janela de 24h/7d, com amostras privadas e regras melhores de extração de modelo, tamanho, preço e distância logística. Qualquer envio, compra, contato ou Notion write continua bloqueado até aprovação explícita com payload inline.",
        "",
    ]
    OUT_MD.write_text("\n".join(md))
    ROUTINE_MD.parent.mkdir(parents=True, exist_ok=True)
    ROUTINE_MD.write_text("\n".join(md))
    print(json.dumps({
        "status": out["status"],
        "messages_scanned": out["messages_scanned"],
        "candidate_clusters": out["candidate_clusters"],
        "top_count": out["top_count"],
        "top_preview": top[:3],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
