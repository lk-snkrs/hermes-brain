#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,json,os,pathlib,time,urllib.parse
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT=pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
ABC=ROOT/'scripts/lk_execute_approved_abc_20260514.py'
APPLY=ROOT/'reports/lk-gmc-2026-05-14-lia-gtin-apply.json'
OUT=ROOT/'reports/lk-gmc-2026-05-14-lia-gtin-point-repair.json'
MD=ROOT/'reports/lk-gmc-2026-05-14-lia-gtin-point-repair.md'
BRAIN=ROOT/'areas/lk/rotinas/gmc-2026-05-14-lia-gtin-point-repair.md'
PRIV=pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
TARGET_CODES={'reserved_gtin','restricted_gtin'}
REPAIRS={
 'local:pt:BR:LIA_FN5880-001-1':'196977897832',
 'local:pt:BR:LIA_FN5880-001-3':'196977897832',
 'local:pt:BR:LIA_FN5880-001-6':'196977897832',
 'local:pt:BR:LIA_HJ3386-300-8':'197601227759',
}

def load(path,name):
 spec=importlib.util.spec_from_file_location(name,path); m=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(m); return m
abc=load(ABC,'abc')
def now(): return datetime.now(timezone.utc).isoformat()
def product_status_get(mid,token,pid):
 return abc.request_json(f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/productstatuses/{urllib.parse.quote(pid,safe="")}',token=token,attempts=4,timeout=90)
def upsert(mid,token,product):
 return abc.request_json(f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/products',token=token,method='POST',payload=product,attempts=5,timeout=120)
def codes(st): return sorted(set(i.get('code') for i in (st.get('itemLevelIssues') or []) if i.get('code') in TARGET_CODES))
def main():
 sec=abc.load_doppler(); mid=sec['MERCHANT_CENTER_ID_LK']; token=abc.google_access_token(abc.parse_service_account(sec))
 PRIV.mkdir(parents=True,exist_ok=True); os.chmod(PRIV,0o700)
 stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
 rb=PRIV/f'lk-gmc-lia-gtin-point-repair-rollback-{stamp}.json'
 progress=PRIV/f'lk-gmc-lia-gtin-point-repair-progress-{stamp}.jsonl'
 records=[]; execs=[]
 for pid,target in REPAIRS.items():
  cur=abc.content_product_get(mid,token,pid)
  records.append({'product_id':pid,'current_product_resource':cur,'old_gtin':cur.get('gtin'),'new_gtin':target})
 rb.write_text(json.dumps({'generated_at':now(),'scope':'Point repair local/LIA GTINs still flagged reserved_gtin after first apply; change only gtin','records':records},ensure_ascii=False,indent=2)+'\n'); os.chmod(rb,0o600)
 progress.write_text(''); os.chmod(progress,0o600)
 for rec in records:
  prod=json.loads(json.dumps(rec['current_product_resource'])); prod.pop('source',None); prod['gtin']=rec['new_gtin']
  try:
   resp=upsert(mid,token,prod); item={'product_id':rec['product_id'],'status':'patched','old_gtin':rec['old_gtin'],'new_gtin':rec['new_gtin'],'response_id':resp.get('id')}
  except Exception as e:
   item={'product_id':rec['product_id'],'status':'error','old_gtin':rec['old_gtin'],'new_gtin':rec['new_gtin'],'error':str(e)[:1000]}; execs.append(item); break
  execs.append(item); progress.open('a').write(json.dumps(item,ensure_ascii=False)+'\n'); time.sleep(.4)
 time.sleep(95)
 verify=[]
 for rec in records:
  fresh=abc.content_product_get(mid,token,rec['product_id'])
  verify.append({'product_id':rec['product_id'],'expected_gtin':rec['new_gtin'],'actual_gtin':fresh.get('gtin'),'match':fresh.get('gtin')==rec['new_gtin']})
 time.sleep(75)
 token=abc.google_access_token(abc.parse_service_account(sec))
 # Recheck all 34 from prior apply if available, otherwise just repairs.
 prev=json.loads(APPLY.read_text())
 all_ids=[r['product_id'] for r in prev.get('execution_results',[])] or list(REPAIRS)
 st=[]
 for pid in all_ids:
  try: s=product_status_get(mid,token,pid); st.append({'product_id':pid,'target_issue_codes':codes(s),'all_issue_codes':sorted(set(i.get('code') for i in (s.get('itemLevelIssues') or []) if i.get('code')))})
  except Exception as e: st.append({'product_id':pid,'status_read':'error','error':str(e)[:500]})
  time.sleep(.15)
 payload={'generated_at':now(),'status':'completed' if all(v['match'] for v in verify) else 'completed_with_readback_mismatch','summary':{'repair_count':len(records),'execution_counts':dict(Counter(x['status'] for x in execs)),'verify_counts':dict(Counter('match' if v['match'] else 'mismatch' for v in verify)),'final_rows_with_target_issue':sum(1 for x in st if x.get('target_issue_codes')),'final_target_issue_counts':dict(Counter(c for x in st for c in x.get('target_issue_codes',[])))},'rollback_snapshot_path':str(rb),'progress_jsonl_path':str(progress),'execution_results':execs,'verified_results':verify,'final_productstatus_results':st,'not_performed':['Shopify write','Tiny write','POS/local inventory config','price/title/category/image/availability update','feed upload/fetch','campaign/message/send']}
 OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
 lines=['# LK GMC Local/LIA GTIN point repair — 2026-05-14','',f"Gerado em: `{payload['generated_at']}`",'', '## Resultado', f"- Status: `{payload['status']}`", f"- Reparos: `{payload['summary']['repair_count']}`", f"- Execução: `{payload['summary']['execution_counts']}`", f"- Readback: `{payload['summary']['verify_counts']}`", f"- Productstatuses finais com issue GTIN alvo nos 34: `{payload['summary']['final_rows_with_target_issue']}`; `{payload['summary']['final_target_issue_counts']}`",'', '## Não executado']+[f'- {x}' for x in payload['not_performed']]
 MD.write_text('\n'.join(lines)+'\n'); BRAIN.write_text(MD.read_text())
 print(json.dumps({'status':payload['status'],'summary':payload['summary'],'out':str(OUT)},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
