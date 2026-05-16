#!/usr/bin/env python3
"""LK GMC P2B/B size-in-title pilot executor.

Patches only productAttributes.title on Merchant API v1 ProductInputs for the
100 approved shoe variants preview where adding size to GMC title is a controlled
pilot. Does not change Shopify.
"""
from __future__ import annotations
import argparse, base64, csv, importlib.util, json, os, pathlib, time, urllib.error, urllib.parse, urllib.request
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
W4 = ROOT / 'scripts/lk_gmc_p1_attribute_wave4_aggressive_nonprice_executor_20260513.py'
TITLE_PREVIEW = ROOT / 'reports/lk-gmc-2026-05-13-p2b-size-title-pilot-b-preview.csv'
RUN_STAMP = '2026-05-13-p2b-size-title-pilot-b-executor'
PUBLIC_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
PUBLIC_CSV = ROOT / f'reports/lk-gmc-{RUN_STAMP}.csv'
PUBLIC_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
APPROVAL_TEXT_REQUIRED = 'Aprovo aplicar o piloto B nos 100 títulos de tênis do preview, somente no GMC/ProductInput, com rollback e verificação; não alterar Shopify'
DATA_SOURCE_ID = '10636492695'


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def import_w4():
    spec = importlib.util.spec_from_file_location('w4', W4)
    mod = importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(mod)
    return mod


def b64url_no_pad(s: str) -> str:
    return base64.urlsafe_b64encode(s.encode()).decode().rstrip('=')


def product_parts(content_api_id: str) -> tuple[str, str, str, str]:
    parts = content_api_id.split(':', 3)
    if len(parts) != 4:
        raise ValueError(f'bad_content_api_product_id: {content_api_id}')
    return parts[0], parts[1], parts[2], parts[3]


def product_input_name(mid: str, pid: str) -> tuple[str, str, str, str, str]:
    channel, lang, label, offer = product_parts(pid)
    if channel != 'online':
        raise ValueError(f'only_online_supported_for_size_title_pilot_b: {pid}')
    encoded = b64url_no_pad(f'{lang}~{label}~{offer}')
    return f'accounts/{mid}/productInputs/{encoded}', encoded, lang, label, offer


def request_json(url: str, token: str, method: str = 'GET', payload: dict[str, Any] | None = None, attempts: int = 6) -> dict[str, Any]:
    data = None if payload is None else json.dumps(payload, ensure_ascii=False).encode()
    last = ''
    for i in range(1, attempts + 1):
        req = urllib.request.Request(url, data=data, method=method)
        req.add_header('Authorization', 'Bearer ' + token)
        if payload is not None:
            req.add_header('Content-Type', 'application/json; charset=utf-8')
        try:
            with urllib.request.urlopen(req, timeout=150) as r:
                raw = r.read().decode()
                return json.loads(raw) if raw else {}
        except urllib.error.HTTPError as e:
            raw = e.read().decode(errors='replace')
            last = f'http_{e.code}: {raw[:1500]}'
            if e.code not in {429, 500, 502, 503, 504} or i == attempts:
                raise RuntimeError(last) from e
        except Exception as e:
            last = str(e)[:1500]
            if i == attempts:
                raise RuntimeError(last) from e
        time.sleep(min(90, 2 ** i))
    raise RuntimeError(last or 'request_failed')


def merchant_product_get(mid: str, encoded_product: str, token: str) -> dict[str, Any]:
    name = f'accounts/{mid}/products/{encoded_product}'
    return request_json('https://merchantapi.googleapis.com/products/v1/' + urllib.parse.quote(name, safe='/'), token)


def patch_title(mid: str, token: str, pid: str, title: str) -> dict[str, Any]:
    name, _encoded, lang, label, offer = product_input_name(mid, pid)
    body = {
        'name': name,
        'offerId': offer,
        'contentLanguage': lang,
        'feedLabel': label,
        'productAttributes': {'title': title},
    }
    data_source = f'accounts/{mid}/dataSources/{DATA_SOURCE_ID}'
    qs = urllib.parse.urlencode({'dataSource': data_source, 'updateMask': 'productAttributes.title'})
    url = 'https://merchantapi.googleapis.com/products/v1/' + urllib.parse.quote(name, safe='/') + '?' + qs
    return request_json(url, token, method='PATCH', payload=body)


