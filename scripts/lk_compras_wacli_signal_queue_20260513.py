#!/usr/bin/env python3
"""Build a sanitized LK Compras WhatsApp signal queue from local wacli store.

Read-only: calls wacli with --read-only and writes only local sanitized/private artifacts.
No WhatsApp sends, no Notion writes, no external contact.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import hashlib
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

WACLI = "/opt/data/bin/wacli"
ACCOUNT = "lk-compras"
ROOT = Path("/opt/data/hermes_bruno_ingest/hermes-brain")
PRIVATE_DIR = Path("/opt/data/hermes_bruno_ingest/local_sql/wacli_lk_compras")
REPORT_JSON = ROOT / "reports/lk-compras-whatsapp-signal-queue-2026-05-13.json"
REPORT_MD = ROOT / "reports/lk-compras-whatsapp-signal-queue-2026-05-13.md"
ROUTINE_MD = ROOT / "areas/lk/rotinas/lk-compras-whatsapp-signal-queue-2026-05-13.md"

CLASSES = {
    "pedido_de_compra": ["pedido", "pedir", "cotação", "cotacao", "comprar", "compra", "preciso", "procurando", "consegue", "encomenda", "busco", "procuro"],
    "resposta_fornecedor": ["tenho", "temos", "disponível", "disponivel", "chegou", "consigo", "separar", "disponibilidade", "tem sim"],
    "negociacao_preco": ["valor", "preço", "preco", "quanto", "desconto", "pix", "boleto", "cartão", "cartao", "à vista", "avista", "menor", "fecha", "fechar"],
    "proximidade_sp_logistica": ["são paulo", "sao paulo", " sp", "entrega", "retirada", "retirar", "motoboy", "sedex", "transportadora", "envio", "prazo", "chega", "zona"],
    "fechamento_compra": ["fechado", "fechou", "vou ficar", "pode separar", "manda pix", "paguei", "pagamento", "comprado", "nota", "nf", "notion", "lançar", "lancar"],
    "produto_tamanho_estoque": ["estoque", "grade", "numeração", "numeracao", "tamanho", "unidade", "par ", "pares", "us ", "br ", "tam"],
}

PII_RE = re.compile(r"\b\d{8,}@(?:s\.whatsapp\.net|g\.us)\b|\b\+?55?\d{10,13}\b", re.I)
URL_RE = re.compile(r"https?://\S+", re.I)
PRICE_RE = re.compile(r"R\$\s*\d+[.,]?\d*|\b\d{3,5}(?:[,.]\d{2})?\b")
SIZE_RE = re.compile(r"\b(?:3[4-9]|4[0-6])\b")


def run_json(cmd: list[str]) -> dict:
    p = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return json.loads(p.stdout, strict=False)


def msg_text(m: dict) -> str:
    vals = [str(m.get(k, "")) for k in ("Text", "DisplayText", "MediaCaption") if m.get(k)]
    text = "\n".join(vals)
    return PII_RE.sub("[redacted]", text)[:5000]


def signal_id(m: dict) -> str:
    raw = f"{m.get('ChatJID','')}|{m.get('MsgID','')}|{m.get('Timestamp','')}"
    return hashlib.sha256(raw.encode()).hexdigest()[:12]


def chat_hash(m: dict) -> str:
    return hashlib.sha256(str(m.get("ChatJID", "")).encode()).hexdigest()[:10]


def classify(m: dict) -> tuple[list[str], list[str]]:
    text = msg_text(m)
    low = text.lower()
    classes = [name for name, kws in CLASSES.items() if any(kw in low for kw in kws)]
    hints = []
    if URL_RE.search(text): hints.append("link")
    if PRICE_RE.search(text): hints.append("preço/número")
    if SIZE_RE.search(text): hints.append("tamanho provável")
    if m.get("MediaType") or m.get("Filename") or m.get("MimeType"): hints.append("mídia")
    return classes, hints


def recommended_next(classes: list[str]) -> str:
    s = set(classes)
    if {"pedido_de_compra", "resposta_fornecedor", "negociacao_preco"} & s and "proximidade_sp_logistica" in s:
        return "rank_cheapest_vs_closer_to_sp"
    if "pedido_de_compra" in s:
        return "await_or_collect_supplier_responses"
    if "negociacao_preco" in s:
        return "compare_price_options"
    if "fechamento_compra" in s:
        return "prepare_notion_logging_preview_after_human_purchase"
    if "produto_tamanho_estoque" in s:
        return "validate_product_size_stock_context"
    return "monitor_or_ignore"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=1000)
    args = ap.parse_args()

    generated_at = datetime.now(timezone.utc).isoformat()
    stats = run_json([WACLI, "--account", ACCOUNT, "--read-only", "store", "stats", "--json"])["data"]
    obj = run_json([WACLI, "--account", ACCOUNT, "--read-only", "messages", "list", "--limit", str(args.limit), "--json"])
    data = obj.get("data") or {}
    messages = data.get("messages") or []

    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE_DIR, 0o700)
    private_raw = PRIVATE_DIR / f"raw_signal_queue_source_{generated_at[:19].replace(':','').replace('-','')}.json"
    private_raw.write_text(json.dumps({"generated_at": generated_at, "messages": messages}, ensure_ascii=False, indent=2))
    os.chmod(private_raw, 0o600)

    counts = Counter()
    queue = []
    chat_counts = Counter()
    for m in messages:
        classes, hints = classify(m)
        for c in classes:
            counts[c] += 1
        ch = chat_hash(m)
        chat_counts[ch] += 1
        if classes:
            queue.append({
                "signal_id": signal_id(m),
                "account": ACCOUNT,
                "source_type": "group" if str(m.get("ChatJID", "")).endswith("@g.us") else "dm_or_unknown",
                "chat_hash": ch,
                "timestamp_utc": m.get("Timestamp"),
                "from_me": bool(m.get("FromMe")),
                "signal_classes": classes,
                "hints": hints,
                "decision_basis_candidates": ["cheapest", "closer_to_sp_small_price_delta"] if ("negociacao_preco" in classes or "proximidade_sp_logistica" in classes) else [],
                "recommended_next_step": recommended_next(classes),
                "approval_required_before": ["send", "contact", "purchase", "notion_write", "external_task", "business_system_write"],
                "sanitized_summary": "Sinal classificado sem nome, telefone, JID ou texto literal.",
            })

    out = {
        "generated_at": generated_at,
        "status": "read_only_sanitized_queue_ready",
        "source_label": "platform_signal_wacli_local",
        "account": ACCOUNT,
        "store_stats": stats,
        "messages_scanned": len(messages),
        "unique_chat_hashes": len(chat_counts),
        "signal_counts": dict(counts),
        "queue_count": len(queue),
        "top_chat_hash_counts": chat_counts.most_common(10),
        "queue_sample": queue[:25],
        "private_raw_path": str(private_raw),
        "non_actions": ["no_whatsapp_send", "no_supplier_contact", "no_customer_contact", "no_purchase", "no_reservation", "no_notion_write", "no_shopify_tiny_merchant_db_write", "no_cron"],
    }
    REPORT_JSON.parent.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    md = [
        "# LK Compras — WhatsApp Signal Queue v1",
        "",
        "Status: `read_only_sanitized_queue_ready`",
        f"Data: {generated_at}",
        "Fonte: `platform_signal_wacli_local` (`lk-compras`).",
        "",
        "## Resumo",
        "",
        f"- Mensagens escaneadas: {len(messages)}.",
        f"- Chats únicos na amostra: {len(chat_counts)}.",
        f"- Sinais classificados: {len(queue)}.",
        f"- Store atual: chats={stats.get('chats')}; groups={stats.get('groups')}; messages={stats.get('messages')}.",
        "",
        "## Contagens por sinal",
        "",
    ]
    for k, v in sorted(counts.items(), key=lambda kv: kv[1], reverse=True):
        md.append(f"- `{k}`: {v}")
    md += [
        "",
        "## Regra de decisão aprendida",
        "",
        "Compra LK não é apenas menor preço: escolher menor preço viável **ou** fonte mais perto de São Paulo quando a diferença não for grande.",
        "Depois da compra humana, lançar no Notion.",
        "",
        "## Não executado",
        "",
        "- Nenhum WhatsApp enviado.",
        "- Nenhum contato com fornecedor/grupo/cliente.",
        "- Nenhuma compra/reserva/pagamento.",
        "- Nenhum write em Notion.",
        "- Nenhum write em Shopify/Tiny/Merchant/banco/Klaviyo/Meta/Google/n8n.",
        "- Nenhum nome, telefone, JID ou texto literal publicado.",
        "",
        "## Próximo seguro",
        "",
        "Transformar esta fila em preview de ranking por produto/tamanho/preço/logística. Qualquer envio, compra ou lançamento Notion exige aprovação explícita atual.",
        "",
    ]
    REPORT_MD.write_text("\n".join(md))
    ROUTINE_MD.parent.mkdir(parents=True, exist_ok=True)
    ROUTINE_MD.write_text("\n".join(md))
    print(json.dumps({k: out[k] for k in ["status", "messages_scanned", "unique_chat_hashes", "signal_counts", "queue_count"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
