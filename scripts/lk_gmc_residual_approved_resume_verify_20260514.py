#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,json,os,pathlib,time,urllib.parse
from collections import Counter
from datetime import datetime,timezone
from typing import Any
ROOT=pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
ABC=ROOT/'scripts/lk_execute_approved_abc_20260514.py'
AUD=ROOT/'scripts/lk_gmc_catalog_duplication_audit_20260512.py'
PRIVATE=pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
RUN='2026-05-14-residual-approved-resume-verify'
OUT=ROOT/f'reports/lk-gmc-{RUN}.json'
MD=ROOT/f'reports/lk-gmc-{RUN}.md'
BRAIN=ROOT/f'areas/lk/rotinas/gmc-{RUN}.md'
TARGET={'price_updated','strikethrough_price_updated','missing_item_attribute_for_product_type','restricted_gtin','reserved_gtin','landing_page_error','image_single_color','image_link_broken','landing_page_pending_crawl'}

def now(): return datetime.now(timezone.utc).isoformat()
def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path); m=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(m); return m
abc=load(ABC,'abc')
aud=load(AUD,'aud')

def latest_pair():
    ps=sorted(PRIVATE.glob('lk-gmc-2026-05-14-residual-approved-executor-progress-*.jsonl'), key=lambda p:p.stat().st_mtime, reverse=True)
    if not ps: raise RuntimeError('no progress files')
    p=ps[0]
    stamp=p.stem.rsplit('-',1)[-1]
    r=PRIVATE/f'lk-gmc-2026-05-14-residual-approved-executor-rollback-{stamp}.json'
    if not r.exists():
        # fallback by mtime
        rs=sorted(PRIVATE.glob('lk-gmc-2026-05-14-residual-approved-executor-rollback-*.json'), key=lambda x:x.stat().st_mtime, reverse=True)
        r=rs[0]
    return p,r

def upsert_content_product(mid,token,product):
    url=f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/products'
    return abc.request_json(url,token=token,method='POST',payload=product,attempts=5,timeout=120)

def amount_to_value(d):
    if not isinstance(d,dict): return None
    if 'amountMicros' in d:
        return f"{int(d['amountMicros'])/1_000_000:.2f}"
    if 'value' in d:
        try: return f"{float(d['value']):.2f}"
        except Exception: return str(d['value'])
    return None

def actual_value(v):
    if isinstance(v,dict) and 'value' in v:
        try: return f"{float(v['value']):.2f}"
        except Exception: return str(v['value'])
    return v

def compare_attrs(cur, expected):
    result={}
    ok=True
    for k,exp in expected.items():
        act=cur.get(k)
        if k in {'price','salePrice'}:
            ev=amount_to_value(exp); av=actual_value(act); match=(ev==av)
        else:
            ev=exp; av=act; match=(ev==av)
        result[k]={'expected':ev,'actual':av,'match':match}
        ok = ok and match
    return ok,result

