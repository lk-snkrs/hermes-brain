#!/usr/bin/env python3
from __future__ import annotations
import importlib.util, json, pathlib, re, time, urllib.parse, urllib.request
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT=pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
ABC=ROOT/'scripts/lk_execute_approved_abc_20260514.py'
GTIN_HELPER=ROOT/'scripts/lk_gmc_gtin_relaxed_same_product_repair_20260514.py'
TRIAGE=ROOT/'reports/lk-gmc-2026-05-14-residual-triage-current.json'
OUT=ROOT/'reports/lk-gmc-2026-05-14-lia-gtin-preview.json'
MD=ROOT/'reports/lk-gmc-2026-05-14-lia-gtin-preview.md'
BRAIN=ROOT/'areas/lk/rotinas/gmc-2026-05-14-lia-gtin-preview.md'
TARGET_CODES={'restricted_gtin','reserved_gtin'}

def now(): return datetime.now(timezone.utc).isoformat()

def load_module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(m); return m

def request_kicks(sec,path,params):
    key=sec.get('KICKS_DEV_API_KEY') or sec.get('KICKS_API_KEY') or sec.get('KICKSDB_API_KEY')
    if not key: return {'error':'missing_kicks_key'}
    url='https://api.kicks.dev'+path+'?'+urllib.parse.urlencode(params)
    req=urllib.request.Request(url,headers={'Authorization':'Bearer '+key})
    try:
        with urllib.request.urlopen(req,timeout=12) as r: return json.loads(r.read().decode())
    except Exception as e:
        return {'error':str(e)[:500]}

def title_search_query(title):
    t=re.sub(r'\b(T[eê]nis|Sneaker|Branco|Preto|Cinza|Vermelho|Verde|Marrom|Rosa|Colorido|Azul|Bege|Dourado|Prata)\b',' ',title or '', flags=re.I)
    t=re.sub(r'\s+',' ',t).strip()
    return t[:90]

def compact_product(x):
    return {k:x.get(k) for k in ['identifier','sku','size','name','brand','source','title','id'] if x.get(k) is not None}

