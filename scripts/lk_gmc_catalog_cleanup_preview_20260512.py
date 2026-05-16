#!/usr/bin/env python3
"""Read-only cleanup preview for inflated LK Merchant Center catalog.

Builds a suppression/deletion *preview only* for Merchant products by comparing
Merchant offer IDs/dimensions to the local Shopify/Data Spine snapshot. This
script never calls Merchant insert/update/delete/custombatch.
"""
from __future__ import annotations
import base64, csv, io, json, pathlib, sqlite3, subprocess, tempfile, time, urllib.parse, urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from typing import Any

ROOT=pathlib.Path(__file__).resolve().parents[1]
DOPPLER_TOKEN_FILE=pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
LOCAL_DB=pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite')
OUT_JSON=ROOT/'reports/lk-gmc-catalog-cleanup-preview-2026-05-12.json'
OUT_MD=ROOT/'reports/lk-gmc-catalog-cleanup-preview-2026-05-12.md'
OUT_CSV=ROOT/'reports/lk-gmc-catalog-cleanup-preview-2026-05-12.csv'
BRAIN_DOC=ROOT/'areas/lk/rotinas/gmc-catalog-cleanup-preview-2026-05-12.md'
SCOPE='https://www.googleapis.com/auth/content'

def b64url(b:bytes)->str: return base64.urlsafe_b64encode(b).decode().rstrip('=')
def load_secrets():
    token=DOPPLER_TOKEN_FILE.read_text().strip()
    req=urllib.request.Request('https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json')
    req.add_header('Authorization','Basic '+base64.b64encode((token+':').encode()).decode())
    return json.loads(urllib.request.urlopen(req,timeout=60).read().decode())
def google_token(secrets):
    raw=secrets.get('GOOGLE_SERVICE_ACCOUNT_JSON') or secrets.get('GA4_LK_N8N_ZIPPER_SERVICE_ACCOUNT') or secrets.get('GA4_LK_SERVICE_ACCOUNT')
    sa=json.loads(raw) if raw and raw.strip().startswith('{') else json.loads(base64.b64decode(raw or '').decode())
    now=int(time.time()); claim={'iss':sa['client_email'],'scope':SCOPE,'aud':sa.get('token_uri') or 'https://oauth2.googleapis.com/token','iat':now,'exp':now+3600}
    inp=b64url(json.dumps({'alg':'RS256','typ':'JWT'},separators=(',',':')).encode())+'.'+b64url(json.dumps(claim,separators=(',',':')).encode())
    with tempfile.NamedTemporaryFile('w',delete=False) as f: f.write(sa['private_key']); kp=f.name
    try: sig=subprocess.run(['openssl','dgst','-sha256','-sign',kp],input=inp.encode(),capture_output=True,check=True).stdout
    finally: pathlib.Path(kp).unlink(missing_ok=True)
    req=urllib.request.Request(sa.get('token_uri') or 'https://oauth2.googleapis.com/token',data=urllib.parse.urlencode({'grant_type':'urn:ietf:params:oauth:grant-type:jwt-bearer','assertion':inp+'.'+b64url(sig)}).encode(),method='POST')
    req.add_header('Content-Type','application/x-www-form-urlencoded')
    return json.loads(urllib.request.urlopen(req,timeout=60).read().decode())['access_token']
def get_json(url, token):
    req=urllib.request.Request(url); req.add_header('Authorization','Bearer '+token)
    return json.loads(urllib.request.urlopen(req,timeout=120).read().decode())
