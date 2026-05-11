#!/usr/bin/env python3
"""LK Phase 5 P1: private recipient IDs + Tiny stock guard.

Read-only:
- Pulls LK Supabase orders/items/customers/customer_rfm.
- Rebuilds P1 customer-anchor candidate rows from the existing best-seller preview.
- Writes a private, non-committed recipient file outside the repo with IDs only/no raw PII.
- Checks Tiny stock for top anchor sizes via produto.obter.estoque.
- Writes public aggregate/anonymized JSON+MD reports under reports/.

No sends. No writes to Supabase/Shopify/Tiny/Klaviyo/WhatsApp.
"""
from __future__ import annotations

import base64
import collections
import hashlib
import json
import pathlib
import re
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
PREVIEW = ROOT / "reports/lk-phase5-p1-best-seller-campaign-preview-2026-05-11.json"
OUT_JSON = ROOT / "reports/lk-phase5-p1-recipients-stock-guard-2026-05-11.json"
OUT_MD = ROOT / "reports/lk-phase5-p1-recipients-stock-guard-2026-05-11.md"
PRIVATE_DIR = pathlib.Path("/opt/data/hermes_bruno_ingest/private_exports/lk_crm")
PRIVATE_OUT = PRIVATE_DIR / "lk_phase5_p1_recipient_ids_2026-05-11.json"
DOPPLER_TOKEN_FILE = pathlib.Path("/opt/data/hermes_bruno_ingest/.secrets/doppler_token")
VALID_FINANCIAL = {"paid", "partially_paid"}
TINY_DELAY_SECONDS = 1.35


def load_secrets() -> dict[str, str]:
    token = DOPPLER_TOKEN_FILE.read_text().strip()
    req = urllib.request.Request(
        "https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json"
    )
    req.add_header("Authorization", "Basic " + base64.b64encode((token + ":").encode()).decode())
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)


def supabase_fetch(url: str, key: str, table: str, select: str) -> list[dict[str, Any]]:
    headers = {"apikey": key, "Authorization": "Bearer " + key}
    out: list[dict[str, Any]] = []
    offset = 0
    while True:
        qs = urllib.parse.urlencode({"select": select, "limit": "1000", "offset": str(offset)})
        req = urllib.request.Request(f"{url.rstrip('/')}/rest/v1/{table}?{qs}", headers=headers)
        with urllib.request.urlopen(req, timeout=90) as resp:
            rows = json.load(resp)
        out.extend(rows)
        if len(rows) < 1000:
            return out
        offset += 1000


def tiny_call(token: str, method: str, params: dict[str, Any]) -> dict[str, Any]:
    time.sleep(TINY_DELAY_SECONDS)
    data = urllib.parse.urlencode({**params, "token": token, "formato": "json"}).encode()
    req = urllib.request.Request(f"https://api.tiny.com.br/api2/{method}.php", data=data, method="POST")
    with urllib.request.urlopen(req, timeout=90) as resp:
        return json.load(resp)


def customer_ref(email: str) -> str:
    return hashlib.sha256(email.lower().strip().encode()).hexdigest()[:12]


def size_from_variant_title(text: Any) -> str:
    s = str(text or "").strip().replace(",", ".")
    m = re.search(r"(\d{2}(?:\.5)?)", s)
    return m.group(1) if m else s


def size_from_tiny_variant(v: dict[str, Any]) -> str:
    grade = v.get("grade")
    if isinstance(grade, dict) and grade:
        return " ".join(str(x) for x in grade.values())
    nm = v.get("nome") or ""
    if isinstance(nm, dict):
        return " ".join(str(x) for x in nm.values())
    text = str(nm)
    if " - " in text:
        return text.split(" - ")[-1]
    return size_from_variant_title(text)


def norm_size(text: Any) -> str:
    return str(text or "").strip().replace(",", ".").lower()


def segment_from_rfm(r: dict[str, Any] | None) -> str | None:
    if not r:
        return None
    r_score = int(r.get("r_score") or 0)
    freq = int(r.get("frequency_orders") or 0)
    m_score = int(r.get("m_score") or 0)
    if r_score >= 4 and freq == 1 and m_score >= 4:
        return "Novo alto potencial"
    if r_score >= 4 and freq >= 2 and m_score >= 4:
        return "Champions/VIP"
    return None


