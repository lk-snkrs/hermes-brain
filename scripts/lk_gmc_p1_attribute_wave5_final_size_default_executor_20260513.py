#!/usr/bin/env python3
"""GMC P1 Wave5 final size-default executor for remaining non-price size issues.

Fills remaining missing `sizes` only. Price is not touched. Uses Lucas's
Merchant completeness policy: default M for apparel rows with no size signal,
and Único for books/accessories/kits/toys/cosmetics/non-apparel one-size goods.
"""
from __future__ import annotations
import argparse, csv, importlib.util, json, os, pathlib, time
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT=pathlib.Path(__file__).resolve().parents[1]
WAVE4_PATH=ROOT/'scripts/lk_gmc_p1_attribute_wave4_aggressive_nonprice_executor_20260513.py'
RUN_STAMP='2026-05-13-p1-attribute-wave5-final-size-default-executor'
PUBLIC_JSON=ROOT/f'reports/lk-gmc-{RUN_STAMP}.json'
PUBLIC_CSV=ROOT/f'reports/lk-gmc-{RUN_STAMP}.csv'
PUBLIC_MD=ROOT/f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN=ROOT/f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
PRIVATE_DIR=pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
APPROVAL_TEXT_REQUIRED='Lucas approved GMC P1 Attribute Wave5 final size defaults apply'
APPAREL_HINTS=['camiseta','camisa','calça','calca','moletom','short','jaqueta','hoodie','sweatshort','jeans','tricot','trico']

def load_w4():
    spec=importlib.util.spec_from_file_location('w4', WAVE4_PATH); mod=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(mod); return mod

def utc_now(): return datetime.now(timezone.utc).isoformat()

def default_size(title: str) -> tuple[str,str]:
    low=(title or '').lower()
    if any(h in low for h in APPAREL_HINTS):
        return 'M','default_apparel_M_lucas_completeness_policy'
    return 'Único','default_one_size_lucas_completeness_policy'

def build_rows(w, products, statuses, limit):
    p={x.get('id'):x for x in products}; rows=[]; counters=Counter()
    for st in statuses:
        attrs=w.required_attrs(st); pid=st.get('productId'); prod=p.get(pid) or {}
        if 'size' not in attrs: continue
        if not prod:
            decision='blocked_product_not_currently_present'; sugg={}; evidence={}; reasons=['product missing']
        elif w.norm_list(prod.get('sizes')):
            decision='blocked_size_already_present'; sugg={}; evidence={}; reasons=['size already present']
        else:
            size, ev=default_size(prod.get('title') or st.get('title') or '')
            decision='ready_for_wave5_final_size_default_apply'; sugg={'sizes':[size]}; evidence={'sizes':ev}; reasons=['remaining size issue filled by Lucas completeness policy; price untouched if present']
        counters[decision]+=1
        rows.append({'product_id':pid,'offer_id':w.parse_offer(pid or ''),'merchant_title':prod.get('title') or st.get('title'),'fresh_required_attrs':sorted(attrs),'suggested_attributes':sugg,'evidence':evidence,'decision_state':decision,'decision_reasons':reasons,'selected_for_apply':False,'has_price_required_attr':'price' in attrs})
    ready=[r for r in rows if r['decision_state']=='ready_for_wave5_final_size_default_apply']
    selected={r['product_id'] for r in ready[:limit]}
    for r in rows: r['selected_for_apply']=r['product_id'] in selected
    return rows, {'fresh_merchant_products_current':len(products),'fresh_merchant_productstatuses_current':len(statuses),'size_required_rows_current':len(rows),'decision_state_counts':dict(counters),'ready_total':len(ready),'selected_for_apply_if_approved':len(selected),'limit':limit,'write_allowed_now':0}

def prepare_product(cur, row):
    out=json.loads(json.dumps(cur, ensure_ascii=False))
    for k in ['id','kind','source']: out.pop(k, None)
    out['sizes']=row['suggested_attributes']['sizes']
    return out

