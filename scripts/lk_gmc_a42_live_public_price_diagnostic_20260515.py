#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import pathlib
import re
import time
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_UP
from typing import Any

ROOT = pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
ABC_PATH = ROOT / 'scripts/lk_execute_approved_abc_20260514.py'
PACKET_A = ROOT / 'reports/gmc_approval_packets_20260515/packet_a_price_only_42_preview.json'
APPLY = ROOT / 'reports/lk-gmc-2026-05-15-content-api-price-only-fallback-a42.json'
RUN = '2026-05-15-a42-live-shopify-public-price-diagnostic'
OUT_JSON = ROOT / f'reports/lk-gmc-{RUN}.json'
OUT_MD = ROOT / f'areas/lk/rotinas/gmc-{RUN}.md'


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


def public_product_js(link: str) -> dict[str, Any]:
    parsed = urllib.parse.urlparse(link)
    parts = [p for p in parsed.path.split('/') if p]
    handle = None
    if 'products' in parts:
        i = parts.index('products')
        if i + 1 < len(parts):
            handle = parts[i+1]
    variant = (urllib.parse.parse_qs(parsed.query).get('variant') or [None])[0]
    if not handle:
        return {'error': 'no_handle'}
    url = f'https://lksneakers.com.br/products/{handle}.js'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 LKOS read-only price diagnostic'})
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.loads(r.read().decode())
        variants = data.get('variants') or []
        chosen = None
        if variant:
            chosen = next((v for v in variants if str(v.get('id')) == str(variant)), None)
        if not chosen and variants:
            chosen = variants[0]
        cents = chosen.get('price') if chosen else None
        compare_cents = chosen.get('compare_at_price') if chosen else None
        return {
            'handle': handle,
            'variant_id': variant,
            'status': 200,
            'public_variant_price_brl': money(Decimal(cents) / Decimal(100)) if cents is not None else None,
            'public_variant_compare_at_brl': money(Decimal(compare_cents) / Decimal(100)) if compare_cents is not None else None,
            'variant_title': chosen.get('title') if chosen else None,
        }
    except Exception as e:
        return {'handle': handle, 'variant_id': variant, 'error': str(e)[:800]}


def main() -> None:
    packet = json.loads(PACKET_A.read_text())
    apply = json.loads(APPLY.read_text())
    actual_by_pid = {r['product_id']: r for r in apply.get('rows', [])}
    rows = []
    for r in packet:
        actual = actual_by_pid.get(r['product_id'], {})
        pub = public_product_js(r.get('merchant_link') or '')
        row = {
            'product_id': r['product_id'],
            'title': r.get('title'),
            'target_from_local_snapshot_brl': r.get('target_shopify_price_brl'),
            'merchant_after_fallback_brl': actual.get('actual_price_brl'),
            **pub,
        }
        row['public_matches_merchant_after'] = pub.get('public_variant_price_brl') == row['merchant_after_fallback_brl']
        row['public_matches_target_snapshot'] = pub.get('public_variant_price_brl') == row['target_from_local_snapshot_brl']
        rows.append(row)
        time.sleep(0.15)
    summary = {
        'rows': len(rows),
        'public_matches_merchant_after': sum(1 for r in rows if r.get('public_matches_merchant_after')),
        'public_matches_target_snapshot': sum(1 for r in rows if r.get('public_matches_target_snapshot')),
        'public_errors': sum(1 for r in rows if r.get('error')),
        'public_price_relation_counts': dict(Counter('public_eq_merchant' if r.get('public_matches_merchant_after') else ('public_eq_target' if r.get('public_matches_target_snapshot') else 'public_diff_both') for r in rows)),
    }
    payload = {'generated_at': now(), 'status': 'read_only_live_public_price_diagnostic_complete', 'summary': summary, 'rows': rows, 'not_performed': ['Merchant write','Shopify write','Tiny write','feed fetch/upload','campaign/message/contact']}
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
    lines = ['# LK GMC — A42 live Shopify public price diagnostic', '', f"Gerado em: `{payload['generated_at']}`", f"Status: `{payload['status']}`", '', '## Resumo']
    for k, v in summary.items():
        lines.append(f'- {k}: `{v}`')
    lines += ['', '## Amostra']
    for r in rows[:12]:
        lines.append(f"- `{r['product_id']}` — public `{r.get('public_variant_price_brl')}` / Merchant pós `{r.get('merchant_after_fallback_brl')}` / target snapshot `{r.get('target_from_local_snapshot_brl')}` — {r.get('title')}")
    lines += ['', '## Interpretação', '- Se `public_matches_merchant_after` for alto, o Merchant está refletindo a vitrine pública e o snapshot local/Shopify usado como target estava stale ou divergente.', '- Nesse caso, não insistir em preço via Merchant; corrigir fonte Shopify/canal/loja primeiro.', '', '## Não executado'] + [f'- {x}' for x in payload['not_performed']]
    OUT_MD.write_text('\n'.join(lines) + '\n')
    print(json.dumps({'summary': summary, 'report': str(OUT_MD)}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
