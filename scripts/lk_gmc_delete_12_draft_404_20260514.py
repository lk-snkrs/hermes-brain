#!/usr/bin/env python3
from __future__ import annotations
import csv, importlib.util, json, os, pathlib, time, urllib.error, urllib.parse, urllib.request
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
AUDIT = ROOT/'scripts/lk_gmc_catalog_duplication_audit_20260512.py'
URL_PREVIEW = ROOT/'reports/lk-gmc-a-url-probe-landing-page-errors-2026-05-14.json'
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
RUN_STAMP = '2026-05-14-draft-404-merchant-delete'
OUT_JSON = ROOT/f'reports/lk-gmc-{RUN_STAMP}.json'
OUT_MD = ROOT/f'reports/lk-gmc-{RUN_STAMP}.md'
OUT_CSV = ROOT/f'reports/lk-gmc-{RUN_STAMP}.csv'


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()

def load_audit():
    spec = importlib.util.spec_from_file_location('audit', AUDIT)
    mod = importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(mod)
    return mod

def request_json(url: str, token: str, method='GET', attempts=5) -> dict[str,Any]:
    last=''
    for i in range(1, attempts+1):
        req=urllib.request.Request(url, method=method)
        req.add_header('Authorization','Bearer '+token)
        try:
            with urllib.request.urlopen(req, timeout=150) as r:
                raw=r.read().decode()
                return {'http_status': r.status, 'body': json.loads(raw) if raw else {}}
        except urllib.error.HTTPError as e:
            raw=e.read().decode(errors='replace')
            if method == 'DELETE' and e.code == 404:
                return {'http_status':404, 'body':{}, 'already_absent': True}
            last=f'http_{e.code}: {raw[:1000]}'
            if e.code not in {429,500,502,503,504} or i == attempts:
                raise RuntimeError(last) from e
        except Exception as e:
            last=str(e)[:1000]
            if i == attempts: raise RuntimeError(last) from e
        time.sleep(min(60,2**i))
    raise RuntimeError(last or 'request_failed')

def product_url(mid: str, pid: str) -> str:
    return f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/products/' + urllib.parse.quote(pid, safe='')

def status_url(mid: str, pid: str) -> str:
    return f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/productstatuses/' + urllib.parse.quote(pid, safe='')

def get_optional(url: str, token: str) -> dict[str,Any]|None:
    try:
        return request_json(url, token)['body']
    except RuntimeError as e:
        if str(e).startswith('http_404'):
            return None
        raise

def list_all(endpoint: str, mid: str, token: str) -> list[dict[str,Any]]:
    rows=[]; page=None
    while True:
        qs={'maxResults':'250'}
        if page: qs['pageToken']=page
        url=f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/{endpoint}?'+urllib.parse.urlencode(qs)
        data=request_json(url, token)['body']
        batch=data.get('resources') or []
        rows.extend(batch)
        page=data.get('nextPageToken')
        if not page or not batch: break
    return rows

def load_targets() -> list[dict[str,Any]]:
    data=json.loads(URL_PREVIEW.read_text())
    rows=data['rows']
    out=[]
    seen=set()
    for r in rows:
        pid=r['productId']
        if not pid.startswith('online:pt:BR:'):
            raise RuntimeError(f'blocked_non_online_target:{pid}')
        if pid in seen: continue
        seen.add(pid)
        probe=r.get('probe') or {}
        out.append({'product_id':pid,'title':r.get('title'),'link':r.get('link'),'probe_status':probe.get('status'),'http_code':probe.get('http_code'), 'issue':r.get('issue')})
    if len(out)!=12:
        raise RuntimeError(f'expected_12_targets_got_{len(out)}')
    return out

