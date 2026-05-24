#!/usr/bin/env python3
"""Resumable exact-ID scale for LK GMC availability=in stock.

Avoids slow full Merchant list scans. For each candidate exact online product ID:
- products.get current resource;
- skip if already availability=in stock;
- save current resource to private rollback jsonl before write;
- products.insert/upsert with availability=in stock only;
- products.get verify;
- productstatuses.get verify that availability diagnostic is absent for that ID.
"""
from __future__ import annotations

import argparse, csv, importlib.util, json, os, pathlib, time, urllib.parse
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
EXECUTOR_PATH = ROOT / 'scripts/lk_gmc_p1_execute_availability_in_stock_policy_20260512.py'
INPUT_CSV = ROOT / 'reports/lk-gmc-2026-05-12-p1-availability-in-stock-policy-packet.csv'
RUN_STAMP = '2026-05-12-p1-availability-in-stock-policy-resumable-scale'
PUBLIC_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
PUBLIC_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
CONTROL = ROOT / 'areas/lk/projetos/lk-os-implementation-control.md'
INDEX = ROOT / 'empresa/rotinas/_index.md'
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
PROGRESS_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_progress')
PROGRESS_PATH = PROGRESS_DIR / f'lk-gmc-{RUN_STAMP}-progress.jsonl'
SUMMARY_PATH = PROGRESS_DIR / f'lk-gmc-{RUN_STAMP}-summary.json'
TARGET_VALUE = 'in stock'
REQ_CODES = {'item_missing_required_attribute', 'missing_item_attribute_for_product_type'}
NOT_PERFORMED = ['merchant_delete','merchant_price_title_link_image_update','tiny_call','tiny_write','shopify_write','feed_update_or_fetch','database_write','pos_write','campaign_or_external_send','sourcing_or_supplier_contact']


def utc_now(): return datetime.now(timezone.utc).isoformat()

def import_executor():
    spec=importlib.util.spec_from_file_location('availability_executor', EXECUTOR_PATH)
    mod=importlib.util.module_from_spec(spec); assert spec.loader is not None; spec.loader.exec_module(mod); return mod

def productstatus_url(mid: str, pid: str) -> str:
    return f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/productstatuses/{urllib.parse.quote(pid, safe="")}'

def get_status(exe, mid: str, pid: str, token: str) -> dict[str, Any]:
    return exe.request_json(productstatus_url(mid,pid), token=token)

def missing_availability(status: dict[str, Any]) -> bool:
    for issue in status.get('itemLevelIssues') or []:
        if issue.get('code') in REQ_CODES:
            attr=str(issue.get('attributeName') or '').strip().lower().replace('_',' ')
            if attr == 'availability': return True
    return False

def load_rows():
    with INPUT_CSV.open(newline='', encoding='utf-8') as f:
        rows=list(csv.DictReader(f))
    out=[]; seen=set()
    for r in rows:
        pid=r.get('product_id')
        if pid and pid not in seen and pid.startswith('online:'):
            seen.add(pid); out.append(r)
    return out

def load_done():
    done={}; counts=Counter()
    if PROGRESS_PATH.exists():
        for line in PROGRESS_PATH.read_text(encoding='utf-8').splitlines():
            if not line.strip(): continue
            try: item=json.loads(line)
            except Exception: continue
            pid=item.get('product_id')
            if pid: done[pid]=item; counts[item.get('status')]+=1
    return done, counts

def append_progress(item):
    PROGRESS_DIR.mkdir(parents=True, exist_ok=True); os.chmod(PROGRESS_DIR,0o700)
    with PROGRESS_PATH.open('a', encoding='utf-8') as f:
        os.chmod(PROGRESS_PATH,0o600)
        f.write(json.dumps(item,ensure_ascii=False)+'\n'); f.flush()

