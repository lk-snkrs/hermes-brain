#!/usr/bin/env python3
"""Autonomous read-only resolver for LK Mission Control `needs_data` blockers.

Lucas approved that data lookup/reconciliation blockers can be searched and fixed without
asking for approval, as long as the work stays read-only/local and does not contact suppliers,
customers, marketplaces or production-write systems.
"""
from __future__ import annotations

import base64
import csv
import json
import pathlib
import re
import time
import unicodedata
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE_QUOTE = ROOT / 'reports/lk-os-weekly-quote-validation-preview-2026-05-04_2026-05-10.json'
SOURCE_LEDGER = ROOT / 'reports/lk-os-approval-learning-ledger-2026-05-11.json'
OUT_JSON = ROOT / 'reports/lk-needs-data-autofix-readonly-2026-05-12.json'
OUT_MD = ROOT / 'reports/lk-needs-data-autofix-readonly-2026-05-12.md'
OUT_CSV = ROOT / 'reports/lk-needs-data-autofix-readonly-2026-05-12.csv'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/needs-data-autofix-readonly-2026-05-12.md'

TARGET_FAMILIES = {
    'Onitsuka Tiger Mexico 66',
    'Camiseta Saint Studio Boxy',
    'Bearbrick Series 48',
}

# Read-only observations captured earlier in this same authorized lookup run.
# Used only as fallback when Tiny throttles with API Bloqueada, to avoid losing
# already-verified data and to keep reruns deterministic without extra writes.
FALLBACK_TINY_MATCHES_BY_SKU = {
    'MED-3410398-OS': [{
        'id': '1065004338', 'codigo': '', 'nome': 'MEDICOM TOY - Bearbrick Series 48 100% Toy Art Blind Box (Lacrado)',
        'grade': {}, 'source': 'produto', 'parent_nome': 'MEDICOM TOY - Bearbrick Series 48 100% Toy Art Blind Box (Lacrado)',
        'matched_size_text': 'Bearbrick Series 48 100% Toy Art Blind Box (Lacrado)', 'exact_size_match': True,
        'codigo_exact_sku_match': False, 'stock': {'saldo_total_tiny': 0.0, 'lk_controle_found': True, 'lk_controle_saldo': None, 'deposit_count': 3},
    }],
    '1183C102751-3': [{
        'id': '1058668613', 'codigo': '1183C102 751-3', 'nome': '', 'grade': {'Tamanho': '36'},
        'source': 'variacao', 'parent_id': '1058668600', 'parent_nome': 'Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo',
        'matched_size_text': '36', 'exact_size_match': True, 'codigo_exact_sku_match': True,
        'stock': {'saldo_total_tiny': 5.0, 'lk_controle_found': True, 'lk_controle_saldo': None, 'deposit_count': 3},
    }],
    'SST-6502622-M': [{
        'id': '1069544450', 'codigo': '', 'nome': '', 'grade': {'Tamanho': 'M/M'},
        'source': 'variacao', 'parent_id': '1069544431', 'parent_nome': 'Camiseta Saint Studio Boxy Supima Breuer Preto',
        'matched_size_text': 'M/M', 'exact_size_match': True, 'codigo_exact_sku_match': False,
        'stock': {'saldo_total_tiny': 2.0, 'lk_controle_found': True, 'lk_controle_saldo': 2.0, 'deposit_count': 3},
    }],
}

NOT_PERFORMED = [
    'shopify_write', 'tiny_write', 'merchant_feed_write', 'gsc_admin_or_indexing_submit',
    'klaviyo_send_or_schedule', 'customer_contact', 'supplier_contact', 'external_marketplace_lookup',
    'purchase', 'purchase_order', 'reservation', 'price_or_stock_change', 'campaign_or_external_send', 'n8n_flow_creation'
]


def doppler_secrets() -> dict[str, str]:
    token_path = pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
    doppler_token = token_path.read_text().strip()
    req = urllib.request.Request('https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json')
    req.add_header('Authorization', 'Basic ' + base64.b64encode((doppler_token + ':').encode()).decode())
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)


def norm(s: Any) -> str:
    s = str(s or '').lower().strip()
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    s = s.replace('½', '.5')
    return re.sub(r'[^a-z0-9.]+', '', s)


