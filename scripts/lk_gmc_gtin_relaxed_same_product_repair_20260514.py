#!/usr/bin/env python3
from __future__ import annotations
import importlib.util, json, os, pathlib, re, time, urllib.parse, urllib.request
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT=pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
ABC=ROOT/'scripts/lk_execute_approved_abc_20260514.py'
TRIAGE=ROOT/'reports/lk-gmc-2026-05-14-residual-triage-current.json'
PRIVATE=pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
RUN='2026-05-14-gtin-relaxed-same-product-repair'
OUT=ROOT/f'reports/lk-gmc-{RUN}.json'
MD=ROOT/f'reports/lk-gmc-{RUN}.md'
BRAIN=ROOT/f'areas/lk/rotinas/gmc-{RUN}.md'
DATA_SOURCE_ID='10636492695'
APPROVAL=(
    'Lucas approved relaxed GTIN rule by Telegram voice: for GMC, GTIN does not need to match exact size; '
    'use a GTIN from another size when the product/model is the same because Google maps/metas the variant later.'
)
TARGET_CODES={'restricted_gtin','reserved_gtin'}


def now(): return datetime.now(timezone.utc).isoformat()

def load_abc():
    spec=importlib.util.spec_from_file_location('abc',ABC)
    m=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(m); return m

def clean_sku(offer:str|None,title:str|None='') -> str:
    s=re.sub(r'^LIA_','',str(offer or '').strip())
    # Numeric Nike/Jordan SKUs sometimes lose the color hyphen: 553558612-6 -> 553558-612.
    m=re.match(r'([A-Z0-9]+-\d{3})(?:-\d+)?$',s, re.I)
    if m: return m.group(1).upper()
    m=re.match(r'(\d{6})(\d{3})(?:-\d+)?$',s)
    if m: return (m.group(1)+'-'+m.group(2)).upper()
    # Some LK/POS SKUs lose the hyphen: DD1503601-39 -> DD1503-601.
    m=re.match(r'([A-Z]{1,3}\d{4})(\d{3})(?:-\d+)?$',s, re.I)
    if m: return (m.group(1)+'-'+m.group(2)).upper()
    # Adidas/New Balance style IDs often have no color hyphen: IE0875-5 -> IE0875; U9060ZGE-4 -> U9060ZGE.
    m=re.match(r'([A-Z]{1,3}\d{3,5}[A-Z]{0,4})(?:-\d+)?$',s, re.I)
    if m: return m.group(1).upper()
    m=re.search(r'\b([A-Z0-9]{2,12}-\d{3})\b', title or '', re.I)
    if m: return m.group(1).upper()
    m=re.search(r'\b([A-Z]{1,3}\d{4})(\d{3})\b', title or '', re.I)
    if m: return (m.group(1)+'-'+m.group(2)).upper()
    return s.upper()

def style_sku(raw:str|None,title:str|None='') -> str:
    return clean_sku(raw, title)

def extract_variant_id(link:str|None):
    qs=urllib.parse.parse_qs(urllib.parse.urlparse(link or '').query)
    return (qs.get('variant') or [None])[0]

def normalize_tokens(text:str|None):
    stop={'tenis','tênis','nike','air','jordan','adidas','asics','new','balance','the','of','low','high','mid','og','sb','x','branco','preto','cinza','azul','vermelho','marrom','verde','colorido','bege','rosa','premium'}
    toks=[]
    for t in re.findall(r'[a-z0-9]+', (text or '').lower()):
        if len(t)>=3 and t not in stop: toks.append(t)
    return set(toks)

def valid_gtin(value:Any)->bool:
    s=str(value or '').strip()
    # For GMC/LK, avoid GTIN-8 because Merchant can classify short retailer/article codes as reserved.
    # Use normal UPC/EAN/GTIN-12/13/14 only.
    if not re.fullmatch(r'\d{12,14}',s): return False
    if s.startswith(('2','02','04')): return False
    # GS1 mod-10 check digit. Left pad to 14 for uniform validation.
    body=s[:-1]; check=int(s[-1]); rev=list(map(int, body[::-1]))
    total=sum((3 if i%2==0 else 1)*d for i,d in enumerate(rev))
    return (10-total%10)%10 == check

