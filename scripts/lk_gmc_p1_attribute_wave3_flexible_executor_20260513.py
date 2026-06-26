#!/usr/bin/env python3
"""GMC P1 Wave3 flexible attribute executor after Lucas approved completeness > perfect fidelity.

Default dry-run. Uses Wave3 preview rows and applies only non-price, non-destructive
attribute completions with some evidence/default:
- color inferred from title or Shopify color tag
- ageGroup=adult / gender=unisex defaults
- sizes only when the preview already has a non-empty sizes suggestion

Excludes price. Apply requires exact approval text and writes private rollback
snapshots before any Merchant upsert.
"""
from __future__ import annotations

import argparse, csv, importlib.util, json, os, pathlib, time, urllib.error, urllib.parse, urllib.request
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / 'scripts/lk_gmc_catalog_duplication_audit_20260512.py'
PREVIEW_JSON = ROOT / 'reports/lk-gmc-2026-05-13-p1-attribute-remaining-wave3-preview.json'
RUN_STAMP = '2026-05-13-p1-attribute-wave3-flexible-executor'
PUBLIC_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
PUBLIC_CSV = ROOT / f'reports/lk-gmc-{RUN_STAMP}.csv'
PUBLIC_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
REQ_CODES = {'item_missing_required_attribute', 'missing_item_attribute_for_product_type'}
APPROVAL_TEXT_REQUIRED = 'Lucas approved GMC P1 Attribute Wave3 flexible non-price apply'
ALLOWED_DECISIONS = {
    'candidate_wave3_color_tag_high_confidence',
    'candidate_wave3_color_title_review',
    'candidate_wave3_size_age_gender_review',
    'candidate_wave3_mixed_review',
}
ALLOWED_FIELDS = {'color', 'sizes', 'ageGroup', 'gender'}


def utc_now() -> str: return datetime.now(timezone.utc).isoformat()

def import_audit():
    spec=importlib.util.spec_from_file_location('audit', AUDIT_PATH); mod=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(mod); return mod

def request_json(url: str, token: str, method: str='GET', payload: dict[str, Any] | None=None, max_attempts: int=6) -> dict[str, Any]:
    data=None if payload is None else json.dumps(payload, ensure_ascii=False).encode('utf-8')
    last=''
    for attempt in range(1, max_attempts+1):
        req=urllib.request.Request(url, data=data, method=method); req.add_header('Authorization','Bearer '+token)
        if payload is not None: req.add_header('Content-Type','application/json; charset=utf-8')
        try:
            with urllib.request.urlopen(req, timeout=150) as r:
                raw=r.read().decode(); return json.loads(raw) if raw else {}
        except urllib.error.HTTPError as e:
            raw=e.read().decode(errors='replace'); last=f'http_{e.code}: {raw[:1200]}'
            if e.code not in {429,500,502,503,504} or attempt==max_attempts: raise RuntimeError(last) from e
            time.sleep(min(90, 2**attempt))
        except Exception as e:
            last=str(e)[:1200]
            if attempt==max_attempts: raise RuntimeError(last) from e
            time.sleep(min(90, 2**attempt))
    raise RuntimeError(last or 'request_failed')

def list_all(endpoint: str, mid: str, token: str) -> list[dict[str, Any]]:
    rows=[]; page=None
    while True:
        qs={'maxResults':'250'}
        if page: qs['pageToken']=page
        url=f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/{endpoint}?'+urllib.parse.urlencode(qs)
        data=request_json(url, token)
        batch=data.get('resources') or []
        rows.extend(batch)
        page=data.get('nextPageToken')
        if not page or not batch: break
    return rows

def product_url(mid: str, pid: str) -> str:
    return f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/products/{urllib.parse.quote(pid, safe="")}'

