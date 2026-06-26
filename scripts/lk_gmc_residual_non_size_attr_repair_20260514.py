#!/usr/bin/env python3
from __future__ import annotations
import json,pathlib,importlib.util,os,time
from collections import Counter,defaultdict
from datetime import datetime,timezone
ROOT=pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain'); TRIAGE=ROOT/'reports/lk-gmc-2026-05-14-residual-triage-current.json'; ABC=ROOT/'scripts/lk_execute_approved_abc_20260514.py'; PRIVATE=pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots'); OUT=ROOT/'reports/lk-gmc-2026-05-14-residual-non-size-attr-repair.json'
def load():
 spec=importlib.util.spec_from_file_location('abc',ABC); m=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(m); return m
def main():
 abc=load(); sec=abc.load_doppler(); mid=sec['MERCHANT_CENTER_ID_LK']; token=abc.google_access_token(abc.parse_service_account(sec)); data=json.loads(TRIAGE.read_text())
 grouped={}
 for r in data['rows']:
  missing=[i.get('attributeName') for i in r['issues'] if i['code']=='missing_item_attribute_for_product_type']
  attrs={}
  if 'color' in missing and not r.get('color'):
   t=(r.get('title') or '').lower()
   attrs['color']='Colorido' if any(x in t for x in ['pop mart','labubu','blind box','mickey']) else None
  if 'age group' in missing and not r.get('ageGroup'): attrs['ageGroup']='adult'
  if 'gender' in missing and not r.get('gender'): attrs['gender']='unisex'
  attrs={k:v for k,v in attrs.items() if v}
  if attrs: grouped[r['product_id']]={'row':r,'attrs':attrs}
 PRIVATE.mkdir(parents=True,exist_ok=True); os.chmod(PRIVATE,0o700); rb=PRIVATE/f'lk-gmc-2026-05-14-residual-non-size-attr-repair-rollback-{datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")}.json'
 records=[]; results=[]
 for pid,g in grouped.items():
  cur=abc.content_product_get(mid,token,pid); records.append({'product_id':pid,'current_content_api_product_resource':cur,'planned_attrs':g['attrs']})
 rb.write_text(json.dumps({'generated_at':datetime.now(timezone.utc).isoformat(),'scope':'Merchant API v1 ProductInputs PATCH non-size missing attrs only: color/ageGroup/gender','records':records},ensure_ascii=False,indent=2)+'\n'); os.chmod(rb,0o600)
 for rec in records:
  try:
   abc.patch_product_input_attrs(mid,token,rec['product_id'],rec['planned_attrs']); results.append({'product_id':rec['product_id'],'status':'patched','attrs':rec['planned_attrs']})
  except Exception as e: results.append({'product_id':rec['product_id'],'status':'error','attrs':rec['planned_attrs'],'error':str(e)[:800]})
  time.sleep(.25)
 time.sleep(35); verify=[]
 for rec in records:
  try:
   cur=abc.content_product_get(mid,token,rec['product_id']); act={k:cur.get(k) for k in rec['planned_attrs']}; verify.append({'product_id':rec['product_id'],'expected':rec['planned_attrs'],'actual':act,'match':all(str(act.get(k) or '').lower()==str(v).lower() for k,v in rec['planned_attrs'].items())})
  except Exception as e: verify.append({'product_id':rec['product_id'],'error':str(e)[:500]})
 payload={'status':'completed_with_errors' if any(r['status']=='error' for r in results) else 'completed','summary':{'planned':len(records),'execution':dict(Counter(r['status'] for r in results)),'verify_match':sum(v.get('match') for v in verify),'verify_total':len(verify)},'rollback_snapshot_path':str(rb),'execution_results':results,'verify_results':verify}
 OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n'); print(json.dumps({'status':payload['status'],'summary':payload['summary'],'out':str(OUT),'rollback':str(rb)},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