def load_rows(limit: int) -> list[dict[str, Any]]:
    rows = []
    with TITLE_PREVIEW.open(encoding='utf-8') as f:
        for r in csv.DictReader(f):
            title = (r.get('proposed_gmc_title') or '').strip()
            if not title or len(title) > 150:
                raise RuntimeError(f'invalid_title_for_offer {r.get("offer_id")}: length={len(title)}')
            rows.append({
                'product_id': r['product_id'],
                'offer_id': r['offer_id'],
                'current_gmc_title': r['current_gmc_title'],
                'proposed_gmc_title': title,
                'shopify_product_title': r.get('shopify_product_title') or '',
                'variant_id': r.get('variant_id') or '',
                'variant_sku': r.get('variant_sku') or '',
                'size': r.get('size') or '',
                'confidence': r.get('confidence') or '',
                'source': r.get('source') or '',
                'link': r.get('link') or '',
                'selected_for_apply': True,
            })
    return rows[:limit]


def snapshot(records: list[dict[str, Any]], limit: int) -> pathlib.Path:
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True); os.chmod(PRIVATE_DIR, 0o700)
    path = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-rollback-{datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")}.json'
    path.write_text(json.dumps({
        'generated_at': utc_now(),
        'scope': f'P2B/B size-in-title pilot Merchant API v1 ProductInputs patch only; dataSource={DATA_SOURCE_ID}; limit={limit}',
        'approval_text_required': APPROVAL_TEXT_REQUIRED,
        'rollback_instruction': 'Use Merchant API v1 ProductInputs PATCH updateMask=productAttributes.title with previous title from current_content_api_product_resource.title if rollback is needed.',
        'records': records,
    }, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    os.chmod(path, 0o600); return path


def write_outputs(mode: str, rows: list[dict[str, Any]], exec_results: list[dict[str, Any]], verified: list[dict[str, Any]], rollback: pathlib.Path | None, limit: int):
    ec=Counter(x.get('execution_status') for x in exec_results); vc=Counter(x.get('verify_status') for x in verified)
    payload={
        'generated_at': utc_now(),
        'status': 'p2b_size_title_pilot_b_apply_verified' if mode=='apply' else 'p2b_size_title_pilot_b_dry_run_ready',
        'mode': mode,
        'api': 'Merchant API v1 ProductInputs PATCH',
        'data_source': f'accounts/*/dataSources/{DATA_SOURCE_ID}',
        'approval_required_for_apply': APPROVAL_TEXT_REQUIRED,
        'summary': {
            'selected_for_apply': len(rows), 'limit': limit,
            'execution_results_summary': dict(ec),
            'verify_results_summary': dict(vc),
            'verified_match_expected': sum(1 for x in verified if x.get('match_expected')),
        },
        'private_rollback_snapshot_path': str(rollback) if rollback else None,
        'rows': rows,
        'execution_results': exec_results,
        'verified_results': verified,
        'not_performed': ['shopify_write', 'shopify_title_update', 'handle_update', 'description_update', 'price_update', 'availability_update', 'googleProductCategory_update', 'productTypes_update', 'merchant_delete', 'tiny_write', 'database_write', 'feed_fetch_or_upload', 'message_or_campaign_send'],
    }
    PUBLIC_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    fields=['product_id','offer_id','current_gmc_title','proposed_gmc_title','shopify_product_title','variant_id','variant_sku','size','confidence','source','link','selected_for_apply']
    with PUBLIC_CSV.open('w', newline='', encoding='utf-8') as f:
        wr=csv.DictWriter(f, fieldnames=fields, extrasaction='ignore'); wr.writeheader(); wr.writerows(rows)
    lines=['# LK GMC P2B/B Size-in-title Pilot Executor — 2026-05-13','',f'Status: `{payload["status"]}`','', '## Escopo','- API: Merchant API v1 ProductInputs PATCH.','- Campo: `productAttributes.title` somente.',f'- Data source: `accounts/*/dataSources/{DATA_SOURCE_ID}`','- Sem alteração de título visível da Shopify.', '', '## Resultado',f'- Selecionados: {len(rows)}',f'- Execution: {dict(ec)}',f'- Verify: {dict(vc)}',f'- Match esperado: {payload["summary"]["verified_match_expected"]}/{len(verified)}', '', '## Rollback privado', f'- `{rollback}`' if rollback else '- Não criado no dry-run.', '', '## Não executado']
    for x in payload['not_performed']: lines.append(f'- {x}')
    PUBLIC_MD.write_text('\n'.join(lines)+'\n', encoding='utf-8')
    BRAIN_DOC.parent.mkdir(parents=True, exist_ok=True); BRAIN_DOC.write_text(PUBLIC_MD.read_text(encoding='utf-8'), encoding='utf-8')
    print(json.dumps({'status': payload['status'], 'summary': payload['summary'], 'report': str(PUBLIC_MD), 'rollback': str(rollback) if rollback else None}, ensure_ascii=False, indent=2))


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--apply', action='store_true'); ap.add_argument('--approval-text', default=''); ap.add_argument('--limit', type=int, default=100); ap.add_argument('--verify-delay', type=int, default=150)
    args=ap.parse_args(); mode='apply' if args.apply else 'dry-run'
    if args.apply and args.approval_text != APPROVAL_TEXT_REQUIRED:
        raise RuntimeError(f'apply_blocked_missing_exact_approval_text: {APPROVAL_TEXT_REQUIRED}')
    rows=load_rows(args.limit); exec_results=[]; verified=[]; rollback=None
    if args.apply:
        w=import_w4(); audit=w.import_audit(); secrets=audit.load_doppler(); mid=secrets.get('MERCHANT_CENTER_ID_LK'); token=audit.google_access_token(audit.parse_service_account(secrets))
        products={p.get('id'):p for p in w.list_all('products', mid, token)}
        records=[]
        for r in rows:
            cur=products.get(r['product_id'])
            if not cur: raise RuntimeError('current_product_missing: '+r['product_id'])
            records.append({'product_id': r['product_id'], 'current_content_api_product_resource': cur, 'planned_update': r})
        rollback=snapshot(records, args.limit)
        progress = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-progress-{rollback.stem.rsplit("-",1)[-1]}.jsonl'
        with progress.open('w', encoding='utf-8') as f:
            os.chmod(progress, 0o600)
            for rec in records:
                r=rec['planned_update']
                try:
                    resp=patch_title(mid, token, r['product_id'], r['proposed_gmc_title'])
                    item={'product_id': r['product_id'], 'offer_id': r['offer_id'], 'execution_status': 'patched_p2b_size_title_pilot_b_v1', 'product_input': resp.get('name')}
                except Exception as e:
                    item={'product_id': r['product_id'], 'offer_id': r['offer_id'], 'execution_status': 'failed_patch_v1', 'error': str(e)[:1500]}
                    exec_results.append(item); f.write(json.dumps(item, ensure_ascii=False)+'\n'); f.flush(); continue
                exec_results.append(item); f.write(json.dumps(item, ensure_ascii=False)+'\n'); f.flush(); time.sleep(0.25)
        if args.verify_delay: time.sleep(args.verify_delay)
        for res in exec_results:
            r=next((x for x in rows if x['product_id']==res['product_id']), None)
            if res.get('execution_status')!='patched_p2b_size_title_pilot_b_v1' or not r:
                verified.append({**res, 'verify_status': 'not_verified_due_to_execution_status'}); continue
            try:
                _name, encoded, _lang, _label, _offer = product_input_name(mid, r['product_id'])
                mp=merchant_product_get(mid, encoded, token)
                attrs=mp.get('productAttributes') or {}
                actual = attrs.get('title') or ''
                verified.append({**res, 'verify_status': 'verified_merchant_product_get', 'actual_title': actual, 'expected_title': r['proposed_gmc_title'], 'match_expected': actual == r['proposed_gmc_title']})
            except Exception as e:
                verified.append({**res, 'verify_status': 'verify_failed', 'verify_error': str(e)[:1200]})
    write_outputs(mode, rows, exec_results, verified, rollback, args.limit)

if __name__ == '__main__': main()
