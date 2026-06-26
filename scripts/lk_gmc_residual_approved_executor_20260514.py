#!/usr/bin/env python3
from __future__ import annotations
import base64,json,os,pathlib,re,time,urllib.parse,importlib.util
from collections import Counter,defaultdict
from datetime import datetime,timezone
from typing import Any
ROOT=pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
ABC=ROOT/'scripts/lk_execute_approved_abc_20260514.py'
TRIAGE=ROOT/'reports/lk-gmc-2026-05-14-residual-triage-current.json'
PRIVATE=pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
RUN='2026-05-14-residual-approved-executor'
OUT=ROOT/f'reports/lk-gmc-{RUN}.json'; MD=ROOT/f'reports/lk-gmc-{RUN}.md'; BRAIN=ROOT/f'areas/lk/rotinas/gmc-{RUN}.md'
APPROVAL='Lucas approved residual corrections 1-5 in Telegram; Kicks.dev allowed for missing GTINs'
DATA_SOURCE_ID='10636492695'

def now(): return datetime.now(timezone.utc).isoformat()
def load_abc(): spec=importlib.util.spec_from_file_location('abc',ABC); m=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(m); return m
def cents(v): return {'amountMicros':str(int(round(float(v)*1000000))),'currencyCode':'BRL'}
def norm_price(v):
    if v in (None,''): return None
    return f'{float(v):.2f}'
def pid_online(pid): return str(pid).startswith('online:')
def clean_sku(offer,title=''):
    s=re.sub(r'^LIA_','',offer or '')
    # remove final LK variant suffix only when style-code pattern remains
    m=re.match(r'([A-Z0-9]+-\d{3})(?:-\d+)?$',s)
    if m: return m.group(1)
    m=re.search(r'\b([A-Z]{1,3}\d{3,6}-\d{3})\b', title or '')
    return m.group(1) if m else s
def title_color(title):
    colors=['Preto','Branco','Azul','Vermelho','Verde','Cinza','Bege','Marrom','Rosa','Roxo','Laranja','Amarelo','Dourado','Prata','Colorido','Turquesa','Caramelo']
    for c in colors:
        if re.search(r'\b'+re.escape(c)+r'\b', title or '', re.I): return c
    return None
def extract_variant_id(link):
    qs=urllib.parse.parse_qs(urllib.parse.urlparse(link or '').query)
    return (qs.get('variant') or [None])[0]
def extract_handle(link):
    return urllib.parse.urlparse(link or '').path.rstrip('/').split('/')[-1]
def gql(abc,secrets,query,variables): return abc.shopify_graphql(secrets,query,variables)
def shopify_variant_by_legacy(abc,secrets,legacy):
    if not legacy: return None
    q='''query V($id:ID!){ productVariant(id:$id){ id legacyResourceId title sku barcode price compareAtPrice availableForSale image{url} product{id legacyResourceId title handle status onlineStoreUrl featuredImage{url} images(first:8){nodes{url}} tags productType vendor} } }'''
    gid='gid://shopify/ProductVariant/'+str(legacy)
    return (gql(abc,secrets,q,{'id':gid}).get('data') or {}).get('productVariant')
def shopify_product_by_handle(abc,secrets,handle):
    q='''query P($handle:String!){ productByHandle(handle:$handle){ id legacyResourceId title handle status onlineStoreUrl featuredImage{url} images(first:8){nodes{url}} tags productType vendor variants(first:50){nodes{id legacyResourceId title sku barcode price compareAtPrice availableForSale image{url}}} } }'''
    return (gql(abc,secrets,q,{'handle':handle}).get('data') or {}).get('productByHandle')
def request_kicks(sec,path,params):
    key=sec.get('KICKS_DEV_API_KEY') or sec.get('KICKS_API_KEY') or sec.get('KICKSDB_API_KEY')
    if not key: return {}
    url='https://api.kicks.dev'+path+'?'+urllib.parse.urlencode(params)
    import urllib.request as urlrequest
    req=urlrequest.Request(url,headers={'Authorization':'Bearer '+key})
    try:
        with urlrequest.urlopen(req,timeout=8) as r: return json.loads(r.read().decode())
    except Exception as e:
        return {'error':str(e)[:300]}
