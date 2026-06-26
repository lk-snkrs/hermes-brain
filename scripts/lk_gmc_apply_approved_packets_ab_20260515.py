#!/usr/bin/env python3
from __future__ import annotations

import csv
import importlib.util
import json
import os
import pathlib
import sqlite3
import time
import urllib.parse
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_UP
from typing import Any

ROOT = pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
ABC_PATH = ROOT / 'scripts/lk_execute_approved_abc_20260514.py'
PACKET_DIR = ROOT / 'reports/gmc_approval_packets_20260515'
PACKET_A = PACKET_DIR / 'packet_a_price_only_42_preview.json'
PACKET_B = PACKET_DIR / 'packet_b_draft404_20_preview.json'
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
LOCAL_DB = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite')
RUN = '2026-05-15-approved-packets-a42-b20'
OUT_JSON = ROOT / f'reports/lk-gmc-{RUN}.json'
OUT_CSV_A = ROOT / f'reports/lk-gmc-{RUN}-price-a42.csv'
OUT_CSV_B = ROOT / f'reports/lk-gmc-{RUN}-draft404-b20.csv'
OUT_MD = ROOT / f'reports/lk-gmc-{RUN}.md'
BRAIN_MD = ROOT / f'areas/lk/rotinas/gmc-{RUN}.md'
APPROVAL = 'Lucas approved all GMC packets A42 price-only and B20 DRAFT/404 suppress/delete in Telegram: aprovo todos'
DATA_SOURCE_ID = '10636492695'