def main():
    abc=load_module(ABC,'abc')
    gh=load_module(GTIN_HELPER,'gtin_helper')
    sec=abc.load_doppler(); mid=sec['MERCHANT_CENTER_ID_LK']; token=abc.google_access_token(abc.parse_service_account(sec))
    data=json.loads(TRIAGE.read_text())
    local_rows=[r for r in data['rows'] if str(r.get('product_id','')).startswith('local:') and TARGET_CODES & {i.get('code') for i in r.get('issues',[])}]
    out=[]
    for r in local_rows:
        pid=r['product_id']
        item={'product_id':pid,'offerId':r.get('offerId'),'title':r.get('title'),'current_gtin':r.get('gtin'),'issues':[i.get('code') for i in r.get('issues',[]) if i.get('code') in TARGET_CODES]}
        try:
            cur=abc.content_product_get(mid,token,pid)
        except Exception as e:
            cur={'get_error':str(e)[:500]}
        item['merchant_source']={k:cur.get(k) for k in ['id','source','channel','offerId','mpn','itemGroupId','contentLanguage','targetCountry','gtin']}
        raw_sku=cur.get('mpn') or r.get('offerId') or ''
        style=gh.style_sku(raw_sku, r.get('title'))
        item['normalized_style_sku']=style
        kd={'data':[]}
        if style and (re.search(r'[A-Z0-9]+-\d{3}',style,re.I) or re.search(r'^[A-Z]{1,3}\d{3,5}[A-Z]{0,4}$',style,re.I) or re.search(r'^\d{6}-\d{3}$',style)):
            kd=request_kicks(sec,'/v3/unified/gtin',{'sku':style,'limit':100,'source':'stockx'})
            chosen,sample=gh.select_gtin(r,kd.get('data') or [],style)
            if chosen:
                item.update({'candidate_state':'candidate_same_style_sku','recommended_gtin':chosen['identifier'],'kicks_evidence':chosen,'kicks_sample':sample[:3]})
            else:
                item.update({'candidate_state':'no_valid_gtin_by_style_sku','kicks_count':len(kd.get('data') or []),'kicks_error':kd.get('error'),'kicks_sample':[compact_product(x) for x in (kd.get('data') or [])[:3]]})
        else:
            item['candidate_state']='needs_title_search_no_safe_style_sku'
        if item.get('candidate_state') in {'no_valid_gtin_by_style_sku','needs_title_search_no_safe_style_sku'}:
            q=title_search_query(r.get('title'))
            sr=request_kicks(sec,'/v3/stockx/products',{'query':q,'limit':5})
            products=sr.get('data') or []
            # Prefer first title-search product with a SKU that returns a valid GTIN and overlaps product tokens.
            selected=None; selected_gtin=None; selected_sample=[]
            for p in products[:5]:
                sku=p.get('sku') or p.get('styleId')
                if not sku: continue
                gd=request_kicks(sec,'/v3/unified/gtin',{'sku':sku,'limit':50,'source':'stockx'})
                fake=dict(r); fake['title']=' '.join([r.get('title') or '', p.get('title') or '', p.get('name') or ''])
                ch,samp=gh.select_gtin(fake,gd.get('data') or [],sku)
                if ch:
                    selected=p; selected_gtin=ch; selected_sample=samp[:3]; break
                time.sleep(.12)
            if selected_gtin:
                item.update({'candidate_state':'candidate_title_search_fallback','title_search_query':q,'stockx_product':compact_product(selected),'recommended_gtin':selected_gtin['identifier'],'kicks_evidence':selected_gtin,'kicks_sample':selected_sample})
            else:
                item.update({'title_search_query':q,'title_search_sample':[compact_product(x) for x in products[:3]]})
        if item.get('recommended_gtin'):
            item['recommended_write_route']='approval_required_content_api_full_local_product_update_preserve_resource_change_gtin_only'
            item['risk']='medium_local_inventory_pos_visibility'
        else:
            item['recommended_write_route']='blocked_no_safe_gtin_candidate'
            item['risk']='n/a'
        out.append(item); time.sleep(.15)
    payload={'generated_at':now(),'read_only':True,'source_labels':['fact_merchant_center','fact_shopify_pos_local_inventory_inferred','market_signal_kicks_dev'],'summary':{'local_lia_gtin_rows':len(local_rows),'by_candidate_state':dict(Counter(x['candidate_state'] for x in out)),'candidate_writes_if_approved':sum(1 for x in out if x.get('recommended_gtin')),'blocked_no_candidate':sum(1 for x in out if not x.get('recommended_gtin'))},'rows':out,'not_performed':['Merchant write','Content API insert/update','Shopify write','Tiny write','local inventory/POS changes','feed fetch/upload','campaign/message/send']}
    OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    lines=['# LK GMC local/LIA GTIN preview — 2026-05-14','',f"Generated: `{payload['generated_at']}`",'', '## Summary']
    for k,v in payload['summary'].items(): lines.append(f'- {k}: `{v}`')
    lines += ['', '## Write route if approved', '- Local/LIA rows are `source=api`, `channel=local`; Merchant API ProductInputs read returned 404 for sampled local rows.', '- Recommended route is **not** ProductInputs v1. Use Content API full product-resource update/insert preserving the current local product and changing only `gtin`, with private rollback before every row.', '- Pilot first; local inventory affects physical-store/local surfaces.', '', '## Candidate examples']
    for x in out[:12]:
        lines.append(f"- `{x['product_id']}` → state `{x['candidate_state']}`; current `{x.get('current_gtin')}`; recommended `{x.get('recommended_gtin','')}`; style `{x.get('normalized_style_sku')}`")
    lines += ['', '## Não executado'] + [f'- {x}' for x in payload['not_performed']]
    MD.write_text('\n'.join(lines)+'\n')
    BRAIN.parent.mkdir(parents=True,exist_ok=True); BRAIN.write_text(MD.read_text())
    print(json.dumps({'summary':payload['summary'],'out':str(OUT),'md':str(MD)},ensure_ascii=False,indent=2))

if __name__=='__main__': main()
