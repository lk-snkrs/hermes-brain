#!/usr/bin/env python3
"""LK GMC P1-B availability approval packet using Tiny as stock truth.

Read-only by default: fetches current Merchant products/productstatuses, joins exact
online offer IDs to Tiny exact codigo and official-deposit stock, and produces a
no-write approval packet for setting Merchant availability. No Merchant, Tiny,
Shopify, feed, DB, POS, campaign or external writes are performed.
"""
from __future__ import annotations

import argparse
import base64
import csv
import importlib.util
import json
import os
import pathlib
import sqlite3
import time
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / 'scripts/lk_gmc_catalog_duplication_audit_20260512.py'
LOCAL_DB = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite')
DOPPLER_TOKEN_FILE = pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_reconciliation')
RUN_STAMP = '2026-05-12-p1-availability-tiny-packet'
OUT_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
OUT_CSV = ROOT / f'reports/lk-gmc-{RUN_STAMP}.csv'
OUT_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
PRIVATE_JSONL = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-tiny-stock-cache.jsonl'
PRIVATE_CSV = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-full-private.csv'
CONTROL = ROOT / 'areas/lk/projetos/lk-os-implementation-control.md'
INDEX = ROOT / 'empresa/rotinas/_index.md'
OFFICIAL_DEPOSIT = 'LK | CONTROLE ESTOQUE'
REQ_CODES = {'item_missing_required_attribute', 'missing_item_attribute_for_product_type'}
VALID_AVAILABILITY = {'in stock', 'out of stock'}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def import_audit():
    spec = importlib.util.spec_from_file_location('audit', AUDIT_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def load_secrets() -> dict[str, str]:
    token = os.environ.get('DOPPLER_TOKEN') or DOPPLER_TOKEN_FILE.read_text().strip()
    req = urllib.request.Request('https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json')
    req.add_header('Authorization', 'Basic ' + base64.b64encode((token + ':').encode()).decode())
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)


def tiny_call(token: str, method: str, params: dict[str, Any], attempts: int = 5) -> dict[str, Any]:
    last = ''
    for attempt in range(1, attempts + 1):
        data = urllib.parse.urlencode({**params, 'token': token, 'formato': 'json'}).encode()
        req = urllib.request.Request(f'https://api.tiny.com.br/api2/{method}.php', data=data, method='POST')
        try:
            with urllib.request.urlopen(req, timeout=90) as resp:
                return json.load(resp)
        except Exception as e:
            last = str(e)[:500]
            if attempt == attempts:
                raise
            time.sleep(min(30, 1.5 * attempt))
    raise RuntimeError(last or 'tiny_call_failed')


def chan(pid: str) -> str:
    return (pid or '').split(':', 1)[0] if ':' in (pid or '') else 'unknown'


def offer_id(pid: str) -> str:
    parts = (pid or '').split(':', 3)
    return parts[3] if len(parts) == 4 else pid


def norm_attr(attr: str) -> str:
    return (attr or '').strip().lower().replace('_', ' ')


def missing_required_attrs(status: dict[str, Any]) -> set[str]:
    return {
        norm_attr(i.get('attributeName') or '')
        for i in (status.get('itemLevelIssues') or [])
        if i.get('code') in REQ_CODES and norm_attr(i.get('attributeName') or '')
    }


def load_shopify_index() -> dict[str, dict[str, Any]]:
    if not LOCAL_DB.exists():
        return {}
    con = sqlite3.connect(str(LOCAL_DB))
    con.row_factory = sqlite3.Row
    rows = con.execute('''
        select v.sku, v.inventory_quantity, v.is_active as variant_is_active,
               v.price, v.barcode, v.source_variant_id, v.title as variant_title,
               p.title as product_title, p.status as product_status, p.handle
        from lk_product_variants v
        left join lk_products p on p.product_id = v.product_id
        where coalesce(v.sku,'') <> ''
    ''').fetchall()
    con.close()
    out: dict[str, dict[str, Any]] = {}
    for r in rows:
        sku = str(r['sku'] or '').strip()
        rec = dict(r)
        existing = out.get(sku)
        if not existing:
            out[sku] = rec
        elif str(existing.get('product_status') or '').lower() != 'active' and str(rec.get('product_status') or '').lower() == 'active':
            out[sku] = rec
    return out


