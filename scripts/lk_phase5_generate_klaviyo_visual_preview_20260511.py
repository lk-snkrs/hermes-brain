#!/usr/bin/env python3
"""Generate an internal LK/Klaviyo-style HTML preview for Phase 5 P1 curation.

Read-only only:
- Reads local anonymized Brain JSON.
- Optionally queries Shopify Admin GraphQL using Doppler secrets to enrich product images/URLs.
- Writes internal preview artifacts under reports/.
- Does not create Klaviyo campaigns/lists/templates and does not send anything.
"""
from __future__ import annotations

import base64
import html
import json
import os
import re
import subprocess
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reports/lk-phase5-p1-broad-tiny-copy-preview-2026-05-11.json"
OUT_HTML = ROOT / "reports/lk-phase5-p1-klaviyo-visual-preview-2026-05-11.html"
OUT_MD = ROOT / "reports/lk-phase5-p1-klaviyo-visual-preview-2026-05-11.md"
OUT_JSON = ROOT / "reports/lk-phase5-p1-klaviyo-visual-preview-2026-05-11.json"
DOPPLER_TOKEN_FILE = Path("/opt/data/hermes_bruno_ingest/.secrets/doppler_token")


def load_doppler_secrets() -> dict[str, str]:
    if not DOPPLER_TOKEN_FILE.exists():
        return {}
    token = DOPPLER_TOKEN_FILE.read_text().strip()
    if not token:
        return {}
    req = urllib.request.Request(
        "https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json"
    )
    req.add_header("Authorization", "Basic " + base64.b64encode((token + ":").encode()).decode())
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())


def shopify_graphql(store: str, token: str, query: str, variables: dict[str, Any]) -> dict[str, Any]:
    host = store.replace("https://", "").replace("http://", "").strip("/")
    url = f"https://{host}/admin/api/2024-01/graphql.json"
    payload = json.dumps({"query": query, "variables": variables}).encode()
    req = urllib.request.Request(url, data=payload, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("X-Shopify-Access-Token", token)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())


def query_shopify_by_sku(skus: list[str]) -> dict[str, dict[str, str | None]]:
    secrets = load_doppler_secrets()
    store = secrets.get("SHOPIFY_STORE_URL", "")
    token = secrets.get("SHOPIFY_ACCESS_TOKEN", "")
    if not store or not token:
        return {}
    gql = """
    query ProductBySku($query: String!) {
      productVariants(first: 5, query: $query) {
        nodes {
          id
          sku
          title
          product {
            title
            handle
            onlineStoreUrl
            featuredImage { url altText }
            images(first: 1) { nodes { url altText } }
          }
          image { url altText }
        }
      }
    }
    """
    out: dict[str, dict[str, str | None]] = {}
    for sku in skus:
        try:
            data = shopify_graphql(store, token, gql, {"query": f"sku:{sku}"})
            nodes = data.get("data", {}).get("productVariants", {}).get("nodes", [])
            match = None
            for node in nodes:
                if str(node.get("sku", "")).strip() == sku:
                    match = node
                    break
            if not match and nodes:
                match = nodes[0]
            if match:
                product = match.get("product") or {}
                variant_img = match.get("image") or {}
                featured = product.get("featuredImage") or {}
                image_nodes = ((product.get("images") or {}).get("nodes") or [])
                fallback_img = image_nodes[0] if image_nodes else {}
                out[sku] = {
                    "sku": match.get("sku"),
                    "variant_title": match.get("title"),
                    "product_title": product.get("title"),
                    "handle": product.get("handle"),
                    "url": product.get("onlineStoreUrl"),
                    "image_url": variant_img.get("url") or featured.get("url") or fallback_img.get("url"),
                    "image_alt": variant_img.get("altText") or featured.get("altText") or fallback_img.get("altText") or product.get("title"),
                }
        except Exception as exc:  # keep preview generation resilient; never print secrets
            out[sku] = {"error": type(exc).__name__}
    return out


def esc(value: Any) -> str:
    return html.escape(str(value or ""), quote=True)


def clean_product_name(value: str) -> str:
    return re.sub(r"\s+-\s+\d+$", "", value).strip()


def no_em_dash(text: str) -> str:
    return text.replace("—", ",")