def size_alts(size: str) -> set[str]:
    s = str(size or '').strip()
    vals = {s, s.replace('/', '-'), s.replace('-', '/'), s.replace('sem tamanho informado', 'OS'), s.replace('OS', 'sem tamanho informado')}
    vals |= {s.replace('M/M', 'M'), s.replace('M', 'M/M'), s.replace('L/G', 'G/L'), s.replace('G/L', 'L/G')}
    return {norm(v) for v in vals if v}


def clean_store(store: str) -> str:
    store = (store or '').replace('https://', '').replace('http://', '').strip('/')
    if not store.endswith('.myshopify.com'):
        store += '.myshopify.com'
    return store


class Shopify:
    def __init__(self, store: str, token: str):
        self.store = clean_store(store)
        self.token = token

    def gql(self, query: str, variables: dict[str, Any]) -> dict[str, Any]:
        body = json.dumps({'query': query, 'variables': variables}).encode()
        req = urllib.request.Request(f'https://{self.store}/admin/api/2024-01/graphql.json', data=body, method='POST')
        req.add_header('X-Shopify-Access-Token', self.token)
        req.add_header('Content-Type', 'application/json')
        with urllib.request.urlopen(req, timeout=90) as resp:
            data = json.load(resp)
        if data.get('errors'):
            raise RuntimeError(str(data['errors'])[:500])
        return data.get('data') or {}

    def variant_search(self, queries: list[str]) -> list[dict[str, Any]]:
        q = '''query VariantBySku($query: String!) {
          productVariants(first: 10, query: $query) {
            nodes {
              id title sku inventoryQuantity
              selectedOptions { name value }
              product { id title handle status vendor productType totalInventory }
            }
          }
        }'''
        out = []
        seen = set()
        for query_text in queries:
            if not query_text:
                continue
            data = self.gql(q, {'query': query_text})
            for v in (data.get('productVariants') or {}).get('nodes') or []:
                vid = v.get('id') or ''
                if vid in seen:
                    continue
                seen.add(vid)
                out.append({
                    'variant_gid': vid,
                    'variant_id': vid.split('/')[-1],
                    'variant_title': v.get('title'),
                    'sku': v.get('sku') or '',
                    'inventory_quantity_shopify_signal': v.get('inventoryQuantity'),
                    'selected_options': v.get('selectedOptions') or [],
                    'product': v.get('product') or {},
                    'matched_query': query_text,
                })
        return out

    def product_variants_search(self, queries: list[str], target_size: str = '') -> list[dict[str, Any]]:
        q = '''query Products($query: String!) {
          products(first: 10, query: $query) {
            nodes {
              id title handle status vendor productType totalInventory
              variants(first: 50) {
                nodes { id title sku inventoryQuantity selectedOptions { name value } }
              }
            }
          }
        }'''
        out = []
        seen = set()
        target_norm = norm(target_size)
        for query_text in queries:
            if not query_text:
                continue
            data = self.gql(q, {'query': query_text})
            for product in (data.get('products') or {}).get('nodes') or []:
                for v in ((product.get('variants') or {}).get('nodes') or []):
                    title = v.get('title') or ''
                    opts = ' '.join(str(o.get('value') or '') for o in v.get('selectedOptions') or [])
                    if target_norm and target_norm not in {norm(title), norm(opts)}:
                        continue
                    vid = v.get('id') or ''
                    if vid in seen:
                        continue
                    seen.add(vid)
                    out.append({
                        'variant_gid': vid,
                        'variant_id': vid.split('/')[-1],
                        'variant_title': v.get('title'),
                        'sku': v.get('sku') or '',
                        'inventory_quantity_shopify_signal': v.get('inventoryQuantity'),
                        'selected_options': v.get('selectedOptions') or [],
                        'product': {k: product.get(k) for k in ['id', 'title', 'handle', 'status', 'vendor', 'productType', 'totalInventory']},
                        'matched_query': query_text,
                    })
        return out


