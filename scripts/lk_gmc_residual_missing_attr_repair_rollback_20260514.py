#!/usr/bin/env python3
from __future__ import annotations
import json,pathlib,os,importlib.util,time
from collections import Counter
ROOT=pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
RB=pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-14-residual-missing-attr-content-api-repair-rollback-20260514T162237Z.json')
ONDA=ROOT/'scripts/lk_gmc_p1_attribute_completion_onda1_executor_20260513.py'
ABC=ROOT/'scripts/lk_execute_approved_abc_20260514.py'
OUT=ROOT/'reports/lk-gmc-2026-05-14-residual-missing-attr-repair-rollback-applied.json'
def load(p,n):
 spec=importlib.util.spec_from_file_location(n,p); m=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(m); return m
def main():
 abc=load(ABC,'abc'); onda=load(ONDA,'onda'); sec=abc.load_doppler(); mid=sec['MERCHANT_CENTER_ID_LK']; token=abc.google_access_token(abc.parse_service_account(sec))
 data=json.loads(RB.read_text()); res=[]; ver=[]
 for rec in data['records']:
  body=json.loads(json.dumps(rec['current_product_resource'],ensure_ascii=False))
  for k in ['id','kind','source']: body.pop(k,None)
  try:
   onda.upsert_product(mid,body,token); res.append({'product_id':rec['product_id'],'status':'restored_prior_resource'})
  except Exception as e:
   res.append({'product_id':rec['product_id'],'status':'error','error':str(e)[:1000]}); break
  time.sleep(.25)
 time.sleep(45)
 for rec in data['records']:
  try:
   cur=abc.content_product_get(mid,token,rec['product_id']); ver.append({'product_id':rec['product_id'],'status':'read','ageGroup':cur.get('ageGroup'),'gender':cur.get('gender'),'sizes':cur.get('sizes')})
  except Exception as e: ver.append({'product_id':rec['product_id'],'status':'error','error':str(e)[:500]})
 payload={'status':'completed_with_errors' if any(r['status']=='error' for r in res) else 'completed','source_rollback':str(RB),'execution':dict(Counter(r['status'] for r in res)),'results':res,'verify':ver}
 OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'status':payload['status'],'execution':payload['execution'],'out':str(OUT)},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
