#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, pathlib
from collections import Counter
from datetime import datetime, timezone

ROOT=pathlib.Path(__file__).resolve().parents[1]
P2=ROOT/'scripts/lk_gmc_p2_category_product_type_executor_20260513.py'
OUT_JSON=ROOT/'reports/lk-gmc-2026-05-13-p2a-next-online-fresh-post-status-target.json'
OUT_MD=ROOT/'reports/lk-gmc-2026-05-13-p2a-next-online-fresh-post-status-target.md'

def load_mod(path,name):
    spec=importlib.util.spec_from_file_location(name,path); mod=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(mod); return mod

def load_ids(progress):
    ids=[]
    for line in pathlib.Path(progress).read_text(encoding='utf-8').splitlines():
        if not line.strip(): continue
        d=json.loads(line)
        if d.get('execution_status')=='patched_p2a_next_v1': ids.append(d['product_id'])
    return ids

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--progress',required=True); args=ap.parse_args()
    p2=load_mod(P2,'p2status'); w=p2.import_w4(); audit=w.import_audit(); secrets=audit.load_doppler(); mid=secrets.get('MERCHANT_CENTER_ID_LK'); token=audit.google_access_token(audit.parse_service_account(secrets))
    target=set(load_ids(args.progress))
    statuses=w.list_all('productstatuses',mid,token)
    rows=[]; issue_counts=Counter(); req_counts=Counter()
    for st in statuses:
        pid=st.get('productId') or st.get('id') or ''
        if pid not in target: continue
        req=sorted(w.required_attrs(st)); issues=[i.get('code') or 'unknown' for i in (st.get('itemLevelIssues') or [])]
        rows.append({'product_id':pid,'required_attrs':req,'issue_codes':issues})
        for a in req: req_counts[a]+=1
        for c in issues: issue_counts[c]+=1
    payload={'generated_at':datetime.now(timezone.utc).isoformat(),'status':'post_status_recheck_target_ids_fresh','target_count':len(target),'status_rows_found':len(rows),'required_attr_counts_target':dict(req_counts.most_common()),'issue_counts_target':dict(issue_counts.most_common()),'rows_sample':rows[:50]}
    OUT_JSON.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    lines=['# LK GMC P2A Fresh Post-status Target Recheck','',f"Status: `{payload['status']}`",'',f"- Target count: {payload['target_count']}",f"- Status rows found: {payload['status_rows_found']}",f"- Required attr counts target: {payload['required_attr_counts_target']}",f"- Issue counts target: {payload['issue_counts_target']}"]
    OUT_MD.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(json.dumps({'status':payload['status'],'target_count':len(target),'status_rows_found':len(rows),'required_attr_counts_target':payload['required_attr_counts_target'],'issue_counts_target':payload['issue_counts_target'],'report':str(OUT_MD)},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
