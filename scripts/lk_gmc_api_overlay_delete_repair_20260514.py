#!/usr/bin/env python3
from __future__ import annotations
import json,pathlib,importlib.util,urllib.parse,os,time
from datetime import datetime,timezone
from collections import Counter
ROOT=pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain'); ABC=ROOT/'scripts/lk_execute_approved_abc_20260514.py'; PRIVATE=pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots'); OUT=ROOT/'reports/lk-gmc-2026-05-14-api-overlay-delete-repair.json'
def load():
 spec=importlib.util.spec_from_file_location('abc',ABC); m=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(m); return m
def main():
 abc=load(); sec=abc.load_doppler(); mid=sec['MERCHANT_CENTER_ID_LK']; token=abc.google_access_token(abc.parse_service_account(sec))
 ids=set()
 for p in [PRIVATE/'lk-gmc-2026-05-14-residual-missing-attr-content-api-repair-rollback-20260514T162237Z.json', PRIVATE/'lk-gmc-2026-05-14-residual-non-size-attr-repair-rollback-20260514T163122Z.json']:
  data=json.loads(p.read_text());
  for r in data['records']: ids.add(r['product_id'])
 records=[]
 for pid in sorted(ids):
  try:
   cur=abc.content_product_get(mid,token,pid); src=cur.get('source')
  except Exception as e:
   cur={'get_error':str(e)[:500]}; src=None
  if src=='api': records.append({'product_id':pid,'current_product_resource':cur,'reason':'delete API overlay introduced by failed Content API repair to allow original crawl/feed item to resurface'})
 PRIVATE.mkdir(parents=True,exist_ok=True); os.chmod(PRIVATE,0o700); rb=PRIVATE/f'lk-gmc-2026-05-14-api-overlay-delete-repair-rollback-{datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")}.json'
 rb.write_text(json.dumps({'generated_at':datetime.now(timezone.utc).isoformat(),'scope':'Delete exact Content API source=api overlays created during failed missing-attribute repair; do not touch non-api rows','records':records},ensure_ascii=False,indent=2)+'\n'); os.chmod(rb,0o600)
 results=[]
 for rec in records:
  pid=rec['product_id']; url=f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/products/{urllib.parse.quote(pid,safe="")}'
  try: abc.request_json(url,token=token,method='DELETE'); results.append({'product_id':pid,'status':'deleted_api_overlay'})
  except Exception as e: results.append({'product_id':pid,'status':'error','error':str(e)[:1000]})
  time.sleep(.2)
 time.sleep(90)
 verify=[]
 for rec in records:
  pid=rec['product_id']
  try:
   cur=abc.content_product_get(mid,token,pid); verify.append({'product_id':pid,'verify':'present_after_delete','source':cur.get('source'),'ageGroup':cur.get('ageGroup'),'gender':cur.get('gender'),'sizes':cur.get('sizes'),'color':cur.get('color')})
  except Exception as e: verify.append({'product_id':pid,'verify':'absent_or_waiting','detail':str(e)[:300]})
 payload={'status':'completed_with_errors' if any(r['status']=='error' for r in results) else 'completed','summary':{'selected_api_overlays':len(records),'execution':dict(Counter(r['status'] for r in results)),'verify':dict(Counter(v['verify'] for v in verify))},'rollback_snapshot_path':str(rb),'results':results,'verify':verify}
 OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n'); print(json.dumps({'status':payload['status'],'summary':payload['summary'],'out':str(OUT),'rollback':str(rb)},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
