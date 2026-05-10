#!/usr/bin/env python3
"""LK weekly influencer sales report.

Read-only workflow:
- Pulls Meta Ads insights at ad level for the last 7 completed São Paulo days and previous 7 days.
- Uses a canonical Meta purchase/action-value key per ad, avoiding alias double count.
- Pulls Shopify orders for the same windows.
- Attributes Shopify orders/products only when textual evidence contains influencer aliases.
- Sends a comparative HTML email via Gmail OAuth from Doppler when --send is enabled.

No production writes, campaign changes, Shopify mutations, or DB writes.
"""
from __future__ import annotations

import argparse
import base64
import datetime as dt
import html
import json
import os
import re
import sys
from collections import defaultdict
from email.mime.text import MIMEText
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple
from urllib.parse import parse_qs, urlparse

import requests
from zoneinfo import ZoneInfo

BASE = Path('/opt/data')
OUT_DIR = BASE / 'lk_weekly_influencer_sales_reports'
AUDIT_JSON = BASE / 'lk_influencer_audit_corrected_2026-05-10' / 'audit.json'
DOPPLER_TOKEN_FILE = Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
TZ = ZoneInfo('America/Sao_Paulo')
META_ACCOUNT_FALLBACK = 'act_1242062509867163'
CANONICAL_ACTIONS = [
    'offsite_conversion.fb_pixel_purchase',
    'omni_purchase',
    'purchase',
]

EXTRA_ALIASES = {
    'Silvia Henz': ['silvia', 'henz', 'heinz', 'onitsuka'],
    'Helena Lunardelli': ['helena', 'lunardelli'],
    'Lala Noleto': ['lala', 'noleto'],
    'Ju Mesquita': ['ju mesquita', 'juliana mesquita'],
    'Maria Fernanda': ['maria fernanda'],
    'Malu Borges': ['malu borges'],
    'Gio Pagano': ['gio pagano', 'giovanna pagano'],
    'Ma Zanetti': ['ma zanetti', 'má zanetti'],
}


def load_secrets() -> Dict[str, str]:
    if DOPPLER_TOKEN_FILE.exists() and not os.environ.get('DOPPLER_TOKEN'):
        os.environ['DOPPLER_TOKEN'] = DOPPLER_TOKEN_FILE.read_text().strip()
    token = os.environ.get('DOPPLER_TOKEN', '')
    if not token:
        raise RuntimeError('DOPPLER_TOKEN missing')
    r = requests.get(
        'https://api.doppler.com/v3/configs/config/secrets/download',
        params={'project': 'lc-keys', 'config': 'prd', 'format': 'json'},
        auth=(token, ''),
        timeout=60,
    )
    r.raise_for_status()
    return r.json()


def normalize_text(s: Any) -> str:
    s = str(s or '').lower()
    table = str.maketrans('áàãâäéèêëíìîïóòõôöúùûüçñ', 'aaaaaeeeeiiiiooooouuuucn')
    s = s.translate(table)
    return re.sub(r'\s+', ' ', s)


def money(v: float) -> str:
    return ('R$ {:,.2f}'.format(float(v or 0))).replace(',', 'X').replace('.', ',').replace('X', '.')


def pct_change(now: float, prev: float) -> str:
    if prev == 0 and now == 0:
        return '0%'
    if prev == 0:
        return '+∞'
    return f'{((now - prev) / prev) * 100:+.1f}%'.replace('.', ',')


def parse_num(v: Any) -> float:
    try:
        return float(v or 0)
    except Exception:
        return 0.0


def canonical_metric(items: Iterable[Dict[str, Any]]) -> Tuple[float, str | None]:
    vals = {a.get('action_type'): parse_num(a.get('value')) for a in (items or [])}
    for key in CANONICAL_ACTIONS:
        if key in vals:
            return vals[key], key
    return 0.0, None


def load_aliases() -> Dict[str, List[str]]:
    aliases: Dict[str, set[str]] = defaultdict(set)
    if AUDIT_JSON.exists():
        data = json.loads(AUDIT_JSON.read_text(encoding='utf-8'))
        for row in data.get('influencers', []):
            name = row.get('influencer')
            if not name:
                continue
            aliases[name].add(name)
            for raw in row.get('raw_names') or []:
                aliases[name].add(raw)
    for name, vals in EXTRA_ALIASES.items():
        aliases[name].add(name)
        for v in vals:
            aliases[name].add(v)
    # Add normalized individual tokens for names with >= 2 tokens only when specific enough.
    clean: Dict[str, List[str]] = {}
    for name, vals in aliases.items():
        out = set()
        for v in vals:
            nv = normalize_text(v)
            if len(nv) >= 3:
                out.add(nv)
        clean[name] = sorted(out, key=len, reverse=True)
    return clean


