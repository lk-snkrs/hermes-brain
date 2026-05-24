#!/usr/bin/env python3
"""LK GMC P1 core attributes root-cause probe, read-only/no-write.

Investigates why the P1 required-attribute preview found a large block of online
products missing core attributes (title/link/image link/price/availability).
Reads Merchant Content API and local Shopify/Data Spine snapshot only. Emits
sanitized reports and does not write to Merchant, Shopify, Tiny, feeds, DB, POS
or external surfaces.
"""
from __future__ import annotations

import csv
import importlib.util
import json
import pathlib
import sqlite3
from collections import Counter, defaultdict
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / 'scripts/lk_gmc_catalog_duplication_audit_20260512.py'
LOCAL_DB = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite')
PREVIEW_JSON = ROOT / 'reports/lk-gmc-2026-05-12-p1-attribute-completion-preview.json'
RUN_STAMP = '2026-05-12-p1-core-attributes-root-cause-probe'
OUT_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
OUT_CSV = ROOT / f'reports/lk-gmc-{RUN_STAMP}.csv'
OUT_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
CONTROL = ROOT / 'areas/lk/projetos/lk-os-implementation-control.md'
INDEX = ROOT / 'empresa/rotinas/_index.md'
CORE_ATTRS = {'title', 'link', 'image link', 'price', 'availability'}
REQ_CODES = {'item_missing_required_attribute', 'missing_item_attribute_for_product_type'}


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


def price_present(prod: dict[str, Any]) -> bool:
    p = prod.get('price')
    if isinstance(p, dict):
        return bool(p.get('value'))
    return bool(p)


def image_present(prod: dict[str, Any]) -> bool:
    return bool(prod.get('imageLink') or prod.get('additionalImageLinks'))


def core_presence(prod: dict[str, Any]) -> dict[str, bool]:
    return {
        'title': bool(prod.get('title')),
        'link': bool(prod.get('link')),
        'image link': image_present(prod),
        'price': price_present(prod),
        'availability': bool(prod.get('availability')),
    }


