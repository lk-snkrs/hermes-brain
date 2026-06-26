#!/usr/bin/env python3
from __future__ import annotations
import importlib.util, json, os, pathlib, time, urllib.parse
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
ABC = ROOT/'scripts/lk_execute_approved_abc_20260514.py'
PREVIEW = ROOT/'reports/lk-gmc-2026-05-14-lia-gtin-preview.json'
OUT_JSON = ROOT/'reports/lk-gmc-2026-05-14-lia-gtin-apply.json'
OUT_MD = ROOT/'reports/lk-gmc-2026-05-14-lia-gtin-apply.md'
BRAIN_MD = ROOT/'areas/lk/rotinas/gmc-2026-05-14-lia-gtin-apply.md'
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
TARGET_CODES = {'restricted_gtin','reserved_gtin'}
PILOT_COUNT = 5


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


def target_status_codes(status: dict[str, Any]) -> list[str]:
    out=[]
    for dest in status.get('destinationStatuses') or []:
        pass
    for issue in status.get('itemLevelIssues') or []:
        code = issue.get('code')
        if code in TARGET_CODES:
            out.append(code)
    return sorted(set(out))


def important_subset(p: dict[str, Any]) -> dict[str, Any]:
    keys = ['id','offerId','channel','contentLanguage','targetCountry','source','title','link','imageLink','gtin','mpn','itemGroupId','brand','price','availability','googleProductCategory','productTypes','color','sizes','ageGroup','gender']
    return {k:p.get(k) for k in keys if k in p}


def build_records(preview: dict[str, Any]) -> list[dict[str, Any]]:
    rows=[]
    for r in preview['rows']:
        pid = r['product_id']
        gtin = str(r.get('recommended_gtin') or '').strip()
        if not pid.startswith('local:pt:BR:LIA_'):
            raise RuntimeError(f'unsafe_non_lia_product_id:{pid}')
        if not gtin or not gtin.isdigit() or len(gtin) not in {12,13,14}:
            raise RuntimeError(f'unsafe_gtin:{pid}:{gtin}')
        # Avoid known restricted/reserved ranges from prior GTIN repair policy.
        if gtin.startswith(('2','02','04')):
            raise RuntimeError(f'candidate_gtin_reserved_range:{pid}:{gtin}')
        rows.append({
            'product_id': pid,
            'title': r.get('title'),
            'current_gtin_preview': r.get('current_gtin'),
            'recommended_gtin': gtin,
            'candidate_state': r.get('candidate_state'),
            'normalized_style_sku': r.get('normalized_style_sku'),
            'kicks_evidence': r.get('kicks_evidence'),
        })
    if len(rows) != 34:
        raise RuntimeError(f'unexpected_record_count:{len(rows)}')
    return rows