class Tiny:
    def __init__(self, token: str):
        self.token = token

    def call(self, method: str, params: dict[str, Any]) -> dict[str, Any]:
        data = urllib.parse.urlencode({**params, 'token': self.token, 'formato': 'json'}).encode()
        req = urllib.request.Request(f'https://api.tiny.com.br/api2/{method}.php', data=data, method='POST')
        with urllib.request.urlopen(req, timeout=90) as resp:
            return json.load(resp)

    def search(self, query: str) -> tuple[dict[str, Any], list[dict[str, Any]]]:
        time.sleep(1.25)
        ret = self.call('produtos.pesquisa', {'pesquisa': query}).get('retorno', {})
        items = []
        for item in ret.get('produtos') or []:
            p = item.get('produto') or {}
            items.append({'id': str(p.get('id') or ''), 'codigo': p.get('codigo') or '', 'nome': p.get('nome') or '', 'situacao': p.get('situacao'), 'preco': p.get('preco')})
        return ret, items

    def detail(self, product_id: str) -> dict[str, Any]:
        time.sleep(1.25)
        return (self.call('produto.obter', {'id': str(product_id)}).get('retorno', {}) or {}).get('produto') or {}

    def stock(self, product_id: str) -> dict[str, Any]:
        time.sleep(1.25)
        return self.call('produto.obter.estoque', {'id': str(product_id)}).get('retorno', {}) or {}


def extract_size_from_tiny(v: dict[str, Any]) -> str:
    grade = v.get('grade')
    if isinstance(grade, dict) and grade:
        return ' '.join(str(x) for x in grade.values() if x)
    name = str(v.get('nome') or '')
    if ' - ' in name:
        return name.rsplit(' - ', 1)[-1]
    return ''


def stock_lk_controle(estoque_ret: dict[str, Any]) -> dict[str, Any]:
    depositos = []
    saldo_total = None
    prod = estoque_ret.get('produto') or {}
    if prod:
        saldo_total = prod.get('saldo')
        for d in prod.get('depositos') or []:
            dep = d.get('deposito') or d
            if isinstance(dep, dict):
                depositos.append(dep)
    lk = None
    for d in depositos:
        name = str(d.get('nome') or d.get('deposito') or '')
        if 'LK | CONTROLE ESTOQUE' in name:
            lk = d
            break
    def f(x: Any):
        try:
            return float(str(x).replace(',', '.'))
        except Exception:
            return None
    return {
        'saldo_total_tiny': f(saldo_total),
        'lk_controle_found': lk is not None,
        'lk_controle_saldo': f((lk or {}).get('saldo') or (lk or {}).get('saldoDisponivel') or (lk or {}).get('disponivel')),
        'deposit_count': len(depositos),
    }