def fetch_tiny_code_index(token: str, sleep_s: float = 1.0) -> dict[str, dict[str, Any]]:
    by_code: dict[str, dict[str, Any]] = {}
    page = 1
    total_pages = None
    while True:
        ret = {}
        for page_attempt in range(1, 6):
            body = tiny_call(token, 'produtos.pesquisa', {'pesquisa': '', 'pagina': page})
            ret = (body or {}).get('retorno') or {}
            if ret.get('status') == 'OK':
                break
            if str(ret.get('codigo_erro')) == '6':
                # Tiny temporarily blocks bursts. Treat as backpressure, not data.
                # Cool down and retry the same page; do not turn this into stock evidence.
                time.sleep(min(900, 120 * page_attempt))
                continue
            raise RuntimeError(f"tiny_produtos_pesquisa_failed_page_{page}: code={ret.get('codigo_erro')} status={ret.get('status')}")
        if ret.get('status') != 'OK':
            raise RuntimeError(f"tiny_produtos_pesquisa_rate_limited_page_{page}: code={ret.get('codigo_erro')} status={ret.get('status')}")
        if total_pages is None:
            try:
                total_pages = int(ret.get('numero_paginas') or 1)
            except Exception:
                total_pages = 1
        for wrap in ret.get('produtos') or []:
            prod = (wrap or {}).get('produto') or {}
            code = str(prod.get('codigo') or '').strip()
            if code and code not in by_code:
                by_code[code] = {
                    'tiny_id': str(prod.get('id') or ''),
                    'tiny_nome': prod.get('nome'),
                    'tiny_codigo': code,
                    'tiny_situacao': prod.get('situacao'),
                    'tiny_tipo_variacao': prod.get('tipoVariacao'),
                    'tiny_gtin_present': bool(prod.get('gtin')),
                }
        if page >= total_pages:
            break
        page += 1
        if sleep_s:
            time.sleep(sleep_s)
    return by_code


def load_stock_cache() -> dict[str, dict[str, Any]]:
    cache: dict[str, dict[str, Any]] = {}
    if not PRIVATE_JSONL.exists():
        return cache
    for line in PRIVATE_JSONL.read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except Exception:
            continue
        # Never reuse rate-limit/API-error rows as evidence for availability.
        if item.get('stock_decision_state') == 'blocked_tiny_stock_api_error' or item.get('tiny_stock_status') != 'OK':
            continue
        code = str(item.get('tiny_codigo') or item.get('offer_id') or '').strip()
        if code:
            cache[code] = item
    return cache


def official_saldo(produto: dict[str, Any]) -> tuple[bool, float | None, float | None, int]:
    deposits = produto.get('depositos') or []
    seen = False
    saldo = None
    reservado = None
    for wrap in deposits:
        dep = wrap.get('deposito') or {}
        if dep.get('nome') == OFFICIAL_DEPOSIT:
            seen = True
            raw = dep.get('saldo')
            if raw not in (None, ''):
                try:
                    saldo = float(str(raw).replace(',', '.'))
                except Exception:
                    saldo = None
            raw_res = dep.get('saldoReservado') or dep.get('reservado')
            if raw_res not in (None, ''):
                try:
                    reservado = float(str(raw_res).replace(',', '.'))
                except Exception:
                    reservado = None
    return seen, saldo, reservado, len(deposits)


