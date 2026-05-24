#!/usr/bin/env python3
from __future__ import annotations
import base64, importlib.util, json, os, pathlib, time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from typing import Any

ROOT=pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
ABC=ROOT/'scripts/lk_execute_approved_abc_20260514.py'
EXEC=ROOT/'scripts/lk_gmc_residual_approved_executor_20260514.py'
REPORT_IN=ROOT/'reports/lk-gmc-2026-05-14-residual-approved-resume-verify.json'
PRIVATE=pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
RUN='2026-05-14-price-mismatch-fresh-repair'
OUT=ROOT/f'reports/lk-gmc-{RUN}.json'
MD=ROOT/f'reports/lk-gmc-{RUN}.md'
BRAIN=ROOT/f'areas/lk/rotinas/gmc-{RUN}.md'

def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path); m=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(m); return m
abc=load(ABC,'abc'); ex=load(EXEC,'ex')

def now(): return datetime.now(timezone.utc).isoformat()
def money(v):
    if v in (None,''): return None
    try: return f'{float(v):.2f}'
    except Exception: return str(v)
def cents(v): return {'amountMicros':str(int(round(float(v)*1_000_000))),'currencyCode':'BRL'}
def amount(d):
    if not isinstance(d,dict): return None
    if 'value' in d: return money(d.get('value'))
    if 'amountMicros' in d: return f"{int(d['amountMicros'])/1_000_000:.2f}"
    return None
def compare(cur:dict[str,Any], expected:dict[str,Any]):
    detail={}; ok=True
    for k,exp in expected.items():
        ev=amount(exp); av=amount(cur.get(k)); match=(ev==av)
        detail[k]={'expected':ev,'actual':av,'match':match}; ok=ok and match
    return ok,detail

