#!/usr/bin/env python3
"""Read-only Merchant Center datafeed source inventory for LK."""
from __future__ import annotations
import base64, json, pathlib, subprocess, tempfile, time, urllib.parse, urllib.request
from datetime import datetime, timezone
from typing import Any
ROOT=pathlib.Path(__file__).resolve().parents[1]
DOPPLER_TOKEN_FILE=pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
OUT_JSON=ROOT/'reports/lk-gmc-datafeed-source-inventory-2026-05-12.json'
OUT_MD=ROOT/'reports/lk-gmc-datafeed-source-inventory-2026-05-12.md'
BRAIN_DOC=ROOT/'areas/lk/rotinas/gmc-datafeed-source-inventory-2026-05-12.md'
SCOPE='https://www.googleapis.com/auth/content'

def b64url(b:bytes)->str: return base64.urlsafe_b64encode(b).decode().rstrip('=')
def doppler():
    token=DOPPLER_TOKEN_FILE.read_text().strip(); req=urllib.request.Request('https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json'); req.add_header('Authorization','Basic '+base64.b64encode((token+':').encode()).decode())
    return json.loads(urllib.request.urlopen(req,timeout=60).read().decode())
def gtoken(secrets):
    raw=secrets.get('GOOGLE_SERVICE_ACCOUNT_JSON') or secrets.get('GA4_LK_N8N_ZIPPER_SERVICE_ACCOUNT') or secrets.get('GA4_LK_SERVICE_ACCOUNT'); sa=json.loads(raw) if raw and raw.strip().startswith('{') else json.loads(base64.b64decode(raw or '').decode())
    now=int(time.time()); claim={'iss':sa['client_email'],'scope':SCOPE,'aud':sa.get('token_uri') or 'https://oauth2.googleapis.com/token','iat':now,'exp':now+3600}
    inp=b64url(json.dumps({'alg':'RS256','typ':'JWT'},separators=(',',':')).encode())+'.'+b64url(json.dumps(claim,separators=(',',':')).encode())
    with tempfile.NamedTemporaryFile('w',delete=False) as f: f.write(sa['private_key']); kp=f.name
    try: sig=subprocess.run(['openssl','dgst','-sha256','-sign',kp],input=inp.encode(),capture_output=True,check=True).stdout
    finally: pathlib.Path(kp).unlink(missing_ok=True)
    req=urllib.request.Request(sa.get('token_uri') or 'https://oauth2.googleapis.com/token',data=urllib.parse.urlencode({'grant_type':'urn:ietf:params:oauth:grant-type:jwt-bearer','assertion':inp+'.'+b64url(sig)}).encode(),method='POST'); req.add_header('Content-Type','application/x-www-form-urlencoded')
    return json.loads(urllib.request.urlopen(req,timeout=60).read().decode())['access_token']
def get(url,token):
    req=urllib.request.Request(url); req.add_header('Authorization','Bearer '+token)
    return json.loads(urllib.request.urlopen(req,timeout=120).read().decode())
def sanitize_feed(f):
    fs=f.get('fetchSchedule') or {}; fetch_url=fs.get('fetchUrl') or ''
    public_hint='gist' if 'gist' in fetch_url else ('shopify' if 'shopify' in fetch_url else ('google' if 'google' in fetch_url else ('other' if fetch_url else 'none')))
    return {k:f.get(k) for k in ['id','name','fileName','contentLanguage','targetCountry','attributeLanguage','intendedDestinations','targets','format','schedule'] } | {'fetch_url_kind':public_hint,'fetch_url_present':bool(fetch_url)}
def main():
    sec=doppler(); token=gtoken(sec); mid=sec['MERCHANT_CENTER_ID_LK']
    feeds=[]; pt=None
    while True:
        qs={'maxResults':'250'}
        if pt: qs['pageToken']=pt
        data=get(f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/datafeeds?'+urllib.parse.urlencode(qs),token)
        feeds += data.get('resources') or []
        pt=data.get('nextPageToken')
        if not pt: break
    sanitized=[sanitize_feed(f) for f in feeds]
    payload={'generated_at':datetime.now(timezone.utc).isoformat(),'scope':'LK GMC datafeed source inventory read-only','status':'gmc_datafeed_source_inventory_ready_readonly','datafeed_count':len(sanitized),'datafeeds':sanitized,'not_performed':['datafeed_update','feed_delete','merchant_product_delete','shopify_write','campaign_send']}
    OUT_JSON.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    lines=['# LK GMC Datafeed Source Inventory, 2026-05-12','','Status: `'+payload['status']+'`','',f"- datafeed_count: {len(sanitized)}",'']
    for f in sanitized:
        lines.append(f"- {f.get('id')} | {f.get('name')} | file={f.get('fileName')} | fetch_url_kind={f.get('fetch_url_kind')} | targets={f.get('targets')}")
    OUT_MD.write_text('\n'.join(lines)+'\n'); BRAIN_DOC.write_text(OUT_MD.read_text())
    print(json.dumps({'status':payload['status'],'datafeed_count':len(sanitized),'names':[f.get('name') for f in sanitized]},ensure_ascii=False))
if __name__=='__main__': main()
