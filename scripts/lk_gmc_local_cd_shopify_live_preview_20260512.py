#!/usr/bin/env python3
"""Read-only Shopify live validation preview for LK GMC local packages C/D.

Re-runs the current Merchant ranking after A/B execution/rollback, isolates local
package D (local unmatched after LIA_ normalization) and C (local identifier
mismatch), then checks Shopify Admin GraphQL live by normalized SKU. This is a
preview only: no Merchant, Shopify, POS, Tiny, feed, DB, campaign or external
writes.
"""
from __future__ import annotations

import csv
import importlib.util
import json
import os
import pathlib
import sqlite3
import time
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
RANKING_PATH = ROOT / 'scripts/lk_gmc_orphan_ranking_20260512.py'
AUDIT_PATH = ROOT / 'scripts/lk_gmc_catalog_duplication_audit_20260512.py'
LOCAL_DB = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite')
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_reconciliation')
RUN_STAMP = '2026-05-12-local-cd-shopify-live-preview'
PRIVATE_CSV = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}.csv'
OUT_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
OUT_CSV = ROOT / f'reports/lk-gmc-{RUN_STAMP}.csv'
OUT_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
CONTROL = ROOT / 'areas/lk/projetos/lk-os-implementation-control.md'
INDEX = ROOT / 'empresa/rotinas/_index.md'

