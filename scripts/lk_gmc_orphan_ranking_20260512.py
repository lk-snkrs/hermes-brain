#!/usr/bin/env python3
"""Read-only ranker for LK GMC local + online orphan candidates.

Classifies Merchant local P1 and online orphan rows after LIA_ normalization,
using Shopify/Data Spine SKU, variant ID, product ID and GTIN/barcode bridges.
No Merchant, Shopify, database, feed, campaign or external writes are performed.
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
OUT_JSON = ROOT / 'reports/lk-gmc-orphan-ranking-2026-05-12.json'
OUT_CSV = ROOT / 'reports/lk-gmc-orphan-ranking-2026-05-12.csv'
OUT_MD = ROOT / 'reports/lk-gmc-orphan-ranking-2026-05-12.md'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/gmc-orphan-ranking-2026-05-12.md'
CONTROL = ROOT / 'areas/lk/projetos/lk-os-implementation-control.md'
INDEX = ROOT / 'empresa/rotinas/_index.md'


def load_audit_module():
    spec = importlib.util.spec_from_file_location('lk_gmc_catalog_duplication_audit', AUDIT_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def norm_offer(offer: str, channel: str) -> str:
    if channel == 'local' and offer.startswith('LIA_'):
        return offer[4:]
    return offer


def norm_text(value: str | None) -> str:
    return re.sub(r'\s+', ' ', re.sub(r'[^0-9a-zA-ZÀ-ÿ]+', ' ', value or '').strip().lower())


def load_shopify_index() -> dict[str, Any]:
    idx: dict[str, Any] = {
        'skus': set(), 'source_variant_ids': set(), 'variant_ids': set(),
        'inventory_item_ids': set(), 'source_product_ids': set(), 'product_ids': set(),
        'barcodes': set(), 'active_skus': set(), 'sku_to_product': {},
        'barcode_to_sku': {}, 'product_titles': defaultdict(set), 'db_present': LOCAL_DB.exists(),
    }
    if not LOCAL_DB.exists():
        return idx
    con = sqlite3.connect(str(LOCAL_DB))
    cur = con.cursor()
    q = """
    select coalesce(v.sku,''), coalesce(v.variant_id,''), coalesce(v.source_variant_id,''),
           coalesce(v.inventory_item_id,''), coalesce(v.barcode,''), coalesce(v.product_id,''),
           coalesce(p.source_product_id,''), coalesce(p.product_id,''), coalesce(p.title,''),
           coalesce(p.status,''), coalesce(v.title,''), coalesce(v.option1,'')
    from lk_product_variants v left join lk_products p on v.product_id=p.product_id
    """
    for sku, vid, svid, inv, barcode, vpid, spid, pid, ptitle, status, vtitle, opt1 in cur.execute(q):
        if sku:
            idx['skus'].add(str(sku)); idx['sku_to_product'][str(sku)] = {'title': ptitle, 'status': status, 'variant_title': vtitle or opt1}
            if str(status).lower() == 'active': idx['active_skus'].add(str(sku))
        if vid: idx['variant_ids'].add(str(vid))
        if svid: idx['source_variant_ids'].add(str(svid))
        if inv: idx['inventory_item_ids'].add(str(inv))
        if barcode:
            idx['barcodes'].add(str(barcode)); idx['barcode_to_sku'][str(barcode)] = str(sku)
        if spid: idx['source_product_ids'].add(str(spid)); idx['product_titles'][str(spid)].add(ptitle)
        if pid: idx['product_ids'].add(str(pid)); idx['product_titles'][str(pid)].add(ptitle)
        if vpid: idx['product_ids'].add(str(vpid))
    con.close()
    return idx


def status_summary(status: dict[str, Any] | None) -> dict[str, Any]:
    if not status:
        return {'destinations': [], 'has_disapproved': False, 'has_item_level_issues': False, 'creation_date': None, 'last_update_date': None}
    dests = []
    has_disapproved = False
    for d in status.get('destinationStatuses') or []:
        st = d.get('status') or ''
        if st not in {'approved', 'pending'}:
            has_disapproved = True
        dests.append({'destination': d.get('destination'), 'channel': d.get('channel'), 'status': st})
    issues = status.get('itemLevelIssues') or []
    return {
        'destinations': dests,
        'has_disapproved': has_disapproved,
        'has_item_level_issues': bool(issues),
        'item_issue_count': len(issues),
        'creation_date': status.get('creationDate'),
        'last_update_date': status.get('lastUpdateDate'),
    }


def classify(p: dict[str, Any], st: dict[str, Any], idx: dict[str, Any], norm_channels: dict[str, set[str]]) -> dict[str, Any]:
    channel = p.get('channel') or ''
    offer = p.get('offerId') or ''
    recon = norm_offer(offer, channel)
    item_group = str(p.get('itemGroupId') or '')
    gtin = str(p.get('gtin') or '')
    mpn = str(p.get('mpn') or '')
    exact_sku = recon in idx['skus'] or recon in idx['active_skus']
    exact_variant = recon in idx['source_variant_ids'] or recon in idx['variant_ids']
    product_match = bool(item_group and (item_group in idx['source_product_ids'] or item_group in idx['product_ids']))
    gtin_match = bool(gtin and gtin in idx['barcodes'])
    mpn_match = bool(mpn and (mpn in idx['skus'] or mpn in idx['source_variant_ids'] or mpn in idx['variant_ids']))
    stsum = status_summary(st)
    has_both_channels = len(norm_channels.get(recon, set())) > 1
    evidence = []
    if exact_sku: evidence.append('offer_matches_shopify_sku')
    if exact_variant: evidence.append('offer_matches_shopify_variant_id')
    if product_match: evidence.append('item_group_matches_shopify_product_id')
    if gtin_match: evidence.append('gtin_matches_shopify_barcode')
    if mpn_match: evidence.append('mpn_matches_shopify_identifier')
    if has_both_channels: evidence.append('same_normalized_offer_seen_in_local_and_online')
    if stsum['has_disapproved']: evidence.append('merchant_destination_not_approved')
    if stsum['has_item_level_issues']: evidence.append('merchant_item_level_issues')

    any_strong_match = exact_sku or exact_variant or mpn_match
    any_weak_match = product_match or gtin_match

    if channel == 'local':
        if any_strong_match:
            priority, bucket, action = 'P3', 'valid_local_listing', 'keep_monitor_local_listing'
        elif any_weak_match:
            priority, bucket, action = 'P1', 'local_identifier_mismatch', 'fix_or_confirm_local_identifier_mapping_preview'
        else:
            priority, bucket, action = 'P0' if stsum['has_disapproved'] else 'P1', 'local_unmatched_after_normalization', 'investigate_stale_or_wrong_local_item_preview'
    elif channel == 'online':
        if any_strong_match:
            priority, bucket, action = 'P3', 'valid_online_listing', 'keep_monitor_online_listing'
        elif any_weak_match:
            priority, bucket, action = 'P1', 'online_identifier_mismatch', 'fix_or_confirm_online_identifier_mapping_preview'
        else:
            priority = 'P0' if stsum['has_disapproved'] or stsum['has_item_level_issues'] else 'P1'
            bucket, action = 'online_unmatched_possible_stale', 'investigate_stale_or_wrong_online_item_preview'
    else:
        priority, bucket, action = 'P2', 'unknown_channel', 'investigate_unknown_channel_preview'

    # Keep P3 rows out of the action queue, but they count in summary.
    return {
        'priority': priority,
        'bucket': bucket,
        'recommended_action': action,
        'product_id': p.get('id'),
        'channel': channel,
        'offer_id': offer,
        'reconciliation_offer_id': recon,
        'title': p.get('title'),
        'source': p.get('source'),
        'availability': p.get('availability'),
        'item_group_id': item_group,
        'gtin_present': bool(gtin),
        'mpn': mpn,
        'exact_sku_match': exact_sku,
        'exact_variant_match': exact_variant,
        'product_id_match': product_match,
        'gtin_barcode_match': gtin_match,
        'mpn_match': mpn_match,
        'has_local_and_online_normalized_counterpart': has_both_channels,
        'merchant_status': stsum,
        'evidence': evidence,
        'approval_status': 'preview_only_no_write',
    }


def main() -> None:
    mod = load_audit_module()
    sec = mod.load_doppler()
    mid = sec['MERCHANT_CENTER_ID_LK']
    token = mod.google_access_token(mod.parse_service_account(sec))
    products = mod.list_all('products', mid, token)
    statuses = mod.list_all('productstatuses', mid, token)
    status_by_pid = {s.get('productId'): s for s in statuses}
    idx = load_shopify_index()
    norm_channels: dict[str, set[str]] = defaultdict(set)
    for p in products:
        norm_channels[norm_offer(p.get('offerId') or '', p.get('channel') or '')].add(p.get('channel') or '')

    classified = [classify(p, status_by_pid.get(p.get('id')) or {}, idx, norm_channels) for p in products]
    queue = [r for r in classified if r['priority'] in {'P0', 'P1'}]
    queue.sort(key=lambda r: (r['priority'], r['bucket'], r['channel'], r['reconciliation_offer_id']))

    counts = Counter((r['priority'], r['bucket']) for r in classified)
    bucket_counts = Counter(r['bucket'] for r in classified)
    channel_counts = Counter(r['channel'] for r in classified)
    action_counts = Counter(r['recommended_action'] for r in queue)
    priority_counts = Counter(r['priority'] for r in classified)
    queue_priority_counts = Counter(r['priority'] for r in queue)
    queue_channel_counts = Counter(r['channel'] for r in queue)
    samples = queue[:300]
    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'LK GMC orphan ranking read-only',
        'status': 'gmc_orphan_risk_ranker_ready_readonly',
        'source_labels': ['fact_merchant_center', 'fact_shopify_local_snapshot', 'derived_reconciliation'],
        'summary': {
            'merchant_products_read': len(products),
            'merchant_statuses_read': len(statuses),
            'merchant_channels': dict(channel_counts),
            'priority_counts_all': dict(priority_counts),
            'queue_p0_p1_total': len(queue),
            'queue_priority_counts': dict(queue_priority_counts),
            'queue_channel_counts': dict(queue_channel_counts),
            'bucket_counts_all': dict(bucket_counts),
            'priority_bucket_counts': {f'{p}|{b}': c for (p, b), c in counts.items()},
            'action_counts_queue': dict(action_counts),
            'sample_rows_published': len(samples),
        },
        'interpretation': {
            'main_change_from_previous_preview': 'Local rows with LIA_ prefix are no longer treated as orphan when they match Shopify after normalization.',
            'top_safe_focus': 'Investigate P0/P1 rows, especially online/local unmatched and identifier mismatch rows, before any Merchant cleanup/write.',
            'execution_requires_approval': True,
        },
        'sample_rows': samples,
        'not_performed': ['merchant_product_delete', 'merchant_product_update', 'feed_update', 'shopify_write', 'database_write', 'campaign_or_external_send', 'local_inventory_disable'],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    fields = ['priority','bucket','recommended_action','product_id','channel','offer_id','reconciliation_offer_id','title','source','availability','item_group_id','gtin_present','mpn','exact_sku_match','exact_variant_match','product_id_match','gtin_barcode_match','mpn_match','has_local_and_online_normalized_counterpart','evidence','approval_status']
    with OUT_CSV.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in queue[:2000]:
            rr = {k: r.get(k) for k in fields}
            rr['evidence'] = ';'.join(r.get('evidence') or [])
            w.writerow(rr)
    lines = [
        '# LK GMC Orphan Ranking, 2026-05-12', '',
        f"Status: `{payload['status']}`", '',
        '## Resumo executivo',
        f"- Produtos Merchant lidos: {len(products)}",
        f"- Fila P0/P1 total: {len(queue)}",
        f"- P0: {queue_priority_counts.get('P0', 0)}",
        f"- P1: {queue_priority_counts.get('P1', 0)}",
        f"- Canais na fila: {dict(queue_channel_counts)}", '',
        '## Buckets principais',
    ]
    for b, c in bucket_counts.most_common():
        lines.append(f'- {b}: {c}')
    lines.extend(['', '## Interpretação'])
    lines.append('- `valid_local_listing`: local preservado; bateu com Shopify depois de normalizar `LIA_`.')
    lines.append('- `identifier_mismatch`: parece produto real, mas ID/SKU/GTIN precisa saneamento antes de ação.')
    lines.append('- `unmatched_possible_stale` / `unmatched_after_normalization`: maior risco de item antigo, errado ou fonte inconsistente.')
    lines.append('- Nada foi escrito ou removido; isso é ranking de investigação/aprovação.')
    lines.extend(['', '## Próximo bloco seguro recomendado'])
    lines.append('- Abrir amostras P0/P1 por bucket, cruzar com Shopify/Tiny e gerar pacote de correção ou limpeza com rollback.')
    lines.extend(['', '## Não executado'])
    for n in payload['not_performed']:
        lines.append(f'- {n}')
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(OUT_MD.read_text(encoding='utf-8'), encoding='utf-8')

    if CONTROL.exists():
        marker = '### 2026-05-12 — GMC orphan ranking'
        text = CONTROL.read_text(encoding='utf-8')
        block = f"\n{marker}\n\n- Status: read-only concluído.\n- Fila P0/P1 total: {len(queue)}; P0={queue_priority_counts.get('P0',0)}; P1={queue_priority_counts.get('P1',0)}.\n- Preservados como válidos/monitorados: {bucket_counts.get('valid_local_listing',0)} locais e {bucket_counts.get('valid_online_listing',0)} online.\n- Próximo passo seguro: pacote por bucket para correção/limpeza com rollback; nenhuma execução externa/write realizada.\n\n"
        if marker not in text:
            CONTROL.write_text(text.rstrip() + block, encoding='utf-8')
    if INDEX.exists():
        line = '| LK GMC Orphan Ranking 2026-05-12 | `areas/lk/rotinas/gmc-orphan-ranking-2026-05-12.md` | Ranking read-only P0/P1 de locais e online órfãos após normalização `LIA_`, separando válidos, mismatch e possíveis stale, sem Merchant/Shopify writes |'
        text = INDEX.read_text(encoding='utf-8')
        if line not in text:
            anchor = '| LK GMC Local Inventory Source Probe 2026-05-12 | `areas/lk/rotinas/gmc-local-inventory-source-probe-2026-05-12.md` | Investigação read-only confirmou fonte provável do inventário local: Shopify POS/app via Content API, LIA ativo no BR com `posExternalAccountId=shopify.com` |'
            INDEX.write_text(text.replace(anchor, anchor + '\n' + line), encoding='utf-8')
    print(json.dumps({'status': payload['status'], 'summary': payload['summary']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
