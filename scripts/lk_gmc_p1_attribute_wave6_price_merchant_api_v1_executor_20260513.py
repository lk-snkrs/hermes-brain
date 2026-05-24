#!/usr/bin/env python3
"""LK GMC P1 Wave6 price completion via Merchant API ProductInputs v1.

Uses the previously generated Wave6 Shopify/Data Spine price source report and
patches only productAttributes.price on the API data source that rejected Content
API v2.1 price persistence. Creates private rollback snapshots from current
Content API processed products before writes and verifies both Merchant API v1
processed product and Content API product price.
"""
from __future__ import annotations
import argparse, base64, csv, importlib.util, json, os, pathlib, time, urllib.error, urllib.parse, urllib.request
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
W4 = ROOT / 'scripts/lk_gmc_p1_attribute_wave4_aggressive_nonprice_executor_20260513.py'
SOURCE_REPORT = ROOT / 'reports/lk-gmc-2026-05-13-p1-attribute-wave6-price-shopify-source-executor.json'
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
RUN_STAMP = '2026-05-13-p1-attribute-wave6-price-merchant-api-v1-executor'
PUBLIC_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
PUBLIC_CSV = ROOT / f'reports/lk-gmc-{RUN_STAMP}.csv'
PUBLIC_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
APPROVAL_TEXT_REQUIRED = 'Lucas approved Merchant API v1 registration and GMC P1 Wave6 price apply'
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
        raise ValueError(f'only_online_supported_for_wave6_price: {pid}')
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


def patch_price(mid: str, token: str, pid: str, value: str, currency: str) -> dict[str, Any]:
    name, _encoded, lang, label, offer = product_input_name(mid, pid)
    amount_micros = str(int(round(float(value) * 1_000_000)))
    body = {
        'name': name,
        'offerId': offer,
        'contentLanguage': lang,
        'feedLabel': label,
        'productAttributes': {'price': {'amountMicros': amount_micros, 'currencyCode': currency}},
    }
    data_source = f'accounts/{mid}/dataSources/{DATA_SOURCE_ID}'
    qs = urllib.parse.urlencode({'dataSource': data_source, 'updateMask': 'productAttributes.price'})
    url = 'https://merchantapi.googleapis.com/products/v1/' + urllib.parse.quote(name, safe='/') + '?' + qs
    return request_json(url, token, method='PATCH', payload=body)


def load_source_rows(limit: int) -> list[dict[str, Any]]:
    payload = json.loads(SOURCE_REPORT.read_text(encoding='utf-8'))
    rows = [r for r in payload.get('public_rows', []) if r.get('decision_state') == 'ready_for_wave6_price_apply' and r.get('suggested_attributes', {}).get('price')]
    return rows[:limit]