def fetch_stock(token: str, tiny_meta: dict[str, Any]) -> dict[str, Any]:
    tiny_id = tiny_meta.get('tiny_id') or ''
    ret = {}
    for stock_attempt in range(1, 5):
        ret = tiny_call(token, 'produto.obter.estoque', {'id': tiny_id}).get('retorno') or {}
        if ret.get('status') == 'OK':
            break
        if str(ret.get('codigo_erro')) == '6':
            time.sleep(min(900, 120 * stock_attempt))
            continue
        break
    status = ret.get('status')
    if status != 'OK':
        return {
            **tiny_meta,
            'tiny_stock_status': status,
            'tiny_stock_error_code': ret.get('codigo_erro'),
            'tiny_stock_error': ret.get('erros') or ret.get('erro'),
            'tiny_official_deposit_seen': False,
            'tiny_official_deposit_saldo': None,
            'tiny_total_saldo': None,
            'tiny_deposit_count': 0,
            'proposed_availability': '',
            'stock_confidence': 'blocked_tiny_stock_api_error',
            'stock_decision_state': 'blocked_tiny_stock_api_error',
            'tiny_stock_checked_at': utc_now(),
        }
    prod = ret.get('produto') or {}
    seen, saldo, reservado, dep_count = official_saldo(prod)
    try:
        total_saldo = float(str(prod.get('saldo') or 0).replace(',', '.'))
    except Exception:
        total_saldo = None
    try:
        total_res = float(str(prod.get('saldoReservado') or 0).replace(',', '.'))
    except Exception:
        total_res = None
    if seen and saldo is not None:
        proposed = 'in stock' if saldo > 0 else 'out of stock'
        confidence = 'high_tiny_official_deposit'
        decision = 'ready_for_availability_apply_if_lucas_approves'
    elif total_saldo is not None:
        proposed = 'in stock' if total_saldo > 0 else 'out of stock'
        confidence = 'medium_tiny_total_stock_no_official_deposit'
        decision = 'blocked_review_no_official_deposit'
    else:
        proposed = ''
        confidence = 'blocked_no_tiny_stock_number'
        decision = 'blocked_no_tiny_stock_number'
    return {
        **tiny_meta,
        'tiny_stock_status': status,
        'tiny_official_deposit_seen': seen,
        'tiny_official_deposit_saldo': saldo,
        'tiny_official_deposit_reserved': reservado,
        'tiny_total_saldo': total_saldo,
        'tiny_total_reserved': total_res,
        'tiny_deposit_count': dep_count,
        'proposed_availability': proposed,
        'stock_confidence': confidence,
        'stock_decision_state': decision,
        'tiny_stock_checked_at': utc_now(),
    }


