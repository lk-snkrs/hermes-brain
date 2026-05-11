#!/usr/bin/env python3
"""Generate final internal LK/Klaviyo visual preview for P1 Klaviyo-ready physical-store queue.

Read-only only:
- Reads private P1 Klaviyo CSV under private_exports.
- Uses Shopify Admin GraphQL read-only to enrich product image/URL by SKU.
- Writes anonymized Brain reports under reports/.
- Does not create Klaviyo campaigns/lists/templates and does not send anything.
"""
from __future__ import annotations

import csv
import html
import json
from collections import OrderedDict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from lk_phase5_generate_klaviyo_visual_preview_20260511 import (
    LOGO_WHITE,
    load_doppler_secrets,
    no_em_dash,
    query_shopify_by_sku,
    shopify_graphql,
)

ROOT = Path(__file__).resolve().parents[1]
PRIVATE_CSV = Path('/opt/data/hermes_bruno_ingest/private_exports/lk_crm/lk_phase5_p1_klaviyo_ready_2026-05-11.csv')
OUT_HTML = ROOT / 'reports/lk-phase5-p1-klaviyo-ready-visual-preview-2026-05-11.html'
OUT_MD = ROOT / 'reports/lk-phase5-p1-klaviyo-ready-visual-preview-2026-05-11.md'
OUT_JSON = ROOT / 'reports/lk-phase5-p1-klaviyo-ready-visual-preview-2026-05-11.json'


def esc(value: Any) -> str:
    return html.escape(str(value or ''), quote=True)


def read_rows() -> list[dict[str, str]]:
    with PRIVATE_CSV.open(newline='') as f:
        return list(csv.DictReader(f))


def clean_name(value: str) -> str:
    return (value or '').replace('Tênis ', '').replace('Tenis ', '').strip()


def sizes_label(rows: list[dict[str, str]]) -> str:
    sizes: list[str] = []
    for row in rows:
        size = str(row.get('store_purchase_size') or row.get('anchor_size') or '').strip()
        if size and size not in sizes:
            sizes.append(size)
    if not sizes:
        return 'TAMANHO CONFERIDO'
    if len(sizes) == 1:
        return f'TAMANHO {sizes[0]}'
    return 'TAMANHOS ' + ' E '.join([', '.join(sizes[:-1]), sizes[-1]]).strip(', ')


def segment_label(rows: list[dict[str, str]]) -> str:
    segments = []
    for row in rows:
        seg = row.get('segment') or ''
        if seg and seg not in segments:
            segments.append(seg)
    if any('Champions' in s for s in segments):
        return 'VIP LK'
    return 'SEGUNDA COMPRA'


def group_rows(rows: list[dict[str, str]]) -> list[tuple[str, list[dict[str, str]]]]:
    groups: 'OrderedDict[str, list[dict[str, str]]]' = OrderedDict()
    for row in rows:
        key = row.get('anchor_product') or row.get('store_purchase_product') or ''
        groups.setdefault(key, []).append(row)
    return list(groups.items())


def fallback_shopify_by_product(rows: list[dict[str, str]], enrichment: dict[str, Any]) -> dict[str, Any]:
    """Fill missing base-SKU enrichment by searching products read-only in Shopify."""
    missing = []
    for row in rows:
        sku = row.get('anchor_sku') or row.get('store_purchase_sku') or ''
        if sku and not enrichment.get(sku, {}).get('image_url') and sku not in missing:
            missing.append(sku)
    if not missing:
        return enrichment
    secrets = load_doppler_secrets()
    store = secrets.get('SHOPIFY_STORE_URL', '')
    token = secrets.get('SHOPIFY_ACCESS_TOKEN', '')
    if not store or not token:
        return enrichment
    gql = '''
    query ProductFallback($query: String!) {
      products(first: 5, query: $query) {
        nodes {
          title
          handle
          onlineStoreUrl
          featuredImage { url altText }
          images(first: 1) { nodes { url altText } }
          variants(first: 8) { nodes { sku title image { url altText } } }
        }
      }
    }
    '''
    rows_by_sku = {row.get('anchor_sku') or row.get('store_purchase_sku') or '': row for row in rows}
    for sku in missing:
        row = rows_by_sku.get(sku, {})
        product_name = row.get('anchor_product') or row.get('store_purchase_product') or sku
        queries = [sku, clean_name(product_name)]
        for query in queries:
            try:
                data = shopify_graphql(store, token, gql, {'query': query})
            except Exception as exc:
                enrichment[sku] = {'error': type(exc).__name__}
                continue
            nodes = data.get('data', {}).get('products', {}).get('nodes', [])
            if not nodes:
                continue
            product = nodes[0]
            featured = product.get('featuredImage') or {}
            image_nodes = ((product.get('images') or {}).get('nodes') or [])
            fallback_img = image_nodes[0] if image_nodes else {}
            variant_nodes = ((product.get('variants') or {}).get('nodes') or [])
            variant_img = {}
            for variant in variant_nodes:
                if str(variant.get('sku') or '').startswith(sku):
                    variant_img = variant.get('image') or {}
                    break
            enrichment[sku] = {
                'sku': sku,
                'product_title': product.get('title'),
                'handle': product.get('handle'),
                'url': product.get('onlineStoreUrl'),
                'image_url': variant_img.get('url') or featured.get('url') or fallback_img.get('url'),
                'image_alt': variant_img.get('altText') or featured.get('altText') or fallback_img.get('altText') or product.get('title'),
                'fallback_query': query,
            }
            break
    return enrichment