def snapshot(records: list[dict[str, Any]], limit: int) -> pathlib.Path:
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True); os.chmod(PRIVATE_DIR, 0o700)
    path = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-rollback-{datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")}.json'
    path.write_text(json.dumps({
        'generated_at': utc_now(),
        'scope': f'Merchant API v1 productAttributes.price patch only; dataSource={DATA_SOURCE_ID}; limit={limit}',
        'approval_text_required': APPROVAL_TEXT_REQUIRED,
        'rollback_instruction': 'Use Merchant API v1 PATCH with previous price if present, or remove price by patching updateMask productAttributes.price with empty value only if truly needed; prefer manual review because these rows originally lacked price.',
        'records': records,
    }, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    os.chmod(path, 0o600)
    return path


def status_recheck(w, mid: str, token: str) -> dict[str, Any]:
    statuses = w.list_all('productstatuses', mid, token)
    attr_counts = Counter()
    rows = 0
    for st in statuses:
        attrs = w.required_attrs(st)
        if attrs:
            rows += 1
            for a in attrs:
                attr_counts[a] += 1
    return {'fresh_productstatuses_after': len(statuses), 'required_attr_rows_after': rows, 'required_attr_counts_after': dict(attr_counts.most_common())}


def write_outputs(mode: str, rows: list[dict[str, Any]], exec_results: list[dict[str, Any]], verify_results: list[dict[str, Any]], rollback: pathlib.Path | None, post: dict[str, Any] | None):
    ec = Counter(r.get('execution_status') for r in exec_results)
    vc = Counter(r.get('verify_status') for r in verify_results)
    payload = {
        'generated_at': utc_now(),
        'status': 'merchant_api_v1_price_apply_verified' if mode == 'apply' else 'merchant_api_v1_price_dry_run_ready',
        'mode': mode,
        'scope': 'Patch only productAttributes.price via Merchant API ProductInputs v1; Shopify/Data Spine price source from Wave6 report.',
        'data_source': f'accounts/*/dataSources/{DATA_SOURCE_ID}',
        'approval_required_for_apply': APPROVAL_TEXT_REQUIRED,
        'summary': {
            'source_ready_rows': len(rows),
            'execution_results_summary': dict(ec),
            'verify_results_summary': dict(vc),
            'verified_content_price_match_expected': sum(1 for r in verify_results if r.get('content_price_match_expected')),
            'verified_merchant_price_match_expected': sum(1 for r in verify_results if r.get('merchant_price_match_expected')),
            **(post or {}),
        },
        'private_rollback_snapshot_path': str(rollback) if rollback else None,
        'public_rows': rows,
        'execution_results': exec_results,
        'verify_results': verify_results,
        'not_performed': ['merchant_delete', 'non_price_update', 'shopify_write', 'tiny_call_or_write', 'database_write', 'feed_fetch', 'campaign_or_message_send'],
    }
    PUBLIC_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    fields = ['product_id', 'offer_id', 'merchant_title', 'merchant_link', 'suggested_attributes', 'evidence', 'decision_state']
    with PUBLIC_CSV.open('w', newline='', encoding='utf-8') as f:
        wr = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore'); wr.writeheader()
        for r in rows:
            o = {k: r.get(k) for k in fields}; o['suggested_attributes'] = json.dumps(o.get('suggested_attributes'), ensure_ascii=False); o['evidence'] = json.dumps(o.get('evidence'), ensure_ascii=False); wr.writerow(o)
    lines = [
        '# LK GMC P1 Wave6 — Price via Merchant API v1', '', f'Status: `{payload["status"]}`', '',
        '## Escopo', '- Campo alterado: `productAttributes.price` somente.', '- Fonte de preço: Shopify/Data Spine, relatório Wave6.', f'- Data source: `accounts/*/dataSources/{DATA_SOURCE_ID}`', '',
        '## Resultado', f'- Linhas fonte: {len(rows)}', f'- Execução: {dict(ec)}', f'- Verificação Merchant API: {payload["summary"]["verified_merchant_price_match_expected"]}/{len(verify_results)}', f'- Verificação Content API: {payload["summary"]["verified_content_price_match_expected"]}/{len(verify_results)}',
    ]
    if post:
        lines += [f'- Required rows after: {post["required_attr_rows_after"]}', f'- Counts after: {post["required_attr_counts_after"]}']
    lines += ['', '## Rollback privado', f'- `{rollback}`' if rollback else '- Não criado no dry-run.', '', '## Não executado']
    lines += [f'- {x}' for x in payload['not_performed']]
    PUBLIC_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.parent.mkdir(parents=True, exist_ok=True)
    BRAIN_DOC.write_text(PUBLIC_MD.read_text(encoding='utf-8'), encoding='utf-8')
    print(json.dumps({'status': payload['status'], 'summary': payload['summary'], 'report': str(PUBLIC_MD), 'rollback': str(rollback) if rollback else None}, ensure_ascii=False, indent=2))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--approval-text', default='')
    ap.add_argument('--limit', type=int, default=1000)
    ap.add_argument('--verify-delay', type=int, default=120)
    ap.add_argument('--post-status-delay', type=int, default=180)
    args = ap.parse_args()
    mode = 'apply' if args.apply else 'dry-run'
    if args.apply and args.approval_text != APPROVAL_TEXT_REQUIRED:
        raise RuntimeError(f'apply_blocked_missing_exact_approval_text: {APPROVAL_TEXT_REQUIRED}')
    w = import_w4(); audit = w.import_audit(); secrets = audit.load_doppler(); mid = secrets.get('MERCHANT_CENTER_ID_LK')
    token = audit.google_access_token(audit.parse_service_account(secrets))
    rows = load_source_rows(args.limit)
    exec_results: list[dict[str, Any]] = []
    verify_results: list[dict[str, Any]] = []
    rollback = None
    if args.apply:
        records = []
        for r in rows:
            cur = w.get_product(mid, r['product_id'], token)
            records.append({'product_id': r['product_id'], 'current_content_api_product_resource': cur, 'planned_update': r})
        rollback = snapshot(records, args.limit)
        progress = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-progress-{rollback.stem.rsplit("-",1)[-1]}.jsonl'
        with progress.open('w', encoding='utf-8') as f:
            os.chmod(progress, 0o600)
            for r in rows:
                price = r['suggested_attributes']['price']
                try:
                    resp = patch_price(mid, token, r['product_id'], price['value'], price['currency'])
                    item = {'product_id': r['product_id'], 'execution_status': 'patched_price_v1', 'expected_price': price, 'product_input': resp.get('name')}
                except Exception as e:
                    item = {'product_id': r['product_id'], 'execution_status': 'failed_patch_v1', 'error': str(e)[:1500]}
                    exec_results.append(item); f.write(json.dumps(item, ensure_ascii=False) + '\n'); f.flush(); break
                exec_results.append(item); f.write(json.dumps(item, ensure_ascii=False) + '\n'); f.flush(); time.sleep(0.25)
        if args.verify_delay:
            time.sleep(args.verify_delay)
        for item in exec_results:
            r = next((x for x in rows if x['product_id'] == item['product_id']), None)
            if item.get('execution_status') != 'patched_price_v1' or not r:
                verify_results.append({**item, 'verify_status': 'not_verified_due_to_execution_status'}); continue
            expected = r['suggested_attributes']['price']
            expected_micros = str(int(round(float(expected['value']) * 1_000_000)))
            try:
                _name, encoded, _lang, _label, _offer = product_input_name(mid, r['product_id'])
                mp = merchant_product_get(mid, encoded, token)
                cp = w.get_product(mid, r['product_id'], token)
                mprice = (mp.get('productAttributes') or {}).get('price') or {}
                cprice = cp.get('price') or {}
                verify_results.append({
                    **item,
                    'verify_status': 'verified_gets',
                    'merchant_price': mprice,
                    'content_price': cprice,
                    'merchant_price_match_expected': mprice.get('amountMicros') == expected_micros and mprice.get('currencyCode') == expected['currency'],
                    'content_price_match_expected': cprice.get('value') == expected['value'] and cprice.get('currency') == expected['currency'],
                })
            except Exception as e:
                verify_results.append({**item, 'verify_status': 'verify_failed', 'verify_error': str(e)[:1500]})
        if args.post_status_delay:
            time.sleep(args.post_status_delay)
        post = status_recheck(w, mid, token)
    else:
        post = None
    write_outputs(mode, rows, exec_results, verify_results, rollback, post)


if __name__ == '__main__':
    main()