def main():
    sec=abc.load_doppler(); mid=sec['MERCHANT_CENTER_ID_LK']; token=abc.google_access_token(abc.parse_service_account(sec))
    report=json.loads(REPORT_IN.read_text())
    mismatches=[v for v in report.get('verify_results',[]) if v.get('kind')=='price_saleprice_shopify_variant' and v.get('verify_status')=='read' and not v.get('match_expected')]
    PRIVATE.mkdir(parents=True,exist_ok=True); os.chmod(PRIVATE,0o700)
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    rollback=PRIVATE/f'lk-gmc-{RUN}-rollback-{stamp}.json'
    progress=PRIVATE/f'lk-gmc-{RUN}-progress-{stamp}.jsonl'
    actions=[]; rollback_records=[]; triage=[]
    for row in mismatches:
        pid=row['product_id']
        try:
            cur=abc.content_product_get(mid,token,pid)
            vid=ex.extract_variant_id(cur.get('link')) or (cur.get('offerId') if str(cur.get('offerId','')).isdigit() else None)
            v=ex.shopify_variant_by_legacy(abc,sec,vid) if vid else None
            if not v:
                triage.append({'product_id':pid,'bucket':'blocked_no_shopify_variant','legacy_variant':vid}); continue
            sp=money(v.get('price')); cap=money(v.get('compareAtPrice'))
            sale=bool(cap and sp and float(cap)>float(sp))
            target_price=cap if sale else sp
            target_sale=sp if sale else None
            cur_price=amount(cur.get('price')); cur_sale=amount(cur.get('salePrice'))
            attrs={}
            # For sale rows, send both price and salePrice together; earlier salePrice-only masks did not reliably persist.
            if sale:
                if target_price and (cur_price!=target_price or cur_sale!=target_sale):
                    attrs['price']=cents(target_price); attrs['salePrice']=cents(target_sale)
            else:
                if cur_sale:
                    triage.append({'product_id':pid,'bucket':'review_clear_salePrice_no_shopify_sale','legacy_variant':vid,'shopify_price':sp,'shopify_compareAtPrice':cap,'merchant_price':cur_price,'merchant_salePrice':cur_sale})
                    continue
                if target_price and cur_price!=target_price:
                    attrs['price']=cents(target_price)
            if attrs:
                rollback_records.append({'product_id':pid,'current_content_api_product_resource':cur,'planned_attrs':attrs,'evidence':{'shopify_variant_legacy':vid,'sku':v.get('sku'),'shopify_price':sp,'shopify_compareAtPrice':cap,'merchant_price':cur_price,'merchant_salePrice':cur_sale}})
                actions.append({'product_id':pid,'attrs':attrs})
                triage.append({'product_id':pid,'bucket':'needs_patch_sale' if 'salePrice' in attrs else 'needs_patch_price','legacy_variant':vid})
            else:
                triage.append({'product_id':pid,'bucket':'no_action_current_matches_shopify','legacy_variant':vid,'shopify_price':sp,'shopify_compareAtPrice':cap,'merchant_price':cur_price,'merchant_salePrice':cur_sale})
        except Exception as e:
            triage.append({'product_id':pid,'bucket':'blocked_error','error':str(e)[:800]})
        time.sleep(.06)
    rollback.write_text(json.dumps({'generated_at':now(),'approval':'Lucas approved correcting remaining LK OS/GMC residuals in Telegram; fresh repair only for price mismatches that do not match live Shopify variant prices.','records':rollback_records},ensure_ascii=False,indent=2)+'\n'); os.chmod(rollback,0o600)
    execs=[]
    with progress.open('w',encoding='utf-8') as f:
        os.chmod(progress,0o600)
        for a in actions:
            try:
                resp=abc.patch_product_input_attrs(mid,token,a['product_id'],a['attrs'])
                res={'product_id':a['product_id'],'status':'patched','attrs':a['attrs'],'response_name':resp.get('name')}
            except Exception as e:
                res={'product_id':a['product_id'],'status':'error','attrs':a['attrs'],'error':str(e)[:1200]}
            execs.append(res); f.write(json.dumps(res,ensure_ascii=False)+'\n'); f.flush(); time.sleep(.35)
    time.sleep(90)
    verify=[]
    for a in actions:
        try:
            cur=abc.content_product_get(mid,token,a['product_id'])
            ok,detail=compare(cur,a['attrs'])
            verify.append({'product_id':a['product_id'],'status':'read','match_expected':ok,'detail':detail})
        except Exception as e:
            verify.append({'product_id':a['product_id'],'status':'error','error':str(e)[:800]})
        time.sleep(.07)
    payload={'generated_at':now(),'status':'completed_verified' if actions and all(v.get('match_expected') for v in verify) and not any(e.get('status')=='error' for e in execs) else 'completed_with_review','input_mismatches':len(mismatches),'triage_counts':dict(Counter(t.get('bucket') for t in triage)),'actions_count':len(actions),'execution_counts':dict(Counter(e.get('status') for e in execs)),'verify_counts':dict(Counter(v.get('status') for v in verify)),'verify_matches':sum(1 for v in verify if v.get('match_expected')),'verify_mismatches':sum(1 for v in verify if v.get('status')=='read' and not v.get('match_expected')),'rollback_path':str(rollback),'progress_path':str(progress),'triage':triage,'executions':execs,'verify':verify,'not_performed':['Shopify write','Tiny write','feed fetch/upload','campaign/message/send','bulk reapply','salePrice clearing for no-Shopify-sale rows']}
    OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    lines=['# LK GMC price mismatch fresh repair — 2026-05-14','',f"Status: `{payload['status']}`",'', '## Summary']
    for k in ['input_mismatches','triage_counts','actions_count','execution_counts','verify_counts','verify_matches','verify_mismatches']:
        lines.append(f'- {k}: `{payload[k]}`')
    lines += ['', '## Paths', f'- Rollback privado: `{rollback}`', f'- Progresso privado: `{progress}`', '', '## Não executado'] + [f'- {x}' for x in payload['not_performed']]
    MD.write_text('\n'.join(lines)+'\n')
    BRAIN.write_text(MD.read_text())
    print(json.dumps({k:payload[k] for k in ['status','input_mismatches','triage_counts','actions_count','execution_counts','verify_matches','verify_mismatches','rollback_path','progress_path']},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