def write_rollback_record(batch_path: pathlib.Path, rec: dict[str, Any]):
    with batch_path.open('a', encoding='utf-8') as f:
        os.chmod(batch_path,0o600)
        f.write(json.dumps(rec,ensure_ascii=False)+'\n'); f.flush()

def write_report(rows, done, batch_reports, status):
    counts=Counter(item.get('status') for item in done.values())
    missing_status=sum(1 for item in done.values() if item.get('productstatus_missing_availability_after') is True)
    summary={
        'packet_rows': len(rows),
        'processed_unique': len(done),
        'counts': dict(counts),
        'success_or_already_in_stock': counts.get('updated_verified_in_stock',0)+counts.get('already_in_stock',0),
        'updated_verified_in_stock': counts.get('updated_verified_in_stock',0),
        'already_in_stock': counts.get('already_in_stock',0),
        'failed': counts.get('failed',0),
        'remaining_unprocessed': len(rows)-len(done),
        'productstatus_missing_availability_after_count': missing_status,
    }
    payload={'generated_at':utc_now(),'status':status,'approval_context':'Lucas chose option 1: scale in controlled batches after successful pilot 25.','summary':summary,'batches':batch_reports,'not_performed':NOT_PERFORMED,'progress_path':str(PROGRESS_PATH),'rollback_dir':str(PRIVATE_DIR)}
    PUBLIC_JSON.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    SUMMARY_PATH.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); os.chmod(SUMMARY_PATH,0o600)
    lines=['# LK GMC P1-B Availability In-Stock Policy Resumable Scale, 2026-05-12','',f"Status: `{status}`",'','## Resultado',f"- Packet rows: {summary['packet_rows']}",f"- Processados: {summary['processed_unique']}",f"- Success/already in stock: {summary['success_or_already_in_stock']}",f"- Atualizados e verificados: {summary['updated_verified_in_stock']}",f"- Já estavam in stock: {summary['already_in_stock']}",f"- Falhas: {summary['failed']}",f"- Restantes não processados: {summary['remaining_unprocessed']}",f"- Ainda com productstatus availability missing após processamento: {summary['productstatus_missing_availability_after_count']}",'','## Batches']
    for b in batch_reports[-20:]: lines.append(f"- Batch {b['batch_no']}: selected={b['selected']} updated={b['updated_verified_in_stock']} already={b['already_in_stock']} failed={b['failed']} rollback={b['rollback_path']}")
    lines += ['','## Não executado']+[f'- {n}' for n in NOT_PERFORMED]
    content='\n'.join(lines)+'\n'
    PUBLIC_MD.write_text(content,encoding='utf-8'); BRAIN_DOC.write_text(content,encoding='utf-8')
    if CONTROL.exists():
        marker='### 2026-05-12 — GMC P1-B availability in-stock policy resumable scale'
        text=CONTROL.read_text(encoding='utf-8')
        block=f"\n{marker}\n\n- Status: `{status}`.\n- Aprovação: opção 1, escala em lotes controlados.\n- Resultado atual: processed={summary['processed_unique']}; success_or_already={summary['success_or_already_in_stock']}; failed={summary['failed']}; remaining={summary['remaining_unprocessed']}.\n"
        if marker not in text: CONTROL.write_text(text.rstrip()+block+'\n',encoding='utf-8')
    if INDEX.exists():
        line=f'| LK GMC P1-B Availability In-Stock Policy Resumable Scale 2026-05-12 | `areas/lk/rotinas/gmc-{RUN_STAMP}.md` | Escala em lotes controlados/resumível: availability=in stock com rollback privado por lote e verificação exact-ID |'
        text=INDEX.read_text(encoding='utf-8')
        if line not in text: INDEX.write_text(text.rstrip()+'\n'+line+'\n',encoding='utf-8')
    return payload

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--batch-size',type=int,default=100); ap.add_argument('--max-batches',type=int,default=20); ap.add_argument('--sleep',type=float,default=0.1); args=ap.parse_args()
    exe=import_executor(); audit=exe.import_audit(); secrets=audit.load_doppler(); mid=secrets['MERCHANT_CENTER_ID_LK']; token=audit.google_access_token(audit.parse_service_account(secrets))
    rows=load_rows(); done,_=load_done(); batch_reports=[]
    for batch_no in range(1,args.max_batches+1):
        pending=[r for r in rows if r['product_id'] not in done]
        selected=pending[:args.batch_size]
        if not selected: break
        PRIVATE_DIR.mkdir(parents=True,exist_ok=True); os.chmod(PRIVATE_DIR,0o700)
        rollback_path=PRIVATE_DIR/f'lk-gmc-{RUN_STAMP}-batch-{batch_no:02d}-rollback-{datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")}.jsonl'
        bc=Counter(); selected_ids=[]
        for r in selected:
            pid=r['product_id']; selected_ids.append(pid)
            try:
                current=exe.get_product(mid,pid,token)
                if current.get('availability') == TARGET_VALUE:
                    try: st=get_status(exe,mid,pid,token); ps_missing=missing_availability(st)
                    except Exception: ps_missing=None
                    item={'ts':utc_now(),'product_id':pid,'status':'already_in_stock','availability_after_get':TARGET_VALUE,'productstatus_missing_availability_after':ps_missing}
                    append_progress(item); done[pid]=item; bc['already_in_stock']+=1; continue
                write_rollback_record(rollback_path, {'ts':utc_now(),'product_id':pid,'current_product_resource':current,'planned_update':{'availability':TARGET_VALUE}})
                updated=exe.upsert_product(mid, exe.prepare_updated_product(current), token)
                time.sleep(args.sleep)
                after=exe.get_product(mid,pid,token)
                try: st=get_status(exe,mid,pid,token); ps_missing=missing_availability(st)
                except Exception: ps_missing=None
                ok=after.get('availability')==TARGET_VALUE
                item={'ts':utc_now(),'product_id':pid,'status':'updated_verified_in_stock' if ok else 'failed','availability_after_response':updated.get('availability'),'availability_after_get':after.get('availability'),'productstatus_missing_availability_after':ps_missing}
                append_progress(item); done[pid]=item; bc[item['status']]+=1
            except Exception as e:
                item={'ts':utc_now(),'product_id':pid,'status':'failed','error':str(e)[:1200]}
                append_progress(item); done[pid]=item; bc['failed']+=1
                # fail-fast for HTTP/API validation errors; report and stop.
                batch_reports.append({'batch_no':batch_no,'selected':len(selected_ids),'updated_verified_in_stock':bc['updated_verified_in_stock'],'already_in_stock':bc['already_in_stock'],'failed':bc['failed'],'rollback_path':str(rollback_path)})
                payload=write_report(rows,done,batch_reports,'stopped_after_failure')
                print(json.dumps({'status':'stopped_after_failure','failed_pid':pid,'summary':payload['summary']},ensure_ascii=False), flush=True); return
        batch_reports.append({'batch_no':batch_no,'selected':len(selected),'updated_verified_in_stock':bc['updated_verified_in_stock'],'already_in_stock':bc['already_in_stock'],'failed':bc['failed'],'rollback_path':str(rollback_path)})
        payload=write_report(rows,done,batch_reports,'partial_running')
        print(json.dumps({'batch':batch_no, **batch_reports[-1], 'processed':payload['summary']['processed_unique'], 'remaining':payload['summary']['remaining_unprocessed']},ensure_ascii=False), flush=True)
    status='complete_verified' if len(done)>=len(rows) and not any(x.get('status')=='failed' for x in done.values()) else 'paused_after_batch_limit'
    payload=write_report(rows,done,batch_reports,status)
    print(json.dumps({'status':status,'summary':payload['summary'],'public_report':str(PUBLIC_MD)},ensure_ascii=False,indent=2), flush=True)

if __name__=='__main__': main()