def main():
    secrets=abc.load_doppler(); mid=secrets['MERCHANT_CENTER_ID_LK']; token=abc.google_access_token(abc.parse_service_account(secrets))
    progress,rollback=latest_pair()
    records=json.loads(rollback.read_text()).get('records',[])
    rec_by_id={r['product_id']:r for r in records}
    lines=[json.loads(x) for x in progress.read_text().splitlines() if x.strip()]
    repair_progress=PRIVATE/f'lk-gmc-{RUN}-local-repair-{datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")}.jsonl'
    local_repairs=[]
    with repair_progress.open('w',encoding='utf-8') as f:
        os.chmod(repair_progress,0o600)
        for x in lines:
            if x.get('status')!='error' or x.get('kind')!='image_link_repair' or not str(x.get('product_id','')).startswith('local:'):
                continue
            rec=rec_by_id.get(x['product_id']) or {}
            cur=rec.get('current_content_api_product_resource') or {}
            if not cur or cur.get('get_error'):
                item={**x,'resume_status':'blocked_no_current_resource'}
            else:
                product=json.loads(json.dumps(cur,ensure_ascii=False))
                product.pop('source',None)
                # Keep Content API local identity/resource; change only image fields.
                for k,v in (x.get('attrs') or {}).items(): product[k]=v
                try:
                    resp=upsert_content_product(mid,token,product)
                    item={**x,'resume_status':'local_content_upsert_patched','response_id':resp.get('id'),'response_imageLink':resp.get('imageLink')}
                except Exception as e:
                    item={**x,'resume_status':'local_content_upsert_error','resume_error':str(e)[:1200]}
            local_repairs.append(item); f.write(json.dumps(item,ensure_ascii=False)+'\n'); f.flush(); time.sleep(.25)
    # allow readback
    time.sleep(75)
    verify=[]
    for x in lines:
        pid=x.get('product_id'); rec=rec_by_id.get(pid) or {}; expected=x.get('attrs') or rec.get('planned_attrs') or {}
        if x.get('status')=='error' and x.get('kind')=='image_link_repair' and str(pid).startswith('local:'):
            lr=next((y for y in local_repairs if y.get('product_id')==pid),{})
            if lr.get('resume_status')!='local_content_upsert_patched':
                verify.append({'product_id':pid,'kind':x.get('kind'),'verify_status':'not_verified_resume_failed','resume_status':lr.get('resume_status'),'error':lr.get('resume_error')}); continue
        elif x.get('status')!='patched':
            verify.append({'product_id':pid,'kind':x.get('kind'),'verify_status':'not_verified_execution_status','execution_status':x.get('status'),'error':x.get('error')}); continue
        try:
            cur=abc.content_product_get(mid,token,pid)
            ok,detail=compare_attrs(cur,expected)
            verify.append({'product_id':pid,'kind':x.get('kind'),'verify_status':'read','match_expected':ok,'detail':detail})
        except Exception as e:
            verify.append({'product_id':pid,'kind':x.get('kind'),'verify_status':'error','error':str(e)[:800]})
        time.sleep(.05)
    # status counts after propagation window
    time.sleep(120)
    token=abc.google_access_token(abc.parse_service_account(secrets))
    statuses=aud.list_all('productstatuses',mid,token)
    cnt=Counter(); acted=set(x.get('product_id') for x in lines); cntacted=Counter(); rowsacted=set()
    for st in statuses:
        pid=st.get('productId')
        for iss in st.get('itemLevelIssues') or []:
            code=str(iss.get('code') or iss.get('servability') or iss.get('attributeName'))
            if code in TARGET:
                cnt[code]+=1
                if pid in acted:
                    cntacted[code]+=1; rowsacted.add(pid)
    payload={'generated_at':now(),'status':'completed_with_verify_mismatches' if any(v.get('verify_status')=='read' and not v.get('match_expected') for v in verify) or any(v.get('verify_status') in {'error','not_verified_resume_failed'} for v in verify) else 'completed_verified','source_progress_path':str(progress),'source_rollback_path':str(rollback),'local_repair_progress_path':str(repair_progress),'summary':{'source_progress_lines':len(lines),'source_execution_counts':dict(Counter(x.get('status') for x in lines)),'source_kind_counts':dict(Counter(x.get('kind') for x in lines)),'local_repairs':dict(Counter(x.get('resume_status') for x in local_repairs)),'verify_counts':dict(Counter(v.get('verify_status') for v in verify)),'verify_matches':sum(1 for v in verify if v.get('match_expected')),'verify_mismatches':sum(1 for v in verify if v.get('verify_status')=='read' and not v.get('match_expected')),'productstatuses_read':len(statuses),'target_issue_instances_after':dict(cnt),'target_issue_instances_after_on_acted_ids':dict(cntacted),'acted_ids_with_target_issue_after':len(rowsacted)},'local_repairs':local_repairs,'verify_results':verify,'not_performed':['Shopify write','Tiny write','feed fetch/upload','campaign/message/send','bulk reapply after timeout']}
    OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    lines_md=['# LK GMC residual approved resume/verify — 2026-05-14','',f"Status: `{payload['status']}`",'', '## Summary']
    for k,v in payload['summary'].items(): lines_md.append(f'- {k}: `{v}`')
    lines_md += ['', '## Paths', f'- Progress fonte: `{progress}`', f'- Rollback fonte: `{rollback}`', f'- Local repair progress: `{repair_progress}`', '', '## Não executado'] + [f'- {x}' for x in payload['not_performed']]
    MD.write_text('\n'.join(lines_md)+'\n')
    BRAIN.parent.mkdir(parents=True,exist_ok=True); BRAIN.write_text(MD.read_text())
    print(json.dumps({'status':payload['status'],'summary':payload['summary'],'out':str(OUT),'md':str(MD)},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