def stock_for_product_id(tiny_token: str, product_id: str) -> dict[str, Any]:
    ret = tiny_call(tiny_token, "produto.obter.estoque", {"id": str(product_id)}).get("retorno", {})
    p = ret.get("produto") or {}
    saldo = float(p.get("saldo") or 0)
    reservado = float(p.get("saldoReservado") or 0)
    return {
        "status": ret.get("status"),
        "tiny_id": str(p.get("id") or product_id),
        "nome": p.get("nome"),
        "codigo": p.get("codigo"),
        "situacao": p.get("situacao"),
        "saldo": saldo,
        "saldo_reservado": reservado,
        "saldo_disponivel_estimado": max(saldo - reservado, 0),
        "depositos": [
            {
                "nome": (d.get("deposito") or {}).get("nome"),
                "desconsiderar": (d.get("deposito") or {}).get("desconsiderar"),
                "saldo": (d.get("deposito") or {}).get("saldo"),
            }
            for d in (p.get("depositos") or [])
        ],
    }


def find_tiny_variant_stock(tiny_token: str, sku: str, title: str, size: str) -> dict[str, Any]:
    # First try exact/common SKU search. For some Tiny parents, the returned product has variations.
    queries = [sku, title, " ".join(title.split()[:5])]
    seen_products: set[str] = set()
    candidates: list[dict[str, Any]] = []
    searches: list[dict[str, Any]] = []
    for q in [x for i, x in enumerate(queries) if x and x not in queries[:i]]:
        ret = tiny_call(tiny_token, "produtos.pesquisa", {"pesquisa": q}).get("retorno", {})
        found = []
        for item in ret.get("produtos") or []:
            p = item.get("produto") or {}
            rec = {k: p.get(k) for k in ["id", "nome", "codigo", "situacao", "preco"]}
            found.append(rec)
            pid = str(p.get("id") or "")
            if pid and pid not in seen_products:
                seen_products.add(pid)
                candidates.append(rec)
        searches.append({"query_kind": "sku" if q == sku else "title", "status": ret.get("status"), "count": len(found)})
        if candidates and q == sku:
            break

    target_norm = norm_size(size)
    matches: list[dict[str, Any]] = []
    for c in candidates[:8]:
        pid = str(c.get("id") or "")
        if not pid:
            continue
        prod_ret = tiny_call(tiny_token, "produto.obter", {"id": pid}).get("retorno", {})
        prod = prod_ret.get("produto") or {}
        variants = prod.get("variacoes") or []
        if variants:
            for wrap in variants:
                v = wrap.get("variacao") or {}
                vsize = size_from_tiny_variant(v)
                code = str(v.get("codigo") or prod.get("codigo") or "")
                if norm_size(vsize) == target_norm or (sku and code == sku):
                    vid = str(v.get("id") or "")
                    if vid:
                        st = stock_for_product_id(tiny_token, vid)
                        matches.append({"match_source": "parent_variation", "requested_sku": sku, "requested_size": size, "tiny_size": vsize, **st})
        else:
            vsize = size_from_tiny_variant(prod)
            code = str(prod.get("codigo") or "")
            if norm_size(vsize) == target_norm or (sku and code == sku):
                st = stock_for_product_id(tiny_token, pid)
                matches.append({"match_source": "direct_product", "requested_sku": sku, "requested_size": size, "tiny_size": vsize, **st})
    # Deduplicate by Tiny ID.
    dedup: dict[str, dict[str, Any]] = {}
    for m in matches:
        dedup[str(m.get("tiny_id"))] = m
    matches = list(dedup.values())
    available = sum(float(m.get("saldo_disponivel_estimado") or 0) for m in matches if (m.get("situacao") in [None, "A", "Ativo", "ativo"]))
    return {
        "sku": sku,
        "size": size,
        "searches": searches,
        "match_count": len(matches),
        "available_estimated_total": available,
        "status": "available" if available > 0 else ("zero_stock" if matches else "not_mapped"),
        "matches": matches,
    }


