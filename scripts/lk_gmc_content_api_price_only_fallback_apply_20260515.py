#!/usr/bin/env python3
from __future__ import annotations

import csv
import importlib.util
import json
import os
import pathlib
import sqlite3
import time
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_UP
from typing import Any

ROOT = pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
ABC_PATH = ROOT / 'scripts/lk_execute_approved_abc_20260514.py'
SRC = ROOT / 'reports/lk-gmc-2026-05-15-a42-b20-recheck-content-fallback-preview.json'
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
LOCAL_DB = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite')
RUN = '2026-05-15-content-api-price-only-fallback-a42'
OUT_JSON = ROOT / f'reports/lk-gmc-{RUN}.json'
OUT_CSV = ROOT / f'reports/lk-gmc-{RUN}.csv'
OUT_MD = ROOT / f'reports/lk-gmc-{RUN}.md'
BRAIN_MD = ROOT / f'areas/lk/rotinas/gmc-{RUN}.md'
APPROVAL = 'Lucas approved GMC fallback Content API price-only 42 in Telegram: Aprovo'


def load_module(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(mod)
    return mod

abc = load_module(ABC_PATH, 'abc')


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def money(v: Any) -> str | None:
    if v in (None, ''):
        return None
    try:
        return f"{Decimal(str(v)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}"
    except Exception:
        return str(v)


def amount(d: Any) -> str | None:
    if not isinstance(d, dict):
        return None
    if 'value' in d:
        return money(d.get('value'))
    if 'amountMicros' in d:
        return money(Decimal(int(d['amountMicros'])) / Decimal(1_000_000))
    return None


def upsert_content_product(mid: str, token: str, product: dict[str, Any]) -> dict[str, Any]:
    p = json.loads(json.dumps(product, ensure_ascii=False))
    p.pop('source', None)
    return abc.request_json(f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/products', token=token, method='POST', payload=p, attempts=5, timeout=150)


def write_csv(path: pathlib.Path, rows: list[dict[str, Any]]) -> None:
    fields = ['product_id','execution_status','expected_price_brl','actual_price_brl','actual_sale_price_brl','match_expected','response_id','error']
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
                'gmc_content_api_price_only_fallback_a42_20260515', payload['generated_at'], payload['generated_at'],
                'LK', 'GMC', 'Lucas: Aprovo', 'LK-APPROVAL-GMC-GATE-20260515', payload['status'], 'A3',
                'Monitor productstatuses after delayed propagation; rollback only if price mismatch/regression is confirmed.',
                'No salePrice/strikethrough; no Shopify/Tiny/feed/campaign/external send.',
                0, 1, str(BRAIN_MD), json.dumps(payload['summary'], ensure_ascii=False), 'Hermes'
            ))
            con.commit()
    finally:
        con.close()


