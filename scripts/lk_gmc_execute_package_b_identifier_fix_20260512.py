#!/usr/bin/env python3
"""Execute LK GMC package B online identifier fixes with rollback evidence.

Approved scope: package B_online_identifier_fix only.

What this script does in --apply mode:
- Finds unambiguous online identifier mismatches where the current Merchant offerId
  maps to exactly one Shopify/Data Spine SKU via link variant, unique GTIN, or a
  single product SKU prefix.
- Inserts a replacement Merchant product with the corrected offerId/SKU.
- Deletes the old Merchant product only after the replacement insert succeeds.
- Writes private rollback records and public sanitized reports.

What this script never does:
- local channel writes
- Shopify writes
- feed writes/fetchNow
- database writes
- campaign/customer sends
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import os
import pathlib
import sqlite3
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / 'scripts/lk_gmc_catalog_duplication_audit_20260512.py'
SNAPSHOT = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-executable-previews-rollback-2026-05-12.json')
LOCAL_DB = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite')
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
RUN_STAMP = '2026-05-12-package-b-identifier-fix'
PUBLIC_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
PUBLIC_CSV = ROOT / f'reports/lk-gmc-{RUN_STAMP}.csv'
PUBLIC_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
CONTROL = ROOT / 'areas/lk/projetos/lk-os-implementation-control.md'
INDEX = ROOT / 'empresa/rotinas/_index.md'
PACKAGE = 'B_online_identifier_fix'


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_audit_module():
    spec = importlib.util.spec_from_file_location('lk_gmc_catalog_duplication_audit', AUDIT_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def load_snapshot() -> list[dict[str, Any]]:
    data = json.loads(SNAPSHOT.read_text(encoding='utf-8'))
    return [r for r in data.get('records', []) if r.get('package') == PACKAGE]


def get_json(url: str, token: str) -> dict[str, Any]:
    req = urllib.request.Request(url)
    req.add_header('Authorization', 'Bearer ' + token)
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode())


def send_json(url: str, token: str, method: str, body: dict[str, Any] | None = None) -> dict[str, Any]:
    data = None if body is None else json.dumps(body, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header('Authorization', 'Bearer ' + token)
    if body is not None:
        req.add_header('Content-Type', 'application/json; charset=utf-8')
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            raw = r.read().decode()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        raw = e.read().decode(errors='replace')
        raise RuntimeError(f'http_{e.code}: {raw[:1000]}') from e


def delete_product(merchant_id: str, product_id: str, token: str) -> dict[str, Any]:
    pid = urllib.parse.quote(product_id, safe='')
    url = f'https://shoppingcontent.googleapis.com/content/v2.1/{merchant_id}/products/{pid}'
    return send_json(url, token, 'DELETE')


def insert_product(merchant_id: str, product: dict[str, Any], token: str) -> dict[str, Any]:
    url = f'https://shoppingcontent.googleapis.com/content/v2.1/{merchant_id}/products'
    return send_json(url, token, 'POST', product)


def list_all_products(merchant_id: str, token: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    page_token = None
    for _ in range(500):
        qs = {'maxResults': '250'}
        if page_token:
            qs['pageToken'] = page_token
        url = f'https://shoppingcontent.googleapis.com/content/v2.1/{merchant_id}/products?' + urllib.parse.urlencode(qs)
        data = get_json(url, token)
        batch = data.get('resources') or []
        rows.extend(batch)
        page_token = data.get('nextPageToken')
        if not page_token or not batch:
            break
    return rows


def variant_id_from_link(link: str) -> str:
    try:
        return (urllib.parse.parse_qs(urllib.parse.urlparse(link or '').query).get('variant') or [''])[0]
    except Exception:
        return ''


def resolve_target_sku(cur: sqlite3.Cursor, product: dict[str, Any]) -> tuple[str | None, str, dict[str, Any]]:
    offer = str(product.get('offerId') or '')
    item_group = str(product.get('itemGroupId') or '')
    gtin = str(product.get('gtin') or '')
    variant = variant_id_from_link(product.get('link') or '')

    if variant:
        rows = [dict(x) for x in cur.execute(
            """
            select v.*, p.status as pstatus, p.title as ptitle, p.source_product_id as p_source_product_id
            from lk_product_variants v left join lk_products p on v.product_id=p.product_id
            where v.source_variant_id=? or v.variant_id=?
            """,
            (variant, variant),
        )]
        rows = [r for r in rows if r.get('sku')]
        if len(rows) == 1:
            return str(rows[0]['sku']), 'link_variant_to_shopify_sku', rows[0]

    if gtin:
        rows = [dict(x) for x in cur.execute(
            """
            select v.*, p.status as pstatus, p.title as ptitle, p.source_product_id as p_source_product_id
            from lk_product_variants v left join lk_products p on v.product_id=p.product_id
            where v.barcode=?
            """,
            (gtin,),
        )]
        active = [r for r in rows if str(r.get('pstatus') or '').lower() == 'active' and r.get('sku')]
        if len(active) == 1:
            return str(active[0]['sku']), 'unique_gtin_to_active_shopify_sku', active[0]

    if item_group:
        rows = [dict(x) for x in cur.execute(
            """
            select v.*, p.status as pstatus, p.title as ptitle, p.source_product_id as p_source_product_id
            from lk_product_variants v left join lk_products p on v.product_id=p.product_id
            where (p.source_product_id=? or p.product_id=?) and v.sku like ?
            """,
            (item_group, item_group, offer + '-%'),
        )]
        rows = [r for r in rows if r.get('sku')]
        if len(rows) == 1:
            return str(rows[0]['sku']), 'single_product_sku_prefix', rows[0]

    return None, 'no_unambiguous_target', {}


def replacement_product(product: dict[str, Any], target_offer_id: str) -> dict[str, Any]:
    # Keep accepted product attributes; remove output-only identifiers.
    out = json.loads(json.dumps(product, ensure_ascii=False))
    for k in ['id', 'kind', 'source']:
        out.pop(k, None)
    out['offerId'] = target_offer_id
    # Align MPN with corrected SKU only when the old MPN equals the old offerId.
    if str(product.get('mpn') or '') == str(product.get('offerId') or ''):
        out['mpn'] = target_offer_id
    return out


def build_plan(current_products: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    snapshot_records = load_snapshot()
    current_ids = {p.get('id') for p in current_products}
    con = sqlite3.connect(str(LOCAL_DB))
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    plan: list[dict[str, Any]] = []
    counters: Counter[str] = Counter()
    for rec in snapshot_records:
        p = rec.get('merchant_product_resource') or {}
        classification = rec.get('classification') or {}
        old_pid = p.get('id') or classification.get('product_id')
        if p.get('channel') != 'online' or not str(old_pid).startswith('online:pt:BR:'):
            counters['skipped_non_online'] += 1
            continue
        if old_pid not in current_ids:
            counters['skipped_old_not_current'] += 1
            continue
        target_sku, reason, matched_variant = resolve_target_sku(cur, p)
        if not target_sku:
            counters['skipped_no_unambiguous_target'] += 1
            continue
        if target_sku == p.get('offerId'):
            counters['skipped_already_correct'] += 1
            continue
        new_pid = f"online:{p.get('contentLanguage') or 'pt'}:{p.get('targetCountry') or 'BR'}:{target_sku}"
        if new_pid in current_ids:
            counters['skipped_target_already_exists'] += 1
            continue
        new_product = replacement_product(p, target_sku)
        plan.append({
            'package': PACKAGE,
            'old_product_id': old_pid,
            'old_offer_id': p.get('offerId'),
            'new_product_id': new_pid,
            'new_offer_id': target_sku,
            'title': p.get('title'),
            'resolution_reason': reason,
            'variant_from_link': variant_id_from_link(p.get('link') or ''),
            'shopify_sku': target_sku,
            'shopify_source_variant_id': matched_variant.get('source_variant_id'),
            'shopify_variant_id': matched_variant.get('variant_id'),
            'shopify_product_id': matched_variant.get('product_id'),
            'barcode': matched_variant.get('barcode'),
            'merchant_gtin': p.get('gtin'),
            'replacement_product': new_product,
            'rollback_original_product': p,
            'rollback_original_status': rec.get('merchant_product_status') or {},
            'execution_status': 'planned_not_executed',
        })
        counters['planned'] += 1
        counters[reason] += 1
    con.close()
    return plan, {'snapshot_b_records': len(snapshot_records), 'counters': dict(counters)}


def write_outputs(mode: str, summary: dict[str, Any], plan: list[dict[str, Any]], private_records: list[dict[str, Any]]) -> None:
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE_DIR, 0o700)
    private_path = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-rollback.json'
    private_payload = {
        'generated_at': utc_now(),
        'mode': mode,
        'scope': PACKAGE,
        'rollback_note': 'For applied rows: reinsert rollback_original_product and delete new_product_id if rollback is needed.',
        'records': private_records,
    }
    private_path.write_text(json.dumps(private_payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    os.chmod(private_path, 0o600)

    public_rows = []
    for r in plan:
        public_rows.append({
            'old_product_id': r['old_product_id'],
            'old_offer_id': r['old_offer_id'],
            'new_product_id': r['new_product_id'],
            'new_offer_id': r['new_offer_id'],
            'title': r['title'],
            'resolution_reason': r['resolution_reason'],
            'execution_status': r.get('execution_status'),
            'insert_status': r.get('insert_status'),
            'delete_status': r.get('delete_status'),
            'error_class': r.get('error_class'),
        })
    payload = {
        'generated_at': utc_now(),
        'status': 'gmc_package_b_identifier_fix_applied' if mode == 'apply' else 'gmc_package_b_identifier_fix_dry_run_ready',
        'scope': PACKAGE,
        'source_labels': ['fact_merchant_center', 'fact_shopify_local_snapshot', 'derived_reconciliation', 'manual_approval_lucas_2026_05_12'],
        'summary': summary | {'private_rollback_path': str(private_path)},
        'public_rows': public_rows,
        'not_touched': ['local_channel', 'shopify', 'feed', 'database', 'campaign_or_external_send', 'google_business_profile', 'pos_inventory'],
    }
    PUBLIC_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    fields = ['old_product_id', 'old_offer_id', 'new_product_id', 'new_offer_id', 'title', 'resolution_reason', 'execution_status', 'insert_status', 'delete_status', 'error_class']
    with PUBLIC_CSV.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for row in public_rows:
            w.writerow(row)
    lines = [
        '# LK GMC Package B Identifier Fix, 2026-05-12', '',
        f"Status: `{payload['status']}`", '',
        '## Resumo executivo',
        f"- Pacote: `{PACKAGE}`",
        f"- Modo: `{mode}`",
        f"- Registros B no snapshot: {summary.get('snapshot_b_records')}",
        f"- Candidatos unambíguos planejados: {summary.get('planned')}",
        f"- Inserções Merchant OK: {summary.get('insert_ok', 0)}",
        f"- Deletes Merchant antigos OK: {summary.get('delete_ok', 0)}",
        f"- Falhas: {summary.get('failed', 0)}",
        f"- Snapshot privado de rollback: `{private_path}`", '',
        '## Interpretação',
        '- Executei apenas correções online com SKU alvo unambíguo no Data Spine/Shopify local.',
        '- Itens B ambíguos foram preservados para investigação; não forcei mapping por inferência fraca.', '',
        '## Não tocado',
    ]
    for item in payload['not_touched']:
        lines.append(f'- {item}')
    lines.extend(['', '## Arquivos', f'- JSON: `{PUBLIC_JSON}`', f'- CSV: `{PUBLIC_CSV}`'])
    PUBLIC_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(PUBLIC_MD.read_text(encoding='utf-8'), encoding='utf-8')

    if CONTROL.exists():
        marker = '### 2026-05-12 — GMC Package B identifier fix execution'
        text = CONTROL.read_text(encoding='utf-8')
        block = f"\n{marker}\n\n- Status: {payload['status']}.\n- Escopo aprovado por Lucas: `{PACKAGE}` online.\n- Aplicados: insert_ok={summary.get('insert_ok',0)}, delete_ok={summary.get('delete_ok',0)}, falhas={summary.get('failed',0)}; candidatos unambíguos={summary.get('planned')}.\n- Snapshot privado de rollback: `{private_path}`.\n- Não tocado: local, Shopify, feed, banco, campanhas, GMB/POS.\n\n"
        if marker not in text:
            CONTROL.write_text(text.rstrip() + block, encoding='utf-8')
    if INDEX.exists():
        line = f'| LK GMC Package B Identifier Fix 2026-05-12 | `areas/lk/rotinas/gmc-{RUN_STAMP}.md` | Execução controlada do pacote B online: correção por SKU alvo unambíguo, rollback privado, sem tocar local/Shopify/feed/banco |'
        text = INDEX.read_text(encoding='utf-8')
        if line not in text:
            INDEX.write_text(text.rstrip() + '\n' + line + '\n', encoding='utf-8')


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true', help='execute Merchant insert/delete for approved unambiguous package B rows')
    ap.add_argument('--max', type=int, default=0, help='optional max rows to apply, 0 means all planned')
    ap.add_argument('--sleep', type=float, default=0.05, help='sleep between write calls')
    args = ap.parse_args()

    audit = load_audit_module()
    secrets = audit.load_doppler()
    merchant_id = secrets.get('MERCHANT_CENTER_ID_LK')
    if not merchant_id:
        raise RuntimeError('missing_merchant_center_id')
    token = audit.google_access_token(audit.parse_service_account(secrets))
    current_products = list_all_products(merchant_id, token)
    plan, base_summary = build_plan(current_products)
    if args.max and args.max > 0:
        plan = plan[:args.max]
    summary = {
        'mode': 'apply' if args.apply else 'dry_run',
        'merchant_products_current_read': len(current_products),
        **base_summary,
        'planned': len(plan),
    }
    private_records: list[dict[str, Any]] = []

    if args.apply:
        for row in plan:
            started = utc_now()
            try:
                inserted = insert_product(merchant_id, row['replacement_product'], token)
                row['insert_status'] = 'ok'
                row['inserted_product_id'] = inserted.get('id') or row['new_product_id']
                time.sleep(args.sleep)
                try:
                    delete_product(merchant_id, row['old_product_id'], token)
                    row['delete_status'] = 'ok'
                    row['execution_status'] = 'applied_insert_new_delete_old'
                    summary['insert_ok'] = summary.get('insert_ok', 0) + 1
                    summary['delete_ok'] = summary.get('delete_ok', 0) + 1
                except Exception as delete_err:
                    row['delete_status'] = 'failed'
                    row['error_class'] = 'delete_old_failed_after_insert'
                    row['error_message'] = str(delete_err)[:800]
                    # Roll back the new duplicate if old deletion failed.
                    try:
                        delete_product(merchant_id, row['new_product_id'], token)
                        row['rollback_new_delete_status'] = 'ok'
                        row['execution_status'] = 'rolled_back_new_after_delete_old_failed'
                    except Exception as rollback_err:
                        row['rollback_new_delete_status'] = 'failed'
                        row['rollback_error_message'] = str(rollback_err)[:800]
                        row['execution_status'] = 'needs_manual_review_duplicate_possible'
                    summary['failed'] = summary.get('failed', 0) + 1
            except Exception as insert_err:
                row['insert_status'] = 'failed'
                row['delete_status'] = 'not_attempted'
                row['execution_status'] = 'failed_before_delete_old_intact'
                row['error_class'] = 'insert_new_failed'
                row['error_message'] = str(insert_err)[:800]
                summary['failed'] = summary.get('failed', 0) + 1
            row['started_at'] = started
            row['finished_at'] = utc_now()
            private_records.append(row)
            time.sleep(args.sleep)
    else:
        for row in plan:
            row['execution_status'] = 'dry_run_not_executed'
            private_records.append(row)

    write_outputs('apply' if args.apply else 'dry_run', summary, plan, private_records)
    print(json.dumps({'status': 'ok', 'summary': summary, 'public_report': str(PUBLIC_MD)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