def select_image_from_shopify(p,v):
    imgs=[]
    if v and (v.get('image') or {}).get('url'): imgs.append(v['image']['url'])
    if p and (p.get('featuredImage') or {}).get('url'): imgs.append(p['featuredImage']['url'])
    if p:
        imgs += [n.get('url') for n in ((p.get('images') or {}).get('nodes') or []) if n.get('url')]
    # avoid 1x1/no image not possible here; prefer first non-empty Shopify image
    seen=[]
    for u in imgs:
        if u and u not in seen: seen.append(u)
    return seen

def main():
    abc=load_abc(); sec=abc.load_doppler(); mid=sec['MERCHANT_CENTER_ID_LK']; token=abc.google_access_token(abc.parse_service_account(sec))
    data=json.loads(TRIAGE.read_text()); rows=data['rows']
    PRIVATE.mkdir(parents=True,exist_ok=True); os.chmod(PRIVATE,0o700)
    rollback=PRIVATE/f'lk-gmc-{RUN}-rollback-{datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")}.json'
    snap=[]; actions=[]; execs=[]
    def add_action(r,attrs,kind,evidence):
        if not attrs: return
        pid=r['product_id']
        try: cur=abc.content_product_get(mid,token,pid)
        except Exception as e: cur={'get_error':str(e)[:500]}
        snap.append({'product_id':pid,'kind':kind,'current_content_api_product_resource':cur,'planned_attrs':attrs,'evidence':evidence})
        actions.append({'product_id':pid,'kind':kind,'attrs':attrs,'evidence':evidence})
    # price + sale price: only online exact Shopify variant evidence
    price_rows=[r for r in rows if pid_online(r['product_id']) and {'price_updated','strikethrough_price_updated'} & {i['code'] for i in r['issues']}]
    for r in price_rows:
        vid=extract_variant_id(r.get('link')) or r.get('offerId') if str(r.get('offerId','')).isdigit() else extract_variant_id(r.get('link'))
        v=shopify_variant_by_legacy(abc,sec,vid) if vid else None
        if not v: continue
        price=norm_price(v.get('compareAtPrice') or v.get('price')); sale=norm_price(v.get('price')) if v.get('compareAtPrice') and float(v.get('compareAtPrice'))>float(v.get('price')) else None
        attrs={}
        curp=(r.get('price') or {}).get('value'); curs=(r.get('salePrice') or {}).get('value')
        if price and norm_price(curp)!=price: attrs['price']=cents(price)
        if sale and norm_price(curs)!=sale: attrs['salePrice']=cents(sale)
        # if issue is strikethrough and current sale already exists but micros may still be stale, repatch both exact values
        if sale and not attrs and 'strikethrough_price_updated' in {i['code'] for i in r['issues']}: attrs={'price':cents(price),'salePrice':cents(sale)}
        add_action(r,attrs,'price_saleprice_shopify_variant',{'shopify_variant_legacy':vid,'sku':v.get('sku'),'shopify_price':v.get('price'),'shopify_compareAtPrice':v.get('compareAtPrice')})
        time.sleep(.08)
    # missing attrs high confidence
    for r in rows:
        codes={i['code'] for i in r['issues']}
        if 'missing_item_attribute_for_product_type' not in codes or not pid_online(r['product_id']): continue
        vid=extract_variant_id(r.get('link')) or (r.get('offerId') if str(r.get('offerId','')).isdigit() else None)
        v=shopify_variant_by_legacy(abc,sec,vid) if vid else None
        p=v.get('product') if v else shopify_product_by_handle(abc,sec,extract_handle(r.get('link')))
        text=' '.join([r.get('title') or '', (p or {}).get('title') or '', (v or {}).get('title') or '', ' '.join((p or {}).get('tags') or [])])
        attrs={}
        missing={i.get('attributeName') or '' for i in r['issues'] if i['code']=='missing_item_attribute_for_product_type'}
        if any('color' in x.lower() for x in missing) and not r.get('color'):
            c=title_color(text); 
            if c: attrs['color']=c
        if any('age' in x.lower() for x in missing) and not r.get('ageGroup'): attrs['ageGroup']='adult'
        if any('gender' in x.lower() for x in missing) and not r.get('gender'):
            tl=text.lower(); attrs['gender']='female' if any(w in tl for w in ['women','femin','womens']) else ('male' if any(w in tl for w in ['men\'s','mascul','mens']) else 'unisex')
        if any('size' in x.lower() for x in missing) and not r.get('sizes'):
            vt=(v or {}).get('title') or ''
            m=re.search(r'(?:tamanho\s*)?(\d{2}|PP|P|M|G|GG|XG|XL|XXL|XS|S|L)\b', vt+' '+(r.get('title') or ''), re.I)
            if m: attrs['sizes']=[m.group(1).upper()]
        add_action(r,attrs,'missing_attribute_completion',{'shopify_variant_legacy':vid,'shopify_variant_title':(v or {}).get('title'),'shopify_product_title':(p or {}).get('title')})
        time.sleep(.08)
    # image issues: replace broken/single-color imageLink from Shopify exact product/variant if available, fallback Kicks product image by SKU
    for r in rows:
        codes={i['code'] for i in r['issues']}
        if not ({'image_link_broken','image_single_color'} & codes): continue
        vid=extract_variant_id(r.get('link'))
        v=shopify_variant_by_legacy(abc,sec,vid) if vid else None; p=(v or {}).get('product') if v else shopify_product_by_handle(abc,sec,extract_handle(r.get('link')))
        imgs=select_image_from_shopify(p,v); ev={'source':'shopify','variant':vid,'image_count':len(imgs)}
        if not imgs:
            sku=clean_sku(r.get('offerId'),r.get('title'))
            kd=request_kicks(sec,'/v3/stockx/products',{'query':sku,'limit':1})
            first=(kd.get('data') or [{}])[0]
            imgs=[first.get('image')] if first.get('image') else []
            ev={'source':'kicks.dev/stockx','sku':sku,'product':first.get('title')}
        attrs={}
        if imgs: attrs={'imageLink':imgs[0]}
        if len(imgs)>1: attrs['additionalImageLinks']=imgs[1:10]
        add_action(r,attrs,'image_link_repair',ev)
        time.sleep(.08)
    # landing page errors: delete exact Merchant product if Shopify handle absent/draft/archived; leave active online rows to recrawl naturally
    for r in rows:
        codes={i['code'] for i in r['issues']}
        if 'landing_page_error' not in codes: continue
        p=shopify_product_by_handle(abc,sec,extract_handle(r.get('link')))
        status=(p or {}).get('status')
        if (not p) or status in {'DRAFT','ARCHIVED'}:
            try: cur=abc.content_product_get(mid,token,r['product_id'])
            except Exception as e: cur={'get_error':str(e)[:500]}
            snap.append({'product_id':r['product_id'],'kind':'landing_page_stale_delete','current_content_api_product_resource':cur,'evidence':{'shopify_handle_state':'not_found' if not p else status,'handle':extract_handle(r.get('link'))}})
            actions.append({'product_id':r['product_id'],'kind':'landing_page_stale_delete','attrs':{},'evidence':{'shopify_handle_state':'not_found' if not p else status}})
        time.sleep(.08)
    # GTIN: only high confidence exact Kicks match by sku + current/product title + Shopify/LK size direct string, no BR-US conversion
    for r in rows:
        codes={i['code'] for i in r['issues']}
        if not ({'restricted_gtin','reserved_gtin'} & codes): continue
        offer=r.get('offerId') or ''; sku=clean_sku(offer,r.get('title'))
        if not re.search(r'[A-Z].*\d',sku): continue
        kd=request_kicks(sec,'/v3/unified/gtin',{'sku':sku,'limit':100,'source':'stockx'})
        vals=kd.get('data') or []
        # direct size from Merchant title; no conversion to avoid wrong GTINs
        mt=re.search(r'Tamanho\s+([0-9]+(?:\.[05])?|[A-Z]{1,3})\b',r.get('title') or '',re.I)
        size=mt.group(1) if mt else None
        matches=[x for x in vals if size and str(x.get('size')).lower()==str(size).lower()]
        if len(matches)==1 and matches[0].get('identifier') and matches[0].get('identifier')!=r.get('gtin'):
            add_action(r,{'gtin':matches[0]['identifier']},'gtin_kicks_exact_size',{'kicks_sku':sku,'kicks_size':matches[0].get('size'),'source':'kicks.dev unified gtin','name':matches[0].get('name')})
        time.sleep(.25)
    rollback.write_text(json.dumps({'generated_at':now(),'approval':APPROVAL,'dataSource':DATA_SOURCE_ID,'records':snap},ensure_ascii=False,indent=2)+'\n'); os.chmod(rollback,0o600)
    progress=PRIVATE/f'lk-gmc-{RUN}-progress-{rollback.stem.rsplit("-",1)[-1]}.jsonl'; os.chmod(progress.parent,0o700)
    with progress.open('w',encoding='utf-8') as f:
        os.chmod(progress,0o600)
        for a in actions:
            pid=a['product_id']
            try:
                if a['kind']=='landing_page_stale_delete':
                    url=f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/products/{urllib.parse.quote(pid,safe="")}'
                    abc.request_json(url,token=token,method='DELETE'); res={'product_id':pid,'kind':a['kind'],'status':'deleted_or_absent'}
                else:
                    abc.patch_product_input_attrs(mid,token,pid,a['attrs']); res={'product_id':pid,'kind':a['kind'],'status':'patched','attrs':a['attrs']}
            except Exception as e:
                res={'product_id':pid,'kind':a['kind'],'status':'error','error':str(e)[:1200],'attrs':a.get('attrs')}
            execs.append(res); f.write(json.dumps(res,ensure_ascii=False)+'\n'); f.flush(); time.sleep(.28)
    time.sleep(45)
    verify=[]
    for a in actions:
        pid=a['product_id']
        try:
            if a['kind']=='landing_page_stale_delete':
                try: abc.content_product_get(mid,token,pid); verify.append({'product_id':pid,'kind':a['kind'],'verify':'still_present'})
                except Exception as e: verify.append({'product_id':pid,'kind':a['kind'],'verify':'absent_or_get_failed','detail':str(e)[:200]})
            else:
                cur=abc.content_product_get(mid,token,pid); actual={k:cur.get(k) for k in a['attrs']}
                verify.append({'product_id':pid,'kind':a['kind'],'verify':'read','expected':a['attrs'],'actual':actual})
        except Exception as e: verify.append({'product_id':pid,'kind':a['kind'],'verify':'error','error':str(e)[:500]})
        time.sleep(.06)
    # fresh target status counts after settle (may still lag)
    time.sleep(120)
    fresh={}
    try:
        import importlib.util
        aud_path=ROOT/'scripts/lk_gmc_catalog_duplication_audit_20260512.py'; spec=importlib.util.spec_from_file_location('aud',aud_path); aud=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(aud)
        stats=aud.list_all('productstatuses',mid,token); cnt=Counter()
        acted={a['product_id'] for a in actions}
        cntacted=Counter()
        for st in stats:
            for iss in st.get('itemLevelIssues') or []:
                code=str(iss.get('code') or iss.get('servability') or iss.get('attributeName'))
                if code in {'price_updated','strikethrough_price_updated','missing_item_attribute_for_product_type','restricted_gtin','reserved_gtin','landing_page_error','image_single_color','image_link_broken','landing_page_pending_crawl'}:
                    cnt[code]+=1
                    if st.get('productId') in acted: cntacted[code]+=1
        fresh={'target_issue_instances_after':dict(cnt),'target_issue_instances_after_on_acted_ids':dict(cntacted),'productstatuses_read':len(stats)}
    except Exception as e: fresh={'status_recheck_error':str(e)[:800]}
    payload={'generated_at':now(),'approval':APPROVAL,'status':'completed_with_errors' if any(x['status']=='error' for x in execs) else 'completed','summary':{'planned_actions':len(actions),'planned_by_kind':dict(Counter(a['kind'] for a in actions)),'execution':dict(Counter(e['status'] for e in execs)),'verify':dict(Counter(v.get('verify') for v in verify)),**fresh},'rollback_snapshot_path':str(rollback),'progress_path':str(progress),'actions':actions,'execution_results':execs,'verify_results':verify,'not_performed':['Shopify write','Tiny write','campaign/message/send','feed fetch/upload','price policy invention; prices copied only from exact Shopify variant']}
    OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    lines=['# LK GMC residual approved executor — 2026-05-14','',f"Status: `{payload['status']}`",'', '## Summary']
    for k,v in payload['summary'].items(): lines.append(f'- {k}: `{v}`')
    lines += ['', '## Snapshots', f'- Rollback privado: `{rollback}`', f'- Progress privado: `{progress}`', '', '## Não executado']+[f'- {x}' for x in payload['not_performed']]
    MD.write_text('\n'.join(lines)+'\n'); BRAIN.parent.mkdir(parents=True,exist_ok=True); BRAIN.write_text(MD.read_text())
    print(json.dumps({'status':payload['status'],'summary':payload['summary'],'out':str(OUT),'md':str(MD),'rollback':str(rollback)},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