def match_influencer(text: str, aliases: Dict[str, List[str]]) -> str | None:
    nt = normalize_text(text)
    best = None
    best_len = 0
    for name, vals in aliases.items():
        for a in vals:
            if a and a in nt and len(a) > best_len:
                best, best_len = name, len(a)
    return best


def date_windows(now: dt.datetime | None = None) -> Dict[str, Tuple[dt.datetime, dt.datetime]]:
    now = now or dt.datetime.now(TZ)
    today = now.date()
    current_end_date = today - dt.timedelta(days=1)
    current_start_date = current_end_date - dt.timedelta(days=6)
    previous_end_date = current_start_date - dt.timedelta(days=1)
    previous_start_date = previous_end_date - dt.timedelta(days=6)
    def span(a: dt.date, b: dt.date):
        return (dt.datetime.combine(a, dt.time.min, TZ), dt.datetime.combine(b, dt.time.max, TZ))
    return {'current': span(current_start_date, current_end_date), 'previous': span(previous_start_date, previous_end_date)}


def shopify_base(secrets: Dict[str, str]) -> Tuple[str, str]:
    token = secrets.get('SHOPIFY_ACCESS_TOKEN') or secrets.get('SHOPIFY_ADMIN_TOKEN') or secrets.get('SHOPIFY_API_TOKEN')
    store = secrets.get('SHOPIFY_STORE') or secrets.get('SHOPIFY_STORE_URL') or secrets.get('SHOPIFY_SHOP_NAME') or secrets.get('SHOPIFY_STORE_HANDLE')
    if not token or not store:
        raise RuntimeError('missing Shopify credentials')
    store = store.strip()
    if store.startswith('http'):
        host = urlparse(store).netloc
    else:
        host = store
    if '.myshopify.com' not in host:
        host = f'{host}.myshopify.com'
    return host, token


def fetch_shopify_orders(secrets: Dict[str, str], start: dt.datetime, end: dt.datetime) -> List[Dict[str, Any]]:
    host, token = shopify_base(secrets)
    url = f'https://{host}/admin/api/2024-10/orders.json'
    headers = {'X-Shopify-Access-Token': token}
    fields = ','.join([
        'id','name','created_at','total_price','subtotal_price','currency','landing_site','referring_site','source_name',
        'discount_codes','note','note_attributes','tags','line_items','customer','financial_status','cancelled_at'
    ])
    params = {
        'status': 'any',
        'limit': 250,
        'created_at_min': start.astimezone(dt.timezone.utc).isoformat().replace('+00:00','Z'),
        'created_at_max': end.astimezone(dt.timezone.utc).isoformat().replace('+00:00','Z'),
        'fields': fields,
        'order': 'created_at asc',
    }
    out = []
    while True:
        r = requests.get(url, headers=headers, params=params, timeout=60)
        r.raise_for_status()
        out.extend(r.json().get('orders', []))
        link = r.headers.get('Link','')
        m = re.search(r'<([^>]+)>; rel="next"', link)
        if not m:
            break
        url = m.group(1)
        params = None
    return out


def order_evidence_text(o: Dict[str, Any]) -> str:
    chunks = [o.get('landing_site'), o.get('referring_site'), o.get('source_name'), o.get('note'), o.get('tags')]
    for dc in o.get('discount_codes') or []:
        chunks.append(dc.get('code'))
    for na in o.get('note_attributes') or []:
        chunks.append(na.get('name'))
        chunks.append(na.get('value'))
    return ' | '.join(str(c or '') for c in chunks)


