#!/usr/bin/env python3
import json, pathlib, urllib.request, urllib.parse, base64, time, re, unicodedata
from datetime import datetime
from collections import Counter

ROOT=pathlib.Path(__file__).resolve().parents[1]
prev=json.loads((ROOT/'reports/lk-p0-residual-live-lookup-enriched-2026-05-11.json').read_text())
done_ids={'1069544054','1069544710'}
remaining=[]
for r in prev['results']:
    ids={str(m.get('id')) for m in (r.get('tiny_size_matches') or [])}
    if ids & done_ids:
        continue
    remaining.append(r)

req=urllib.request.Request('https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json')
dt=pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token').read_text().strip()
req.add_header('Authorization','Basic '+base64.b64encode((dt+':').encode()).decode())
with urllib.request.urlopen(req, timeout=60) as resp:
    secrets=json.load(resp)
tiny_token=secrets['TINY_API_TOKEN']
shop_token=secrets['SHOPIFY_ACCESS_TOKEN']
store=secrets.get('SHOPIFY_STORE_URL') or secrets.get('SHOPIFY_STORE') or secrets.get('SHOPIFY_SHOP_NAME') or secrets.get('SHOPIFY_STORE_HANDLE')
store=store.replace('https://','').replace('http://','').strip('/')
if not store.endswith('.myshopify.com'):
    store += '.myshopify.com'

def tiny_call(method, params):
    data=urllib.parse.urlencode({**params,'token':tiny_token,'formato':'json'}).encode()
    req=urllib.request.Request(f'https://api.tiny.com.br/api2/{method}.php', data=data, method='POST')
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.load(r)

def shop_get(path):
    req=urllib.request.Request(f'https://{store}/admin/api/2024-01/{path}')
    req.add_header('X-Shopify-Access-Token', shop_token)
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.load(r)

def norm(s):
    s=str(s or '').lower()
    s=unicodedata.normalize('NFKD', s).encode('ascii','ignore').decode()
    s=s.replace('½','.5')
    s=re.sub(r'[^a-z0-9.]+','',s)
    return s

def size_alts(size):
    s=str(size or '')
    vals={s, s.replace('/','-'), s.replace('-','/'), s.replace('S/P','P/S'), s.replace('P/S','S/P'), s.replace('L/G','G/L'), s.replace('G/L','L/G'), s.replace('G-L','G/L'), s.replace('P-S','P/S'), s.replace('42.5','425')}
    return {norm(x) for x in vals if x}

def extract_size(v):
    if isinstance(v.get('grade'), dict) and v.get('grade'):
        return ' '.join(str(x) for x in v['grade'].values())
    name=v.get('nome') or ''
    if ' - ' in str(name):
        return str(name).split(' - ')[-1]
    return ''

def detail_candidates(cands, target_size):
    out=[]; seen=set(); alts=size_alts(target_size)
    for c in cands[:15]:
        cid=str(c.get('id'))
        if cid in seen:
            continue
        seen.add(cid)
        time.sleep(1.25)
        try:
            ret=tiny_call('produto.obter', {'id':cid}).get('retorno',{})
        except Exception as e:
            out.append({'id':cid,'error':str(e)[:120]})
            continue
        prod=ret.get('produto') or {}
        vars=[]
        if prod:
            vars.append({'id':str(prod.get('id')), 'codigo':prod.get('codigo') or '', 'nome':prod.get('nome') or '', 'grade':prod.get('grade') or {}, 'source':'produto'})
            for w in prod.get('variacoes') or []:
                vv=w.get('variacao') or {}
                vars.append({'id':str(vv.get('id')), 'codigo':vv.get('codigo') or '', 'nome':vv.get('nome') or vv.get('grade') or '', 'grade':vv.get('grade') or {}, 'source':'variacao', 'parent_id':str(prod.get('id'))})
        matches=[]
        for v in vars:
            sz=extract_size(v)
            # Exact normalized grade/size match only. Avoid substring false positives:
            # S/P must not match XS/PP; L/G must not match XL/GG.
            if norm(sz) in alts:
                matches.append({**v, 'matched_size_text': sz})
        out.append({'id':cid,'status':ret.get('status'), 'nome':prod.get('nome'), 'codigo':prod.get('codigo') or '', 'tipoVariacao':prod.get('tipoVariacao'), 'matches':matches})
    return out

