#!/usr/bin/env python3
"""Verify completed Wave4 aggressive non-price progress after terminal timeout."""
from __future__ import annotations
import importlib.util, json, pathlib, time
from collections import Counter
from datetime import datetime, timezone

ROOT=pathlib.Path(__file__).resolve().parents[1]
WAVE4_PATH=ROOT/'scripts/lk_gmc_p1_attribute_wave4_aggressive_nonprice_executor_20260513.py'
ROLLBACK=pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-13-p1-attribute-wave4-aggressive-nonprice-executor-rollback-20260513T141552Z.json')
PROGRESS=pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-13-p1-attribute-wave4-aggressive-nonprice-executor-progress-20260513T141552Z.jsonl')
OUT=ROOT/'reports/lk-gmc-2026-05-13-p1-attribute-wave4-aggressive-nonprice-timeout-recovered-verify.json'
MD=ROOT/'reports/lk-gmc-2026-05-13-p1-attribute-wave4-aggressive-nonprice-timeout-recovered-verify.md'
BRAIN=ROOT/'areas/lk/rotinas/gmc-2026-05-13-p1-attribute-wave4-aggressive-nonprice-timeout-recovered-verify.md'

def load_wave4():
    spec=importlib.util.spec_from_file_location('wave4', WAVE4_PATH); mod=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(mod); return mod

def utc_now(): return datetime.now(timezone.utc).isoformat()

def main():
    w=load_wave4(); audit=w.import_audit(); secrets=audit.load_doppler(); mid=secrets.get('MERCHANT_CENTER_ID_LK')
    token=audit.google_access_token(audit.parse_service_account(secrets))
    rollback=json.loads(ROLLBACK.read_text(encoding='utf-8'))
    planned={rec['product_id']:rec['planned_update'] for rec in rollback['records']}
    progress=[json.loads(x) for x in PROGRESS.read_text(encoding='utf-8').splitlines() if x.strip()]
    # Verify all progress rows. No new writes.
    verified=[]
    for res in progress:
        pid=res.get('product_id'); row=planned.get(pid,{})
        if res.get('execution_status')!='updated_wave4_aggressive_nonprice_attrs' or not pid:
            verified.append({**res,'verify_status':'not_verified_due_to_execution_status'}); continue
        try:
            prod=w.get_product(mid,pid,token); ok=True; actual={}
            for k,v in (row.get('suggested_attributes') or {}).items():
                av=w.norm_list(prod.get(k)) if k=='sizes' else prod.get(k); actual[k]=av; ok=ok and (av==v)
            verified.append({**res,'verify_status':'verified_product_get','actual_attrs':actual,'attrs_match_expected':ok})
        except Exception as e:
            verified.append({**res,'verify_status':'verify_failed','verify_error':str(e)[:1200]})
    time.sleep(90)
    post=w.post_status_recheck(mid,token)
    ec=Counter(r.get('execution_status') for r in progress); vc=Counter(r.get('verify_status') for r in verified); matched=sum(1 for r in verified if r.get('attrs_match_expected'))
    field_counts=Counter(k for rec in rollback['records'] for k in rec['planned_update'].get('suggested_attributes',{}))
    payload={'generated_at':utc_now(),'status':'gmc_p1_attribute_wave4_aggressive_nonprice_apply_timeout_recovered_verified','mode':'apply_recovered_verify_only','scope':'Recovered verification for Wave4 apply after terminal timeout. Progress shows writes completed; this script performed no writes, only products.get and productstatuses recheck.','source_labels':['fact_merchant_center','manual_approval','derived_reconciliation'],'rollback_snapshot':str(ROLLBACK),'progress_jsonl':str(PROGRESS),'summary':{'planned_records':len(rollback['records']),'progress_rows':len(progress),'execution_results_summary':dict(ec),'verify_results_summary':dict(vc),'verified_attrs_match_expected':matched,'suggested_field_counts':dict(field_counts),**post},'verified_results':verified,'not_performed':['merchant_write_in_recovery_script','merchant_price_update','merchant_delete','feed_update_or_fetch','shopify_write','tiny_call_or_write','database_write','klaviyo_or_whatsapp_send','notion_or_n8n_write','loyalty_or_judgeme_action']}
    OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    lines=['# LK GMC P1 Attribute Completion — Wave4 Timeout-Recovered Verify, 2026-05-13','',f"Status: `{payload['status']}`",'','## Resultado',f"- Planned records: {len(rollback['records'])}",f"- Progress rows: {len(progress)}",f"- Execution: {dict(ec)}",f"- Verify: {dict(vc)}",f"- Match esperado: {matched}/{len(verified)}",f"- Required rows after: {post['required_attr_rows_after']}",f"- Required instances after: {post['required_attr_instances_after']}",f"- Counts after: {post['required_attr_counts_after']}",'','## Rollback privado',f'- `{ROLLBACK}`','','## Não executado na recuperação']
    for n in payload['not_performed']: lines.append(f'- {n}')
    MD.write_text('\n'.join(lines)+'\n',encoding='utf-8'); BRAIN.write_text(MD.read_text(encoding='utf-8'),encoding='utf-8')
    print(json.dumps({'status':payload['status'],'summary':payload['summary'],'report':str(MD)},ensure_ascii=False,indent=2))

if __name__=='__main__': main()