def main() -> None:
    raise SystemExit(
        'SUPERSEDED_BY_LUCAS_GMC_IN_STOCK_POLICY_2026_05_12: '
        'do not run Tiny-backed GMC availability packet. GMC availability should be `in stock` '
        'even when Tiny has zero/no stock; Tiny remains internal stockout/sourcing evidence only. '
        'Use a corrected Merchant availability-in-stock approval packet with rollback and Telegram-inline approval.'
    )
    ap = argparse.ArgumentParser()
    ap.add_argument('--limit', type=int, default=None, help='Limit rows for testing')
    ap.add_argument('--tiny-sleep', type=float, default=1.5, help='Sleep between Tiny stock calls')
    ap.add_argument('--tiny-index-sleep', type=float, default=1.0, help='Sleep between Tiny product-index pages')
    args = ap.parse_args()

    audit = import_audit()
    secrets = load_secrets()
    merchant_id = secrets.get('MERCHANT_CENTER_ID_LK')
    tiny_token = secrets.get('TINY_API_TOKEN') or ''
    if not merchant_id:
        raise RuntimeError('missing_merchant_center_id')
    if not tiny_token:
        raise RuntimeError('missing_tiny_api_token')
    gtoken = audit.google_access_token(audit.parse_service_account(secrets))
    products = audit.list_all('products', merchant_id, gtoken)
    statuses = audit.list_all('productstatuses', merchant_id, gtoken)
    product_by_id = {p.get('id'): p for p in products}
    shopify_by_sku = load_shopify_index()

    candidates = []
    for st in statuses:
        pid = st.get('productId') or ''
        attrs = missing_required_attrs(st)
        if chan(pid) == 'online' and 'availability' in attrs:
            prod = product_by_id.get(pid) or {}
            oid = offer_id(pid)
            candidates.append({
                'product_id': pid,
                'offer_id': oid,
                'diagnostic_required_attrs': sorted(attrs),
                'current_product_present': bool(prod),
                'current_availability': prod.get('availability') or '',
                'merchant_title': prod.get('title') or st.get('title') or '',
            })
    candidates = sorted(candidates, key=lambda r: r['product_id'])
    if args.limit:
        candidates = candidates[:args.limit]

    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE_DIR, 0o700)
    tiny_index = fetch_tiny_code_index(tiny_token, sleep_s=args.tiny_index_sleep)
    stock_cache = load_stock_cache()
    out_rows: list[dict[str, Any]] = []

    with PRIVATE_JSONL.open('a', encoding='utf-8') as cache_f:
        os.chmod(PRIVATE_JSONL, 0o600)
        for i, c in enumerate(candidates, start=1):
            oid = c['offer_id']
            shop = shopify_by_sku.get(oid) or {}
            tiny_meta = tiny_index.get(oid)
            if not tiny_meta:
                row = {
                    **c,
                    'shopify_exact_sku_seen': bool(shop),
                    'shopify_product_status': shop.get('product_status') or '',
                    'shopify_inventory_quantity_snapshot': shop.get('inventory_quantity'),
                    'tiny_exact_codigo_seen': False,
                    'proposed_availability': '',
                    'stock_confidence': 'blocked_no_tiny_exact_codigo',
                    'decision_state': 'blocked_no_tiny_exact_codigo',
                    'write_allowed_now': False,
                }
                out_rows.append(row)
                continue
            stock = stock_cache.get(oid)
            if not stock:
                if args.tiny_sleep:
                    time.sleep(args.tiny_sleep)
                stock = fetch_stock(tiny_token, tiny_meta)
                cache_f.write(json.dumps(stock, ensure_ascii=False) + '\n')
                cache_f.flush()
            decision = stock.get('stock_decision_state') or 'blocked_unknown_tiny_stock_state'
            proposed = stock.get('proposed_availability') or ''
            if proposed not in VALID_AVAILABILITY:
                decision = decision if str(decision).startswith('blocked') else 'blocked_invalid_availability_value'
            row = {
                **c,
                'shopify_exact_sku_seen': bool(shop),
                'shopify_product_status': shop.get('product_status') or '',
                'shopify_inventory_quantity_snapshot': shop.get('inventory_quantity'),
                'tiny_exact_codigo_seen': True,
                'tiny_id': stock.get('tiny_id'),
                'tiny_situacao': stock.get('tiny_situacao'),
                'tiny_tipo_variacao': stock.get('tiny_tipo_variacao'),
                'tiny_official_deposit_seen': stock.get('tiny_official_deposit_seen'),
                'tiny_official_deposit_saldo': stock.get('tiny_official_deposit_saldo'),
                'tiny_total_saldo': stock.get('tiny_total_saldo'),
                'proposed_availability': proposed,
                'stock_confidence': stock.get('stock_confidence'),
                'decision_state': decision,
                'write_scope_if_approved': 'update exact Merchant online product availability only, preserving current resource and using products.insert upsert',
                'rollback_required_before_write': True,
                'write_allowed_now': False,
            }
            out_rows.append(row)

    counts = Counter(r['decision_state'] for r in out_rows)
    proposed_counts = Counter(r['proposed_availability'] or 'none' for r in out_rows)
    confidence_counts = Counter(r['stock_confidence'] for r in out_rows)
    ready = [r for r in out_rows if r['decision_state'] == 'ready_for_availability_apply_if_lucas_approves']
    ready_in = [r for r in ready if r.get('proposed_availability') == 'in stock']
    ready_out = [r for r in ready if r.get('proposed_availability') == 'out of stock']
    blocked = [r for r in out_rows if r not in ready]

    fields = ['product_id','offer_id','merchant_title','diagnostic_required_attrs','current_product_present','current_availability','shopify_exact_sku_seen','shopify_product_status','shopify_inventory_quantity_snapshot','tiny_exact_codigo_seen','tiny_id','tiny_situacao','tiny_tipo_variacao','tiny_official_deposit_seen','tiny_official_deposit_saldo','tiny_total_saldo','proposed_availability','stock_confidence','decision_state','write_scope_if_approved','rollback_required_before_write','write_allowed_now']
    for path in (OUT_CSV, PRIVATE_CSV):
        with path.open('w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
            w.writeheader(); w.writerows(out_rows)
    os.chmod(PRIVATE_CSV, 0o600)

    payload = {
        'generated_at': utc_now(),
        'status': 'gmc_p1_availability_tiny_packet_ready_no_write',
        'scope': 'P1-B read-only/no-write approval packet for Merchant availability using Tiny exact codigo + official deposit stock truth',
        'source_labels': ['fact_merchant_center', 'fact_tiny_stock', 'fact_shopify_local_snapshot', 'derived_reconciliation', 'manual_approval_required'],
        'summary': {
            'merchant_products_current': len(products),
            'merchant_productstatuses_current': len(statuses),
            'online_missing_availability_candidates': len(out_rows),
            'decision_state_counts': dict(counts),
            'proposed_availability_counts': dict(proposed_counts),
            'stock_confidence_counts': dict(confidence_counts),
            'ready_for_availability_apply_if_lucas_approves': len(ready),
            'ready_in_stock': len(ready_in),
            'ready_out_of_stock': len(ready_out),
            'blocked_or_review': len(blocked),
            'tiny_index_codes_loaded': len(tiny_index),
            'merchant_writes': 0,
            'tiny_writes': 0,
            'shopify_writes': 0,
            'feed_writes': 0,
            'database_writes': 0,
            'external_sends': 0,
        },
        'samples': {
            'ready_in_stock': ready_in[:15],
            'ready_out_of_stock': ready_out[:15],
            'blocked_or_review': blocked[:20],
        },
        'files': {
            'public_json': str(OUT_JSON),
            'public_csv': str(OUT_CSV),
            'public_md': str(OUT_MD),
            'private_csv_chmod_600': str(PRIVATE_CSV),
            'private_tiny_stock_cache_jsonl_chmod_600': str(PRIVATE_JSONL),
        },
        'not_performed': ['merchant_product_update', 'merchant_product_insert_upsert', 'tiny_write', 'shopify_write', 'feed_update_or_fetch', 'database_write', 'pos_write', 'campaign_or_external_send'],
        'approval_wording': 'Aprovo aplicar availability no Merchant para os {n} itens ready do packet P1-B usando Tiny oficial: {in_stock} in stock e {out_stock} out of stock; sem alterar Tiny/Shopify/feed/DB/POS/campanhas, com rollback snapshot privado antes do write.'.format(n=len(ready), in_stock=len(ready_in), out_stock=len(ready_out)),
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    lines = [
        '# LK GMC P1-B Availability Tiny Packet, 2026-05-12', '',
        f"Status: `{payload['status']}`", '',
        '## Resumo executivo',
        f"- Produtos online com diagnóstico `availability` ausente: {len(out_rows)}",
        f"- Ready para apply se Lucas aprovar: {len(ready)}",
        f"- Proposta `in stock`: {len(ready_in)}",
        f"- Proposta `out of stock`: {len(ready_out)}",
        f"- Bloqueados/revisão: {len(blocked)}",
        f"- Estados: {dict(counts)}",
        '- Merchant/Tiny/Shopify/feed/DB/POS writes: 0', '',
        '## Fonte e regra',
        f"- `fact_tiny_stock`: Tiny `codigo` exato + depósito oficial `{OFFICIAL_DEPOSIT}`.",
        '- Shopify local é apenas evidência auxiliar, não verdade de estoque.',
        '- `availability` só entra como proposta quando Tiny tem `codigo` exato e saldo do depósito oficial.', '',
        '## Arquivos',
        f"- JSON público: `{OUT_JSON}`",
        f"- CSV público: `{OUT_CSV}`",
        f"- CSV privado/auditoria chmod 600: `{PRIVATE_CSV}`",
        f"- Cache Tiny privado chmod 600: `{PRIVATE_JSONL}`", '',
        '## Approval wording',
        f"`{payload['approval_wording']}`", '',
        '## Não executado',
    ]
    for item in payload['not_performed']:
        lines.append(f'- {item}')
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(OUT_MD.read_text(encoding='utf-8'), encoding='utf-8')

    if CONTROL.exists():
        marker = '### 2026-05-12 — GMC P1-B availability Tiny packet'
        text = CONTROL.read_text(encoding='utf-8')
        block = (
            f"\n{marker}\n\n"
            f"- Status: `{payload['status']}`.\n"
            f"- Read-only packet: {len(out_rows)} online rows com `availability` ausente; {len(ready)} ready via Tiny depósito oficial ({len(ready_in)} in stock / {len(ready_out)} out of stock); {len(blocked)} bloqueados/revisão.\n"
            f"- Nenhum Merchant/Tiny/Shopify/feed/DB/POS/campaign write executado.\n"
            f"- Próximo gate: aprovação explícita para apply de `availability` somente nos ready IDs, com snapshot rollback privado.\n"
        )
        if marker not in text:
            CONTROL.write_text(text.rstrip() + block + '\n', encoding='utf-8')
    if INDEX.exists():
        line = f'| LK GMC P1-B Availability Tiny Packet 2026-05-12 | `areas/lk/rotinas/gmc-{RUN_STAMP}.md` | Packet no-write para availability usando Tiny como verdade de estoque; {len(ready)} ready, {len(blocked)} bloqueados/revisão |'
        text = INDEX.read_text(encoding='utf-8')
        if line not in text:
            INDEX.write_text(text.rstrip() + '\n' + line + '\n', encoding='utf-8')

    print(json.dumps({'status': payload['status'], 'summary': payload['summary'], 'public_report': str(OUT_MD)}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
