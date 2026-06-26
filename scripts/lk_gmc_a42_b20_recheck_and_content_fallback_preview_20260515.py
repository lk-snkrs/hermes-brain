#!/usr/bin/env python3
from __future__ import annotations

import csv
import importlib.util
import json
import pathlib
import time
import urllib.parse
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_UP
from typing import Any

ROOT = pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
ABC_PATH = ROOT / 'scripts/lk_execute_approved_abc_20260514.py'
PACKET_A = ROOT / 'reports/gmc_approval_packets_20260515/packet_a_price_only_42_preview.json'
PACKET_B = ROOT / 'reports/gmc_approval_packets_20260515/packet_b_draft404_20_preview.json'
RUN = '2026-05-15-a42-b20-recheck-content-fallback-preview'
OUT_JSON = ROOT / f'reports/lk-gmc-{RUN}.json'
OUT_CSV = ROOT / f'reports/lk-gmc-{RUN}-fallback-price-only.csv'
OUT_MD = ROOT / f'reports/lk-gmc-{RUN}.md'
BRAIN_MD = ROOT / f'areas/lk/rotinas/gmc-{RUN}.md'


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


def price_obj(value: str) -> dict[str, str]:
    return {'value': money(value), 'currency': 'BRL'}


def content_url(mid: str, pid: str) -> str:
    return f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/products/{urllib.parse.quote(pid, safe="")}'


def status_url(mid: str, pid: str) -> str:
    return f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/productstatuses/{urllib.parse.quote(pid, safe="")}'


def optional_get(url: str, token: str) -> dict[str, Any] | None:
    try:
        return abc.request_json(url, token=token)
    except Exception as e:
        if 'http_404' in str(e):
            return None
        raise


def merchant_v1(mid: str, token: str, pid: str) -> dict[str, Any] | None:
    try:
        _name, encoded, *_ = abc.product_input_name(mid, pid)
        return abc.merchant_product_get(mid, token, encoded)
    except Exception as e:
        return {'error': str(e)[:1000]}