def card_copy(product: str, rows: list[dict[str, str]]) -> str:
    count = len(rows)
    name = clean_name(product)
    if count == 1:
        return f'Uma leitura individual a partir do {name}, com peças que preservam a mesma intenção de estilo e disponibilidade conferida no tamanho certo.'
    return f'Uma curadoria curta para {count} clientes que escolheram {name} na LK Flagship, reunindo caminhos próximos de estilo com disponibilidade conferida nos tamanhos certos.'


def build_html(rows: list[dict[str, str]], enrichment: dict[str, Any]) -> str:
    cards: list[str] = []
    for product, product_rows in group_rows(rows):
        sku = product_rows[0].get('anchor_sku') or product_rows[0].get('store_purchase_sku') or ''
        enrich = enrichment.get(sku, {})
        img = enrich.get('image_url') or ''
        img_html = (
            f'<img class="product-img" src="{esc(img)}" alt="{esc(enrich.get("image_alt") or product)}">'
            if img
            else '<div class="image-fallback">Imagem Shopify não encontrada<br><span>Preview interno</span></div>'
        )
        cards.append(f'''
          <article class="card">
            <div class="media">{img_html}</div>
            <div class="info">
              <div class="eyebrow">{esc(segment_label(product_rows))} · {esc(sizes_label(product_rows))} · {len(product_rows)} CLIENTE(S)</div>
              <h3>{esc(clean_name(product))}</h3>
              <p class="copy">{esc(card_copy(product, product_rows))}</p>
              <p class="meta">Preview visual interno, sem campanha criada e sem envio.</p>
              <a class="button" href="{esc(enrich.get('url') or '#')}">Falar com consultor</a>
            </div>
          </article>
        ''')

    html_doc = f'''<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>LK Phase 5 P1, Klaviyo ready visual preview</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Inter:wght@300;400;500&display=swap');
    * {{ box-sizing:border-box; }}
    body {{ margin:0; background:#FFFFFF; color:#111111; font-family:Inter, Arial, Helvetica, sans-serif; }}
    .frame {{ max-width:600px; margin:0 auto; background:#FFFFFF; }}
    .header {{ background:#050505; height:150px; display:flex; align-items:center; justify-content:center; text-align:center; }}
    .header img {{ display:block; width:78px; height:auto; }}
    .topline {{ background:#FFFFFF; padding:27px 20px 20px; text-align:center; border-bottom:1px solid #EEEEEE; }}
    .topline span {{ font-size:11px; letter-spacing:6px; text-transform:uppercase; color:#8F8F8F; font-weight:300; }}
    .hero {{ background:#F2ECE4; padding:58px 46px 46px; text-align:center; border-bottom:1px solid #E5D7C9; position:relative; overflow:hidden; }}
    .hero:before {{ content:""; position:absolute; top:0; left:50%; transform:translateX(-50%); width:118px; height:5px; background:#B08A67; border-radius:0 0 999px 999px; }}
    .hero .kicker {{ display:inline-block; font-size:10px; letter-spacing:6px; text-transform:uppercase; color:#8A6F5B; margin-bottom:24px; font-weight:400; background:#FFFFFF; border:1px solid #E5D7C9; border-radius:999px; padding:11px 16px 10px 22px; }}
    .rule {{ width:38px; height:1px; background:#CDB49C; margin:25px auto 28px; }}
    h1 {{ margin:0; font-family:'Playfair Display', Georgia, 'Times New Roman', serif; font-weight:400; font-size:50px; line-height:.95; letter-spacing:-1.2px; }}
    h1 .warm {{ color:#B08A67; }}
    h1 em {{ color:#8A8A8A; font-style:italic; font-weight:400; }}
    .hero p {{ color:#777777; font-size:16px; line-height:1.85; margin:0 auto; max-width:425px; }}
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
    <section class="topline"><span>CURADORIA LK · FILA KLAVIYO P1</span></section>
    <section class="hero">
      <div class="kicker">PREVIEW DE APROVAÇÃO</div>
      <h1><span class="warm">Pronto</span> para<br><em>revisão.</em></h1>
      <div class="rule"></div>
      <p>Seleção visual dos grupos Klaviyo P1 da loja física. Tudo permanece interno: sem campanha, sem lista e sem envio.</p>
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
</html>'''
    return no_em_dash(html_doc)