def snapshot(records, limit):
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True); os.chmod(PRIVATE_DIR,0o700)
    path=PRIVATE_DIR/f'lk-gmc-{RUN_STAMP}-rollback-{datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")}.json'
    path.write_text(json.dumps({'generated_at':utc_now(),'scope':f'Wave5 final size default apply limit={limit}; update only sizes; price excluded','approval_text_required':APPROVAL_TEXT_REQUIRED,'records':records},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    os.chmod(path,0o600); return path

def apply_selected(w, mid, token, rows, products, limit):
    cur={p.get('id'):p for p in products}; records=[]
    for r in [x for x in rows if x['selected_for_apply']]: records.append({'product_id':r['product_id'],'current_product_resource':cur[r['product_id']],'planned_update':r})
    rollback=snapshot(records,limit); results=[]; progress=PRIVATE_DIR/f'lk-gmc-{RUN_STAMP}-progress-{rollback.stem.rsplit("-",1)[-1]}.jsonl'
    with progress.open('w',encoding='utf-8') as f:
        os.chmod(progress,0o600)
        for rec in records:
            r=rec['planned_update']
            try:
                w.upsert_product(mid, prepare_product(rec['current_product_resource'],r), token)
                item={'product_id':r['product_id'],'execution_status':'updated_wave5_final_size_default','fields':['sizes']}
            except Exception as e:
                item={'product_id':r['product_id'],'execution_status':'failed_http_or_validation','error':str(e)[:1200]}; results.append(item); f.write(json.dumps(item,ensure_ascii=False)+'\n'); f.flush(); break
            results.append(item); f.write(json.dumps(item,ensure_ascii=False)+'\n'); f.flush(); time.sleep(0.2)
    return results, rollback

def verify(w, mid, token, rows, results, delay):
    if delay: time.sleep(delay)
    byid={r['product_id']:r for r in rows}; out=[]
    for res in results:
        pid=res.get('product_id'); row=byid.get(pid,{})
        if res.get('execution_status')!='updated_wave5_final_size_default': out.append({**res,'verify_status':'not_verified_due_to_execution_status'}); continue
        try:
            prod=w.get_product(mid,pid,token); actual=w.norm_list(prod.get('sizes')); expected=row.get('suggested_attributes',{}).get('sizes'); out.append({**res,'verify_status':'verified_product_get','actual_sizes':actual,'attrs_match_expected':actual==expected})
        except Exception as e: out.append({**res,'verify_status':'verify_failed','verify_error':str(e)[:1200]})
    return out

def write_outputs(mode, summary, rows, exec_results, verified, rollback, post):
    ec=Counter(r.get('execution_status') for r in exec_results); vc=Counter(r.get('verify_status') for r in verified); matched=sum(1 for r in verified if r.get('attrs_match_expected'))
    payload={'generated_at':utc_now(),'status':'gmc_p1_attribute_wave5_final_size_defaults_apply_verified' if mode=='apply' else 'gmc_p1_attribute_wave5_final_size_defaults_dry_run_ready','mode':mode,'scope':'Wave5 sizes-only defaults for remaining size diagnostics; price excluded.','source_labels':['fact_merchant_center','manual_approval','derived_reconciliation'],'approval_required_for_apply':APPROVAL_TEXT_REQUIRED,'summary':{**summary,'execution_results_summary':dict(ec),'verify_results_summary':dict(vc),'verified_attrs_match_expected':matched,**(post or {})},'private_rollback_snapshot_path':str(rollback) if rollback else None,'public_rows':rows,'execution_results':exec_results,'verified_results':verified,'not_performed':['merchant_price_update','merchant_delete','merchant_color_age_gender_update','feed_update_or_fetch','shopify_write','tiny_call_or_write','database_write','klaviyo_or_whatsapp_send','notion_or_n8n_write','loyalty_or_judgeme_action']}
    PUBLIC_JSON.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    fields=['product_id','offer_id','merchant_title','fresh_required_attrs','suggested_attributes','evidence','decision_state','selected_for_apply','has_price_required_attr','decision_reasons']
    with PUBLIC_CSV.open('w',newline='',encoding='utf-8') as f:
        wcsv=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore'); wcsv.writeheader()
        for r in rows:
            o={k:r.get(k) for k in fields}; o['fresh_required_attrs']='; '.join(o.get('fresh_required_attrs') or []); o['suggested_attributes']=json.dumps(o.get('suggested_attributes') or {},ensure_ascii=False); o['evidence']=json.dumps(o.get('evidence') or {},ensure_ascii=False); o['decision_reasons']='; '.join(o.get('decision_reasons') or []); wcsv.writerow(o)
    lines=['# LK GMC P1 Attribute Completion — Wave5 Final Size Defaults, 2026-05-13','',f"Status: `{payload['status']}`",'','## Resultado',f"- Ready: {summary['ready_total']}",f"- Selecionados/aplicados: {summary['selected_for_apply_if_approved']}",f"- Execution: {dict(ec)}",f"- Verify: {dict(vc)}",f"- Match esperado: {matched}/{len(verified)}"]
    if post: lines += [f"- Required rows after: {post['required_attr_rows_after']}",f"- Required instances after: {post['required_attr_instances_after']}",f"- Counts after: {post['required_attr_counts_after']}"]
    lines += ['','## Rollback privado',f'- `{rollback}`' if rollback else '- Não criado no dry-run.','','## Não executado']
    for n in payload['not_performed']: lines.append(f'- {n}')
    PUBLIC_MD.write_text('\n'.join(lines)+'\n',encoding='utf-8'); BRAIN.write_text(PUBLIC_MD.read_text(encoding='utf-8'),encoding='utf-8')
    print(json.dumps({'status':payload['status'],'summary':payload['summary'],'report':str(PUBLIC_MD),'rollback':str(rollback) if rollback else None},ensure_ascii=False,indent=2))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--apply',action='store_true'); ap.add_argument('--approval-text',default=''); ap.add_argument('--limit',type=int,default=1000); ap.add_argument('--verify-delay',type=int,default=90); ap.add_argument('--post-status-delay',type=int,default=90); args=ap.parse_args()
    mode='apply' if args.apply else 'dry-run'
    if args.apply and args.approval_text != APPROVAL_TEXT_REQUIRED: raise RuntimeError(f'apply_blocked_missing_exact_approval_text: {APPROVAL_TEXT_REQUIRED}')
    w=load_w4(); audit=w.import_audit(); secrets=audit.load_doppler(); mid=secrets.get('MERCHANT_CENTER_ID_LK')
    token=audit.google_access_token(audit.parse_service_account(secrets)); products=w.list_all('products',mid,token); statuses=w.list_all('productstatuses',mid,token)
    rows,summary=build_rows(w,products,statuses,args.limit); exec_results=[]; verified=[]; rollback=None; post=None
    if mode=='apply':
        exec_results,rollback=apply_selected(w,mid,token,rows,products,args.limit); verified=verify(w,mid,token,rows,exec_results,args.verify_delay)
        if args.post_status_delay: time.sleep(args.post_status_delay)
        post=w.post_status_recheck(mid,token)
    write_outputs(mode,summary,rows,exec_results,verified,rollback,post)
if __name__=='__main__': main()
