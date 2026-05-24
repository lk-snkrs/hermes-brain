#!/usr/bin/env python3
from __future__ import annotations
import importlib.util, json, pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
P2=ROOT/'scripts/lk_gmc_p2_category_product_type_executor_20260513.py'
OUT=ROOT/'reports/lk-gmc-2026-05-13-post-p2a-required-attr-single-row-probe.json'
def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path); mod=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(mod); return mod
p2=load(P2,'p2'); w=p2.import_w4(); audit=w.import_audit(); secrets=audit.load_doppler(); mid=secrets.get('MERCHANT_CENTER_ID_LK'); token=audit.google_access_token(audit.parse_service_account(secrets))
statuses=w.list_all('productstatuses', mid, token)
rows=[]
for st in statuses:
    attrs=w.required_attrs(st)
    if attrs:
        rows.append({'product_id':st.get('productId') or st.get('product_id') or st.get('id'),'required_attrs':sorted(list(attrs)),'title':st.get('title'), 'issues':st.get('itemLevelIssues')})
OUT.write_text(json.dumps({'count':len(rows),'rows':rows},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'count':len(rows),'rows':rows[:5],'report':str(OUT)},ensure_ascii=False,indent=2))
