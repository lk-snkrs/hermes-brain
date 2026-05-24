#!/usr/bin/env python3
from __future__ import annotations
import base64, json, os, pathlib, time, urllib.error, urllib.request
from datetime import datetime, timezone
from decimal import Decimal

ROOT=pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
DOPPLER_TOKEN_FILE=pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
V3=ROOT/'reports/lk-sourcing-exact-size-validator-v3-2026-05-15.json'
V4=ROOT/'reports/lk-sourcing-br-to-us-size-conversion-v4-2026-05-15.json'
OUT_JSON=ROOT/'reports/lk-sourcing-br-to-us-size-conversion-v5-2026-05-15.json'
OUT_MD=ROOT/'reports/lk-sourcing-br-to-us-size-conversion-v5-2026-05-15.md'
MC_MD=ROOT/'areas/lk/rotinas/mission-control-sourcing-br-to-us-size-conversion-v5-2026-05-15.md'
NOTION_VERSION='2022-06-28'
NOTION_DB='2b127dc9-e033-805b-81b6-f62f5467ce77'
MARKER='LK OS sourcing v5 — researched BR→US conversion table; Hermes matches size automatically — 2026-05-15'

# Sources used to create the table:
# 1) ShoeSize.io Brazil→US guide: Brazilian sizing follows BR = EU - 2 and gives BR↔US charts.
# 2) Nike official size-fit pages (mens/womens footwear): EU↔US Men/Women rows.
# Operational rule: convert LK BR to EU via EU=BR+2, then map EU to US marketplace size by gender/market.
SOURCES=[
    'https://shoesize.io/brazil-to-us-shoe-size-converter/ — BR = EU - 2; Brazil→US guide/charts',
    'https://www.nike.com/size-fit/mens-footwear — official EU↔US Men footwear chart',
    'https://www.nike.com/size-fit/womens-footwear — official EU↔US Women footwear chart',
]

# EU→US tables transcribed from Nike official footwear pages. We use Decimal strings to keep halves exact.
EU_TO_US_MEN={
    '35.5':'3.5','36':'4','36.5':'4.5','37.5':'5','38':'5.5','38.5':'6','39':'6.5','40':'7','40.5':'7.5','41':'8','42':'8.5','42.5':'9','43':'9.5','44':'10','44.5':'10.5','45':'11','45.5':'11.5','46':'12','47':'12.5','47.5':'13','48':'13.5','48.5':'14','49':'14.5','49.5':'15','50':'15.5','50.5':'16','51':'16.5','51.5':'17','52':'17.5','52.5':'18','53':'18.5','53.5':'19','54':'19.5','54.5':'20','55':'20.5','55.5':'21','56':'21.5','56.5':'22'
}
EU_TO_US_WOMEN={
    '33.5':'3.5','34.5':'4','35':'4.5','35.5':'5','36':'5.5','36.5':'6','37.5':'6.5','38':'7','38.5':'7.5','39':'8','40':'8.5','40.5':'9','41':'9.5','42':'10','42.5':'10.5','43':'11','44':'11.5','44.5':'12','45':'12.5','45.5':'13','46':'13.5','47':'14','47.5':'14.5','48':'15','48.5':'15.5','49':'16','50':'16.5','50.5':'17','51':'17.5','51.5':'18','52':'18.5','52.5':'19','53':'19.5','53.5':'20','54':'20.5','54.5':'21','55':'21.5','55.5':'22','56':'22.5'
}

# Some marketplace/source pages use rounded BR→US charts without half sizes. Prefer brand/EU map above;
# if EU integer is absent for the market, fallback to nearest EU row within 0.5 and mark it.
def fmt_decimal(d: Decimal) -> str:
    return str(int(d)) if d == int(d) else str(d).rstrip('0').rstrip('.')

def nearest_us(eu: Decimal, table: dict[str,str]):
    exact=table.get(fmt_decimal(eu))
    if exact is not None:
        return exact, 'exact_eu_brand_chart'
    candidates=[]
    for k,v in table.items():
        kd=Decimal(k); diff=abs(kd-eu)
        if diff <= Decimal('0.5'):
            candidates.append((diff,kd,v))
    if not candidates:
        return None, 'outside_table'
    candidates.sort(key=lambda x:(x[0], x[1]))
    diff,kd,v=candidates[0]
    return v, f'nearest_eu_brand_chart:{fmt_decimal(kd)}'

def br_to_us_size(br, gender):
    br_d=Decimal(str(br))
    eu=br_d+Decimal('2')
    g=(gender or '').lower()
    if g=='women':
        us,method=nearest_us(eu, EU_TO_US_WOMEN); label=f'US W {us}' if us else 'US W n/d'
    elif g=='men':
        us,method=nearest_us(eu, EU_TO_US_MEN); label=f'US M {us}' if us else 'US M n/d'
    else:
        us_m,method_m=nearest_us(eu, EU_TO_US_MEN)
        us_w,method_w=nearest_us(eu, EU_TO_US_WOMEN)
        us={'men':us_m,'women':us_w}; method=f'men:{method_m}; women:{method_w}'
        label=f'US M {us_m} / US W {us_w} — conferir listagem StockX/GOAT'
    return {'br':fmt_decimal(br_d),'eu':fmt_decimal(eu),'us_value':us,'label':label,'method':method,'gender':g or 'unknown'}

