#!/usr/bin/env python3
"""Read-only post A/B reconciliation for remaining LK GMC package B rows.

No Merchant/Shopify/feed/database writes. Reads live Merchant products and local
LK Data Spine snapshot, classifies why B rows remain unsafe, and emits sanitized
public reports plus a private review CSV without PII/secrets.
"""
from __future__ import annotations

import csv
import importlib.util
import json
import os
import pathlib
import re
import sqlite3
import urllib.parse
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / 'scripts/lk_gmc_catalog_duplication_audit_20260512.py'
B_SCRIPT = ROOT / 'scripts/lk_gmc_execute_package_b_identifier_fix_20260512.py'
SNAPSHOT = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-executable-previews-rollback-2026-05-12.json')
LOCAL_DB = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite')
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_reconciliation')
RUN_STAMP = '2026-05-12-post-ab-b-remaining-reconciliation'
OUT_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
OUT_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
PRIVATE_CSV = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-review.csv'
PACKAGE = 'B_online_identifier_fix'


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def import_module(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def norm(s: str | None) -> str:
    s = (s or '').lower().strip()
    s = re.sub(r'[^a-z0-9]+', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


def variant_id_from_link(link: str | None) -> str:
    try:
        return (urllib.parse.parse_qs(urllib.parse.urlparse(link or '').query).get('variant') or [''])[0]
    except Exception:
        return ''


def load_snapshot_b() -> list[dict[str, Any]]:
    data = json.loads(SNAPSHOT.read_text(encoding='utf-8'))
    return [r for r in data.get('records', []) if r.get('package') == PACKAGE]


def qrows(cur: sqlite3.Cursor, sql: str, params: tuple[Any, ...]) -> list[dict[str, Any]]:
    return [dict(r) for r in cur.execute(sql, params)]


def active_sku_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [r for r in rows if str(r.get('pstatus') or '').lower() == 'active' and r.get('sku')]


def analyze_blockers(cur: sqlite3.Cursor, product: dict[str, Any]) -> dict[str, Any]:
    offer = str(product.get('offerId') or '')
    item_group = str(product.get('itemGroupId') or '')
    gtin = str(product.get('gtin') or '')
    title = str(product.get('title') or '')
    variant = variant_id_from_link(product.get('link'))
    title_norm = norm(title)

    out: dict[str, Any] = {
        'variant_from_link': variant,
        'has_gtin': bool(gtin),
        'has_item_group_id': bool(item_group),
        'title_norm': title_norm,
    }

    if variant:
        rows = qrows(cur, """
            select v.*, p.status as pstatus, p.title as ptitle, p.source_product_id as p_source_product_id
            from lk_product_variants v left join lk_products p on v.product_id=p.product_id
            where v.source_variant_id=? or v.variant_id=?
        """, (variant, variant))
        out['variant_match_rows'] = len(rows)
        out['variant_active_sku_rows'] = len(active_sku_rows(rows))
        out['variant_skus'] = sorted({str(r.get('sku') or '') for r in active_sku_rows(rows) if r.get('sku')})[:8]
    else:
        out['variant_match_rows'] = 0
        out['variant_active_sku_rows'] = 0
        out['variant_skus'] = []

    if gtin:
        rows = qrows(cur, """
            select v.*, p.status as pstatus, p.title as ptitle, p.source_product_id as p_source_product_id
            from lk_product_variants v left join lk_products p on v.product_id=p.product_id
            where v.barcode=?
        """, (gtin,))
        active = active_sku_rows(rows)
        out['gtin_match_rows'] = len(rows)
        out['gtin_active_sku_rows'] = len(active)
        out['gtin_active_skus'] = sorted({str(r.get('sku') or '') for r in active if r.get('sku')})[:8]
    else:
        out['gtin_match_rows'] = 0
        out['gtin_active_sku_rows'] = 0
        out['gtin_active_skus'] = []

    if item_group:
        rows = qrows(cur, """
            select v.*, p.status as pstatus, p.title as ptitle, p.source_product_id as p_source_product_id
            from lk_product_variants v left join lk_products p on v.product_id=p.product_id
            where (p.source_product_id=? or p.product_id=?)
        """, (item_group, item_group))
        active = active_sku_rows(rows)
        prefix_active = [r for r in active if str(r.get('sku') or '').startswith(offer + '-')]
        out['item_group_active_sku_rows'] = len(active)
        out['item_group_prefix_active_rows'] = len(prefix_active)
        out['item_group_active_skus_sample'] = sorted({str(r.get('sku') or '') for r in active if r.get('sku')})[:10]
    else:
        out['item_group_active_sku_rows'] = 0
        out['item_group_prefix_active_rows'] = 0
        out['item_group_active_skus_sample'] = []

    # Exact normalized product-title match is evidence only, not safe execution.
    exact_title_products = []
    if title_norm:
        rows = qrows(cur, """
            select product_id, source_product_id, title, status
            from lk_products
            where lower(coalesce(status,''))='active'
        """, ())
        exact_title_products = [r for r in rows if norm(r.get('title')) == title_norm]
    out['title_exact_active_products'] = len(exact_title_products)
    out['title_exact_source_product_ids'] = sorted({str(r.get('source_product_id') or r.get('product_id') or '') for r in exact_title_products})[:8]

    return out


def classify(row: dict[str, Any], current_ids: set[str], current_offer_ids: set[str], cur: sqlite3.Cursor, bmod: Any) -> dict[str, Any]:
    product = row.get('merchant_product_resource') or {}
    old_pid = product.get('id') or (row.get('classification') or {}).get('product_id')
    old_offer = str(product.get('offerId') or '')
    target_sku, strict_reason, _ = bmod.resolve_target_sku(cur, product)
    new_pid = f"online:{product.get('contentLanguage') or 'pt'}:{product.get('targetCountry') or 'BR'}:{target_sku}" if target_sku else ''
    blockers = analyze_blockers(cur, product)

    if old_pid not in current_ids:
        state = 'old_absent_after_ab'
    elif target_sku and new_pid in current_ids:
        state = 'old_present_target_already_exists'
    elif target_sku:
        state = 'strict_target_now_safe_candidate'
    else:
        state = 'old_present_no_strict_target'

    if state == 'old_present_no_strict_target':
        if blockers['gtin_active_sku_rows'] > 1:
            blocker = 'gtin_duplicate_active_skus'
        elif blockers['gtin_active_sku_rows'] == 0 and blockers['has_gtin']:
            blocker = 'gtin_not_found_in_active_shopify'
        elif blockers['variant_active_sku_rows'] > 1:
            blocker = 'link_variant_duplicate_active_skus'
        elif blockers['variant_active_sku_rows'] == 0 and blockers['variant_from_link']:
            blocker = 'link_variant_not_found_active'
        elif blockers['item_group_active_sku_rows'] > 1 and blockers['item_group_prefix_active_rows'] != 1:
            blocker = 'item_group_multiple_variants_no_single_prefix'
        elif blockers['title_exact_active_products'] == 1:
            blocker = 'title_only_single_product_evidence_needs_size_sku_confirmation'
        elif blockers['title_exact_active_products'] > 1:
            blocker = 'title_ambiguous_multiple_active_products'
        else:
            blocker = 'insufficient_evidence'
    else:
        blocker = state

    return {
        'old_product_id': old_pid,
        'old_offer_id': old_offer,
        'title': product.get('title'),
        'item_group_id': product.get('itemGroupId'),
        'merchant_gtin': product.get('gtin'),
        'strict_target_sku': target_sku or '',
        'strict_reason': strict_reason,
        'new_product_id': new_pid,
        'state_after_ab': state,
        'blocker': blocker,
        **{k: (json.dumps(v, ensure_ascii=False) if isinstance(v, list) else v) for k, v in blockers.items()},
    }


def main() -> None:
    audit = import_module(AUDIT_PATH, 'lk_gmc_catalog_duplication_audit')
    bmod = import_module(B_SCRIPT, 'lk_gmc_execute_package_b_identifier_fix')
    secrets = audit.load_doppler()
    merchant_id = secrets.get('MERCHANT_CENTER_ID_LK')
    if not merchant_id:
        raise RuntimeError('missing_merchant_center_id')
    token = audit.google_access_token(audit.parse_service_account(secrets))
    products = bmod.list_all_products(merchant_id, token)
    current_ids = {p.get('id') for p in products}
    current_offer_ids = {p.get('offerId') for p in products}

    con = sqlite3.connect(str(LOCAL_DB))
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    rows = [classify(r, current_ids, current_offer_ids, cur, bmod) for r in load_snapshot_b()]
    con.close()

    counters = Counter(r['state_after_ab'] for r in rows)
    blockers = Counter(r['blocker'] for r in rows if r['state_after_ab'] == 'old_present_no_strict_target')
    # A conservative review queue: title-only evidence, not write-ready.
    review_queue = [r for r in rows if r['blocker'] == 'title_only_single_product_evidence_needs_size_sku_confirmation']

    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE_DIR, 0o700)
    fields = ['old_product_id','old_offer_id','title','item_group_id','merchant_gtin','strict_target_sku','strict_reason','new_product_id','state_after_ab','blocker','variant_from_link','variant_match_rows','variant_active_sku_rows','variant_skus','gtin_match_rows','gtin_active_sku_rows','gtin_active_skus','item_group_active_sku_rows','item_group_prefix_active_rows','item_group_active_skus_sample','title_exact_active_products','title_exact_source_product_ids']
    with PRIVATE_CSV.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        w.writeheader()
        w.writerows(rows)
    os.chmod(PRIVATE_CSV, 0o600)

    payload = {
        'generated_at': utc_now(),
        'status': 'gmc_post_ab_b_remaining_reconciliation_readonly',
        'scope': 'Package B remaining read-only reconciliation after applied A/B',
        'source_labels': ['fact_merchant_center', 'fact_shopify_local_snapshot', 'derived_reconciliation'],
        'merchant_products_current_read': len(products),
        'snapshot_b_records': len(rows),
        'state_counts': dict(counters),
        'remaining_no_strict_target_blockers': dict(blockers),
        'review_queue_title_only_count': len(review_queue),
        'private_review_csv': str(PRIVATE_CSV),
        'not_touched': ['merchant_product_write_or_delete', 'local_channel', 'shopify', 'feed', 'database', 'campaign_or_external_send', 'google_business_profile', 'pos_inventory'],
        'interpretation': {
            'safe_write_ready_now': counters.get('strict_target_now_safe_candidate', 0),
            'needs_manual_or_data_spine_refresh': counters.get('old_present_no_strict_target', 0),
            'note': 'Title-only matches are evidence for manual/Data Spine review, not safe identifier writes.'
        }
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    lines = [
        '# LK GMC Post A/B Package B Remaining Reconciliation, 2026-05-12', '',
        f"Status: `{payload['status']}`", '',
        '## Resumo executivo',
        f"- Merchant products live lidos: {len(products)}",
        f"- Registros B do snapshot original: {len(rows)}",
        f"- Old absent depois do A/B: {counters.get('old_absent_after_ab', 0)}",
        f"- Old presente sem target estrito: {counters.get('old_present_no_strict_target', 0)}",
        f"- Old presente com target já existente: {counters.get('old_present_target_already_exists', 0)}",
        f"- Candidatos estritos novos agora write-ready: {counters.get('strict_target_now_safe_candidate', 0)}",
        f"- Fila de revisão title-only: {len(review_queue)}",
        '',
        '## Principais bloqueios dos B restantes sem target estrito',
    ]
    for k, v in blockers.most_common(12):
        lines.append(f'- {k}: {v}')
    lines.extend([
        '',
        '## Veredito',
        '- Não apareceu novo B seguro para escrita automática nesta revalidação.',
        '- Os casos title-only ajudam a revisão humana/Data Spine, mas não bastam para mudar offerId no Merchant sem confirmar tamanho/SKU.',
        f'- CSV privado de revisão: `{PRIVATE_CSV}`',
        '',
        '## Não tocado',
    ])
    for item in payload['not_touched']:
        lines.append(f'- {item}')
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(OUT_MD.read_text(encoding='utf-8'), encoding='utf-8')

    print(json.dumps({
        'status': payload['status'],
        'merchant_products_current_read': len(products),
        'snapshot_b_records': len(rows),
        'state_counts': dict(counters),
        'top_blockers': blockers.most_common(8),
        'private_review_csv': str(PRIVATE_CSV),
        'public_report': str(OUT_MD),
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
