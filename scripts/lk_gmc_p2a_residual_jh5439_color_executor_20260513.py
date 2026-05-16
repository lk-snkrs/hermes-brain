#!/usr/bin/env python3
"""LK GMC residual JH5439 color executor.

Scope: Merchant API v1 ProductInputs PATCH for dataSource 10636492695,
productAttributes.color only, 11 exact JH5439 variants. Default dry-run writes
public preview only. Apply requires exact Lucas approval text and creates private
rollback snapshot before any PATCH.
"""
from __future__ import annotations
import argparse, importlib.util, json, os, pathlib, time, urllib.parse
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
P2_PATH = ROOT / 'scripts/lk_gmc_p2_category_product_type_executor_20260513.py'
RUN_STAMP = '2026-05-13-p2a-residual-jh5439-color'
PUBLIC_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}-executor.json'
PUBLIC_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}-executor.md'
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
APPROVAL_TEXT_REQUIRED = 'Aprovo corrigir color Bordô nas 11 variantes JH5439 no GMC via Merchant API v1, com rollback e verificação.'
TARGET_COLOR = 'Bordô'
PRODUCT_IDS = [f'online:pt:BR:JH5439-{i}' for i in range(1,12)]

def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()

def load_mod(path: pathlib.Path, name: str):
    spec=importlib.util.spec_from_file_location(name, path)
    mod=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(mod)
    return mod

def merchant_attrs(p2, mid: str, token: str, pid: str) -> dict[str, Any]:
    _name, encoded, *_ = p2.product_input_name(mid, pid)
    return (p2.merchant_product_get(mid, encoded, token).get('productAttributes') or {})

def patch_color(p2, mid: str, token: str, pid: str) -> dict[str, Any]:
    name, _encoded, lang, label, offer = p2.product_input_name(mid, pid)
    body={'name': name, 'offerId': offer, 'contentLanguage': lang, 'feedLabel': label, 'productAttributes': {'color': TARGET_COLOR}}
    data_source=f'accounts/{mid}/dataSources/{p2.DATA_SOURCE_ID}'
    qs=urllib.parse.urlencode({'dataSource': data_source, 'updateMask': 'productAttributes.color'})
    url='https://merchantapi.googleapis.com/products/v1/' + urllib.parse.quote(name, safe='/') + '?' + qs
    return p2.request_json(url, token, method='PATCH', payload=body)

