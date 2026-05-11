#!/usr/bin/env python3
import base64,json,pathlib,time,urllib.parse,urllib.request,unicodedata,re
from datetime import datetime, timezone
ROOT=pathlib.Path(__file__).resolve().parents[1]
PREVIEW=ROOT/'reports/lk-p0-remaining-tiny-code-preview-2026-05-11.json'
FOLLOWUP=ROOT/'reports/lk-p0-remaining-followup-readonly-2026-05-11.json'
OUT=ROOT/'reports/lk-p0-blocked-six-live-recheck-2026-05-11.json'

dt=pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token').read_text().strip()
req=urllib.request.Request('https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json')
req.add_header('Authorization','Basic '+base64.b64encode((dt+':').encode()).decode())
with urllib.request.urlopen(req,timeout=60) as resp: secrets=json.load(resp)
TINY=secrets['TINY_API_TOKEN']; SHOP=secrets['SHOPIFY_ACCESS_TOKEN']
store=secrets.get('SHOPIFY_STORE_URL') or secrets.get('SHOPIFY_STORE') or secrets.get('SHOPIFY_SHOP_NAME') or secrets.get('SHOPIFY_STORE_HANDLE')
store=store.replace('https://','').replace('http://','').strip('/')
if not store.endswith('.myshopify.com'): store+='.myshopify.com'

def tiny_call(method, params):
    time.sleep(4.0)
    data=urllib.parse.urlencode({**params,'token':TINY,'formato':'json'}).encode()
    req=urllib.request.Request(f'https://api.tiny.com.br/api2/{method}.php',data=data,method='POST')
    with urllib.request.urlopen(req,timeout=90) as r: return json.load(r)
def shop_get(path):
    req=urllib.request.Request(f'https://{store}/admin/api/2024-01/{path}')
    req.add_header('X-Shopify-Access-Token',SHOP)
    with urllib.request.urlopen(req,timeout=90) as r: return json.load(r)
def norm(s):
    s=str(s or '').lower(); s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode(); s=s.replace('½','.5')
    return re.sub(r'[^a-z0-9.]+','',s)
def size_alts(size):
    s=str(size or '')
    vals={s,s.replace('/','-'),s.replace('-','/'),s.replace('S/P','P/S'),s.replace('P/S','S/P'),s.replace('L/G','G/L'),s.replace('G/L','L/G'),s.replace('G-L','G/L'),s.replace('P-S','P/S')}
    return {norm(x) for x in vals if x}
def extract_size(v):
    if isinstance(v.get('grade'),dict) and v.get('grade'):
        return ' '.join(str(x) for x in v['grade'].values())
    nm=v.get('nome') or ''
    if isinstance(nm,dict): return ' '.join(str(x) for x in nm.values())
    if ' - ' in str(nm): return str(nm).split(' - ')[-1]
    return ''
def compact_product(p):
    return {k:p.get(k) for k in ['id','nome','codigo','preco','preco_promocional','unidade','origem','situacao','tipo','grade','idProdutoPai'] if k in p}
def product_details_for_candidate(cid, target_size):
    ret=tiny_call('produto.obter', {'id':cid}).get('retorno',{})
    p=ret.get('produto') or {}
    records=[]
    if p:
        records.append({'source':'produto', **compact_product(p)})
        for w in p.get('variacoes') or []:
            v=w.get('variacao') or {}
            records.append({'source':'variacao','parent_id':str(p.get('id')), **compact_product(v)})
    alts=size_alts(target_size)
    matches=[]
    for rec in records:
        sz=extract_size(rec)
        if norm(sz) in alts:
            matches.append({**rec,'matched_size_text':sz})
    return {'candidate_id':str(cid),'status':ret.get('status'),'product':compact_product(p),'size_matches':matches}
