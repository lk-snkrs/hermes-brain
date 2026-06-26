#!/usr/bin/env python3
"""LK GMC follow-up after P2A pilot: color micro-fix then Shoes scale.

Approved scope from Lucas: (1) fix single required color row, then (2) scale P2A
category/productTypes for remaining Shoes. Uses Merchant API v1 ProductInputs
PATCH for dataSource 10636492695. Creates private rollback snapshots and verifies
with Merchant products.get plus productstatuses recheck.
"""
from __future__ import annotations
import argparse, importlib.util, json, os, pathlib, time
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
P2_PATH = ROOT / 'scripts/lk_gmc_p2_category_product_type_executor_20260513.py'
RUN_STAMP = '2026-05-13-p2a-color-and-shoes-scale'
PUBLIC_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
PUBLIC_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
APPROVAL_TEXT_REQUIRED = 'Lucas approved GMC color micro-fix and P2A Shoes scale'
COLOR_PID = 'online:pt:BR:SLBCS'
COLOR_EXPECTED = 'Verde'
SHOES_GPC = 'Apparel & Accessories > Shoes'
SHOES_PT = ['Calçados']

def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()

def load_mod(path: pathlib.Path, name: str):
    spec=importlib.util.spec_from_file_location(name, path)
    mod=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(mod)
    return mod

def patch_attr(p2, mid: str, token: str, pid: str, attrs: dict[str, Any], update_mask: str) -> dict[str, Any]:
    name, _encoded, lang, label, offer = p2.product_input_name(mid, pid)
    body={'name': name, 'offerId': offer, 'contentLanguage': lang, 'feedLabel': label, 'productAttributes': attrs}
    import urllib.parse
    data_source=f'accounts/{mid}/dataSources/{p2.DATA_SOURCE_ID}'
    qs=urllib.parse.urlencode({'dataSource': data_source, 'updateMask': update_mask})
    url='https://merchantapi.googleapis.com/products/v1/' + urllib.parse.quote(name, safe='/') + '?' + qs
    return p2.request_json(url, token, method='PATCH', payload=body)

def merchant_attrs(p2, mid: str, token: str, pid: str) -> dict[str, Any]:
    _name, encoded, *_ = p2.product_input_name(mid, pid)
    return (p2.merchant_product_get(mid, encoded, token).get('productAttributes') or {})

