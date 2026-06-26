#!/usr/bin/env python3
"""GMC P1 Wave6 price completion executor using Shopify/Data Spine price source.

Lucas explicitly said to continue/correct the remaining P1 price diagnostics.
This executor updates Merchant `price` only when a current Merchant product with
missing price can be matched to LK Shopify local Data Spine by exact Shopify
handle from Merchant link, exact offer/SKU/variant id, or exact normalized title.
Policy for multi-variant products: use the lowest positive Shopify variant price
as the Merchant item price (price-from behavior) and preserve all other product
fields. Creates private rollback snapshot before writes and verifies via
products.get plus productstatuses recheck.
"""
from __future__ import annotations
import argparse, csv, importlib.util, json, os, pathlib, re, sqlite3, time, urllib.parse
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT=pathlib.Path(__file__).resolve().parents[1]
W4=ROOT/'scripts/lk_gmc_p1_attribute_wave4_aggressive_nonprice_executor_20260513.py'
LOCAL_DB=pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite')
RUN_STAMP='2026-05-13-p1-attribute-wave6-price-shopify-source-executor'
PUBLIC_JSON=ROOT/f'reports/lk-gmc-{RUN_STAMP}.json'
PUBLIC_CSV=ROOT/f'reports/lk-gmc-{RUN_STAMP}.csv'
PUBLIC_MD=ROOT/f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN=ROOT/f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
PRIVATE_DIR=pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
APPROVAL_TEXT_REQUIRED='Lucas approved GMC P1 Wave6 price completion from Shopify source apply'

def utc_now(): return datetime.now(timezone.utc).isoformat()
def load_w4():
    spec=importlib.util.spec_from_file_location('w4', W4); mod=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(mod); return mod

def norm_title(s):
    import unicodedata
    s=str(s or '').lower(); s=unicodedata.normalize('NFKD',s); s=''.join(ch for ch in s if not unicodedata.combining(ch)); s=re.sub(r'\blk sneakers?\b',' ',s); s=re.sub(r'[^a-z0-9]+',' ',s).strip(); return s

def handle_from_link(link: str|None) -> str|None:
    if not link: return None
    path=urllib.parse.urlparse(link).path.strip('/')
    parts=[p for p in path.split('/') if p]
    if 'products' in parts:
        i=parts.index('products')
        if i+1 < len(parts): return parts[i+1]
    return None

def load_price_sources():
    con=sqlite3.connect(str(LOCAL_DB)); con.row_factory=sqlite3.Row; cur=con.cursor()
    q="""select v.sku,v.source_variant_id,v.source_product_id,v.product_id,v.title variant_title,v.option1,v.option2,v.price,v.compare_at_price,p.title product_title,p.handle,p.status from lk_product_variants v left join lk_products p on p.product_id=v.product_id where v.price is not null and v.price > 0"""
    rows=[dict(r) for r in cur.execute(q)]; con.close()
    by_handle={}; by_title={}; by_offer={}
    for d in rows:
        if d.get('handle'): by_handle.setdefault(str(d['handle']),[]).append(d)
        nt=norm_title(d.get('product_title'))
        if nt: by_title.setdefault(nt,[]).append(d)
        for k in ['sku','source_variant_id','source_product_id','product_id']:
            v=d.get(k)
            if v: by_offer.setdefault(str(v),[]).append(d)
    return by_handle, by_title, by_offer

def choose_price(cands):
    prices=sorted(set(round(float(c['price']),2) for c in cands if c.get('price') is not None and float(c['price'])>0))
    if not prices: return None, []
    return prices[0], prices

def source_for_product(w, prod, pid, by_handle, by_title, by_offer):
    offer=w.parse_offer(pid); handle=handle_from_link(prod.get('link')); title=prod.get('title')
    attempts=[]
    if handle:
        c=by_handle.get(handle,[]); attempts.append(('shopify_handle_from_merchant_link',handle,len(c)))
        price,prices=choose_price(c)
        if price: return price, prices, 'shopify_handle_from_merchant_link', handle, c
    c=by_offer.get(offer,[]); attempts.append(('exact_offer_sku_or_variant_or_product_id',offer,len(c)))
    price,prices=choose_price(c)
    if price: return price, prices, 'exact_offer_sku_or_variant_or_product_id', offer, c
    nt=norm_title(title); c=by_title.get(nt,[]); attempts.append(('exact_normalized_title',nt,len(c)))
    price,prices=choose_price(c)
    if price: return price, prices, 'exact_normalized_title', nt, c
    return None, [], 'blocked_no_shopify_price_source', json.dumps(attempts,ensure_ascii=False), []