def request_kicks(sec,path,params):
    key=sec.get('KICKS_DEV_API_KEY') or sec.get('KICKS_API_KEY') or sec.get('KICKSDB_API_KEY')
    if not key: return {'error':'missing_kicks_key'}
    url='https://api.kicks.dev'+path+'?'+urllib.parse.urlencode(params)
    req=urllib.request.Request(url,headers={'Authorization':'Bearer '+key})
    try:
        with urllib.request.urlopen(req,timeout=12) as r: return json.loads(r.read().decode())
    except Exception as e:
        return {'error':str(e)[:500]}

def gql(abc,secrets,query,variables): return abc.shopify_graphql(secrets,query,variables)

def shopify_variant_by_legacy(abc,secrets,legacy):
    if not legacy: return None
    q='''query V($id:ID!){ productVariant(id:$id){ id legacyResourceId title sku barcode product{id legacyResourceId title handle vendor tags} } }'''
    gid='gid://shopify/ProductVariant/'+str(legacy)
    return (gql(abc,secrets,q,{'id':gid}).get('data') or {}).get('productVariant')

def select_gtin(row, vals, sku):
    row_tokens=normalize_tokens(' '.join([row.get('title') or '', row.get('brand') or '', sku or '']))
    candidates=[]
    for x in vals:
        ident=x.get('identifier') or x.get('gtin')
        if not valid_gtin(ident):
            continue
        if str(ident)==str(row.get('gtin') or ''):
            continue
        if sku and str(x.get('sku') or '').upper()!=str(sku).upper():
            continue
        name=x.get('name') or x.get('title') or ''
        cand_tokens=normalize_tokens(' '.join([name, x.get('brand') or '', x.get('sku') or '']))
        overlap=len(row_tokens & cand_tokens)
        # SKU equality is the hard product identity. Token overlap catches obvious unrelated API noise.
        if overlap < 1 and not sku:
            continue
        candidates.append({'identifier':str(ident),'size':x.get('size'),'name':name,'brand':x.get('brand'),'sku':x.get('sku'),'overlap':overlap,'source':x.get('source')})
    # Prefer highest title overlap, then stable UPC/EAN length before arbitrary Kicks ordering.
    candidates.sort(key=lambda c:(-c['overlap'], 0 if len(c['identifier']) in (12,13) else 1, c['identifier']))
    return candidates[0] if candidates else None, candidates[:5]