QUERY = '''query VariantBySku($q: String!) {
  productVariants(first: 20, query: $q) {
    edges {
      node {
        id
        legacyResourceId
        sku
        title
        barcode
        inventoryQuantity
        product { id legacyResourceId title handle status }
      }
    }
  }
}'''


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def import_module(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def shop_host(raw: str) -> str:
    return (raw or '').strip().replace('https://', '').replace('http://', '').strip('/')


def shopify_search_exact_sku(host: str, token: str, sku: str) -> list[dict[str, Any]]:
    # Quote the SKU to avoid broad tokenized search for SKUs containing spaces.
    q = 'sku:"' + sku.replace('\\', '\\\\').replace('"', '\\"') + '"'
    body = json.dumps({'query': QUERY, 'variables': {'q': q}}).encode('utf-8')
    req = urllib.request.Request(f'https://{host}/admin/api/2024-01/graphql.json', data=body, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-Shopify-Access-Token', token)
    with urllib.request.urlopen(req, timeout=120) as r:
        data = json.loads(r.read().decode())
    if data.get('errors'):
        raise RuntimeError(json.dumps(data['errors'])[:1000])
    nodes = [edge['node'] for edge in data.get('data', {}).get('productVariants', {}).get('edges', [])]
    return [n for n in nodes if (n.get('sku') or '') == sku]


def load_tiny_skus() -> set[str]:
    if not LOCAL_DB.exists():
        return set()
    con = sqlite3.connect(str(LOCAL_DB))
    cur = con.cursor()
    try:
        rows = cur.execute("select distinct coalesce(sku,'') from tiny_anchor_stock where coalesce(sku,'')<>''").fetchall()
        return {str(r[0]) for r in rows if r and r[0]}
    finally:
        con.close()


def public_row(row: dict[str, Any]) -> dict[str, Any]:
    exact = row.get('shopify_exact_matches') or []
    first = exact[0] if exact else {}
    product = first.get('product') or {}
    return {
        'package': row['package'],
        'old_bucket': row['old_bucket'],
        'decision_state': row['decision_state'],
        'product_id': row['product_id'],
        'offer_id': row['offer_id'],
        'normalized_sku': row['normalized_sku'],
        'merchant_title': row.get('merchant_title'),
        'source': row.get('source'),
        'availability': row.get('availability'),
        'shopify_exact_match_count': len(exact),
        'shopify_product_status': product.get('status') or '',
        'shopify_product_title': product.get('title') or '',
        'shopify_variant_legacy_id': first.get('legacyResourceId') or '',
        'shopify_inventory_quantity': first.get('inventoryQuantity'),
        'tiny_local_sku_match': row['tiny_local_sku_match'],
        'recommended_next_action': row['recommended_next_action'],
    }


def main() -> None:
    ranking = import_module(RANKING_PATH, 'lk_gmc_orphan_ranking')
    audit = import_module(AUDIT_PATH, 'lk_gmc_catalog_duplication_audit')
    secrets = audit.load_doppler()
    merchant_id = secrets.get('MERCHANT_CENTER_ID_LK')
    host = shop_host(secrets.get('SHOPIFY_STORE_URL') or '')
    shopify_token = secrets.get('SHOPIFY_ACCESS_TOKEN') or ''
    if not merchant_id:
        raise RuntimeError('missing_merchant_center_id')
    if not host or not shopify_token:
        raise RuntimeError('missing_shopify_credentials')

    content_token = audit.google_access_token(audit.parse_service_account(secrets))
    products = audit.list_all('products', merchant_id, content_token)
    statuses = audit.list_all('productstatuses', merchant_id, content_token)
    status_by_pid = {s.get('productId'): s for s in statuses}
    idx = ranking.load_shopify_index()
    norm_channels: dict[str, set[str]] = defaultdict(set)
    for p in products:
        norm_channels[ranking.norm_offer(p.get('offerId') or '', p.get('channel') or '')].add(p.get('channel') or '')
    classified = [ranking.classify(p, status_by_pid.get(p.get('id')) or {}, idx, norm_channels) for p in products]

    local_queue = [r for r in classified if r.get('bucket') in {'local_identifier_mismatch', 'local_unmatched_after_normalization'}]
    local_queue.sort(key=lambda r: (r['bucket'], r['reconciliation_offer_id']))

    unique_skus = sorted({r.get('reconciliation_offer_id') or '' for r in local_queue if r.get('reconciliation_offer_id')})
    tiny_skus = load_tiny_skus()

    shopify_by_sku: dict[str, list[dict[str, Any]]] = {}
    for i, sku in enumerate(unique_skus, start=1):
        shopify_by_sku[sku] = shopify_search_exact_sku(host, shopify_token, sku)
        # Keep the probe polite; 1300 single-SKU queries are okay but avoid a hard burst.
        if i % 100 == 0:
            time.sleep(0.5)

    out_rows: list[dict[str, Any]] = []
    for r in local_queue:
        sku = r.get('reconciliation_offer_id') or ''
        matches = shopify_by_sku.get(sku, [])
        active_matches = [m for m in matches if ((m.get('product') or {}).get('status') == 'ACTIVE')]
        package = 'C_local_identifier_fix' if r['bucket'] == 'local_identifier_mismatch' else 'D_local_stale_triage'
        if active_matches:
            decision = 'valid_local_listing_after_shopify_live_sku_match_noop'
            next_action = 'preserve_local_listing; update stale local Data Spine/index before considering Merchant write'
        elif matches:
            decision = 'shopify_sku_exists_but_product_not_active_review_before_local_cleanup'
            next_action = 'manual review; do not delete until POS/Tiny/source confirms stale'
        elif sku in tiny_skus:
            decision = 'tiny_local_sku_present_but_shopify_live_sku_not_found_review_required'
            next_action = 'validate Tiny/POS/source mapping before any Merchant local cleanup'
        else:
            decision = 'no_shopify_live_exact_sku_no_tiny_local_match_cleanup_candidate_after_pos_validation'
            next_action = 'candidate only for POS/Tiny validation; no local delete/update without explicit approval and rollback'
        out_rows.append({
            'package': package,
            'old_bucket': r['bucket'],
            'decision_state': decision,
            'product_id': r['product_id'],
            'offer_id': r['offer_id'],
            'normalized_sku': sku,
            'merchant_title': r.get('title'),
            'source': r.get('source'),
            'availability': r.get('availability'),
            'shopify_exact_matches': matches,
            'tiny_local_sku_match': sku in tiny_skus,
            'recommended_next_action': next_action,
            'merchant_status': r.get('merchant_status') or {},
            'evidence_before_live_probe': r.get('evidence') or [],
        })

    counts = Counter(row['decision_state'] for row in out_rows)
    package_counts = Counter(row['package'] for row in out_rows)
    decision_by_package: dict[str, Counter] = defaultdict(Counter)
    for row in out_rows:
        decision_by_package[row['package']][row['decision_state']] += 1

    safe_noop = [r for r in out_rows if r['decision_state'] == 'valid_local_listing_after_shopify_live_sku_match_noop']
    cleanup_candidates = [r for r in out_rows if r['decision_state'] == 'no_shopify_live_exact_sku_no_tiny_local_match_cleanup_candidate_after_pos_validation']
    non_active_review = [r for r in out_rows if r['decision_state'] == 'shopify_sku_exists_but_product_not_active_review_before_local_cleanup']
    tiny_review = [r for r in out_rows if r['decision_state'] == 'tiny_local_sku_present_but_shopify_live_sku_not_found_review_required']

    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE_DIR, 0o700)
    private_fields = ['package','old_bucket','decision_state','product_id','offer_id','normalized_sku','merchant_title','source','availability','shopify_exact_match_count','shopify_product_status','shopify_product_title','shopify_variant_legacy_id','shopify_inventory_quantity','tiny_local_sku_match','recommended_next_action']
    with PRIVATE_CSV.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=private_fields)
        w.writeheader()
        for row in out_rows:
            w.writerow({k: public_row(row).get(k) for k in private_fields})
    os.chmod(PRIVATE_CSV, 0o600)

    public_rows = [public_row(r) for r in out_rows]
    payload = {
        'generated_at': utc_now(),
        'status': 'gmc_local_cd_shopify_live_preview_readonly',
        'scope': 'Read-only Shopify live validation for Merchant local packages C/D after LIA_ normalization',
        'source_labels': ['fact_merchant_center', 'fact_shopify', 'fact_tiny_stock_local_snapshot', 'derived_reconciliation', 'manual_approval_required'],
        'summary': {
            'merchant_products_read': len(products),
            'merchant_statuses_read': len(statuses),
            'local_cd_rows_evaluated': len(out_rows),
            'unique_normalized_skus_queried_in_shopify_live': len(unique_skus),
            'package_counts': dict(package_counts),
            'decision_state_counts': dict(counts),
            'decision_state_counts_by_package': {pkg: dict(cnt) for pkg, cnt in decision_by_package.items()},
            'safe_noop_after_shopify_live_count': len(safe_noop),
            'cleanup_candidate_after_pos_validation_count': len(cleanup_candidates),
            'non_active_shopify_review_count': len(non_active_review),
            'tiny_present_review_count': len(tiny_review),
            'merchant_writes': 0,
            'shopify_writes': 0,
            'feed_writes': 0,
            'pos_or_local_inventory_writes': 0,
            'database_writes': 0,
            'external_sends': 0,
        },
        'interpretation': {
            'primary_finding': 'Most C/D local rows are valid after Shopify live exact-SKU validation; the earlier local queue was inflated by Data Spine/local snapshot drift, not necessarily stale local inventory.',
            'safe_policy': 'Preserve local listings that have a Shopify live ACTIVE exact SKU. Do not delete or change local/POS rows without POS/Tiny validation plus explicit package approval.',
            'recommended_next_step': 'Update the local Data Spine/diagnostic classifier to treat Shopify-live exact SKU as a no-op validity guard, then only build an approval packet for the small residual cleanup-candidate set after POS/Tiny validation.',
        },
        'samples': {
            'safe_noop': [public_row(r) for r in safe_noop[:20]],
            'cleanup_candidates_after_pos_validation': [public_row(r) for r in cleanup_candidates[:20]],
            'non_active_shopify_review': [public_row(r) for r in non_active_review[:20]],
            'tiny_present_review': [public_row(r) for r in tiny_review[:20]],
        },
        'private_csv': str(PRIVATE_CSV),
        'not_performed': ['merchant_product_delete','merchant_product_update','content_api_custombatch','feed_update','shopify_write','database_write','local_inventory_disable','pos_inventory_write','campaign_or_external_send'],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    public_fields = private_fields
    with OUT_CSV.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=public_fields)
        w.writeheader()
        for row in public_rows:
            w.writerow({k: row.get(k) for k in public_fields})

    lines = [
        '# LK GMC Local C/D Shopify Live Preview, 2026-05-12', '',
        f"Status: `{payload['status']}`", '',
        '## Resumo executivo',
        f"- Produtos Merchant lidos: {len(products)}",
        f"- Linhas local C/D avaliadas: {len(out_rows)}",
        f"- SKUs normalizados consultados no Shopify live: {len(unique_skus)}",
        f"- Pacotes: {dict(package_counts)}",
        f"- Estados: {dict(counts)}",
        '- Merchant/Shopify/feed/POS/DB writes: 0', '',
        '## Veredito operacional',
        f"- Validar por Shopify live reduziu o risco local: {len(safe_noop)} linhas têm SKU exato ativo no Shopify e devem ser preservadas como `noop/valid`.",
        f"- Restam {len(cleanup_candidates)} candidatos sem SKU exato no Shopify live e sem match Tiny local; ainda são apenas candidatos e exigem validação POS/Tiny antes de qualquer cleanup.",
        f"- {len(non_active_review)} linhas têm SKU no Shopify mas produto não ativo; revisão manual/POS antes de mexer no local.",
        f"- {len(tiny_review)} linhas têm sinal Tiny local sem Shopify live; revisar mapeamento antes de mexer no Merchant.", '',
        '## Próximo bloco seguro',
        '- Não executar C/D como delete/update em massa.',
        '- Incorporar esta validação Shopify-live no classificador para que Data Spine drift não gere falsos positivos.',
        '- Só depois montar pacote residual com rollback para os candidatos que também falharem em POS/Tiny.', '',
        '## Arquivos',
        f"- JSON público: `{OUT_JSON}`",
        f"- CSV público: `{OUT_CSV}`",
        f"- CSV privado/auditoria chmod 600: `{PRIVATE_CSV}`", '',
        '## Não executado',
    ]
    for item in payload['not_performed']:
        lines.append(f'- {item}')
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(OUT_MD.read_text(encoding='utf-8'), encoding='utf-8')

    if CONTROL.exists():
        marker = '### 2026-05-12 — GMC local C/D Shopify live preview'
        text = CONTROL.read_text(encoding='utf-8')
        block = (
            f"\n{marker}\n\n"
            f"- Status: preview read-only/local concluído.\n"
            f"- Local C/D avaliados: {len(out_rows)}; pacotes {dict(package_counts)}.\n"
            f"- Shopify live validou como no-op/valid: {len(safe_noop)}.\n"
            f"- Candidatos residuais após POS/Tiny: {len(cleanup_candidates)}; nenhum write executado.\n"
            f"- Próximo: atualizar classificador/approval packet residual, mantendo local inventory preservado por padrão.\n\n"
        )
        if marker not in text:
            CONTROL.write_text(text.rstrip() + block, encoding='utf-8')

    if INDEX.exists():
        text = INDEX.read_text(encoding='utf-8')
        line = '| LK GMC Local C/D Shopify Live Preview 2026-05-12 | `areas/lk/rotinas/gmc-2026-05-12-local-cd-shopify-live-preview.md` | Preview read-only dos pacotes locais C/D com validação Shopify live por SKU normalizado `LIA_`, preservando local listings válidos e sem writes |'
        if line not in text:
            INDEX.write_text(text.rstrip() + '\n' + line + '\n', encoding='utf-8')

    print(json.dumps({'status': payload['status'], 'summary': payload['summary'], 'public_report': str(OUT_MD)}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
