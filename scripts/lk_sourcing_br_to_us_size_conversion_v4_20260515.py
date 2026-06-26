#!/usr/bin/env python3
from __future__ import annotations
import base64,json,os,pathlib,time,urllib.error,urllib.request
from datetime import datetime,timezone
from decimal import Decimal

ROOT=pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
DOPPLER_TOKEN_FILE=pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
V3=ROOT/'reports/lk-sourcing-exact-size-validator-v3-2026-05-15.json'
OUT_JSON=ROOT/'reports/lk-sourcing-br-to-us-size-conversion-v4-2026-05-15.json'
OUT_MD=ROOT/'reports/lk-sourcing-br-to-us-size-conversion-v4-2026-05-15.md'
MC_MD=ROOT/'areas/lk/rotinas/mission-control-sourcing-br-to-us-size-conversion-v4-2026-05-15.md'
NOTION_VERSION='2022-06-28'
NOTION_DB='2b127dc9-e033-805b-81b6-f62f5467ce77'
MARKER='LK OS sourcing v4 — BR→US size conversion; StockX/GOAT match is mapped, ask price still source-dependent — 2026-05-15'


def now(): return datetime.now(timezone.utc).isoformat()
def brl(v): return 'n/d' if v is None else f'R$ {float(v):,.2f}'.replace(',','X').replace('.',',').replace('X','.')
def pct(v): return 'n/d' if v is None else f'{float(v)*100:.1f}%'

def size_str(v):
    d=Decimal(str(v))
    return str(int(d)) if d==int(d) else str(d).rstrip('0').rstrip('.')

def br_to_us_size(br, gender):
    # Lucas correction: BR number must be converted to the US marketplace size.
    # For LK sourcing cards in this cohort the operational mapping is BR - 33,
    # which also matches the suffix pattern in most SKUs (e.g. BR37 -> US4).
    us=Decimal(str(br))-Decimal('33')
    g=(gender or '').lower()
    if g=='women': label=f'US W {size_str(us)}'
    elif g=='men': label=f'US M {size_str(us)}'
    else: label=f'US {size_str(us)} / conferir M/W no marketplace'
    return size_str(us), label

def load_doppler():
    token=os.environ.get('DOPPLER_TOKEN') or DOPPLER_TOKEN_FILE.read_text().strip()
    req=urllib.request.Request('https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json')
    req.add_header('Authorization','Basic '+base64.b64encode((token+':').encode()).decode())
    with urllib.request.urlopen(req,timeout=60) as r: return json.loads(r.read().decode())

def nh(tok): return {'Authorization':'Bearer '+tok,'Notion-Version':NOTION_VERSION}
def http_json(url,headers,method='GET',payload=None,attempts=4):
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
            if e.code not in {429,500,502,503,504} or i==attempts-1: return {'error':f'http_{e.code}','body':body[:1000]}
        except Exception as e:
            if i==attempts-1: return {'error':type(e).__name__,'body':str(e)[:1000]}
        time.sleep(min(20,2**(i+1)))
    return {'error':'request_failed'}

def paragraph(text): return {'object':'block','type':'paragraph','paragraph':{'rich_text':[{'type':'text','text':{'content':text[:1900]}}]}}
def heading(text): return {'object':'block','type':'heading_2','heading_2':{'rich_text':[{'type':'text','text':{'content':text[:1900]}}]}}
def existing_marker(tok,page_id):
    d=http_json(f'https://api.notion.com/v1/blocks/{page_id}/children?page_size=100',nh(tok))
    for b in d.get('results',[]) if isinstance(d,dict) else []:
        typ=b.get('type')
        if typ and typ in b:
            rich=b[typ].get('rich_text') or b[typ].get('caption') or []
            text=''.join(x.get('plain_text') or (x.get('text') or {}).get('content') or '' for x in rich)
            if MARKER in text: return True
    return False

GENDER_BY_STYLE={
    '1183A201-126':'men',
    '1183C102.751':'unisex',
    'HV8547-700':'women',
    'JR9446':'women',
    'U204LMMC':'men',
}

