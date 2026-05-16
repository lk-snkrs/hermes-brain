#!/usr/bin/env python3
"""LK GMC P1 attribute completion Onda 2 pilot executor/dry-run.

Default is dry-run. Selects a conservative pilot from current Onda 2 review
candidates: exact online product IDs, fresh required-attribute diagnostics still
present, no existing conflicting size/age/gender, and suggested attributes
limited to sizes + ageGroup=adult + gender=unisex.

Apply is blocked unless --apply and exact approval text are provided. On apply,
rollback snapshots are written privately before any Merchant upsert.
"""
from __future__ import annotations

import argparse, csv, importlib.util, json, os, pathlib, time, urllib.error, urllib.parse, urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / 'scripts/lk_gmc_catalog_duplication_audit_20260512.py'
PACKET_JSON = ROOT / 'reports/lk-gmc-p1-attribute-completion-packet-v2-2026-05-13.json'
RUN_STAMP = '2026-05-13-p1-attribute-completion-wave2-pilot-executor'
PUBLIC_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
PUBLIC_CSV = ROOT / f'reports/lk-gmc-{RUN_STAMP}.csv'
PUBLIC_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
CONTROL = ROOT / 'areas/lk/projetos/lk-os-implementation-control.md'
INDEX = ROOT / 'empresa/rotinas/_index.md'
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
REQ_CODES = {'item_missing_required_attribute', 'missing_item_attribute_for_product_type'}
WAVE2_STATE = 'candidate_medium_confidence_attr_preview_needs_review'
APPROVAL_TEXT_REQUIRED = 'Lucas approved GMC P1 Attribute Wave2 pilot apply'


def utc_now() -> str: return datetime.now(timezone.utc).isoformat()

def import_audit():
    spec=importlib.util.spec_from_file_location('audit', AUDIT_PATH); mod=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(mod); return mod

def request_json(url: str, token: str, method: str='GET', payload: dict[str, Any] | None=None, max_attempts: int=5) -> dict[str, Any]:
    data=None if payload is None else json.dumps(payload, ensure_ascii=False).encode()
    last=''
    for attempt in range(1,max_attempts+1):
        req=urllib.request.Request(url, data=data, method=method); req.add_header('Authorization','Bearer '+token)
        if payload is not None: req.add_header('Content-Type','application/json; charset=utf-8')
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                raw=r.read().decode(); return json.loads(raw) if raw else {}
        except urllib.error.HTTPError as e:
            raw=e.read().decode(errors='replace'); last=f'http_{e.code}: {raw[:1200]}'
            if e.code not in {429,500,502,503,504} or attempt==max_attempts: raise RuntimeError(last) from e
            time.sleep(min(60,2**attempt))
        except Exception as e:
            last=str(e)[:1200]
            if attempt==max_attempts: raise RuntimeError(last) from e
            time.sleep(min(60,2**attempt))
    raise RuntimeError(last or 'request_failed')

def product_url(mid: str, pid: str) -> str:
    return f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/products/{urllib.parse.quote(pid, safe="")}'

