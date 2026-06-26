#!/usr/bin/env python3
from __future__ import annotations
import json,pathlib,os,importlib.util,time
from collections import Counter
from datetime import datetime,timezone
ROOT=pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
EXEC=ROOT/'reports/lk-gmc-2026-05-14-residual-approved-executor.json'
ABC=ROOT/'scripts/lk_execute_approved_abc_20260514.py'
ONDA=ROOT/'scripts/lk_gmc_p1_attribute_completion_onda1_executor_20260513.py'
PRIVATE=pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
OUT=ROOT/'reports/lk-gmc-2026-05-14-residual-missing-attr-repair.json'
MD=ROOT/'reports/lk-gmc-2026-05-14-residual-missing-attr-repair.md'
def load(p,n):
 spec=importlib.util.spec_from_file_location(n,p); m=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(m); return m
def main():
 abc=load(ABC,'abc'); onda=load(ONDA,'onda'); sec=abc.load_doppler(); mid=sec['MERCHANT_CENTER_ID_LK']; token=abc.google_access_token(abc.parse_service_account(sec))
 data=json.loads(EXEC.read_text()); actions={a['product_id']:a for a in data['actions'] if a['kind']=='missing_attribute_completion'}
 errs=[e for e in data['execution_results'] if e['status']=='error' and e['kind']=='missing_attribute_completion']
 PRIVATE.mkdir(parents=True,exist_ok=True); os.chmod(PRIVATE,0o700)
 rb=PRIVATE/f'lk-gmc-2026-05-14-residual-missing-attr-content-api-repair-rollback-{datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")}.json'
 records=[]; results=[]
 for e in errs:
  pid=e['product_id']; attrs=actions[pid]['attrs']
  cur=abc.content_product_get(mid,token,pid)
  records.append({'product_id':pid,'current_product_resource':cur,'planned_update':attrs,'reason':'repair prior Merchant API ProductInputs v1 rejected sizes; Content API products.insert supports sizes'})
 rb.write_text(json.dumps({'generated_at':datetime.now(timezone.utc).isoformat(),'scope':'Exact residual missing-attribute repair via Content API products.insert/upsert for sizes/ageGroup/gender/color only','records':records},ensure_ascii=False,indent=2)+'\n'); os.chmod(rb,0o600)
 for rec in records:
  body=onda.prepare_updated_product(rec['current_product_resource'],rec['planned_update'])
  try:
   resp=onda.upsert_product(mid,body,token); results.append({'product_id':rec['product_id'],'status':'upserted_content_api','updated':rec['planned_update'],'response_subset':{k:resp.get(k) for k in rec['planned_update']}})
  except Exception as e:
   results.append({'product_id':rec['product_id'],'status':'error','updated':rec['planned_update'],'error':str(e)[:1200]}); break
  time.sleep(.25)
 time.sleep(30)
 verify=[]
 for rec in records:
  try:
   cur=abc.content_product_get(mid,token,rec['product_id']); actual={k:cur.get(k) for k in rec['planned_update']}
   verify.append({'product_id':rec['product_id'],'status':'read','expected':rec['planned_update'],'actual':actual,'match':all(actual.get(k)==v for k,v in rec['planned_update'].items())})
  except Exception as e: verify.append({'product_id':rec['product_id'],'status':'error','error':str(e)[:500]})
 payload={'generated_at':datetime.now(timezone.utc).isoformat(),'status':'completed_with_errors' if any(r['status']=='error' for r in results) else 'completed','summary':{'target_rows':len(records),'execution':dict(Counter(r['status'] for r in results)),'verify_match':sum(v.get('match') for v in verify),'verify_total':len(verify)},'rollback_snapshot_path':str(rb),'execution_results':results,'verify_results':verify,'not_performed':['price','gtin','image','landing page','Shopify/Tiny/feed/campaign']}
 OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
 MD.write_text('\n'.join(['# LK GMC residual missing attr repair — 2026-05-14','',f"Status: `{payload['status']}`",f"- Target rows: {len(records)}",f"- Execução: {payload['summary']['execution']}",f"- Readback match: {payload['summary']['verify_match']}/{payload['summary']['verify_total']}",f"- Rollback privado: `{rb}`"])+"\n")
 print(json.dumps({'status':payload['status'],'summary':payload['summary'],'out':str(OUT),'rollback':str(rb)},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