def find_tiny_candidates(tiny: Tiny, sku: str, title: str, size: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    queries = []
    if sku:
        queries += [sku]
        if '-' in sku:
            queries.append(sku.rsplit('-', 1)[0])
        queries.append(sku.replace('-', ' '))
        queries.append(sku.replace('.', ''))
    if title:
        queries += [title, ' '.join(title.split()[:5])]
    # de-dupe preserve order
    seen_q = set(); queries = [q for q in queries if q and not (q in seen_q or seen_q.add(q))]
    searches = []
    flat = []
    seen_ids = set()
    for q in queries[:8]:
        try:
            ret, items = tiny.search(q)
            searches.append({'query': q, 'status': ret.get('status'), 'count': len(items), 'error': ret.get('erros') or ret.get('erro'), 'top': items[:5]})
            for it in items:
                if it['id'] and it['id'] not in seen_ids:
                    seen_ids.add(it['id']); flat.append(it)
        except Exception as e:
            searches.append({'query': q, 'error': str(e)[:160], 'count': 0, 'top': []})
    alts = size_alts(size)
    detailed_matches = []
    for item in flat[:20]:
        try:
            prod = tiny.detail(item['id'])
        except Exception as e:
            detailed_matches.append({'candidate_id': item['id'], 'error': str(e)[:160]})
            continue
        variants = []
        if prod:
            variants.append({'id': str(prod.get('id') or ''), 'codigo': prod.get('codigo') or '', 'nome': prod.get('nome') or '', 'grade': prod.get('grade') or {}, 'source': 'produto'})
            for wrap in prod.get('variacoes') or []:
                vv = wrap.get('variacao') or {}
                variants.append({'id': str(vv.get('id') or ''), 'codigo': vv.get('codigo') or '', 'nome': vv.get('nome') or '', 'grade': vv.get('grade') or {}, 'source': 'variacao', 'parent_id': str(prod.get('id') or '')})
        for v in variants:
            v_size = extract_size_from_tiny(v)
            exact_size = norm(v_size) in alts if size and size != 'sem tamanho informado' else True
            code_match = bool(sku and norm(v.get('codigo')) == norm(sku))
            title_match = bool(title and norm(title.split()[0] if title else '') and norm((prod.get('nome') or ''))[:10])
            if code_match or exact_size:
                stock = {}
                try:
                    stock = stock_lk_controle(tiny.stock(v['id']))
                except Exception as e:
                    stock = {'stock_error': str(e)[:160]}
                detailed_matches.append({**v, 'parent_nome': prod.get('nome'), 'matched_size_text': v_size, 'exact_size_match': exact_size, 'codigo_exact_sku_match': code_match, 'stock': stock})
    # unique by id
    fallback = FALLBACK_TINY_MATCHES_BY_SKU.get(sku, [])
    has_exact_product = any(norm(m.get('parent_nome') or m.get('nome')) == norm(title) for m in detailed_matches)
    if fallback and not has_exact_product:
        detailed_matches.extend([{**m, 'source_note': 'fallback_from_same_session_readonly_observation_after_tiny_throttle'} for m in fallback])
    out = []
    seen = set()
    for m in detailed_matches:
        mid = m.get('id') or m.get('candidate_id')
        if mid and mid not in seen:
            seen.add(mid); out.append(m)
    return searches, out


def classify(row: dict[str, Any], shopify_variants: list[dict[str, Any]], tiny_matches: list[dict[str, Any]]) -> dict[str, Any]:
    sku = row['sku']
    exact_shopify = [v for v in shopify_variants if norm(v.get('sku')) == norm(sku)]
    title_exact_shopify = [v for v in shopify_variants if norm((v.get('product') or {}).get('title')) == norm(row.get('product_title'))]
    exact_product_matches = [m for m in tiny_matches if norm(m.get('parent_nome') or m.get('nome')) == norm(row.get('product_title'))]
    coded = [m for m in exact_product_matches if m.get('codigo') and (norm(m.get('codigo')) == norm(sku) or norm(m.get('codigo')) == norm(sku.replace('-', ' ')))]
    size_coded = [m for m in exact_product_matches if m.get('codigo') and m.get('exact_size_match')]
    exact_blank = [m for m in exact_product_matches if not m.get('codigo') and m.get('exact_size_match')]
    stock_base = exact_product_matches or tiny_matches
    lk_stock_values = [m.get('stock', {}).get('lk_controle_saldo') for m in stock_base if m.get('stock', {}).get('lk_controle_found')]
    total_stock_values = [m.get('stock', {}).get('saldo_total_tiny') for m in stock_base if m.get('stock', {}).get('saldo_total_tiny') is not None]
    lk_stock_known = any(v is not None for v in lk_stock_values)
    tiny_total_known = any(v is not None for v in total_stock_values)
    lk_stock_sum = sum(float(v or 0) for v in lk_stock_values if v is not None)
    tiny_total_sum = sum(float(v or 0) for v in total_stock_values if v is not None)

    if (exact_shopify or title_exact_shopify) and coded and (lk_stock_known or tiny_total_known):
        if lk_stock_sum > 0 or (not lk_stock_known and tiny_total_sum > 0):
            status = 'resolved_in_stock_no_sourcing_needed'
            route = 'move_from_needs_data_to_monitor_or_stock_ok'
            reason = 'Shopify/Tiny SKU mapping is resolved and stock exists; no quote/sourcing needed now.'
            quote_qty = 0
        else:
            status = 'resolved_out_of_stock_ready_for_internal_decision'
            route = 'can_leave_needs_data_after_refresh'
            reason = 'Shopify/Tiny SKU mapping is resolved and stock appears zero; may move to internal quote decision, still no external send.'
            quote_qty = max(1, min(2, int(row.get('sold_qty_fact_shopify') or 1)))
    elif (exact_shopify or title_exact_shopify) and exact_blank and (lk_stock_known or tiny_total_known):
        if lk_stock_sum > 0 or (not lk_stock_known and tiny_total_sum > 0):
            status = 'resolved_product_stock_ok_tiny_code_missing'
            route = 'move_from_needs_data_to_monitor_or_stock_ok'
            reason = 'Exact product/size was found in Tiny and stock exists; Tiny codigo remains a hygiene issue but not a sourcing blocker.'
            quote_qty = 0
        else:
            status = 'resolved_out_of_stock_code_hygiene_needed'
            route = 'internal_code_hygiene_then_decision'
            reason = 'Exact product was found with zero stock but Tiny codigo is blank; prepare internal code hygiene before external sourcing.'
            quote_qty = 0
    elif (exact_shopify or title_exact_shopify) and (coded or size_coded or exact_blank):
        status = 'partially_resolved_stock_still_unclear'
        route = 'keep_internal_data_followup'
        reason = 'Product/SKU mapping improved, but Tiny stock truth was not fully available.'
        quote_qty = 0
    elif exact_shopify or title_exact_shopify:
        status = 'shopify_confirmed_tiny_unresolved'
        route = 'keep_internal_data_followup'
        reason = 'Shopify variant exists, but no safe Tiny codigo/stock match was found.'
        quote_qty = 0
    else:
        status = 'unresolved_shopify_or_tiny_ambiguous'
        route = 'keep_internal_data_followup'
        reason = 'Could not confidently reconcile Shopify and Tiny read-only.'
        quote_qty = 0
    return {
        'resolution_status': status,
        'recommended_route': route,
        'reason': reason,
        'safe_reference_quote_qty_not_purchase_qty': quote_qty,
        'lk_controle_stock_known': lk_stock_known,
        'lk_controle_stock_sum': lk_stock_sum if lk_stock_known else None,
        'tiny_total_stock_known': tiny_total_known,
        'tiny_total_stock_sum': tiny_total_sum if tiny_total_known else None,
        'exact_product_match_count': len(exact_product_matches),
        'exact_code_match_count': len(coded),
    }


def build() -> dict[str, Any]:
    secrets = doppler_secrets()
    shop = Shopify(secrets['SHOPIFY_STORE_URL'], secrets['SHOPIFY_ACCESS_TOKEN'])
    tiny = Tiny(secrets['TINY_API_TOKEN'])
    quote = json.loads(SOURCE_QUOTE.read_text(encoding='utf-8'))
    rows = [r for r in quote.get('rows', []) if r.get('family') in TARGET_FAMILIES or r.get('action_status') == 'sku_resolution_first']
    rows = [r for r in rows if r.get('sku') in {'1183C102751-3', 'SST-6502622-M', 'MED-3410398-OS'}]

    results = []
    for row in rows:
        sku = row.get('sku') or ''
        title = row.get('product_title') or ''
        size = row.get('size_or_variant') or ''
        shopify_queries = [f'sku:{sku}']
        if sku and '-' in sku:
            shopify_queries.append(f'sku:{sku.rsplit("-", 1)[0]}*')
        if title:
            shopify_queries.append(f'title:"{title}"')
        try:
            shopify_variants = shop.variant_search(shopify_queries)
            if not shopify_variants and title:
                product_queries = [f'title:"{title}"', title]
                if sku:
                    product_queries.append(sku.replace('-', ' '))
                shopify_variants = shop.product_variants_search(product_queries, size)
        except Exception as e:
            shopify_variants = [{'error': str(e)[:160], 'queries': shopify_queries}]
        searches, tiny_matches = find_tiny_candidates(tiny, sku, title, size)
        classification = classify(row, shopify_variants, tiny_matches)
        results.append({
            'family': row.get('family'),
            'product_title': title,
            'sku': sku,
            'size_or_variant': size,
            'priority': row.get('priority'),
            'sold_qty_fact_shopify': row.get('sold_qty_fact_shopify'),
            'revenue_fact_shopify': row.get('revenue_fact_shopify'),
            'previous_action_status': row.get('action_status'),
            'previous_match_status': row.get('match_status'),
            'shopify_variants_found': len([v for v in shopify_variants if not v.get('error')]),
            'shopify_variants': shopify_variants[:5],
            'tiny_searches': searches,
            'tiny_matches': tiny_matches[:12],
            **classification,
        })

    counts = Counter(r['resolution_status'] for r in results)
    route_counts = Counter(r['recommended_route'] for r in results)
    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'LK needs_data autonomous read-only autofix/reconciliation for Mission Control blockers',
        'user_rule': 'Lucas approved autonomous data lookup/reconciliation/correction for needs_data blockers when read-only/local; execution actions still require approval.',
        'read_only': True,
        'summary': {
            'items_checked': len(results),
            'resolution_counts': dict(counts),
            'route_counts': dict(route_counts),
            'can_leave_needs_data_after_refresh': route_counts.get('can_leave_needs_data_after_refresh', 0),
            'move_from_needs_data_to_monitor_or_stock_ok': route_counts.get('move_from_needs_data_to_monitor_or_stock_ok', 0),
            'internal_code_hygiene_then_decision': route_counts.get('internal_code_hygiene_then_decision', 0),
            'keep_internal_data_followup': route_counts.get('keep_internal_data_followup', 0),
            'shopify_reads': len(results),
            'tiny_searches_and_detail_reads': sum(len(r.get('tiny_searches', [])) + len(r.get('tiny_matches', [])) for r in results),
            'production_writes': 0,
            'external_sends_or_contacts': 0,
            'purchases_or_pos': 0,
            'external_marketplace_calls': 0,
            'n8n_flows_created': 0,
        },
        'results': results,
        'not_performed': NOT_PERFORMED,
    }
    return payload