def load_shopify_index() -> dict[str, list[dict[str, Any]]]:
    if not LOCAL_DB.exists():
        return {}
    con = sqlite3.connect(str(LOCAL_DB))
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    rows = cur.execute('''
        select v.sku, v.title as variant_title, v.option1, v.option2, v.option3,
               v.price, v.inventory_quantity, v.barcode, v.source_variant_id,
               v.is_active as variant_is_active,
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


def shopify_core_presence(match: dict[str, Any]) -> dict[str, bool]:
    return {
        'title': bool(match.get('product_title')),
        'link': bool(match.get('handle') and match.get('source_variant_id')),
        'image link': bool(match.get('featured_image_url')),
        'price': match.get('price') is not None and str(match.get('price')) != '',
        # For root-cause, Shopify local inventory can evidence availability candidate,
        # but Tiny remains stock truth before operational stock decisions.
        'availability': match.get('inventory_quantity') is not None,
    }


def classify_root_cause(
    product_present: bool,
    merchant_presence: dict[str, bool],
    missing_core: set[str],
    active_matches: list[dict[str, Any]],
    shopify_presence: dict[str, bool],
    all_missing_attrs: set[str],
) -> str:
    if not product_present:
        return 'root_cause_status_without_product_resource_probe_again_or_stale_status'
    if missing_core and all(merchant_presence.get(a, False) for a in missing_core):
        return 'root_cause_diagnostic_says_missing_but_product_resource_has_core_attrs'
    merchant_missing = {a for a in missing_core if not merchant_presence.get(a, False)}
    if merchant_missing and active_matches and all(shopify_presence.get(a, False) for a in merchant_missing):
        return 'root_cause_merchant_payload_missing_core_attrs_shopify_has_evidence'
    if merchant_missing and active_matches:
        return 'root_cause_merchant_and_shopify_source_missing_some_core_values'
    if merchant_missing and not active_matches:
        return 'root_cause_no_active_exact_shopify_sku_for_core_attr_repair'
    if not missing_core and all_missing_attrs:
        return 'root_cause_metadata_only_required_attrs_after_current_refresh'
    return 'root_cause_manual_review_needed'


def main() -> None:
    if not PREVIEW_JSON.exists():
        raise RuntimeError(f'missing_preview_json: {PREVIEW_JSON}')
    preview = json.loads(PREVIEW_JSON.read_text(encoding='utf-8'))
    audit = import_audit()
    secrets = audit.load_doppler()
    merchant_id = secrets.get('MERCHANT_CENTER_ID_LK')
    if not merchant_id:
        raise RuntimeError('missing_merchant_center_id')
    token = audit.google_access_token(audit.parse_service_account(secrets))
    products = audit.list_all('products', merchant_id, token)
    statuses = audit.list_all('productstatuses', merchant_id, token)
    product_by_id = {p.get('id'): p for p in products}
    status_by_id = {s.get('productId'): s for s in statuses}
    shopify_by_sku = load_shopify_index()

    preview_rows = preview.get('public_rows') or []
    core_preview_ids = {
        r.get('product_id') for r in preview_rows
        if r.get('decision_state') == 'candidate_core_attr_preview_needs_approval'
    }

    rows = []
    attr_diagnostic_counts = Counter()
    for pid in sorted(x for x in core_preview_ids if x):
        st = status_by_id.get(pid) or {}
        prod = product_by_id.get(pid) or {}
        status_attrs = {
            norm_attr(i.get('attributeName') or '')
            for i in (st.get('itemLevelIssues') or [])
            if i.get('code') in REQ_CODES and norm_attr(i.get('attributeName') or '')
        }
        missing_core = status_attrs & CORE_ATTRS
        attr_diagnostic_counts.update(missing_core)
        oid = offer_id(pid)
        matches = shopify_by_sku.get(oid, [])
        active_matches = [m for m in matches if str(m.get('product_status') or '').lower() == 'active']
        chosen = active_matches[0] if active_matches else (matches[0] if matches else {})
        m_presence = core_presence(prod)
        s_presence = shopify_core_presence(chosen) if chosen else {a: False for a in CORE_ATTRS}
        merchant_missing_core = sorted(a for a in missing_core if not m_presence.get(a, False))
        shopify_can_supply_missing_core = sorted(a for a in merchant_missing_core if s_presence.get(a, False))
        root = classify_root_cause(
            bool(prod), m_presence, missing_core, active_matches, s_presence, status_attrs
        )
        row = {
            'product_id': pid,
            'offer_id': oid,
            'channel': chan(pid),
            'root_cause_bucket': root,
            'diagnostic_required_attrs': sorted(status_attrs),
            'diagnostic_missing_core_attrs': sorted(missing_core),
            'merchant_product_resource_present': bool(prod),
            'merchant_core_presence': m_presence,
            'merchant_missing_core_attrs_from_status': merchant_missing_core,
            'shopify_exact_sku_match_count': len(matches),
            'shopify_active_match_count': len(active_matches),
            'shopify_core_presence_for_chosen_match': s_presence,
            'shopify_can_supply_missing_core_attrs': shopify_can_supply_missing_core,
            'merchant_title': prod.get('title'),
            'shopify_product_title': chosen.get('product_title'),
            'shopify_handle_present': bool(chosen.get('handle')),
            'shopify_variant_id_present': bool(chosen.get('source_variant_id')),
            'shopify_featured_image_present': bool(chosen.get('featured_image_url')),
            'shopify_price_present': chosen.get('price') is not None and str(chosen.get('price')) != '',
            'shopify_inventory_quantity_present': chosen.get('inventory_quantity') is not None,
            'recommended_next': '',
            'write_allowed_now': False,
        }
        if root == 'root_cause_merchant_payload_missing_core_attrs_shopify_has_evidence':
            row['recommended_next'] = 'Eligible for a narrow approval packet: exact product IDs, exact core attrs from Shopify evidence, private rollback snapshot before Content API update/supplemental strategy.'
        elif root == 'root_cause_diagnostic_says_missing_but_product_resource_has_core_attrs':
            row['recommended_next'] = 'Do not write yet; recheck after Merchant consistency delay and compare productstatus vs product resource before changing payload.'
        elif root == 'root_cause_merchant_and_shopify_source_missing_some_core_values':
            row['recommended_next'] = 'Manual/source fix first for fields missing from Shopify/Data Spine; do not auto-update from incomplete evidence.'
        else:
            row['recommended_next'] = 'Manual review/no write until source evidence is complete.'
        rows.append(row)

    bucket_counts = Counter(r['root_cause_bucket'] for r in rows)
    merchant_missing_counts = Counter(a for r in rows for a in r['merchant_missing_core_attrs_from_status'])
    shopify_supply_counts = Counter(a for r in rows for a in r['shopify_can_supply_missing_core_attrs'])
    exact_update_candidates = [
        r for r in rows
        if r['root_cause_bucket'] == 'root_cause_merchant_payload_missing_core_attrs_shopify_has_evidence'
    ]
    stale_or_recheck = [
        r for r in rows
        if r['root_cause_bucket'] == 'root_cause_diagnostic_says_missing_but_product_resource_has_core_attrs'
    ]
    incomplete_source = [
        r for r in rows
        if r['root_cause_bucket'] == 'root_cause_merchant_and_shopify_source_missing_some_core_values'
    ]

    summary = {
        'merchant_products_current': len(products),
        'merchant_productstatuses_current': len(statuses),
        'core_attr_preview_rows_loaded': len(core_preview_ids),
        'core_attr_rows_currently_rechecked': len(rows),
        'root_cause_bucket_counts': dict(bucket_counts),
        'diagnostic_missing_core_attr_counts': dict(attr_diagnostic_counts),
        'merchant_payload_missing_core_attr_counts': dict(merchant_missing_counts),
        'shopify_can_supply_missing_core_attr_counts': dict(shopify_supply_counts),
        'exact_update_candidate_rows_for_future_approval_packet': len(exact_update_candidates),
        'recheck_before_write_rows': len(stale_or_recheck),
        'incomplete_source_rows': len(incomplete_source),
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
        'status': 'gmc_p1_core_attributes_root_cause_probe_readonly_ready',
        'scope': 'Read-only root-cause probe for P1 online products missing title/link/image link/price/availability diagnostics',
        'source_labels': ['fact_merchant_center', 'fact_shopify_local_snapshot', 'derived_reconciliation', 'manual_approval_required'],
        'summary': summary,
        'interpretation': {
            'verdict': 'Core-attribute diagnostics were rechecked against current Merchant product resources and local Shopify SKU evidence. Rows are split into exact update candidates, consistency recheck/no-write, incomplete-source, and manual-review buckets.',
            'recommended_next_safe_block': 'Generate a separate approval packet only for rows where Merchant payload is missing core attributes and Shopify has exact active-SKU evidence for every missing core value; include private rollback product snapshots before any write executor.',
        },
        'approval_contract': {
            'current_state': 'probe_only_no_execution',
            'not_authorized_now': ['merchant_product_update','content_api_custombatch','supplemental_feed_upload','datafeedFetchNow','shopify_write','tiny_write','database_write','pos_or_local_inventory_change','campaign_or_external_send'],
            'future_write_requires': 'Lucas explicit approval for exact product IDs + exact fields + rollback snapshot path + execution method (Content API update/custombatch vs supplemental feed).',
            'hard_guards_for_future_executor': [
                'load exact candidate JSON only',
                'abort if product resource is absent',
                'snapshot full products.get resource before update',
                'abort if any missing core attr lacks Shopify exact active SKU evidence',
                'never touch local channel rows in this package',
                'verify product resource and productstatus after Content API consistency delay',
            ],
        },
        'rows': rows,
        'samples': {
            'exact_update_candidates': exact_update_candidates[:25],
            'recheck_before_write': stale_or_recheck[:25],
            'incomplete_source': incomplete_source[:25],
        },
        'not_performed': ['merchant_product_delete','merchant_product_insert','merchant_product_update','content_api_custombatch','supplemental_feed_upload','datafeed_fetchNow','feed_update','shopify_write','tiny_write','database_write','pos_or_local_inventory_setting_change','campaign_or_external_send'],
    }

    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    fields = [
        'product_id','offer_id','root_cause_bucket','diagnostic_missing_core_attrs',
        'merchant_product_resource_present','merchant_missing_core_attrs_from_status',
        'shopify_exact_sku_match_count','shopify_active_match_count',
        'shopify_can_supply_missing_core_attrs','shopify_product_title','recommended_next','write_allowed_now'
    ]
    with OUT_CSV.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            out = {k: r.get(k) for k in fields}
            for k in ['diagnostic_missing_core_attrs','merchant_missing_core_attrs_from_status','shopify_can_supply_missing_core_attrs']:
                out[k] = ';'.join(out.get(k) or [])
            w.writerow(out)

    lines = [
        '# LK GMC P1 Core Attributes Root-Cause Probe, 2026-05-12', '',
        f"Status: `{payload['status']}`", '',
        '## Resumo executivo',
        f"- Linhas core-attr P1 rechecadas: {summary['core_attr_rows_currently_rechecked']}",
        f"- Candidatas a approval packet futuro: {summary['exact_update_candidate_rows_for_future_approval_packet']}",
        f"- Recheck/no-write por possível inconsistência productstatus vs product resource: {summary['recheck_before_write_rows']}",
        f"- Fonte incompleta/manual: {summary['incomplete_source_rows']}",
        f"- Buckets: {summary['root_cause_bucket_counts']}",
        f"- Core attrs faltantes no payload Merchant segundo status/payload: {summary['merchant_payload_missing_core_attr_counts']}",
        f"- Core attrs que Shopify local consegue suprir: {summary['shopify_can_supply_missing_core_attr_counts']}",
        '- Writes executados: 0', '',
        '## Veredito',
        '- Probe read-only concluído. O próximo passo seguro é gerar um approval packet menor somente para linhas onde Merchant está sem core attrs e Shopify/Data Spine tem evidência de SKU ativo exato para todos os campos faltantes.', '',
        '## Não executado',
    ]
    for n in payload['not_performed']:
        lines.append(f'- {n}')
    lines.extend(['', '## Arquivos', f'- JSON: `{OUT_JSON}`', f'- CSV: `{OUT_CSV}`'])
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(OUT_MD.read_text(encoding='utf-8'), encoding='utf-8')

    if CONTROL.exists():
        marker = '### 2026-05-12 — GMC P1 core attributes root-cause probe'
        text = CONTROL.read_text(encoding='utf-8')
        block = (f"\n{marker}\n\n"
                 f"- Status: {payload['status']}.\n"
                 f"- Linhas core-attr rechecadas: {summary['core_attr_rows_currently_rechecked']}; "
                 f"approval candidates futuros={summary['exact_update_candidate_rows_for_future_approval_packet']}; "
                 f"recheck/no-write={summary['recheck_before_write_rows']}; fonte incompleta/manual={summary['incomplete_source_rows']}.\n"
                 f"- Nenhum write executado; qualquer aplicação exige pacote exato, snapshot privado de rollback e aprovação Lucas.\n\n")
        if marker not in text:
            CONTROL.write_text(text.rstrip() + block, encoding='utf-8')
    if INDEX.exists():
        line = f'| LK GMC P1 Core Attributes Root-Cause Probe 2026-05-12 | `areas/lk/rotinas/gmc-{RUN_STAMP}.md` | Probe read-only das causas de title/link/image/price/availability ausentes por exact product ID; separa approval candidates de recheck/manual |'
        text = INDEX.read_text(encoding='utf-8')
        if line not in text:
            INDEX.write_text(text.rstrip() + '\n' + line + '\n', encoding='utf-8')

    print(json.dumps({'status': payload['status'], 'summary': summary, 'public_report': str(OUT_MD)}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
