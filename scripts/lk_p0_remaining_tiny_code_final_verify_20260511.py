#!/usr/bin/env python3
import base64,json,pathlib,time,urllib.parse,urllib.request
from datetime import datetime, timezone
ROOT=pathlib.Path(__file__).resolve().parents[1]
OUT=ROOT/'reports/lk-p0-remaining-tiny-code-final-verification-2026-05-11.json'
EXPECTED={
 '1069545385':'NKE-9054174-41',
 '1070120736':'ONI-0995678-425',
 '1069544047':'NB-0254942-37',
 '1070119554':'ONI-6772830-38',
 '1069542767':'ALO-8506462-S',
 '1069544315':'SST-4542302-L',
 '1069930823':'PAC-1197278-S',
}
dt=pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token').read_text().strip()
req=urllib.request.Request('https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json')
req.add_header('Authorization','Basic '+base64.b64encode((dt+':').encode()).decode())
with urllib.request.urlopen(req,timeout=60) as resp: TOKEN=json.load(resp)['TINY_API_TOKEN']
def call(method, params):
 data=urllib.parse.urlencode({**params,'token':TOKEN,'formato':'json'}).encode(); req=urllib.request.Request(f'https://api.tiny.com.br/api2/{method}.php',data=data,method='POST')
 with urllib.request.urlopen(req,timeout=90) as r: return json.load(r)
def snap(p):
 return {k:p.get(k) for k in ['id','nome','codigo','preco','preco_promocional','unidade','origem','situacao','tipo','grade','idProdutoPai'] if k in p}
results=[]
for id,target in EXPECTED.items():
 time.sleep(5)
 ret=call('produto.obter', {'id':id}).get('retorno',{})
 p=ret.get('produto') or {}
 results.append({'tiny_child_id':id,'expected_codigo':target,'status':ret.get('status'),'snapshot':snap(p),'ok':ret.get('status')=='OK' and (p.get('codigo') or '')==target})
report={'generated_at':datetime.now(timezone.utc).isoformat(),'scope':'Final live Tiny read-back verification for 7 approved P0 codigo writes','counts':{'checked':len(results),'ok':sum(1 for r in results if r['ok']),'failed':sum(1 for r in results if not r['ok'])},'results':results}
OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'report':str(OUT),'counts':report['counts'],'failed':[r for r in results if not r['ok']]},ensure_ascii=False,indent=2))
