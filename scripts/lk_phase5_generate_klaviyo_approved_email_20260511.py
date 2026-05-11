#!/usr/bin/env python3
"""Generate customer-facing LK/Klaviyo HTML for approved Phase 5 P1 physical-store queue.

Safe scope:
- Reads approved Klaviyo import CSV from private_exports.
- Uses Shopify read-only enrichment via existing preview generator.
- Writes no-PII customer-facing HTML/MD/JSON under reports/.
- Does not create Klaviyo campaigns/lists/templates and does not send anything.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from lk_phase5_generate_klaviyo_ready_visual_preview_20260511 import (
    LOGO_WHITE,
    clean_name,
    esc,
    fallback_shopify_by_product,
    group_rows,
    no_em_dash,
    query_shopify_by_sku,
    read_rows,
)

ROOT = Path(__file__).resolve().parents[1]
OUT_HTML = ROOT / 'reports/lk-phase5-p1-klaviyo-approved-email-2026-05-11.html'
OUT_MD = ROOT / 'reports/lk-phase5-p1-klaviyo-approved-email-2026-05-11.md'
OUT_JSON = ROOT / 'reports/lk-phase5-p1-klaviyo-approved-email-2026-05-11.json'
PRIVATE_IMPORT = Path('/opt/data/hermes_bruno_ingest/private_exports/lk_crm/lk_phase5_p1_klaviyo_approved_import_2026-05-11.csv')


def card_copy(product: str) -> str:
    name = clean_name(product)
    if '204L' in name:
        return 'Uma silhueta limpa, atual e fácil de encaixar no guarda-roupa, com disponibilidade conferida para a curadoria LK.'
    if 'Onitsuka' in name or 'Mexico 66' in name:
        return 'Uma leitura leve e sofisticada para quem busca um sneaker com presença discreta, textura e acabamento premium.'
    return 'Uma seleção pontual, escolhida pela proximidade de estilo com a sua última visita à LK Flagship.'


def build_html(rows: list[dict[str, str]], enrichment: dict[str, Any]) -> str:
    cards: list[str] = []
    for product, product_rows in group_rows(rows):
        sku = product_rows[0].get('anchor_sku') or product_rows[0].get('store_purchase_sku') or ''
        enrich = enrichment.get(sku, {})
        img = enrich.get('image_url') or ''
        img_html = (
            f'<img class="product-img" src="{esc(img)}" alt="{esc(enrich.get("image_alt") or product)}">'
            if img
            else '<div class="image-fallback">Imagem indisponível</div>'
        )
        cards.append(f'''
          <article class="card">
            <div class="media">{img_html}</div>
            <div class="info">
              <div class="eyebrow">SELEÇÃO PERSONALIZADA LK</div>
              <h3>{esc(clean_name(product))}</h3>
              <p class="copy">{esc(card_copy(product))}</p>
              <a class="button" href="{esc(enrich.get('url') or 'https://lksneakers.com.br/')}">Falar com consultor</a>
            </div>
          </article>
        ''')

    html_doc = f'''<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Curadoria LK</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Inter:wght@300;400;500&display=swap');
    * {{ box-sizing:border-box; }}
    body {{ margin:0; background:#FFFFFF; color:#111111; font-family:Inter, Arial, Helvetica, sans-serif; }}
    .frame {{ max-width:600px; margin:0 auto; background:#FFFFFF; }}
    .header {{ background:#050505; height:150px; display:flex; align-items:center; justify-content:center; text-align:center; }}
    .header img {{ display:block; width:78px; height:auto; }}
    .topline {{ background:#F8F5F1; padding:27px 20px 20px; text-align:center; border-bottom:1px solid #E5D7C9; }}
    .topline span {{ display:inline-block; font-size:11px; letter-spacing:6px; text-transform:uppercase; color:#8A6F5B; font-weight:400; }}
    .hero {{ background:#F2ECE4; padding:58px 46px 50px; text-align:center; border-bottom:1px solid #E5D7C9; position:relative; overflow:hidden; }}
    .hero:before {{ content:""; position:absolute; top:0; left:50%; transform:translateX(-50%); width:118px; height:5px; background:#B08A67; border-radius:0 0 999px 999px; }}
    .hero .kicker {{ display:inline-block; font-size:10px; letter-spacing:6px; text-transform:uppercase; color:#8A6F5B; margin-bottom:24px; font-weight:400; background:#FFFFFF; border:1px solid #E5D7C9; border-radius:999px; padding:11px 16px 10px 22px; }}
    .rule {{ width:38px; height:1px; background:#CDB49C; margin:25px auto 28px; }}
    h1 {{ margin:0; font-family:'Playfair Display', Georgia, 'Times New Roman', serif; font-weight:400; font-size:49px; line-height:.96; letter-spacing:-1.2px; }}
    h1 .warm {{ color:#B08A67; }}
    h1 em {{ color:#777777; font-style:italic; font-weight:400; }}
    .hero p {{ color:#6F6963; font-size:16px; line-height:1.85; margin:0 auto; max-width:425px; }}
    .grid {{ background:#FFFFFF; display:block; }}
    .card {{ border-bottom:1px solid #EEEEEE; background:#FFFFFF; }}
    .media {{ background:#FFFFFF; min-height:285px; display:flex; align-items:center; justify-content:center; overflow:hidden; line-height:0; padding:28px 48px 10px; }}
    .product-img {{ width:100%; max-width:490px; max-height:245px; object-fit:contain; object-position:center center; display:block; }}
    .image-fallback {{ color:#777777; font-size:13px; line-height:1.6; text-align:center; padding:34px; }}
    .info {{ background:#EEE8E0; padding:40px 58px 46px; text-align:center; display:flex; flex-direction:column; align-items:center; }}
    .eyebrow {{ color:#9F9891; font-size:9px; letter-spacing:5px; text-transform:uppercase; margin-bottom:16px; font-weight:300; }}
    h3 {{ font-family:'Playfair Display', Georgia, 'Times New Roman', serif; font-size:31px; line-height:1.1; font-weight:400; margin:0 0 16px; color:#111111; max-width:430px; }}
    .copy {{ color:#777777; font-size:14px; line-height:1.9; margin:0 0 24px; max-width:410px; }}
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
      h1 {{ font-size:43px; }}
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
    <section class="topline"><span>CURADORIA LK</span></section>
    <section class="hero">
      <div class="kicker">SELEÇÃO PERSONALIZADA</div>
      <h1><span class="warm">Uma curadoria</span><br><em>para você.</em></h1>
      <div class="rule"></div>
      <p>Depois da sua visita à LK Flagship, separamos algumas opções que conversam com o seu estilo e com o momento da sua coleção.</p>
    </section>
    <section class="grid">
      {''.join(cards)}
    </section>
    <section class="manifesto"><p>"Escolhas raras ficam melhores quando fazem sentido no seu guarda-roupa."</p><div class="sig">LK Sneakers</div></section>
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
    skus: list[str] = []
    for row in rows:
        sku = row.get('anchor_sku') or row.get('store_purchase_sku') or ''
        if sku and sku not in skus:
            skus.append(sku)
    enrichment = fallback_shopify_by_product(rows, query_shopify_by_sku(skus))
    html_doc = build_html(rows, enrichment)
    OUT_HTML.write_text(html_doc)
    loaded_images = sum(1 for sku in skus if enrichment.get(sku, {}).get('image_url'))
    groups = group_rows(rows)
    summary = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'Customer-facing approved email HTML prepared locally. No Klaviyo object, no list and no send created.',
        'approved_import_csv': str(PRIVATE_IMPORT),
        'html_email': str(OUT_HTML.relative_to(ROOT)),
        'source_rows': len(rows),
        'visual_product_groups': len(groups),
        'unique_skus': len(skus),
        'shopify_images_loaded': loaded_images,
        'subject_options': [
            'Uma curadoria LK pensada para você',
            'Peças que conversam com a sua última escolha',
            'Sua seleção personalizada LK',
        ],
        'preheader': 'Selecionamos algumas opções com o olhar da LK Flagship para o seu próximo sneaker.',
        'guardrails': [
            'Nenhum objeto Klaviyo criado',
            'Nenhuma lista criada',
            'Nenhum envio externo',
            'Nenhum write em Shopify/Tiny/Supabase',
            'HTML sem raw PII',
        ],
    }
    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')
    lines = [
        '# LK Phase 5 P1, e-mail Klaviyo aprovado localmente, 2026-05-11', '',
        '## Veredito', '',
        'Preparei a versão customer-facing do e-mail, sem linguagem interna de preview, P1, Klaviyo ou sem envio. Nenhum objeto externo foi criado.', '',
        '## Assunto sugerido', '',
        '- Uma curadoria LK pensada para você', '',
        '## Preheader', '',
        '- Selecionamos algumas opções com o olhar da LK Flagship para o seu próximo sneaker.', '',
        '## Controles', '',
        f'- Linhas aprovadas no import privado: {len(rows)}',
        f'- Grupos visuais por produto: {len(groups)}',
        f'- Imagens Shopify carregadas: {loaded_images}/{len(skus)}',
        '- PII no HTML/Brain: não',
        '- Klaviyo criado: não',
        '- Lista criada: não',
        '- Envio externo: não', '',
        '## Arquivos', '',
        f'- HTML customer-facing: `{OUT_HTML.relative_to(ROOT)}`',
        f'- JSON: `{OUT_JSON.relative_to(ROOT)}`',
        f'- CSV privado aprovado para import: `{PRIVATE_IMPORT}`',
    ]
    OUT_MD.write_text(no_em_dash('\n'.join(lines) + '\n'))
    print(json.dumps({'html': str(OUT_HTML), 'md': str(OUT_MD), 'json': str(OUT_JSON), 'rows': len(rows), 'groups': len(groups), 'images': f'{loaded_images}/{len(skus)}'}, ensure_ascii=False))


if __name__ == '__main__':
    main()