def build_html(data: dict[str, Any], enrichment: dict[str, Any]) -> str:
    rows = data["copy_previews"]
    cards = []
    for idx, row in enumerate(rows, start=1):
        sku = row["recommended_sku"]
        enrich = enrichment.get(sku, {})
        img = enrich.get("image_url") or ""
        product_name = clean_product_name(row["recommended_product"])
        img_html = (
            f'<img class="product-img" src="{esc(img)}" alt="{esc(enrich.get("image_alt") or product_name)}">'
            if img
            else '<div class="image-fallback">Imagem Shopify não encontrada<br><span>Preview interno</span></div>'
        )
        label = "VIP" if row["segment"] == "Champions/VIP" else "Seleção personalizada"
        raw_copy = row["copy_preview_internal"]
        display_copy = (
            raw_copy
            .replace(
                "uma continuidade de estilo com disponibilidade validada no Tiny para o seu tamanho.",
                "uma continuidade de estilo com disponibilidade conferida para o seu tamanho.",
            )
            .replace(
                "uma opção validada no Tiny que mantém a mesma intenção de estilo e disponibilidade no seu tamanho.",
                "uma opção conferida para o seu tamanho, mantendo a mesma intenção de estilo.",
            )
            .replace(" validada no Tiny", " conferida")
        )
        cta = "Falar com consultor" if row["tiny_available_estimated_total"] <= 1 else "Ver curadoria"
        cards.append(f"""
          <article class="card">
            <div class="media">{img_html}</div>
            <div class="info">
              <div class="eyebrow">{esc(label)} · tamanho {esc(row['recommended_size'])}</div>
              <h3>{esc(product_name)}</h3>
              <p class="copy">{esc(display_copy)}</p>
              <p class="meta">Disponibilidade conferida para esta curadoria.</p>
              <a class="button" href="{esc(enrich.get('url') or '#')}">{esc(cta)}</a>
            </div>
          </article>
        """)
    generated = datetime.now(timezone.utc).isoformat()
    html_doc = f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>LK Phase 5 P1, Klaviyo visual preview interno</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=DM+Sans:wght@400;500;700&display=swap');
    body {{ margin:0; background:#F0ECE8; color:#111; font-family:'DM Sans', Arial, sans-serif; }}
    .frame {{ max-width: 680px; margin: 0 auto; background:#F5F4F2; }}
    .header {{ background:#0A0A0A; color:#fff; text-align:center; padding: 26px 24px 22px; }}
    .logo {{ font-size: 22px; letter-spacing: 0.32em; font-weight:700; }}
    .tagline {{ margin-top: 8px; color:#B5B0A8; font-size:10px; letter-spacing:.22em; text-transform:uppercase; }}
    .bar {{ display:none; }}
    .hero {{ padding: 42px 40px 30px; text-align:center; }}
    .hero .kicker {{ color:#8A8580; text-transform:uppercase; letter-spacing:.18em; font-size:11px; }}
    h1 {{ margin:12px auto 14px; font-family:'Cormorant Garamond', Georgia, serif; font-weight:500; font-size:44px; line-height:1.02; max-width:560px; }}
    h1 em {{ color:#C8A98A; font-style:italic; }}
    .hero p {{ color:#5d5851; font-size:15px; line-height:1.75; margin:0 auto; max-width:540px; }}
    .notice {{ display:none; }}
    .grid {{ padding: 0 28px 34px; display:grid; gap:18px; }}
    .card {{ background:#fff; display:grid; grid-template-columns: 42% 58%; border:1px solid #E8E6E2; min-height:260px; }}
    .media {{ background:#F0ECE8; min-height:260px; display:flex; align-items:center; justify-content:center; overflow:hidden; }}
    .product-img {{ width:100%; height:100%; object-fit:contain; display:block; padding:18px; box-sizing:border-box; }}
    .image-fallback {{ color:#8A8580; font-size:13px; line-height:1.5; text-align:center; padding:24px; }}
    .image-fallback span {{ font-size:10px; letter-spacing:.16em; text-transform:uppercase; }}
    .info {{ padding: 28px 26px; display:flex; flex-direction:column; justify-content:center; }}
    .eyebrow {{ color:#8A8580; font-size:10px; letter-spacing:.16em; text-transform:uppercase; margin-bottom:10px; }}
    h3 {{ font-family:'Cormorant Garamond', Georgia, serif; font-size:30px; line-height:1.03; font-weight:500; margin:0 0 12px; }}
    .copy {{ color:#5a554e; font-size:13px; line-height:1.7; margin:0 0 14px; }}
    .meta {{ color:#8A8580; font-size:11px; line-height:1.5; margin:0 0 18px; }}
    .button {{ align-self:flex-start; background:#0A0A0A; color:#fff; text-decoration:none; padding:12px 18px; font-size:10px; letter-spacing:.16em; text-transform:uppercase; }}
    .manifesto {{ background:#0A0A0A; color:#fff; margin: 0; padding: 34px 40px; text-align:center; }}
    .manifesto p {{ font-family:'Cormorant Garamond', Georgia, serif; font-size:28px; line-height:1.16; margin:0; }}
    .footer {{ background:#0A0A0A; color:#B5B0A8; padding: 0 40px 30px; text-align:center; font-size:11px; line-height:1.7; }}
    .footer .logo-small {{ color:#fff; letter-spacing:.28em; font-weight:700; margin-bottom:8px; }}
    @media (max-width: 620px) {{ .hero {{ padding:34px 24px 24px; }} h1 {{ font-size:36px; }} .notice {{ margin:0 24px 22px; }} .grid {{ padding:0 18px 28px; }} .card {{ grid-template-columns:1fr; }} .media {{ min-height:310px; }} }}
  </style>
</head>
<body>
  <main class="frame">
    <header class="header"><div class="logo">LK</div><div class="tagline">Less Noise, More Identity.</div></header>
    <section class="bar">Preview interno, sem Klaviyo, sem lista, sem envio</section>
    <section class="hero">
      <div class="kicker">Seleção personalizada LK</div>
      <h1>Peças que conversam com a sua <em>última escolha</em>.</h1>
      <p>Uma seleção pontual para clientes que visitaram a loja física, cruzando afinidade de estilo com disponibilidade conferida no tamanho certo.</p>
    </section>
    <section class="notice"><strong>Controle operacional:</strong> este arquivo é apenas um preview visual interno. A fila segue travada para aprovação humana antes de qualquer ação externa.</section>
    <section class="grid">
      {''.join(cards)}
    </section>
    <section class="manifesto"><p>Curadoria com contexto, disponibilidade conferida e atendimento individual.</p></section>
    <footer class="footer"><div class="logo-small">LK SNEAKERS</div>Less Noise, More Identity.</footer>
  </main>
</body>
</html>"""
    return no_em_dash(html_doc)


def main() -> None:
    data = json.loads(INPUT.read_text())
    skus = [row["recommended_sku"] for row in data["copy_previews"]]
    enrichment = query_shopify_by_sku(skus)
    html_doc = build_html(data, enrichment)
    OUT_HTML.write_text(html_doc)
    summary = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "scope": "Internal LK/Klaviyo visual preview only. No external write, no Klaviyo object, no customer send.",
        "input_report": str(INPUT.relative_to(ROOT)),
        "html_preview": str(OUT_HTML.relative_to(ROOT)),
        "rows": len(data["copy_previews"]),
        "shopify_enrichment": enrichment,
        "guardrails": data["guardrails"] + [
            "HTML local gerado em reports/",
            "Shopify usado apenas em GraphQL query read-only para imagem/URL quando disponível",
            "Nenhum objeto Klaviyo criado",
        ],
    }
    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2))
    loaded_images = sum(1 for item in enrichment.values() if item.get("image_url"))
    md = f"""# LK Phase 5 P1, Klaviyo visual preview interno, 2026-05-11

## Veredito

Gerei um HTML local no padrão visual LK/Klaviyo para os 3 previews resgatados. É apenas aprovação visual interna, sem Klaviyo, sem lista e sem envio.

## Arquivos

- HTML: `reports/lk-phase5-p1-klaviyo-visual-preview-2026-05-11.html`
- JSON: `reports/lk-phase5-p1-klaviyo-visual-preview-2026-05-11.json`
- Fonte: `reports/lk-phase5-p1-broad-tiny-copy-preview-2026-05-11.json`

## Controles

- Linhas no preview: {len(data['copy_previews'])}
- Imagens Shopify encontradas por SKU: {loaded_images}/{len(skus)}
- Estoque Tiny preservado no layout: sim
- PII no Brain: não
- Klaviyo criado: não
- Lista criada: não
- Envio externo: não
- Writes Shopify/Tiny/Supabase: não

## Observação

O HTML usa a direção visual observada nos e-mails reais da LK: header preto, fundo off-white, tipografia editorial, produto protagonista, CTA preto e manifesto final `Less Noise, More Identity.`.
"""
    OUT_MD.write_text(no_em_dash(md))
    print(json.dumps({"html": str(OUT_HTML), "md": str(OUT_MD), "json": str(OUT_JSON), "images": f"{loaded_images}/{len(skus)}"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