def get_product(mid: str, pid: str, token: str) -> dict[str, Any]: return request_json(product_url(mid,pid), token)
def upsert_product(mid: str, product: dict[str, Any], token: str) -> dict[str, Any]: return request_json(f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/products', token=token, method='POST', payload=product)

def norm_attr(v: Any) -> str: return str(v or '').strip().lower().replace('_',' ')
def required_attrs(status: dict[str, Any] | None) -> set[str]:
    out=set()
    for issue in (status or {}).get('itemLevelIssues') or []:
        if issue.get('code') in REQ_CODES:
            a=norm_attr(issue.get('attributeName'))
            if a: out.add(a)
    return out

def norm_list(v: Any) -> list[str]:
    if v is None: return []
    if isinstance(v, list): return [str(x).strip() for x in v if str(x).strip()]
    t=str(v).strip(); return [t] if t else []

def load_preview_rows() -> list[dict[str, Any]]:
    data=json.loads(PREVIEW_JSON.read_text(encoding='utf-8'))
    rows=[r for r in data.get('rows') or [] if r.get('decision_state') in ALLOWED_DECISIONS]
    rows.sort(key=lambda r: (r.get('decision_state') or '', r.get('product_id') or ''))
    return rows

def sanitize_suggestions(raw: dict[str, Any], fresh: set[str], prod: dict[str, Any]) -> dict[str, Any]:
    out={}
    if 'color' in raw and 'color' in fresh and not prod.get('color') and raw.get('color'):
        out['color']=raw['color']
    if 'sizes' in raw and 'size' in fresh and not norm_list(prod.get('sizes')) and norm_list(raw.get('sizes')):
        out['sizes']=norm_list(raw.get('sizes'))
    if 'ageGroup' in raw and 'age group' in fresh and not prod.get('ageGroup') and raw.get('ageGroup'):
        out['ageGroup']=raw['ageGroup']
    if 'gender' in raw and 'gender' in fresh and not prod.get('gender') and raw.get('gender'):
        out['gender']=raw['gender']
    return out

def build_rows(candidates, products, statuses, limit):
    p_by_id={p.get('id'):p for p in products}; s_by_id={s.get('productId'):s for s in statuses}
    rows=[]; counters=Counter()
    for c in candidates:
        pid=c.get('product_id'); prod=p_by_id.get(pid); fresh=required_attrs(s_by_id.get(pid)); raw=c.get('suggested_attributes') or {}; evidence=c.get('evidence') or {}
        decision='ready_for_wave3_flexible_apply_if_lucas_approves'; reasons=[]; sugg={}
        if not prod:
            decision='blocked_product_not_currently_present'; reasons.append('fresh product missing')
        elif 'price' in fresh:
            decision='blocked_price_required_attr_present'; reasons.append('price is excluded from flexible non-price apply')
        else:
            sugg=sanitize_suggestions(raw, fresh, prod)
            if not sugg:
                decision='blocked_no_current_non_price_suggestion'; reasons.append('no non-price suggestion still needed')
            elif not set(sugg) <= ALLOWED_FIELDS:
                decision='blocked_field_outside_contract'; reasons.append('field outside allowed contract')
            else:
                reasons.append('Lucas approved completeness over perfect fidelity for non-critical attrs; suggestion has evidence/default')
        counters[decision]+=1
        rows.append({'product_id':pid,'merchant_title':prod.get('title') if prod else c.get('merchant_title'),'preview_decision_state':c.get('decision_state'),'fresh_required_attrs':sorted(fresh),'current_color':prod.get('color') if prod else None,'current_sizes':norm_list(prod.get('sizes')) if prod else [],'current_ageGroup':prod.get('ageGroup') if prod else None,'current_gender':prod.get('gender') if prod else None,'suggested_attributes':sugg,'evidence':evidence,'decision_state':decision,'decision_reasons':reasons,'selected_for_apply':False,'write_scope_if_approved':'non-price attrs only: color/sizes/ageGroup/gender, preserving current product resource','rollback_required_before_write':True})
    ready=[r for r in rows if r['decision_state']=='ready_for_wave3_flexible_apply_if_lucas_approves']
    selected={r['product_id'] for r in ready[:limit]}
    for r in rows: r['selected_for_apply']=r['product_id'] in selected
    return rows, {'preview_candidates':len(candidates),'fresh_merchant_products_current':len(products),'fresh_merchant_productstatuses_current':len(statuses),'decision_state_counts':dict(counters),'ready_total':len(ready),'selected_for_apply_if_approved':len(selected),'target_fields':['color','sizes','ageGroup','gender'],'limit':limit,'write_allowed_now':0}

def prepare_product(cur, row):
    out=json.loads(json.dumps(cur, ensure_ascii=False))
    for k in ['id','kind','source']: out.pop(k, None)
    for k,v in row['suggested_attributes'].items(): out[k]=v
    return out

def snapshot(records, limit):
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True); os.chmod(PRIVATE_DIR,0o700)
    path=PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-rollback-{datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")}.json'
    path.write_text(json.dumps({'generated_at':utc_now(),'scope':f'Wave3 flexible non-price apply limit={limit}; update only suggested color/sizes/ageGroup/gender','approval_text_required':APPROVAL_TEXT_REQUIRED,'rollback_instruction':'Use products.insert/upsert with current_product_resource; verify after delay.','records':records},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    os.chmod(path,0o600); return path

def apply_selected(mid, token, rows, products, limit):
    cur={p.get('id'):p for p in products}; records=[]
    for r in [x for x in rows if x.get('selected_for_apply')]:
        if not cur.get(r['product_id']): raise RuntimeError('pre_apply_current_resource_missing: '+str(r['product_id']))
        records.append({'product_id':r['product_id'],'current_product_resource':cur[r['product_id']],'planned_update':r})
    rollback=snapshot(records, limit); results=[]; progress=PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-progress-{rollback.stem.rsplit("-",1)[-1]}.jsonl'
    with progress.open('w', encoding='utf-8') as f:
        os.chmod(progress,0o600)
        for rec in records:
            r=rec['planned_update']
            try:
                updated=upsert_product(mid, prepare_product(rec['current_product_resource'], r), token)
                item={'product_id':r['product_id'],'execution_status':'updated_wave3_flexible_attrs','fields':sorted(r['suggested_attributes'].keys())}
            except Exception as e:
                item={'product_id':r['product_id'],'execution_status':'failed_http_or_validation','error':str(e)[:1200]}; results.append(item); f.write(json.dumps(item,ensure_ascii=False)+'\n'); f.flush(); break
            results.append(item); f.write(json.dumps(item,ensure_ascii=False)+'\n'); f.flush(); time.sleep(0.2)
    return results, rollback

def verify(mid, token, rows, results, delay):
    if delay: time.sleep(delay)
    byid={r['product_id']:r for r in rows}; out=[]
    for res in results:
        pid=res.get('product_id'); r=byid.get(pid,{})
        if res.get('execution_status')!='updated_wave3_flexible_attrs' or not pid: out.append({**res,'verify_status':'not_verified_due_to_execution_status'}); continue
        try:
            prod=get_product(mid,pid,token); ok=True; actual={}
            for k,v in (r.get('suggested_attributes') or {}).items():
                av=norm_list(prod.get(k)) if k=='sizes' else prod.get(k); actual[k]=av; ok = ok and (av==v)
            out.append({**res,'verify_status':'verified_product_get','actual_attrs':actual,'attrs_match_expected':ok})
        except Exception as e: out.append({**res,'verify_status':'verify_failed','verify_error':str(e)[:1200]})
    return out

def write_outputs(mode, summary, rows, exec_results, verified, rollback):
    ec=Counter(r.get('execution_status') for r in exec_results); vc=Counter(r.get('verify_status') for r in verified); matched=sum(1 for r in verified if r.get('attrs_match_expected'))
    payload={'generated_at':utc_now(),'status':'gmc_p1_attribute_wave3_flexible_apply_verified' if mode=='apply' else 'gmc_p1_attribute_wave3_flexible_dry_run_ready','mode':mode,'scope':'Wave3 flexible non-price attrs after Lucas approval: color/sizes/ageGroup/gender only; price excluded.','source_labels':['fact_merchant_center','fact_shopify_local_snapshot','derived_reconciliation','manual_approval'],'approval_required_for_apply':APPROVAL_TEXT_REQUIRED,'summary':{**summary,'execution_results_summary':dict(ec),'verify_results_summary':dict(vc),'verified_attrs_match_expected':matched},'private_rollback_snapshot_path':str(rollback) if rollback else None,'public_rows':rows,'execution_results':exec_results,'verified_results':verified,'not_performed':['merchant_write' if mode!='apply' else 'merchant_delete','merchant_delete','merchant_price_update','merchant_title_link_image_availability_update','feed_update_or_fetch','shopify_write','tiny_call_or_write','database_write','pos_or_local_inventory_write','klaviyo_or_whatsapp_send','notion_or_n8n_write','loyalty_or_judgeme_action']}
    PUBLIC_JSON.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    fields=['product_id','merchant_title','preview_decision_state','fresh_required_attrs','suggested_attributes','evidence','decision_state','selected_for_apply','decision_reasons']
    with PUBLIC_CSV.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore'); w.writeheader()
        for r in rows:
            o={k:r.get(k) for k in fields}; o['fresh_required_attrs']='; '.join(o.get('fresh_required_attrs') or []); o['suggested_attributes']=json.dumps(o.get('suggested_attributes') or {},ensure_ascii=False); o['evidence']=json.dumps(o.get('evidence') or {},ensure_ascii=False); o['decision_reasons']='; '.join(o.get('decision_reasons') or []); w.writerow(o)
    lines=['# LK GMC P1 Attribute Completion — Wave3 Flexible Executor, 2026-05-13','',f"Status: `{payload['status']}`",'','## Escopo',f'- Modo: `{mode}`','- Campos permitidos: `color`, `sizes`, `ageGroup`, `gender`.','- Excluído: `price`.','- Critério Lucas: completude para ranking > fidelidade perfeita em atributos não críticos.','','## Resultado',f"- Preview candidates: {summary['preview_candidates']}",f"- Ready: {summary['ready_total']}",f"- Selecionados: {summary['selected_for_apply_if_approved']}",'','## Estados']
    for k,v in sorted(summary['decision_state_counts'].items()): lines.append(f'- {k}: {v}')
    lines.extend(['','## Execução/verificação',f"- Execution: {dict(ec)}",f"- Verify: {dict(vc)}",f"- Match esperado: {matched}/{len(verified)}",'','## Rollback privado',f'- `{rollback}`' if rollback else '- Não criado no dry-run.','','## Não executado'])
    for n in payload['not_performed']: lines.append(f'- {n}')
    PUBLIC_MD.write_text('\n'.join(lines)+'\n',encoding='utf-8'); BRAIN_DOC.write_text(PUBLIC_MD.read_text(encoding='utf-8'),encoding='utf-8')
    print(json.dumps({'status':payload['status'],'mode':mode,'summary':payload['summary'],'public_report':str(PUBLIC_MD),'private_rollback_snapshot_path':str(rollback) if rollback else None},ensure_ascii=False,indent=2))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--apply',action='store_true'); ap.add_argument('--approval-text',default=''); ap.add_argument('--limit',type=int,default=1000); ap.add_argument('--verify-delay',type=int,default=90); args=ap.parse_args()
    mode='apply' if args.apply else 'dry-run'
    if args.apply and args.approval_text != APPROVAL_TEXT_REQUIRED: raise RuntimeError(f'apply_blocked_missing_exact_approval_text: {APPROVAL_TEXT_REQUIRED}')
    audit=import_audit(); secrets=audit.load_doppler(); mid=secrets.get('MERCHANT_CENTER_ID_LK')
    if not mid: raise RuntimeError('missing_merchant_center_id')
    token=audit.google_access_token(audit.parse_service_account(secrets)); products=list_all('products',mid,token); statuses=list_all('productstatuses',mid,token)
    rows,summary=build_rows(load_preview_rows(),products,statuses,args.limit)
    exec_results=[]; verified=[]; rollback=None
    if mode=='apply': exec_results, rollback=apply_selected(mid,token,rows,products,args.limit); verified=verify(mid,token,rows,exec_results,args.verify_delay)
    write_outputs(mode,summary,rows,exec_results,verified,rollback)

if __name__=='__main__': main()