def snapshot(records: list[dict[str, Any]], scope: str) -> pathlib.Path:
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True); os.chmod(PRIVATE_DIR, 0o700)
    path=PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-rollback-{datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")}.json'
    path.write_text(json.dumps({'generated_at':utc_now(),'scope':scope,'approval_text_required':APPROVAL_TEXT_REQUIRED,'rollback_instruction':'Use Merchant API v1 ProductInputs PATCH with previous_product_attributes/current_content_api_product_resource values if rollback is needed; review before rollback because P2A is additive SEO metadata.','records':records},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    os.chmod(path,0o600); return path

def required_probe(w, mid: str, token: str) -> dict[str, Any]:
    statuses=w.list_all('productstatuses', mid, token)
    required_rows=[]; issue_counts=Counter(); req_counts=Counter()
    for st in statuses:
        for issue in st.get('itemLevelIssues') or []:
            issue_counts[issue.get('code') or 'unknown'] += 1
        attrs=w.required_attrs(st)
        if attrs:
            pid=st.get('productId') or st.get('id')
            required_rows.append({'product_id':pid,'required_attrs':sorted(list(attrs)),'title':st.get('title')})
            for a in attrs: req_counts[a]+=1
    return {'fresh_productstatuses_after':len(statuses),'required_attr_rows_after':len(required_rows),'required_attr_counts_after':dict(req_counts.most_common()),'required_rows_sample':required_rows[:10],'top_item_level_issue_counts_after':dict(issue_counts.most_common(12))}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--apply',action='store_true'); ap.add_argument('--approval-text',default=''); ap.add_argument('--verify-delay',type=int,default=120); ap.add_argument('--post-status-delay',type=int,default=180)
    args=ap.parse_args(); mode='apply' if args.apply else 'dry-run'
    if args.apply and args.approval_text != APPROVAL_TEXT_REQUIRED:
        raise RuntimeError('apply_blocked_missing_exact_approval_text: '+APPROVAL_TEXT_REQUIRED)
    p2=load_mod(P2_PATH,'p2'); w=p2.import_w4(); audit=w.import_audit(); secrets=audit.load_doppler(); mid=secrets.get('MERCHANT_CENTER_ID_LK'); token=audit.google_access_token(audit.parse_service_account(secrets))
    products={p.get('id'):p for p in w.list_all('products', mid, token)}
    all_candidates=p2.load_candidates(100000)
    shoes=[r for r in all_candidates if r['suggested_googleProductCategory']==SHOES_GPC and r['suggested_productTypes']==SHOES_PT]
    # Preflight merchant-state skip: avoid re-patching already compliant pilot rows.
    shoes_ready=[]; shoes_skipped=[]
    for r in shoes:
        try:
            attrs=merchant_attrs(p2, mid, token, r['product_id'])
            if attrs.get('googleProductCategory')==SHOES_GPC and (attrs.get('productTypes') or [])==SHOES_PT:
                shoes_skipped.append({'product_id':r['product_id'],'status':'already_matching_p2a_shoes'})
            else:
                r['previous_product_attributes']={'googleProductCategory':attrs.get('googleProductCategory'),'productTypes':attrs.get('productTypes') or []}
                shoes_ready.append(r)
        except Exception as e:
            shoes_skipped.append({'product_id':r['product_id'],'status':'preflight_get_failed','error':str(e)[:1000]})
        time.sleep(0.03)
    color_pre=None
    try:
        color_pre=merchant_attrs(p2, mid, token, COLOR_PID)
    except Exception as e:
        color_pre={'preflight_error':str(e)[:1000]}
    color_ready = color_pre.get('color') != COLOR_EXPECTED
    records=[]
    if color_ready:
        records.append({'product_id':COLOR_PID,'planned_update':{'color':COLOR_EXPECTED},'previous_product_attributes':color_pre,'current_content_api_product_resource':products.get(COLOR_PID)})
    for r in shoes_ready:
        records.append({'product_id':r['product_id'],'planned_update':{'googleProductCategory':SHOES_GPC,'productTypes':SHOES_PT},'previous_product_attributes':r.get('previous_product_attributes'), 'current_content_api_product_resource':products.get(r['product_id'])})
    exec_results=[]; verify_results=[]; rollback=None; post=None
    if args.apply:
        rollback=snapshot(records, f'color micro-fix plus P2A Shoes remaining scale; color_ready={color_ready}; shoes_ready={len(shoes_ready)}')
        progress=PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-progress-{rollback.stem.rsplit("-",1)[-1]}.jsonl'
        with progress.open('w',encoding='utf-8') as f:
            os.chmod(progress,0o600)
            if color_ready:
                try:
                    resp=patch_attr(p2, mid, token, COLOR_PID, {'color':COLOR_EXPECTED}, 'productAttributes.color')
                    item={'product_id':COLOR_PID,'execution_status':'patched_color_v1','product_input':resp.get('name'),'expected_color':COLOR_EXPECTED}
                except Exception as e:
                    item={'product_id':COLOR_PID,'execution_status':'failed_patch_color_v1','error':str(e)[:1500]}
                exec_results.append(item); f.write(json.dumps(item,ensure_ascii=False)+'\n'); f.flush()
                if item['execution_status'].startswith('failed_'):
                    raise RuntimeError('color_patch_failed; aborting_shoes_scale: '+item.get('error',''))
                time.sleep(0.25)
            for r in shoes_ready:
                try:
                    resp=p2.patch_category_product_types(mid, token, r['product_id'], SHOES_GPC, SHOES_PT)
                    item={'product_id':r['product_id'],'execution_status':'patched_p2a_shoes_v1','product_input':resp.get('name')}
                except Exception as e:
                    item={'product_id':r['product_id'],'execution_status':'failed_patch_p2a_shoes_v1','error':str(e)[:1500]}
                    exec_results.append(item); f.write(json.dumps(item,ensure_ascii=False)+'\n'); f.flush(); break
                exec_results.append(item); f.write(json.dumps(item,ensure_ascii=False)+'\n'); f.flush(); time.sleep(0.18)
        if args.verify_delay: time.sleep(args.verify_delay)
        for item in exec_results:
            pid=item['product_id']
            try:
                attrs=merchant_attrs(p2, mid, token, pid)
                if item['execution_status']=='patched_color_v1':
                    match=attrs.get('color')==COLOR_EXPECTED
                    verify_results.append({**item,'verify_status':'verified_merchant_product_get','actual_color':attrs.get('color'),'match_expected':match})
                elif item['execution_status']=='patched_p2a_shoes_v1':
                    match=attrs.get('googleProductCategory')==SHOES_GPC and (attrs.get('productTypes') or [])==SHOES_PT
                    verify_results.append({**item,'verify_status':'verified_merchant_product_get','actual_googleProductCategory':attrs.get('googleProductCategory'),'actual_productTypes':attrs.get('productTypes') or [],'match_expected':match})
                else:
                    verify_results.append({**item,'verify_status':'not_verified_due_to_execution_status'})
            except Exception as e:
                verify_results.append({**item,'verify_status':'verify_failed','verify_error':str(e)[:1200]})
            time.sleep(0.03)
        if args.post_status_delay: time.sleep(args.post_status_delay)
        post=required_probe(w, mid, token)
    summary={'mode':mode,'color_target':{'product_id':COLOR_PID,'expected_color':COLOR_EXPECTED,'pre_color':color_pre,'selected_for_apply':color_ready},'shoes_candidates_total':len(shoes),'shoes_already_matching_skipped':len(shoes_skipped),'shoes_ready_to_patch':len(shoes_ready),'shoes_preflight_skipped_sample':shoes_skipped[:10],'records_selected':len(records),'execution_results_summary':dict(Counter(x.get('execution_status') for x in exec_results)),'verify_results_summary':dict(Counter(x.get('verify_status') for x in verify_results)),'verified_match_expected':sum(1 for x in verify_results if x.get('match_expected'))}
    if post: summary.update(post)
    payload={'generated_at':utc_now(),'status':'apply_verified' if mode=='apply' else 'dry_run_ready','approval_required_for_apply':APPROVAL_TEXT_REQUIRED,'summary':summary,'private_rollback_snapshot_path':str(rollback) if rollback else None,'execution_results':exec_results,'verify_results':verify_results,'not_performed':['title_update','price_update','availability_update','image_or_link_update','merchant_delete','shopify_write','tiny_write','database_write','feed_fetch_or_upload','campaign_or_message_send']}
    PUBLIC_JSON.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    lines=['# LK GMC P2A — Color micro-fix + Shoes scale, 2026-05-13','',f"Status: `{payload['status']}`",'', '## Resultado',f"- Color target: {COLOR_PID} -> {COLOR_EXPECTED}; selected={color_ready}",f"- Shoes candidates total: {len(shoes)}",f"- Shoes already matching/skipped: {len(shoes_skipped)}",f"- Shoes patched target: {len(shoes_ready)}",f"- Execution: {summary['execution_results_summary']}",f"- Verify: {summary['verify_results_summary']}",f"- Match esperado: {summary['verified_match_expected']}/{len(verify_results)}"]
    if post:
        lines += [f"- Productstatuses after: {post['fresh_productstatuses_after']}",f"- Required attr rows after: {post['required_attr_rows_after']}",f"- Required attr counts after: {post['required_attr_counts_after']}",f"- Top issues after: {post['top_item_level_issue_counts_after']}"]
    lines += ['', '## Rollback privado', f"- `{rollback}`" if rollback else '- Não criado no dry-run.', '', '## Não executado']
    lines += [f"- {x}" for x in payload['not_performed']]
    PUBLIC_MD.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(json.dumps({'status':payload['status'],'summary':summary,'report':str(PUBLIC_MD),'rollback':str(rollback) if rollback else None},ensure_ascii=False,indent=2))

if __name__=='__main__': main()
