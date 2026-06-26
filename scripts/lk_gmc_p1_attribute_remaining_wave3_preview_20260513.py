#!/usr/bin/env python3
"""Read-only GMC P1 remaining required-attribute Wave3 preview after Onda 2.

No Merchant writes. Fetches fresh Merchant products/productstatuses, joins to the
local Shopify snapshot by exact offer_id/SKU where possible, and classifies
remaining required-attribute diagnostics into safe preview buckets.
"""
from __future__ import annotations

import csv
import importlib.util
import json
import pathlib
import re
import sqlite3
from collections import Counter, defaultdict
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / 'scripts/lk_gmc_catalog_duplication_audit_20260512.py'
LOCAL_DB = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite')
RUN_STAMP = '2026-05-13-p1-attribute-remaining-wave3-preview'
OUT_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
OUT_CSV = ROOT / f'reports/lk-gmc-{RUN_STAMP}.csv'
OUT_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
CONTROL = ROOT / 'areas/lk/projetos/lk-os-implementation-control.md'
INDEX = ROOT / 'empresa/rotinas/_index.md'
REQ_CODES = {'item_missing_required_attribute', 'missing_item_attribute_for_product_type'}
COLOR_WORDS = [
    'preto', 'branco', 'cinza', 'azul', 'verde', 'vermelho', 'rosa', 'roxo', 'amarelo',
    'laranja', 'marrom', 'bege', 'creme', 'off white', 'off-white', 'prata', 'dourado',
    'bordô', 'vinho', 'caramelo', 'taupe', 'areia', 'grafite', 'navy', 'black', 'white',
    'grey', 'gray', 'blue', 'green', 'red', 'pink', 'purple', 'yellow', 'orange', 'brown',
    'cream', 'silver', 'gold'
]
COLOR_MAP = {
    'black': 'Preto', 'white': 'Branco', 'grey': 'Cinza', 'gray': 'Cinza', 'blue': 'Azul',
    'green': 'Verde', 'red': 'Vermelho', 'pink': 'Rosa', 'purple': 'Roxo', 'yellow': 'Amarelo',
    'orange': 'Laranja', 'brown': 'Marrom', 'cream': 'Creme', 'silver': 'Prata', 'gold': 'Dourado',
    'off white': 'Off White', 'off-white': 'Off White'
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def import_audit():
    spec = importlib.util.spec_from_file_location('audit', AUDIT_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def parse_product_id(pid: str) -> dict[str, str]:
    parts = (pid or '').split(':', 3)
    if len(parts) == 4:
        return {'channel': parts[0], 'content_language': parts[1], 'target_country': parts[2], 'offer_id': parts[3]}
    return {'channel': '', 'content_language': '', 'target_country': '', 'offer_id': pid or ''}


def norm_attr(value: Any) -> str:
    return str(value or '').strip().lower().replace('_', ' ')


def required_attrs(status: dict[str, Any] | None) -> set[str]:
    out = set()
    for issue in (status or {}).get('itemLevelIssues') or []:
        if issue.get('code') in REQ_CODES:
            a = norm_attr(issue.get('attributeName'))
            if a:
                out.add(a)
    return out


def norm_list(v: Any) -> list[str]:
    if v is None:
        return []
    if isinstance(v, list):
        return [str(x).strip() for x in v if str(x).strip()]
    t = str(v).strip()
    return [t] if t else []


def title_case_color(s: str) -> str:
    s = COLOR_MAP.get(s.lower(), s)
    return ' '.join(w.capitalize() for w in re.split(r'\s+', s.replace('-', ' ')) if w)


def extract_color_from_tags(tags: Any) -> str | None:
    if not tags:
        return None
    vals = []
    if isinstance(tags, str):
        try:
            vals = json.loads(tags)
        except Exception:
            vals = [t.strip() for t in tags.split(',')]
    elif isinstance(tags, list):
        vals = tags
    for t in vals:
        txt = str(t).strip()
        if txt.lower().startswith('color:'):
            c = txt.split(':', 1)[1].strip()
            return c or None
    return None


def extract_color_from_title(title: str) -> str | None:
    txt = ' ' + re.sub(r'[^\wÀ-ÿ\- ]+', ' ', (title or '').lower()) + ' '
    found = []
    for c in COLOR_WORDS:
        pat = ' ' + c.lower() + ' '
        if pat in txt.replace('-', ' ' if '-' in c else '-') or pat in txt:
            canon = title_case_color(c)
            if canon not in found:
                found.append(canon)
    if not found:
        return None
    # Keep conservative: at most 3 words/colors, because GMC accepts free-text color.
    return ' / '.join(found[:3])


def load_shopify_snapshot() -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    by_sku: dict[str, dict[str, Any]] = {}
    by_variant_id: dict[str, dict[str, Any]] = {}
    if not LOCAL_DB.exists():
        return by_sku, by_variant_id
    con = sqlite3.connect(str(LOCAL_DB))
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    q = """
    select v.sku, v.source_variant_id, v.title as variant_title, v.option1, v.option2, v.option3,
           v.price, v.compare_at_price, v.barcode, v.product_title,
           p.title as product_title2, p.handle, p.vendor, p.product_type, p.status, p.tags,
           p.featured_image_url
      from lk_product_variants v
      left join lk_products p on p.product_id = v.product_id
    """
    for row in cur.execute(q):
        d = dict(row)
        sku = str(d.get('sku') or '').strip()
        svi = str(d.get('source_variant_id') or '').strip()
        if sku:
            by_sku[sku] = d
        if svi:
            by_variant_id[svi] = d
    con.close()
    return by_sku, by_variant_id


def suggestion_for(attrs: set[str], product: dict[str, Any], shop: dict[str, Any] | None) -> tuple[dict[str, Any], dict[str, str], str]:
    suggestions: dict[str, Any] = {}
    evidence: dict[str, str] = {}
    title = (shop or {}).get('product_title') or (shop or {}).get('product_title2') or product.get('title') or ''
    if 'color' in attrs and not product.get('color'):
        color = extract_color_from_tags((shop or {}).get('tags'))
        if color:
            suggestions['color'] = color
            evidence['color'] = 'shopify_tag_color'
        else:
            color = extract_color_from_title(title or product.get('title') or '')
            if color:
                suggestions['color'] = color
                evidence['color'] = 'title_color_token_low_to_medium_confidence'
    if 'size' in attrs and not norm_list(product.get('sizes')):
        size = (shop or {}).get('option1') or (shop or {}).get('variant_title')
        if size and str(size).strip().lower() != 'default title':
            suggestions['sizes'] = [str(size).strip()]
            evidence['sizes'] = 'shopify_variant_option_or_title'
    if 'age group' in attrs and not product.get('ageGroup'):
        suggestions['ageGroup'] = 'adult'
        evidence['ageGroup'] = 'default_review_required'
    if 'gender' in attrs and not product.get('gender'):
        suggestions['gender'] = 'unisex'
        evidence['gender'] = 'default_review_required'
    if 'price' in attrs and not product.get('price'):
        price = (shop or {}).get('price')
        if price:
            suggestions['price'] = {'value': str(price), 'currency': 'BRL'}
            evidence['price'] = 'shopify_variant_price_local_snapshot_review_required'
    # Decision buckets.
    target = set()
    if 'color' in attrs: target.add('color')
    if 'size' in attrs: target.add('sizes')
    if 'age group' in attrs: target.add('ageGroup')
    if 'gender' in attrs: target.add('gender')
    if 'price' in attrs: target.add('price')
    if not suggestions:
        decision = 'blocked_no_safe_suggestion'
    elif set(suggestions) >= target and all(evidence.get(k) == 'shopify_tag_color' for k in ['color'] if k in suggestions) and target <= {'color'}:
        decision = 'candidate_wave3_color_tag_high_confidence'
    elif target <= {'color'} and 'color' in suggestions:
        decision = 'candidate_wave3_color_title_review'
    elif target <= {'sizes', 'ageGroup', 'gender'} and {'sizes', 'ageGroup', 'gender'} & set(suggestions):
        decision = 'candidate_wave3_size_age_gender_review'
    elif 'price' in target:
        decision = 'candidate_wave3_price_review_do_not_apply_without_price_policy'
    else:
        decision = 'candidate_wave3_mixed_review'
    return suggestions, evidence, decision


def main() -> None:
    audit = import_audit()
    secrets = audit.load_doppler()
    merchant_id = secrets.get('MERCHANT_CENTER_ID_LK')
    if not merchant_id:
        raise RuntimeError('missing_merchant_center_id')
    token = audit.google_access_token(audit.parse_service_account(secrets))
    products = audit.list_all('products', merchant_id, token)
    statuses = audit.list_all('productstatuses', merchant_id, token)
    product_by_id = {p.get('id'): p for p in products}
    by_sku, by_variant_id = load_shopify_snapshot()

    rows = []
    for st in statuses:
        pid = st.get('productId')
        attrs = required_attrs(st)
        if not attrs:
            continue
        prod = product_by_id.get(pid) or {}
        meta = parse_product_id(pid or '')
        offer = meta['offer_id']
        shop = by_sku.get(offer) or by_variant_id.get(offer)
        suggestions, evidence, decision = suggestion_for(attrs, prod, shop)
        rows.append({
            'product_id': pid,
            'channel': meta['channel'],
            'offer_id': offer,
            'merchant_title': prod.get('title') or st.get('title'),
            'merchant_current_color': prod.get('color'),
            'merchant_current_sizes': norm_list(prod.get('sizes')),
            'merchant_current_ageGroup': prod.get('ageGroup'),
            'merchant_current_gender': prod.get('gender'),
            'merchant_current_price': prod.get('price'),
            'fresh_required_attrs': sorted(attrs),
            'shopify_match': bool(shop),
            'shopify_product_title': (shop or {}).get('product_title') or (shop or {}).get('product_title2'),
            'shopify_variant_title': (shop or {}).get('variant_title'),
            'shopify_option1': (shop or {}).get('option1'),
            'shopify_tags_color': extract_color_from_tags((shop or {}).get('tags')),
            'suggested_attributes': suggestions,
            'evidence': evidence,
            'decision_state': decision,
            'apply_allowed_now': False,
        })
    rows.sort(key=lambda r: (r['decision_state'], r.get('merchant_title') or '', r.get('product_id') or ''))

    summary = {
        'generated_at': utc_now(),
        'fresh_merchant_products_current': len(products),
        'fresh_merchant_productstatuses_current': len(statuses),
        'required_attr_rows_current': len(rows),
        'required_attr_instances_current': sum(len(r['fresh_required_attrs']) for r in rows),
        'required_attr_counts': dict(Counter(a for r in rows for a in r['fresh_required_attrs']).most_common()),
        'decision_state_counts': dict(Counter(r['decision_state'] for r in rows)),
        'shopify_match_rows': sum(1 for r in rows if r['shopify_match']),
        'write_allowed_now': 0,
    }
    sample_by_state = defaultdict(list)
    for r in rows:
        if len(sample_by_state[r['decision_state']]) < 12:
            sample_by_state[r['decision_state']].append(r)

    payload = {
        'status': 'gmc_p1_attribute_remaining_wave3_preview_read_only',
        'scope': 'Read-only preview/classification of remaining required attributes after Onda 2. No Merchant writes.',
        'source_labels': ['fact_merchant_center', 'fact_shopify_local_snapshot', 'derived_reconciliation'],
        'summary': summary,
        'sample_by_decision_state': sample_by_state,
        'rows': rows,
        'not_performed': ['merchant_write', 'merchant_delete', 'feed_update_or_fetch', 'shopify_write', 'tiny_call_or_write', 'database_write', 'pos_or_local_inventory_write', 'klaviyo_or_whatsapp_send', 'notion_or_n8n_write', 'loyalty_or_judgeme_action'],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    fields = ['product_id','offer_id','merchant_title','fresh_required_attrs','shopify_match','shopify_product_title','shopify_variant_title','shopify_tags_color','suggested_attributes','evidence','decision_state','apply_allowed_now']
    with OUT_CSV.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        w.writeheader()
        for r in rows:
            out = {k: r.get(k) for k in fields}
            out['fresh_required_attrs'] = '; '.join(out.get('fresh_required_attrs') or [])
            out['suggested_attributes'] = json.dumps(out.get('suggested_attributes') or {}, ensure_ascii=False)
            out['evidence'] = json.dumps(out.get('evidence') or {}, ensure_ascii=False)
            w.writerow(out)

    lines = [
        '# LK GMC P1 Attribute Completion — Remaining Wave3 Preview, 2026-05-13', '',
        f"Status: `{payload['status']}`", '',
        '## Escopo',
        '- Reconsulta fresh read-only de Merchant products/productstatuses.',
        '- Classificação dos required attributes remanescentes depois da Onda 2.',
        '- Join local com Shopify snapshot por offer_id/SKU ou variant_id quando possível.',
        '- Nenhum write/delete/feed/fetch.', '',
        '## Resultado executivo',
        f"- Merchant products atuais: {summary['fresh_merchant_products_current']}",
        f"- Productstatuses atuais: {summary['fresh_merchant_productstatuses_current']}",
        f"- Rows com required attributes atuais: {summary['required_attr_rows_current']}",
        f"- Instâncias de required attributes atuais: {summary['required_attr_instances_current']}",
        f"- Rows com match Shopify local: {summary['shopify_match_rows']}",
        '', '## Required attrs por atributo',
    ]
    for k, v in summary['required_attr_counts'].items():
        lines.append(f'- {k}: {v}')
    lines.extend(['', '## Buckets Onda 3'])
    for k, v in sorted(summary['decision_state_counts'].items(), key=lambda x: (-x[1], x[0])):
        lines.append(f'- {k}: {v}')
    lines.extend(['', '## Amostras por bucket'])
    for state, sample in sorted(sample_by_state.items()):
        lines.append(f'### {state}')
        for r in sample[:8]:
            lines.append(f"- `{r['product_id']}` — {r.get('merchant_title')} — missing={r.get('fresh_required_attrs')} — sugestão={r.get('suggested_attributes')} — evidência={r.get('evidence')}")
    lines.extend(['', '## Próximo passo seguro', '- Preparar executor dry-run apenas para um bucket de alta confiança, preferencialmente `candidate_wave3_color_tag_high_confidence`, sem apply até nova aprovação inline.', '', '## Não executado'])
    for n in payload['not_performed']:
        lines.append(f'- {n}')
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(OUT_MD.read_text(encoding='utf-8'), encoding='utf-8')
    if CONTROL.exists():
        marker = '### 2026-05-13 — GMC P1 remaining attribute Wave3 preview'
        text = CONTROL.read_text(encoding='utf-8')
        block = (f"\n{marker}\n\n"
                 f"- Status: `{payload['status']}`.\n"
                 f"- Required attr rows: {summary['required_attr_rows_current']}; instances: {summary['required_attr_instances_current']}.\n"
                 f"- Buckets: {summary['decision_state_counts']}.\n"
                 f"- Nenhum write/delete adicional executado.\n")
        if marker not in text:
            CONTROL.write_text(text.rstrip() + block + '\n', encoding='utf-8')
    if INDEX.exists():
        line = f'| LK GMC P1 Remaining Attribute Wave3 Preview 2026-05-13 | `areas/lk/rotinas/gmc-{RUN_STAMP}.md` | Preview read-only dos required attrs remanescentes pós-Onda 2, com buckets Onda 3 |'
        text = INDEX.read_text(encoding='utf-8')
        if line not in text:
            INDEX.write_text(text.rstrip() + '\n' + line + '\n', encoding='utf-8')
    print(json.dumps({'status': payload['status'], 'summary': summary, 'public_report': str(OUT_MD), 'csv': str(OUT_CSV)}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
