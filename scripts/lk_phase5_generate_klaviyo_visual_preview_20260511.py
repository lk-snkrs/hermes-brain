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
import re
import urllib.request
from collections import OrderedDict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reports/lk-phase5-p1-broad-tiny-copy-preview-2026-05-11.json"
OUT_HTML = ROOT / "reports/lk-phase5-p1-klaviyo-visual-preview-2026-05-11.html"
OUT_MD = ROOT / "reports/lk-phase5-p1-klaviyo-visual-preview-2026-05-11.md"
OUT_JSON = ROOT / "reports/lk-phase5-p1-klaviyo-visual-preview-2026-05-11.json"
DOPPLER_TOKEN_FILE = Path("/opt/data/hermes_bruno_ingest/.secrets/doppler_token")
LOGO_WHITE = "https://lksneakers.com.br/cdn/shop/files/LOGO-LK-BRANCO_885e01ed-68da-4988-b5a2-4ff4a10e238b.png?v=1763660281"


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
        except Exception as exc:
            out[sku] = {"error": type(exc).__name__}
    return out


def esc(value: Any) -> str:
    return html.escape(str(value or ""), quote=True)


def clean_product_name(value: str) -> str:
    return re.sub(r"\s+-\s+\d+$", "", value).strip()


def no_em_dash(text: str) -> str:
    return text.replace("—", ",")


def sizes_label(rows: list[dict[str, Any]]) -> str:
    sizes = []
    for row in rows:
        size = str(row.get("recommended_size") or "").strip()
        if size and size not in sizes:
            sizes.append(size)
    if not sizes:
        return "tamanho conferido"
    if len(sizes) == 1:
        return f"tamanho {sizes[0]}"
    return "tamanhos " + " e ".join([", ".join(sizes[:-1]), sizes[-1]]).strip(", ")


def customer_copy_for_group(product_name: str, rows: list[dict[str, Any]]) -> str:
    if len(rows) > 1:
        origins = []
        for row in rows:
            origin = clean_product_name(row.get("purchase_product", ""))
            if origin and origin not in origins:
                origins.append(origin)
        if len(origins) == 1:
            return (
                f"A partir da sua escolha por {origins[0]}, reunimos {product_name}: "
                f"uma continuidade de estilo com disponibilidade conferida nos {sizes_label(rows)}."
            )
        return (
            f"A partir das últimas escolhas feitas na LK, reunimos {product_name}: "
            f"uma continuidade de estilo com disponibilidade conferida nos {sizes_label(rows)}."
        )
    row = rows[0]
    raw = str(row.get("copy_preview_internal") or "")
    return (
        raw.replace(
            "uma continuidade de estilo com disponibilidade validada no Tiny para o seu tamanho.",
            "uma continuidade de estilo com disponibilidade conferida para o seu tamanho.",
        )
        .replace(
            "uma opção validada no Tiny que mantém a mesma intenção de estilo e disponibilidade no seu tamanho.",
            "uma opção conferida para o seu tamanho, mantendo a mesma intenção de estilo.",
        )
        .replace(" validada no Tiny", " conferida")
    )


def grouped_rows(rows: list[dict[str, Any]]) -> list[tuple[str, list[dict[str, Any]]]]:
    groups: "OrderedDict[str, list[dict[str, Any]]]" = OrderedDict()
    for row in rows:
        product_name = clean_product_name(str(row.get("recommended_product") or ""))
        groups.setdefault(product_name, []).append(row)
    return list(groups.items())