def write_outputs(payload: dict[str,Any]):
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2)+'\n')
    fields=['product_id','title','link','execution_status','delete_status','verified_absent_products_list','verified_absent_productstatuses_list','error']
    with OUT_CSV.open('w', newline='', encoding='utf-8') as f:
        w=csv.DictWriter(f, fieldnames=fields); w.writeheader()
        for r in payload['rows']:
            w.writerow({k:r.get(k) for k in fields})
    lines=['# LK GMC — Delete/Suppress 12 Shopify DRAFT 404 items, 2026-05-14','',f"Gerado em: `{payload['generated_at']}`",'', '## Resultado',
           f"- Status: `{payload['status']}`", f"- Escopo aprovado: opção 2 — remover/suprimir os 12 itens Merchant com landing page 404 porque Shopify está DRAFT.",
           f"- Targets: {payload['summary']['targets']}", f"- Deletes OK: {payload['summary'].get('delete_ok',0)}", f"- Já ausentes/404 idempotente: {payload['summary'].get('already_absent',0)}", f"- Verificados ausentes em products.list: {payload['summary'].get('verified_absent_products_list',0)}", f"- Verificados ausentes em productstatuses.list: {payload['summary'].get('verified_absent_productstatuses_list',0)}", f"- Falhas/anomalias: {payload['summary'].get('failed',0)+payload['summary'].get('verification_anomalies',0)}", '', '## Itens']
    for r in payload['rows']:
        lines.append(f"- `{r['product_id']}` — `{r.get('execution_status')}` — absent_products={r.get('verified_absent_products_list')} — absent_statuses={r.get('verified_absent_productstatuses_list')} — {r.get('title')}")
    lines += ['', '## Rollback', f"- Snapshot privado: `{payload['private_rollback_snapshot_path']}`", '- Para rollback, reinserir os recursos originais salvos no snapshot privado.', '', '## Não executado']
    for x in payload['not_performed']:
        lines.append(f'- {x}')
    OUT_MD.write_text('\n'.join(lines)+'\n')

def main():
    audit=load_audit(); secrets=audit.load_doppler(); mid=secrets['MERCHANT_CENTER_ID_LK']; token=audit.google_access_token(audit.parse_service_account(secrets))
    targets=load_targets()
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True); os.chmod(PRIVATE_DIR,0o700)
    rb=PRIVATE_DIR/f'lk-gmc-{RUN_STAMP}-rollback-{datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")}.json'
    records=[]
    for t in targets:
        prod=get_optional(product_url(mid,t['product_id']), token)
        st=get_optional(status_url(mid,t['product_id']), token)
        records.append({**t, 'current_product_resource': prod, 'current_product_status': st})
    rb.write_text(json.dumps({'generated_at':utc_now(),'scope':'delete exact 12 online Merchant products with Shopify DRAFT/landing_page_404','approval':'Lucas chose option 2 in Telegram','records':records}, ensure_ascii=False, indent=2)+'\n')
    os.chmod(rb,0o600)
    rows=[]; summary=Counter(targets=len(targets))
    for rec in records:
        row={k:rec.get(k) for k in ['product_id','title','link']}
        if not rec.get('current_product_resource'):
            row['execution_status']='already_absent_before_delete'; row['delete_status']='already_absent'; summary['already_absent']+=1
        else:
            try:
                res=request_json(product_url(mid,rec['product_id']), token, method='DELETE')
                if res.get('already_absent'):
                    row['execution_status']='already_absent_at_delete'; row['delete_status']='already_absent_404'; summary['already_absent']+=1
                else:
                    row['execution_status']='deleted_exact_product_id'; row['delete_status']='ok'; summary['delete_ok']+=1
            except Exception as e:
                row['execution_status']='delete_failed'; row['delete_status']='failed'; row['error']=str(e)[:800]; summary['failed']+=1
        rows.append(row); time.sleep(0.2)
    time.sleep(35)
    products=list_all('products', mid, token); statuses=list_all('productstatuses', mid, token)
    live_ids={p.get('id') for p in products}; status_ids={s.get('productId') for s in statuses}
    for row in rows:
        row['verified_absent_products_list']=row['product_id'] not in live_ids
        row['verified_absent_productstatuses_list']=row['product_id'] not in status_ids
        if row['verified_absent_products_list']: summary['verified_absent_products_list']+=1
        if row['verified_absent_productstatuses_list']: summary['verified_absent_productstatuses_list']+=1
        if not row['verified_absent_products_list'] or not row['verified_absent_productstatuses_list']:
            summary['verification_anomalies']+=1
    status='applied_verified_absent' if summary.get('verification_anomalies',0)==0 and summary.get('failed',0)==0 else 'applied_needs_review'
    payload={'generated_at':utc_now(),'status':status,'source_labels':['fact_merchant_center','fact_shopify_readonly','manual_approval_lucas_option_2'],'summary':dict(summary),'private_rollback_snapshot_path':str(rb),'rows':rows,'not_performed':['Shopify publish/write','Shopify redirect creation','feed upload/fetchNow','Tiny write','price/availability/title/category changes','campaign/message/WhatsApp/supplier contact']}
    write_outputs(payload)
    print(json.dumps({'status':status,'summary':dict(summary),'out_json':str(OUT_JSON),'out_md':str(OUT_MD),'rollback':str(rb)}, ensure_ascii=False))

if __name__=='__main__': main()