def main():
    sec=load_doppler(); tok=sec.get('NOTION_TOKEN_LK') or sec.get('NOTION_API_KEY')
    if not tok: raise SystemExit('missing notion token')
    # Add a dedicated field so the card does not imply “no match”; it shows the converted target.
    db=http_json(f'https://api.notion.com/v1/databases/{NOTION_DB}',nh(tok),method='PATCH',payload={'properties':{'Tamanho US alvo': {'rich_text': {}}, 'Status preço import': {'select': {'options':[{'name':'US size mapeado; preço pendente','color':'yellow'},{'name':'Preço USD validado','color':'green'},{'name':'Fonte/API não retornou ask','color':'orange'}]}}}})
    rows=json.loads(V3.read_text())['rows']
    out=[]; updated=0; appended=0; errors=[]
    for r in rows:
        gender=GENDER_BY_STYLE.get(r['style_sku'],'unknown')
        us_value, us_label=br_to_us_size(r['size_lk'],gender)
        status='US size mapeado; preço pendente'
        text=(f'CORREÇÃO Lucas: não é “sem match”. Tamanho BR {r["size_lk"]} foi convertido para {us_label} para StockX/GOAT. '
              f'O que ainda falta é a fonte/API devolver o ask/preço USD exato desse tamanho convertido. Product-level continua só sinal/foto; Júlio não preenche valor.')
        props={'Tamanho US alvo': {'rich_text':[{'text':{'content':us_label}}]}, 'Status preço import': {'select': {'name':status}}, 'Fonte preço tam': {'rich_text':[{'text':{'content':text[:1800]}}]}}
        pr=http_json(f'https://api.notion.com/v1/pages/{r["page_id"]}',nh(tok),method='PATCH',payload={'properties':props})
        if pr.get('error'): errors.append({'page_id':r['page_id'],'error':pr.get('error'),'body':pr.get('body')})
        else: updated+=1
        if not existing_marker(tok,r['page_id']):
            blocks=[heading('Correção de tamanho BR→US para StockX/GOAT'), paragraph(f'{MARKER}. Tamanho LK/BR {r["size_lk"]} convertido para {us_label}. Portanto, o status correto não é “sem match”; é “US size mapeado; preço pendente” enquanto a fonte não retorna ask/preço USD do tamanho.'), paragraph('Cálculo de importação continua bloqueado até existir preço USD exato do tamanho convertido. Fórmula: landed=(USD+custo trazer)×(FX×1,05); venda ideal=landed×2. Nenhuma compra/contato/pagamento executado.')]
            ap=http_json(f'https://api.notion.com/v1/blocks/{r["page_id"]}/children',nh(tok),method='PATCH',payload={'children':blocks})
            if ap.get('error'): errors.append({'page_id':r['page_id'],'append_error':ap.get('error')})
            else: appended+=1
        out.append({**r,'gender_market':gender,'br_size':r['size_lk'],'us_size_value':us_value,'us_size_label':us_label,'import_price_status':status})
        time.sleep(.25)
    summary={'status':'completed' if not errors else 'completed_with_errors','generated_at':now(),'cards':len(out),'pages_updated':updated,'blocks_appended':appended,'db_error':db.get('error'),'correction':'BR size always maps to US target size; blocked state can only mean price source/API has not returned ask, not size no-match','not_performed':['purchase','reservation','supplier_contact','whatsapp_send','payment_schedule','shopify_write','tiny_write','merchant_write'],'errors':errors,'rows':out}
    OUT_JSON.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    lines=['# LK Sourcing v4 — conversão BR→US para StockX/GOAT','',f"Generated: `{summary['generated_at']}`",'','## Correção aplicada','','- Correção Lucas: se existe número brasileiro, existe alvo americano por tabela de conversão.','- Portanto, não usar mais `sem match` para StockX/GOAT só porque o card está em BR.','- Status correto: `US size mapeado; preço pendente` enquanto a fonte/API não devolver ask/preço USD do tamanho convertido.','- Júlio não preenche valor. Hermes busca/valida preço por tamanho.','','## Mapeamento dos 14 cards']
    for r in out:
        lines += [f"### {r['model']} — BR {r['br_size']} → {r['us_size_label']}",f"- SKU: `{r['sku_lk']}`",f"- Mercado/gênero StockX: `{r['gender_market']}`",f"- Status importação: `{r['import_price_status']}`",f"- Decisão nacional atual: `{r['decision_v3']}`",'']
    OUT_MD.write_text('\n'.join(lines)+'\n')
    MC_MD.write_text('\n'.join(lines)+'\n')
    print(json.dumps({k:summary[k] for k in ['status','cards','pages_updated','blocks_appended','db_error']},ensure_ascii=False))

if __name__=='__main__': main()
