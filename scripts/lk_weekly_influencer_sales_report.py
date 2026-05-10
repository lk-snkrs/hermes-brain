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
    # Pareto-compatible: keep Maria, Maria Fernanda and Mariah separated.
    'Maria Fernanda': ['maria fernanda'],
    'Mariah': ['mariah'],
    'Maria': ['maria'],
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


def split_product_key(product: Any) -> Dict[str, str]:
    raw = str(product or '')
    m = re.match(r'^(.*?)\s*/\s*SKU\s+(.+?)(?:\s*/\s*(.+))?$', raw)
    if not m:
        return {'name': raw, 'sku': 'SKU não identificado', 'variant': ''}
    name = (m.group(1) or '').strip()
    sku = (m.group(2) or '').strip()
    variant = (m.group(3) or '').strip()
    return {'name': name, 'sku': sku, 'variant': variant}


def build_product_ranking(rep: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Product-first ranking aggregated by influencer + SKU + size.

    This is the operating view Lucas expects. We aggregate title variations for
    the same influencer/SKU/variant so the ranking does not duplicate the same
    sold item because Shopify titles differ by color suffix or legacy naming.
    """
    grouped: Dict[Tuple[str, str, str], Dict[str, Any]] = {}
    for r in rep.get('rows', []):
        products = r.get('products') or []
        if not products:
            continue
        for p in products:
            parts = split_product_key(p.get('product'))
            influencer = str(r.get('influencer') or '')
            key = (influencer, parts['sku'], parts['variant'])
            qty = int(parse_num(p.get('qty')))
            revenue = parse_num(p.get('revenue'))
            if key not in grouped:
                grouped[key] = {
                    'influencer': influencer,
                    'product_name': parts['name'],
                    'sku': parts['sku'],
                    'variant': parts['variant'],
                    'qty': 0,
                    'revenue': 0.0,
                    'shopify_orders': r.get('shopify_orders', 0),
                    'shopify_revenue': parse_num(r.get('shopify_revenue')),
                    'bridge_text': r.get('bridge_text', 0),
                    'bridge_meta_ad_id': r.get('bridge_meta_ad_id', 0),
                    'meta_purchases': parse_num(r.get('meta_purchases')),
                    'meta_spend': parse_num(r.get('meta_spend')),
                    'meta_value': parse_num(r.get('meta_value')),
                    'title_variants': set(),
                }
            row = grouped[key]
            row['qty'] += qty
            row['revenue'] += revenue
            row['title_variants'].add(str(p.get('product') or ''))
            # Prefer the more complete human title, but keep SKU/variant canonical.
            if len(parts['name']) > len(row.get('product_name') or ''):
                row['product_name'] = parts['name']
    out: List[Dict[str, Any]] = []
    for row in grouped.values():
        row['title_variants'] = sorted(row['title_variants'])
        row['product'] = f"{row['product_name']} / SKU {row['sku']}" + (f" / {row['variant']}" if row.get('variant') else '')
        out.append(row)
    out.sort(key=lambda x: (x['revenue'], x['qty'], x['meta_purchases']), reverse=True)
    return out

def render_md(rep: Dict[str, Any]) -> str:
    cur = rep['windows']['current']; prev = rep['windows']['previous']
    product_rows = build_product_ranking(rep)
    lines = []
    lines.append('# LK — Ranking semanal: influencer × produto vendido')
    lines.append('')
    lines.append(f"Janela atual: {cur[0].date()} a {cur[1].date()} (BRT)")
    lines.append(f"Comparativo: {prev[0].date()} a {prev[1].date()} (BRT)")
    lines.append('')
    lines.append('Leitura correta: Shopify é a fonte de venda/produto. Meta é sinal de mídia. Um produto só entra no ranking quando o pedido Shopify tem ponte verificável: cupom/UTM/texto ou `ad_id` Meta exato em `utm_content`/`ad_id`/`fb_ad_id`. `campaign_id`/`adset_id` genérico não é atribuição segura.')
    lines.append('')
    lines.append('## Ranking de produtos vendidos com ponte Shopify')
    lines.append('')
    if product_rows:
        for i, row in enumerate(product_rows[:40], 1):
            lines.append(f"{i}. **{row['influencer']}** — {row['product_name']}")
            lines.append(f"   - SKU/tamanho: {row['sku']}" + (f" / {row['variant']}" if row.get('variant') else ""))
            lines.append(f"   - Vendido Shopify: qty {row['qty']} / {money(row['revenue'])}")
            lines.append(f"   - Ponte: {row['bridge_text']} texto + {row['bridge_meta_ad_id']} ad_id Meta")
            lines.append(f"   - Meta do influencer na semana: {row['meta_purchases']:.0f} compras canônicas / spend {money(row['meta_spend'])}")
    else:
        lines.append('Nenhum produto com ponte Shopify segura nesta janela.')
    lines.append('')
    lines.append('## Influencers com sinal Meta, mas sem produto Shopify atribuível')
    lines.append('')
    for r in rep['rows']:
        if r.get('meta_purchases', 0) > 0 and not r.get('products'):
            lines.append(f"- {r['influencer']}: {r['meta_purchases']:.0f} compras Meta / spend {money(r['meta_spend'])} / valor Meta {money(r['meta_value'])} — `meta_signal_only`, sem ponte Shopify segura.")
    return '\n'.join(lines)


def render_html(rep: Dict[str, Any]) -> str:
    cur = rep['windows']['current']; prev = rep['windows']['previous']
    product_rows = build_product_ranking(rep)
    signal_only = [r for r in rep.get('rows', []) if r.get('meta_purchases', 0) > 0 and not r.get('products')]
    total_products = len(product_rows)
    total_product_revenue = sum(r['revenue'] for r in product_rows)
    total_qty = sum(r['qty'] for r in product_rows)
    css = """
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=DM+Sans:wght@400;500;700&display=swap');
    :root{--ink:#0A0A0A;--ink-soft:#1A1A1A;--paper:#F0ECE8;--paper-soft:#F5F4F2;--surface:#FFFFFF;--bone:#FDF9F5;--line:#E8E6E2;--line-warm:#DDD0C0;--muted:#8A8580;--muted-light:#B5B0A8;--accent:#C8A98A;--accent-soft:#E8D8C4;--serif:'Cormorant Garamond',Georgia,serif;--sans:'DM Sans',Arial,sans-serif}
    *{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);padding:0}.page{max-width:640px;margin:0 auto;background:var(--surface)}.brand-header{background:var(--ink);color:white;text-align:center;padding:28px 28px 24px}.brand-word{font:400 30px/1 var(--serif);letter-spacing:-.04em}.context-bar{background:var(--ink-soft);color:var(--accent-soft);text-align:center;padding:12px 18px;font:700 10px/1.4 var(--sans);letter-spacing:.22em;text-transform:uppercase}.hero{background:var(--bone);padding:54px 28px 42px;text-align:center;border-bottom:1px solid var(--line)}.eyebrow{margin:0;color:var(--muted);font:700 10px/1.3 var(--sans);letter-spacing:.24em;text-transform:uppercase}.rule{width:42px;height:1px;background:var(--line-warm);margin:22px auto}.hero h1{font:400 48px/.95 var(--serif);letter-spacing:-.04em;margin:0}.hero h1 em{display:block;color:var(--accent);font-style:italic}.hero-copy{max-width:520px;margin:20px auto 0;color:var(--muted);font:400 14px/1.75 var(--sans)}.metrics{display:grid;grid-template-columns:repeat(3,1fr);border-bottom:1px solid var(--line);background:var(--paper-soft)}.metric{padding:22px 14px;text-align:center;border-right:1px solid var(--line)}.metric:last-child{border-right:0}.metric .k{font:700 9px/1.2 var(--sans);letter-spacing:.18em;color:var(--muted);text-transform:uppercase}.metric .v{font:400 28px/1 var(--serif);letter-spacing:-.03em;margin-top:8px}.section{padding:42px 26px;border-bottom:1px solid var(--line)}.section-title{font:400 34px/1 var(--serif);letter-spacing:-.03em;margin:0 0 10px}.section-sub{font:400 13px/1.7 var(--sans);color:var(--muted);margin:0 0 24px}.rank-row{display:grid;grid-template-columns:46px minmax(0,1fr);gap:14px;padding:20px 0;border-top:1px solid var(--line)}.badge{background:var(--ink);color:white;height:34px;display:flex;align-items:center;justify-content:center;font:700 10px/1 var(--sans);letter-spacing:.12em}.inf{font:700 10px/1.2 var(--sans);letter-spacing:.2em;text-transform:uppercase;color:var(--muted);margin-bottom:7px}.product{font:400 25px/1.08 var(--serif);letter-spacing:-.018em;margin:0 0 12px}.row-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:8px}.pill{background:var(--paper-soft);padding:11px 12px;border:1px solid var(--line)}.pill .k{font:700 9px/1.2 var(--sans);letter-spacing:.16em;color:var(--muted);text-transform:uppercase}.pill .v{font:700 13px/1.3 var(--sans);margin-top:4px}.bridge{margin-top:10px;color:var(--muted);font:400 12px/1.55 var(--sans)}.signal{padding:16px 0;border-top:1px solid var(--line);display:grid;grid-template-columns:minmax(0,1fr) auto;gap:12px}.signal b{font:700 11px/1.3 var(--sans);letter-spacing:.16em;text-transform:uppercase}.signal span{color:var(--muted);font:400 12px/1.55 var(--sans)}.footer{background:var(--ink);color:white;text-align:center;padding:34px 26px}.footer p{margin:10px auto 0;max-width:480px;color:var(--accent-soft);font:400 13px/1.7 var(--sans)}@media(max-width:520px){.page{max-width:none}.hero{padding:42px 22px 34px}.hero h1{font-size:40px}.metrics{grid-template-columns:1fr}.metric{border-right:0;border-bottom:1px solid var(--line)}.row-grid{grid-template-columns:1fr}.section{padding:34px 22px}.product{font-size:23px}}
    """
    css += """@media(max-width:520px){.hero{padding:42px 22px 34px}.hero h1{font-size:40px}.metrics{grid-template-columns:1fr}.metric{border-right:0;border-bottom:1px solid var(--line)}.metric:last-child{border-bottom:0}.rank-row{grid-template-columns:38px minmax(0,1fr);gap:12px}.row-grid{grid-template-columns:1fr}.section{padding:34px 22px}.section-title{font-size:30px}.product{font-size:25px}.page{max-width:100%}}"""
    parts = [f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><style>{css}</style></head><body><main class="page">']
    parts.append('<header class="brand-header"><div class="brand-word">LK Sneakers</div></header>')
    parts.append('<div class="context-bar">CURADORIA LK · INFLUENCERS · PRODUTO VENDIDO</div>')
    parts.append('<section class="hero"><p class="eyebrow">RELATÓRIO SEMANAL</p><div class="rule"></div><h1>Influencer ×<em>Produto vendido.</em></h1>')
    parts.append(f'<p class="hero-copy">{cur[0].date()} a {cur[1].date()} · Ranking operacional por produto vendido com ponte Shopify segura. Meta entra como sinal de mídia, não como verdade de produto.</p></section>')
    parts.append('<section class="metrics">')
    parts.append(f'<div class="metric"><div class="k">Produtos ranqueados</div><div class="v">{total_products}</div></div>')
    parts.append(f'<div class="metric"><div class="k">Qtd. vendida</div><div class="v">{total_qty}</div></div>')
    parts.append(f'<div class="metric"><div class="k">Receita com ponte</div><div class="v">{money(total_product_revenue)}</div></div>')
    parts.append('</section>')
    parts.append('<section class="section"><h2 class="section-title">Ranking de produtos vendidos</h2>')
    parts.append('<p class="section-sub">Cada linha é uma combinação influencer + produto/SKU/tamanho. Este é o bloco para decisão de estoque, recompra e leitura de fit entre influencer e produto.</p>')
    if product_rows:
        for i, row in enumerate(product_rows[:30], 1):
            parts.append('<article class="rank-row">')
            parts.append(f'<div class="badge">#{i}</div><div>')
            parts.append(f'<div class="inf">{html.escape(str(row["influencer"]))}</div>')
            parts.append(f'<h3 class="product">{html.escape(str(row["product_name"]))}</h3>')
            parts.append(f'<div class="bridge">SKU {html.escape(str(row["sku"]))}' + (f' · Tam. {html.escape(str(row["variant"]))}' if row.get('variant') else '') + '</div>')
            parts.append('<div class="row-grid">')
            parts.append(f'<div class="pill"><div class="k">Vendido Shopify</div><div class="v">qty {row["qty"]} · {money(row["revenue"])}</div></div>')
            parts.append(f'<div class="pill"><div class="k">Meta do influencer</div><div class="v">{row["meta_purchases"]:.0f} compras · {money(row["meta_spend"])} spend</div></div>')
            parts.append('</div>')
            parts.append(f'<div class="bridge">Ponte usada no pedido: {row["bridge_text"]} texto + {row["bridge_meta_ad_id"]} ad_id Meta. Produto só entra aqui porque existe evidência Shopify.</div>')
            parts.append('</div></article>')
    else:
        parts.append('<p class="section-sub">Nenhum produto com ponte Shopify segura nesta janela.</p>')
    parts.append('</section>')
    if signal_only:
        parts.append('<section class="section"><h2 class="section-title">Sinal Meta sem produto</h2>')
        parts.append('<p class="section-sub">Aqui o Meta indica compra/valor, mas o Shopify não trouxe cupom, UTM textual ou ad_id exato suficiente para ligar pedido e produto ao influencer.</p>')
        for r in signal_only[:12]:
            parts.append('<div class="signal">')
            parts.append(f'<div><b>{html.escape(str(r["influencer"]))}</b><br><span>{r["meta_purchases"]:.0f} compras Meta · spend {money(r["meta_spend"])} · valor Meta {money(r["meta_value"])}</span></div>')
            parts.append('<span>meta_signal_only</span></div>')
        parts.append('</section>')
    parts.append('<footer class="footer"><div class="brand-word">LK Sneakers</div><p>Less Noise, More Identity. Relatório read-only: não altera campanhas, Shopify, estoque ou CRM.</p></footer>')
    parts.append('</main></body></html>')
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
    meta_cur = fetch_meta(secrets, *windows['current'], aliases, include_creatives=False)
    meta_prev = fetch_meta(secrets, *windows['previous'], aliases)
    shop_orders_cur = fetch_shopify_orders(secrets, *windows['current'])
    shop_orders_prev = fetch_shopify_orders(secrets, *windows['previous'])
    shop_cur = summarize_shopify(shop_orders_cur, aliases, meta_cur.get('ad_id_to_influencer'))
    shop_prev = summarize_shopify(shop_orders_prev, aliases, meta_prev.get('ad_id_to_influencer'))
    rep = merge_report(meta_cur, meta_prev, shop_cur, shop_prev, windows)
    rep['product_ranking'] = build_product_ranking(rep)
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