def snapshot(records: list[dict[str, Any]]) -> pathlib.Path:
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True); os.chmod(PRIVATE_DIR, 0o700)
    path=PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-rollback-{datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")}.json'
    path.write_text(json.dumps({'generated_at':utc_now(),'scope':'JH5439 color residual fix only','approval_text_required':APPROVAL_TEXT_REQUIRED,'rollback_instruction':'Review before rollback; patch productAttributes.color back to previous_product_attributes.color if needed.','records':records},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    os.chmod(path,0o600); return path

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--apply',action='store_true'); ap.add_argument('--approval-text',default=''); ap.add_argument('--verify-delay',type=int,default=90)
    args=ap.parse_args(); mode='apply' if args.apply else 'dry-run'
    if args.apply and args.approval_text != APPROVAL_TEXT_REQUIRED:
        raise RuntimeError('apply_blocked_missing_exact_approval_text: '+APPROVAL_TEXT_REQUIRED)
    p2=load_mod(P2_PATH,'p2'); w=p2.import_w4(); audit=w.import_audit(); secrets=audit.load_doppler(); mid=secrets.get('MERCHANT_CENTER_ID_LK'); token=audit.google_access_token(audit.parse_service_account(secrets))
    records=[]
    for pid in PRODUCT_IDS:
        attrs=merchant_attrs(p2, mid, token, pid)
        title=attrs.get('title')
        ready = (attrs.get('color') != TARGET_COLOR) and title == 'Tênis Adidas Handball Spezial Bordô'
        records.append({'product_id':pid,'title':title,'previous_product_attributes':{'color':attrs.get('color'),'googleProductCategory':attrs.get('googleProductCategory'),'productTypes':attrs.get('productTypes') or []},'planned_update':{'color':TARGET_COLOR},'eligible':ready,'evidence':'title_exact_match_contains_Bordô' if ready else 'not_eligible_current_color_or_title_mismatch'})
        time.sleep(0.03)
    exec_results=[]; verify_results=[]; rollback=None
    if args.apply:
        selected=[r for r in records if r['eligible']]
        rollback=snapshot(selected)
        progress=PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-progress-{rollback.stem.rsplit("-",1)[-1]}.jsonl'
        with progress.open('w',encoding='utf-8') as f:
            os.chmod(progress,0o600)
            for r in selected:
                try:
                    resp=patch_color(p2, mid, token, r['product_id'])
                    item={'product_id':r['product_id'],'execution_status':'patched_color_v1','product_input':resp.get('name'),'expected_color':TARGET_COLOR}
                except Exception as e:
                    item={'product_id':r['product_id'],'execution_status':'failed_patch_color_v1','error':str(e)[:1500]}
                    exec_results.append(item); f.write(json.dumps(item,ensure_ascii=False)+'\n'); f.flush(); break
                exec_results.append(item); f.write(json.dumps(item,ensure_ascii=False)+'\n'); f.flush(); time.sleep(0.20)
        if args.verify_delay: time.sleep(args.verify_delay)
        for item in exec_results:
            try:
                attrs=merchant_attrs(p2, mid, token, item['product_id'])
                verify_results.append({**item,'verify_status':'verified_merchant_product_get','actual_color':attrs.get('color'),'match_expected':attrs.get('color')==TARGET_COLOR})
            except Exception as e:
                verify_results.append({**item,'verify_status':'verify_failed','verify_error':str(e)[:1200]})
            time.sleep(0.03)
    summary={'mode':mode,'records_total':len(records),'eligible':sum(1 for r in records if r['eligible']),'execution_results_summary':dict(Counter(x.get('execution_status') for x in exec_results)),'verify_results_summary':dict(Counter(x.get('verify_status') for x in verify_results)),'verified_match_expected':sum(1 for x in verify_results if x.get('match_expected'))}
    payload={'generated_at':utc_now(),'status':'apply_verified' if args.apply and summary['verified_match_expected']==len(exec_results) else ('apply_completed_needs_review' if args.apply else 'dry_run_ready'),'approval_required_for_apply':APPROVAL_TEXT_REQUIRED,'summary':summary,'private_rollback_snapshot_path':str(rollback) if rollback else None,'records':records,'execution_results':exec_results,'verify_results':verify_results,'not_performed':['title_update','price_update','availability_update','category_or_product_type_update','image_or_link_update','merchant_delete','shopify_write','tiny_write','database_write','feed_fetch_or_upload','campaign_or_message_send']}
    PUBLIC_JSON.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    lines=['# LK GMC P2A residual JH5439 color executor — 2026-05-13','',f"Status: `{payload['status']}`",'', '## Resultado',f"- Mode: {mode}",f"- Records total: {summary['records_total']}",f"- Eligible: {summary['eligible']}",f"- Execution: {summary['execution_results_summary']}",f"- Verify: {summary['verify_results_summary']}",f"- Match esperado: {summary['verified_match_expected']}/{len(verify_results)}",'', '## Rollback privado', f"- `{rollback}`" if rollback else '- Não criado no dry-run.', '', '## Approval text', f"`{APPROVAL_TEXT_REQUIRED}`", '', '## Não executado']
    lines += [f"- {x}" for x in payload['not_performed']]
    PUBLIC_MD.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(json.dumps({'status':payload['status'],'summary':summary,'report':str(PUBLIC_MD),'rollback':str(rollback) if rollback else None},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
