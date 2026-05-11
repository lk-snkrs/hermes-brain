#!/usr/bin/env python3
import base64,json,pathlib,time,urllib.parse,urllib.request
ids=['1069545385','1070120736','1069544047','1070119554','1069542767','1069544315','1069930823']
dt=pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token').read_text().strip()
req=urllib.request.Request('https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json')
req.add_header('Authorization','Basic '+base64.b64encode((dt+':').encode()).decode())
with urllib.request.urlopen(req,timeout=60) as resp: token=json.load(resp)['TINY_API_TOKEN']
def call(method, params):
    data=urllib.parse.urlencode({**params,'token':token,'formato':'json'}).encode()
    req=urllib.request.Request(f'https://api.tiny.com.br/api2/{method}.php',data=data,method='POST')
    with urllib.request.urlopen(req,timeout=90) as r: return json.load(r)
def obter(id):
    time.sleep(1.5)
    return call('produto.obter', {'id':id}).get('retorno',{})
out=[]
for id in ids:
    ret=obter(id); p=ret.get('produto') or {}; parent=p.get('idProdutoPai')
    rec={'id':id,'status':ret.get('status'),'nome':p.get('nome'),'codigo':p.get('codigo'),'idProdutoPai':parent,'child_keys':sorted(p.keys())}
    if parent:
        pret=obter(parent); pp=pret.get('produto') or {}
        hits=[]
        for w in pp.get('variacoes') or []:
            v=w.get('variacao') or {}
            if str(v.get('id'))==id:
                hits.append({k:v.get(k) for k in sorted(v.keys()) if k in ['id','sequencia','codigo','nome','grade','preco','preco_promocional','unidade','origem','situacao','tipo']})
        rec['parent_status']=pret.get('status'); rec['parent_nome']=pp.get('nome'); rec['parent_variation_hit']=hits
    out.append(rec)
print(json.dumps(out, ensure_ascii=False, indent=2))
