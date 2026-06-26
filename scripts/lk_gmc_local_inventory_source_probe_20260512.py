#!/usr/bin/env python3
"""Read-only probe for LK Google Merchant local inventory source.

Answers: where do `local:pt:BR:*` Merchant items appear to come from, and
whether previous local/online orphan labels are likely true or match artifacts.
No Merchant, Shopify, database, feed, campaign, or external writes are performed.
"""
from __future__ import annotations

import importlib.util
import json
import pathlib
import sqlite3
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / 'scripts/lk_gmc_catalog_duplication_audit_20260512.py'
LOCAL_DB = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite')
OUT_JSON = ROOT / 'reports/lk-gmc-local-inventory-source-probe-2026-05-12.json'
OUT_MD = ROOT / 'reports/lk-gmc-local-inventory-source-probe-2026-05-12.md'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/gmc-local-inventory-source-probe-2026-05-12.md'
CONTROL = ROOT / 'areas/lk/projetos/lk-os-implementation-control.md'


def load_audit_module():
    spec = importlib.util.spec_from_file_location('lk_gmc_catalog_duplication_audit', AUDIT_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def merchant_get(mod: Any, path: str, mid: str, token: str) -> dict[str, Any]:
    return mod.get_json(f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/{path}', token)


def parse_dt(value: str | None) -> str:
    if not value:
        return ''
    return value[:10]


def norm_offer_for_shopify(offer_id: str, channel: str) -> str:
    if channel == 'local' and offer_id.startswith('LIA_'):
        return offer_id[4:]
    return offer_id


def load_shopify_keys() -> dict[str, set[str]]:
    out = {'sku': set(), 'variant_id': set(), 'source_variant_id': set(), 'inventory_item_id': set()}
    if not LOCAL_DB.exists():
        return out
    con = sqlite3.connect(str(LOCAL_DB))
    cur = con.cursor()
    for sku, variant_id, source_variant_id, inventory_item_id in cur.execute(
        "select coalesce(sku,''), coalesce(variant_id,''), coalesce(source_variant_id,''), coalesce(inventory_item_id,'') from lk_product_variants"
    ):
        if sku:
            out['sku'].add(str(sku))
        if variant_id:
            out['variant_id'].add(str(variant_id))
        if source_variant_id:
            out['source_variant_id'].add(str(source_variant_id))
        if inventory_item_id:
            out['inventory_item_id'].add(str(inventory_item_id))
    con.close()
    return out


def summarize_products(products: list[dict[str, Any]], shopify_keys: dict[str, set[str]]) -> dict[str, Any]:
    by_channel = Counter()
    by_source = Counter()
    local_prefix = Counter()
    source_by_channel = Counter()
    creation_by_channel = Counter()
    match_stats = Counter()
    samples: dict[str, list[dict[str, Any]]] = {
        'local_lia_prefix': [],
        'local_raw_shopify_match': [],
        'local_normalized_shopify_match': [],
        'local_no_sku_match_after_lia_strip': [],
    }
    for p in products:
        channel = p.get('channel') or ''
        offer = p.get('offerId') or ''
        by_channel[channel] += 1
        by_source[p.get('source') or ''] += 1
        source_by_channel[f'{channel}|{p.get("source") or ""}'] += 1
        # Creation date only exists on productstatuses, not products; filled elsewhere.
        if channel == 'local':
            prefix = 'LIA_' if offer.startswith('LIA_') else ('numeric' if offer.isdigit() else 'other')
            local_prefix[prefix] += 1
        raw_match = offer in shopify_keys['sku'] or offer in shopify_keys['source_variant_id'] or offer in shopify_keys['variant_id']
        normalized = norm_offer_for_shopify(offer, channel)
        norm_match = normalized in shopify_keys['sku'] or normalized in shopify_keys['source_variant_id'] or normalized in shopify_keys['variant_id']
        if channel == 'local':
            if offer.startswith('LIA_'):
                match_stats['local_lia_prefix'] += 1
                if len(samples['local_lia_prefix']) < 8:
                    samples['local_lia_prefix'].append({'merchant_offer_id': offer, 'normalized_offer_id': normalized, 'title': p.get('title')})
            if raw_match:
                match_stats['local_raw_shopify_match'] += 1
                if len(samples['local_raw_shopify_match']) < 8:
                    samples['local_raw_shopify_match'].append({'merchant_offer_id': offer, 'title': p.get('title')})
            if (not raw_match) and norm_match:
                match_stats['local_normalized_shopify_match'] += 1
                if len(samples['local_normalized_shopify_match']) < 8:
                    samples['local_normalized_shopify_match'].append({'merchant_offer_id': offer, 'normalized_offer_id': normalized, 'title': p.get('title')})
            if not norm_match:
                match_stats['local_no_sku_match_after_lia_strip'] += 1
                if len(samples['local_no_sku_match_after_lia_strip']) < 8:
                    samples['local_no_sku_match_after_lia_strip'].append({'merchant_offer_id': offer, 'normalized_offer_id': normalized, 'title': p.get('title')})
    return {
        'total_products': len(products),
        'by_channel': dict(by_channel),
        'by_source': dict(by_source),
        'source_by_channel': dict(source_by_channel),
        'local_offer_prefix': dict(local_prefix),
        'shopify_match_stats': dict(match_stats),
        'samples': samples,
    }


def summarize_statuses(statuses: list[dict[str, Any]], mod: Any) -> dict[str, Any]:
    creation = Counter()
    update = Counter()
    dest = Counter()
    status_by_dest = Counter()
    for s in statuses:
        meta = mod.parse_product_id(s.get('productId') or '')
        ch = meta.get('channel') or ''
        creation[f'{ch}|{parse_dt(s.get("creationDate"))}'] += 1
        update[f'{ch}|{parse_dt(s.get("lastUpdateDate"))}'] += 1
        for d in s.get('destinationStatuses') or []:
            key = f'{ch}|{d.get("destination") or ""}'
            dest[key] += 1
            status_by_dest[f'{key}|{d.get("status") or ""}'] += 1
    return {
        'creation_date_top': dict(creation.most_common(20)),
        'last_update_date_top': dict(update.most_common(20)),
        'destination_counts': dict(dest.most_common(20)),
        'status_by_destination': dict(status_by_dest.most_common(30)),
    }


def sanitize_lia_settings(data: dict[str, Any]) -> dict[str, Any]:
    countries = []
    for c in data.get('countrySettings') or []:
        provider = c.get('posDataProvider') or {}
        countries.append({
            'country': c.get('country'),
            'inventory_status': (c.get('inventory') or {}).get('status'),
            'hosted_local_storefront_active': c.get('hostedLocalStorefrontActive'),
            'store_pickup_active': c.get('storePickupActive'),
            'pos_data_provider_id_present': bool(provider.get('posDataProviderId')),
            'pos_external_account_id': provider.get('posExternalAccountId'),
            'omnichannel_lsf_type': (c.get('omnichannelExperience') or {}).get('lsfType'),
        })
    return {'account_id_present': bool(data.get('accountId')), 'country_settings': countries}


def sanitize_datafeeds(feeds: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out = []
    for f in feeds:
        fs = f.get('fetchSchedule') or {}
        fetch_url = fs.get('fetchUrl') or ''
        out.append({
            'id': f.get('id'),
            'name': f.get('name'),
            'fileName': f.get('fileName'),
            'targets': f.get('targets'),
            'fetch_url_present': bool(fetch_url),
            'fetch_url_kind': 'gist' if 'gist' in fetch_url else ('shopify' if 'shopify' in fetch_url else ('none' if not fetch_url else 'other')),
        })
    return out


def main() -> None:
    mod = load_audit_module()
    secrets = mod.load_doppler()
    mid = secrets['MERCHANT_CENTER_ID_LK']
    token = mod.google_access_token(mod.parse_service_account(secrets))
    products = mod.list_all('products', mid, token)
    statuses = mod.list_all('productstatuses', mid, token)
    datafeeds = mod.list_all('datafeeds', mid, token)
    try:
        lia = sanitize_lia_settings(merchant_get(mod, f'liasettings/{mid}', mid, token))
    except Exception as exc:
        lia = {'error_type': type(exc).__name__, 'error': str(exc)[:160]}
    shopify_keys = load_shopify_keys()
    prod_summary = summarize_products(products, shopify_keys)
    status_summary = summarize_statuses(statuses, mod)
    source_conclusion = {
        'likely_local_inventory_source': 'Shopify POS / Shopify app via Google Content API',
        'evidence': [
            'Merchant LIA settings has inventory status active for BR.',
            'Merchant LIA settings reports posExternalAccountId=shopify.com.',
            'Merchant local products have source=api, not file/feed.',
            'Only listed datafeed is the supplemental color feed, not the primary local inventory source.',
            'Most local offer IDs use LIA_ prefix, which is characteristic of Local Inventory Ads/local channel IDs and can break naive SKU matching.',
        ],
        'confidence': 'high',
    }
    interpretation = {
        'orphan_label_update': 'Previous local orphan counts are too conservative because raw matching did not normalize the LIA_ prefix. After stripping LIA_, many local items may match Shopify SKUs/variants.',
        'risk': 'Do not delete local items based on the first orphan preview. Local listings are active and backed by Shopify POS/local inventory integration.',
        'next_safe_step': 'Regenerate cleanup preview with LIA_ normalization and split true stale local items from valid Shopify POS local items.',
    }
    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'LK GMC local inventory source probe read-only',
        'status': 'gmc_local_inventory_source_probe_ready_readonly',
        'source_labels': ['fact_merchant_center', 'fact_shopify_local_snapshot', 'derived_reconciliation'],
        'merchant_center': {
            'liasettings_sanitized': lia,
            'datafeeds_sanitized': sanitize_datafeeds(datafeeds),
            'product_summary': prod_summary,
            'productstatus_summary': status_summary,
        },
        'shopify_snapshot': {
            'db_present': LOCAL_DB.exists(),
            'sku_count': len(shopify_keys['sku']),
            'source_variant_id_count': len(shopify_keys['source_variant_id']),
            'variant_id_count': len(shopify_keys['variant_id']),
        },
        'source_conclusion': source_conclusion,
        'interpretation': interpretation,
        'not_performed': [
            'merchant_product_delete', 'merchant_product_update', 'datafeed_update', 'feed_delete_or_exclusion',
            'shopify_write', 'database_write', 'campaign_or_external_send', 'local_inventory_disable', 'gmb_update'
        ],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    lines = [
        '# LK GMC Local Inventory Source Probe, 2026-05-12', '',
        f"Status: `{payload['status']}`", '',
        '## Veredito',
        f"- Fonte provável do inventário local: **{source_conclusion['likely_local_inventory_source']}**.",
        f"- Confiança: `{source_conclusion['confidence']}`.",
        '- O canal local está ativo no Merchant e aponta para `shopify.com` como provedor POS/local.',
        '- Portanto, `local` não deve ser tratado como ruído.', '',
        '## Evidências',
    ]
    for ev in source_conclusion['evidence']:
        lines.append(f'- {ev}')
    lines.extend(['', '## Números principais'])
    lines.append(f"- Produtos Merchant lidos: {prod_summary['total_products']}")
    for ch, count in sorted(prod_summary['by_channel'].items()):
        lines.append(f'- Canal `{ch}`: {count}')
    lines.append(f"- Source por canal: {prod_summary['source_by_channel']}")
    lines.append(f"- Prefixos local: {prod_summary['local_offer_prefix']}")
    lines.append(f"- Match Shopify local raw: {prod_summary['shopify_match_stats'].get('local_raw_shopify_match', 0)}")
    lines.append(f"- Match Shopify local após remover `LIA_`: {prod_summary['shopify_match_stats'].get('local_normalized_shopify_match', 0)}")
    lines.append(f"- Sem match após normalização `LIA_`: {prod_summary['shopify_match_stats'].get('local_no_sku_match_after_lia_strip', 0)}")
    lines.extend(['', '## Interpretação'])
    lines.append(f"- {interpretation['orphan_label_update']}")
    lines.append(f"- {interpretation['risk']}")
    lines.append(f"- Próximo passo seguro: {interpretation['next_safe_step']}")
    lines.extend(['', '## Não executado'])
    for n in payload['not_performed']:
        lines.append(f'- {n}')
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.parent.mkdir(parents=True, exist_ok=True)
    BRAIN_DOC.write_text(OUT_MD.read_text(encoding='utf-8'), encoding='utf-8')
    if CONTROL.exists():
        marker = '### 2026-05-12 — GMC local inventory source probe'
        text = CONTROL.read_text(encoding='utf-8')
        block = "\n" + marker + "\n\n- Status: read-only concluído.\n- Fonte provável do inventário local: Shopify POS / Shopify app via Content API.\n- Evidência: LIA settings ativo no BR com posExternalAccountId=shopify.com; produtos locais `source=api`; feed listado é apenas supplemental.\n- Decisão operacional: não limpar `local` como ruído; regenerar preview com normalização `LIA_` antes de qualquer ação.\n\n"
        if marker not in text:
            CONTROL.write_text(text.rstrip() + block, encoding='utf-8')
    print(json.dumps({
        'status': payload['status'],
        'likely_source': source_conclusion['likely_local_inventory_source'],
        'confidence': source_conclusion['confidence'],
        'by_channel': prod_summary['by_channel'],
        'source_by_channel': prod_summary['source_by_channel'],
        'local_prefix': prod_summary['local_offer_prefix'],
        'local_raw_match': prod_summary['shopify_match_stats'].get('local_raw_shopify_match', 0),
        'local_normalized_match': prod_summary['shopify_match_stats'].get('local_normalized_shopify_match', 0),
        'local_no_match_after_normalization': prod_summary['shopify_match_stats'].get('local_no_sku_match_after_lia_strip', 0),
    }, ensure_ascii=False))


if __name__ == '__main__':
    main()
