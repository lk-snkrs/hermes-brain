#!/usr/bin/env python3
"""Fast resumable scale for approved LK GMC availability=in stock.

Uses products.get and products.insert/upsert only per exact ID, with rollback jsonl
before writes and post-batch products.get verification. Avoids per-ID
productstatuses checks during the write path; final productstatus audit can be run
separately if needed.
"""
from __future__ import annotations
import argparse,csv,importlib.util,json,os,pathlib,time
from collections import Counter
from datetime import datetime,timezone
from typing import Any
ROOT=pathlib.Path(__file__).resolve().parents[1]
EXECUTOR_PATH=ROOT/'scripts/lk_gmc_p1_execute_availability_in_stock_policy_20260512.py'
INPUT_CSV=ROOT/'reports/lk-gmc-2026-05-12-p1-availability-in-stock-policy-packet.csv'
RUN_STAMP='2026-05-12-p1-availability-in-stock-policy-fast-scale'
PUBLIC_JSON=ROOT/f'reports/lk-gmc-{RUN_STAMP}.json'; PUBLIC_MD=ROOT/f'reports/lk-gmc-{RUN_STAMP}.md'; BRAIN_DOC=ROOT/f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
CONTROL=ROOT/'areas/lk/projetos/lk-os-implementation-control.md'; INDEX=ROOT/'empresa/rotinas/_index.md'
PRIVATE_DIR=pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots'); PROGRESS_DIR=pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_progress')
PROGRESS_PATH=PROGRESS_DIR/f'lk-gmc-{RUN_STAMP}-progress.jsonl'; TARGET='in stock'
NOT=['merchant_delete','merchant_price_title_link_image_update','tiny_call','tiny_write','shopify_write','feed_update_or_fetch','database_write','pos_write','campaign_or_external_send','sourcing_or_supplier_contact']
def now(): return datetime.now(timezone.utc).isoformat()
def imp():
 spec=importlib.util.spec_from_file_location('exe',EXECUTOR_PATH); m=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(m); return m
def rows():
 with INPUT_CSV.open(newline='',encoding='utf-8') as f: rr=list(csv.DictReader(f))
 seen=set(); out=[]
 for r in rr:
  pid=r.get('product_id')
  if pid and pid.startswith('online:') and pid not in seen: seen.add(pid); out.append(r)
 return out
