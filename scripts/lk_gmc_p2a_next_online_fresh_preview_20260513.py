#!/usr/bin/env python3
from __future__ import annotations
import csv, importlib.util, json, pathlib, re, time
from collections import Counter
from datetime import datetime, timezone

ROOT=pathlib.Path(__file__).resolve().parents[1]
P2=ROOT/'scripts/lk_gmc_p2_category_product_type_executor_20260513.py'
spec=importlib.util.spec_from_file_location('p2fresh', P2)
p2=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(p2)
w=p2.import_w4(); audit=w.import_audit(); secrets=audit.load_doppler(); mid=secrets.get('MERCHANT_CENTER_ID_LK'); token=audit.google_access_token(audit.parse_service_account(secrets))
products=w.list_all('products', mid, token)

def attrs(p): return p.get('productAttributes') or p.get('attributes') or {}
def pid(p): return p.get('id') or p.get('productId') or p.get('name','').split('/')[-1]
def offer(id_): return id_.split(':')[-1]
def guess_category(title):
    s=(title or '').lower()
    if any(x in s for x in ['camiseta','t-shirt','tee shirt','short sleeve','long sleeve']): return ('Apparel & Accessories > Clothing > Shirts & Tops','Camiseta','shirt_token_high_confidence')
    if any(x in s for x in ['moletom','hoodie','jaqueta','jacket','sweatshirt']): return ('Apparel & Accessories > Clothing > Outerwear','Moletom/Jaqueta','outerwear_token_high_confidence')
    if any(x in s for x in ['shorts','bermuda']): return ('Apparel & Accessories > Clothing > Shorts','Shorts','shorts_token_high_confidence')
    if any(x in s for x in ['calça','pants','sweatpants']): return ('Apparel & Accessories > Clothing > Pants','Calça','pants_token_high_confidence')
    if any(x in s for x in ['boné','bone ','cap ']): return ('Apparel & Accessories > Clothing Accessories > Hats','Boné','hat_token_high_confidence')
    if any(x in s for x in ['bolsa','bag','shoulder bag','tote','wallet','carteira']): return ('Luggage & Bags > Handbags, Wallets & Cases','Bolsa/Carteira','bag_token_high_confidence')
    if any(x in s for x in ['tênis ','tenis ','sneaker','handball spezial','samba og','gazelle','air jordan','air force','sb dunk','yeezy','new balance','asics gel','onitsuka','slide','mule']): return ('Apparel & Accessories > Shoes','Tênis','shoe_token_high_confidence')
    return (None,None,None)
priority={'Apparel & Accessories > Clothing > Shirts & Tops':0,'Apparel & Accessories > Clothing > Outerwear':1,'Apparel & Accessories > Clothing > Shorts':2,'Apparel & Accessories > Clothing > Pants':3,'Apparel & Accessories > Clothing Accessories > Hats':4,'Luggage & Bags > Handbags, Wallets & Cases':5,'Apparel & Accessories > Shoes':6}
base=[]
for p in products:
    id_=pid(p)
    if not id_.startswith('online:pt:BR:'): continue
    at=attrs(p); title=at.get('title') or p.get('title') or ''
    sgpc,spt,evid=guess_category(title)
    if not sgpc: continue
    base.append({'product_id':id_,'offer_id':offer(id_),'title':title,'suggested_googleProductCategory':sgpc,'suggested_productTypes':[spt],'evidence':evid})
base.sort(key=lambda r:(priority.get(r['suggested_googleProductCategory'],9), r['suggested_productTypes'][0], r['title'], r['product_id']))
selected=[]; checked=0; skipped_compliant=0; skipped_error=[]
for r in base:
    if len(selected)>=250: break
    checked+=1
    try:
        _name, enc, *_=p2.product_input_name(mid, r['product_id'])
        fresh=(p2.merchant_product_get(mid, enc, token).get('productAttributes') or {})
        cur_gpc=fresh.get('googleProductCategory'); cur_pts=fresh.get('productTypes') or []
        if cur_gpc==r['suggested_googleProductCategory'] and cur_pts==r['suggested_productTypes']:
            skipped_compliant+=1; continue
        selected.append({**r,'fresh_current_googleProductCategory':cur_gpc or '','fresh_current_productTypes':cur_pts,'fresh_title':fresh.get('title') or r['title'],'eligible_for_p2a_next_wave':True})
    except Exception as e:
        skipped_error.append({'product_id':r['product_id'],'error':str(e)[:500]})
    time.sleep(0.03)
summary={'generated_at':datetime.now(timezone.utc).isoformat(),'mode':'fresh_read_only_preview_no_write','base_candidates':len(base),'checked_until_selected':checked,'skipped_already_compliant':skipped_compliant,'selected_count':len(selected),'selected_bucket_counts':{f'{k[0]} / {k[1]}':v for k,v in Counter((r['suggested_googleProductCategory'],r['suggested_productTypes'][0]) for r in selected).most_common()},'selected_rows':selected,'skipped_error_sample':skipped_error[:20],'approval_text_recommended':'Aprovo aplicar P2A next wave fresh em 250 produtos online no GMC via Merchant API v1, apenas googleProductCategory e productTypes, com rollback e verificação.','not_performed':['merchant_write','shopify_write','tiny_write','price_update','availability_update','title_update','image_or_link_update','local_inventory_write','feed_fetch_or_upload','campaign_or_message_send']}
json_path=ROOT/'reports/lk-gmc-2026-05-13-p2a-next-online-fresh-preview.json'
md_path=ROOT/'reports/lk-gmc-2026-05-13-p2a-next-online-fresh-preview.md'
csv_path=ROOT/'reports/lk-gmc-2026-05-13-p2a-next-online-preview-pilot.csv'
json_path.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with csv_path.open('w',newline='',encoding='utf-8') as f:
    fields=['product_id','offer_id','title','fresh_current_googleProductCategory','fresh_current_productTypes','suggested_googleProductCategory','suggested_productTypes','evidence','eligible_for_p2a_next_wave']
    wr=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore'); wr.writeheader()
    for r in selected:
        o={k:r.get(k) for k in fields}; o['fresh_current_productTypes']=json.dumps(o['fresh_current_productTypes'],ensure_ascii=False); o['suggested_productTypes']=json.dumps(o['suggested_productTypes'],ensure_ascii=False); wr.writerow(o)
lines=['# LK GMC P2A Next Online Fresh Preview — 2026-05-13','',f"Status: `fresh_read_only_preview_no_write`",'','## Resumo',f"- Base candidates: {len(base)}",f"- Checked: {checked}",f"- Skipped already compliant: {skipped_compliant}",f"- Selected: {len(selected)}",f"- Buckets selected: {summary['selected_bucket_counts']}",'','## Approval recomendado',f"`{summary['approval_text_recommended']}`",'','## Amostra']
for r in selected[:20]: lines.append(f"- `{r['product_id']}` — {r['title']} → {r['suggested_googleProductCategory']} / {r['suggested_productTypes'][0]}")
lines += ['','## Não executado']+[f'- {x}' for x in summary['not_performed']]
md_path.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(json.dumps({'status':'fresh_preview_ready','base_candidates':len(base),'checked':checked,'skipped_already_compliant':skipped_compliant,'selected':len(selected),'buckets':summary['selected_bucket_counts'],'report':str(md_path),'csv':str(csv_path)},ensure_ascii=False,indent=2))
