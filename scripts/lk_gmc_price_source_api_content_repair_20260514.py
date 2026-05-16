#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,json,os,pathlib,time
from collections import Counter
from datetime import datetime,timezone
from typing import Any
ROOT=pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
ABC=ROOT/'scripts/lk_execute_approved_abc_20260514.py'
EXEC=ROOT/'scripts/lk_gmc_residual_approved_executor_20260514.py'
SRC=ROOT/'reports/lk-gmc-2026-05-14-residual-approved-resume-verify.json'
PRIVATE=pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
RUN='2026-05-14-price-source-api-content-repair'
OUT=ROOT/f'reports/lk-gmc-{RUN}.json'; MD=ROOT/f'reports/lk-gmc-{RUN}.md'; BRAIN=ROOT/f'areas/lk/rotinas/gmc-{RUN}.md'
def load(p,n):
 spec=importlib.util.spec_from_file_location(n,p); m=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(m); return m
abc=load(ABC,'abc'); ex=load(EXEC,'ex')
def now(): return datetime.now(timezone.utc).isoformat()
def money(v):
 if v in (None,''): return None
 try: return f'{float(v):.2f}'
 except Exception: return str(v)
def price_obj(v): return {'value':money(v),'currency':'BRL'}
def amount(d):
 if not isinstance(d,dict): return None
 if 'value' in d: return money(d.get('value'))
 if 'amountMicros' in d: return f"{int(d['amountMicros'])/1_000_000:.2f}"
 return None