def extract_meta_ad_ids_from_order(o: Dict[str, Any]) -> set[str]:
    """Extract exact Meta ad ids from Shopify evidence.

    We only use URL parameters that normally carry the ad/creative id (`utm_content`).
    Campaign/adset ids are intentionally excluded because several influencers can share
    generic campaigns/adsets, which would create false product attribution.
    """
    ids: set[str] = set()
    candidates: List[str] = []
    for field in ['landing_site', 'referring_site']:
        val = str(o.get(field) or '')
        if val:
            candidates.append(val)
    for na in o.get('note_attributes') or []:
        for key in ['value', 'name']:
            val = str(na.get(key) or '')
            if val:
                candidates.append(val)
    for raw in candidates:
        qs_text = raw
        if raw.startswith('/'):
            qs_text = 'https://lk.local' + raw
        try:
            parsed = urlparse(qs_text)
            params = parse_qs(parsed.query)
        except Exception:
            params = {}
        for key in ['utm_content', 'ad_id', 'fb_ad_id']:
            for val in params.get(key, []):
                for m in re.findall(r'\d{12,}', str(val)):
                    ids.add(m)
    return ids


def summarize_shopify(orders: List[Dict[str, Any]], aliases: Dict[str, List[str]], meta_ad_bridge: Dict[str, str] | None = None) -> Dict[str, Any]:
    meta_ad_bridge = meta_ad_bridge or {}
    by = defaultdict(lambda: {'orders':0, 'revenue':0.0, 'bridge_text':0, 'bridge_meta_ad_id':0, 'products':defaultdict(lambda:{'qty':0,'revenue':0.0})})
    unattributed = {'orders':0, 'revenue':0.0}
    ambiguous = {'orders':0, 'revenue':0.0}
    for o in orders:
        if o.get('cancelled_at'):
            continue
        total = parse_num(o.get('total_price'))
        matched_ad_influencers = sorted({meta_ad_bridge[i] for i in extract_meta_ad_ids_from_order(o) if i in meta_ad_bridge}) if meta_ad_bridge else []
        if len(matched_ad_influencers) == 1:
            # Exact Meta ad_id in Shopify UTM is stronger than loose textual matches,
            # which can be polluted by supplier names, internal tags or product copy.
            inf = matched_ad_influencers[0]
            bridge_type = 'meta_ad_id'
        elif len(matched_ad_influencers) > 1:
            ambiguous['orders'] += 1; ambiguous['revenue'] += total
            continue
        else:
            inf = match_influencer(order_evidence_text(o), aliases)
            bridge_type = 'text' if inf else None
        if not inf:
            unattributed['orders'] += 1; unattributed['revenue'] += total
            continue
        by[inf]['orders'] += 1; by[inf]['revenue'] += total
        if bridge_type == 'meta_ad_id':
            by[inf]['bridge_meta_ad_id'] += 1
        else:
            by[inf]['bridge_text'] += 1
        for li in o.get('line_items') or []:
            title = li.get('title') or li.get('name') or 'Produto sem nome'
            sku = li.get('sku') or 'SKU vazio'
            variant = li.get('variant_title') or ''
            key = f'{title} / SKU {sku}' + (f' / {variant}' if variant and variant not in title else '')
            qty = int(parse_num(li.get('quantity')))
            by[inf]['products'][key]['qty'] += qty
            by[inf]['products'][key]['revenue'] += parse_num(li.get('price')) * qty
    # convert products
    ret = {}
    for inf, d in by.items():
        products = sorted(d['products'].items(), key=lambda kv: (kv[1]['qty'], kv[1]['revenue']), reverse=True)[:8]
        ret[inf] = {
            'orders': d['orders'],
            'revenue': d['revenue'],
            'bridge_text': d.get('bridge_text', 0),
            'bridge_meta_ad_id': d.get('bridge_meta_ad_id', 0),
            'products': [{'product':k, **v} for k,v in products],
        }
    return {'by_influencer':ret, 'unattributed':unattributed, 'ambiguous': ambiguous, 'total_orders':len(orders), 'total_revenue':sum(parse_num(o.get('total_price')) for o in orders if not o.get('cancelled_at'))}


def safe_image_url(raw: Any) -> str | None:
    url = str(raw or '').strip()
    if not url.startswith('http'):
        return None
    try:
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
    except Exception:
        return None
    blocked = {'access_token', 'appsecret_proof', 'client_secret'}
    if any(k.lower() in blocked for k in params):
        return None
    return url