def main() -> None:
    rows = read_rows()
    skus = []
    for row in rows:
        sku = row.get('anchor_sku') or row.get('store_purchase_sku') or ''
        if sku and sku not in skus:
            skus.append(sku)
    enrichment = fallback_shopify_by_product(rows, query_shopify_by_sku(skus))
    html_doc = build_html(rows, enrichment)
    OUT_HTML.write_text(html_doc)
    groups = group_rows(rows)
    loaded_images = sum(1 for sku in skus if enrichment.get(sku, {}).get('image_url'))
    summary = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'Internal visual approval preview for P1 Klaviyo-ready physical-store queue. No sends, no external writes, no PII in Brain output.',
        'source_private_csv': str(PRIVATE_CSV),
        'html_preview': str(OUT_HTML.relative_to(ROOT)),
        'source_rows': len(rows),
        'visual_product_groups': len(groups),
        'unique_skus': len(skus),
        'shopify_images_loaded': loaded_images,
        'groups': [
            {
                'product': product,
                'count': len(product_rows),
                'sizes': sizes_label(product_rows),
                'segment_label': segment_label(product_rows),
            }
            for product, product_rows in groups
        ],
        'shopify_enrichment_by_sku': enrichment,
        'guardrails': [
            'Preview interno apenas',
            'Nenhum objeto Klaviyo criado',
            'Nenhuma lista externa criada',
            'Nenhum envio externo',
            'Nenhum write em Shopify/Tiny/Supabase',
            'Brain report sem raw PII',
        ],
    }
    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')
    lines = [
        '# LK Phase 5 P1, Klaviyo-ready visual preview, 2026-05-11',
        '',
        '## Veredito',
        '',
        'Gerei um preview visual interno para a fila Klaviyo P1 já filtrada para loja física. Não criei campanha, lista ou envio.',
        '',
        '## Controles',
        '',
        f'- Linhas privadas de origem: {len(rows)}',
        f'- Grupos visuais por produto: {len(groups)}',
        f'- SKUs únicos consultados no Shopify read-only: {len(skus)}',
        f'- Imagens Shopify carregadas: {loaded_images}/{len(skus)}',
        '- PII no Brain: não',
        '- Klaviyo criado: não',
        '- Lista criada: não',
        '- Envio externo: não',
        '',
        '## Grupos no preview',
        '',
    ]
    for product, product_rows in groups:
        lines.append(f'- {clean_name(product)}: {len(product_rows)} cliente(s), {sizes_label(product_rows)}, {segment_label(product_rows)}')
    lines += ['', '## Arquivos', '', f'- HTML: `{OUT_HTML.relative_to(ROOT)}`', f'- JSON: `{OUT_JSON.relative_to(ROOT)}`']
    OUT_MD.write_text(no_em_dash('\n'.join(lines) + '\n'))
    print(json.dumps({'html': str(OUT_HTML), 'md': str(OUT_MD), 'json': str(OUT_JSON), 'rows': len(rows), 'groups': len(groups), 'images': f'{loaded_images}/{len(skus)}'}, ensure_ascii=False))


if __name__ == '__main__':
    main()
