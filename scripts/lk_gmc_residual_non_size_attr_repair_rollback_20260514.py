#!/usr/bin/env python3
from __future__ import annotations
import json,pathlib,importlib.util,time
ROOT=pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
RB=pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-14-residual-non-size-attr-repair-rollback-20260514T163122Z.json')
ONDA=ROOT/'scripts/lk_gmc_p1_attribute_completion_onda1_executor_20260513.py'; ABC=ROOT/'scripts/lk_execute_approved_abc_20260514.py'; OUT=ROOT/'reports/lk-gmc-2026-05-14-residual-non-size-attr-repair-rollback-applied.json'
def load(p,n):
 spec=importlib.util.spec_from_file_location(n,p); m=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(m); return m
def main():
 abc=load(ABC,'abc'); onda=load(ONDA,'onda'); sec=abc.load_doppler(); mid=sec['MERCHANT_CENTER_ID_LK']; token=abc.google_access_token(abc.parse_service_account(sec)); data=json.loads(RB.read_text()); res=[]
 for rec in data['records']:
  body=json.loads(json.dumps(rec['current_content_api_product_resource'],ensure_ascii=False))
  for k in ['id','kind','source']: body.pop(k,None)
  try: onda.upsert_product(mid,body,token); res.append({'product_id':rec['product_id'],'status':'restored'})
  except Exception as e: res.append({'product_id':rec['product_id'],'status':'error','error':str(e)[:1000]}); break
  time.sleep(.25)
 OUT.write_text(json.dumps({'status':'completed','source_rollback':str(RB),'results':res},ensure_ascii=False,indent=2)+'\n'); print(json.dumps({'status':'completed','out':str(OUT),'count':len(res)},ensure_ascii=False))
if __name__=='__main__': main()
