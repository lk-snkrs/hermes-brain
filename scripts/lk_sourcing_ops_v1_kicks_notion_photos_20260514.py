#!/usr/bin/env python3
from __future__ import annotations
import base64, json, os, pathlib, re, time, urllib.error, urllib.parse, urllib.request
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
DOPPLER_TOKEN_FILE = pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
PAYLOAD = ROOT/'reports/lk-compras-unified-sourcing-payload-2026-05-14.json'
NOTION_EXEC = ROOT/'reports/lk-compras-unified-sourcing-notion-execution-2026-05-14.json'
OUT_JSON = ROOT/'reports/lk-sourcing-ops-v1-kicks-notion-photos-2026-05-14.json'
OUT_MD = ROOT/'reports/lk-sourcing-ops-v1-kicks-notion-photos-2026-05-14.md'
MC_MD = ROOT/'areas/lk/rotinas/mission-control-sourcing-ops-v1-2026-05-14.md'
NOTION_VERSION = '2022-06-28'
USD_BRL = 4.911381
FX_BUFFER = 1.05
CUSTO_TRAZER_USD = 100.0
IMPORT_MULTIPLIER = 1.0
MARKUP_TARGET = 2.0
FACTOR_BRL_PER_USD = USD_BRL * FX_BUFFER
RUN_MARKER = 'LK OS sourcing ops v1 — KicksDev/photo enrichment — 2026-05-14'


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_doppler() -> dict[str, str]:
    token = os.environ.get('DOPPLER_TOKEN') or DOPPLER_TOKEN_FILE.read_text().strip()
    req = urllib.request.Request('https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json')
    req.add_header('Authorization', 'Basic ' + base64.b64encode((token + ':').encode()).decode())
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())


def http_json(url: str, headers: dict[str, str], method='GET', payload: dict[str, Any] | None = None, attempts=4) -> dict[str, Any]:
    data = None if payload is None else json.dumps(payload, ensure_ascii=False).encode('utf-8')
    for i in range(attempts):
        req = urllib.request.Request(url, data=data, method=method)
        for k, v in headers.items():
            req.add_header(k, v)
        if data is not None:
            req.add_header('Content-Type', 'application/json; charset=utf-8')
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                raw = r.read().decode()
                return json.loads(raw) if raw else {}
        except urllib.error.HTTPError as e:
            body = e.read().decode(errors='replace')
            if e.code not in {429, 500, 502, 503, 504} or i == attempts - 1:
                return {'error': f'http_{e.code}', 'body': body[:500]}
        except Exception as e:
            if i == attempts - 1:
                return {'error': type(e).__name__, 'body': str(e)[:500]}
        time.sleep(min(20, 2 ** (i + 1)))
    return {'error': 'request_failed'}


def notion_headers(token: str) -> dict[str, str]:
    return {'Authorization': 'Bearer ' + token, 'Notion-Version': NOTION_VERSION}


def kicks_headers(key: str) -> dict[str, str]:
    return {'Authorization': 'Bearer ' + key}


def style_sku(sku: str) -> str:
    s = (sku or '').strip().upper()
    # LK variant suffixes often append size index: U204LMMC-4, 1183A201-126-5, JR9446-2.
    if re.search(r'[A-Z]', s):
        s = re.sub(r'-\d+$', '', s)
    return s.replace(' ', '-')


def norm_sku(s: str | None) -> str:
    return re.sub(r'[^A-Z0-9]', '', (s or '').upper())


def parse_brl(text: str | None) -> float | None:
    if not text:
        return None
    m = re.search(r'R\$\s*([0-9\.]+,[0-9]{2})', text)
    if not m:
        return None
    return float(m.group(1).replace('.', '').replace(',', '.'))


def gross_margin_pct(sale_brl: float | None, cost_brl: float | None) -> float | None:
    if not sale_brl or cost_brl is None:
        return None
    return (sale_brl - cost_brl) / sale_brl


def brl(v: float | None) -> str:
    if v is None:
        return 'n/d'
    return f'R$ {v:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


def usd(v: float | None) -> str:
    if v is None:
        return 'n/d'
    return f'US$ {v:,.2f}'


def kicks_search(key: str, path: str, query: str) -> dict[str, Any] | None:
    url = 'https://api.kicks.dev' + path + '?' + urllib.parse.urlencode({'query': query, 'limit': 5})
    data = http_json(url, kicks_headers(key))
    if data.get('error'):
        return {'error': data.get('error'), 'body': data.get('body')}
    rows = data.get('data') or []
    exact = [x for x in rows if norm_sku(x.get('sku')) == norm_sku(query)]
    return (exact or rows or [None])[0]


