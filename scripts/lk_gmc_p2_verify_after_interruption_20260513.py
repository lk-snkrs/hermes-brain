#!/usr/bin/env python3
"""Verify LK GMC P2A pilot after interrupted terminal wrapper; no writes."""
from __future__ import annotations
import importlib.util, json, pathlib, time
from collections import Counter
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
P2 = ROOT / 'scripts/lk_gmc_p2_category_product_type_executor_20260513.py'
OUT_JSON = ROOT / 'reports/lk-gmc-2026-05-13-p2-category-product-type-post-interruption-verify.json'
OUT_MD = ROOT / 'reports/lk-gmc-2026-05-13-p2-category-product-type-post-interruption-verify.md'
PROGRESS = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-13-p2-category-product-type-executor-progress-20260513T163349Z.jsonl')

def load_mod(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(mod)
    return mod

def main():
    p2 = load_mod(P2, 'p2')
    w = p2.import_w4(); audit = w.import_audit(); secrets = audit.load_doppler(); mid = secrets.get('MERCHANT_CENTER_ID_LK')
    token = audit.google_access_token(audit.parse_service_account(secrets))
    candidates = {r['product_id']: r for r in p2.load_candidates(100)}
    progressed=[]
    for line in PROGRESS.read_text(encoding='utf-8').splitlines():
        if line.strip(): progressed.append(json.loads(line))
    verify=[]
    for item in progressed:
        r = candidates.get(item['product_id'])
        if item.get('execution_status') != 'patched_p2a_category_product_type_v1' or not r:
            verify.append({**item, 'verify_status':'not_verified_due_to_execution_status_or_candidate_missing'})
            continue
        try:
            _name, encoded, _lang, _label, _offer = p2.product_input_name(mid, r['product_id'])
            mp = p2.merchant_product_get(mid, encoded, token)
            attrs = mp.get('productAttributes') or {}
            match = attrs.get('googleProductCategory') == r['suggested_googleProductCategory'] and (attrs.get('productTypes') or []) == r['suggested_productTypes']
            verify.append({**item, 'verify_status':'verified_merchant_product_get', 'expected_googleProductCategory': r['suggested_googleProductCategory'], 'expected_productTypes': r['suggested_productTypes'], 'actual_googleProductCategory': attrs.get('googleProductCategory'), 'actual_productTypes': attrs.get('productTypes') or [], 'match_expected': match})
        except Exception as e:
            verify.append({**item, 'verify_status':'verify_failed', 'verify_error': str(e)[:1500]})
        time.sleep(0.1)
    statuses = w.list_all('productstatuses', mid, token)
    required_rows=0; required_counts=Counter(); issue_counts=Counter()
    for st in statuses:
        for issue in st.get('itemLevelIssues') or []:
            issue_counts[issue.get('code') or 'unknown'] += 1
        attrs=w.required_attrs(st)
        if attrs:
            required_rows += 1
            for a in attrs: required_counts[a]+=1
    vc=Counter(v.get('verify_status') for v in verify)
    payload={'generated_at':datetime.now(timezone.utc).isoformat(),'mode':'read_only_post_interruption_verify','progress_path':str(PROGRESS),'summary':{'progressed_rows':len(progressed),'progress_execution_counts':dict(Counter(i.get('execution_status') for i in progressed)),'verify_counts':dict(vc),'match_expected':sum(1 for v in verify if v.get('match_expected')),'fresh_productstatuses_after':len(statuses),'required_attr_rows_after':required_rows,'required_attr_counts_after':dict(required_counts.most_common()),'top_item_level_issue_counts_after':dict(issue_counts.most_common(12))},'verify_results':verify,'not_performed':['no_writes','no_reapply','no_delete','no_shopify_tiny_db_campaign_message_changes']}
    OUT_JSON.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    lines=['# LK GMC P2A Post-Interruption Verify — 2026-05-13','',f"Status: `{'verified' if payload['summary']['match_expected']==len(progressed) else 'needs_review'}`",'', '## Resultado',f"- Progress rows: {len(progressed)}",f"- Execução progress: {payload['summary']['progress_execution_counts']}",f"- Verify: {payload['summary']['verify_counts']}",f"- Match esperado: {payload['summary']['match_expected']}/{len(progressed)}",f"- Productstatuses: {len(statuses)}",f"- Required attr rows after: {required_rows}",f"- Required counts after: {dict(required_counts.most_common())}",f"- Top issues after: {dict(issue_counts.most_common(12))}",'','## Não executado']
    lines += [f"- {x}" for x in payload['not_performed']]
    OUT_MD.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(json.dumps({'status':'verified' if payload['summary']['match_expected']==len(progressed) else 'needs_review','summary':payload['summary'],'report':str(OUT_MD)},ensure_ascii=False,indent=2))

if __name__ == '__main__': main()