def get_product(mid: str, pid: str, token: str) -> dict[str, Any]: return request_json(product_url(mid,pid), token=token)
def upsert_product(mid: str, product: dict[str, Any], token: str) -> dict[str, Any]: return request_json(f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/products', token=token, method='POST', payload=product)
def channel(pid: str) -> str: return (pid or '').split(':',1)[0] if ':' in (pid or '') else 'unknown'

def missing_required_attrs(status: dict[str, Any]) -> set[str]:
    out=set()
    for issue in status.get('itemLevelIssues') or []:
        if issue.get('code') in REQ_CODES:
            attr=str(issue.get('attributeName') or '').strip().lower().replace('_',' ')
            if attr: out.add(attr)
    return out

def norm_list(v: Any) -> list[str]:
    if v is None: return []
    if isinstance(v,list): return [str(x).strip() for x in v if str(x).strip()]
    t=str(v).strip(); return [t] if t else []

def load_wave2() -> list[dict[str, Any]]:
    data=json.loads(PACKET_JSON.read_text(encoding='utf-8'))
    rows=[r for r in data.get('candidates') or [] if r.get('decision_state')==WAVE2_STATE]
    rows.sort(key=lambda r: ((r.get('merchant_title') or '').lower(), r.get('product_id') or ''))
    return rows

def build_rows(candidates: list[dict[str, Any]], products: list[dict[str, Any]], statuses: list[dict[str, Any]], limit: int) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    p_by_id={p.get('id'):p for p in products}; s_by_id={s.get('productId'):s for s in statuses}
    rows=[]; counters=Counter(); seen=set()
    for c in candidates:
        pid=c.get('product_id') or ''
        if pid in seen: counters['blocked_duplicate_candidate_id']+=1; continue
        seen.add(pid); prod=p_by_id.get(pid); stat=s_by_id.get(pid) or {}; fresh=missing_required_attrs(stat)
        sugg=c.get('suggested_attributes') or {}; sugg_sizes=norm_list(sugg.get('sizes'))
        current_sizes=norm_list(prod.get('sizes')) if prod else []
        current_age=prod.get('ageGroup') if prod else None; current_gender=prod.get('gender') if prod else None
        expected_missing=set(c.get('missing_attributes') or [])
        reasons=[]
        if channel(pid)!='online': decision='blocked_non_online'; reasons.append('not online')
        elif not prod: decision='blocked_not_currently_present'; reasons.append('fresh product missing')
        elif not ({'age group','gender','size'} & fresh): decision='skipped_not_freshly_missing_target_attrs'; reasons.append('fresh status does not currently flag target attrs')
        elif expected_missing - {'age group','gender','size'}: decision='blocked_packet_has_extra_attrs'; reasons.append('packet includes non pilot attrs')
        elif set(sugg.keys()) != {'sizes','ageGroup','gender'}: decision='blocked_suggestion_not_exact_3field'; reasons.append('suggested fields outside pilot contract')
        elif not sugg_sizes: decision='blocked_missing_suggested_size'; reasons.append('no suggested size')
        elif sugg.get('ageGroup')!='adult' or sugg.get('gender')!='unisex': decision='blocked_non_default_age_gender'; reasons.append('not adult/unisex default')
        elif current_sizes and current_sizes != sugg_sizes: decision='blocked_existing_size_conflict'; reasons.append('existing sizes conflict')
        elif current_age and current_age != 'adult': decision='blocked_existing_age_conflict'; reasons.append('existing ageGroup conflict')
        elif current_gender and current_gender != 'unisex': decision='blocked_existing_gender_conflict'; reasons.append('existing gender conflict')
        elif current_sizes == sugg_sizes and current_age == 'adult' and current_gender == 'unisex': decision='skipped_already_has_expected_attrs'; reasons.append('product already has expected size/adult/unisex attrs')
        else: decision='ready_for_wave2_pilot_apply_if_lucas_approves'; reasons.append('fresh missing attrs + exact adult/unisex/size suggestion')
        counters[decision]+=1
        rows.append({'product_id':pid,'offer_id':c.get('offer_id'),'merchant_title':prod.get('title') if prod else c.get('merchant_title'),'shopify_product_title':c.get('shopify_product_title'),'shopify_variant_title':c.get('shopify_variant_title'),'fresh_missing_required_attrs':sorted(fresh),'packet_missing_attributes':c.get('missing_attributes') or [],'current_sizes':current_sizes,'current_age_group':current_age,'current_gender':current_gender,'suggested_sizes':sugg_sizes,'suggested_age_group':sugg.get('ageGroup'),'suggested_gender':sugg.get('gender'),'decision_state':decision,'decision_reasons':reasons,'selected_for_apply':False,'write_scope_if_approved':'sizes + ageGroup + gender only, exact online Merchant product resource, products.insert upsert','rollback_required_before_write':True})
    ready=[r for r in rows if r['decision_state']=='ready_for_wave2_pilot_apply_if_lucas_approves']
    # Deterministic diverse selection by product-title family first, then fill.
    byfam=defaultdict(list)
    for r in ready:
        fam=' '.join((r.get('merchant_title') or '').split()[:5]).lower() or 'unknown'; byfam[fam].append(r)
    selected=[]; selected_ids=set()
    for fam in sorted(byfam):
        if len(selected)>=limit: break
        item=sorted(byfam[fam], key=lambda x:x.get('product_id') or '')[0]
        selected.append(item); selected_ids.add(item['product_id'])
    for r in ready:
        if len(selected)>=limit: break
        if r['product_id'] not in selected_ids:
            selected.append(r); selected_ids.add(r['product_id'])
    for r in rows: r['selected_for_apply']=r['product_id'] in selected_ids
    summary={'wave2_packet_rows':len(candidates),'fresh_merchant_products_current':len(products),'fresh_merchant_productstatuses_current':len(statuses),'decision_state_counts':dict(counters),'ready_total':len(ready),'selected_for_apply_if_approved':len(selected_ids),'target_fields':['sizes','ageGroup','gender'],'limit':limit,'write_allowed_now':0}
    return rows, summary

def prepare_product(current: dict[str, Any], r: dict[str, Any]) -> dict[str, Any]:
    out=json.loads(json.dumps(current, ensure_ascii=False))
    for k in ['id','kind','source']: out.pop(k, None)
    out['sizes']=r['suggested_sizes']; out['ageGroup']=r['suggested_age_group']; out['gender']=r['suggested_gender']
    return out

def write_snapshot(records: list[dict[str, Any]], limit: int) -> pathlib.Path:
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True); os.chmod(PRIVATE_DIR,0o700)
    path=PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-rollback-{datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")}.json'
    path.write_text(json.dumps({'generated_at':utc_now(),'scope':f'Wave2 pilot apply limit={limit}; update sizes+ageGroup+gender only','approval_text_required':APPROVAL_TEXT_REQUIRED,'rollback_instruction':'Use products.insert/upsert with current_product_resource; verify after delay.','records':records}, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    os.chmod(path,0o600); return path

def apply_selected(mid: str, token: str, rows: list[dict[str, Any]], products: list[dict[str, Any]], limit: int) -> tuple[list[dict[str, Any]], pathlib.Path]:
    current={p.get('id'):p for p in products}; selected=[r for r in rows if r.get('selected_for_apply')]
    records=[]
    for r in selected:
        cur=current.get(r['product_id'])
        if not cur or cur.get('id')!=r['product_id']: raise RuntimeError('pre_apply_current_resource_missing: '+r['product_id'])
        records.append({'product_id':r['product_id'],'current_product_resource':cur,'planned_update':r})
    rollback=write_snapshot(records, limit)
    results=[]; progress=PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-progress-{rollback.stem.rsplit("-",1)[-1]}.jsonl'
    with progress.open('w', encoding='utf-8') as f:
        os.chmod(progress,0o600)
        for rec in records:
            r=rec['planned_update']
            try:
                updated=upsert_product(mid, prepare_product(rec['current_product_resource'], r), token)
                item={'product_id':r['product_id'],'execution_status':'updated_wave2_attrs','sizes_after_response':updated.get('sizes'),'ageGroup_after_response':updated.get('ageGroup'),'gender_after_response':updated.get('gender')}
            except Exception as e:
                item={'product_id':r['product_id'],'execution_status':'failed_http_or_validation','error':str(e)[:1200]}; results.append(item); f.write(json.dumps(item,ensure_ascii=False)+'\n'); f.flush(); break
            results.append(item); f.write(json.dumps(item,ensure_ascii=False)+'\n'); f.flush(); time.sleep(0.2)
    return results, rollback

def verify(mid: str, token: str, rows: list[dict[str, Any]], results: list[dict[str, Any]], delay: int) -> list[dict[str, Any]]:
    if delay: time.sleep(delay)
    byid={r['product_id']:r for r in rows}; out=[]
    for res in results:
        pid=res.get('product_id'); r=byid.get(pid,{})
        if res.get('execution_status')!='updated_wave2_attrs' or not pid: out.append({**res,'verify_status':'not_verified_due_to_execution_status'}); continue
        try:
            prod=get_product(mid,pid,token); actual_sizes=norm_list(prod.get('sizes'))
            ok=(actual_sizes==(r.get('suggested_sizes') or []) and prod.get('ageGroup')==r.get('suggested_age_group') and prod.get('gender')==r.get('suggested_gender'))
            out.append({**res,'verify_status':'verified_product_get','sizes_after_get':actual_sizes,'ageGroup_after_get':prod.get('ageGroup'),'gender_after_get':prod.get('gender'),'attrs_match_expected':ok})
        except Exception as e: out.append({**res,'verify_status':'verify_failed','verify_error':str(e)[:1200]})
    return out

def write_outputs(mode: str, summary: dict[str, Any], rows: list[dict[str, Any]], exec_results: list[dict[str, Any]], verified: list[dict[str, Any]], rollback: pathlib.Path | None, limit: int) -> None:
    ec=Counter(r.get('execution_status') for r in exec_results); vc=Counter(r.get('verify_status') for r in verified); matched=sum(1 for r in verified if r.get('attrs_match_expected'))
    payload={'generated_at':utc_now(),'status':'gmc_p1_attribute_wave2_pilot_apply_verified' if mode=='apply' else 'gmc_p1_attribute_wave2_pilot_executor_dry_run_ready','mode':mode,'scope':'Onda 2 conservative pilot; exact online IDs; sizes + ageGroup adult + gender unisex only.','source_labels':['fact_merchant_center','fact_shopify_local_snapshot','derived_reconciliation'],'approval_required_for_apply':APPROVAL_TEXT_REQUIRED,'summary':{**summary,'execution_results_summary':dict(ec),'verify_results_summary':dict(vc),'verified_attrs_match_expected':matched},'private_rollback_snapshot_path':str(rollback) if rollback else None,'public_rows':rows,'execution_results':exec_results,'verified_results':verified,'not_performed':['merchant_write' if mode!='apply' else 'merchant_delete','merchant_delete','merchant_price_title_link_image_availability_update','feed_update_or_fetch','shopify_write','tiny_call_or_write','database_write','pos_or_local_inventory_write','klaviyo_or_whatsapp_send','notion_or_n8n_write','loyalty_or_judgeme_action']}
    PUBLIC_JSON.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n', encoding='utf-8')
    fields=['product_id','merchant_title','shopify_variant_title','fresh_missing_required_attrs','current_sizes','current_age_group','current_gender','suggested_sizes','suggested_age_group','suggested_gender','decision_state','selected_for_apply','decision_reasons','write_scope_if_approved','rollback_required_before_write']
    with PUBLIC_CSV.open('w', newline='', encoding='utf-8') as f:
        w=csv.DictWriter(f, fieldnames=fields, extrasaction='ignore'); w.writeheader()
        for r in rows:
            o={k:r.get(k) for k in fields}
            for k in ['fresh_missing_required_attrs','current_sizes','suggested_sizes','decision_reasons']: o[k]='; '.join(o.get(k) or [])
            w.writerow(o)
    lines=['# LK GMC P1 Attribute Completion — Onda 2 Pilot Executor, 2026-05-13','',f"Status: `{payload['status']}`",'','## Escopo',f'- Modo: `{mode}`','- Onda: 2, piloto conservador.','- Campos alvo: `sizes`, `ageGroup`, `gender`.','- Valores default aceitos no piloto: `ageGroup=adult`, `gender=unisex`.','- Canal: `online` apenas.','- Apply produtivo: bloqueado até aprovação inline específica.','','## Resultado do preflight',f"- Rows Onda 2 no packet: {summary['wave2_packet_rows']}",f"- Merchant products atuais: {summary['fresh_merchant_products_current']}",f"- Productstatuses atuais: {summary['fresh_merchant_productstatuses_current']}",f"- Ready para apply futuro: {summary['ready_total']}",f"- Selecionados no piloto se aprovado: {summary['selected_for_apply_if_approved']}",'','## Estados']
    for k,v in sorted(summary['decision_state_counts'].items()): lines.append(f'- {k}: {v}')
    lines.extend(['','## Amostra selecionada para piloto'])
    for r in [x for x in rows if x.get('selected_for_apply')][:25]: lines.append(f"- `{r['product_id']}` — {r.get('merchant_title')} — missing={r.get('fresh_missing_required_attrs')} — aplicar se aprovado: size={r.get('suggested_sizes')}, ageGroup={r.get('suggested_age_group')}, gender={r.get('suggested_gender')}")
    lines.extend(['','## Aprovação necessária para apply futuro',f'- Texto exato requerido pelo executor: `{APPROVAL_TEXT_REQUIRED}`','- Recomendação: aplicar primeiro piloto de 50, verificar via `products.get`, depois medir `productstatuses` antes de escalar.','','## Rollback privado',f'- `{rollback}`' if rollback else '- Não criado no dry-run; será criado antes de qualquer apply.','','## Não executado'])
    for n in payload['not_performed']: lines.append(f'- {n}')
    PUBLIC_MD.write_text('\n'.join(lines)+'\n', encoding='utf-8'); BRAIN_DOC.write_text(PUBLIC_MD.read_text(encoding='utf-8'), encoding='utf-8')
    if CONTROL.exists():
        marker='### 2026-05-13 — GMC P1 attribute completion Onda 2 pilot executor dry-run'
        text=CONTROL.read_text(encoding='utf-8')
        block=f"\n{marker}\n\n- Status: `{payload['status']}`.\n- Escopo: Onda 2 piloto conservador; `sizes` + `ageGroup=adult` + `gender=unisex`; exact online Merchant IDs.\n- Resultado dry-run: {summary['ready_total']} ready; {summary['selected_for_apply_if_approved']} selecionados no piloto; nenhum write executado.\n- Apply futuro exige aprovação inline: `{APPROVAL_TEXT_REQUIRED}`.\n"
        if marker not in text: CONTROL.write_text(text.rstrip()+block+'\n', encoding='utf-8')
    if INDEX.exists():
        line=f'| LK GMC P1 Attribute Completion Onda 2 Pilot Executor 2026-05-13 | `areas/lk/rotinas/gmc-{RUN_STAMP}.md` | Dry-run/executor piloto Onda 2: sizes + ageGroup + gender, apply bloqueado por aprovação inline |'
        text=INDEX.read_text(encoding='utf-8')
        if line not in text: INDEX.write_text(text.rstrip()+'\n'+line+'\n', encoding='utf-8')
    print(json.dumps({'status':payload['status'],'mode':mode,'summary':payload['summary'],'public_report':str(PUBLIC_MD),'private_rollback_snapshot_path':str(rollback) if rollback else None}, ensure_ascii=False, indent=2))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--apply', action='store_true'); ap.add_argument('--approval-text', default=''); ap.add_argument('--limit', type=int, default=50); ap.add_argument('--verify-delay', type=int, default=60); args=ap.parse_args()
    mode='apply' if args.apply else 'dry-run'
    if args.apply and args.approval_text != APPROVAL_TEXT_REQUIRED: raise RuntimeError(f'apply_blocked_missing_exact_approval_text: {APPROVAL_TEXT_REQUIRED}')
    audit=import_audit(); secrets=audit.load_doppler(); mid=secrets.get('MERCHANT_CENTER_ID_LK')
    if not mid: raise RuntimeError('missing_merchant_center_id')
    token=audit.google_access_token(audit.parse_service_account(secrets)); products=audit.list_all('products', mid, token); statuses=audit.list_all('productstatuses', mid, token)
    rows, summary=build_rows(load_wave2(), products, statuses, args.limit)
    exec_results=[]; verified=[]; rollback=None
    if mode=='apply': exec_results, rollback=apply_selected(mid, token, rows, products, args.limit); verified=verify(mid, token, rows, exec_results, args.verify_delay)
    write_outputs(mode, summary, rows, exec_results, verified, rollback, args.limit)

if __name__=='__main__': main()
