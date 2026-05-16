#!/usr/bin/env python3
"""GMC P1 Wave4 aggressive non-price attribute executor.

Lucas approved completeness > perfect fidelity for non-critical Merchant attrs.
This executor fetches fresh Merchant products/productstatuses and fills only
non-price attrs (color/sizes/ageGroup/gender) using broader evidence/defaults:
- color from title tokens; fallback Multicolor when color is required but absent
- sizes from merchant title/offer tokens (numeric/alpha/OS); fallback Único only
  for obvious one-size/accessory titles or offer suffix -OS
- ageGroup=adult and gender=unisex defaults

Price remains excluded even when the product also has price diagnostics.
Writes are via POST /products, preserving current product resource, with private
rollback snapshots and products.get verification.
"""
from __future__ import annotations

import argparse, csv, importlib.util, json, os, pathlib, re, time, urllib.error, urllib.parse, urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / 'scripts/lk_gmc_catalog_duplication_audit_20260512.py'
RUN_STAMP = '2026-05-13-p1-attribute-wave4-aggressive-nonprice-executor'
PUBLIC_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
PUBLIC_CSV = ROOT / f'reports/lk-gmc-{RUN_STAMP}.csv'
PUBLIC_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
REQ_CODES = {'item_missing_required_attribute', 'missing_item_attribute_for_product_type'}
ALLOWED_FIELDS = {'color', 'sizes', 'ageGroup', 'gender'}
APPROVAL_TEXT_REQUIRED = 'Lucas approved GMC P1 Attribute Wave4 aggressive non-price apply'

COLOR_MAP = {
    'preto':'Preto','preta':'Preto','black':'Preto','jet black':'Preto',
    'branco':'Branco','branca':'Branco','white':'Branco','off white':'Off White','off-white':'Off White',
    'cinza':'Cinza','grey':'Cinza','gray':'Cinza','heather grey':'Cinza','ash':'Cinza',
    'azul':'Azul','blue':'Azul','navy':'Azul','marinho':'Azul',
    'verde':'Verde','green':'Verde','pine':'Verde',
    'vermelho':'Vermelho','red':'Vermelho',
    'rosa':'Rosa','pink':'Rosa',
    'roxo':'Roxo','purple':'Roxo',
    'amarelo':'Amarelo','yellow':'Amarelo',
    'laranja':'Laranja','orange':'Laranja',
    'marrom':'Marrom','brown':'Marrom','wood':'Marrom',
    'bege':'Bege','homestead':'Bege','taupe':'Bege','areia':'Bege','natural':'Bege','palha':'Bege','cream':'Creme','creme':'Creme',
    'prata':'Prata','silver':'Prata','dourado':'Dourado','gold':'Dourado',
    'vinho':'Vinho','bordô':'Vinho','leopard':'Animal Print','leopardo':'Animal Print'
}
COLOR_TOKENS = sorted(COLOR_MAP, key=len, reverse=True)
ONE_SIZE_HINTS = ['boné','bone','cap','bolsa','bag','pingente','chaveiro','figure','blind box','lacrado','hat','commuter','briefcase']
ALPHA_SIZES = ['XXS','XS','PP','P','S','M','G','L','GG','XL','XXL','XXXL']


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
        data=request_json(url, token); batch=data.get('resources') or []
        rows.extend(batch); page=data.get('nextPageToken')
        if not page or not batch: break
    return rows

def product_url(mid: str, pid: str) -> str:
    return f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/products/{urllib.parse.quote(pid, safe="")}'

