#!/usr/bin/env python3
from __future__ import annotations
import base64, json, os, pathlib, re, time, urllib.error, urllib.parse, urllib.request
from datetime import datetime, timezone
from typing import Any

ROOT=pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
DOPPLER_TOKEN_FILE=pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
PAYLOAD=ROOT/'reports/lk-compras-unified-sourcing-payload-2026-05-14.json'
NOTION_EXEC=ROOT/'reports/lk-compras-unified-sourcing-notion-execution-2026-05-14.json'
OUT_JSON=ROOT/'reports/lk-sourcing-ops-v2-markup2-exact-size-2026-05-15.json'
OUT_MD=ROOT/'reports/lk-sourcing-ops-v2-markup2-exact-size-2026-05-15.md'
MC_MD=ROOT/'areas/lk/rotinas/mission-control-sourcing-ops-v2-markup2-exact-size-2026-05-15.md'
JULIO_MD=ROOT/'reports/lk-sourcing-julio-instructions-2026-05-15.md'
NOTION_DB='2b127dc9-e033-805b-81b6-f62f5467ce77'
NOTION_VERSION='2022-06-28'
USD_BRL=4.911381
FX_BUFFER=1.05
DEFAULT_CUSTO_TRAZER_USD=100.0
MARKUP=2.0
RUN_MARKER='LK OS sourcing ops v2 — markup2 exact-size guard — 2026-05-15'
RUN_MARKER_V2B='LK OS sourcing ops v2b — Hermes validates exact-size price; Júlio does not fill values — 2026-05-15'


def now(): return datetime.now(timezone.utc).isoformat()

def load_doppler():
    token=os.environ.get('DOPPLER_TOKEN') or DOPPLER_TOKEN_FILE.read_text().strip()
    req=urllib.request.Request('https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json')
    req.add_header('Authorization','Basic '+base64.b64encode((token+':').encode()).decode())
    with urllib.request.urlopen(req,timeout=60) as r: return json.loads(r.read().decode())

def http_json(url, headers, method='GET', payload=None, attempts=4):
    data=None if payload is None else json.dumps(payload,ensure_ascii=False).encode()
    for i in range(attempts):
        req=urllib.request.Request(url,data=data,method=method)
        for k,v in headers.items(): req.add_header(k,v)
        if data is not None: req.add_header('Content-Type','application/json; charset=utf-8')
        try:
            with urllib.request.urlopen(req,timeout=90) as r:
                raw=r.read().decode(); return json.loads(raw) if raw else {}
        except urllib.error.HTTPError as e:
            body=e.read().decode(errors='replace')
            if e.code not in {429,500,502,503,504} or i==attempts-1:
                return {'error':f'http_{e.code}','body':body[:1000]}
        except Exception as e:
            if i==attempts-1: return {'error':type(e).__name__,'body':str(e)[:1000]}
        time.sleep(min(20,2**(i+1)))
    return {'error':'request_failed'}

def nh(tok): return {'Authorization':'Bearer '+tok,'Notion-Version':NOTION_VERSION}
def kh(key): return {'Authorization':'Bearer '+key}

def parse_brl(text):
    if not text: return None
    m=re.search(r'R\$\s*([0-9\.]+,[0-9]{2})',text)
    return float(m.group(1).replace('.','').replace(',','.')) if m else None

def brl(v):
    if v is None: return 'n/d'
    return f'R$ {v:,.2f}'.replace(',','X').replace('.',',').replace('X','.')

def usd(v): return 'n/d' if v is None else f'US$ {float(v):,.2f}'

def pct(v): return 'n/d' if v is None else f'{v*100:.1f}%'

def style_sku(sku):
    s=(sku or '').strip().upper()
    if re.search(r'[A-Z]',s): s=re.sub(r'-\d+$','',s)
    return s.replace(' ','-')

def norm_sku(s): return re.sub(r'[^A-Z0-9]','',(s or '').upper())

def kicks_search(key,path,query):
    url='https://api.kicks.dev'+path+'?'+urllib.parse.urlencode({'query':query,'limit':5})
    d=http_json(url,kh(key))
    if d.get('error'): return {'error':d.get('error'),'body':d.get('body')}
    rows=d.get('data') or []
    exact=[x for x in rows if norm_sku(x.get('sku'))==norm_sku(query)]
    return (exact or rows or [None])[0]

