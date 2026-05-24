#!/usr/bin/env python3
"""Execute LK GMC package A online stale triage with rollback evidence.

Approved scope: A_online_stale_triage only.
Deletes exact Merchant online product IDs classified as online_unmatched_possible_stale.
No local, Shopify, feed, DB, POS, GMB or campaign writes.
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import os
import pathlib
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
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
RUN_STAMP = '2026-05-12-package-a-online-stale-triage'
PACKAGE = 'A_online_stale_triage'
PUBLIC_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
PUBLIC_CSV = ROOT / f'reports/lk-gmc-{RUN_STAMP}.csv'
PUBLIC_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
CONTROL = ROOT / 'areas/lk/projetos/lk-os-implementation-control.md'
INDEX = ROOT / 'empresa/rotinas/_index.md'


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_audit_module():
    spec = importlib.util.spec_from_file_location('lk_gmc_catalog_duplication_audit', AUDIT_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def get_json(url: str, token: str) -> dict[str, Any]:
    req = urllib.request.Request(url)
    req.add_header('Authorization', 'Bearer ' + token)
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode())


def delete_product(merchant_id: str, product_id: str, token: str) -> dict[str, Any]:
    url = f'https://shoppingcontent.googleapis.com/content/v2.1/{merchant_id}/products/' + urllib.parse.quote(product_id, safe='')
    req = urllib.request.Request(url, method='DELETE')
    req.add_header('Authorization', 'Bearer ' + token)
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            raw = r.read().decode()
            return {'http_status': r.status, 'body': json.loads(raw) if raw else {}}
    except urllib.error.HTTPError as e:
        raw = e.read().decode(errors='replace')
        if e.code == 404:
            return {'http_status': 404, 'body': {}, 'already_absent': True}
        raise RuntimeError(f'http_{e.code}: {raw[:1000]}') from e


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


def load_plan(current_products: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    data = json.loads(SNAPSHOT.read_text(encoding='utf-8'))
    current_ids = {p.get('id') for p in current_products}
    rows = [r for r in data.get('records', []) if r.get('package') == PACKAGE]
    plan: list[dict[str, Any]] = []
    counters: Counter[str] = Counter()
    for rec in rows:
        p = rec.get('merchant_product_resource') or {}
        c = rec.get('classification') or {}
        pid = p.get('id') or c.get('product_id')
        if p.get('channel') != 'online' or not str(pid).startswith('online:pt:BR:'):
            counters['skipped_non_online'] += 1
            continue
        if pid not in current_ids:
            counters['skipped_already_absent'] += 1
            continue
        plan.append({
            'package': PACKAGE,
            'product_id': pid,
            'offer_id': p.get('offerId'),
            'title': p.get('title'),
            'priority': c.get('priority'),
            'bucket': c.get('bucket'),
            'item_issue_count': c.get('item_issue_count'),
            'rollback_original_product': p,
            'rollback_original_status': rec.get('merchant_product_status') or {},
            'execution_status': 'planned_not_executed',
        })
        counters['planned'] += 1
    return plan, {'snapshot_a_records': len(rows), 'counters': dict(counters)}


def write_outputs(mode: str, summary: dict[str, Any], plan: list[dict[str, Any]], private_records: list[dict[str, Any]]) -> None:
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE_DIR, 0o700)
    private_path = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-rollback.json'
    private_payload = {
        'generated_at': utc_now(),
        'mode': mode,
        'scope': PACKAGE,
        'rollback_note': 'For applied rows: reinsert rollback_original_product if rollback is needed.',
        'records': private_records,
    }
    private_path.write_text(json.dumps(private_payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    os.chmod(private_path, 0o600)

    public_rows = [{
        'product_id': r.get('product_id'),
        'offer_id': r.get('offer_id'),
        'title': r.get('title'),
        'priority': r.get('priority'),
        'bucket': r.get('bucket'),
        'execution_status': r.get('execution_status'),
        'delete_status': r.get('delete_status'),
        'verified_absent_live': r.get('verified_absent_live'),
        'error_class': r.get('error_class'),
    } for r in plan]
    payload = {
        'generated_at': utc_now(),
        'status': 'gmc_package_a_online_stale_triage_applied_verified' if mode == 'apply' else 'gmc_package_a_online_stale_triage_dry_run_ready',
        'scope': PACKAGE,
        'source_labels': ['fact_merchant_center', 'derived_reconciliation', 'manual_approval_lucas_2026_05_12'],
        'summary': summary | {'private_rollback_path': str(private_path)},
        'public_rows': public_rows,
        'not_touched': ['local_channel', 'shopify', 'feed', 'database', 'campaign_or_external_send', 'google_business_profile', 'pos_inventory'],
    }
    PUBLIC_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    fields = ['product_id', 'offer_id', 'title', 'priority', 'bucket', 'execution_status', 'delete_status', 'verified_absent_live', 'error_class']
    with PUBLIC_CSV.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for row in public_rows:
            w.writerow(row)
    lines = [
        '# LK GMC Package A Online Stale Triage, 2026-05-12', '',
        f"Status: `{payload['status']}`", '',
        '## Resumo executivo',
        f'- Pacote: `{PACKAGE}`',
        f'- Modo: `{mode}`',
        f"- Registros A no snapshot: {summary.get('snapshot_a_records')}",
        f"- Planejados/aplicados: {summary.get('planned')}",
        f"- Deletes Merchant OK: {summary.get('delete_ok', 0)}",
        f"- Já ausentes antes da execução: {summary.get('already_absent', 0)}",
        f"- Verificados ausentes no final: {summary.get('verified_absent_live', 0)}",
        f"- Falhas finais: {summary.get('failed', 0)}",
        f"- Snapshot privado de rollback: `{private_path}`", '',
        '## Interpretação',
        '- Executei apenas product IDs online exatos do bucket A online_unmatched_possible_stale.',
        '- Não mexi no canal local nem em Shopify/feed/banco/POS.', '',
        '## Não tocado',
    ]
    for item in payload['not_touched']:
        lines.append(f'- {item}')
    lines.extend(['', '## Arquivos', f'- JSON: `{PUBLIC_JSON}`', f'- CSV: `{PUBLIC_CSV}`'])
    PUBLIC_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(PUBLIC_MD.read_text(encoding='utf-8'), encoding='utf-8')
    if CONTROL.exists():
        marker = '### 2026-05-12 — GMC Package A online stale triage execution'
        text = CONTROL.read_text(encoding='utf-8')
        block = f"\n{marker}\n\n- Status: {payload['status']}.\n- Escopo aprovado por Lucas: `{PACKAGE}` online.\n- Deletes OK={summary.get('delete_ok',0)}, verificados ausentes={summary.get('verified_absent_live',0)}, falhas={summary.get('failed',0)}.\n- Snapshot privado de rollback: `{private_path}`.\n- Não tocado: local, Shopify, feed, banco, campanhas, GMB/POS.\n\n"
        if marker not in text:
            CONTROL.write_text(text.rstrip() + block, encoding='utf-8')
    if INDEX.exists():
        line = f'| LK GMC Package A Online Stale Triage 2026-05-12 | `areas/lk/rotinas/gmc-{RUN_STAMP}.md` | Execução controlada do pacote A online stale por product IDs exatos, rollback privado, sem tocar local/Shopify/feed/banco |'
        text = INDEX.read_text(encoding='utf-8')
        if line not in text:
            INDEX.write_text(text.rstrip() + '\n' + line + '\n', encoding='utf-8')


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--max', type=int, default=0)
    ap.add_argument('--sleep', type=float, default=0.02)
    args = ap.parse_args()
    audit = load_audit_module()
    secrets = audit.load_doppler()
    merchant_id = secrets.get('MERCHANT_CENTER_ID_LK')
    if not merchant_id:
        raise RuntimeError('missing_merchant_center_id')
    token = audit.google_access_token(audit.parse_service_account(secrets))
    before = list_all_products(merchant_id, token)
    plan, base = load_plan(before)
    if args.max and args.max > 0:
        plan = plan[:args.max]
    summary = {
        'mode': 'apply' if args.apply else 'dry_run',
        'merchant_products_before_read': len(before),
        **base,
        'planned': len(plan),
    }
    private_records: list[dict[str, Any]] = []
    if args.apply:
        for row in plan:
            row['started_at'] = utc_now()
            try:
                res = delete_product(merchant_id, row['product_id'], token)
                if res.get('already_absent'):
                    row['delete_status'] = 'already_absent_404'
                    row['execution_status'] = 'already_absent_before_delete'
                    summary['already_absent'] = summary.get('already_absent', 0) + 1
                else:
                    row['delete_status'] = 'ok'
                    row['execution_status'] = 'applied_delete_exact_product_id'
                    summary['delete_ok'] = summary.get('delete_ok', 0) + 1
            except Exception as e:
                row['delete_status'] = 'failed'
                row['execution_status'] = 'failed_old_intact_or_unknown'
                row['error_class'] = 'delete_failed'
                row['error_message'] = str(e)[:800]
                summary['failed'] = summary.get('failed', 0) + 1
            row['finished_at'] = utc_now()
            private_records.append(row)
            time.sleep(args.sleep)
        # Verify via full product listing after a consistency delay.
        time.sleep(20)
        after = list_all_products(merchant_id, token)
        live_ids = {p.get('id') for p in after}
        verified = 0
        anomalies = 0
        for row in plan:
            absent = row['product_id'] not in live_ids
            row['verified_absent_live'] = absent
            if absent:
                verified += 1
            else:
                anomalies += 1
        summary['merchant_products_after_read'] = len(after)
        summary['verified_absent_live'] = verified
        summary['verification_anomalies'] = anomalies
        if anomalies:
            summary['failed'] = summary.get('failed', 0) + anomalies
    else:
        for row in plan:
            row['execution_status'] = 'dry_run_not_executed'
            private_records.append(row)
    write_outputs('apply' if args.apply else 'dry_run', summary, plan, private_records)
    print(json.dumps({'status': 'ok', 'summary': summary, 'public_report': str(PUBLIC_MD)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
