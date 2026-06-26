#!/usr/bin/env python3
from __future__ import annotations
import importlib.util, json, pathlib, re, time
from collections import Counter
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
w4_path = ROOT / 'scripts/lk_gmc_p1_attribute_wave4_aggressive_nonprice_executor_20260513.py'
spec = importlib.util.spec_from_file_location('w4_baseline', w4_path)
w = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(w)
audit = w.import_audit()
secrets = audit.load_doppler()
mid = secrets.get('MERCHANT_CENTER_ID_LK')
token = audit.google_access_token(audit.parse_service_account(secrets))
products = w.list_all('products', mid, token)
statuses = w.list_all('productstatuses', mid, token)
issue_counts = Counter()
required_attr_counts = Counter()
required_rows = 0
for st in statuses:
    for issue in st.get('itemLevelIssues') or []:
        issue_counts[issue.get('code') or 'unknown'] += 1
    try:
        req = w.required_attrs(st)
    except Exception:
        req = []
    if req:
        required_rows += 1
        for a in req:
            required_attr_counts[a] += 1

def attrs(p):
    return p.get('productAttributes') or p.get('attributes') or {}

def pid(p):
    return p.get('id') or p.get('productId') or p.get('name', '').split('/')[-1]

def offer(id_):
    return id_.split(':')[-1]

def title_flags(t):
    t = (t or '').strip()
    flags = []
    if not t:
        flags.append('empty_title')
    if re.fullmatch(r'[0-9]{1,3}', t):
        flags.append('numeric_only_title')
    if len(t) < 12:
        flags.append('very_short_title')
    if len(t) > 150:
        flags.append('over_150_chars')
    if t.upper() == t and len(t) > 10:
        flags.append('all_caps')
    if any(x in t.lower() for x in ['frete', 'promo', 'desconto', 'black friday']):
        flags.append('promo_word')
    return flags

def guess_category(title):
    s = (title or '').lower()
    if any(x in s for x in ['tênis', 'tenis', 'sneaker', 'sapat', 'handball', 'samba', 'gazelle', 'jordan', 'air force', 'dunk', 'yeezy', 'new balance', 'adidas', 'nike']):
        return ('Apparel & Accessories > Shoes', 'Tênis', 'shoe_token')
    if any(x in s for x in ['camiseta', 't-shirt', 'shirt', 'tee ']):
        return ('Apparel & Accessories > Clothing > Shirts & Tops', 'Camiseta', 'shirt_token')
    if any(x in s for x in ['shorts', 'bermuda']):
        return ('Apparel & Accessories > Clothing > Shorts', 'Shorts', 'shorts_token')
    if any(x in s for x in ['moletom', 'hoodie', 'jaqueta', 'jacket']):
        return ('Apparel & Accessories > Clothing > Outerwear', 'Moletom/Jaqueta', 'outerwear_token')
    if any(x in s for x in ['boné', 'bone', 'cap ']):
        return ('Apparel & Accessories > Clothing Accessories > Hats', 'Boné', 'hat_token')
    if any(x in s for x in ['bolsa', 'bag', 'shoulder', 'wallet', 'carteira']):
        return ('Luggage & Bags > Handbags, Wallets & Cases', 'Bolsa/Carteira', 'bag_token')
    return (None, None, None)

title_issue_records = []
p2a_candidates = []
p2c_size_candidates = []
buckets = Counter()
for p in products:
    id_ = pid(p)
    at = attrs(p)
    t = at.get('title') or p.get('title') or ''
    gpc = at.get('googleProductCategory')
    pts = at.get('productTypes') or []
    sizes = at.get('sizes') or at.get('size') or []
    fl = title_flags(t)
    if fl:
        title_issue_records.append({'product_id': id_, 'offer_id': offer(id_), 'title': t, 'flags': fl, 'gpc': gpc, 'productTypes': pts})
        for f in fl:
            buckets[f] += 1
    sgpc, spt, evid = guess_category(t)
    if sgpc and (not gpc or not pts):
        p2a_candidates.append({'product_id': id_, 'offer_id': offer(id_), 'title': t, 'current_googleProductCategory': gpc, 'current_productTypes': pts, 'suggested_googleProductCategory': sgpc, 'suggested_productTypes': [spt], 'evidence': evid})
    is_shoe = bool((gpc and ('Sapatos' in gpc or gpc == 'Apparel & Accessories > Shoes')) or (pts and any('Tênis' in str(x) for x in pts)))
    if is_shoe:
        has_num_in_title = bool(re.search(r'\b(3[3-9]|4[0-9]|OS|Único|Unico)\b', t, re.I))
        sz = sizes if isinstance(sizes, list) else ([sizes] if sizes else [])
        if sz and not has_num_in_title:
            p2c_size_candidates.append({'product_id': id_, 'offer_id': offer(id_), 'title': t, 'current_sizes': sz[:3], 'suggested_title': (t + ' - Tam. ' + str(sz[0]))[:150], 'evidence': 'merchant_sizes_attr_title_lacks_size'})
summary = {
    'generated_at': datetime.now(timezone.utc).isoformat(),
    'mode': 'read_only_baseline',
    'products_total': len(products),
    'productstatuses_total': len(statuses),
    'required_attr_rows': required_rows,
    'required_attr_counts': dict(required_attr_counts.most_common()),
    'top_item_level_issue_counts': dict(issue_counts.most_common(20)),
    'title_issue_counts': dict(buckets.most_common()),
    'p2a_missing_category_or_product_type_candidates': len(p2a_candidates),
    'p2c_size_title_candidates': len(p2c_size_candidates),
    'title_issue_sample': title_issue_records[:50],
    'p2a_candidates_sample': p2a_candidates[:50],
    'p2c_size_candidates_sample': p2c_size_candidates[:50],
    'not_performed': ['merchant_write', 'shopify_write', 'tiny_write', 'price_update', 'availability_update', 'title_update', 'category_update', 'feed_fetch_or_upload', 'campaign_or_message_send'],
}
json_path = ROOT / 'reports/lk-gmc-2026-05-13-next-improvement-readonly-baseline.json'
md_path = ROOT / 'reports/lk-gmc-2026-05-13-next-improvement-readonly-baseline.md'
json_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
lines = [
    '# LK GMC Next Improvement — Read-only baseline',
    '',
    f"Generated: {summary['generated_at']}",
    '',
    '## Summary',
    f"- Products: {len(products)}",
    f"- Productstatuses: {len(statuses)}",
    f"- Required attr rows: {required_rows}",
    f"- Required attr counts: {summary['required_attr_counts']}",
    f"- Top item issues: {summary['top_item_level_issue_counts']}",
    f"- Title issue counts: {summary['title_issue_counts']}",
    f"- P2A missing category/product_type candidates: {len(p2a_candidates)}",
    f"- P2C size-title candidates: {len(p2c_size_candidates)}",
    '',
    '## Not performed',
]
lines += [f'- {x}' for x in summary['not_performed']]
md_path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(json.dumps({'status': 'read_only_baseline_ready', 'products': len(products), 'productstatuses': len(statuses), 'required_attr_rows': required_rows, 'required_attr_counts': summary['required_attr_counts'], 'top_item_issues': dict(issue_counts.most_common(8)), 'title_issue_counts': summary['title_issue_counts'], 'p2a_candidates': len(p2a_candidates), 'p2c_size_candidates': len(p2c_size_candidates), 'report': str(md_path)}, ensure_ascii=False, indent=2))
