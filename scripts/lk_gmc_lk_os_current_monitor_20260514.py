#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,json,pathlib,os,time
from collections import Counter,defaultdict
from datetime import datetime,timezone
ROOT=pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
ABC=ROOT/'scripts/lk_execute_approved_abc_20260514.py'
AUD=ROOT/'scripts/lk_gmc_catalog_duplication_audit_20260512.py'
RESUME=ROOT/'reports/lk-gmc-2026-05-14-residual-approved-resume-verify.json'
REPAIR=ROOT/'reports/lk-gmc-2026-05-14-price-source-api-content-repair.json'
OUT=ROOT/'reports/lk-gmc-2026-05-14-lk-os-current-monitor.json'
MD=ROOT/'reports/lk-gmc-2026-05-14-lk-os-current-monitor.md'
BRAIN=ROOT/'areas/lk/rotinas/gmc-2026-05-14-lk-os-current-monitor.md'
TARGET={'price_updated','strikethrough_price_updated','missing_item_attribute_for_product_type','restricted_gtin','reserved_gtin','landing_page_error','image_single_color','image_link_broken','landing_page_pending_crawl'}
def load(p,n):
 spec=importlib.util.spec_from_file_location(n,p); m=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(m); return m
abc=load(ABC,'abc'); aud=load(AUD,'aud')
def now(): return datetime.now(timezone.utc).isoformat()
def main():
 sec=abc.load_doppler(); mid=sec['MERCHANT_CENTER_ID_LK']; token=abc.google_access_token(abc.parse_service_account(sec))
 statuses=aud.list_all('productstatuses',mid,token)
 cnt=Counter(); affected=defaultdict(set)
 for st in statuses:
  pid=st.get('productId')
  for iss in st.get('itemLevelIssues') or []:
   code=str(iss.get('code') or iss.get('servability') or iss.get('attributeName'))
   if code in TARGET:
    cnt[code]+=1; affected[code].add(pid)
 resume=json.loads(RESUME.read_text()) if RESUME.exists() else {}
 repair=json.loads(REPAIR.read_text()) if REPAIR.exists() else {}
 payload={'generated_at':now(),'productstatuses_read':len(statuses),'target_issue_instances':dict(cnt),'target_product_counts':{k:len(v) for k,v in affected.items()},'last_resume_status':resume.get('status'),'last_resume_summary':resume.get('summary',{}),'price_repair_status':repair.get('status'),'price_repair_summary':{k:repair.get(k) for k in ['input_targets','triage_counts','actions_count','execution_counts','verify_matches','verify_mismatches']},'not_performed':['Shopify write','Tiny write','feed fetch/upload','campaign/message/send','bulk reapply after non-persisting price writes']}
 OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
 lines=['# LK OS current GMC monitor — 2026-05-14','',f"Generated: `{payload['generated_at']}`",'',f"Productstatuses read: `{len(statuses)}`",'', '## Target issue instances']
 for k,v in sorted(cnt.items()): lines.append(f'- {k}: `{v}` instances / `{len(affected[k])}` products')
 lines += ['', '## Latest execution readout', f"- Resume status: `{payload['last_resume_status']}`", f"- Price repair status: `{payload['price_repair_status']}`", f"- Price repair summary: `{payload['price_repair_summary']}`", '', '## Não executado']+[f'- {x}' for x in payload['not_performed']]
 MD.write_text('\n'.join(lines)+'\n'); BRAIN.write_text(MD.read_text())
 print(json.dumps({'productstatuses_read':len(statuses),'target_issue_instances':dict(cnt),'target_product_counts':payload['target_product_counts'],'price_repair_status':payload['price_repair_status'],'price_verify_mismatches':payload['price_repair_summary'].get('verify_mismatches')},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