def verify_products(mid: str, token: str, records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    verified=[]
    for rec in records:
        pid=rec['product_id']
        try:
            fresh=abc.content_product_get(mid, token, pid)
            ok = str(fresh.get('gtin') or '') == rec['recommended_gtin'] and fresh.get('id') == pid and fresh.get('channel') == 'local'
            verified.append({'product_id':pid,'verify_status':'read','expected_gtin':rec['recommended_gtin'],'actual_gtin':fresh.get('gtin'),'same_id':fresh.get('id')==pid,'channel':fresh.get('channel'),'source':fresh.get('source'),'match_expected':ok,'fresh_subset':important_subset(fresh)})
        except Exception as e:
            verified.append({'product_id':pid,'verify_status':'error','expected_gtin':rec['recommended_gtin'],'error':str(e)[:800],'match_expected':False})
        time.sleep(0.15)
    return verified


def status_recheck(mid: str, token: str, records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out=[]
    for rec in records:
        pid=rec['product_id']
        try:
            st=product_status_get(mid, token, pid)
            out.append({'product_id':pid,'status_read':'ok','target_issue_codes':target_status_codes(st),'all_issue_codes':sorted(set(i.get('code') for i in (st.get('itemLevelIssues') or []) if i.get('code'))), 'destination_status_count':len(st.get('destinationStatuses') or [])})
        except Exception as e:
            out.append({'product_id':pid,'status_read':'error','error':str(e)[:800]})
        time.sleep(0.15)
    return out


def main():
    secrets=abc.load_doppler()
    mid=secrets['MERCHANT_CENTER_ID_LK']
    token=abc.google_access_token(abc.parse_service_account(secrets))
    preview=json.loads(PREVIEW.read_text())
    records=build_records(preview)

    PRIVATE_DIR.mkdir(parents=True, exist_ok=True); os.chmod(PRIVATE_DIR, 0o700)
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    rollback_path=PRIVATE_DIR/f'lk-gmc-lia-gtin-rollback-{stamp}.json'
    progress_path=PRIVATE_DIR/f'lk-gmc-lia-gtin-progress-{stamp}.jsonl'

    rollback=[]
    for rec in records:
        cur=abc.content_product_get(mid, token, rec['product_id'])
        if cur.get('id') != rec['product_id'] or cur.get('channel') != 'local':
            raise RuntimeError(f'preflight_identity_mismatch:{rec["product_id"]}:{cur.get("id")}:{cur.get("channel")}')
        rollback.append({'product_id':rec['product_id'],'current_product_resource':cur,'current_subset':important_subset(cur),'target_gtin':rec['recommended_gtin'],'candidate_state':rec['candidate_state'],'kicks_evidence':rec.get('kicks_evidence')})
        time.sleep(0.08)
    rollback_path.write_text(json.dumps({'generated_at':utc_now(),'approval':'Lucas approved option 2: all 34 local/LIA GTINs; execute pilot 5 then scale 29 if pilot verifies','scope':'Content API products.insert/upsert preserving exact local:LIA resource and changing only gtin','rollback_instruction':'Reinsert current_product_resource for affected product_id via Content API products.insert, then verify products.get/productstatuses.','records':rollback}, ensure_ascii=False, indent=2)+'\n')
    os.chmod(rollback_path, 0o600)
    progress_path.write_text('')
    os.chmod(progress_path, 0o600)

    execution=[]
    def apply_batch(batch_name: str, batch: list[dict[str, Any]]):
        for rec in batch:
            rb=next(x for x in rollback if x['product_id']==rec['product_id'])
            current=rb['current_product_resource']
            if str(current.get('gtin') or '') == rec['recommended_gtin']:
                item={'batch':batch_name,'product_id':rec['product_id'],'execution_status':'skipped_already_matching','old_gtin':current.get('gtin'),'new_gtin':rec['recommended_gtin']}
            else:
                product=json.loads(json.dumps(current))
                old=product.get('gtin')
                # Content API products.insert rejects read-only response fields.
                # Preserve the resource semantics but omit server-managed fields.
                product.pop('source', None)
                product['gtin']=rec['recommended_gtin']
                try:
                    resp=upsert_product(mid, token, product)
                    item={'batch':batch_name,'product_id':rec['product_id'],'execution_status':'patched','old_gtin':old,'new_gtin':rec['recommended_gtin'],'response_id':resp.get('id'),'response_gtin':resp.get('gtin')}
                except Exception as e:
                    item={'batch':batch_name,'product_id':rec['product_id'],'execution_status':'error','old_gtin':old,'new_gtin':rec['recommended_gtin'],'error':str(e)[:1200]}
                    execution.append(item)
                    with progress_path.open('a', encoding='utf-8') as f: f.write(json.dumps(item, ensure_ascii=False)+'\n')
                    raise
            execution.append(item)
            with progress_path.open('a', encoding='utf-8') as f: f.write(json.dumps(item, ensure_ascii=False)+'\n')
            time.sleep(0.35)

    pilot=records[:PILOT_COUNT]
    rest=records[PILOT_COUNT:]
    apply_batch('pilot_5', pilot)
    # Local/LIA Content API upserts can return before readback reflects the new GTIN.
    time.sleep(75)
    pilot_verify=verify_products(mid, token, pilot)
    pilot_ok=all(v.get('match_expected') for v in pilot_verify)
    if not pilot_ok:
        status='stopped_after_pilot_verify_failed'
        scale_verify=[]; final_status=[]
    else:
        apply_batch('scale_remaining_29', rest)
        time.sleep(90)
        scale_verify=verify_products(mid, token, rest)
        # Give diagnostics a little propagation time; product readback is the hard correctness check.
        time.sleep(75)
        token=abc.google_access_token(abc.parse_service_account(secrets))
        final_status=status_recheck(mid, token, records)
        status='completed' if all(v.get('match_expected') for v in pilot_verify+scale_verify) else 'completed_with_readback_mismatch'

    payload={
        'generated_at': utc_now(),
        'approval': 'Lucas: segue o 2 (all 34 local/LIA GTINs; pilot 5 then scale 29)',
        'status': status,
        'source_labels':['manual_approval','fact_merchant_center','market_signal_kicks_dev'],
        'summary': {
            'approved_records': len(records),
            'pilot_records': len(pilot),
            'scaled_records': len(rest) if pilot_ok else 0,
            'execution_counts': dict(Counter(x['execution_status'] for x in execution)),
            'pilot_verify_counts': dict(Counter('match' if x.get('match_expected') else 'mismatch' for x in pilot_verify)),
            'scale_verify_counts': dict(Counter('match' if x.get('match_expected') else 'mismatch' for x in scale_verify)),
            'final_target_issue_counts': dict(Counter(code for row in final_status for code in row.get('target_issue_codes',[]))),
            'final_rows_with_target_issue': sum(1 for row in final_status if row.get('target_issue_codes')),
        },
        'rollback_snapshot_path': str(rollback_path),
        'progress_jsonl_path': str(progress_path),
        'execution_results': execution,
        'pilot_verified_results': pilot_verify,
        'scale_verified_results': scale_verify,
        'final_productstatus_results': final_status,
        'not_performed':['Shopify write','Tiny write','POS/local inventory config change','feed fetch/upload','price update','availability update','title/category/image update','campaign/message/send','supplier/contact/purchase']
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2)+'\n')
    lines=[
        '# LK GMC Local/LIA GTIN Apply — 2026-05-14','',
        f"Gerado em: `{payload['generated_at']}`",'',
        '## Resultado',
        f"- Status: `{status}`",
        f"- Aprovados: `{len(records)}`",
        f"- Piloto: `{len(pilot)}`; escala: `{len(rest) if pilot_ok else 0}`",
        f"- Execução: `{payload['summary']['execution_counts']}`",
        f"- Readback piloto: `{payload['summary']['pilot_verify_counts']}`",
        f"- Readback escala: `{payload['summary']['scale_verify_counts']}`",
        f"- Productstatuses finais com issue alvo GTIN: `{payload['summary']['final_rows_with_target_issue']}`; códigos `{payload['summary']['final_target_issue_counts']}`",
        '', '## Escopo executado',
        '- Content API `products.insert`/upsert em product IDs exatos `local:pt:BR:LIA_*`.',
        '- Recurso atual preservado; campo alterado: somente `gtin`.',
        '- Piloto 5 verificado antes de aplicar os 29 restantes.',
        '', '## Auditoria privada',
        f"- Rollback: `{rollback_path}`",
        f"- Progresso: `{progress_path}`",
        '', '## Não executado'
    ]
    lines += [f'- {x}' for x in payload['not_performed']]
    OUT_MD.write_text('\n'.join(lines)+'\n')
    BRAIN_MD.write_text(OUT_MD.read_text())
    print(json.dumps({'status':status,'summary':payload['summary'],'out_json':str(OUT_JSON),'out_md':str(OUT_MD)}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
