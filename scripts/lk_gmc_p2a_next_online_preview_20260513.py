#!/usr/bin/env python3
from __future__ import annotations
import importlib.util, json, pathlib, re, csv
from collections import Counter, defaultdict
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
w4_path = ROOT / 'scripts/lk_gmc_p1_attribute_wave4_aggressive_nonprice_executor_20260513.py'
spec = importlib.util.spec_from_file_location('w4_p2a_next', w4_path)
w = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(w)
audit = w.import_audit()
secrets = audit.load_doppler()
mid = secrets.get('MERCHANT_CENTER_ID_LK')
token = audit.google_access_token(audit.parse_service_account(secrets))
products = w.list_all('products', mid, token)

def attrs(p):
    return p.get('productAttributes') or p.get('attributes') or {}

def pid(p):
    return p.get('id') or p.get('productId') or p.get('name', '').split('/')[-1]

def offer(id_):
    return id_.split(':')[-1]

def guess_category(title):
    s = (title or '').lower()
    # High-confidence mapped classes only. Avoid broad brand-only guessing here.
    if any(x in s for x in ['tênis ', 'tenis ', 'sneaker', 'handball spezial', 'samba og', 'gazelle', 'air jordan', 'air force', 'sb dunk', 'yeezy', 'new balance', 'asics gel', 'onitsuka', 'slide', 'mule']):
        return ('Apparel & Accessories > Shoes', 'Tênis', 'shoe_token_high_confidence')
    if any(x in s for x in ['camiseta', 't-shirt', 'tee shirt', 'short sleeve', 'long sleeve']):
        return ('Apparel & Accessories > Clothing > Shirts & Tops', 'Camiseta', 'shirt_token_high_confidence')
    if any(x in s for x in ['shorts', 'bermuda']):
        return ('Apparel & Accessories > Clothing > Shorts', 'Shorts', 'shorts_token_high_confidence')
    if any(x in s for x in ['moletom', 'hoodie', 'jaqueta', 'jacket', 'sweatshirt']):
        return ('Apparel & Accessories > Clothing > Outerwear', 'Moletom/Jaqueta', 'outerwear_token_high_confidence')
    if any(x in s for x in ['boné', 'bone ', 'cap ']):
        return ('Apparel & Accessories > Clothing Accessories > Hats', 'Boné', 'hat_token_high_confidence')
    if any(x in s for x in ['bolsa', 'bag', 'shoulder bag', 'tote', 'wallet', 'carteira']):
        return ('Luggage & Bags > Handbags, Wallets & Cases', 'Bolsa/Carteira', 'bag_token_high_confidence')
    if any(x in s for x in ['calça', 'pants', 'sweatpants']):
        return ('Apparel & Accessories > Clothing > Pants', 'Calça', 'pants_token_high_confidence')
    return (None, None, None)

rows=[]
for p in products:
    id_=pid(p)
    if not id_.startswith('online:pt:BR:'):
        continue
    at=attrs(p)
    t=at.get('title') or p.get('title') or ''
    gpc=at.get('googleProductCategory')
    pts=at.get('productTypes') or []
    sgpc,spt,evid=guess_category(t)
    if not sgpc:
        continue
    if gpc and pts:
        continue
    rows.append({
        'product_id':id_,
        'offer_id':offer(id_),
        'title':t,
        'current_googleProductCategory':gpc or '',
        'current_productTypes':pts,
        'suggested_googleProductCategory':sgpc,
        'suggested_productTypes':[spt],
        'evidence':evid,
        'eligible_for_p2a_next_wave': True,
    })