def get_product(mid: str, pid: str, token: str) -> dict[str, Any]: return request_json(product_url(mid,pid), token)
def upsert_product(mid: str, product: dict[str, Any], token: str) -> dict[str, Any]: return request_json(f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/products', token=token, method='POST', payload=product)

def norm_attr(v: Any) -> str: return str(v or '').strip().lower().replace('_',' ')
def norm_list(v: Any) -> list[str]:
    if v is None: return []
    if isinstance(v, list): return [str(x).strip() for x in v if str(x).strip()]
    t=str(v).strip(); return [t] if t else []

def required_attrs(status: dict[str, Any] | None) -> set[str]:
    out=set()
    for issue in (status or {}).get('itemLevelIssues') or []:
        if issue.get('code') in REQ_CODES:
            a=norm_attr(issue.get('attributeName'))
            if a: out.add(a)
    return out

def parse_offer(pid: str) -> str:
    parts=(pid or '').split(':',3)
    return parts[3] if len(parts)==4 else (pid or '')

def clean_text(*parts: str) -> str:
    return ' '.join(str(p or '') for p in parts if p).strip()

def infer_color(title: str) -> tuple[str|None,str|None]:
    t=' '+re.sub(r'[^\wÀ-ÿ\-/ ]+', ' ', (title or '').lower()).replace('/', ' / ')+' '
    found=[]
    for tok in COLOR_TOKENS:
        pat=' '+tok.lower().replace('-', ' ')+' '
        hay=t.replace('-', ' ')
        if pat in hay:
            val=COLOR_MAP[tok]
            if val not in found: found.append(val)
    if found:
        return ' / '.join(found[:3]), 'title_color_token_aggressive'
    return 'Multicolor', 'default_color_multicolor_lucas_completeness_policy'

def infer_size(title: str, offer: str) -> tuple[list[str]|None,str|None]:
    raw=clean_text(title, offer)
    txt=raw.strip()
    # Exact numeric title like "34" or "36/37" from malformed feed rows.
    if re.fullmatch(r'\d{2}(?:[\./]\d{1,2}(?:\.5)?)?', txt):
        return [txt], 'merchant_title_exact_size_token'
    # Offer suffixes / explicit one-size.
    if re.search(r'(?:^|[-_\s])(OS|ONE\s*SIZE|U|ÚNICO|UNICO)(?:$|[-_\s])', raw, re.I):
        return ['Único'], 'offer_or_title_one_size_token'
    # Apparel alpha size suffix in offer, e.g. ALD-2515934-L, or title "M/m".
    m=re.search(r'(?:^|[-_\s/])('+'|'.join(re.escape(x) for x in ALPHA_SIZES)+r')(?:$|[-_\s/])', raw, re.I)
    if m:
        return [m.group(1).upper()], 'offer_or_title_alpha_size_token'
    # Shoe/apparel numeric size somewhere in title/offer, conservative range.
    nums=re.findall(r'(?<!\d)(3[3-9]|4[0-7])(?:[\./](?:3[3-9]|4[0-7]|5))?(?!\d)', raw)
    if nums:
        return [nums[0]], 'offer_or_title_numeric_size_token'
    low=raw.lower()
    if any(h in low for h in ONE_SIZE_HINTS):
        return ['Único'], 'default_one_size_for_accessory_title'
    return None, None

def suggestions_for(pid: str, prod: dict[str,Any], status: dict[str,Any]|None) -> tuple[dict[str,Any],dict[str,str],list[str]]:
    attrs=required_attrs(status); title=prod.get('title') or (status or {}).get('title') or ''; offer=parse_offer(pid)
    sugg={}; evidence={}; reasons=[]
    if 'color' in attrs and not prod.get('color'):
        c, ev = infer_color(title)
        if c: sugg['color']=c; evidence['color']=ev; reasons.append('color filled from title token or Multicolor fallback')
    if 'size' in attrs and not norm_list(prod.get('sizes')):
        sizes, ev = infer_size(title, offer)
        if sizes: sugg['sizes']=sizes; evidence['sizes']=ev; reasons.append('size filled from title/offer/one-size token')
    if 'age group' in attrs and not prod.get('ageGroup'):
        sugg['ageGroup']='adult'; evidence['ageGroup']='default_adult_lucas_completeness_policy'; reasons.append('ageGroup default adult')
    if 'gender' in attrs and not prod.get('gender'):
        sugg['gender']='unisex'; evidence['gender']='default_unisex_lucas_completeness_policy'; reasons.append('gender default unisex')
    # Never add price, even when required.
    return sugg, evidence, reasons

def build_rows(products, statuses, limit):
    p_by_id={p.get('id'):p for p in products}; rows=[]; counters=Counter(); attr_counts=Counter(); field_counts=Counter()
    for st in statuses:
        pid=st.get('productId'); attrs=required_attrs(st)
        if not attrs: continue
        for a in attrs: attr_counts[a]+=1
        prod=p_by_id.get(pid) or {}; sugg,evidence,reasons=suggestions_for(pid, prod, st)
        nonprice_attrs=attrs & {'color','size','age group','gender'}
        if not nonprice_attrs:
            decision='blocked_price_only_no_nonprice_update'
        elif not prod:
            decision='blocked_product_not_currently_present'
        elif not sugg:
            decision='blocked_no_nonprice_inference_even_aggressive'
        elif not set(sugg) <= ALLOWED_FIELDS:
            decision='blocked_field_outside_contract'
        else:
            decision='ready_for_wave4_aggressive_nonprice_apply'
            for k in sugg: field_counts[k]+=1
        counters[decision]+=1
        rows.append({'product_id':pid,'offer_id':parse_offer(pid or ''),'merchant_title':prod.get('title') or st.get('title'),'fresh_required_attrs':sorted(attrs),'suggested_attributes':sugg,'evidence':evidence,'decision_state':decision,'decision_reasons':reasons + (['price remains excluded'] if 'price' in attrs else []),'selected_for_apply':False,'current_color':prod.get('color'),'current_sizes':norm_list(prod.get('sizes')),'current_ageGroup':prod.get('ageGroup'),'current_gender':prod.get('gender'),'has_price_required_attr':'price' in attrs})
    ready=[r for r in rows if r['decision_state']=='ready_for_wave4_aggressive_nonprice_apply']
    ready.sort(key=lambda r: (r['has_price_required_attr'], r.get('merchant_title') or '', r['product_id'] or ''))
    selected={r['product_id'] for r in ready[:limit]}
    for r in rows: r['selected_for_apply']=r['product_id'] in selected
    summary={'fresh_merchant_products_current':len(products),'fresh_merchant_productstatuses_current':len(statuses),'required_attr_rows_current':len(rows),'required_attr_instances_current':sum(len(r['fresh_required_attrs']) for r in rows),'required_attr_counts':dict(attr_counts.most_common()),'decision_state_counts':dict(counters),'ready_total':len(ready),'selected_for_apply_if_approved':len(selected),'suggested_field_counts':dict(field_counts),'limit':limit,'write_allowed_now':0}
    return rows, summary

def prepare_product(cur, row):
    out=json.loads(json.dumps(cur, ensure_ascii=False))
    for k in ['id','kind','source']: out.pop(k, None)
    for k,v in row['suggested_attributes'].items(): out[k]=v
    return out

def snapshot(records, limit):
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True); os.chmod(PRIVATE_DIR,0o700)
    path=PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-rollback-{datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")}.json'
    path.write_text(json.dumps({'generated_at':utc_now(),'scope':f'Wave4 aggressive non-price apply limit={limit}; update only color/sizes/ageGroup/gender; price excluded','approval_text_required':APPROVAL_TEXT_REQUIRED,'rollback_instruction':'Use POST /products with current_product_resource; verify after delay.','records':records}, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
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
                upsert_product(mid, prepare_product(rec['current_product_resource'], r), token)
                item={'product_id':r['product_id'],'execution_status':'updated_wave4_aggressive_nonprice_attrs','fields':sorted(r['suggested_attributes'].keys())}
            except Exception as e:
                item={'product_id':r['product_id'],'execution_status':'failed_http_or_validation','error':str(e)[:1200]}; results.append(item); f.write(json.dumps(item,ensure_ascii=False)+'\n'); f.flush(); break
            results.append(item); f.write(json.dumps(item,ensure_ascii=False)+'\n'); f.flush(); time.sleep(0.2)
    return results, rollback

def verify(mid, token, rows, results, delay):
    if delay: time.sleep(delay)
    byid={r['product_id']:r for r in rows}; out=[]
    for res in results:
        pid=res.get('product_id'); r=byid.get(pid,{})
        if res.get('execution_status')!='updated_wave4_aggressive_nonprice_attrs' or not pid:
            out.append({**res,'verify_status':'not_verified_due_to_execution_status'}); continue
        try:
            prod=get_product(mid,pid,token); ok=True; actual={}
            for k,v in (r.get('suggested_attributes') or {}).items():
                av=norm_list(prod.get(k)) if k=='sizes' else prod.get(k); actual[k]=av; ok = ok and (av==v)
            out.append({**res,'verify_status':'verified_product_get','actual_attrs':actual,'attrs_match_expected':ok})
        except Exception as e: out.append({**res,'verify_status':'verify_failed','verify_error':str(e)[:1200]})
    return out

def post_status_recheck(mid, token):
    products=list_all('products',mid,token); statuses=list_all('productstatuses',mid,token)
    attrs=[]
    for st in statuses:
        a=required_attrs(st)
        if a: attrs.extend(a)
    return {'fresh_merchant_products_after':len(products),'fresh_productstatuses_after':len(statuses),'required_attr_rows_after':sum(1 for st in statuses if required_attrs(st)),'required_attr_instances_after':len(attrs),'required_attr_counts_after':dict(Counter(attrs).most_common())}

def write_outputs(mode, summary, rows, exec_results, verified, rollback, post):
    ec=Counter(r.get('execution_status') for r in exec_results); vc=Counter(r.get('verify_status') for r in verified); matched=sum(1 for r in verified if r.get('attrs_match_expected'))
    payload={'generated_at':utc_now(),'status':'gmc_p1_attribute_wave4_aggressive_nonprice_apply_verified' if mode=='apply' else 'gmc_p1_attribute_wave4_aggressive_nonprice_dry_run_ready','mode':mode,'scope':'Wave4 aggressive non-price attrs: color/sizes/ageGroup/gender only; price excluded even when present.','source_labels':['fact_merchant_center','derived_reconciliation','manual_approval'],'approval_required_for_apply':APPROVAL_TEXT_REQUIRED,'summary':{**summary,'execution_results_summary':dict(ec),'verify_results_summary':dict(vc),'verified_attrs_match_expected':matched, **(post or {})},'private_rollback_snapshot_path':str(rollback) if rollback else None,'public_rows':rows,'execution_results':exec_results,'verified_results':verified,'not_performed':['merchant_price_update','merchant_delete','merchant_title_link_image_availability_update','feed_update_or_fetch','shopify_write','tiny_call_or_write','database_write','pos_or_local_inventory_write','klaviyo_or_whatsapp_send','notion_or_n8n_write','loyalty_or_judgeme_action']}
    PUBLIC_JSON.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    fields=['product_id','offer_id','merchant_title','fresh_required_attrs','suggested_attributes','evidence','decision_state','selected_for_apply','has_price_required_attr','decision_reasons']
    with PUBLIC_CSV.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore'); w.writeheader()
        for r in rows:
            o={k:r.get(k) for k in fields}; o['fresh_required_attrs']='; '.join(o.get('fresh_required_attrs') or []); o['suggested_attributes']=json.dumps(o.get('suggested_attributes') or {},ensure_ascii=False); o['evidence']=json.dumps(o.get('evidence') or {},ensure_ascii=False); o['decision_reasons']='; '.join(o.get('decision_reasons') or []); w.writerow(o)
    lines=['# LK GMC P1 Attribute Completion — Wave4 Aggressive Non-Price Executor, 2026-05-13','',f"Status: `{payload['status']}`",'','## Escopo',f'- Modo: `{mode}`','- Campos permitidos: `color`, `sizes`, `ageGroup`, `gender`.','- Excluído: `price` mesmo quando o produto também tem issue de preço.','- Critério Lucas: completude para ranking > fidelidade perfeita em atributos não críticos.','','## Resultado',f"- Required rows pré-execução: {summary['required_attr_rows_current']}",f"- Required instances pré-execução: {summary['required_attr_instances_current']}",f"- Ready: {summary['ready_total']}",f"- Selecionados/aplicados: {summary['selected_for_apply_if_approved']}",f"- Suggested fields: {summary['suggested_field_counts']}",'','## Estados']
    for k,v in sorted(summary['decision_state_counts'].items()): lines.append(f'- {k}: {v}')
    lines.extend(['','## Execução/verificação',f"- Execution: {dict(ec)}",f"- Verify: {dict(vc)}",f"- Match esperado: {matched}/{len(verified)}"])
    if post:
        lines.extend(['','## Recheck pós-delay',f"- Rows required attrs after: {post['required_attr_rows_after']}",f"- Instances required attrs after: {post['required_attr_instances_after']}",f"- Counts after: {post['required_attr_counts_after']}"])
    lines.extend(['','## Rollback privado',f'- `{rollback}`' if rollback else '- Não criado no dry-run.','','## Não executado'])
    for n in payload['not_performed']: lines.append(f'- {n}')
    PUBLIC_MD.write_text('\n'.join(lines)+'\n',encoding='utf-8'); BRAIN_DOC.write_text(PUBLIC_MD.read_text(encoding='utf-8'),encoding='utf-8')
    print(json.dumps({'status':payload['status'],'mode':mode,'summary':payload['summary'],'public_report':str(PUBLIC_MD),'private_rollback_snapshot_path':str(rollback) if rollback else None},ensure_ascii=False,indent=2))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--apply',action='store_true'); ap.add_argument('--approval-text',default=''); ap.add_argument('--limit',type=int,default=1000); ap.add_argument('--verify-delay',type=int,default=90); ap.add_argument('--post-status-delay',type=int,default=60); args=ap.parse_args()
    mode='apply' if args.apply else 'dry-run'
    if args.apply and args.approval_text != APPROVAL_TEXT_REQUIRED: raise RuntimeError(f'apply_blocked_missing_exact_approval_text: {APPROVAL_TEXT_REQUIRED}')
    audit=import_audit(); secrets=audit.load_doppler(); mid=secrets.get('MERCHANT_CENTER_ID_LK')
    if not mid: raise RuntimeError('missing_merchant_center_id')
    token=audit.google_access_token(audit.parse_service_account(secrets)); products=list_all('products',mid,token); statuses=list_all('productstatuses',mid,token)
    rows,summary=build_rows(products,statuses,args.limit)
    exec_results=[]; verified=[]; rollback=None; post=None
    if mode=='apply':
        exec_results, rollback=apply_selected(mid,token,rows,products,args.limit); verified=verify(mid,token,rows,exec_results,args.verify_delay)
        if args.post_status_delay: time.sleep(args.post_status_delay)
        post=post_status_recheck(mid,token)
    write_outputs(mode,summary,rows,exec_results,verified,rollback,post)

if __name__=='__main__': main()