def stockx_product(key: str, style: str) -> dict[str, Any] | None:
    p = kicks_search(key, '/v3/stockx/products', style)
    if not p or p.get('error'):
        return p
    return p


def goat_product(key: str, style: str) -> dict[str, Any] | None:
    # GOAT stores SKUs with spaces in some rows; try hyphen style then plain/space fallback.
    for q in [style, style.replace('-', ' '), style.replace('-', '')]:
        p = kicks_search(key, '/v3/goat/products', q)
        if p and not p.get('error') and norm_sku(p.get('sku')) == norm_sku(style):
            return p
    return p if p else None


def image_block(url: str, caption: str) -> dict[str, Any]:
    return {'object': 'block', 'type': 'image', 'image': {'type': 'external', 'external': {'url': url}, 'caption': [{'type': 'text', 'text': {'content': caption[:1900]}}]}}


def paragraph(text: str) -> dict[str, Any]:
    return {'object': 'block', 'type': 'paragraph', 'paragraph': {'rich_text': [{'type': 'text', 'text': {'content': text[:1900]}}]}}


def page_has_marker(token: str, page_id: str) -> bool:
    url = f'https://api.notion.com/v1/blocks/{page_id}/children?page_size=100'
    data = http_json(url, notion_headers(token))
    for b in data.get('results', []) if isinstance(data, dict) else []:
        typ = b.get('type')
        if typ and typ in b:
            rich = b[typ].get('rich_text') or b[typ].get('caption') or []
            text = ''.join(((x.get('plain_text') or (x.get('text') or {}).get('content') or '') for x in rich))
            if RUN_MARKER in text:
                return True
    return False


def patch_page_cover(token: str, page_id: str, image_url: str) -> dict[str, Any]:
    payload = {'cover': {'type': 'external', 'external': {'url': image_url}}}
    return http_json(f'https://api.notion.com/v1/pages/{page_id}', notion_headers(token), method='PATCH', payload=payload)


def append_enrichment(token: str, page_id: str, blocks: list[dict[str, Any]]) -> dict[str, Any]:
    return http_json(f'https://api.notion.com/v1/blocks/{page_id}/children', notion_headers(token), method='PATCH', payload={'children': blocks})


def import_cost(price_usd: float | None) -> float | None:
    if price_usd is None:
        return None
    return (price_usd + CUSTO_TRAZER_USD) * FACTOR_BRL_PER_USD


def recommendation(card: dict[str, Any], stockx: dict[str, Any] | None, goat: dict[str, Any] | None) -> dict[str, Any]:
    sale = parse_brl(card.get('Preço médio vendido'))
    nat_cost = parse_brl(card.get('Opção nacional/Droper'))
    stockx_min = stockx.get('min_price') if isinstance(stockx, dict) and isinstance(stockx.get('min_price'), (int, float)) else None
    stockx_avg = stockx.get('avg_price') if isinstance(stockx, dict) and isinstance(stockx.get('avg_price'), (int, float)) else None
    landed_min = import_cost(float(stockx_min)) if stockx_min is not None else None
    landed_avg = import_cost(float(stockx_avg)) if stockx_avg is not None else None
    m_nat = gross_margin_pct(sale, nat_cost)
    m_imp_min = gross_margin_pct(sale, landed_min)
    if stockx_min is None:
        verdict = 'needs_manual_authenticated_size_price'
    elif m_imp_min is not None and m_imp_min >= 0.30:
        verdict = 'import_signal_good_but_verify_exact_size'
    elif m_imp_min is not None and m_imp_min >= 0.20:
        verdict = 'import_signal_borderline_verify_exact_size'
    elif m_nat is not None and m_nat >= 0.30:
        verdict = 'national_route_preferred_if_available'
    elif m_nat is not None and m_nat >= 0.20:
        verdict = 'national_borderline_human_compare_logistics'
    else:
        verdict = 'likely_skip_or_watchlist_unless_exact_size_price_better'
    return {
        'sale_price_brl': sale,
        'national_cost_brl': nat_cost,
        'national_margin_pct': m_nat,
        'stockx_min_usd_product_level': stockx_min,
        'stockx_avg_usd_product_level': stockx_avg,
        'stockx_landed_min_brl': landed_min,
        'stockx_landed_avg_brl': landed_avg,
        'import_margin_pct_min_signal': m_imp_min,
        'verdict': verdict,
        'limitation': 'KicksDev StockX price is product-level market signal; exact size ask still requires authenticated/manual lookup before purchase.'
    }


