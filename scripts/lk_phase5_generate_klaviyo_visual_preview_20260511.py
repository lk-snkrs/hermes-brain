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
        return (
            "Um modelo de leitura neutra e rara, selecionado para continuar suas últimas escolhas na LK, "
            f"com disponibilidade conferida nos {sizes_label(rows)}."
        )
    return (
        "Selecionado a partir da sua compra presencial, mantém a mesma intenção de estilo "
        "com disponibilidade conferida para o seu tamanho."
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
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Inter:wght@300;400;500&display=swap');
    * {{ box-sizing:border-box; }}
    body {{ margin:0; background:#FFFFFF; color:#111111; font-family:Inter, Arial, Helvetica, sans-serif; }}
    .frame {{ max-width:600px; margin:0 auto; background:#FFFFFF; }}
    .header {{ background:#050505; height:150px; display:flex; align-items:center; justify-content:center; text-align:center; }}
    .header img {{ display:block; width:78px; height:auto; }}
    .topline {{ background:#FFFFFF; padding:27px 20px 20px; text-align:center; border-bottom:1px solid #EEEEEE; }}
    .topline span {{ font-size:11px; letter-spacing:6px; text-transform:uppercase; color:#8F8F8F; font-weight:300; }}
    .hero {{ background:#FFFFFF; padding:58px 46px 46px; text-align:center; border-bottom:1px solid #EEEEEE; }}
    .hero .kicker {{ font-size:10px; letter-spacing:8px; text-transform:uppercase; color:#AAA4A0; margin-bottom:24px; font-weight:300; }}
    .rule {{ width:38px; height:1px; background:#EEEEEE; margin:24px auto 28px; }}
    h1 {{ margin:0; font-family:'Playfair Display', Georgia, 'Times New Roman', serif; font-weight:400; font-size:50px; line-height:.95; letter-spacing:-1.2px; }}
    h1 em {{ color:#8A8A8A; font-style:italic; font-weight:400; }}
    .hero .rule.after {{ margin:25px auto 28px; }}
    .hero p {{ color:#777777; font-size:16px; line-height:1.85; margin:0 auto; max-width:425px; letter-spacing:0; }}
    .grid {{ background:#FFFFFF; display:block; }}
    .card {{ border-bottom:1px solid #EEEEEE; background:#FFFFFF; }}
    .media {{ background:#FFFFFF; min-height:285px; display:flex; align-items:center; justify-content:center; overflow:hidden; line-height:0; padding:28px 48px 10px; }}
    .product-img {{ width:100%; max-width:490px; max-height:245px; object-fit:contain; object-position:center center; display:block; }}
    .image-fallback {{ color:#777777; font-size:13px; line-height:1.6; text-align:center; padding:34px; }}
    .image-fallback span {{ font-size:10px; letter-spacing:5px; text-transform:uppercase; color:#C3C3C3; }}
    .info {{ background:#EEE8E0; padding:40px 58px 46px; text-align:center; display:flex; flex-direction:column; align-items:center; }}
    .eyebrow {{ color:#9F9891; font-size:9px; letter-spacing:5px; text-transform:uppercase; margin-bottom:16px; font-weight:300; }}
    h3 {{ font-family:'Playfair Display', Georgia, 'Times New Roman', serif; font-size:31px; line-height:1.1; font-weight:400; margin:0 0 16px; color:#111111; max-width:430px; }}
    .copy {{ color:#777777; font-size:14px; line-height:1.9; margin:0 0 18px; max-width:410px; }}
    .meta {{ color:#8A8A8A; font-size:10px; line-height:1.6; margin:0 0 24px; letter-spacing:.5px; }}
    .button {{ align-self:center; background:#050505; color:#FFFFFF; text-decoration:none; padding:16px 24px; font-size:9px; letter-spacing:3px; text-transform:uppercase; }}
    .manifesto {{ background:#050505; color:#FFFFFF; margin:0; padding:58px 44px 50px; text-align:center; }}
    .manifesto p {{ font-family:'Playfair Display', Georgia, 'Times New Roman', serif; font-weight:400; font-style:italic; font-size:25px; line-height:1.45; margin:0 0 20px; color:#F8F8F8; }}
    .manifesto .sig {{ font-size:9px; letter-spacing:4px; text-transform:uppercase; color:#8A8A8A; }}
    .footer {{ background:#050505; padding:48px 44px 44px; text-align:center; color:#8A8A8A; }}
    .footer-logo {{ display:inline-block; margin-bottom:22px; width:66px; height:auto; }}
    .footer-slogan {{ font-family:'Playfair Display', Georgia, 'Times New Roman', serif; font-weight:400; font-style:italic; font-size:15px; color:#B5B0A8; letter-spacing:.8px; line-height:1.45; margin-bottom:26px; }}
    .footer-rule {{ width:32px; height:1px; background:rgba(255,255,255,.14); margin:0 auto 22px; }}
    .address {{ font-size:11px; font-weight:300; line-height:1.9; color:#8A8A8A; }}
    .links {{ margin-top:18px; }}
    .links a {{ font-size:9px; letter-spacing:3px; text-transform:uppercase; color:#B5B0A8; text-decoration:none; margin:0 9px; }}
    .unsubscribe {{ margin-top:24px; padding-top:20px; border-top:1px solid rgba(255,255,255,.08); }}
    .unsubscribe a {{ font-size:9px; letter-spacing:2.5px; text-transform:uppercase; color:#8A8A8A; text-decoration:none; }}
    @media (max-width:620px) {{
      .frame {{ max-width:100%; }}
      .hero {{ padding:54px 34px 44px; }}
      h1 {{ font-size:44px; }}
      .hero p {{ font-size:15px; }}
      .media {{ min-height:270px; padding:26px 32px 8px; }}
      .product-img {{ max-height:220px; }}
      .info {{ padding:38px 32px 44px; }}
      h3 {{ font-size:29px; }}
      .copy {{ font-size:13.5px; }}
    }}
  </style>
</head>
<body>
  <main class="frame">
    <header class="header"><img alt="LK Sneakers" src="{esc(LOGO_WHITE)}"></header>
    <section class="topline"><span>CURADORIA LK · DISPONIBILIDADE CONFERIDA</span></section>
    <section class="hero">
      <div class="kicker">SELEÇÃO EXCLUSIVA</div>
      <h1>Sua curadoria<br><em>está pronta.</em></h1>
      <div class="rule after"></div>
      <p>Peças escolhidas para continuar a sua última compra na LK, com estética próxima e disponibilidade conferida no seu tamanho.</p>
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