def list_products(mid, token):
    rows=[]; pt=None
    while True:
        qs={'maxResults':'250'}
        if pt: qs['pageToken']=pt
        data=get_json(f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/products?'+urllib.parse.urlencode(qs),token)
        rows += data.get('resources') or []
        pt=data.get('nextPageToken')
        if not pt: break
    return rows
def parse_pid(pid):
    parts=(pid or '').split(':',3)
    if len(parts)==4: return {'channel':parts[0],'lang':parts[1],'country':parts[2],'offer_id':parts[3]}
    return {'channel':'unknown','lang':'','country':'','offer_id':pid or ''}
def normalized_offer_id(offer_id, channel):
    # LK local inventory rows from Shopify POS/Local Inventory Ads use LIA_<sku>.
    # Strip only for reconciliation; never mutate Merchant IDs from this preview.
    if channel == 'local' and (offer_id or '').startswith('LIA_'):
        return offer_id[4:]
    return offer_id
def local_sets():
    con=sqlite3.connect(str(LOCAL_DB)); cur=con.cursor()
    skus=set(r[0] for r in cur.execute("select distinct sku from lk_product_variants where coalesce(sku,'')<>''"))
    source_variant_ids=set(str(r[0]) for r in cur.execute("select distinct source_variant_id from lk_product_variants where coalesce(source_variant_id,'')<>''"))
    variant_ids=set(str(r[0]) for r in cur.execute("select distinct variant_id from lk_product_variants where coalesce(variant_id,'')<>''"))
    active_skus=set(r[0] for r in cur.execute("select distinct sku from lk_product_variants v join lk_products p on v.product_id=p.product_id where coalesce(v.sku,'')<>'' and lower(coalesce(p.status,''))='active'"))
    con.close(); return skus, source_variant_ids|variant_ids, active_skus
def main():
    secrets=load_secrets(); token=google_token(secrets); mid=secrets['MERCHANT_CENTER_ID_LK']
    products=list_products(mid, token)
    skus, variant_ids, active_skus=local_sets()
    by_offer=defaultdict(list)
    parsed=[]
    for p in products:
        pid=p.get('id') or ''
        meta=parse_pid(pid); p['_meta']=meta; parsed.append(p); by_offer[meta['offer_id']].append(p)
    rows=[]
    reason_counts=Counter(); action_counts=Counter(); channel_counts=Counter()
    for p in parsed:
        m=p['_meta']; oid=m['offer_id']; recon_oid=normalized_offer_id(oid, m['channel']); chans={x['_meta']['channel'] for x in by_offer[oid]}
        matches_sku=recon_oid in skus or recon_oid in active_skus
        matches_variant_id=recon_oid in variant_ids
        has_online='online' in chans; has_local='local' in chans
        action='monitor_keep_for_now'; reason='no_safe_cleanup_signal'
        priority='P3'
        if m['channel']=='local' and oid.startswith('LIA_') and (matches_sku or matches_variant_id):
            action='keep_valid_local_listing_preview_only'; reason='local_lia_prefix_matches_shopify_after_normalization'; priority='P3'
        elif m['channel']=='local' and has_online:
            action='cleanup_candidate_local_duplicate_preview_only'; reason='same_offer_id_exists_as_online_and_local'; priority='P1'
        elif m['channel']=='local' and not (matches_sku or matches_variant_id):
            action='investigate_or_suppress_local_orphan_preview_only'; reason='local_offer_id_not_found_after_lia_normalization_in_shopify_sku_or_variant_ids'; priority='P1'
        elif m['channel']=='local':
            action='review_local_listing_policy_preview_only'; reason='local_channel_matches_shopify_identifier_but_may_not_be_needed_for_LK'; priority='P2'
        elif m['channel']=='online' and not (matches_sku or matches_variant_id):
            action='investigate_online_orphan_preview_only'; reason='online_offer_id_not_found_in_shopify_sku_or_variant_ids'; priority='P2'
        reason_counts[reason]+=1; action_counts[action]+=1; channel_counts[m['channel']]+=1
        if priority in {'P1','P2'}:
            rows.append({'priority':priority,'product_id':p.get('id'),'offer_id':oid,'reconciliation_offer_id':recon_oid,'channel':m['channel'],'title':p.get('title'),'action':action,'reason':reason,'has_online_counterpart':has_online,'has_local_counterpart':has_local,'matches_shopify_sku':matches_sku,'matches_shopify_variant_id':matches_variant_id,'approval_status':'preview_only_requires_explicit_cleanup_approval'})
    rows.sort(key=lambda r: (r['priority'], r['action'], r['offer_id']))
    public_rows=rows[:500]
    payload={'generated_at':datetime.now(timezone.utc).isoformat(),'scope':'LK GMC catalog cleanup preview read-only','status':'gmc_catalog_cleanup_preview_ready_readonly','summary':{'merchant_products_read':len(products),'merchant_channels':dict(channel_counts),'preview_rows_total_p1_p2':len(rows),'p1_rows':sum(1 for r in rows if r['priority']=='P1'),'p2_rows':sum(1 for r in rows if r['priority']=='P2'),'action_counts':dict(action_counts),'reason_counts':dict(reason_counts),'sample_rows_published':len(public_rows),'merchant_writes':0,'shopify_writes':0},'recommendation':{'next_best_improvement':'Do not clean the local channel as generic noise. LK uses local listings; first handle only local rows that remain unmatched after LIA_ normalization and investigate online orphan rows. Any Merchant execution requires a separate approved package with rollback.','approval_required_for_execution':True,'execution_not_included':True},'normalization_notes':['Local inventory IDs from Shopify POS/Local Inventory Ads use LIA_<sku>.','Cleanup preview strips LIA_ only for matching against Shopify/Data Spine; it does not modify Merchant IDs.','Previous raw orphan count should not be used for execution.'],'sample_rows':public_rows,'not_performed':['merchant_product_delete','merchant_product_update','datafeed_update','local_inventory_feed_change','shopify_write','campaign_send','external_contact']}
    OUT_JSON.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    with OUT_CSV.open('w',newline='',encoding='utf-8') as f:
        fields=['priority','product_id','offer_id','reconciliation_offer_id','channel','title','action','reason','has_online_counterpart','has_local_counterpart','matches_shopify_sku','matches_shopify_variant_id','approval_status']
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(public_rows)
    lines=['# LK GMC Catalog Cleanup Preview, 2026-05-12','','Status: `'+payload['status']+'`','','## Resumo']
    for k,v in payload['summary'].items(): lines.append(f'- {k}: {v}')
    lines += ['','## Melhor melhoria candidata','- A LK usa Local Listings/inventário local, então o canal `local` deve ser preservado.','- O preview agora normaliza `LIA_<sku>` para `<sku>` apenas para reconciliação contra Shopify/Data Spine.','- Alvo seguro agora: investigar somente locais que continuam sem match após essa normalização e online órfãos; execução exige aprovação específica e rollback.','','## Não executado']
    for n in payload['not_performed']: lines.append(f'- {n}')
    OUT_MD.write_text('\n'.join(lines)+'\n'); BRAIN_DOC.write_text(OUT_MD.read_text())
    print(json.dumps({'status':payload['status'],'summary':payload['summary']},ensure_ascii=False))
if __name__=='__main__': main()