def main():
    sec = load_doppler()
    notion_token = sec.get('NOTION_TOKEN_LK') or sec.get('NOTION_API_KEY')
    kicks_key = sec.get('KICKS_DEV_API_KEY') or sec.get('KICKS_API_KEY') or sec.get('KICKSDB_API_KEY')
    if not notion_token:
        raise SystemExit('missing Notion token')
    if not kicks_key:
        raise SystemExit('missing KicksDev key')
    cards = json.loads(PAYLOAD.read_text())['cards']
    exec_rows = {r['title']: r for r in json.loads(NOTION_EXEC.read_text())['results']}
    rows = []
    updated_cover = updated_blocks = skipped_no_page = 0
    product_cache: dict[str, dict[str, Any]] = {}
    for card in cards:
        title = card['Nome']
        page_id = (exec_rows.get(title) or {}).get('page_id')
        style = style_sku(card.get('SKU') or '')
        if style not in product_cache:
            sx = stockx_product(kicks_key, style)
            time.sleep(0.25)
            goat = goat_product(kicks_key, style)
            time.sleep(0.25)
            product_cache[style] = {'stockx': sx, 'goat': goat}
        sx = product_cache[style]['stockx']
        goat = product_cache[style]['goat']
        image = None
        if isinstance(sx, dict):
            image = sx.get('image') or (sx.get('gallery') or [None])[0]
        if not image and isinstance(goat, dict):
            image = goat.get('image_url') or (goat.get('images') or [None])[0]
        rec = recommendation(card, sx if isinstance(sx, dict) else None, goat if isinstance(goat, dict) else None)
        row = {
            'title': title,
            'page_id': page_id,
            'page_url': (exec_rows.get(title) or {}).get('url'),
            'priority': card.get('Prioridade'),
            'model': card.get('Modelo'),
            'size_lk': card.get('Tamanho'),
            'sku_lk': card.get('SKU'),
            'style_sku': style,
            'kicks_stockx': None if not isinstance(sx, dict) else {k: sx.get(k) for k in ['id','title','sku','link','image','min_price','avg_price','max_price','weekly_orders']},
            'kicks_goat': None if not isinstance(goat, dict) else {k: goat.get(k) for k in ['id','name','sku','link','image_url','weekly_orders']},
            'image_url': image,
            'recommendation': rec,
            'notion_update': None,
        }
        if not page_id:
            skipped_no_page += 1
            row['notion_update'] = 'skipped_no_page_id'
        else:
            if image:
                cov = patch_page_cover(notion_token, page_id, image)
                if not cov.get('error'):
                    updated_cover += 1
                marker_exists = page_has_marker(notion_token, page_id)
                if not marker_exists:
                    caption = f"{RUN_MARKER}. Fonte imagem: KicksDev/StockX" + (f" · {sx.get('title')}" if isinstance(sx, dict) and sx.get('title') else '')
                    text = (
                        f"{RUN_MARKER}. KicksDev consultado para {style}. "
                        f"StockX produto: {(sx or {}).get('title') if isinstance(sx, dict) else 'n/d'}; "
                        f"min/avg/max produto: {usd(rec['stockx_min_usd_product_level'])} / {usd(rec['stockx_avg_usd_product_level'])} / {usd((sx or {}).get('max_price') if isinstance(sx, dict) else None)}. "
                        f"Custo importado sinal-min: {brl(rec['stockx_landed_min_brl'])}; margem sinal-min: "
                        f"{(rec['import_margin_pct_min_signal']*100):.1f}%" if rec['import_margin_pct_min_signal'] is not None else f"{RUN_MARKER}. KicksDev consultado para {style}. Sem preço StockX utilizável."
                    )
                    guard = 'Limite: preço KicksDev é sinal por produto, não ask garantido por tamanho. Júlio precisa validar preço exato autenticado/manual antes de compra. Sem compra, reserva, contato, pagamento, Shopify/Tiny/Merchant.'
                    ap = append_enrichment(notion_token, page_id, [image_block(image, caption), paragraph(text), paragraph(guard)])
                    if not ap.get('error'):
                        updated_blocks += 1
                    row['notion_update'] = {'cover_error': cov.get('error'), 'append_error': ap.get('error'), 'marker_preexisted': False}
                else:
                    row['notion_update'] = {'cover_error': cov.get('error'), 'append_skipped': 'marker_already_exists'}
            else:
                row['notion_update'] = 'skipped_no_image'
        rows.append(row)
        time.sleep(0.35)
    summary = {
        'status': 'completed',
        'generated_at': now(),
        'cards': len(cards),
        'unique_styles_queried': len(product_cache),
        'notion_covers_updated': updated_cover,
        'notion_blocks_appended': updated_blocks,
        'skipped_no_page': skipped_no_page,
        'formula': {
            'custo_final_estimado_brl': '(preco_usd + custo_trazer_usd) × (dolar_atual × 1.05) × 2',
            'usd_brl': USD_BRL,
            'custo_trazer_usd': CUSTO_TRAZER_USD,
            'factor_brl_per_usd': FACTOR_BRL_PER_USD,
        },
        'guardrails': ['no_purchase','no_reservation','no_supplier_contact','no_whatsapp_send','no_payment_schedule','no_shopify_write','no_tiny_write','no_merchant_write'],
        'rows': rows,
    }
    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2)+'\n')
    lines = [
        '# LK Sourcing Ops v1 — KicksDev + fotos Notion + rotina Júlio', '',
        f"Generated: `{summary['generated_at']}`", '',
        '## Veredito', '',
        '- Rotina v1 implementada para os 14 cards Notion já criados.',
        f"- KicksDev consultado para {summary['unique_styles_queried']} estilos únicos.",
        f"- Capas Notion atualizadas: {summary['notion_covers_updated']}.",
        f"- Blocos de foto/inteligência adicionados: {summary['notion_blocks_appended']}.",
        '- Preço KicksDev usado como **sinal por produto**; preço exato por tamanho ainda precisa lookup autenticado/manual antes de compra.',
        '- Nenhuma compra, reserva, contato, pagamento, WhatsApp, Shopify, Tiny ou Merchant executado.', '',
        '## Regra fixa a partir daqui', '',
        '- Todo card de sourcing LK deve ter foto do produto quando houver imagem confiável de Shopify/KicksDev/StockX/GOAT/Droper.',
        '- Mission Control deve exibir imagem/foto_url nos cards executivos quando o formato permitir.', '',
        '## Fórmula importação', '',
        f"`(preco_usd + {CUSTO_TRAZER_USD:.0f}) × ({USD_BRL:.6f} × 1,05) × 2` = fator `{FACTOR_BRL_PER_USD:.4f}` por US$", '',
        '## Fila Júlio — próximos passos operacionais', '',
        '1. Abrir os cards `Aguardando Aprovação` no Notion.',
        '2. Validar disponibilidade real e tamanho exato.',
        '3. Se nacional/Droper/grupo estiver com margem ruim, preencher preço exato StockX/GOAT autenticado/manual.',
        '4. Comparar com teto/margem; decidir comprar nacional, importar, pular ou watchlist.',
        '5. Compra continua humana; registrar resultado no Notion.', '',
        '## Cards',
    ]
    for r in rows:
        rec = r['recommendation']
        lines += [
            f"### {r['priority']} — {r['model']} — Tam {r['size_lk']} — `{r['sku_lk']}`",
            f"- Foto: {r['image_url'] or 'n/d'}",
            f"- StockX/KicksDev produto: {(r['kicks_stockx'] or {}).get('title') or 'n/d'}",
            f"- Sinal StockX min/avg: {usd(rec['stockx_min_usd_product_level'])} / {usd(rec['stockx_avg_usd_product_level'])}",
            f"- Custo importado pelo min sinal: {brl(rec['stockx_landed_min_brl'])}",
            f"- Margem import min sinal: {((rec['import_margin_pct_min_signal'] or 0)*100):.1f}%" if rec['import_margin_pct_min_signal'] is not None else '- Margem import min sinal: n/d',
            f"- Veredito motor: `{rec['verdict']}`",
            f"- Notion: {r['page_url'] or r['notion_update']}",
            '',
        ]
    OUT_MD.write_text('\n'.join(lines)+'\n')
    MC_MD.write_text('\n'.join(lines[:35]) + '\n\nFonte completa: `reports/lk-sourcing-ops-v1-kicks-notion-photos-2026-05-14.md`\n')
    print(json.dumps({k: summary[k] for k in ['status','cards','unique_styles_queried','notion_covers_updated','notion_blocks_appended','skipped_no_page']}, ensure_ascii=False))

if __name__ == '__main__':
    main()
