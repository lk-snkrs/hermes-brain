#!/usr/bin/env python3
"""Approved point repair for LK GMC P2A bag/wallet googleProductCategory mismatches.

Scope: exact 44 ProductInputs from read-only mismatch report where expected
Luggage & Bags > Handbags, Wallets & Cases but current googleProductCategory is null.
Writes only productAttributes.googleProductCategory + productAttributes.productTypes through
Merchant API v1 ProductInputs PATCH. No title/price/availability/delete/Shopify/Tiny/Notion.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import pathlib
import time
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
P2_PATH = ROOT / 'scripts/lk_gmc_p2_category_product_type_executor_20260513.py'
SOURCE_REVIEW = ROOT / 'reports/lk-gmc-2026-05-14-p2a-128-mismatch-readonly-review.json'
PUBLIC_JSON = ROOT / 'reports/lk-gmc-2026-05-14-p2a-bags-44-point-repair.json'
PUBLIC_MD = ROOT / 'reports/lk-gmc-2026-05-14-p2a-bags-44-point-repair.md'
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
APPROVAL_TEXT_REQUIRED = 'Fazer o 2'
# Google taxonomy canonical path for handbags/wallets; the earlier source expectation
# used a non-current `Luggage & Bags > ...` path that Merchant did not persist.
TARGET_GPC = 'Apparel & Accessories > Handbags, Wallets & Cases'
SOURCE_EXPECTED_GPC = 'Luggage & Bags > Handbags, Wallets & Cases'
TARGET_PT = ['Bolsa/Carteira']
NOT_PERFORMED = [
    'title_update', 'price_update', 'availability_update', 'image_or_link_update',
    'merchant_delete', 'local_inventory_write', 'shopify_write', 'tiny_write',
    'database_write', 'notion_write', 'feed_fetch_or_upload', 'campaign_or_message_send',
    'marketplace_lookup',
]

def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()

def load_mod(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(mod)
    return mod

def refresh_token(w, audit, secrets):
    return audit.google_access_token(audit.parse_service_account(secrets))

def merchant_attrs(p2, mid: str, token: str, product_id: str) -> dict[str, Any]:
    _name, encoded, *_ = p2.product_input_name(mid, product_id)
    return (p2.merchant_product_get(mid, encoded, token).get('productAttributes') or {})

def write_public(status: str, summary: dict[str, Any], rollback_path: pathlib.Path | None, progress_path: pathlib.Path | None, verify_results: list[dict[str, Any]]):
    payload = {
        'generated_at': utc_now(),
        'status': status,
        'source_review': str(SOURCE_REVIEW),
        'summary': summary,
        'private_rollback_snapshot_path': str(rollback_path) if rollback_path else None,
        'private_progress_path': str(progress_path) if progress_path else None,
        'verify_results': verify_results,
        'not_performed': NOT_PERFORMED,
    }
    PUBLIC_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    lines = [
        '# LK GMC P2A — Bags 44 point repair 2026-05-14', '',
        f"Status: `{status}`", '',
        '## Scope',
        '- Merchant API v1 ProductInputs PATCH.',
        f'- Exact selected products: {summary.get("selected_count", 0)}',
        f'- Target googleProductCategory: `{TARGET_GPC}`',
        f'- Target productTypes: `{TARGET_PT}`', '',
        '## Summary',
    ]
    for k, v in summary.items():
        lines.append(f'- {k}: {v}')
    lines += ['', '## Not performed'] + [f'- {x}' for x in NOT_PERFORMED]
    PUBLIC_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--approval-text', default='')
    ap.add_argument('--verify-delay', type=int, default=120)
    ap.add_argument('--sleep', type=float, default=0.20)
    args = ap.parse_args()
    if args.apply and args.approval_text.strip() != APPROVAL_TEXT_REQUIRED:
        raise RuntimeError('apply_blocked_missing_exact_approval_text: Fazer o 2')

    review = json.loads(SOURCE_REVIEW.read_text(encoding='utf-8'))
    selected = [m for m in review['mismatches'] if m.get('expected_googleProductCategory') == SOURCE_EXPECTED_GPC and m.get('actual_googleProductCategory') is None]
    selected = sorted(selected, key=lambda r: r['product_id'])
    if len(selected) != 44:
        raise RuntimeError(f'unexpected_selected_count:{len(selected)}')

    p2 = load_mod(P2_PATH, 'p2_bags_repair')
    w = p2.import_w4()
    audit = w.import_audit()
    secrets = audit.load_doppler()
    mid = secrets.get('MERCHANT_CENTER_ID_LK')
    token = refresh_token(w, audit, secrets)
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE_DIR, 0o700)
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    rollback_path = PRIVATE_DIR / f'lk-gmc-2026-05-14-p2a-bags-44-point-repair-rollback-{stamp}.json'
    progress_path = PRIVATE_DIR / f'lk-gmc-2026-05-14-p2a-bags-44-point-repair-progress-{stamp}.jsonl'

    preflight = []
    for idx, r in enumerate(selected, 1):
        if idx % 25 == 0:
            token = refresh_token(w, audit, secrets)
        attrs = merchant_attrs(p2, mid, token, r['product_id'])
        preflight.append({
            **r,
            'current_googleProductCategory': attrs.get('googleProductCategory'),
            'current_productTypes': attrs.get('productTypes') or [],
        })
        time.sleep(0.03)
    still_needs = [r for r in preflight if r['current_googleProductCategory'] != TARGET_GPC or r['current_productTypes'] != TARGET_PT]
    summary = {
        'mode': 'apply' if args.apply else 'dry-run',
        'selected_count': len(selected),
        'source_expected_googleProductCategory': SOURCE_EXPECTED_GPC,
        'target_googleProductCategory': TARGET_GPC,
        'still_needs_patch_preflight': len(still_needs),
        'preflight_current_patterns': dict(Counter(f"{r['current_googleProductCategory']} / {r['current_productTypes']}" for r in preflight)),
    }
    if not args.apply:
        write_public('dry_run_ready', summary, None, None, [])
        print(json.dumps({'status': 'dry_run_ready', 'summary': summary, 'report': str(PUBLIC_MD)}, ensure_ascii=False, indent=2), flush=True)
        return

    rollback_payload = {
        'generated_at': utc_now(),
        'approval_text': args.approval_text,
        'scope': 'exact 44 bags/wallets P2A point repair only',
        'target_googleProductCategory': TARGET_GPC,
        'target_productTypes': TARGET_PT,
        'records': preflight,
    }
    rollback_path.write_text(json.dumps(rollback_payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    os.chmod(rollback_path, 0o600)

    exec_results = []
    with progress_path.open('w', encoding='utf-8') as progress:
        os.chmod(progress_path, 0o600)
        for idx, r in enumerate(still_needs, 1):
            if idx % 25 == 0:
                token = refresh_token(w, audit, secrets)
            try:
                resp = p2.patch_category_product_types(mid, token, r['product_id'], TARGET_GPC, TARGET_PT)
                item = {'product_id': r['product_id'], 'execution_status': 'patched_bags_44_point_repair_v1', 'product_input': resp.get('name')}
            except Exception as e:
                item = {'product_id': r['product_id'], 'execution_status': 'failed_patch_bags_44_point_repair_v1', 'error': str(e)[:1200]}
            exec_results.append(item)
            progress.write(json.dumps(item, ensure_ascii=False) + '\n'); progress.flush()
            print(json.dumps({'phase': 'patch', 'idx': idx, 'total': len(still_needs), 'status': item['execution_status']}, ensure_ascii=False), flush=True)
            if item['execution_status'].startswith('failed'):
                summary.update({'execution_results_summary': dict(Counter(x['execution_status'] for x in exec_results))})
                write_public('apply_stopped_on_patch_failure', summary, rollback_path, progress_path, [])
                print(json.dumps({'status': 'apply_stopped_on_patch_failure', 'failed': item, 'progress': str(progress_path)}, ensure_ascii=False, indent=2), flush=True)
                return
            time.sleep(args.sleep)

    if args.verify_delay:
        print(json.dumps({'phase': 'verify_delay', 'seconds': args.verify_delay}, ensure_ascii=False), flush=True)
        time.sleep(args.verify_delay)
    token = refresh_token(w, audit, secrets)
    verify = []
    for idx, r in enumerate(still_needs, 1):
        if idx % 25 == 0:
            token = refresh_token(w, audit, secrets)
        attrs = merchant_attrs(p2, mid, token, r['product_id'])
        actual_gpc = attrs.get('googleProductCategory')
        actual_pts = attrs.get('productTypes') or []
        verify.append({
            'product_id': r['product_id'],
            'verify_status': 'verified_merchant_product_get',
            'actual_googleProductCategory': actual_gpc,
            'actual_productTypes': actual_pts,
            'match_expected': actual_gpc == TARGET_GPC and actual_pts == TARGET_PT,
        })
        time.sleep(0.03)
    summary.update({
        'execution_results_summary': dict(Counter(x['execution_status'] for x in exec_results)),
        'patched_count': sum(1 for x in exec_results if x['execution_status'] == 'patched_bags_44_point_repair_v1'),
        'verify_match_expected': sum(1 for x in verify if x['match_expected']),
        'verify_mismatch_count': sum(1 for x in verify if not x['match_expected']),
        'verify_patterns': dict(Counter(f"{x['actual_googleProductCategory']} / {x['actual_productTypes']}" for x in verify)),
    })
    status = 'apply_verified' if summary['verify_mismatch_count'] == 0 else 'apply_completed_needs_review'
    write_public(status, summary, rollback_path, progress_path, verify)
    print(json.dumps({'status': status, 'summary': summary, 'report': str(PUBLIC_MD), 'rollback': str(rollback_path), 'progress': str(progress_path)}, ensure_ascii=False, indent=2), flush=True)

if __name__ == '__main__':
    main()