def build_html(data: dict[str, Any], enrichment: dict[str, Any]) -> str:
    rows = data["copy_previews"]
    cards = []
    for product_name, product_rows in grouped_rows(rows):
        row = product_rows[0]
        sku = row["recommended_sku"]
        enrich = enrichment.get(sku, {})
        img = enrich.get("image_url") or ""
        img_html = (
            f'<img class="product-img" src="{esc(img)}" alt="{esc(enrich.get("image_alt") or product_name)}">'
            if img
            else '<div class="image-fallback">Imagem Shopify não encontrada<br><span>Preview interno</span></div>'
        )
        label = "VIP" if any(r.get("segment") == "Champions/VIP" for r in product_rows) else "Seleção personalizada"
        display_copy = customer_copy_for_group(product_name, product_rows)
        cta = "Falar com consultor" if any(float(r.get("tiny_available_estimated_total") or 0) <= 1 for r in product_rows) else "Ver curadoria"
        cards.append(f"""
          <article class="card">
            <div class="media">{img_html}</div>
            <div class="info">
              <div class="eyebrow">{esc(label)} · {esc(sizes_label(product_rows))}</div>
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
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,500;1,300;1,500&family=DM+Sans:wght@300;400;500;700&display=swap');
    * {{ box-sizing:border-box; }}
    body {{ margin:0; background:#E8E6E2; color:#0A0A0A; font-family:'DM Sans', Arial, sans-serif; }}
    .frame {{ max-width: 640px; margin: 0 auto; background:#FFFFFF; }}
    .header {{ background:#0A0A0A; text-align:center; padding:26px 44px; }}
    .header img {{ display:inline-block; width:48px; height:auto; }}
    .topline {{ background:#F5F4F2; padding:12px 44px; text-align:center; border-bottom:1px solid #E8E6E2; }}
    .topline span {{ font-size:9px; letter-spacing:3px; text-transform:uppercase; color:#8A8580; }}
    .hero {{ background:#F5F4F2; padding:56px 44px 42px; text-align:center; border-bottom:1px solid #E8E6E2; }}
    .hero .kicker {{ font-size:8px; letter-spacing:5px; text-transform:uppercase; color:#B5B0A8; margin-bottom:14px; }}
    .rule {{ width:24px; height:1px; background:#E0DDD8; margin:0 auto 22px; }}
    h1 {{ margin:0; font-family:'Cormorant Garamond', Georgia, serif; font-weight:300; font-size:56px; line-height:.96; letter-spacing:-1.8px; }}
    h1 em {{ color:#8A8580; font-style:italic; }}
    .hero .rule.after {{ margin:24px auto 22px; }}
    .hero p {{ color:#8A8580; font-size:13px; line-height:2.0; margin:0 auto; max-width:390px; letter-spacing:.2px; }}
    .grid {{ background:#FFFFFF; display:grid; gap:0; }}
    .card {{ display:grid; grid-template-columns:48% 52%; border-bottom:1px solid #E8E6E2; min-height:292px; }}
    .media {{ background:#FFFFFF; min-height:292px; display:flex; align-items:center; justify-content:center; overflow:hidden; line-height:0; }}
    .product-img {{ width:100%; height:100%; object-fit:contain; display:block; padding:24px; }}
    .image-fallback {{ color:#8A8580; font-size:13px; line-height:1.5; text-align:center; padding:24px; }}
    .image-fallback span {{ font-size:10px; letter-spacing:.16em; text-transform:uppercase; }}
    .info {{ background:#EEE8E0; padding:34px 32px; display:flex; flex-direction:column; justify-content:center; border-left:1px solid #E8E6E2; }}
    .eyebrow {{ color:#B5B0A8; font-size:7.5px; letter-spacing:3px; text-transform:uppercase; margin-bottom:10px; }}
    h3 {{ font-family:'Cormorant Garamond', Georgia, serif; font-size:30px; line-height:1.05; font-weight:300; margin:0 0 14px; }}
    .copy {{ color:#6B655E; font-size:12.5px; line-height:1.85; margin:0 0 15px; }}
    .meta {{ color:#8A8580; font-size:10px; line-height:1.5; margin:0 0 18px; }}
    .button {{ align-self:flex-start; background:#0A0A0A; color:#FFFFFF; text-decoration:none; padding:14px 20px; font-size:9px; letter-spacing:2.5px; text-transform:uppercase; }}
    .manifesto {{ background:#0A0A0A; color:#FFFFFF; margin:0; padding:40px 44px; text-align:center; }}
    .manifesto p {{ font-family:'Cormorant Garamond', Georgia, serif; font-weight:300; font-style:italic; font-size:24px; line-height:1.45; margin:0 0 18px; }}
    .manifesto .sig {{ font-size:9px; letter-spacing:2.5px; text-transform:uppercase; color:#8A8580; }}
    .footer {{ background:#0A0A0A; padding:40px 44px; text-align:center; color:#8A8580; }}
    .footer-logo {{ display:inline-block; margin-bottom:20px; width:48px; height:auto; }}
    .footer-slogan {{ font-family:'Cormorant Garamond', Georgia, serif; font-weight:300; font-style:italic; font-size:13px; color:#B5B0A8; letter-spacing:1.2px; line-height:1.45; margin-bottom:24px; }}
    .footer-rule {{ width:28px; height:1px; background:rgba(255,255,255,.1); margin:0 auto 20px; }}
    .address {{ font-size:11px; font-weight:300; line-height:1.9; color:#8A8580; }}
    .links {{ margin-top:16px; }}
    .links a {{ font-size:9px; letter-spacing:2.5px; text-transform:uppercase; color:#B5B0A8; text-decoration:none; margin:0 10px; }}
    .unsubscribe {{ margin-top:20px; padding-top:18px; border-top:1px solid rgba(255,255,255,.06); }}
    .unsubscribe a {{ font-size:9px; letter-spacing:2px; text-transform:uppercase; color:#8A8580; text-decoration:none; }}
    @media (max-width:620px) {{
      .hero {{ padding:44px 28px 34px; }} h1 {{ font-size:42px; }}
      .card {{ grid-template-columns:1fr; }} .media {{ min-height:320px; }} .info {{ border-left:0; border-top:1px solid #E8E6E2; }}
    }}
  </style>
</head>
<body>
  <main class="frame">
    <header class="header"><img alt="LK Sneakers" src="{esc(LOGO_WHITE)}"></header>
    <section class="topline"><span>SELEÇÃO PERSONALIZADA LK · CURADORIA PÓS-COMPRA</span></section>
    <section class="hero">
      <div class="kicker">ESCOLHAS PENSADAS PARA CONTINUAR O SEU ESTILO</div>
      <div class="rule"></div>
      <h1>Peças que conversam<br><em>com a sua última escolha.</em></h1>
      <div class="rule after"></div>
      <p>Uma seleção pontual para clientes que visitaram a loja física, cruzando afinidade de estilo com disponibilidade conferida no tamanho certo.</p>
    </section>
    <section class="grid">
      {''.join(cards)}
    </section>
    <section class="manifesto"><p>"Curadoria com contexto, disponibilidade conferida e atendimento individual."</p><div class="sig">LK Sneakers</div></section>
    <footer class="footer">
      <img class="footer-logo" alt="LK Sneakers" src="{esc(LOGO_WHITE)}">
      <div class="footer-slogan">O que é raro,<br>merece ser encontrado</div>
      <div class="footer-rule"></div>
      <div class="address">LK Sneakers · Rua Melo Alves, 344 · Jardins, São Paulo</div>
      <div class="links">
        <a href="https://instagram.com/lk.sneakers">Instagram</a>
        <a href="https://tiktok.com/@lk.sneakers_">TikTok</a>
        <a href="https://wa.me/5511999661409">WhatsApp</a>
      </div>
      <div class="unsubscribe"><a href="#">Cancelar inscrição</a></div>
    </footer>
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
    loaded_images = sum(1 for item in enrichment.values() if item.get("image_url"))
    unique_cards = len(grouped_rows(data["copy_previews"]))
    summary = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "scope": "Internal LK/Klaviyo visual preview only. No external write, no Klaviyo object, no customer send.",
        "input_report": str(INPUT.relative_to(ROOT)),
        "html_preview": str(OUT_HTML.relative_to(ROOT)),
        "source_rows": len(data["copy_previews"]),
        "visual_cards": unique_cards,
        "deduped_visual_products": True,
        "shopify_images_loaded": loaded_images,
        "shopify_enrichment": enrichment,
        "klaviyo_reference": {
            "campaign": "Adidas Ballerina Bad Bunny Flamboyan, LK Sneakers",
            "campaign_id": "01KRBW5EKCSPE8MHTVQYF88QAT",
            "template_id": "V2UsSq",
            "observed_read_only": True,
        },
        "guardrails": data["guardrails"] + [
            "HTML local gerado em reports/",
            "Shopify usado apenas em GraphQL query read-only para imagem/URL quando disponível",
            "Klaviyo usado apenas em leitura para referência visual da última campanha enviada",
            "Nenhum objeto Klaviyo criado",
        ],
    }
    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2))
    md = f"""# LK Phase 5 P1, Klaviyo visual preview interno, 2026-05-11

## Veredito

Corrigi o HTML local no padrão real da última news enviada no Klaviyo. É apenas aprovação visual interna, sem Klaviyo, sem lista e sem envio.

## Ajustes aplicados

- Logo branco real da LK no header.
- Linha de chamada abaixo do header, no padrão da última campanha enviada.
- Imagem em bloco branco e texto em bloco off-white.
- Produtos duplicados visualmente agrupados: 3 linhas operacionais viraram {unique_cards} cards visuais.
- Footer aproximado ao Klaviyo real, com logo, endereço, links e unsubscribe.
- Slogan atualizado só no footer: `O que é raro, merece ser encontrado`.

## Arquivos

- HTML: `reports/lk-phase5-p1-klaviyo-visual-preview-2026-05-11.html`
- JSON: `reports/lk-phase5-p1-klaviyo-visual-preview-2026-05-11.json`
- Fonte: `reports/lk-phase5-p1-broad-tiny-copy-preview-2026-05-11.json`

## Controles

- Linhas operacionais no preview: {len(data['copy_previews'])}
- Cards visuais: {unique_cards}
- Imagens Shopify encontradas por SKU: {loaded_images}/{len(skus)}
- PII no Brain: não
- Klaviyo criado: não
- Lista criada: não
- Envio externo: não
- Writes Shopify/Tiny/Supabase: não

## Referência consultada

Última campanha enviada no Klaviyo, lida em modo read-only: `Adidas Ballerina Bad Bunny Flamboyan, LK Sneakers`, template `V2UsSq`.
"""
    OUT_MD.write_text(no_em_dash(md))
    print(json.dumps({"html": str(OUT_HTML), "md": str(OUT_MD), "json": str(OUT_JSON), "images": f"{loaded_images}/{len(skus)}", "cards": unique_cards}, ensure_ascii=False))


if __name__ == "__main__":
    main()