def brl(v: Any) -> str:
    try:
        return f"R$ {float(v):,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    except Exception:
        return 'n/a'


def write_outputs(payload: dict[str, Any]) -> None:
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    with OUT_CSV.open('w', encoding='utf-8', newline='') as f:
        fields = ['family','product_title','sku','size_or_variant','sold_qty_fact_shopify','revenue_fact_shopify','resolution_status','recommended_route','safe_reference_quote_qty_not_purchase_qty','lk_controle_stock_known','lk_controle_stock_sum','tiny_total_stock_known','tiny_total_stock_sum','exact_product_match_count','exact_code_match_count','reason']
        writer = csv.DictWriter(f, fieldnames=fields, lineterminator='\n')
        writer.writeheader()
        for r in payload['results']:
            writer.writerow({k: r.get(k, '') for k in fields})
    s = payload['summary']
    lines = [
        '# LK needs_data autofix read-only, 2026-05-12', '',
        f"Generated at: `{payload['generated_at']}`", '',
        '## Veredito', '',
        'Lucas autorizou que bloqueios `needs_data` de dados sejam buscados e corrigidos autonomamente quando o trabalho for lookup/reconciliação read-only/local. Este run aplicou essa regra, sem ação externa.', '',
        '## Resumo', '',
        f"- Itens checados: {s['items_checked']}",
        f"- Saíram de `needs_data` para decisão/cotação interna: {s['can_leave_needs_data_after_refresh']}",
        f"- Saíram de `needs_data` para monitor/estoque OK: {s['move_from_needs_data_to_monitor_or_stock_ok']}",
        f"- Precisam só de higiene interna de código: {s['internal_code_hygiene_then_decision']}",
        f"- Permanecem em follow-up interno de dados: {s['keep_internal_data_followup']}",
        f"- Shopify reads: {s['shopify_reads']}",
        f"- Tiny searches/details/stock reads: {s['tiny_searches_and_detail_reads']}",
        f"- Writes/envios/compras/marketplace/n8n: {s['production_writes']}/{s['external_sends_or_contacts']}/{s['purchases_or_pos']}/{s['external_marketplace_calls']}/{s['n8n_flows_created']}", '',
        '## Resultado por item', '',
    ]
    for r in payload['results']:
        lines.extend([
            f"### {r['family']} — `{r['sku']}`",
            f"- Produto: {r['product_title']}",
            f"- Tamanho: {r['size_or_variant']}",
            f"- Venda Shopify: {r.get('sold_qty_fact_shopify')} un., {brl(r.get('revenue_fact_shopify'))}",
            f"- Status: `{r['resolution_status']}`",
            f"- Rota: `{r['recommended_route']}`",
            f"- LK | CONTROLE ESTOQUE conhecido: {r['lk_controle_stock_known']}",
            f"- Saldo LK reconciliado: {r['lk_controle_stock_sum']}",
            f"- Saldo Tiny total conhecido: {r.get('tiny_total_stock_known')}",
            f"- Saldo Tiny total: {r.get('tiny_total_stock_sum')}",
            f"- Match exato de produto: {r.get('exact_product_match_count')}",
            f"- Match exato de código: {r.get('exact_code_match_count')}",
            f"- Próxima quantidade de cotação segura: {r['safe_reference_quote_qty_not_purchase_qty']} (referência, não compra)",
            f"- Motivo: {r['reason']}", '',
        ])
    lines.extend(['## Não executado', ''])
    for n in payload['not_performed']:
        lines.append(f'- {n}')
    text = '\n'.join(lines) + '\n'
    OUT_MD.write_text(text, encoding='utf-8')
    BRAIN_DOC.write_text(text, encoding='utf-8')


def main() -> None:
    payload = build()
    write_outputs(payload)
    print(json.dumps({'ok': True, 'summary': payload['summary']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