def list_all(endpoint: str, mid: str, token: str) -> list[dict[str, Any]]:
    rows = []
    page = None
    while True:
        qs = {'maxResults': '250'}
        if page:
            qs['pageToken'] = page
        data = abc.request_json(f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/{endpoint}?' + urllib.parse.urlencode(qs), token=token)
        batch = data.get('resources') or []
        rows.extend(batch)
        page = data.get('nextPageToken')
        if not page or not batch:
            break
    return rows


def write_csv(path: pathlib.Path, rows: list[dict[str, Any]]) -> None:
    fields = ['product_id','offerId','title','source','current_content_price_brl','current_content_sale_price_brl','current_merchant_v1_price_brl','target_price_brl','fallback_decision','guardrails']
    with path.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        w.writeheader()
        for r in rows:
            w.writerow(r)


def main() -> None:
    packet_a = json.loads(PACKET_A.read_text())
    packet_b = json.loads(PACKET_B.read_text())
    sec = abc.load_doppler()
    mid = sec['MERCHANT_CENTER_ID_LK']
    token = abc.google_access_token(abc.parse_service_account(sec))

    recheck_a = []
    fallback = []
    for r in packet_a:
        pid = r['product_id']
        target = r['target_shopify_price_brl']
        cur = optional_get(content_url(mid, pid), token)
        v1 = merchant_v1(mid, token, pid) or {}
        pa = v1.get('productAttributes') or {}
        row = {
            'product_id': pid,
            'offerId': r.get('offerId'),
            'title': r.get('title'),
            'target_price_brl': target,
            'source': (cur or {}).get('source'),
            'current_content_price_brl': amount((cur or {}).get('price')),
            'current_content_sale_price_brl': amount((cur or {}).get('salePrice')),
            'current_merchant_v1_price_brl': amount(pa.get('price')),
            'current_merchant_v1_sale_price_brl': amount(pa.get('salePrice')),
            'content_match_expected': amount((cur or {}).get('price')) == target and amount((cur or {}).get('salePrice')) is None,
            'merchant_v1_match_expected': amount(pa.get('price')) == target and amount(pa.get('salePrice')) is None,
        }
        if not cur:
            row['fallback_decision'] = 'blocked_missing_content_product'
        elif cur.get('source') != 'api':
            row['fallback_decision'] = 'blocked_non_api_source'
        elif row['current_content_sale_price_brl'] is not None:
            row['fallback_decision'] = 'blocked_current_sale_price_present'
        elif row['current_content_price_brl'] == target:
            row['fallback_decision'] = 'no_action_already_matches'
        else:
            row['fallback_decision'] = 'candidate_content_api_upsert_price_only'
            product = json.loads(json.dumps(cur, ensure_ascii=False))
            product.pop('source', None)
            product['price'] = price_obj(target)
            product.pop('salePrice', None)
            fallback.append({
                **row,
                'guardrails': 'Content API products.insert/upsert full source=api resource; change price only; remove salePrice only if absent/current null; no Shopify/Tiny/feed/campaign',
                'planned_product_resource': product,
                'rollback_product_resource': cur,
            })
        recheck_a.append(row)
        time.sleep(0.08)

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
        'packet_a_content_matches': sum(1 for r in recheck_a if r['content_match_expected']),
        'packet_a_merchant_v1_matches': sum(1 for r in recheck_a if r['merchant_v1_match_expected']),
        'fallback_decision_counts': dict(Counter(r.get('fallback_decision') for r in recheck_a)),
        'fallback_candidates': len(fallback),
        'packet_b_targets': len(packet_b),
        'packet_b_absent_products_list': sum(1 for r in verify_b if r['absent_from_products_list']),
        'packet_b_absent_productstatuses_list': sum(1 for r in verify_b if r['absent_from_productstatuses_list']),
    }
    payload = {
        'generated_at': now(),
        'status': 'fallback_preview_ready_no_write',
        'merchant_id': mid,
        'summary': summary,
        'recheck_a': recheck_a,
        'fallback_price_only_candidates': fallback,
        'verify_b': verify_b,
        'not_performed': ['Content API upsert', 'Merchant ProductInputs PATCH', 'Shopify write', 'Tiny write', 'feed fetch/upload', 'salePrice/strikethrough update', 'campaign/message/contact'],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
    write_csv(OUT_CSV, fallback)
    lines = [
        '# LK GMC — A42/B20 recheck + Content API fallback preview', '',
        f"Gerado em: `{payload['generated_at']}`", f"Status: `{payload['status']}`", '',
        '## Recheck',
        f"- A Content API match: `{summary['packet_a_content_matches']}/42`",
        f"- A Merchant API v1 match: `{summary['packet_a_merchant_v1_matches']}/42`",
        f"- B ausente products.list: `{summary['packet_b_absent_products_list']}/20`",
        f"- B ausente productstatuses.list: `{summary['packet_b_absent_productstatuses_list']}/20`", '',
        '## Fallback preparado',
        f"- Candidatos Content API price-only: `{summary['fallback_candidates']}`",
        f"- Decisões: `{summary['fallback_decision_counts']}`",
        '- Escopo planejado: `products.insert`/upsert Content API para recursos `source=api`, preservando recurso completo e alterando apenas `price`.',
        '- Excluído: `salePrice`, strikethrough, Shopify, Tiny, feed, campanha.', '',
        '## Aprovação necessária',
        '',
        'Para executar o fallback, usar frase explícita:',
        '',
        '`aprovo GMC fallback Content API price-only 42`', '',
        'Sem isso, não executar write adicional.', '',
        '## Artefatos',
        f"- JSON: `{OUT_JSON}`",
        f"- CSV: `{OUT_CSV}`", '',
        '## Não executado',
    ] + [f'- {x}' for x in payload['not_performed']]
    OUT_MD.write_text('\n'.join(lines) + '\n')
    BRAIN_MD.parent.mkdir(parents=True, exist_ok=True)
    BRAIN_MD.write_text(OUT_MD.read_text())
    print(json.dumps({'summary': summary, 'report': str(BRAIN_MD), 'json': str(OUT_JSON)}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
