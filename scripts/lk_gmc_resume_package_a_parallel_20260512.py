#!/usr/bin/env python3
"""Resume/verify LK GMC package A deletes in parallel after sequential canary run."""
from __future__ import annotations
import concurrent.futures, csv, importlib.util, json, os, pathlib, time, urllib.error, urllib.parse, urllib.request
from datetime import datetime, timezone
from typing import Any

ROOT=pathlib.Path(__file__).resolve().parents[1]
AUDIT_PATH=ROOT/'scripts/lk_gmc_catalog_duplication_audit_20260512.py'
SNAP=pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-executable-previews-rollback-2026-05-12.json')
PRIVATE_DIR=pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
RUN='2026-05-12-package-a-online-stale-triage'
PACKAGE='A_online_stale_triage'
PUBLIC_JSON=ROOT/f'reports/lk-gmc-{RUN}.json'
PUBLIC_CSV=ROOT/f'reports/lk-gmc-{RUN}.csv'
PUBLIC_MD=ROOT/f'reports/lk-gmc-{RUN}.md'
BRAIN=ROOT/f'areas/lk/rotinas/gmc-{RUN}.md'
CONTROL=ROOT/'areas/lk/projetos/lk-os-implementation-control.md'
INDEX=ROOT/'empresa/rotinas/_index.md'

def now(): return datetime.now(timezone.utc).isoformat()
def audit_mod():
    spec=importlib.util.spec_from_file_location('audit',AUDIT_PATH); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod

def delete_one(args):
    mid, token, row=args
    pid=row['product_id']
    url=f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/products/'+urllib.parse.quote(pid,safe='')
    req=urllib.request.Request(url,method='DELETE'); req.add_header('Authorization','Bearer '+token)
    out=dict(row); out['started_at']=now()
    try:
        with urllib.request.urlopen(req,timeout=120) as r:
            r.read(); out['delete_status']='ok'; out['execution_status']='applied_delete_exact_product_id'
    except urllib.error.HTTPError as e:
        if e.code==404:
            out['delete_status']='already_absent_404'; out['execution_status']='already_absent_before_delete'
        else:
            raw=e.read().decode(errors='replace'); out['delete_status']='failed'; out['execution_status']='failed_old_intact_or_unknown'; out['error_class']=f'http_{e.code}'; out['error_message']=raw[:500]
    except Exception as e:
        out['delete_status']='failed'; out['execution_status']='failed_old_intact_or_unknown'; out['error_class']=type(e).__name__; out['error_message']=str(e)[:500]
    out['finished_at']=now(); return out

