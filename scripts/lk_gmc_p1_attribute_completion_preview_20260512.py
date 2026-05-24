#!/usr/bin/env python3
"""LK GMC P1 attribute completion preview, read-only/no-write.

Builds an exact-product-ID preview for current Merchant required-attribute issues.
Uses Merchant Content API reads and local Shopify/Data Spine SQLite reads only.
No Merchant/Shopify/Tiny/feed/DB/POS writes.
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
RUN_STAMP = '2026-05-12-p1-attribute-completion-preview'
OUT_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
OUT_CSV = ROOT / f'reports/lk-gmc-{RUN_STAMP}.csv'
OUT_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
CONTROL = ROOT / 'areas/lk/projetos/lk-os-implementation-control.md'
INDEX = ROOT / 'empresa/rotinas/_index.md'
REQ_CODES = {'item_missing_required_attribute', 'missing_item_attribute_for_product_type'}
CORE_ATTRS = {'title', 'link', 'image link', 'price', 'availability'}
SIZE_ATTRS = {'size', 'age group', 'gender', 'color'}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def import_audit():
    spec = importlib.util.spec_from_file_location('audit', AUDIT_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def chan(pid: str) -> str:
    return (pid or '').split(':', 1)[0] if ':' in (pid or '') else 'unknown'


def offer_id(pid: str) -> str:
    parts = (pid or '').split(':', 3)
    return parts[3] if len(parts) == 4 else pid


def norm_attr(attr: str) -> str:
    return (attr or '').strip().lower().replace('_', ' ')


def infer_age_group(text: str) -> tuple[str, str]:
    t = text.lower()
    if re.search(r'\b(kids|kid|junior|infantil|crian[cç]a|gs\b|ps\b|td\b|baby|toddler)\b', t):
        return 'kids', 'medium_keyword_kids'
    return 'adult', 'medium_lk_default_adult'


def infer_gender(text: str) -> tuple[str, str]:
    t = text.lower()
    if re.search(r'\b(wmns|women|womens|female|feminino|mulher)\b', t):
        return 'female', 'medium_keyword_female'
    if re.search(r'\b(men|mens|male|masculino|homem)\b', t):
        return 'male', 'medium_keyword_male'
    if re.search(r'\b(unisex|unissex)\b', t):
        return 'unisex', 'high_keyword_unisex'
    return 'unisex', 'medium_lk_default_unisex_needs_review'


def infer_color(text: str) -> tuple[str, str]:
    colors = [
        ('preto', 'black'), ('black', 'black'), ('branco', 'white'), ('white', 'white'),
        ('azul', 'blue'), ('blue', 'blue'), ('vermelho', 'red'), ('red', 'red'),
        ('verde', 'green'), ('green', 'green'), ('cinza', 'gray'), ('grey', 'gray'), ('gray', 'gray'),
        ('bege', 'beige'), ('cream', 'beige'), ('marrom', 'brown'), ('brown', 'brown'),
        ('rosa', 'pink'), ('pink', 'pink'), ('amarelo', 'yellow'), ('yellow', 'yellow'),
        ('roxo', 'purple'), ('purple', 'purple'), ('laranja', 'orange'), ('orange', 'orange'),
        ('prata', 'silver'), ('silver', 'silver'), ('dourado', 'gold'), ('gold', 'gold'),
    ]
    found = []
    low = text.lower()
    for token, val in colors:
        if re.search(rf'\b{re.escape(token)}\b', low):
            found.append(val)
    found = list(dict.fromkeys(found))
    if found:
        return '/'.join(found), 'medium_keyword_color'
    return '', 'low_no_color_detected'


def load_shopify_index() -> dict[str, list[dict[str, Any]]]:
    if not LOCAL_DB.exists():
        return {}
    con = sqlite3.connect(str(LOCAL_DB))
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    rows = cur.execute('''
        select v.sku, v.title as variant_title, v.option1, v.option2, v.option3,
               v.price, v.compare_at_price, v.inventory_quantity, v.barcode,
               v.source_variant_id, v.is_active as variant_is_active,
               p.title as product_title, p.handle, p.vendor, p.product_type,
               p.status as product_status, p.tags, p.featured_image_url, p.source_product_id
        from lk_product_variants v
        left join lk_products p on p.product_id = v.product_id
        where coalesce(v.sku,'') <> ''
    ''').fetchall()
    con.close()
    out: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for r in rows:
        out[str(r['sku']).strip()].append(dict(r))
    return out


def shopify_url(handle: str | None, source_variant_id: str | None) -> str:
    if not handle:
        return ''
    base = f'https://www.lksneakers.com.br/products/{handle}'
    if source_variant_id:
        return base + f'?variant={source_variant_id}'
    return base


def build_suggestion(attrs: set[str], match: dict[str, Any]) -> tuple[dict[str, Any], dict[str, str]]:
    text = ' '.join(str(match.get(k) or '') for k in ['product_title','product_type','vendor','tags','variant_title','option1','option2','option3','sku'])
    suggestions: dict[str, Any] = {}
    evidence: dict[str, str] = {}
    if 'title' in attrs:
        suggestions['title'] = match.get('product_title') or ''
        evidence['title'] = 'high_shopify_local_product_title' if suggestions['title'] else 'low_missing_title'
    if 'link' in attrs:
        suggestions['link'] = shopify_url(match.get('handle'), str(match.get('source_variant_id') or ''))
        evidence['link'] = 'medium_constructed_from_shopify_handle_variant' if suggestions['link'] else 'low_missing_handle'
    if 'image link' in attrs:
        suggestions['imageLink'] = match.get('featured_image_url') or ''
        evidence['imageLink'] = 'high_shopify_local_featured_image' if suggestions['imageLink'] else 'low_missing_featured_image'
    if 'price' in attrs:
        price = match.get('price')
        suggestions['price'] = f'{float(price):.2f} BRL' if price is not None else ''
        evidence['price'] = 'high_shopify_local_variant_price' if suggestions['price'] else 'low_missing_price'
    if 'availability' in attrs:
        inv = match.get('inventory_quantity')
        suggestions['availability'] = 'in stock' if isinstance(inv, int) and inv > 0 else 'out of stock'
        evidence['availability'] = 'medium_shopify_local_inventory_quantity'
    if 'size' in attrs:
        size = match.get('option1') or match.get('variant_title') or ''
        suggestions['sizes'] = [str(size)] if size else []
        evidence['sizes'] = 'high_shopify_variant_option_or_title' if size else 'low_missing_size'
    if 'age group' in attrs:
        age, sig = infer_age_group(text)
        suggestions['ageGroup'] = age; evidence['ageGroup'] = sig
    if 'gender' in attrs:
        gender, sig = infer_gender(text)
        suggestions['gender'] = gender; evidence['gender'] = sig
    if 'color' in attrs:
        color, sig = infer_color(text)
        suggestions['color'] = color; evidence['color'] = sig
    return suggestions, evidence


def classify_record(attrs: set[str], matches: list[dict[str, Any]], suggestions: dict[str, Any], evidence: dict[str, str]) -> str:
    if not matches:
        return 'blocked_no_shopify_exact_sku_match'
    active = [m for m in matches if str(m.get('product_status') or '').lower() == 'active']
    if not active:
        return 'blocked_shopify_product_not_active'
    low = [k for k, v in evidence.items() if str(v).startswith('low_')]
    if low:
        return 'ambiguous_missing_source_value'
    if attrs & CORE_ATTRS:
        # Core URL/image/price/title/availability corrections are higher impact and must be previewed separately.
        return 'candidate_core_attr_preview_needs_approval'
    if evidence and all(str(v).startswith('high_') for v in evidence.values()):
        return 'candidate_high_confidence_attr_preview'
    return 'candidate_medium_confidence_attr_preview_needs_review'


def main() -> None:
    audit = import_audit()
    secrets = audit.load_doppler()
    merchant_id = secrets.get('MERCHANT_CENTER_ID_LK')
    token = audit.google_access_token(audit.parse_service_account(secrets))
    products = audit.list_all('products', merchant_id, token)
    statuses = audit.list_all('productstatuses', merchant_id, token)
    product_by_id = {p.get('id'): p for p in products}
    shopify_by_sku = load_shopify_index()

    rows = []
    issue_instances = 0
    for st in statuses:
        pid = st.get('productId') or ''
        if chan(pid) != 'online':
            continue
        attrs = sorted({norm_attr(i.get('attributeName') or '') for i in (st.get('itemLevelIssues') or []) if i.get('code') in REQ_CODES and norm_attr(i.get('attributeName') or '')})
        if not attrs:
            continue
        issue_instances += sum(1 for i in (st.get('itemLevelIssues') or []) if i.get('code') in REQ_CODES)
        oid = offer_id(pid)
        matches = shopify_by_sku.get(oid, [])
        active_matches = [m for m in matches if str(m.get('product_status') or '').lower() == 'active']
        chosen = active_matches[0] if active_matches else (matches[0] if matches else {})
        suggestions, evidence = build_suggestion(set(attrs), chosen) if chosen else ({}, {})
        state = classify_record(set(attrs), matches, suggestions, evidence)
        mprod = product_by_id.get(pid) or {}
        rows.append({
            'product_id': pid,
            'offer_id': oid,
            'merchant_title': mprod.get('title'),
            'missing_attributes': attrs,
            'missing_attr_count': len(attrs),
            'issue_instance_count': sum(1 for i in (st.get('itemLevelIssues') or []) if i.get('code') in REQ_CODES),
            'shopify_exact_sku_match_count': len(matches),
            'shopify_active_match_count': len(active_matches),
            'shopify_product_title': chosen.get('product_title'),
            'shopify_handle': chosen.get('handle'),
            'shopify_variant_title': chosen.get('variant_title'),
            'shopify_inventory_quantity': chosen.get('inventory_quantity'),
            'suggested_attributes': suggestions,
            'evidence': evidence,
            'decision_state': state,
            'write_allowed_now': False,
            'approval_required_for_write': 'Lucas approval required before any Merchant product/update/custombatch/feed/supplemental-feed write.',
        })
    rows.sort(key=lambda r: (r['decision_state'], r['offer_id']))
    state_counts = Counter(r['decision_state'] for r in rows)
    attr_counts = Counter(a for r in rows for a in r['missing_attributes'])
    candidates = [r for r in rows if r['decision_state'].startswith('candidate_')]
    blocked = [r for r in rows if r['decision_state'].startswith('blocked_')]
    summary = {
        'merchant_products_current': len(products),
        'merchant_productstatuses_current': len(statuses),
        'p1_required_attr_products_reviewed': len(rows),
        'p1_required_attr_issue_instances': issue_instances,
        'candidate_rows_for_approval_packet': len(candidates),
        'blocked_rows': len(blocked),
        'decision_state_counts': dict(state_counts),
        'missing_attribute_counts_by_product': dict(attr_counts),
        'write_allowed_now': 0,
        'merchant_writes': 0,
        'shopify_writes': 0,
        'tiny_writes': 0,
        'feed_writes': 0,
        'database_writes': 0,
        'external_sends': 0,
    }
    payload = {
        'generated_at': utc_now(),
        'status': 'gmc_p1_attribute_completion_preview_ready_no_execution',
        'scope': 'No-write preview for current online Merchant required-attribute issues using exact product IDs and local Shopify Data Spine evidence',
        'source_labels': ['fact_merchant_center', 'fact_shopify_local_snapshot', 'derived_reconciliation', 'manual_approval_required'],
        'summary': summary,
        'approval_contract': {
            'current_state': 'preview_only_no_execution',
            'what_lucas_would_approve_later': 'Only after a separate approval packet: write exact suggested attributes for exact current product IDs, with rollback snapshot and no broad query/wildcard updates.',
            'not_authorized_now': ['merchant_product_update','content_api_custombatch','supplemental_feed_upload','datafeed_fetchNow','shopify_write','tiny_write','database_write','pos_or_local_inventory_change','campaign_or_external_send'],
            'hard_guards_for_future_executor': ['load exact candidates from final JSON only','abort if any candidate lacks Shopify exact active SKU evidence','do not modify blocked rows','do not modify local channel/POS rows','verify attributes and diagnostics after Content API delay'],
        },
        'public_rows': rows,
        'samples': {
            'candidates': candidates[:25],
            'blocked': blocked[:25],
        },
        'not_performed': ['merchant_product_delete','merchant_product_insert','merchant_product_update','content_api_custombatch','supplemental_feed_upload','datafeed_fetchNow','feed_update','shopify_write','tiny_write','database_write','pos_or_local_inventory_setting_change','campaign_or_external_send'],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    fields = ['product_id','offer_id','missing_attributes','issue_instance_count','shopify_exact_sku_match_count','shopify_active_match_count','shopify_product_title','shopify_handle','shopify_variant_title','decision_state','suggested_attributes','evidence','write_allowed_now']
    with OUT_CSV.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            out = {k: r.get(k) for k in fields}
            out['missing_attributes'] = ';'.join(r.get('missing_attributes') or [])
            out['suggested_attributes'] = json.dumps(out['suggested_attributes'], ensure_ascii=False)
            out['evidence'] = json.dumps(out['evidence'], ensure_ascii=False)
            w.writerow(out)
    lines = [
        '# LK GMC P1 Attribute Completion Preview, 2026-05-12', '',
        f"Status: `{payload['status']}`", '',
        '## Resumo executivo',
        f"- Produtos online com required-attribute issues revisados: {summary['p1_required_attr_products_reviewed']}",
        f"- Instâncias required-attribute: {summary['p1_required_attr_issue_instances']}",
        f"- Candidatos para approval packet futuro: {summary['candidate_rows_for_approval_packet']}",
        f"- Bloqueados/sem evidência suficiente: {summary['blocked_rows']}",
        f"- Estados: {summary['decision_state_counts']}",
        f"- Atributos faltantes por produto: {summary['missing_attribute_counts_by_product']}",
        '- Writes executados: 0', '',
        '## Veredito',
        '- Preview P1 pronto sem execução. A maior parte dos problemas é core attr ausente em produtos online; pode virar pacote de aprovação separado, mas ainda não deve ser aplicado automaticamente.', '',
        '## Não executado',
    ]
    for n in payload['not_performed']:
        lines.append(f'- {n}')
    lines.extend(['', '## Arquivos', f'- JSON: `{OUT_JSON}`', f'- CSV: `{OUT_CSV}`'])
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(OUT_MD.read_text(encoding='utf-8'), encoding='utf-8')
    if CONTROL.exists():
        marker = '### 2026-05-12 — GMC P1 attribute completion preview'
        text = CONTROL.read_text(encoding='utf-8')
        block = (f"\n{marker}\n\n"
                 f"- Status: {payload['status']}.\n"
                 f"- Produtos/instâncias required-attribute revisados: {summary['p1_required_attr_products_reviewed']} / {summary['p1_required_attr_issue_instances']}.\n"
                 f"- Candidatos approval packet futuro: {summary['candidate_rows_for_approval_packet']}; bloqueados={summary['blocked_rows']}.\n"
                 f"- Nenhum write executado; aplicação exige aprovação separada por exact IDs.\n\n")
        if marker not in text:
            CONTROL.write_text(text.rstrip() + block, encoding='utf-8')
    if INDEX.exists():
        line = f'| LK GMC P1 Attribute Completion Preview 2026-05-12 | `areas/lk/rotinas/gmc-{RUN_STAMP}.md` | Preview no-write de atributos obrigatórios por exact product ID, usando Merchant current diagnostics + Shopify local Data Spine; gera candidatos/bloqueados para approval packet futuro |'
        text = INDEX.read_text(encoding='utf-8')
        if line not in text:
            INDEX.write_text(text.rstrip() + '\n' + line + '\n', encoding='utf-8')
    print(json.dumps({'status': payload['status'], 'summary': summary, 'public_report': str(OUT_MD)}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