def load_module(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(mod)
    return mod

abc = load_module(ABC_PATH, 'abc')


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def money_from_micros(v: Any) -> str | None:
    if v is None:
        return None
    try:
        return f"{Decimal(int(v)) / Decimal(1_000_000):.2f}"
    except Exception:
        return None


def amount(resource: dict[str, Any] | None) -> str | None:
    if not isinstance(resource, dict):
        return None
    if resource.get('value') is not None:
        try:
            return f"{Decimal(str(resource.get('value'))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}"
        except Exception:
            return str(resource.get('value'))
    if resource.get('amountMicros') is not None:
        return money_from_micros(resource.get('amountMicros'))
    return None


def content_product_url(mid: str, pid: str) -> str:
    return f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/products/{urllib.parse.quote(pid, safe="")}'


def status_url(mid: str, pid: str) -> str:
    return f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/productstatuses/{urllib.parse.quote(pid, safe="")}'


def request_optional(url: str, token: str) -> dict[str, Any] | None:
    try:
        return abc.request_json(url, token=token)
    except Exception as e:
        if 'http_404' in str(e):
            return None
        raise


def delete_product(mid: str, token: str, pid: str) -> dict[str, Any]:
    try:
        resp = abc.request_json(content_product_url(mid, pid), token=token, method='DELETE')
        return {'delete_status': 'deleted', 'response': resp}
    except Exception as e:
        if 'http_404' in str(e):
            return {'delete_status': 'already_absent_404'}
        raise


def list_all(endpoint: str, mid: str, token: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    page = None
    while True:
        qs = {'maxResults': '250'}
        if page:
            qs['pageToken'] = page
        url = f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/{endpoint}?' + urllib.parse.urlencode(qs)
        data = abc.request_json(url, token=token)
        batch = data.get('resources') or []
        rows.extend(batch)
        page = data.get('nextPageToken')
        if not page or not batch:
            break
    return rows


def merchant_product_v1(mid: str, token: str, pid: str) -> dict[str, Any]:
    _name, encoded, *_ = abc.product_input_name(mid, pid)
    return abc.merchant_product_get(mid, token, encoded)


def patch_price(mid: str, token: str, row: dict[str, Any]) -> dict[str, Any]:
    attrs = {'price': {'amountMicros': int(row['target_amountMicros']), 'currencyCode': row['currencyCode']}}
    return abc.patch_product_input_attrs(mid, token, row['product_id'], attrs)


def write_csv(path: pathlib.Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    with path.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        w.writeheader()
        for r in rows:
            w.writerow(r)


def log_ledger(payload: dict[str, Any]) -> None:
    if not LOCAL_DB.exists():
        return
    con = sqlite3.connect(str(LOCAL_DB))
    try:
        cols = [r[1] for r in con.execute('pragma table_info(lk_approval_decision_ledger)')]
        if 'decision_id' in cols:
            con.execute('''
                insert or replace into lk_approval_decision_ledger
                (decision_id,created_at,updated_at,business,domain,source_request,rule_id,status,risk_level,allowed_next_action,blocked_actions,requires_future_approval,external_or_visible_write_done,evidence_artifact,learning,owner)
                values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            ''', (
                'gmc_apply_approved_packets_a42_b20_20260515',
                payload['generated_at'], payload['generated_at'], 'LK', 'GMC',
                'Lucas: aprovo todos', 'LK-APPROVAL-GMC-GATE-20260515', payload['status'], 'A3',
                'Monitor delayed productstatuses and rollback if verification anomalies remain after propagation.',
                'No additional bulk writes; no salePrice/strikethrough; no Shopify publish/write; no feed fetch/upload; no external send.',
                0, 1, str(BRAIN_MD), json.dumps(payload['summary'], ensure_ascii=False), 'Hermes',
            ))
            con.commit()
    finally:
        con.close()


def main() -> None:
    packet_a = json.loads(PACKET_A.read_text())
    packet_b = json.loads(PACKET_B.read_text())
    if len(packet_a) != 42:
        raise RuntimeError(f'blocked_expected_42_price_rows_got_{len(packet_a)}')
    if len(packet_b) != 20:
        raise RuntimeError(f'blocked_expected_20_draft404_rows_got_{len(packet_b)}')
    for r in packet_a:
        if r.get('updateMask') != 'productAttributes.price' or 'no salePrice' not in r.get('guardrails', ''):
            raise RuntimeError('blocked_packet_a_guardrail_failed')
    for r in packet_b:
        if str(r.get('shopify_status')) not in {'DRAFT', 'ARCHIVED'} or str(r.get('public_get_status')) != '404' or str(r.get('public_js_status')) != '404':
            raise RuntimeError('blocked_packet_b_guardrail_failed')

    sec = abc.load_doppler()
    mid = sec['MERCHANT_CENTER_ID_LK']
    token = abc.google_access_token(abc.parse_service_account(sec))

    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE_DIR, 0o700)
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    rollback = PRIVATE_DIR / f'lk-gmc-{RUN}-rollback-{stamp}.json'
    progress = PRIVATE_DIR / f'lk-gmc-{RUN}-progress-{stamp}.jsonl'

    rollback_records_a = []
    rollback_records_b = []
    for r in packet_a:
        cur_content = request_optional(content_product_url(mid, r['product_id']), token)
        try:
            cur_v1 = merchant_product_v1(mid, token, r['product_id'])
        except Exception as e:
            cur_v1 = {'error': str(e)[:1000]}
        rollback_records_a.append({'packet': r, 'current_content_api_product_resource': cur_content, 'current_merchant_v1_product_resource': cur_v1})
        time.sleep(0.08)
    for r in packet_b:
        cur_content = request_optional(content_product_url(mid, r['product_id']), token)
        cur_status = request_optional(status_url(mid, r['product_id']), token)
        rollback_records_b.append({'packet': r, 'current_content_api_product_resource': cur_content, 'current_productstatus_resource': cur_status})
        time.sleep(0.08)

    rollback.write_text(json.dumps({
        'generated_at': now(),
        'approval': APPROVAL,
        'scope': 'Apply packet A42 productAttributes.price only; apply packet B20 Content API product delete/suppress for DRAFT/404 only.',
        'data_source': f'accounts/*/dataSources/{DATA_SOURCE_ID}',
        'packet_a_records': rollback_records_a,
        'packet_b_records': rollback_records_b,
        'rollback_instruction': 'For A, patch productAttributes.price back to captured current price. For B, recreate/reprocess from captured current_content_api_product_resource only after confirming Shopify visibility intent.',
    }, ensure_ascii=False, indent=2) + '\n')
    os.chmod(rollback, 0o600)

    exec_a = []
    exec_b = []
    with progress.open('w', encoding='utf-8') as f:
        os.chmod(progress, 0o600)
        for r in packet_a:
            try:
                resp = patch_price(mid, token, r)
                item = {'packet': 'A', 'product_id': r['product_id'], 'execution_status': 'patched_price_only_v1', 'expected_price_brl': r['target_shopify_price_brl'], 'response_name': resp.get('name')}
            except Exception as e:
                item = {'packet': 'A', 'product_id': r['product_id'], 'execution_status': 'failed_patch_price_only_v1', 'expected_price_brl': r['target_shopify_price_brl'], 'error': str(e)[:1500]}
                exec_a.append(item); f.write(json.dumps(item, ensure_ascii=False) + '\n'); f.flush(); break
            exec_a.append(item); f.write(json.dumps(item, ensure_ascii=False) + '\n'); f.flush(); time.sleep(0.35)
        for r in packet_b:
            try:
                res = delete_product(mid, token, r['product_id'])
                item = {'packet': 'B', 'product_id': r['product_id'], 'execution_status': res['delete_status'], 'title': r.get('title')}
            except Exception as e:
                item = {'packet': 'B', 'product_id': r['product_id'], 'execution_status': 'failed_delete', 'title': r.get('title'), 'error': str(e)[:1500]}
                exec_b.append(item); f.write(json.dumps(item, ensure_ascii=False) + '\n'); f.flush(); break
            exec_b.append(item); f.write(json.dumps(item, ensure_ascii=False) + '\n'); f.flush(); time.sleep(0.35)

    time.sleep(90)
    verify_a = []
    for r in packet_a:
        expected = r['target_shopify_price_brl']
        row = {'product_id': r['product_id'], 'expected_price_brl': expected}
        try:
            cp = request_optional(content_product_url(mid, r['product_id']), token)
            row['content_api_price_brl'] = amount((cp or {}).get('price'))
            row['content_api_sale_price_brl'] = amount((cp or {}).get('salePrice'))
            row['content_api_match_expected'] = row['content_api_price_brl'] == expected and row['content_api_sale_price_brl'] is None
        except Exception as e:
            row['content_api_error'] = str(e)[:1000]
            row['content_api_match_expected'] = False
        try:
            mp = merchant_product_v1(mid, token, r['product_id'])
            pa = mp.get('productAttributes') or {}
            row['merchant_v1_price_brl'] = amount(pa.get('price'))
            row['merchant_v1_sale_price_brl'] = amount(pa.get('salePrice'))
            row['merchant_v1_match_expected'] = row['merchant_v1_price_brl'] == expected and row['merchant_v1_sale_price_brl'] is None
        except Exception as e:
            row['merchant_v1_error'] = str(e)[:1000]
            row['merchant_v1_match_expected'] = False
        verify_a.append(row); time.sleep(0.12)

    products = list_all('products', mid, token)
    statuses = list_all('productstatuses', mid, token)
    live_ids = {p.get('id') for p in products}
    status_ids = {s.get('productId') for s in statuses}
    verify_b = []
    for r in packet_b:
        verify_b.append({
            'product_id': r['product_id'],
            'absent_from_products_list': r['product_id'] not in live_ids,
            'absent_from_productstatuses_list': r['product_id'] not in status_ids,
        })

    summary = {
        'packet_a_targets': len(packet_a),
        'packet_b_targets': len(packet_b),
        'packet_a_execution_counts': dict(Counter(x.get('execution_status') for x in exec_a)),
        'packet_b_execution_counts': dict(Counter(x.get('execution_status') for x in exec_b)),
        'packet_a_content_api_matches': sum(1 for x in verify_a if x.get('content_api_match_expected')),
        'packet_a_merchant_v1_matches': sum(1 for x in verify_a if x.get('merchant_v1_match_expected')),
        'packet_b_absent_products_list': sum(1 for x in verify_b if x.get('absent_from_products_list')),
        'packet_b_absent_productstatuses_list': sum(1 for x in verify_b if x.get('absent_from_productstatuses_list')),
        'rollback_path': str(rollback),
        'progress_path': str(progress),
    }
    ok_a = summary['packet_a_execution_counts'].get('patched_price_only_v1', 0) == len(packet_a) and summary['packet_a_merchant_v1_matches'] == len(packet_a)
    ok_b = summary['packet_b_absent_products_list'] == len(packet_b) and summary['packet_b_absent_productstatuses_list'] == len(packet_b) and not any(x.get('execution_status') == 'failed_delete' for x in exec_b)
    status = 'applied_verified' if ok_a and ok_b else 'applied_needs_review_or_delayed_propagation'

    payload = {
        'generated_at': now(),
        'status': status,
        'approval': APPROVAL,
        'merchant_id': mid,
        'data_source': f'accounts/*/dataSources/{DATA_SOURCE_ID}',
        'summary': summary,
        'execution_a': exec_a,
        'execution_b': exec_b,
        'verify_a': verify_a,
        'verify_b': verify_b,
        'private_rollback_snapshot_path': str(rollback),
        'private_progress_path': str(progress),
        'not_performed': ['salePrice/strikethrough update', 'Shopify write/publish', 'Tiny write', 'feed fetch/upload/fetchNow', 'campaign/message/WhatsApp/supplier/customer contact'],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
    write_csv(OUT_CSV_A, verify_a, ['product_id', 'expected_price_brl', 'content_api_price_brl', 'content_api_sale_price_brl', 'content_api_match_expected', 'merchant_v1_price_brl', 'merchant_v1_sale_price_brl', 'merchant_v1_match_expected', 'content_api_error', 'merchant_v1_error'])
    write_csv(OUT_CSV_B, verify_b, ['product_id', 'absent_from_products_list', 'absent_from_productstatuses_list'])

    lines = [
        '# LK GMC — Approved packets A42/B20 execution', '',
        f"Gerado em: `{payload['generated_at']}`", f"Status: `{status}`", '',
        '## Escopo aprovado',
        '- Pacote A: 42 IDs `price-only`, campo `productAttributes.price` somente.',
        '- Pacote B: 20 IDs Shopify DRAFT/404 para delete/suppress no Merchant.',
        '- Aprovação: `aprovo todos` no Telegram.', '',
        '## Resultado',
        f"- A execução: `{summary['packet_a_execution_counts']}`",
        f"- A Merchant API v1 match: `{summary['packet_a_merchant_v1_matches']}/42`",
        f"- A Content API match: `{summary['packet_a_content_api_matches']}/42`",
        f"- B execução: `{summary['packet_b_execution_counts']}`",
        f"- B ausente em products.list: `{summary['packet_b_absent_products_list']}/20`",
        f"- B ausente em productstatuses.list: `{summary['packet_b_absent_productstatuses_list']}/20`",
        '', '## Rollback/progresso privado',
        f"- Rollback: `{rollback}`", f"- Progress: `{progress}`", '',
        '## Artefatos públicos',
        f"- JSON: `{OUT_JSON}`", f"- CSV A: `{OUT_CSV_A}`", f"- CSV B: `{OUT_CSV_B}`", '',
        '## Não executado',
    ] + [f'- {x}' for x in payload['not_performed']]
    BRAIN_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text('\n'.join(lines) + '\n')
    BRAIN_MD.write_text(OUT_MD.read_text())
    log_ledger(payload)
    print(json.dumps({'status': status, 'summary': summary, 'report': str(BRAIN_MD)}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
