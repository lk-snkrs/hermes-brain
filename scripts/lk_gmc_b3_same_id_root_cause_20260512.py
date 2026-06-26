#!/usr/bin/env python3
"""Root-cause audit for the LK GMC B/B3 same-ID incident.

Read-only/local. Explains why 854 rows were classified as B and why B3 was
unsafe, then records hard guard recommendations. No external writes.
"""
from __future__ import annotations

import csv
import json
import pathlib
import sqlite3
from collections import Counter
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
LOCAL_DB = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite')
SHOPIFY_PROBE = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_reconciliation/lk-gmc-2026-05-12-b-remaining-shopify-live-probe.csv')
B2_CSV = ROOT / 'reports/lk-gmc-2026-05-12-package-b2-shopify-live-preview.csv'
RUN_STAMP = '2026-05-12-b3-same-id-root-cause'
OUT_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
OUT_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
INDEX = ROOT / 'empresa/rotinas/_index.md'


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def main() -> None:
    shop_rows = list(csv.DictReader(SHOPIFY_PROBE.open(encoding='utf-8')))
    b2_rows = list(csv.DictReader(B2_CSV.open(encoding='utf-8')))

    con = sqlite3.connect(str(LOCAL_DB))
    cur = con.cursor()
    product_max_updated, product_count = cur.execute('select max(updated_at), count(*) from lk_products').fetchone()
    variant_max_updated, variant_count = cur.execute('select max(updated_at), count(*) from lk_product_variants').fetchone()
    local_sku_counts = Counter()
    for r in shop_rows:
        sku = r.get('shopify_sku') or ''
        hit = cur.execute('select count(*) from lk_product_variants where sku=?', (sku,)).fetchone()[0]
        active = cur.execute("""
            select count(*)
            from lk_product_variants v left join lk_products p on v.product_id=p.product_id
            where v.sku=? and lower(coalesce(p.status,''))='active'
        """, (sku,)).fetchone()[0]
        local_sku_counts[f'local_sku_hit={bool(hit)}|local_active_hit={bool(active)}'] += 1
    con.close()

    shop_state_counts = Counter(r.get('shopify_probe_state') for r in shop_rows)
    same_id = sum(1 for r in b2_rows if r.get('old_product_id') == r.get('new_product_id'))
    diff_id = sum(1 for r in b2_rows if r.get('old_product_id') != r.get('new_product_id'))
    status_counts = Counter(r.get('preview_status') for r in b2_rows)

    payload = {
        'generated_at': utc_now(),
        'status': 'gmc_b3_same_id_root_cause_completed_readonly',
        'source_labels': ['fact_shopify', 'fact_merchant_center', 'fact_shopify_local_snapshot', 'derived_reconciliation'],
        'local_data_spine': {
            'db_path': str(LOCAL_DB),
            'products_count': product_count,
            'products_max_updated': product_max_updated,
            'variants_count': variant_count,
            'variants_max_updated': variant_max_updated,
            'exact_live_shopify_sku_presence_for_854': dict(local_sku_counts),
        },
        'shopify_live_probe': {
            'rows': len(shop_rows),
            'state_counts': dict(shop_state_counts),
        },
        'b2_preview': {
            'rows': len(b2_rows),
            'same_old_new_product_id': same_id,
            'different_old_new_product_id': diff_id,
            'preview_status_counts': dict(status_counts),
        },
        'root_cause': [
            'Original ranker classified online rows as B when weak evidence existed (item_group/product or GTIN) but exact SKU was absent from the local Data Spine snapshot.',
            'For these 854 rows, Shopify live proved the link variant exists, is active, and has the same SKU/offerId as the Merchant product ID.',
            'The B2 preview interpreted target_already_exists without first asserting old_product_id != target_product_id.',
            'Because old_product_id == target_product_id for all 854, B3 delete-old-only was an invalid operation and was correctly rolled back.',
        ],
        'corrective_guards': [
            'Block any delete-old-only row where old_product_id == correct_existing_product_id.',
            'Block any B/B2/B3 executable preview where proposed old/new IDs are equal; classify as valid_or_same_id_noop instead.',
            'Treat weak product/GTIN match plus live Shopify same-SKU as no-op/valid, not as identifier mismatch.',
            'Only execute identifier fix when exact old ID and exact new ID are different and both rollback + presence checks are satisfied.',
        ],
        'not_touched': ['merchant_product_write_or_delete', 'shopify_write', 'feed', 'database_write', 'campaign_or_external_send', 'local_channel', 'pos_inventory'],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    lines = [
        '# LK GMC B3 Same-ID Root Cause, 2026-05-12', '',
        f"Status: `{payload['status']}`", '',
        '## Resumo executivo',
        f"- Linhas investigadas: {len(shop_rows)}",
        f"- Shopify live active variant with SKU: {shop_state_counts.get('shopify_live_active_variant_with_sku_review_candidate', 0)}",
        f"- B2 old_product_id == new_product_id: {same_id}",
        f"- B2 old_product_id != new_product_id: {diff_id}",
        f"- SKU Shopify live ausente no Data Spine local: {local_sku_counts.get('local_sku_hit=False|local_active_hit=False', 0)}",
        f"- Data Spine products max(updated_at): {product_max_updated}",
        f"- Data Spine variants max(updated_at): {variant_max_updated}",
        '',
        '## Causa raiz',
        '- O ranker original colocou esses itens em B porque havia evidência fraca de produto/GTIN, mas o SKU exato não aparecia no Data Spine local.',
        '- O Shopify live mostrou que os 854 variants existem, estão ativos e têm SKU.',
        '- O B2 transformou isso em `target_already_exists`, mas não checou se o target era o próprio old ID.',
        '- Como `old_product_id == target_product_id` nos 854 casos, B3 não era uma limpeza de duplicata; era delete do item real.',
        '',
        '## Correção operacional',
        '- B3 foi revertido e verificado: 854/854 presentes novamente.',
        '- Scripts/skills devem bloquear hard qualquer delete same-ID.',
        '- Esses 854 devem virar `same_id_noop/valid_after_shopify_live`, não pacote de delete.',
        '',
        '## Não tocado',
    ]
    for item in payload['not_touched']:
        lines.append(f'- {item}')
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(OUT_MD.read_text(encoding='utf-8'), encoding='utf-8')

    line = f'| LK GMC B3 Same-ID Root Cause 2026-05-12 | `areas/lk/rotinas/gmc-{RUN_STAMP}.md` | RCA do incidente B3: 854 same-ID, rollback verificado e guardrails anti-delete same-ID |'
    text = INDEX.read_text(encoding='utf-8')
    if line not in text:
        INDEX.write_text(text.rstrip() + '\n' + line + '\n', encoding='utf-8')

    print(json.dumps({'status': payload['status'], 'same_id': same_id, 'local_sku_counts': dict(local_sku_counts), 'public_report': str(OUT_MD)}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
