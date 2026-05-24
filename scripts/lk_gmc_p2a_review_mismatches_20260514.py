#!/usr/bin/env python3
"""Read-only verifier for LK GMC P2A finalize mismatches.

Does not patch/delete/write Merchant. It reads the private progress JSONL from the approved
P2A finalize executor, fetches current Merchant ProductInput attributes, and writes a
private/local mismatch report for diagnosis.
"""
from __future__ import annotations

import importlib.util
import json
import pathlib
import time
from collections import Counter
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
P2_PATH = ROOT / 'scripts/lk_gmc_p2_category_product_type_executor_20260513.py'
PROGRESS = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-13-p2a-finalize-remaining-online-progress-20260513T202857Z.jsonl')
OUT_JSON = ROOT / 'reports/lk-gmc-2026-05-14-p2a-128-mismatch-readonly-review.json'
OUT_MD = ROOT / 'reports/lk-gmc-2026-05-14-p2a-128-mismatch-readonly-review.md'

def load_mod(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(mod)
    return mod

def merchant_attrs(p2, mid: str, token: str, product_id: str) -> dict:
    _name, encoded, *_ = p2.product_input_name(mid, product_id)
    return (p2.merchant_product_get(mid, encoded, token).get('productAttributes') or {})

def refresh_token(w, audit, secrets):
    return audit.google_access_token(audit.parse_service_account(secrets))

def main():
    p2 = load_mod(P2_PATH, 'p2_review')
    w = p2.import_w4()
    audit = w.import_audit()
    secrets = audit.load_doppler()
    mid = secrets.get('MERCHANT_CENTER_ID_LK')
    token = refresh_token(w, audit, secrets)

    rows = [json.loads(line) for line in PROGRESS.read_text(encoding='utf-8').splitlines() if line.strip()]
    patched = [r for r in rows if r.get('execution_status') == 'patched_p2a_finalize_v1']
    mismatches = []
    verified = 0
    failed = []
    for idx, r in enumerate(patched, 1):
        if idx % 500 == 0:
            print(json.dumps({'phase': 'verify_readonly', 'checked': idx, 'total': len(patched), 'mismatches': len(mismatches)}, ensure_ascii=False), flush=True)
            token = refresh_token(w, audit, secrets)
        try:
            fresh = merchant_attrs(p2, mid, token, r['product_id'])
            actual_gpc = fresh.get('googleProductCategory')
            actual_pts = fresh.get('productTypes') or []
            ok = actual_gpc == r.get('expected_googleProductCategory') and actual_pts == (r.get('expected_productTypes') or [])
            verified += 1
            if not ok:
                mismatches.append({
                    'product_id': r['product_id'],
                    'expected_googleProductCategory': r.get('expected_googleProductCategory'),
                    'actual_googleProductCategory': actual_gpc,
                    'expected_productTypes': r.get('expected_productTypes') or [],
                    'actual_productTypes': actual_pts,
                })
        except Exception as e:
            failed.append({'product_id': r.get('product_id'), 'error': str(e)[:800]})
        time.sleep(0.03)

    pattern_counts = Counter(
        (
            m['expected_googleProductCategory'],
            tuple(m['expected_productTypes']),
            m['actual_googleProductCategory'],
            tuple(m['actual_productTypes']),
        ) for m in mismatches
    )
    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'mode': 'readonly_mismatch_review',
        'source_progress': str(PROGRESS),
        'total_patched_rows': len(patched),
        'verified_merchant_product_get': verified,
        'mismatch_count': len(mismatches),
        'failed_count': len(failed),
        'pattern_counts': [
            {
                'count': c,
                'expected_googleProductCategory': pat[0],
                'expected_productTypes': list(pat[1]),
                'actual_googleProductCategory': pat[2],
                'actual_productTypes': list(pat[3]),
            }
            for pat, c in pattern_counts.most_common()
        ],
        'mismatches': mismatches,
        'failed': failed,
        'not_performed': ['merchant_patch', 'merchant_delete', 'title_update', 'price_update', 'availability_update', 'shopify_write', 'tiny_write', 'notion_write', 'marketplace_lookup'],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    lines = [
        '# LK GMC P2A — Read-only mismatch review 2026-05-14',
        '',
        f"Status: `readonly_completed{'_with_failures' if failed else ''}`",
        '',
        '## Summary',
        f"- total_patched_rows: {len(patched)}",
        f"- verified_merchant_product_get: {verified}",
        f"- mismatch_count: {len(mismatches)}",
        f"- failed_count: {len(failed)}",
        '',
        '## Top mismatch patterns',
    ]
    for item in payload['pattern_counts'][:20]:
        lines.append(f"- {item['count']} × expected `{item['expected_googleProductCategory']} / {item['expected_productTypes']}` vs actual `{item['actual_googleProductCategory']} / {item['actual_productTypes']}`")
    lines += ['', '## Not performed'] + [f"- {x}" for x in payload['not_performed']]
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(json.dumps({'status': 'readonly_completed', 'json': str(OUT_JSON), 'md': str(OUT_MD), 'mismatch_count': len(mismatches), 'failed_count': len(failed)}, ensure_ascii=False), flush=True)

if __name__ == '__main__':
    main()