def main() -> None:
    secrets = load_secrets()
    supa_url = secrets["SUPABASE_LK_URL"].rstrip("/")
    supa_key = secrets["SUPABASE_LK_SERVICE_KEY"]
    tiny_token = secrets["TINY_API_TOKEN"]

    preview = json.loads(PREVIEW.read_text())
    selected_queues = preview["selected_p1_queues"]
    anchor_titles = sorted({q["anchor_product"] for q in selected_queues})
    selected_pairs = {(q["segment"], q["anchor_product"]): q for q in selected_queues}

    orders = supabase_fetch(supa_url, supa_key, "orders", "id,customer_id,email,financial_status,cancelled_at,order_created_at,total_price")
    items = supabase_fetch(supa_url, supa_key, "order_items", "order_id,title,variant_title,sku,quantity,line_total,unit_price")
    customers = supabase_fetch(supa_url, supa_key, "customers", "id,email,source_customer_id,accepts_marketing,phone,orders_count,total_spent,tamanho_principal")
    rfm_rows = supabase_fetch(supa_url, supa_key, "customer_rfm", "customer_id,r_score,f_score,m_score,frequency_orders,monetary_value,recency_days,last_order_at")

    valid_orders = {
        str(o["id"]): o
        for o in orders
        if o.get("email") and not o.get("cancelled_at") and o.get("financial_status") in VALID_FINANCIAL
    }
    customers_by_email = {(c.get("email") or "").lower().strip(): c for c in customers if c.get("email")}
    rfm_by_customer_id = {str(r.get("customer_id")): r for r in rfm_rows}
    items_by_order: dict[str, list[dict[str, Any]]] = collections.defaultdict(list)
    for it in items:
        items_by_order[str(it.get("order_id"))].append(it)

    # SKU by anchor/size from paid history.
    sku_by_anchor_size: dict[str, dict[str, collections.Counter[str]]] = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
    for it in items:
        o = valid_orders.get(str(it.get("order_id")))
        if not o or it.get("title") not in anchor_titles:
            continue
        size = size_from_variant_title(it.get("variant_title"))
        sku_by_anchor_size[it["title"]][size][it.get("sku") or ""] += int(float(it.get("quantity") or 0))

    # Candidate rows are customer-anchor pairs matching current P1 segment logic. Dedup by ref/segment/anchor.
    dedup: dict[tuple[str, str, str], dict[str, Any]] = {}
    for oid, o in valid_orders.items():
        email = (o.get("email") or "").lower().strip()
        c = customers_by_email.get(email, {})
        cid = str(o.get("customer_id") or c.get("id") or "")
        rfm = rfm_by_customer_id.get(cid)
        seg = segment_from_rfm(rfm)
        if not seg:
            continue
        ref = customer_ref(email)
        for it in items_by_order.get(oid, []):
            title = it.get("title")
            if (seg, title) not in selected_pairs:
                continue
            key = (ref, seg, title)
            order_dt = str(o.get("order_created_at") or "")
            current = dedup.get(key)
            if not current or order_dt > current.get("last_anchor_order_at", ""):
                dedup[key] = {
                    "customer_ref": ref,
                    "customer_id": cid or None,
                    "source_customer_id": c.get("source_customer_id"),
                    "segment": seg,
                    "anchor_product": title,
                    "anchor_size": size_from_variant_title(it.get("variant_title")),
                    "anchor_sku": it.get("sku"),
                    "last_anchor_order_at": order_dt,
                    "rfm": {
                        "r_score": rfm.get("r_score") if rfm else None,
                        "f_score": rfm.get("f_score") if rfm else None,
                        "m_score": rfm.get("m_score") if rfm else None,
                        "frequency_orders": rfm.get("frequency_orders") if rfm else None,
                        "monetary_value": rfm.get("monetary_value") if rfm else None,
                        "recency_days": rfm.get("recency_days") if rfm else None,
                    },
                    "contact_flags": {
                        "has_email": bool(email),
                        "has_phone": bool(c.get("phone")),
                        "accepts_marketing": c.get("accepts_marketing"),
                    },
                }

    candidate_rows = list(dedup.values())
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    private_payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "scope": "Private LK P1 CRM recipient IDs only; no raw names/emails/phones; do not commit; no send/list creation.",
        "candidate_rows": sorted(candidate_rows, key=lambda r: (r["segment"], r["anchor_product"], r["customer_ref"])),
    }
    PRIVATE_OUT.write_text(json.dumps(private_payload, ensure_ascii=False, indent=2) + "\n")
    PRIVATE_OUT.chmod(0o600)

    group_counts: dict[str, dict[str, Any]] = {}
    size_demand_by_group: dict[str, collections.Counter[str]] = collections.defaultdict(collections.Counter)
    channel_flags_by_group: dict[str, collections.Counter[str]] = collections.defaultdict(collections.Counter)
    for r in candidate_rows:
        g = f"{r['segment']} | {r['anchor_product']}"
        size_demand_by_group[g][str(r.get("anchor_size") or "unknown")] += 1
        flags = r.get("contact_flags") or {}
        if flags.get("has_email"):
            channel_flags_by_group[g]["has_email"] += 1
        if flags.get("has_phone"):
            channel_flags_by_group[g]["has_phone"] += 1
        if flags.get("accepts_marketing") is True:
            channel_flags_by_group[g]["accepts_marketing_true"] += 1
        elif flags.get("accepts_marketing") is False:
            channel_flags_by_group[g]["accepts_marketing_false"] += 1
        else:
            channel_flags_by_group[g]["accepts_marketing_unknown"] += 1

    for q in selected_queues:
        g = f"{q['segment']} | {q['anchor_product']}"
        refs = sorted({r["customer_ref"] for r in candidate_rows if r["segment"] == q["segment"] and r["anchor_product"] == q["anchor_product"]})
        group_counts[g] = {
            "priority": "P1",
            "segment": q["segment"],
            "anchor_product": q["anchor_product"],
            "previous_preview_count": q.get("customers_in_queue"),
            "live_candidate_count": len(refs),
            "dedup_customer_refs_sample": refs[:5],
            "size_demand_top": size_demand_by_group[g].most_common(8),
            "contact_flags": dict(channel_flags_by_group[g]),
        }

    # Tiny stock guard: top historical sizes per anchor from preview, plus live candidate demanded sizes.
    stock_by_anchor: dict[str, Any] = {}
    stock_cache: dict[tuple[str, str, str], dict[str, Any]] = {}
    for title in anchor_titles:
        wanted_sizes = set()
        for q in selected_queues:
            if q["anchor_product"] == title:
                for tv in q.get("top_variants") or []:
                    wanted_sizes.add(size_from_variant_title(tv))
        for r in candidate_rows:
            if r["anchor_product"] == title and r.get("anchor_size"):
                wanted_sizes.add(str(r["anchor_size"]))
        variant_checks = []
        for size in sorted(wanted_sizes, key=lambda x: (float(x) if re.match(r"^\d+(\.\d+)?$", x) else 999, x)):
            sku_counter = sku_by_anchor_size[title].get(size) or collections.Counter()
            sku = sku_counter.most_common(1)[0][0] if sku_counter else ""
            ck = (title, size, sku)
            if ck not in stock_cache:
                stock_cache[ck] = find_tiny_variant_stock(tiny_token, sku, title, size)
            variant_checks.append(stock_cache[ck])
        stock_by_anchor[title] = {
            "checked_sizes": len(variant_checks),
            "available_sizes": [v for v in variant_checks if v["status"] == "available"],
            "zero_or_unmapped_sizes": [v for v in variant_checks if v["status"] != "available"],
            "variant_checks": variant_checks,
        }

    # Readiness per queue: how many candidate rows have their actual purchased size available in Tiny.
    readiness_by_group: dict[str, Any] = {}
    stock_lookup = {(title, v["size"]): v for title, block in stock_by_anchor.items() for v in block["variant_checks"]}
    for q in selected_queues:
        g = f"{q['segment']} | {q['anchor_product']}"
        rows = [r for r in candidate_rows if r["segment"] == q["segment"] and r["anchor_product"] == q["anchor_product"]]
        ready = []
        blocked = []
        for r in rows:
            st = stock_lookup.get((r["anchor_product"], str(r.get("anchor_size") or "")))
            rec = {"customer_ref": r["customer_ref"], "size": r.get("anchor_size"), "stock_status": st.get("status") if st else "not_checked"}
            if st and st.get("status") == "available":
                ready.append(rec)
            else:
                blocked.append(rec)
        readiness_by_group[g] = {
            "live_candidate_count": len(rows),
            "ready_with_same_size_stock": len(ready),
            "blocked_by_stock_or_mapping": len(blocked),
            "ready_refs_sample": ready[:5],
            "blocked_refs_sample": blocked[:5],
            "campaign_gate": "can_preview_recipients_for_approval" if ready else "hold_until_stock_or_alternative_anchor",
        }

    public_report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "scope": "LK Phase 5 P1 recipient structure + Tiny stock guard; read-only; public/anonymized.",
        "guardrails": [
            "No customer-facing send",
            "No Klaviyo/WhatsApp/list creation",
            "No Supabase/Shopify/Tiny writes",
            "No raw customer email/name/phone in repo report or Telegram",
            f"Private ID-only file written outside repo: {PRIVATE_OUT}",
        ],
        "source_counts": {
            "valid_orders_with_email": len(valid_orders),
            "order_items": len(items),
            "customers_table_rows": len(customers),
            "rfm_rows": len(rfm_rows),
            "p1_candidate_customer_anchor_rows": len(candidate_rows),
            "p1_unique_customer_refs": len({r["customer_ref"] for r in candidate_rows}),
        },
        "queue_counts": group_counts,
        "tiny_stock_by_anchor": stock_by_anchor,
        "readiness_by_group": readiness_by_group,
        "next_step_requires_approval": "Use only ready_with_same_size_stock recipients to build final Klaviyo/WhatsApp preview; do not create/send until Lucas approves the exact list/copy/channel.",
    }
    OUT_JSON.write_text(json.dumps(public_report, ensure_ascii=False, indent=2) + "\n")

    lines = [
        "# LK OS Fase 5, P1 recipients + Tiny stock guard, 2026-05-11",
        "",
        "## Escopo",
        "",
        "Estruturei a passagem do preview P1 para uma lista operacional segura. Não houve envio, criação de lista, tag, campanha ou escrita externa.",
        "",
        "## Fontes e guardrails",
        "",
        f"- Pedidos válidos com e-mail: {len(valid_orders)}",
        f"- Itens analisados: {len(items)}",
        f"- Linhas cliente-âncora P1 candidatas: {len(candidate_rows)}",
        f"- Clientes únicos P1: {len({r['customer_ref'] for r in candidate_rows})}",
        "- Tiny consultado em modo read-only: `produtos.pesquisa`, `produto.obter`, `produto.obter.estoque`.",
        "- Arquivo privado com IDs: fora do repo e chmod 600; sem raw email/nome/telefone no relatório versionado.",
        "",
        "## Fila P1 por grupo",
        "",
    ]
    for g, rec in group_counts.items():
        ready = readiness_by_group[g]
        lines += [
            f"### {g}",
            f"- Preview anterior: {rec['previous_preview_count']} clientes",
            f"- Pool vivo recalculado: {rec['live_candidate_count']} cliente-âncora",
            f"- Prontos com estoque no mesmo tamanho: {ready['ready_with_same_size_stock']}",
            f"- Bloqueados por estoque/mapeamento: {ready['blocked_by_stock_or_mapping']}",
            f"- Top tamanhos demandados: {', '.join(f'{s} ({c})' for s, c in rec['size_demand_top'][:5]) or 'n/d'}",
            f"- Gate: {ready['campaign_gate']}",
            "",
        ]
    lines += [
        "## Estoque Tiny, resumo por anchor",
        "",
    ]
    for title, block in stock_by_anchor.items():
        avail = block["available_sizes"]
        z = block["zero_or_unmapped_sizes"]
        lines += [
            f"### {title}",
            f"- Tamanhos checados: {block['checked_sizes']}",
            f"- Tamanhos com saldo disponível estimado: {len(avail)}",
            f"- Tamanhos sem saldo/mapeamento: {len(z)}",
            f"- Disponíveis: {', '.join(f'{v['size']} (disp. {v['available_estimated_total']:.0f})' for v in avail[:12]) or 'nenhum'}",
            "",
        ]
    lines += [
        "## Próximo passo",
        "",
        "Montar o preview final por canal usando somente clientes/tamanhos com `ready_with_same_size_stock`. Qualquer Klaviyo/WhatsApp/lista real continua bloqueado até aprovação explícita do Lucas.",
        "",
        "## Guardrails cumpridos",
        "",
        "- Sem PII no Brain.",
        "- Sem envio externo.",
        "- Sem escrita em Supabase/Shopify/Tiny/Klaviyo/WhatsApp.",
    ]
    OUT_MD.write_text("\n".join(lines) + "\n")

    print(json.dumps({
        "public_json": str(OUT_JSON),
        "public_md": str(OUT_MD),
        "private_ids_file": str(PRIVATE_OUT),
        "source_counts": public_report["source_counts"],
        "ready_by_group": {k: {"ready": v["ready_with_same_size_stock"], "blocked": v["blocked_by_stock_or_mapping"]} for k, v in readiness_by_group.items()},
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
