#!/usr/bin/env python3
"""Read-only recovery verifier for LK GMC P2A color + shoes scale.

The apply process completed PATCH progress rows but failed during final productstatuses
probe because its OAuth access token expired. This script does not reapply anything: it
loads the private progress JSONL, obtains a fresh token, verifies Merchant product attrs,
then writes public recovery reports.
"""
from __future__ import annotations
import importlib.util, json, pathlib, time
from collections import Counter
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
P2_PATH = ROOT / 'scripts/lk_gmc_p2_category_product_type_executor_20260513.py'
PROGRESS = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-13-p2a-color-and-shoes-scale-progress-20260513T171051Z.jsonl')
ROLLBACK = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-13-p2a-color-and-shoes-scale-rollback-20260513T171051Z.json')
PUBLIC_JSON = ROOT / 'reports/lk-gmc-2026-05-13-p2a-color-and-shoes-scale-timeout-recovered-verify.json'
PUBLIC_MD = ROOT / 'reports/lk-gmc-2026-05-13-p2a-color-and-shoes-scale-timeout-recovered-verify.md'
COLOR_PID = 'online:pt:BR:SLBCS'
COLOR_EXPECTED = 'Verde'
SHOES_GPC = 'Apparel & Accessories > Shoes'
SHOES_PT = ['Calçados']

def utc_now(): return datetime.now(timezone.utc).isoformat()

def load_mod(path, name):
    spec=importlib.util.spec_from_file_location(name, path)
    mod=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(mod)
    return mod

def merchant_attrs(p2, mid, token, pid):
    _name, encoded, *_ = p2.product_input_name(mid, pid)
    return (p2.merchant_product_get(mid, encoded, token).get('productAttributes') or {})

def required_probe(w, mid, token):
    statuses=w.list_all('productstatuses', mid, token)
    required_rows=[]; issue_counts=Counter(); req_counts=Counter()
    for st in statuses:
        for issue in st.get('itemLevelIssues') or []:
            issue_counts[issue.get('code') or 'unknown'] += 1
        attrs=w.required_attrs(st)
        if attrs:
            pid=st.get('productId') or st.get('id')
            required_rows.append({'product_id':pid,'required_attrs':sorted(list(attrs)),'title':st.get('title')})
            for a in attrs: req_counts[a]+=1
    return {'fresh_productstatuses_after':len(statuses),'required_attr_rows_after':len(required_rows),'required_attr_counts_after':dict(req_counts.most_common()),'required_rows_sample':required_rows[:20],'top_item_level_issue_counts_after':dict(issue_counts.most_common(15))}

def main():
    p2=load_mod(P2_PATH,'p2_recover')
    w=p2.import_w4(); audit=w.import_audit(); secrets=audit.load_doppler(); mid=secrets.get('MERCHANT_CENTER_ID_LK'); token=audit.google_access_token(audit.parse_service_account(secrets))
    rows=[json.loads(x) for x in PROGRESS.read_text(encoding='utf-8').splitlines() if x.strip()]
    verify=[]
    for item in rows:
        pid=item['product_id']
        try:
            attrs=merchant_attrs(p2, mid, token, pid)
            if item.get('execution_status')=='patched_color_v1':
                match=attrs.get('color')==COLOR_EXPECTED
                verify.append({**item,'verify_status':'verified_merchant_product_get','actual_color':attrs.get('color'),'match_expected':match})
            elif item.get('execution_status')=='patched_p2a_shoes_v1':
                match=attrs.get('googleProductCategory')==SHOES_GPC and (attrs.get('productTypes') or [])==SHOES_PT
                verify.append({**item,'verify_status':'verified_merchant_product_get','actual_googleProductCategory':attrs.get('googleProductCategory'),'actual_productTypes':attrs.get('productTypes') or [],'match_expected':match})
            else:
                verify.append({**item,'verify_status':'not_verified_due_to_execution_status'})
        except Exception as e:
            verify.append({**item,'verify_status':'verify_failed','verify_error':str(e)[:1200]})
        time.sleep(0.025)
    post=required_probe(w, mid, token)
    summary={
        'progress_rows': len(rows),
        'execution_results_summary': dict(Counter(x.get('execution_status') for x in rows)),
        'verify_results_summary': dict(Counter(x.get('verify_status') for x in verify)),
        'verified_match_expected': sum(1 for x in verify if x.get('match_expected')),
        'mismatches_sample': [x for x in verify if not x.get('match_expected')][:20],
        **post,
    }
    payload={'generated_at':utc_now(),'status':'timeout_recovered_verified' if summary['verified_match_expected']==len(verify) else 'timeout_recovered_with_mismatches','source_failure':'original apply process failed only during final productstatuses probe due ACCESS_TOKEN_EXPIRED after writing/verifying progress rows','progress_jsonl':str(PROGRESS),'private_rollback_snapshot_path':str(ROLLBACK),'summary':summary,'verify_results':verify,'not_performed':['no_writes','no_reapply','no_delete','no_shopify_tiny_db_campaign_message_changes']}
    PUBLIC_JSON.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    lines=['# LK GMC P2A — Color + Shoes scale timeout-recovered verify, 2026-05-13','',f"Status: `{payload['status']}`",'', '## Resultado',f"- Progress rows: {summary['progress_rows']}",f"- Execution: {summary['execution_results_summary']}",f"- Verify: {summary['verify_results_summary']}",f"- Match esperado: {summary['verified_match_expected']}/{len(verify)}",f"- Productstatuses after: {post['fresh_productstatuses_after']}",f"- Required attr rows after: {post['required_attr_rows_after']}",f"- Required attr counts after: {post['required_attr_counts_after']}",f"- Top issues after: {post['top_item_level_issue_counts_after']}",'','## Recuperação','- Processo original falhou na sondagem final por ACCESS_TOKEN_EXPIRED; este verificador usou token novo e não reaplicou nada.','','## Rollback privado',f"- `{ROLLBACK}`",'', '## Não executado']
    lines += [f"- {x}" for x in payload['not_performed']]
    PUBLIC_MD.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(json.dumps({'status':payload['status'],'summary':summary,'report':str(PUBLIC_MD)},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