def build_rows(w, products, statuses, limit):
    by_handle,by_title,by_offer=load_price_sources(); p={x.get('id'):x for x in products}; rows=[]; counters=Counter(); price_sources=Counter()
    for st in statuses:
        attrs=w.required_attrs(st); pid=st.get('productId')
        if 'price' not in attrs: continue
        prod=p.get(pid)
        if not prod:
            decision='blocked_product_not_currently_present'; suggested={}; evidence={}; prices=[]
        elif prod.get('price'):
            decision='blocked_price_already_present'; suggested={}; evidence={}; prices=[]
        else:
            price,prices,src,key,cands=source_for_product(w,prod,pid,by_handle,by_title,by_offer)
            if price:
                decision='ready_for_wave6_price_apply'; suggested={'price':{'value':f'{price:.2f}','currency':'BRL'}}; evidence={'price':src,'match_key':key,'policy':'lowest_positive_shopify_variant_price_for_product'}; price_sources[src]+=1
            else:
                decision='blocked_no_shopify_price_source'; suggested={}; evidence={'attempts':key}; prices=[]
        counters[decision]+=1
        rows.append({'product_id':pid,'offer_id':w.parse_offer(pid or ''),'merchant_title':(prod or {}).get('title') or st.get('title'),'merchant_link':(prod or {}).get('link'),'fresh_required_attrs':sorted(attrs),'suggested_attributes':suggested,'source_prices':prices,'evidence':evidence,'decision_state':decision,'selected_for_apply':False})
    ready=[r for r in rows if r['decision_state']=='ready_for_wave6_price_apply']; selected={r['product_id'] for r in ready[:limit]}
    for r in rows: r['selected_for_apply']=r['product_id'] in selected
    return rows, {'fresh_merchant_products_current':len(products),'fresh_merchant_productstatuses_current':len(statuses),'price_required_rows_current':len(rows),'decision_state_counts':dict(counters),'price_source_counts':dict(price_sources),'ready_total':len(ready),'selected_for_apply_if_approved':len(selected),'limit':limit,'write_allowed_now':0}

def prepare_product(cur,row):
    out=json.loads(json.dumps(cur,ensure_ascii=False))
    for k in ['id','kind','source']: out.pop(k,None)
    out['price']=row['suggested_attributes']['price']
    return out