def stockx_product(key,style): return kicks_search(key,'/v3/stockx/products',style)
def goat_product(key,style):
    for q in [style,style.replace('-',' '),style.replace('-','')]:
        p=kicks_search(key,'/v3/goat/products',q)
        if p and not p.get('error') and norm_sku(p.get('sku'))==norm_sku(style): return p
    return p if p else None

def landed_cost_exact(price_usd,custo_trazer_usd=DEFAULT_CUSTO_TRAZER_USD):
    # Correct Lucas rule: this is COST only. No markup applied here.
    return (float(price_usd)+float(custo_trazer_usd))*(USD_BRL*FX_BUFFER)

def ideal_sale_from_cost(cost_brl): return float(cost_brl)*MARKUP

def paragraph(text): return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':text[:1900]}}]}}
def heading(text): return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':text[:1900]}}]}}
def image_block(url,caption): return {'object':'block','type':'image','image':{'type':'external','external':{'url':url},'caption':[{'type':'text','text':{'content':caption[:1900]}}]}}

def ensure_db_props(tok):
    payload={'properties':{
        'Foto Produto': {'url': {}},
        'Preço exato tam USD': {'number': {'format':'dollar'}},
        'Custo trazer USD': {'number': {'format':'dollar'}},
        'Custo landed BRL': {'number': {'format':'real'}},
        'Venda ideal BRL': {'number': {'format':'real'}},
        'Margem venda atual %': {'number': {'format':'percent'}},
        'Fonte preço tam': {'rich_text': {}},
        'Decisão Sourcing': {'select': {'options':[
            {'name':'Precisa validar tamanho','color':'yellow'},
            {'name':'Hermes validar preço/tamanho','color':'orange'},
            {'name':'Comprar nacional','color':'green'},
            {'name':'Importar','color':'blue'},
            {'name':'Pular','color':'red'},
            {'name':'Watchlist','color':'gray'}
        ]}}
    }}
    return http_json(f'https://api.notion.com/v1/databases/{NOTION_DB}',nh(tok),method='PATCH',payload=payload)

def patch_page(tok,page_id,props):
    return http_json(f'https://api.notion.com/v1/pages/{page_id}',nh(tok),method='PATCH',payload={'properties':props})

def append_blocks(tok,page_id,blocks):
    return http_json(f'https://api.notion.com/v1/blocks/{page_id}/children',nh(tok),method='PATCH',payload={'children':blocks})

def existing_marker(tok,page_id):
    d=http_json(f'https://api.notion.com/v1/blocks/{page_id}/children?page_size=100',nh(tok))
    for b in d.get('results',[]) if isinstance(d,dict) else []:
        typ=b.get('type')
        if typ and typ in b:
            rich=b[typ].get('rich_text') or b[typ].get('caption') or []
            text=''.join(x.get('plain_text') or (x.get('text') or {}).get('content') or '' for x in rich)
            if RUN_MARKER in text: return True
    return False


