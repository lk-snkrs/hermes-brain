#!/usr/bin/env python3
from __future__ import annotations
import importlib.util, json, pathlib, os, time, urllib.parse
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_UP
from typing import Any

ROOT = pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
ABC = ROOT/'scripts/lk_execute_approved_abc_20260514.py'
EXEC = ROOT/'scripts/lk_gmc_residual_approved_executor_20260514.py'
DIAG = ROOT/'reports/lk-gmc-2026-05-14-price-source-diagnostic.json'
PRIVATE = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
RUN = '2026-05-14-price-regular-micro-pilot'
OUT = ROOT/f'reports/lk-gmc-{RUN}.json'
MD = ROOT/f'reports/lk-gmc-{RUN}.md'
BRAIN = ROOT/f'areas/lk/rotinas/gmc-{RUN}.md'
DATA_SOURCE_ID = '10636492695'
APPROVAL = 'Lucas approved micro-pilot GMC preço regular: até 5 online IDs regular_price_stale, Merchant API v1 dataSource 10636492695, rollback privado, sem salePrice/settings/feed/Shopify/Tiny.'

def load(p,n):
    spec=importlib.util.spec_from_file_location(n,p); m=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(m); return m
abc=load(ABC,'abc'); ex=load(EXEC,'ex')

def now(): return datetime.now(timezone.utc).isoformat()

def money(v):
    if v in (None,''): return None
    return f'{Decimal(str(v)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)}'