def fetch_meta_creatives(token: str, top_ads: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    """Fetch safe public creative thumbnails for top Meta ads.

    Never persist URLs carrying access_token/appsecret_proof/client_secret.
    Missing images are acceptable; the report must keep running.
    """
    out: Dict[str, Dict[str, Any]] = {}
    for ad in top_ads[:16]:
        ad_id = str(ad.get('ad_id') or '')
        if not ad_id or ad_id in out:
            continue
        try:
            r = requests.get(
                f'https://graph.facebook.com/v20.0/{ad_id}',
                params={'access_token': token, 'fields': 'creative{thumbnail_url,image_url}'},
                timeout=45,
            )
            if r.status_code != 200:
                continue
            creative = (r.json().get('creative') or {})
            image_url = safe_image_url(creative.get('image_url')) or safe_image_url(creative.get('thumbnail_url'))
            if image_url:
                out[ad_id] = {'image_url': image_url}
        except Exception:
            continue
    return out


def fetch_meta(secrets: Dict[str, str], start: dt.datetime, end: dt.datetime, aliases: Dict[str, List[str]], include_creatives: bool = False) -> Dict[str, Any]:
    token = secrets.get('META_ACCESS_TOKEN')
    account = secrets.get('META_ADS_ACCOUNT_ID') or META_ACCOUNT_FALLBACK
    if not account.startswith('act_'):
        account = 'act_' + account
    if not token:
        raise RuntimeError('missing META_ACCESS_TOKEN')
    url = f'https://graph.facebook.com/v20.0/{account}/insights'
    fields = 'campaign_id,adset_id,ad_id,campaign_name,adset_name,ad_name,spend,clicks,impressions,actions,action_values'
    params = {
        'access_token': token,
        'level': 'ad',
        'fields': fields,
        'time_range': json.dumps({'since': start.date().isoformat(), 'until': end.date().isoformat()}),
        'limit': 500,
    }
    rows = []
    while True:
        r = requests.get(url, params=params, timeout=90)
        r.raise_for_status()
        j = r.json(); rows.extend(j.get('data', []))
        nxt = j.get('paging', {}).get('next')
        if not nxt:
            break
        url = nxt; params = None
    by = defaultdict(lambda: {'spend':0.0,'clicks':0,'impressions':0,'purchases':0.0,'value':0.0,'ads':0,'top_ads':[]})
    ad_id_to_influencer: Dict[str, str] = {}
    creative_candidates: List[Dict[str, Any]] = []
    for row in rows:
        text = ' | '.join([row.get('campaign_name',''), row.get('adset_name',''), row.get('ad_name','')])
        inf = match_influencer(text, aliases)
        if not inf:
            continue
        ad_id = row.get('ad_id')
        if ad_id:
            ad_id_to_influencer[str(ad_id)] = inf
        purchases, _ = canonical_metric(row.get('actions') or [])
        value, _ = canonical_metric(row.get('action_values') or [])
        ad_summary = {
            'influencer': inf,
            'ad_id': str(ad_id or ''),
            'campaign_name': row.get('campaign_name') or '',
            'adset_name': row.get('adset_name') or '',
            'ad_name': row.get('ad_name') or '',
            'spend': parse_num(row.get('spend')),
            'clicks': int(parse_num(row.get('clicks'))),
            'impressions': int(parse_num(row.get('impressions'))),
            'purchases': purchases,
            'value': value,
        }
        d = by[inf]
        d['spend'] += ad_summary['spend']
        d['clicks'] += ad_summary['clicks']
        d['impressions'] += ad_summary['impressions']
        d['purchases'] += purchases
        d['value'] += value
        d['ads'] += 1
        d['top_ads'].append(ad_summary)
        if ad_summary['ad_id']:
            creative_candidates.append(ad_summary)
    for d in by.values():
        d['top_ads'] = sorted(d['top_ads'], key=lambda a: (a['purchases'], a['value'], a['spend']), reverse=True)[:3]
    top_ads = sorted(creative_candidates, key=lambda a: (a['purchases'], a['value'], a['spend']), reverse=True)[:12]
    creative_map = fetch_meta_creatives(token, top_ads) if include_creatives else {}
    for ad in top_ads:
        ad.update(creative_map.get(ad.get('ad_id') or '', {}))
    return {'by_influencer':dict(by), 'rows':len(rows), 'account':account, 'ad_id_to_influencer': ad_id_to_influencer, 'top_creatives': top_ads}


def merge_report(meta_cur, meta_prev, shop_cur, shop_prev, windows) -> Dict[str, Any]:
    names = set(meta_cur['by_influencer']) | set(meta_prev['by_influencer']) | set(shop_cur['by_influencer']) | set(shop_prev['by_influencer'])
    rows = []
    for name in sorted(names):
        mc = meta_cur['by_influencer'].get(name, {})
        mp = meta_prev['by_influencer'].get(name, {})
        sc = shop_cur['by_influencer'].get(name, {})
        sp = shop_prev['by_influencer'].get(name, {})
        rows.append({
            'influencer': name,
            'meta_spend': mc.get('spend',0.0), 'meta_spend_prev': mp.get('spend',0.0),
            'meta_purchases': mc.get('purchases',0.0), 'meta_purchases_prev': mp.get('purchases',0.0),
            'meta_value': mc.get('value',0.0), 'meta_value_prev': mp.get('value',0.0),
            'meta_clicks': mc.get('clicks',0), 'meta_clicks_prev': mp.get('clicks',0),
            'shopify_orders': sc.get('orders',0), 'shopify_orders_prev': sp.get('orders',0),
            'shopify_revenue': sc.get('revenue',0.0), 'shopify_revenue_prev': sp.get('revenue',0.0),
            'bridge_text': sc.get('bridge_text',0), 'bridge_meta_ad_id': sc.get('bridge_meta_ad_id',0),
            'products': sc.get('products',[]),
        })
    rows.sort(key=lambda r: (r['shopify_revenue'], r['meta_purchases'], r['meta_spend']), reverse=True)
    return {'windows': windows, 'rows': rows, 'meta': {'current': meta_cur, 'previous': meta_prev}, 'shopify': {'current': shop_cur, 'previous': shop_prev}}


def render_md(rep: Dict[str, Any]) -> str:
    cur = rep['windows']['current']; prev = rep['windows']['previous']
    lines = []
    lines.append('# LK — Relatório semanal de vendas por influencer')
    lines.append('')
    lines.append(f"Janela atual: {cur[0].date()} a {cur[1].date()} (BRT)")
    lines.append(f"Comparativo: {prev[0].date()} a {prev[1].date()} (BRT)")
    lines.append('')
    lines.append('Metodologia: Meta Ads direto por `campaign_name`/`adset_name`/`ad_name`, compra canônica por anúncio; Shopify/produtos atribuídos somente quando há ponte textual ou `ad_id` Meta exato em `utm_content`/`ad_id`. Campanha/adset genérico não é usado como ponte.')
    lines.append('')
    for r in rep['rows'][:20]:
        lines.append(f"## {r['influencer']}")
        lines.append(f"- Shopify com ponte: {r['shopify_orders']} pedidos / {money(r['shopify_revenue'])} ({pct_change(r['shopify_revenue'], r['shopify_revenue_prev'])} vs semana anterior; {r.get('bridge_text',0)} texto + {r.get('bridge_meta_ad_id',0)} ad_id Meta)")
        lines.append(f"- Meta: {r['meta_purchases']:.0f} compras canônicas / spend {money(r['meta_spend'])} / valor Meta {money(r['meta_value'])}")
        if r['products']:
            lines.append('- Produtos com ponte Shopify:')
            for p in r['products'][:5]:
                lines.append(f"  - {p['product']}: qty {p['qty']} / {money(p['revenue'])}")
        else:
            lines.append('- Produtos: sem ponte Shopify textual encontrada nesta semana.')
        lines.append('')
    return '\n'.join(lines)


def render_html(rep: Dict[str, Any]) -> str:
    cur = rep['windows']['current']; prev = rep['windows']['previous']
    css = """
    body{font-family:Inter,Arial,sans-serif;background:#f7f4ef;color:#161616;margin:0;padding:24px}.wrap{max-width:900px;margin:auto;background:#fff;border-radius:18px;padding:26px;border:1px solid #e7ded2}.muted{color:#71675d}.card{border:1px solid #eee0d3;border-radius:14px;padding:16px;margin:16px 0}.name{font-size:22px;font-weight:800}.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin-top:12px}.kv{background:#faf7f2;border-radius:10px;padding:10px}.k{font-size:11px;color:#7d7166;text-transform:uppercase;letter-spacing:.06em}.v{font-size:18px;font-weight:800}.up{color:#0f7a3b}.down{color:#b42318}.prod{font-size:14px;line-height:1.45}.creative-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin:18px 0}.creative{background:#111;color:#fff;border-radius:16px;overflow:hidden}.creative img{width:100%;aspect-ratio:9/16;object-fit:cover;display:block;background:#222}.creative .caption{padding:10px;font-size:13px;line-height:1.35}.creative .metric{color:#f2d6a2;font-weight:800}.creative .muted{color:#c8c1b8}@media(max-width:650px){.grid{grid-template-columns:1fr}.creative-grid{grid-template-columns:1fr 1fr}body{padding:10px}.wrap{padding:16px}}
    """
    parts = [f'<!doctype html><meta charset="utf-8"><style>{css}</style><div class="wrap">']
    parts.append('<h1>LK — Relatório semanal de vendas por influencer</h1>')
    parts.append(f'<p class="muted"><b>Atual:</b> {cur[0].date()} a {cur[1].date()} BRT<br><b>Comparativo:</b> {prev[0].date()} a {prev[1].date()} BRT</p>')
    parts.append('<p class="muted">Meta Ads direto com compra canônica por anúncio. Shopify/produtos entram quando há ponte textual ou ad_id Meta exato em utm_content/ad_id. Campanha/adset genérico não é usado como ponte.</p>')
    creatives = [c for c in rep.get('meta', {}).get('current', {}).get('top_creatives', []) if c.get('image_url')]
    if creatives:
        parts.append('<h2>Top criativos Meta da semana</h2>')
        parts.append('<p class="muted">Preview vertical/mobile dos anúncios com mais compras canônicas. Métrica Meta é sinal de plataforma; produtos só aparecem abaixo quando houver ponte Shopify segura.</p>')
        parts.append('<div class="creative-grid">')
        for c in creatives[:6]:
            parts.append('<div class="creative">')
            parts.append(f'<img src="{html.escape(c["image_url"], quote=True)}" alt="Criativo Meta {html.escape(c.get("influencer", ""), quote=True)}">')
            parts.append('<div class="caption">')
            parts.append(f'<div><b>{html.escape(c.get("influencer", ""))}</b></div>')
            parts.append(f'<div class="metric">{parse_num(c.get("purchases")):.0f} compras / {money(parse_num(c.get("spend")))} spend</div>')
            parts.append(f'<div class="muted">{html.escape((c.get("ad_name") or c.get("adset_name") or "")[:90])}</div>')
            parts.append('</div></div>')
        parts.append('</div>')
    for r in rep['rows'][:20]:

        cls = 'up' if r['shopify_revenue'] >= r['shopify_revenue_prev'] else 'down'
        parts.append('<div class="card">')
        parts.append(f'<div class="name">{html.escape(r["influencer"])}</div>')
        parts.append('<div class="grid">')
        parts.append(f'<div class="kv"><div class="k">Shopify com ponte</div><div class="v">{r["shopify_orders"]} pedidos / {money(r["shopify_revenue"])}</div><div class="{cls}">{pct_change(r["shopify_revenue"], r["shopify_revenue_prev"])} vs semana ant.</div><div class="muted">Ponte: {r.get("bridge_text",0)} texto + {r.get("bridge_meta_ad_id",0)} ad_id Meta</div></div>')
        parts.append(f'<div class="kv"><div class="k">Meta canônico</div><div class="v">{r["meta_purchases"]:.0f} compras / {money(r["meta_spend"])} spend</div><div class="muted">Valor Meta: {money(r["meta_value"])}</div></div>')
        parts.append('</div>')
        if r['products']:
            parts.append('<div class="prod"><b>Produtos com ponte Shopify:</b><ul>')
            for p in r['products'][:6]:
                parts.append(f'<li>{html.escape(p["product"])} — qty {p["qty"]} / {money(p["revenue"])}</li>')
            parts.append('</ul></div>')
        else:
            parts.append('<p class="muted">Produtos: sem ponte Shopify textual encontrada nesta semana.</p>')
        parts.append('</div>')
    parts.append('</div>')
    return '\n'.join(parts)


def send_gmail(secrets: Dict[str,str], to_addr: str, subject: str, html_body: str, text_body: str) -> Dict[str, Any]:
    credential_sets = [
        ('personal', 'GMAIL_CLIENT_ID', 'GMAIL_CLIENT_SECRET', 'GMAIL_REFRESH_TOKEN_PERSONAL'),
        ('default', 'GMAIL_CLIENT_ID', 'GMAIL_CLIENT_SECRET', 'GMAIL_REFRESH_TOKEN'),
        ('lucas', 'GMAIL_LUCAS_CLIENT_ID', 'GMAIL_LUCAS_CLIENT_SECRET', 'GMAIL_LUCAS_REFRESH_TOKEN'),
        ('lucas_oauth', 'GMAIL_LUCAS_OAUTH_CLIENT_ID', 'GMAIL_LUCAS_OAUTH_CLIENT_SECRET', 'GMAIL_LUCAS_REFRESH_TOKEN'),
        ('producao', 'GMAIL_CLIENT_ID_PRODUCAO', 'GMAIL_CLIENT_SECRET_PRODUCAO', 'GMAIL_REFRESH_TOKEN_PRODUCAO'),
    ]
    from_addr = secrets.get('GMAIL_USER') or to_addr
    if not from_addr:
        raise RuntimeError('missing Gmail sender')
    access = None
    used_label = None
    last_error = None
    for label, ci_key, cs_key, rf_key in credential_sets:
        client_id = secrets.get(ci_key)
        client_secret = secrets.get(cs_key)
        refresh = secrets.get(rf_key)
        if not (client_id and client_secret and refresh):
            continue
        tok = requests.post('https://oauth2.googleapis.com/token', data={
            'client_id': client_id, 'client_secret': client_secret, 'refresh_token': refresh, 'grant_type': 'refresh_token'
        }, timeout=60)
        if tok.status_code == 200:
            access = tok.json()['access_token']
            used_label = label
            break
        try:
            last_error = tok.json().get('error')
        except Exception:
            last_error = f'http_{tok.status_code}'
    if not access:
        raise RuntimeError(f'no valid Gmail OAuth credential set; last_error={last_error}')
    msg = MIMEText(html_body, 'html', 'utf-8')
    msg['To'] = to_addr
    msg['From'] = from_addr
    msg['Subject'] = subject
    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode().rstrip('=')
    r = requests.post('https://gmail.googleapis.com/gmail/v1/users/me/messages/send', headers={'Authorization': f'Bearer {access}'}, json={'raw': raw}, timeout=60)
    r.raise_for_status()
    return {**r.json(), 'credential_label': used_label}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--send', action='store_true')
    ap.add_argument('--to', default=None)
    ap.add_argument('--out-dir', default=str(OUT_DIR))
    args = ap.parse_args()
    secrets = load_secrets()
    aliases = load_aliases()
    windows = date_windows()
    outdir = Path(args.out_dir); outdir.mkdir(parents=True, exist_ok=True)
    meta_cur = fetch_meta(secrets, *windows['current'], aliases, include_creatives=True)
    meta_prev = fetch_meta(secrets, *windows['previous'], aliases)
    shop_orders_cur = fetch_shopify_orders(secrets, *windows['current'])
    shop_orders_prev = fetch_shopify_orders(secrets, *windows['previous'])
    shop_cur = summarize_shopify(shop_orders_cur, aliases, meta_cur.get('ad_id_to_influencer'))
    shop_prev = summarize_shopify(shop_orders_prev, aliases, meta_prev.get('ad_id_to_influencer'))
    rep = merge_report(meta_cur, meta_prev, shop_cur, shop_prev, windows)
    slug = windows['current'][1].date().isoformat()
    md = render_md(rep); html_body = render_html(rep)
    md_path = outdir / f'lk-weekly-influencer-sales-{slug}.md'
    html_path = outdir / f'lk-weekly-influencer-sales-{slug}.html'
    json_path = outdir / f'lk-weekly-influencer-sales-{slug}.json'
    serial = json.loads(json.dumps(rep, default=str, ensure_ascii=False))
    md_path.write_text(md, encoding='utf-8')
    html_path.write_text(html_body, encoding='utf-8')
    json_path.write_text(json.dumps(serial, ensure_ascii=False, indent=2), encoding='utf-8')
    sent = None
    if args.send:
        to_addr = args.to or secrets.get('GMAIL_USER')
        if not to_addr:
            raise RuntimeError('missing recipient; pass --to or set GMAIL_USER')
        subject = f'LK — Vendas Influencers semanal ({windows["current"][0].date()} a {windows["current"][1].date()})'
        sent = send_gmail(secrets, to_addr, subject, html_body, md)
    print(json.dumps({
        'ok': True,
        'sent': bool(sent),
        'gmail_message_id': sent.get('id') if sent else None,
        'report_md': str(md_path),
        'report_html': str(html_path),
        'report_json': str(json_path),
        'current_window': [windows['current'][0].isoformat(), windows['current'][1].isoformat()],
        'previous_window': [windows['previous'][0].isoformat(), windows['previous'][1].isoformat()],
        'influencer_rows': len(rep['rows']),
    }, ensure_ascii=False))

if __name__ == '__main__':
    main()
