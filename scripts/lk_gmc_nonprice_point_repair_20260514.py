#!/usr/bin/env python3
from __future__ import annotations
import importlib.util, json, os, pathlib, re, time, urllib.parse
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
ABC = ROOT/'scripts/lk_execute_approved_abc_20260514.py'
TRIAGE = ROOT/'reports/lk-gmc-2026-05-14-residual-triage-current.json'
OUT_JSON = ROOT/'reports/lk-gmc-2026-05-14-nonprice-point-repair.json'
OUT_MD = ROOT/'reports/lk-gmc-2026-05-14-nonprice-point-repair.md'
BRAIN_MD = ROOT/'areas/lk/rotinas/gmc-2026-05-14-nonprice-point-repair.md'
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
TARGET_NONPRICE = {'missing_item_attribute_for_product_type','image_single_color','image_link_broken','landing_page_error'}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_module(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(m)
    return m

abc = load_module(ABC, 'abc')


def product_status_get(mid: str, token: str, pid: str) -> dict[str, Any]:
    url = f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/productstatuses/{urllib.parse.quote(pid, safe="")}'
    return abc.request_json(url, token=token, attempts=4, timeout=90)


def upsert_product(mid: str, token: str, product: dict[str, Any]) -> dict[str, Any]:
    url = f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/products'
    return abc.request_json(url, token=token, method='POST', payload=product, attempts=5, timeout=120)


def content_delete(mid: str, token: str, pid: str) -> dict[str, Any]:
    url = f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/products/{urllib.parse.quote(pid, safe="")}'
    return abc.request_json(url, token=token, method='DELETE', attempts=4, timeout=90)


def extract_handle(link: str|None) -> str|None:
    if not link: return None
    path = urllib.parse.urlparse(link).path.rstrip('/')
    return path.split('/')[-1] if path else None


def shopify_product_by_handle(secrets: dict[str,str], handle: str|None) -> dict[str,Any]|None:
    if not handle: return None
    q='''query P($handle:String!){ productByHandle(handle:$handle){ id legacyResourceId title handle status onlineStoreUrl featuredImage{url} images(first:10){nodes{url}} tags productType vendor } }'''
    return ((abc.shopify_graphql(secrets,q,{'handle':handle}).get('data') or {}).get('productByHandle'))


def product_input_patch(mid: str, token: str, pid: str, attrs: dict[str,Any]) -> dict[str,Any]:
    return abc.patch_product_input_attrs(mid, token, pid, attrs)


def target_codes(row: dict[str,Any]) -> list[str]:
    return sorted({i.get('code') for i in row.get('issues') or [] if i.get('code') in TARGET_NONPRICE})


def title_color(text: str) -> str|None:
    # Prefer LK/Portuguese customer-facing color tokens already present in titles.
    mapping = [
        (r'\bBord[oóô]\b', 'Bordô'),
        (r'\bBranco\b|\bWhite\b', 'Branco'),
        (r'\bPreto\b|\bBlack\b', 'Preto'),
        (r'\bAzul\b|\bBlue\b', 'Azul'),
        (r'\bTurquesa\b|\bTurquoise\b', 'Turquesa'),
        (r'\bBege\b|\bBeige\b|\bLinen\b', 'Bege'),
        (r'\bMarrom\b|\bBrown\b', 'Marrom'),
        (r'\bVerde\b|\bGreen\b', 'Verde'),
        (r'\bVermelho\b|\bRed\b', 'Vermelho'),
        (r'\bRosa\b|\bPink\b', 'Rosa'),
        (r'\bRoxo\b|\bPurple\b', 'Roxo'),
        (r'\bAmarelo\b|\bYellow\b', 'Amarelo'),
        (r'\bCinza\b|\bGrey\b|\bGray\b', 'Cinza'),
        (r'\bColorido\b|\bMulticolor\b', 'Multicolor'),
    ]
    for pat, val in mapping:
        if re.search(pat, text or '', re.I):
            return val
    return None


def important_subset(p: dict[str,Any]) -> dict[str,Any]:
    keys=['id','offerId','channel','contentLanguage','targetCountry','source','title','link','imageLink','additionalImageLinks','gtin','brand','price','salePrice','availability','googleProductCategory','productTypes','color','sizes','ageGroup','gender']
    return {k:p.get(k) for k in keys if k in p}


def status_target_codes(st: dict[str,Any]) -> list[str]:
    return sorted({i.get('code') for i in (st.get('itemLevelIssues') or []) if i.get('code') in TARGET_NONPRICE})


def build_plan(rows: list[dict[str,Any]], secrets: dict[str,str]) -> tuple[list[dict[str,Any]], list[dict[str,Any]]]:
    actions=[]; pending=[]
    for r in rows:
        pid=r['product_id']; codes=set(target_codes(r))
        if not codes:
            continue
        if codes == {'missing_item_attribute_for_product_type'} or 'missing_item_attribute_for_product_type' in codes:
            missing={str(i.get('attributeName') or '').lower() for i in r.get('issues') or [] if i.get('code')=='missing_item_attribute_for_product_type'}
            if pid.startswith('online:') and any('color' in x for x in missing) and not r.get('color'):
                c=title_color(r.get('title') or '')
                if c:
                    actions.append({'product_id':pid,'kind':'online_color_completion','attrs':{'color':c},'evidence':{'title':r.get('title'),'missing_attributes':sorted(missing)}})
                else:
                    pending.append({'product_id':pid,'reason':'missing_color_no_deterministic_title_token','codes':sorted(codes),'title':r.get('title')})
            else:
                pending.append({'product_id':pid,'reason':'missing_attribute_not_safe_for_this_executor','codes':sorted(codes),'missing_attributes':sorted(missing),'current':{'color':r.get('color'),'sizes':r.get('sizes'),'ageGroup':r.get('ageGroup'),'gender':r.get('gender')}})
            continue
        if 'image_single_color' in codes or 'image_link_broken' in codes:
            # Current diagnostics point to `additional image link`; safest reversible action is to clear only additionalImageLinks,
            # preserving main imageLink and all commercial attributes. This avoids inventing or swapping product imagery.
            attr_names={str(i.get('attributeName') or '').lower() for i in r.get('issues') or [] if i.get('code') in {'image_single_color','image_link_broken'}}
            if any('additional image' in x for x in attr_names) and (r.get('additionalImageLinks') or []):
                actions.append({'product_id':pid,'kind':'clear_bad_additional_image_links','attrs':{'additionalImageLinks':[]},'evidence':{'issue_attribute_names':sorted(attr_names),'current_additional_count':len(r.get('additionalImageLinks') or []),'main_image_preserved':r.get('imageLink')}})
            else:
                pending.append({'product_id':pid,'reason':'image_issue_no_safe_additional_link_clear','codes':sorted(codes),'attribute_names':sorted(attr_names),'additional_count':len(r.get('additionalImageLinks') or [])})
            continue
        if 'landing_page_error' in codes:
            handle=extract_handle(r.get('link'))
            p=shopify_product_by_handle(secrets, handle)
            status=(p or {}).get('status')
            if (not p) or status in {'DRAFT','ARCHIVED'}:
                actions.append({'product_id':pid,'kind':'delete_stale_landing_page_product','attrs':{},'evidence':{'handle':handle,'shopify_status':'not_found' if not p else status,'link':r.get('link')}})
            else:
                pending.append({'product_id':pid,'reason':'landing_page_error_but_shopify_product_active_or_unknown_public_probe_needed','codes':sorted(codes),'handle':handle,'shopify_status':status,'onlineStoreUrl':(p or {}).get('onlineStoreUrl')})
            continue
        pending.append({'product_id':pid,'reason':'unhandled_nonprice_codes','codes':sorted(codes)})
    return actions, pending


def main():
    secrets=abc.load_doppler(); mid=secrets['MERCHANT_CENTER_ID_LK']; token=abc.google_access_token(abc.parse_service_account(secrets))
    triage=json.loads(TRIAGE.read_text())
    rows=triage.get('rows') or []
    actions,pending=build_plan(rows,secrets)
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True); os.chmod(PRIVATE_DIR,0o700)
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    rollback_path=PRIVATE_DIR/f'lk-gmc-nonprice-point-repair-rollback-{stamp}.json'
    progress_path=PRIVATE_DIR/f'lk-gmc-nonprice-point-repair-progress-{stamp}.jsonl'
    rollback=[]
    for a in actions:
        cur=abc.content_product_get(mid, token, a['product_id'])
        rollback.append({'product_id':a['product_id'],'kind':a['kind'],'current_product_resource':cur,'current_subset':important_subset(cur),'planned_attrs':a['attrs'],'evidence':a['evidence']})
        time.sleep(0.08)
    rollback_path.write_text(json.dumps({'generated_at':utc_now(),'approval':'Lucas approved continuing correction of small non-price GMC residuals; price excluded/blocked','scope':'non-price point repair only: color completion, clear bad additional image links, delete stale landing-page product when Shopify inactive/absent','rollback_instruction':'For ProductInputs patches, patch back fields from current_subset/current_product_resource. For Content API deletes/upserts, reinsert current_product_resource via Content API products.insert, then verify products.get/productstatuses.','records':rollback},ensure_ascii=False,indent=2)+'\n')
    os.chmod(rollback_path,0o600)
    progress_path.write_text(''); os.chmod(progress_path,0o600)
    execution=[]
    for a in actions:
        pid=a['product_id']
        try:
            if a['kind']=='delete_stale_landing_page_product':
                content_delete(mid, token, pid)
                item={'product_id':pid,'kind':a['kind'],'execution_status':'deleted_or_absent'}
            elif pid.startswith('local:'):
                rb=next(x for x in rollback if x['product_id']==pid)
                product=json.loads(json.dumps(rb['current_product_resource']))
                product.pop('source', None)
                for k,v in a['attrs'].items(): product[k]=v
                resp=upsert_product(mid, token, product)
                item={'product_id':pid,'kind':a['kind'],'execution_status':'patched_content_api','attrs':a['attrs'],'response_id':resp.get('id')}
            elif pid.startswith('online:'):
                resp=product_input_patch(mid, token, pid, a['attrs'])
                item={'product_id':pid,'kind':a['kind'],'execution_status':'patched_productinputs_v1','attrs':a['attrs'],'response_name':resp.get('name')}
            else:
                raise RuntimeError('unsupported_product_channel')
        except Exception as e:
            item={'product_id':pid,'kind':a['kind'],'execution_status':'error','attrs':a.get('attrs'),'error':str(e)[:1200]}
        execution.append(item)
        with progress_path.open('a',encoding='utf-8') as f: f.write(json.dumps(item,ensure_ascii=False)+'\n')
        time.sleep(0.35)
    time.sleep(75)
    verify=[]
    for a in actions:
        pid=a['product_id']
        try:
            if a['kind']=='delete_stale_landing_page_product':
                try:
                    cur=abc.content_product_get(mid, token, pid)
                    verify.append({'product_id':pid,'kind':a['kind'],'verify_status':'still_present','match_expected':False,'fresh_subset':important_subset(cur)})
                except Exception as e:
                    verify.append({'product_id':pid,'kind':a['kind'],'verify_status':'absent_or_get_failed','match_expected':True,'detail':str(e)[:300]})
            else:
                cur=abc.content_product_get(mid, token, pid)
                expected=a['attrs']
                actual={k:cur.get(k) for k in expected}
                ok=True
                for k,v in expected.items():
                    if k=='additionalImageLinks': ok = ok and ((cur.get(k) or []) == v)
                    else: ok = ok and (cur.get(k) == v)
                verify.append({'product_id':pid,'kind':a['kind'],'verify_status':'read','expected':expected,'actual':actual,'match_expected':ok,'fresh_subset':important_subset(cur)})
        except Exception as e:
            verify.append({'product_id':pid,'kind':a['kind'],'verify_status':'error','match_expected':False,'error':str(e)[:800]})
        time.sleep(0.12)
    time.sleep(90)
    token=abc.google_access_token(abc.parse_service_account(secrets))
    status_rows=[]
    for a in actions:
        pid=a['product_id']
        try:
            st=product_status_get(mid, token, pid)
            status_rows.append({'product_id':pid,'kind':a['kind'],'status_read':'ok','target_issue_codes':status_target_codes(st),'all_issue_codes':sorted({i.get('code') for i in (st.get('itemLevelIssues') or []) if i.get('code')})})
        except Exception as e:
            # For deleted products, productstatuses.get can 404/failed; that is acceptable if product delete verified absent.
            status_rows.append({'product_id':pid,'kind':a['kind'],'status_read':'error_or_absent','error':str(e)[:500]})
        time.sleep(0.12)
    status='completed' if not any(x['execution_status']=='error' for x in execution) else 'completed_with_errors'
    payload={
        'generated_at':utc_now(),
        'approval':'Lucas: seguir; prior approval: corrigir o que deve ser corrigido está aprovado',
        'status':status,
        'source_labels':['manual_approval','fact_merchant_center','fact_shopify'],
        'summary':{
            'triage_nonprice_products':len([r for r in rows if set(target_codes(r))]),
            'planned_actions':len(actions),
            'planned_by_kind':dict(Counter(a['kind'] for a in actions)),
            'pending_records':len(pending),
            'pending_by_reason':dict(Counter(p['reason'] for p in pending)),
            'execution_counts':dict(Counter(e['execution_status'] for e in execution)),
            'verify_counts':dict(Counter('match' if v.get('match_expected') else 'mismatch' for v in verify)),
            'final_target_issue_counts_on_acted_ids':dict(Counter(code for row in status_rows for code in row.get('target_issue_codes',[]))),
            'acted_rows_with_target_issue_after':sum(1 for row in status_rows if row.get('target_issue_codes')),
        },
        'rollback_snapshot_path':str(rollback_path),
        'progress_jsonl_path':str(progress_path),
        'actions':actions,
        'pending_records':pending,
        'execution_results':execution,
        'verify_results':verify,
        'final_productstatus_results':status_rows,
        'not_performed':['price/salePrice write','Shopify write','Tiny write','feed fetch/upload','campaign/message/send','bulk reapply','new image asset generation or product-photo invention']
    }
    OUT_JSON.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    lines=['# LK GMC non-price point repair — 2026-05-14','',f"Generated: `{payload['generated_at']}`",'', '## Resultado', f"- Status: `{status}`"]
    for k,v in payload['summary'].items(): lines.append(f'- {k}: `{v}`')
    lines += ['', '## Auditoria privada', f'- Rollback: `{rollback_path}`', f'- Progress: `{progress_path}`', '', '## Bloqueados/pending']
    for p in pending[:30]: lines.append(f"- `{p['product_id']}` — {p['reason']}")
    lines += ['', '## Não executado'] + [f'- {x}' for x in payload['not_performed']]
    OUT_MD.write_text('\n'.join(lines)+'\n')
    BRAIN_MD.parent.mkdir(parents=True, exist_ok=True); BRAIN_MD.write_text(OUT_MD.read_text())
    print(json.dumps({'status':status,'summary':payload['summary'],'out':str(OUT_JSON),'md':str(OUT_MD),'rollback':str(rollback_path)},ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