# Prioritize non-shoes first because shoes already had a major wave; but include shoe residuals if dominant.
priority={'Apparel & Accessories > Clothing > Shirts & Tops':0,'Apparel & Accessories > Clothing > Outerwear':1,'Apparel & Accessories > Clothing > Shorts':2,'Apparel & Accessories > Clothing > Pants':3,'Apparel & Accessories > Clothing Accessories > Hats':4,'Luggage & Bags > Handbags, Wallets & Cases':5,'Apparel & Accessories > Shoes':6}
rows.sort(key=lambda r:(priority.get(r['suggested_googleProductCategory'],9), r['suggested_productTypes'][0], r['title'], r['product_id']))
bucket_counts=Counter((r['suggested_googleProductCategory'], r['suggested_productTypes'][0]) for r in rows)
# Pilot recommendation: first 250 online rows, deterministic high-confidence, no local.
pilot=rows[:250]
summary={
 'generated_at':datetime.now(timezone.utc).isoformat(),
 'mode':'read_only_preview_no_write',
 'scope':'P2A next wave online ProductInputs only; googleProductCategory + productTypes only',
 'eligible_online_total':len(rows),
 'recommended_pilot_count':len(pilot),
 'eligible_bucket_counts':{f'{k[0]} / {k[1]}':v for k,v in bucket_counts.most_common()},
 'recommended_pilot_bucket_counts':{f'{k[0]} / {k[1]}':v for k,v in Counter((r['suggested_googleProductCategory'], r['suggested_productTypes'][0]) for r in pilot).most_common()},
 'pilot_rows':pilot,
 'sample_rows':rows[:80],
 'approval_text_recommended':'Aprovo aplicar P2A next wave piloto em 250 produtos online no GMC via Merchant API v1, apenas googleProductCategory e productTypes, com rollback e verificação.',
 'not_performed':['merchant_write','local_inventory_write','shopify_write','tiny_write','price_update','availability_update','title_update','image_or_link_update','feed_fetch_or_upload','campaign_or_message_send']
}
json_path=ROOT/'reports/lk-gmc-2026-05-13-p2a-next-online-preview.json'
md_path=ROOT/'reports/lk-gmc-2026-05-13-p2a-next-online-preview.md'
csv_path=ROOT/'reports/lk-gmc-2026-05-13-p2a-next-online-preview-pilot.csv'
json_path.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with csv_path.open('w',newline='',encoding='utf-8') as f:
    fields=['product_id','offer_id','title','current_googleProductCategory','current_productTypes','suggested_googleProductCategory','suggested_productTypes','evidence','eligible_for_p2a_next_wave']
    wr=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore'); wr.writeheader()
    for r in pilot:
        o={k:r.get(k) for k in fields}; o['current_productTypes']=json.dumps(o['current_productTypes'],ensure_ascii=False); o['suggested_productTypes']=json.dumps(o['suggested_productTypes'],ensure_ascii=False); wr.writerow(o)
lines=['# LK GMC P2A Next Online Preview — 2026-05-13','',f"Status: `read_only_preview_no_write`",'','## Escopo','- Somente `online:pt:BR:*`.','- Exclui `local:LIA_*`.','- Campos candidatos: `productAttributes.googleProductCategory` + `productAttributes.productTypes`.','- Sem título, preço, disponibilidade, imagem/link, Shopify, Tiny ou feed.','', '## Resumo',f"- Elegíveis online: {len(rows)}",f"- Piloto recomendado: {len(pilot)}",f"- Buckets elegíveis: {summary['eligible_bucket_counts']}",f"- Buckets do piloto: {summary['recommended_pilot_bucket_counts']}",'','## Approval recomendado',f"`{summary['approval_text_recommended']}`",'','## Amostra do piloto']
for r in pilot[:20]:
    lines.append(f"- `{r['product_id']}` — {r['title']} → {r['suggested_googleProductCategory']} / {r['suggested_productTypes'][0]}")
lines += ['', '## Não executado'] + [f'- {x}' for x in summary['not_performed']]
md_path.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(json.dumps({'status':'p2a_next_online_preview_ready','eligible_online_total':len(rows),'recommended_pilot_count':len(pilot),'pilot_buckets':summary['recommended_pilot_bucket_counts'],'report':str(md_path),'csv':str(csv_path)},ensure_ascii=False,indent=2))
