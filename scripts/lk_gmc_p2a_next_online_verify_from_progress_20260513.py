#!/usr/bin/env python3
"""Recover/verify LK GMC P2A next online execution from private progress JSONL.

Read-only verifier: no writes. Verifies productAttributes.googleProductCategory and
productAttributes.productTypes for progressed IDs using Merchant API v1 ProductInputs read.
"""
from __future__ import annotations
import argparse, importlib.util, json, pathlib, time
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
P2_PATH = ROOT / 'scripts/lk_gmc_p2_category_product_type_executor_20260513.py'
PUBLIC_JSON = ROOT / 'reports/lk-gmc-2026-05-13-p2a-next-online-timeout-recovered-fresh-verify.json'
PUBLIC_MD = ROOT / 'reports/lk-gmc-2026-05-13-p2a-next-online-timeout-recovered-fresh-verify.md'


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_mod(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(mod)
    return mod


def load_progress(path: pathlib.Path) -> list[dict[str, Any]]:
    rows=[]
    for line in path.read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        rows.append(json.loads(line))
    return rows


def merchant_attrs(p2, mid: str, token: str, pid: str) -> dict[str, Any]:
    _name, encoded, *_ = p2.product_input_name(mid, pid)
    return (p2.merchant_product_get(mid, encoded, token).get('productAttributes') or {})


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--progress', required=True)
    ap.add_argument('--sleep-per-row', type=float, default=0.03)
    args=ap.parse_args()
    progress_path=pathlib.Path(args.progress)
    p2=load_mod(P2_PATH,'p2verify')
    w=p2.import_w4(); audit=w.import_audit(); secrets=audit.load_doppler(); mid=secrets.get('MERCHANT_CENTER_ID_LK'); token=audit.google_access_token(audit.parse_service_account(secrets))
    rows=load_progress(progress_path)
    verify=[]
    for item in rows:
        pid=item.get('product_id')
        if item.get('execution_status')!='patched_p2a_next_v1':
            verify.append({**item,'verify_status':'skipped_non_patched'})
            continue
        try:
            attrs=merchant_attrs(p2, mid, token, pid)
            actual_gpc=attrs.get('googleProductCategory')
            actual_pts=attrs.get('productTypes') or []
            match=(actual_gpc==item.get('expected_googleProductCategory') and actual_pts==item.get('expected_productTypes'))
            verify.append({**item,'verify_status':'verified_merchant_product_get','actual_googleProductCategory':actual_gpc,'actual_productTypes':actual_pts,'match_expected':match})
        except Exception as e:
            verify.append({**item,'verify_status':'verify_failed','verify_error':str(e)[:1200]})
        time.sleep(args.sleep_per_row)
    summary={
        'generated_at':utc_now(),
        'mode':'read_only_timeout_recovery_verify_no_write',
        'progress_path':str(progress_path),
        'progress_rows':len(rows),
        'execution_summary':dict(Counter(x.get('execution_status') for x in rows)),
        'verify_summary':dict(Counter(x.get('verify_status') for x in verify)),
        'match_expected':sum(1 for x in verify if x.get('match_expected')),
        'mismatch_count':sum(1 for x in verify if x.get('verify_status')=='verified_merchant_product_get' and not x.get('match_expected')),
        'failed_count':sum(1 for x in verify if x.get('verify_status')=='verify_failed'),
    }
    payload={'summary':summary,'verify_results':verify,'not_performed':['merchant_write','shopify_write','tiny_write','price_update','availability_update','title_update','image_or_link_update','local_inventory_write','feed_fetch_or_upload','campaign_or_message_send']}
    PUBLIC_JSON.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    lines=['# LK GMC P2A Next Online — Timeout Recovery Fresh Verify','',f"Status: `{'verified' if summary['match_expected']==len(rows) else 'needs_review'}`",'', '## Resumo',f"- Progress rows: {len(rows)}",f"- Execution: {summary['execution_summary']}",f"- Verify: {summary['verify_summary']}",f"- Match esperado: {summary['match_expected']}/{len(rows)}",f"- Mismatches: {summary['mismatch_count']}",f"- Failed: {summary['failed_count']}",'','## Não executado']
    lines += [f"- {x}" for x in payload['not_performed']]
    PUBLIC_MD.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(json.dumps({'status':'verified' if summary['match_expected']==len(rows) else 'needs_review','summary':summary,'report':str(PUBLIC_MD)},ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