def main():
    sec=load_doppler(); tok=sec.get('NOTION_TOKEN_LK') or sec.get('NOTION_API_KEY'); kicks=sec.get('KICKS_DEV_API_KEY') or sec.get('KICKS_API_KEY') or sec.get('KICKSDB_API_KEY')
    if not tok: raise SystemExit('missing notion token')
    if not kicks: raise SystemExit('missing kicks key')
    db_patch=ensure_db_props(tok)
    cards=json.loads(PAYLOAD.read_text())['cards']
    exec_rows={r['title']:r for r in json.loads(NOTION_EXEC.read_text())['results']}
    cache={}; rows=[]; pages_updated=0; blocks_appended=0
    for card in cards:
        title=card['Nome']; page_id=(exec_rows.get(title) or {}).get('page_id'); style=style_sku(card.get('SKU'))
        if style not in cache:
            sx=stockx_product(kicks,style); time.sleep(.25)
            goat=goat_product(kicks,style); time.sleep(.25)
            cache[style]={'sx':sx,'goat':goat}
        sx=cache[style]['sx']; goat=cache[style]['goat']
        img=None
        if isinstance(sx,dict): img=sx.get('image') or (sx.get('gallery') or [None])[0]
        if not img and isinstance(goat,dict): img=goat.get('image_url') or (goat.get('images') or [None])[0]
        sale=parse_brl(card.get('Preço médio vendido'))
        nat=parse_brl(card.get('Opção nacional/Droper'))
        nat_margin=(sale-nat)/sale if sale and nat is not None else None
        product_signal_min=sx.get('min_price') if isinstance(sx,dict) and isinstance(sx.get('min_price'),(int,float)) else None
        # Never convert product-level market signal into cost/margin for this size.
        exact_price_usd=None
        exact_landed_brl=None
        ideal_sale_brl=None
        margin_current=None
        decision='Hermes validar preço/tamanho'
        source_price='PENDENTE — Hermes precisa buscar/validar preço exato do tamanho correto em fonte confiável/autenticada. Júlio não preenche valor. KicksDev product-level é só sinal/foto, não custo.'
        if nat_margin is not None and nat_margin >= .30:
            decision='Comprar nacional'
            source_price='Custo nacional/Droper do match existente parece viável; ainda confirmar disponibilidade e tamanho antes da compra.'
        props={'Fonte preço tam': {'rich_text':[{'text':{'content':source_price[:1800]}}]}, 'Decisão Sourcing': {'select': {'name':decision}}}
        if img: props['Foto Produto']={'url':img}
        # Set defaults/clear risky import math fields until exact size is known.
        props['Preço exato tam USD']={'number': None}
        props['Custo trazer USD']={'number': DEFAULT_CUSTO_TRAZER_USD}
        props['Custo landed BRL']={'number': None}
        props['Venda ideal BRL']={'number': None}
        props['Margem venda atual %']={'number': nat_margin if decision=='Comprar nacional' else None}
        notion_result=None
        if page_id:
            notion_result=patch_page(tok,page_id,props)
            if not notion_result.get('error'): pages_updated+=1
            if not existing_marker(tok,page_id):
                blocks=[]
                if img: blocks.append(image_block(img,f'{RUN_MARKER}. Foto de referência do produto; não é validação de preço/tamanho.'))
                blocks += [
                    heading('Mesa Júlio — validação de sourcing'),
                    paragraph(f'{RUN_MARKER}. CORREÇÃO Lucas: custo importado = (preço exato USD do TAMANHO + custo trazer USD) × (dólar × 1,05). O markup 2 entra depois: venda ideal = custo landed × 2. Não usar preço product-level como custo do tamanho.'),
                    paragraph(f'{RUN_MARKER_V2B}. CORREÇÃO Lucas: Júlio nunca preenche valor. Hermes deve obter/validar o preço exato do tamanho; se não conseguir, o card fica pendente para Hermes/fonte integrada, não para digitação manual do Júlio.'),
                    paragraph(f'Produto/tamanho LK: {card.get("Modelo")} — Tam {card.get("Tamanho")} — SKU {card.get("SKU")}. Preço venda LK médio: {card.get("Preço médio vendido")}. Custo nacional sinal: {card.get("Opção nacional/Droper")}. Margem nacional prévia: {card.get("Margem nacional pré-taxas")}.),'.replace(').),', ').')),
                    paragraph(f'KicksDev/StockX product-level apenas como sinal: produto={(sx or {}).get("title") if isinstance(sx,dict) else "n/d"}; min produto={usd(product_signal_min)}. NÃO calcular compra/importação com este número sem preço exato do tamanho.'),
                    paragraph('Júlio: não preencher preço USD. Hermes valida o preço do tamanho correto e calcula Custo landed BRL, Venda ideal BRL e decisão final. Júlio atua na decisão/execução operacional; compra/reserva/contato/pagamento continuam humanos.')
                ]
                ap=append_blocks(tok,page_id,blocks)
                if not ap.get('error'): blocks_appended+=1
        rows.append({'title':title,'page_id':page_id,'url':(exec_rows.get(title) or {}).get('url'),'model':card.get('Modelo'),'size_lk':card.get('Tamanho'),'sku_lk':card.get('SKU'),'style_sku':style,'image_url':img,'sale_price_brl':sale,'national_cost_brl':nat,'national_margin_pct':nat_margin,'stockx_product_signal_min_usd':product_signal_min,'exact_size_price_usd':exact_price_usd,'exact_landed_cost_brl':exact_landed_brl,'ideal_sale_brl':ideal_sale_brl,'decision':decision,'notion_error':notion_result.get('error') if isinstance(notion_result,dict) else None})
        time.sleep(.35)
    summary={'status':'completed','generated_at':now(),'db_properties_patch_error':db_patch.get('error'),'cards':len(rows),'unique_styles_queried':len(cache),'pages_updated':pages_updated,'blocks_appended':blocks_appended,'formula_corrected':{'cost_landed_brl':'(exact_size_price_usd + custo_trazer_usd) × (usd_brl × 1.05)','ideal_sale_brl':'cost_landed_brl × 2','usd_brl':USD_BRL,'fx_buffer':FX_BUFFER,'markup':MARKUP,'exact_size_required':True},'not_performed':['purchase','reservation','supplier_contact','whatsapp_send','payment_schedule','shopify_write','tiny_write','merchant_write','notion_view_creation_api_not_supported'], 'rows':rows}
    OUT_JSON.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    lines=['# LK Sourcing Ops v2 — markup 2 + tamanho exato obrigatório','',f"Generated: `{summary['generated_at']}`",'','## Veredito','','- Correção aplicada: **não existe mais x2 dentro do custo**.','- Fórmula correta: `custo landed = (preço exato USD do tamanho + custo trazer USD) × (dólar × 1,05)`.','- Markup 2: `preço de venda ideal = custo landed × 2`.','- Correção aplicada: **não usar preço product-level do KicksDev/StockX como custo do tamanho**. Ele fica só como sinal/foto.','- Correção Lucas 2026-05-15: **Júlio nunca preenche valor**; Hermes deve buscar/validar o preço exato por tamanho.','- Cards Notion atualizados com campos de decisão e guardrail de preço exato por tamanho.','- API do Notion não cria/edita views; a Mesa Júlio foi materializada como campos + Mission Control + instrução. A view visual deve ser criada/ajustada na UI filtrando esses campos.','','## Mesa de Revisão Diária Júlio','','Filtro sugerido no Notion:','- `Status da Compra` = `Aguardando Aprovação`','- `Decisão Sourcing` = `Hermes validar preço/tamanho` ou `Comprar nacional`','- ordenar por prioridade/demanda no título/relatório','','Colunas sugeridas: Foto Produto, Nome, Modelo, Tamanho, Custo, Preço exato tam USD, Custo trazer USD, Custo landed BRL, Venda ideal BRL, Margem venda atual %, Fonte preço tam, Decisão Sourcing, Link.','','## Cards']
    for r in rows:
        lines += [f"### {r['model']} — Tam {r['size_lk']} — `{r['sku_lk']}`",f"- Foto: {r['image_url'] or 'n/d'}",f"- Custo nacional: {brl(r['national_cost_brl'])} · margem nacional: {pct(r['national_margin_pct'])}",f"- StockX product-level sinal min: {usd(r['stockx_product_signal_min_usd'])} — **não usado como custo**",f"- Preço exato tamanho USD: pendente para Hermes validar, não para Júlio preencher",f"- Decisão inicial: `{r['decision']}`",f"- Notion: {r['url']}", '']
    OUT_MD.write_text('\n'.join(lines)+'\n')
    MC_MD.write_text('\n'.join(lines[:45])+'\n\nFonte completa: `reports/lk-sourcing-ops-v2-markup2-exact-size-2026-05-15.md`\n')
    JULIO_MD.write_text('''# Instrução curta — Mesa Júlio LK Compras\n\n## Correção Lucas — 2026-05-15\n\nJúlio **não preenche valor**.\n\n1. Hermes identifica produto/modelo/tamanho e busca/valida preço do tamanho correto em fonte confiável/autenticada.\n2. Hermes calcula quando o preço exato existe: custo landed = (preço USD do tamanho correto + custo trazer USD) × (dólar × 1,05); venda ideal = custo landed × 2.\n3. Júlio usa o card para decisão/execução operacional: comprar, pular, acompanhar, registrar compra/resposta.\n4. Se Hermes não conseguir validar preço exato do tamanho, o card fica como `Hermes precisa validar preço por tamanho`, não como tarefa de preenchimento do Júlio.\n\n## Uso da mesa\n\n1. Abrir cards `Aguardando Aprovação`.\n2. Conferir foto, modelo, tamanho e disponibilidade real.\n3. Nunca usar preço genérico do produto como custo.\n4. Não pedir para Júlio preencher preço USD.\n5. Compra, contato e pagamento continuam humanos; cálculo e validação de preço por tamanho são responsabilidade do Hermes/fonte integrada.\n''')
    print(json.dumps({k:summary[k] for k in ['status','cards','unique_styles_queried','pages_updated','blocks_appended','db_properties_patch_error']},ensure_ascii=False))

if __name__=='__main__': main()