def micros(v: str) -> int:
    return int((Decimal(v) * Decimal(1000000)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

def amount(d: Any):
    if not isinstance(d,dict): return None
    if 'value' in d: return money(d.get('value'))
    if 'amountMicros' in d: return f"{Decimal(int(d['amountMicros']))/Decimal(1000000):.2f}"
    return None

def merchant_product_get(mid: str, token: str, pid: str):
    _name, encoded, *_ = abc.product_input_name(mid, pid)
    name = f'accounts/{mid}/products/{encoded}'
    return abc.request_json('https://merchantapi.googleapis.com/products/v1/' + urllib.parse.quote(name, safe='/'), token=token)

def status_get(mid: str, token: str, pid: str):
    return abc.request_json(f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/productstatuses/{urllib.parse.quote(pid, safe="")}', token=token)

def patch_price(mid: str, token: str, pid: str, price: str):
    return abc.patch_product_input_attrs(mid, token, pid, {'price': {'amountMicros': micros(price), 'currencyCode': 'BRL'}})

def fresh_target(sec, cur):
    vid=ex.extract_variant_id(cur.get('link')) or (cur.get('offerId') if str(cur.get('offerId','')).isdigit() else None)
    if not vid: return None, {'reason':'no_variant_id'}
    v=ex.shopify_variant_by_legacy(abc, sec, vid)
    if not v: return None, {'reason':'no_shopify_variant','variant_id':vid}
    sp=money(v.get('price')); cap=money(v.get('compareAtPrice'))
    sale=bool(cap and sp and Decimal(cap)>Decimal(sp))
    return {'variant_id':vid,'sku':v.get('sku'),'shopify_price':sp,'shopify_compareAtPrice':cap,'target_price':cap if sale else sp,'target_salePrice':sp if sale else None,'sale_mode':sale}, None

def select_candidates(sec, mid, token, limit=5):
    rows=json.loads(DIAG.read_text()).get('rows',[])
    out=[]; skipped=[]
    for r in rows:
        if r.get('diagnosis')!='merchant_stale_vs_shopify_and_public': continue
        pid=r['product_id']
        if not pid.startswith('online:'): continue
        try:
            cur=abc.content_product_get(mid, token, pid)
            cp, cs = amount(cur.get('price')), amount(cur.get('salePrice'))
            tgt, err = fresh_target(sec, cur)
            if err:
                skipped.append({'product_id':pid,'bucket':'blocked_'+err['reason']}); continue
            if tgt['sale_mode'] or tgt['target_salePrice'] is not None or cs is not None:
                skipped.append({'product_id':pid,'bucket':'excluded_sale_or_current_sale','current_salePrice':cs,'target':tgt}); continue
            if not tgt['target_price'] or cp == tgt['target_price']:
                skipped.append({'product_id':pid,'bucket':'no_action_current_matches_or_no_target','current_price':cp,'target':tgt}); continue
            out.append({'product_id':pid,'current_content':cur,'current_price':cp,'current_salePrice':cs,'target':tgt})
            if len(out)>=limit: break
        except Exception as e:
            skipped.append({'product_id':pid,'bucket':'blocked_error','error':str(e)[:700]})
        time.sleep(0.08)
    return out, skipped

def main():
    sec=abc.load_doppler(); mid=sec['MERCHANT_CENTER_ID_LK']; token=abc.google_access_token(abc.parse_service_account(sec))
    candidates, skipped = select_candidates(sec, mid, token, 5)
    PRIVATE.mkdir(parents=True, exist_ok=True); os.chmod(PRIVATE,0o700)
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    rollback=PRIVATE/f'lk-gmc-{RUN}-rollback-{stamp}.json'
    progress=PRIVATE/f'lk-gmc-{RUN}-progress-{stamp}.jsonl'
    rollback.write_text(json.dumps({'generated_at':now(),'approval':APPROVAL,'scope':'price only, no salePrice, exact online IDs, limit 5','records':[{'product_id':c['product_id'],'current_content_api_product_resource':c['current_content'],'planned_price':c['target']['target_price'],'evidence':c['target']} for c in candidates]}, ensure_ascii=False, indent=2)+'\n')
    os.chmod(rollback,0o600)
    execs=[]
    with progress.open('w', encoding='utf-8') as f:
        os.chmod(progress,0o600)
        for c in candidates:
            try:
                resp=patch_price(mid, token, c['product_id'], c['target']['target_price'])
                res={'product_id':c['product_id'],'status':'patched_price_only','expected_price':c['target']['target_price'],'response_name':resp.get('name')}
            except Exception as e:
                res={'product_id':c['product_id'],'status':'error','expected_price':c['target']['target_price'],'error':str(e)[:1200]}
            execs.append(res); f.write(json.dumps(res,ensure_ascii=False)+'\n'); f.flush(); time.sleep(.5)
    # Give Merchant a short consistency window; status can lag much longer, so do not require productstatus clearance here.
    time.sleep(75)
    verify=[]
    for c in candidates:
        pid=c['product_id']; expected=c['target']['target_price']
        row={'product_id':pid,'expected_price':expected}
        try:
            cur=abc.content_product_get(mid, token, pid)
            row['content_api']={'price':amount(cur.get('price')),'salePrice':amount(cur.get('salePrice')),'source':cur.get('source')}
        except Exception as e: row['content_api']={'error':str(e)[:700]}
        try:
            mp=merchant_product_get(mid, token, pid); pa=mp.get('productAttributes') or {}
            row['merchant_v1']={'price':amount(pa.get('price')),'salePrice':amount(pa.get('salePrice'))}
        except Exception as e: row['merchant_v1']={'error':str(e)[:700]}
        try:
            st=status_get(mid, token, pid); issues=[]
            for iss in st.get('itemLevelIssues') or []:
                if iss.get('code') in {'price_updated','strikethrough_price_updated'}:
                    issues.append({k:iss.get(k) for k in ['code','attributeName','detail','description','resolution','servability']})
            row['productstatus_price_issues']=issues
        except Exception as e: row['productstatus_price_issues_error']=str(e)[:700]
        row['content_match_expected']=(row.get('content_api') or {}).get('price')==expected and (row.get('content_api') or {}).get('salePrice') is None
        row['merchant_v1_match_expected']=(row.get('merchant_v1') or {}).get('price')==expected and (row.get('merchant_v1') or {}).get('salePrice') is None
        verify.append(row); time.sleep(.12)
    payload={'generated_at':now(),'status':'pilot_verified_readback' if candidates and all(v['content_match_expected'] and v['merchant_v1_match_expected'] for v in verify) and not any(e['status']=='error' for e in execs) else 'pilot_completed_needs_review','approval':APPROVAL,'data_source':DATA_SOURCE_ID,'selected_count':len(candidates),'skipped_counts':dict(Counter(s.get('bucket') for s in skipped)),'execution_counts':dict(Counter(e.get('status') for e in execs)),'verify_content_matches':sum(v['content_match_expected'] for v in verify),'verify_merchant_v1_matches':sum(v['merchant_v1_match_expected'] for v in verify),'status_issue_counts_after':dict(Counter(i.get('code') for v in verify for i in v.get('productstatus_price_issues',[]))),'rollback_path':str(rollback),'progress_path':str(progress),'candidates':[{'product_id':c['product_id'],'current_price':c['current_price'],'target':c['target']} for c in candidates],'skipped_sample':skipped[:20],'executions':execs,'verify':verify,'not_performed':['salePrice write','automatic item update settings change','feed fetch/upload','Shopify write','Tiny write','campaign/message/send','bulk price write']}
    OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    lines=['# LK GMC price regular micro-pilot — 2026-05-14','',f"Status: `{payload['status']}`",'', '## Scope','- Até 5 IDs online `regular_price_stale`.','- Campo alterado: `productAttributes.price` somente.','- Excluído: `salePrice`, settings, feeds, Shopify, Tiny, campanhas.',f"- DataSource: `{DATA_SOURCE_ID}`",'', '## Result']
    for k in ['selected_count','execution_counts','verify_content_matches','verify_merchant_v1_matches','status_issue_counts_after']:
        lines.append(f'- {k}: `{payload[k]}`')
    lines += ['', '## IDs']
    for c in payload['candidates']:
        lines.append(f"- `{c['product_id']}`: `{c['current_price']}` → `{c['target']['target_price']}`")
    lines += ['', '## Rollback/progress privado', f"- `{rollback}`", f"- `{progress}`", '', '## Not performed'] + [f'- {x}' for x in payload['not_performed']]
    MD.write_text('\n'.join(lines)+'\n'); BRAIN.write_text(MD.read_text())
    print(json.dumps({k:payload[k] for k in ['status','selected_count','execution_counts','verify_content_matches','verify_merchant_v1_matches','status_issue_counts_after','rollback_path']},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