def main():
    abc=load_abc(); sec=abc.load_doppler(); mid=sec['MERCHANT_CENTER_ID_LK']; token=abc.google_access_token(abc.parse_service_account(sec))
    data=json.loads(TRIAGE.read_text())
    rows=[r for r in data['rows'] if TARGET_CODES & {i.get('code') for i in r.get('issues',[])}]
    PRIVATE.mkdir(parents=True,exist_ok=True); os.chmod(PRIVATE,0o700)
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    rollback=PRIVATE/f'lk-gmc-{RUN}-rollback-{stamp}.json'
    progress=PRIVATE/f'lk-gmc-{RUN}-progress-{stamp}.jsonl'
    actions=[]; skipped=[]; snapshots=[]
    for r in rows:
        pid=r['product_id']; channel=pid.split(':',1)[0]
        vid=extract_variant_id(r.get('link'))
        variant=None
        try:
            variant=shopify_variant_by_legacy(abc,sec,vid) if vid else None
        except Exception as e:
            skipped.append({'product_id':pid,'reason':'shopify_variant_lookup_error','error':str(e)[:300]})
        sku=style_sku((variant or {}).get('sku') or r.get('offerId'), r.get('title'))
        if not sku or not (re.search(r'[A-Z0-9]+-\d{3}',sku,re.I) or re.search(r'^[A-Z]{1,3}\d{3,5}[A-Z]{0,4}$',sku,re.I) or re.search(r'^\d{6}-\d{3}$',sku)):
            skipped.append({'product_id':pid,'reason':'no_safe_style_sku','sku':sku})
            continue
        kd=request_kicks(sec,'/v3/unified/gtin',{'sku':sku,'limit':100,'source':'stockx'})
        vals=kd.get('data') or []
        chosen, sample=select_gtin(r, vals, sku)
        if not chosen:
            skipped.append({'product_id':pid,'reason':'no_valid_same_sku_kicks_gtin','sku':sku,'kicks_count':len(vals),'sample':sample,'kicks_error':kd.get('error')})
            time.sleep(.18); continue
        if channel!='online':
            # Local/LIA rows are intentionally not patched here: their source/provider is Shopify POS/local inventory.
            # Avoid creating a wrong data-source overlay. Online counterpart may be fixed separately when present.
            skipped.append({'product_id':pid,'reason':'local_lia_not_patched_in_this_wave','sku':sku,'selected_gtin':chosen['identifier'],'evidence':chosen})
            time.sleep(.18); continue
        try:
            cur=abc.content_product_get(mid,token,pid)
        except Exception as e:
            cur={'get_error':str(e)[:500]}
        # Merchant API v1 ProductAttributes uses repeated `gtins`; Content API readback exposes singular `gtin`.
        attr={'gtins':[chosen['identifier']]}
        snapshots.append({'product_id':pid,'current_content_api_product_resource':cur,'target_attrs':attr,'evidence':{'sku':sku,'kicks_selected':chosen,'rule':'same product/style SKU; exact size match not required per Lucas'}})
        actions.append({'product_id':pid,'attrs':attr,'evidence':{'sku':sku,'kicks_selected':chosen,'current_gtin':r.get('gtin')}})
        time.sleep(.18)
    rollback.write_text(json.dumps({'generated_at':now(),'approval':APPROVAL,'dataSource':DATA_SOURCE_ID,'records':snapshots},ensure_ascii=False,indent=2)+'\n'); os.chmod(rollback,0o600)
    execs=[]
    with progress.open('w',encoding='utf-8') as f:
        os.chmod(progress,0o600)
        for a in actions:
            try:
                res=abc.patch_product_input_attrs(mid,token,a['product_id'],a['attrs'])
                out={'product_id':a['product_id'],'status':'patched','attrs':a['attrs'],'response_name':res.get('name')}
            except Exception as e:
                out={'product_id':a['product_id'],'status':'error','error':str(e)[:1200],'attrs':a['attrs']}
            execs.append(out); f.write(json.dumps(out,ensure_ascii=False)+'\n'); f.flush(); time.sleep(.35)
    time.sleep(45 if actions else 0)
    verify=[]
    for a in actions:
        expected=(a['attrs'].get('gtins') or [a['attrs'].get('gtin')])[0]
        try:
            cur=abc.content_product_get(mid,token,a['product_id'])
            actual=cur.get('gtin') or ((cur.get('gtins') or [None])[0] if isinstance(cur.get('gtins'), list) else None)
            verify.append({'product_id':a['product_id'],'expected_gtin':expected,'actual_gtin':actual,'verify':'match' if str(actual)==str(expected) else 'mismatch'})
        except Exception as e:
            verify.append({'product_id':a['product_id'],'expected_gtin':expected,'verify':'error','error':str(e)[:500]})
        time.sleep(.08)
    payload={
        'generated_at':now(),'approval':APPROVAL,
        'status':'completed_with_errors' if any(e['status']=='error' for e in execs) else 'completed',
        'summary':{
            'gtin_issue_rows_seen':len(rows),'planned_online_patches':len(actions),
            'execution':dict(Counter(e['status'] for e in execs)),
            'verify':dict(Counter(v['verify'] for v in verify)),
            'skipped_by_reason':dict(Counter(s['reason'] for s in skipped))
        },
        'rollback_snapshot_path':str(rollback),'progress_path':str(progress),
        'actions':actions,'execution_results':execs,'verify_results':verify,'skipped':skipped,
        'not_performed':['local/LIA GTIN patch (avoided POS/local inventory data-source overlay)','Shopify write','Tiny write','feed fetch/upload','campaign/message/send','price/title/image/availability changes']
    }
    OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    lines=['# LK GMC GTIN relaxed same-product repair — 2026-05-14','',f"Status: `{payload['status']}`",'', '## Summary']
    for k,v in payload['summary'].items(): lines.append(f'- {k}: `{v}`')
    lines += ['', '## Rule', '- Same product/style SKU is sufficient; exact size GTIN match is not required per Lucas voice approval.', '- GTINs starting with 2/02/04 or failing check digit were rejected.', '', '## Snapshots', f'- Rollback privado: `{rollback}`', f'- Progress privado: `{progress}`', '', '## Não executado'] + [f'- {x}' for x in payload['not_performed']]
    MD.write_text('\n'.join(lines)+'\n')
    BRAIN.parent.mkdir(parents=True,exist_ok=True); BRAIN.write_text(MD.read_text())
    print(json.dumps({'status':payload['status'],'summary':payload['summary'],'out':str(OUT),'rollback':str(rollback)},ensure_ascii=False,indent=2))

if __name__=='__main__': main()