def now(): return datetime.now(timezone.utc).isoformat()
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
    db=http_json(f'https://api.notion.com/v1/databases/{NOTION_DB}',nh(tok),method='PATCH',payload={'properties':{'Tamanho EU ref': {'rich_text': {}}, 'Tamanho US alvo': {'rich_text': {}}, 'Status preço import': {'select': {'options':[{'name':'US size mapeado; preço pendente','color':'yellow'},{'name':'Preço USD validado','color':'green'},{'name':'Fonte/API não retornou ask','color':'orange'}]}}}})
    rows=json.loads(V3.read_text())['rows']
    v4_by_sku={}
    if V4.exists():
        try:
            v4_by_sku={r.get('sku_lk'):r for r in json.loads(V4.read_text()).get('rows',[])}
        except Exception:
            v4_by_sku={}
    out=[]; updated=0; appended=0; errors=[]; changed=[]
    for r in rows:
        gender=GENDER_BY_STYLE.get(r['style_sku'],'unknown')
        conv=br_to_us_size(r['size_lk'],gender)
        prev = (v4_by_sku.get(r.get('sku_lk')) or {}).get('us_size_label')
        status='US size mapeado; preço pendente'
        text=(f'Hermes pesquisou e criou tabela própria: BR {conv["br"]} → EU {conv["eu"]} (regra BR=EU-2) → {conv["label"]} para StockX/GOAT. '
              f'Método: {conv["method"]}. Fonte base: ShoeSize.io + Nike size-fit EU↔US. Júlio não preenche valor; Hermes busca ask/preço USD exato dessa variante. Product-level segue só sinal/foto.')
        props={'Tamanho EU ref': {'rich_text':[{'text':{'content':conv['eu']}}]}, 'Tamanho US alvo': {'rich_text':[{'text':{'content':conv['label']}}]}, 'Status preço import': {'select': {'name':status}}, 'Fonte preço tam': {'rich_text':[{'text':{'content':text[:1800]}}]}}
        pr=http_json(f'https://api.notion.com/v1/pages/{r["page_id"]}',nh(tok),method='PATCH',payload={'properties':props})
        if pr.get('error'): errors.append({'page_id':r['page_id'],'error':pr.get('error'),'body':pr.get('body')})
        else: updated+=1
        if not existing_marker(tok,r['page_id']):
            blocks=[heading('Tabela Hermes BR→US pesquisada'), paragraph(f'{MARKER}. {text}'), paragraph('Regra operacional: se LK tem tamanho BR, Hermes converte sozinho; o bloqueio só pode ser falta de ask/preço USD exato do tamanho convertido, nunca “Júlio preencher valor”. Fórmula de importação preservada: landed=(USD+custo trazer)×(FX×1,05); venda ideal=landed×2.'), paragraph('Não executado: compra, reserva, contato fornecedor, WhatsApp, pagamento, Shopify/Tiny/Merchant.')]
            ap=http_json(f'https://api.notion.com/v1/blocks/{r["page_id"]}/children',nh(tok),method='PATCH',payload={'children':blocks})
            if ap.get('error'): errors.append({'page_id':r['page_id'],'append_error':ap.get('error')})
            else: appended+=1
        row={**r,'conversion_sources':SOURCES,'gender_market':conv['gender'],'br_size':conv['br'],'eu_reference_size':conv['eu'],'us_size_value':conv['us_value'],'us_size_label':conv['label'],'conversion_method':conv['method'],'previous_us_size_label':prev,'import_price_status':status}
        if prev and prev != conv['label']:
            changed.append({'sku_lk':r['sku_lk'],'model':r['model'],'br':conv['br'],'previous':prev,'new':conv['label']})
        out.append(row)
        time.sleep(.25)
    summary={'status':'completed' if not errors else 'completed_with_errors','generated_at':now(),'cards':len(out),'pages_updated':updated,'blocks_appended':appended,'db_error':db.get('error'),'sources':SOURCES,'rule':'BR→EU uses EU=BR+2; EU→US uses official Nike EU↔US table by market gender; unisex outputs both M/W targets','changed_from_v4_count':len(changed),'changed_from_v4':changed,'not_performed':['purchase','reservation','supplier_contact','whatsapp_send','payment_schedule','shopify_write','tiny_write','merchant_write'],'errors':errors,'rows':out}
    OUT_JSON.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    lines=['# LK Sourcing v5 — tabela própria BR→US pesquisada','',f"Generated: `{summary['generated_at']}`",'','## Fontes usadas']
    lines += [f'- {s}' for s in SOURCES]
    lines += ['','## Regra operacional','- `BR → EU`: usar `EU = BR + 2`.', '- `EU → US`: usar tabela oficial de calçados Nike por mercado (`US Men` / `US Women`).', '- Unisex: salvar M/W para o Hermes consultar a listagem correta na StockX/GOAT.', '- Júlio não preenche preço; Hermes busca o ask/preço USD exato da variante convertida.', '', f"## Mudanças vs v4: {len(changed)}"]
    for c in changed:
        lines.append(f"- `{c['sku_lk']}` BR {c['br']}: `{c['previous']}` → `{c['new']}`")
    lines += ['','## Mapeamento dos cards']
    for r in out:
        lines += [f"### {r['model']} — BR {r['br_size']} → EU {r['eu_reference_size']} → {r['us_size_label']}",f"- SKU: `{r['sku_lk']}`",f"- Mercado/gênero: `{r['gender_market']}`",f"- Método: `{r['conversion_method']}`",f"- Status importação: `{r['import_price_status']}`",f"- Decisão nacional atual: `{r['decision_v3']}`",'']
    OUT_MD.write_text('\n'.join(lines)+'\n')
    MC_MD.write_text('\n'.join(lines)+'\n')
    print(json.dumps({k:summary[k] for k in ['status','cards','pages_updated','blocks_appended','changed_from_v4_count','db_error']},ensure_ascii=False))

if __name__=='__main__': main()