def snapshot(records,limit):
    PRIVATE_DIR.mkdir(parents=True,exist_ok=True); os.chmod(PRIVATE_DIR,0o700)
    path=PRIVATE_DIR/f'lk-gmc-{RUN_STAMP}-rollback-{datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")}.json'
    path.write_text(json.dumps({'generated_at':utc_now(),'scope':f'Wave6 price completion limit={limit}; update only price from Shopify/Data Spine source','approval_text_required':APPROVAL_TEXT_REQUIRED,'rollback_instruction':'POST /products current_product_resource; verify after delay.','records':records},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    os.chmod(path,0o600); return path

def apply_selected(w,mid,token,rows,products,limit):
    cur={p.get('id'):p for p in products}; records=[]
    for r in [x for x in rows if x['selected_for_apply']]: records.append({'product_id':r['product_id'],'current_product_resource':cur[r['product_id']],'planned_update':r})
    rollback=snapshot(records,limit); progress=PRIVATE_DIR/f'lk-gmc-{RUN_STAMP}-progress-{rollback.stem.rsplit("-",1)[-1]}.jsonl'; results=[]
    with progress.open('w',encoding='utf-8') as f:
        os.chmod(progress,0o600)
        for rec in records:
            r=rec['planned_update']
            try:
                w.upsert_product(mid,prepare_product(rec['current_product_resource'],r),token)
                item={'product_id':r['product_id'],'execution_status':'updated_wave6_price','price':r['suggested_attributes']['price']}
            except Exception as e:
                item={'product_id':r['product_id'],'execution_status':'failed_http_or_validation','error':str(e)[:1200]}; results.append(item); f.write(json.dumps(item,ensure_ascii=False)+'\n'); f.flush(); break
            results.append(item); f.write(json.dumps(item,ensure_ascii=False)+'\n'); f.flush(); time.sleep(0.2)
    return results, rollback

def verify(w,mid,token,rows,results,delay):
    if delay: time.sleep(delay)
    byid={r['product_id']:r for r in rows}; out=[]
    for res in results:
        pid=res.get('product_id'); row=byid.get(pid,{})
        if res.get('execution_status')!='updated_wave6_price': out.append({**res,'verify_status':'not_verified_due_to_execution_status'}); continue
        try:
            prod=w.get_product(mid,pid,token); actual=prod.get('price'); expected=row.get('suggested_attributes',{}).get('price'); out.append({**res,'verify_status':'verified_product_get','actual_price':actual,'attrs_match_expected':actual==expected})
        except Exception as e: out.append({**res,'verify_status':'verify_failed','verify_error':str(e)[:1200]})
    return out

def write_outputs(mode,summary,rows,exec_results,verified,rollback,post):
    ec=Counter(r.get('execution_status') for r in exec_results); vc=Counter(r.get('verify_status') for r in verified); matched=sum(1 for r in verified if r.get('attrs_match_expected'))
    payload={'generated_at':utc_now(),'status':'gmc_p1_attribute_wave6_price_apply_verified' if mode=='apply' else 'gmc_p1_attribute_wave6_price_dry_run_ready','mode':mode,'scope':'Price-only completion from Shopify/Data Spine source; preserves all other Merchant fields.','source_labels':['fact_merchant_center','fact_shopify_local_snapshot','manual_approval','derived_reconciliation'],'approval_required_for_apply':APPROVAL_TEXT_REQUIRED,'summary':{**summary,'execution_results_summary':dict(ec),'verify_results_summary':dict(vc),'verified_attrs_match_expected':matched,**(post or {})},'private_rollback_snapshot_path':str(rollback) if rollback else None,'public_rows':rows,'execution_results':exec_results,'verified_results':verified,'not_performed':['merchant_delete','merchant_non_price_update','feed_update_or_fetch','shopify_write','tiny_call_or_write','database_write','pos_or_local_inventory_write','klaviyo_or_whatsapp_send','notion_or_n8n_write','loyalty_or_judgeme_action']}
    PUBLIC_JSON.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    fields=['product_id','offer_id','merchant_title','merchant_link','fresh_required_attrs','suggested_attributes','source_prices','evidence','decision_state','selected_for_apply']
    with PUBLIC_CSV.open('w',newline='',encoding='utf-8') as f:
        wr=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore'); wr.writeheader()
        for r in rows:
            o={k:r.get(k) for k in fields}; o['fresh_required_attrs']='; '.join(o.get('fresh_required_attrs') or []); o['suggested_attributes']=json.dumps(o.get('suggested_attributes') or {},ensure_ascii=False); o['source_prices']=json.dumps(o.get('source_prices') or [],ensure_ascii=False); o['evidence']=json.dumps(o.get('evidence') or {},ensure_ascii=False); wr.writerow(o)
    lines=['# LK GMC P1 Attribute Completion — Wave6 Price from Shopify Source, 2026-05-13','',f"Status: `{payload['status']}`",'','## Escopo',f'- Modo: `{mode}`','- Campo alterado: `price` somente.','- Fonte: preço do Shopify/Data Spine por handle/link, offer/SKU/variant ou título normalizado exato.','- Política multi-variante: menor preço positivo de variante Shopify para o produto.','','## Resultado',f"- Price rows atuais: {summary['price_required_rows_current']}",f"- Ready: {summary['ready_total']}",f"- Selecionados/aplicados: {summary['selected_for_apply_if_approved']}",f"- Fontes: {summary['price_source_counts']}",f"- Execution: {dict(ec)}",f"- Verify: {dict(vc)}",f"- Match esperado: {matched}/{len(verified)}"]
    if post: lines += [f"- Required rows after: {post['required_attr_rows_after']}",f"- Required instances after: {post['required_attr_instances_after']}",f"- Counts after: {post['required_attr_counts_after']}"]
    lines += ['','## Rollback privado',f'- `{rollback}`' if rollback else '- Não criado no dry-run.','','## Não executado']
    for n in payload['not_performed']: lines.append(f'- {n}')
    PUBLIC_MD.write_text('\n'.join(lines)+'\n',encoding='utf-8'); BRAIN.write_text(PUBLIC_MD.read_text(encoding='utf-8'),encoding='utf-8')
    print(json.dumps({'status':payload['status'],'summary':payload['summary'],'report':str(PUBLIC_MD),'rollback':str(rollback) if rollback else None},ensure_ascii=False,indent=2))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--apply',action='store_true'); ap.add_argument('--approval-text',default=''); ap.add_argument('--limit',type=int,default=1000); ap.add_argument('--verify-delay',type=int,default=60); ap.add_argument('--post-status-delay',type=int,default=60); args=ap.parse_args()
    mode='apply' if args.apply else 'dry-run'
    if args.apply and args.approval_text != APPROVAL_TEXT_REQUIRED: raise RuntimeError(f'apply_blocked_missing_exact_approval_text: {APPROVAL_TEXT_REQUIRED}')
    w=load_w4(); audit=w.import_audit(); secrets=audit.load_doppler(); mid=secrets.get('MERCHANT_CENTER_ID_LK'); token=audit.google_access_token(audit.parse_service_account(secrets))
    products=w.list_all('products',mid,token); statuses=w.list_all('productstatuses',mid,token); rows,summary=build_rows(w,products,statuses,args.limit)
    exec_results=[]; verified=[]; rollback=None; post=None
    if mode=='apply':
        exec_results,rollback=apply_selected(w,mid,token,rows,products,args.limit); verified=verify(w,mid,token,rows,exec_results,args.verify_delay)
        if args.post_status_delay: time.sleep(args.post_status_delay)
        post=w.post_status_recheck(mid,token)
    write_outputs(mode,summary,rows,exec_results,verified,rollback,post)
if __name__=='__main__': main()