def tiny_search(title, sku):
    queries=[]
    if sku: queries.append(sku)
    queries += [title, ' '.join(title.split()[:5])]
    seen=set(); candidates=[]; searches=[]
    for q in dict.fromkeys([x for x in queries if x]):
        ret=tiny_call('produtos.pesquisa', {'pesquisa':q}).get('retorno',{})
        cs=[]
        for item in ret.get('produtos') or []:
            p=item.get('produto') or {}; rec={k:p.get(k) for k in ['id','codigo','nome','preco','situacao']}
            if rec.get('id') and str(rec['id']) not in seen:
                seen.add(str(rec['id'])); candidates.append(rec)
            cs.append(rec)
        searches.append({'query':q,'status':ret.get('status'),'count':len(cs),'candidates':cs[:10]})
    return searches,candidates
preview=json.loads(PREVIEW.read_text())
followup=json.loads(FOLLOWUP.read_text())
follow_by_variant={str(r.get('shopify_variant_id')):r for r in followup.get('results',[])}
rows=[]
for b in preview['blocked']:
    f=follow_by_variant.get(str(b['shopify_variant_id']),{})
    pid=b.get('shopify_product_id') or f.get('shopify_product_id')
    vid=str(b['shopify_variant_id']); title=b['product_title']; size=b['size']
    prod=shop_get(f'products/{pid}.json').get('product',{})
    variant=next((v for v in prod.get('variants',[]) if str(v.get('id'))==vid),{})
    variants=[{'id':str(v.get('id')),'title':v.get('title'),'sku':v.get('sku') or '','option1':v.get('option1'),'option2':v.get('option2'),'price':v.get('price')} for v in prod.get('variants',[])]
    live_sku=variant.get('sku') or ''
    searches,cands=tiny_search(title, live_sku)
    details=[product_details_for_candidate(c['id'], size) for c in cands[:14] if c.get('id')]
    matches=[]
    for d in details:
        for m in d.get('size_matches') or []:
            if str(m.get('id')) not in {str(x.get('id')) for x in matches}:
                matches.append(m)
    coded=[m for m in matches if m.get('codigo')]
    blank=[m for m in matches if not m.get('codigo')]
    if live_sku and len(blank)==1 and not coded:
        classification='tiny_write_candidate_if_lucas_accepts_target_from_shopify_sku'
        next_action='Preview de preencher codigo Tiny no único match usando SKU Shopify live.'
    elif live_sku and len(blank)>1:
        classification='ambiguous_tiny_duplicate_with_shopify_sku'
        next_action='Decidir qual Tiny ID duplicado representa a variação real antes de preencher codigo; não escrever automático.'
    elif not live_sku and matches:
        classification='needs_canonical_code_decision_shopify_and_tiny_blank'
        next_action='Definir código canônico e escolher Tiny ID correto; depois preparar preview Tiny/Shopify SKU.'
    else:
        classification='needs_cadastro_or_manual_search_no_tiny_size_match'
        next_action='Cadastro/mapeamento manual no Tiny; Shopify SKU também precisa definição se vazio.'
    rows.append({'product_title':title,'shopify_product_id':pid,'shopify_handle':prod.get('handle'),'shopify_variant_id':vid,'size':size,'shopify_sku_live':live_sku,'shopify_variants':variants,'orders_30d_signal':b.get('orders_30d_signal'),'revenue_signal':b.get('revenue_signal'),'tiny_searches':searches,'tiny_size_matches':matches,'tiny_coded_matches':coded,'classification':classification,'next_action':next_action})
report={'generated_at':datetime.now(timezone.utc).isoformat(),'scope':'Read-only live recheck of six remaining blocked LK P0 residual variants after 7 Tiny codigo writes','guardrails':['Shopify GET only','Tiny pesquisa/obter only','no Shopify write','no Tiny write','no price/stock/product/sourcing'], 'summary':{}, 'results':rows}
from collections import Counter
report['summary']=dict(Counter(r['classification'] for r in rows))
OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'report':str(OUT),'summary':report['summary'],'brief':[{'title':r['product_title'],'size':r['size'],'sku':r['shopify_sku_live'],'classification':r['classification'],'tiny_matches':[(m.get('id'),m.get('codigo'),m.get('parent_id'),m.get('matched_size_text')) for m in r['tiny_size_matches']]} for r in rows]},ensure_ascii=False,indent=2))