def done():
 d={}
 # merge pilot/resumable/fast progress knowledge: if product was processed successfully in any local progress report, don't reprocess unless current get says not in stock in a future audit.
 for p in [PROGRESS_PATH, pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_progress/lk-gmc-2026-05-12-p1-availability-in-stock-policy-resumable-scale-progress.jsonl')]:
  if p.exists():
   for line in p.read_text(encoding='utf-8').splitlines():
    if not line.strip(): continue
    try: it=json.loads(line)
    except Exception: continue
    if it.get('product_id') and it.get('status') in ('updated_verified_in_stock','already_in_stock'): d[it['product_id']]=it
 return d
def app(it):
 PROGRESS_DIR.mkdir(parents=True,exist_ok=True); os.chmod(PROGRESS_DIR,0o700)
 with PROGRESS_PATH.open('a',encoding='utf-8') as f: os.chmod(PROGRESS_PATH,0o600); f.write(json.dumps(it,ensure_ascii=False)+'\n'); f.flush()
def rb_write(path,rec):
 with path.open('a',encoding='utf-8') as f: os.chmod(path,0o600); f.write(json.dumps(rec,ensure_ascii=False)+'\n'); f.flush()
def report(allrows,d,batches,status):
 c=Counter(x.get('status') for x in d.values()); summary={'packet_rows':len(allrows),'processed_unique':len(d),'success_or_already_in_stock':c['updated_verified_in_stock']+c['already_in_stock'],'updated_verified_in_stock':c['updated_verified_in_stock'],'already_in_stock':c['already_in_stock'],'failed':c['failed'],'remaining_unprocessed':len(allrows)-len(d),'counts':dict(c)}
 payload={'generated_at':now(),'status':status,'approval_context':'Lucas option 1: scale in controlled batches after successful pilot.','summary':summary,'batches':batches,'not_performed':NOT,'progress_path':str(PROGRESS_PATH)}
 PUBLIC_JSON.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 lines=['# LK GMC P1-B Availability In-Stock Policy Fast Scale, 2026-05-12','',f"Status: `{status}`",'','## Resultado',f"- Packet rows: {summary['packet_rows']}",f"- Processados: {summary['processed_unique']}",f"- Success/already in stock: {summary['success_or_already_in_stock']}",f"- Atualizados/verificados: {summary['updated_verified_in_stock']}",f"- Já estavam in stock: {summary['already_in_stock']}",f"- Falhas: {summary['failed']}",f"- Restantes: {summary['remaining_unprocessed']}",'','## Lotes']
 for b in batches[-20:]: lines.append(f"- Batch {b['batch_no']}: selected={b['selected']} updated={b['updated_verified_in_stock']} already={b['already_in_stock']} failed={b['failed']} rollback={b['rollback_path']}")
 lines += ['','## Não executado']+[f'- {n}' for n in NOT]
 content='\n'.join(lines)+'\n'; PUBLIC_MD.write_text(content,encoding='utf-8'); BRAIN_DOC.write_text(content,encoding='utf-8')
 if CONTROL.exists():
  marker='### 2026-05-12 — GMC P1-B availability in-stock policy fast scale'
  text=CONTROL.read_text(encoding='utf-8'); block=f"\n{marker}\n\n- Status: `{status}`.\n- Aprovação: opção 1, escala em lotes controlados.\n- Resultado: processed={summary['processed_unique']}; success_or_already={summary['success_or_already_in_stock']}; failed={summary['failed']}; remaining={summary['remaining_unprocessed']}.\n"
  if marker not in text: CONTROL.write_text(text.rstrip()+block+'\n',encoding='utf-8')
 if INDEX.exists():
  line=f'| LK GMC P1-B Availability In-Stock Policy Fast Scale 2026-05-12 | `areas/lk/rotinas/gmc-{RUN_STAMP}.md` | Escala aprovada em lotes controlados: availability=in stock, rollback privado por lote, products.get verification |'
  text=INDEX.read_text(encoding='utf-8')
  if line not in text: INDEX.write_text(text.rstrip()+'\n'+line+'\n',encoding='utf-8')
 return payload
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--batch-size',type=int,default=250); ap.add_argument('--max-batches',type=int,default=20); ap.add_argument('--sleep',type=float,default=0.02); ap.add_argument('--verify-delay',type=int,default=15); args=ap.parse_args()
 exe=imp(); au=exe.import_audit(); sec=au.load_doppler(); mid=sec['MERCHANT_CENTER_ID_LK']; tok=au.google_access_token(au.parse_service_account(sec)); allr=rows(); d=done(); batches=[]
 for bn in range(1,args.max_batches+1):
  pending=[r for r in allr if r['product_id'] not in d]
  sel=pending[:args.batch_size]
  if not sel: break
  PRIVATE_DIR.mkdir(parents=True,exist_ok=True); os.chmod(PRIVATE_DIR,0o700); rb=PRIVATE_DIR/f'lk-gmc-{RUN_STAMP}-batch-{bn:02d}-rollback-{datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")}.jsonl'
  bc=Counter(); written=[]
  for r in sel:
   pid=r['product_id']
   try:
    cur=exe.get_product(mid,pid,tok)
    if cur.get('availability')==TARGET:
     it={'ts':now(),'product_id':pid,'status':'already_in_stock','availability_after_get':TARGET}; app(it); d[pid]=it; bc['already_in_stock']+=1; continue
    rb_write(rb,{'ts':now(),'product_id':pid,'current_product_resource':cur,'planned_update':{'availability':TARGET}})
    exe.upsert_product(mid,exe.prepare_updated_product(cur),tok); written.append(pid); time.sleep(args.sleep)
   except Exception as e:
    it={'ts':now(),'product_id':pid,'status':'failed','error':str(e)[:1200]}; app(it); d[pid]=it; bc['failed']+=1; break
  if written: time.sleep(args.verify_delay)
  for pid in written:
   try:
    after=exe.get_product(mid,pid,tok); ok=after.get('availability')==TARGET
    it={'ts':now(),'product_id':pid,'status':'updated_verified_in_stock' if ok else 'failed','availability_after_get':after.get('availability')}
   except Exception as e: it={'ts':now(),'product_id':pid,'status':'failed','error':str(e)[:1200]}
   app(it); d[pid]=it; bc[it['status']]+=1
  batches.append({'batch_no':bn,'selected':len(sel),'updated_verified_in_stock':bc['updated_verified_in_stock'],'already_in_stock':bc['already_in_stock'],'failed':bc['failed'],'rollback_path':str(rb)})
  payload=report(allr,d,batches,'partial_running')
  print(json.dumps({'batch':bn,**batches[-1],'processed':payload['summary']['processed_unique'],'remaining':payload['summary']['remaining_unprocessed']},ensure_ascii=False),flush=True)
  if bc['failed']: break
 status='complete_verified' if len(d)>=len(allr) and not any(x.get('status')=='failed' for x in d.values()) else 'paused_after_batch_limit_or_failure'
 payload=report(allr,d,batches,status); print(json.dumps({'status':status,'summary':payload['summary'],'public_report':str(PUBLIC_MD)},ensure_ascii=False,indent=2),flush=True)
if __name__=='__main__': main()