def tiny_searches(title, sku):
    qs=[]
    if sku:
        qs.append(sku)
    qs.append(title)
    parts=title.split()
    if len(parts)>4:
        qs.append(' '.join(parts[:5]))
    out=[]; seen_ids=set(); flat=[]
    for q in qs:
        time.sleep(1.25)
        try:
            ret=tiny_call('produtos.pesquisa', {'pesquisa':q}).get('retorno',{})
        except Exception as e:
            out.append({'query':q,'error':str(e)[:160]})
            continue
        c=[]
        for item in ret.get('produtos') or []:
            p=item.get('produto') or {}
            rec={'id':str(p.get('id')), 'codigo':p.get('codigo') or '', 'nome':p.get('nome') or '', 'preco':p.get('preco'), 'situacao':p.get('situacao')}
            c.append(rec)
            if rec['id'] and rec['id'] not in seen_ids:
                seen_ids.add(rec['id']); flat.append(rec)
        out.append({'query':q,'status':ret.get('status'),'error':ret.get('erros') or ret.get('erro'),'candidates':c[:10]})
    return out, flat

results=[]
for r in remaining:
    vid=str(r['variant_id']); pid=str(r['product_id']); title=r['product_title']; size=r['variant_title_live']; sku=r.get('shopify_sku_live') or ''
    try:
        prod=shop_get(f'products/{pid}.json').get('product',{})
        variants=[{'id':str(v['id']),'title':v.get('title'), 'sku':v.get('sku') or '', 'option1':v.get('option1'), 'option2':v.get('option2')} for v in prod.get('variants',[])]
    except Exception as e:
        variants=[]
    searches, flat=tiny_searches(title, sku)
    existing={x['id'] for x in flat}
    for c in r.get('tiny_top_candidates') or []:
        rec={'id':str(c.get('id')), 'codigo':c.get('codigo') or '', 'nome':c.get('nome') or '', 'preco':c.get('preco'), 'situacao':c.get('situacao')}
        if rec['id'] and rec['id'] not in existing:
            flat.append(rec); existing.add(rec['id'])
    details=detail_candidates(flat, size)
    all_matches=[]
    for d in details:
        for m in d.get('matches') or []:
            all_matches.append(m)
    ded=[]; seen=set()
    for m in all_matches:
        if m['id'] not in seen:
            seen.add(m['id']); ded.append(m)
    blank_matches=[m for m in ded if not m.get('codigo')]
    coded_matches=[m for m in ded if m.get('codigo')]
    live_variant=next((v for v in variants if v['id']==vid), {})
    sibling_skus=[v for v in variants if v.get('sku')]
    if sku and len(blank_matches)==1:
        eligibility='tiny_codigo_write_preview_candidate_from_shopify_sku'
        target=sku; target_tiny_id=blank_matches[0]['id']; confidence='media_alta'
    elif not sku and len(blank_matches)==1:
        eligibility='needs_human_code_decision_shopify_sku_blank_unique_tiny_match'
        target=None; target_tiny_id=blank_matches[0]['id']; confidence='baixa'
    elif sku and len(blank_matches)>1:
        eligibility='ambiguous_tiny_matches_with_shopify_sku'
        target=sku; target_tiny_id=None; confidence='baixa'
    else:
        eligibility='needs_manual_tiny_mapping_or_cadastro'
        target=None; target_tiny_id=None; confidence='baixa'
    results.append({
        'product_title':title,'shopify_product_id':pid,'shopify_variant_id':vid,'size':size,
        'shopify_sku_live':sku, 'shopify_live_variant':live_variant,
        'shopify_sibling_skus':sibling_skus,
        'orders_30d_signal':r.get('orders_30d_signal'), 'revenue_signal':r.get('revenue_signal'),
        'tiny_searches':searches, 'tiny_detailed_matches':ded, 'tiny_coded_matches':coded_matches,
        'eligibility':eligibility, 'target_tiny_id':target_tiny_id, 'target_codigo':target, 'confidence':confidence,
    })

summary={
 'generated_at':datetime.now().isoformat(timespec='seconds'),
 'scope':'Read-only follow-up for 13 remaining P0 after 2 Tiny codigo writes',
 'guardrails':['read-only Shopify GET','read-only Tiny produtos.pesquisa/produto.obter','no Shopify write','no Tiny write','no sourcing'],
 'count':len(results),
 'summary':dict(Counter(x['eligibility'] for x in results)),
 'results':results,
}
out=ROOT/'reports/lk-p0-remaining-followup-readonly-2026-05-11.json'
out.write_text(json.dumps(summary, ensure_ascii=False, indent=2)+"\n")
print(json.dumps({'report':str(out),'count':len(results),'summary':summary['summary'], 'brief':[{k:x.get(k) for k in ['product_title','size','shopify_sku_live','eligibility','target_tiny_id','target_codigo']} for x in results]}, ensure_ascii=False, indent=2))