def main():
    audit=audit_mod(); sec=audit.load_doppler(); mid=sec['MERCHANT_CENTER_ID_LK']; token=audit.google_access_token(audit.parse_service_account(sec))
    before=audit.list_all('products',mid,token); before_ids={p.get('id') for p in before}
    data=json.loads(SNAP.read_text(encoding='utf-8'))
    snap_rows=[r for r in data['records'] if r.get('package')==PACKAGE]
    plan=[]
    for rec in snap_rows:
        p=rec.get('merchant_product_resource') or {}; c=rec.get('classification') or {}; pid=p.get('id') or c.get('product_id')
        if p.get('channel')=='online' and str(pid).startswith('online:pt:BR:'):
            plan.append({'product_id':pid,'offer_id':p.get('offerId'),'title':p.get('title'),'priority':c.get('priority'),'bucket':c.get('bucket'),'rollback_original_product':p,'rollback_original_status':rec.get('merchant_product_status') or {}})
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as ex:
        results=list(ex.map(delete_one, [(mid,token,row) for row in plan]))
    time.sleep(30)
    after=audit.list_all('products',mid,token); after_ids={p.get('id') for p in after}
    for r in results: r['verified_absent_live']=r['product_id'] not in after_ids
    delete_ok=sum(1 for r in results if r.get('delete_status')=='ok')
    already=sum(1 for r in results if r.get('delete_status')=='already_absent_404')
    failed=sum(1 for r in results if r.get('delete_status')=='failed')
    verified=sum(1 for r in results if r.get('verified_absent_live'))
    anomalies=len(results)-verified
    PRIVATE_DIR.mkdir(parents=True,exist_ok=True); os.chmod(PRIVATE_DIR,0o700)
    private_path=PRIVATE_DIR/f'lk-gmc-{RUN}-rollback.json'
    private_path.write_text(json.dumps({'generated_at':now(),'scope':PACKAGE,'rollback_note':'Reinsert rollback_original_product if rollback is needed.','records':results},ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); os.chmod(private_path,0o600)
    summary={'mode':'apply_parallel_resume','merchant_products_before_read':len(before),'merchant_products_after_read':len(after),'snapshot_a_records':len(snap_rows),'planned':len(plan),'delete_ok':delete_ok,'already_absent':already,'failed':failed,'verified_absent_live':verified,'verification_anomalies':anomalies,'private_rollback_path':str(private_path)}
    public=[{k:r.get(k) for k in ['product_id','offer_id','title','priority','bucket','execution_status','delete_status','verified_absent_live','error_class']} for r in results]
    payload={'generated_at':now(),'status':'gmc_package_a_online_stale_triage_applied_verified' if anomalies==0 and failed==0 else 'gmc_package_a_online_stale_triage_applied_with_anomalies','scope':PACKAGE,'source_labels':['fact_merchant_center','derived_reconciliation','manual_approval_lucas_2026_05_12'],'summary':summary,'public_rows':public,'not_touched':['local_channel','shopify','feed','database','campaign_or_external_send','google_business_profile','pos_inventory']}
    PUBLIC_JSON.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    fields=['product_id','offer_id','title','priority','bucket','execution_status','delete_status','verified_absent_live','error_class']
    with PUBLIC_CSV.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(public)
    lines=['# LK GMC Package A Online Stale Triage, 2026-05-12','',f"Status: `{payload['status']}`",'','## Resumo executivo',f'- Pacote: `{PACKAGE}`','- Modo: `apply_parallel_resume`',f"- Registros A no snapshot: {len(snap_rows)}",f"- Product IDs processados: {len(plan)}",f"- Deletes Merchant OK nesta rodada: {delete_ok}",f"- Já ausentes/idempotentes: {already}",f"- Verificados ausentes no final: {verified}",f"- Falhas finais: {failed}",f"- Anomalias de verificação: {anomalies}",f"- Snapshot privado de rollback: `{private_path}`",'','## Interpretação','- Executei o pacote A por product IDs online exatos do bucket online_unmatched_possible_stale.','- Parte dos IDs já estava ausente por uma execução sequencial anterior que foi interrompida por timeout local; a verificação final cobre o estado live completo.','','## Não tocado']
    lines += [f'- {x}' for x in payload['not_touched']]
    lines += ['', '## Arquivos', f'- JSON: `{PUBLIC_JSON}`', f'- CSV: `{PUBLIC_CSV}`']
    PUBLIC_MD.write_text('\n'.join(lines)+'\n',encoding='utf-8'); BRAIN.write_text(PUBLIC_MD.read_text(encoding='utf-8'),encoding='utf-8')
    if CONTROL.exists():
        marker='### 2026-05-12 — GMC Package A online stale triage execution'
        text=CONTROL.read_text(encoding='utf-8')
        block=f"\n{marker}\n\n- Status: {payload['status']}.\n- Escopo aprovado por Lucas: `{PACKAGE}` online.\n- Product IDs processados={len(plan)}, deletes OK nesta rodada={delete_ok}, já ausentes={already}, verificados ausentes={verified}, falhas={failed}.\n- Snapshot privado de rollback: `{private_path}`.\n- Não tocado: local, Shopify, feed, banco, campanhas, GMB/POS.\n\n"
        if marker in text:
            import re; text=re.sub(r'\n### 2026-05-12 — GMC Package A online stale triage execution\n\n.*?(?=\n### |\Z)', block, text, flags=re.S)
            CONTROL.write_text(text.rstrip()+'\n',encoding='utf-8')
        else: CONTROL.write_text(text.rstrip()+block,encoding='utf-8')
    if INDEX.exists():
        line=f'| LK GMC Package A Online Stale Triage 2026-05-12 | `areas/lk/rotinas/gmc-{RUN}.md` | Execução controlada do pacote A online stale por product IDs exatos, rollback privado, sem tocar local/Shopify/feed/banco |'
        text=INDEX.read_text(encoding='utf-8')
        if line not in text: INDEX.write_text(text.rstrip()+'\n'+line+'\n',encoding='utf-8')
    print(json.dumps({'status':payload['status'],'summary':summary},ensure_ascii=False))
if __name__=='__main__': main()