def upsert(mid,token,product):
 p=json.loads(json.dumps(product,ensure_ascii=False))
 p.pop('source',None)
 return abc.request_json(f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/products',token=token,method='POST',payload=p,attempts=5,timeout=120)
def main():
 sec=abc.load_doppler(); mid=sec['MERCHANT_CENTER_ID_LK']; token=abc.google_access_token(abc.parse_service_account(sec))
 report=json.loads(SRC.read_text())
 targets=[v['product_id'] for v in report.get('verify_results',[]) if v.get('kind')=='price_saleprice_shopify_variant' and v.get('verify_status')=='read' and not v.get('match_expected')]
 PRIVATE.mkdir(parents=True,exist_ok=True); os.chmod(PRIVATE,0o700); stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
 rollback=PRIVATE/f'lk-gmc-{RUN}-rollback-{stamp}.json'; progress=PRIVATE/f'lk-gmc-{RUN}-progress-{stamp}.jsonl'
 actions=[]; snaps=[]; triage=[]
 for pid in targets:
  try:
   cur=abc.content_product_get(mid,token,pid)
   if cur.get('source')!='api': triage.append({'product_id':pid,'bucket':'blocked_non_api_source','source':cur.get('source')}); continue
   vid=ex.extract_variant_id(cur.get('link')) or (cur.get('offerId') if str(cur.get('offerId','')).isdigit() else None)
   v=ex.shopify_variant_by_legacy(abc,sec,vid) if vid else None
   if not v: triage.append({'product_id':pid,'bucket':'blocked_no_shopify_variant','legacy_variant':vid}); continue
   sp=money(v.get('price')); cap=money(v.get('compareAtPrice')); sale=bool(cap and sp and float(cap)>float(sp))
   target_price=cap if sale else sp; target_sale=sp if sale else None
   cur_price=amount(cur.get('price')); cur_sale=amount(cur.get('salePrice'))
   if (cur_price==target_price) and ((cur_sale==target_sale) if sale else (cur_sale is None)):
    triage.append({'product_id':pid,'bucket':'no_action_current_matches_shopify','legacy_variant':vid}); continue
   prod=json.loads(json.dumps(cur,ensure_ascii=False))
   if target_price: prod['price']=price_obj(target_price)
   if sale: prod['salePrice']=price_obj(target_sale)
   else: prod.pop('salePrice',None)
   actions.append({'product_id':pid,'product':prod,'expected':{'price':target_price,'salePrice':target_sale},'evidence':{'legacy_variant':vid,'sku':v.get('sku'),'shopify_price':sp,'shopify_compareAtPrice':cap,'merchant_price':cur_price,'merchant_salePrice':cur_sale,'sale':sale}})
   snaps.append({'product_id':pid,'current_content_api_product_resource':cur,'planned_price':target_price,'planned_salePrice':target_sale,'evidence':actions[-1]['evidence']})
   triage.append({'product_id':pid,'bucket':'needs_content_upsert_sale' if sale else ('needs_content_upsert_clear_sale' if cur_sale else 'needs_content_upsert_price'),'legacy_variant':vid})
  except Exception as e: triage.append({'product_id':pid,'bucket':'blocked_error','error':str(e)[:800]})
  time.sleep(.06)
 rollback.write_text(json.dumps({'generated_at':now(),'approval':'Lucas approved correcting remaining LK OS/GMC residuals; Content API upsert restricted to source=api product resources, preserving full resource and changing price/salePrice only.','records':snaps},ensure_ascii=False,indent=2)+'\n'); os.chmod(rollback,0o600)
 execs=[]
 with progress.open('w',encoding='utf-8') as f:
  os.chmod(progress,0o600)
  for a in actions:
   try:
    resp=upsert(mid,token,a['product'])
    res={'product_id':a['product_id'],'status':'content_upserted','response_id':resp.get('id'),'expected':a['expected']}
   except Exception as e: res={'product_id':a['product_id'],'status':'error','error':str(e)[:1200],'expected':a['expected']}
   execs.append(res); f.write(json.dumps(res,ensure_ascii=False)+'\n'); f.flush(); time.sleep(.35)
 time.sleep(90)
 verify=[]
 for a in actions:
  try:
   cur=abc.content_product_get(mid,token,a['product_id'])
   cp,cs=amount(cur.get('price')),amount(cur.get('salePrice'))
   ok=(cp==a['expected']['price'] and cs==a['expected']['salePrice'])
   verify.append({'product_id':a['product_id'],'status':'read','match_expected':ok,'actual_price':cp,'actual_salePrice':cs,'expected':a['expected']})
  except Exception as e: verify.append({'product_id':a['product_id'],'status':'error','error':str(e)[:800]})
  time.sleep(.07)
 payload={'generated_at':now(),'status':'completed_verified' if actions and all(v.get('match_expected') for v in verify) and not any(e.get('status')=='error' for e in execs) else 'completed_with_review','input_targets':len(targets),'triage_counts':dict(Counter(t.get('bucket') for t in triage)),'actions_count':len(actions),'execution_counts':dict(Counter(e.get('status') for e in execs)),'verify_counts':dict(Counter(v.get('status') for v in verify)),'verify_matches':sum(1 for v in verify if v.get('match_expected')),'verify_mismatches':sum(1 for v in verify if v.get('status')=='read' and not v.get('match_expected')),'rollback_path':str(rollback),'progress_path':str(progress),'triage':triage,'executions':execs,'verify':verify,'not_performed':['Shopify write','Tiny write','feed fetch/upload','campaign/message/send','non-api source upsert']}
 OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
 lines=['# LK GMC price source=api Content repair — 2026-05-14','',f"Status: `{payload['status']}`",'', '## Summary']
 for k in ['input_targets','triage_counts','actions_count','execution_counts','verify_matches','verify_mismatches']:
  lines.append(f'- {k}: `{payload[k]}`')
 lines += ['', '## Paths', f'- Rollback privado: `{rollback}`', f'- Progresso privado: `{progress}`', '', '## Não executado']+[f'- {x}' for x in payload['not_performed']]
 MD.write_text('\n'.join(lines)+'\n'); BRAIN.write_text(MD.read_text())
 print(json.dumps({k:payload[k] for k in ['status','input_targets','triage_counts','actions_count','execution_counts','verify_matches','verify_mismatches','rollback_path']},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