def main() -> None:
    preview = json.loads(SRC.read_text())
    rows = preview.get('fallback_price_only_candidates') or []
    if len(rows) != 42:
        raise RuntimeError(f'blocked_expected_42_candidates_got_{len(rows)}')
    for r in rows:
        if r.get('fallback_decision') != 'candidate_content_api_upsert_price_only':
            raise RuntimeError('blocked_non_candidate_in_fallback')
        if r.get('current_content_sale_price_brl') is not None:
            raise RuntimeError('blocked_sale_price_present')
        prod = r.get('planned_product_resource') or {}
        if amount(prod.get('salePrice')) is not None:
            raise RuntimeError('blocked_planned_sale_price_present')
        if amount(prod.get('price')) != r.get('target_price_brl'):
            raise RuntimeError('blocked_planned_price_mismatch')

    sec = abc.load_doppler()
    mid = sec['MERCHANT_CENTER_ID_LK']
    token = abc.google_access_token(abc.parse_service_account(sec))
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE_DIR, 0o700)
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    rollback = PRIVATE_DIR / f'lk-gmc-{RUN}-rollback-{stamp}.json'
    progress = PRIVATE_DIR / f'lk-gmc-{RUN}-progress-{stamp}.jsonl'
    rollback.write_text(json.dumps({
        'generated_at': now(),
        'approval': APPROVAL,
        'scope': 'Content API products.insert/upsert for 42 source=api resources; price only; no salePrice/strikethrough.',
        'records': [{'product_id': r['product_id'], 'rollback_product_resource': r['rollback_product_resource'], 'planned_product_resource': r['planned_product_resource'], 'target_price_brl': r['target_price_brl']} for r in rows],
        'rollback_instruction': 'Use Content API products.insert with rollback_product_resource if a price regression is confirmed; remove source field before upsert.',
    }, ensure_ascii=False, indent=2) + '\n')
    os.chmod(rollback, 0o600)

    execs = []
    with progress.open('w', encoding='utf-8') as f:
        os.chmod(progress, 0o600)
        for r in rows:
            try:
                resp = upsert_content_product(mid, token, r['planned_product_resource'])
                item = {'product_id': r['product_id'], 'execution_status': 'content_api_upserted_price_only', 'expected_price_brl': r['target_price_brl'], 'response_id': resp.get('id')}
            except Exception as e:
                item = {'product_id': r['product_id'], 'execution_status': 'error', 'expected_price_brl': r['target_price_brl'], 'error': str(e)[:1500]}
                execs.append(item); f.write(json.dumps(item, ensure_ascii=False) + '\n'); f.flush(); break
            execs.append(item); f.write(json.dumps(item, ensure_ascii=False) + '\n'); f.flush(); time.sleep(0.35)

    time.sleep(90)
    verify = []
    for r in rows:
        item = {'product_id': r['product_id'], 'expected_price_brl': r['target_price_brl']}
        try:
            cur = abc.content_product_get(mid, token, r['product_id'])
            item['actual_price_brl'] = amount(cur.get('price'))
            item['actual_sale_price_brl'] = amount(cur.get('salePrice'))
            item['source'] = cur.get('source')
            item['match_expected'] = item['actual_price_brl'] == r['target_price_brl'] and item['actual_sale_price_brl'] is None
        except Exception as e:
            item['match_expected'] = False
            item['error'] = str(e)[:1000]
        verify.append(item); time.sleep(0.08)

    merged = []
    by_exec = {x['product_id']: x for x in execs}
    for v in verify:
        merged.append({**by_exec.get(v['product_id'], {}), **v})
    summary = {
        'targets': len(rows),
        'execution_counts': dict(Counter(x.get('execution_status') for x in execs)),
        'verify_matches': sum(1 for x in verify if x.get('match_expected')),
        'verify_mismatches': sum(1 for x in verify if not x.get('match_expected')),
        'rollback_path': str(rollback),
        'progress_path': str(progress),
    }
    status = 'completed_verified' if summary['execution_counts'].get('content_api_upserted_price_only', 0) == 42 and summary['verify_matches'] == 42 else 'completed_needs_review'
    payload = {
        'generated_at': now(), 'status': status, 'approval': APPROVAL, 'merchant_id': mid,
        'summary': summary, 'rows': merged, 'rollback_path': str(rollback), 'progress_path': str(progress),
        'not_performed': ['salePrice/strikethrough update', 'Shopify write', 'Tiny write', 'feed fetch/upload/fetchNow', 'campaign/message/WhatsApp/supplier/customer contact'],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
    write_csv(OUT_CSV, merged)
    lines = [
        '# LK GMC — Content API price-only fallback A42', '',
        f"Gerado em: `{payload['generated_at']}`", f"Status: `{status}`", '',
        '## Escopo',
        '- Content API `products.insert`/upsert em 42 produtos `source=api`.',
        '- Campo comercial alterado: `price` somente.',
        '- `salePrice`/strikethrough fora do escopo.',
        '', '## Resultado',
        f"- Execução: `{summary['execution_counts']}`",
        f"- Verificados com preço esperado: `{summary['verify_matches']}/42`",
        f"- Mismatches: `{summary['verify_mismatches']}`",
        '', '## Rollback/progresso privado',
        f"- Rollback: `{rollback}`", f"- Progress: `{progress}`", '',
        '## Artefatos', f"- JSON: `{OUT_JSON}`", f"- CSV: `{OUT_CSV}`", '',
        '## Não executado',
    ] + [f'- {x}' for x in payload['not_performed']]
    OUT_MD.write_text('\n'.join(lines) + '\n')
    BRAIN_MD.parent.mkdir(parents=True, exist_ok=True)
    BRAIN_MD.write_text(OUT_MD.read_text())
    log_ledger(payload)
    print(json.dumps({'status': status, 'summary': summary, 'report': str(BRAIN_MD)}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
