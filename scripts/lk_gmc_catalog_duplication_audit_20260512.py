#!/usr/bin/env python3
"""Read-only LK Merchant Center catalog duplication audit.

Compares Merchant Center product/status counts against Shopify/Data Spine local
counts and highlights duplicate offer IDs across productId dimensions.
No Merchant, Shopify, feed, database or external writes are performed.
"""
from __future__ import annotations

import base64
import json
import os
import pathlib
import sqlite3
import subprocess
import tempfile
import time
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOPPLER_TOKEN_FILE = pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
LOCAL_DB = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite')
OUT_JSON = ROOT / 'reports/lk-gmc-catalog-duplication-audit-2026-05-12.json'
OUT_MD = ROOT / 'reports/lk-gmc-catalog-duplication-audit-2026-05-12.md'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/gmc-catalog-duplication-audit-2026-05-12.md'
CONTENT_SCOPE = 'https://www.googleapis.com/auth/content'


def b64url(raw: bytes) -> str:
    return base64.urlsafe_b64encode(raw).decode().rstrip('=')


def load_doppler() -> dict[str, str]:
    token = os.environ.get('DOPPLER_TOKEN') or DOPPLER_TOKEN_FILE.read_text().strip()
    req = urllib.request.Request('https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json')
    req.add_header('Authorization', 'Basic ' + base64.b64encode((token + ':').encode()).decode())
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())


def parse_service_account(secrets: dict[str, str]) -> dict[str, Any]:
    raw = secrets.get('GOOGLE_SERVICE_ACCOUNT_JSON') or secrets.get('GA4_LK_N8N_ZIPPER_SERVICE_ACCOUNT') or secrets.get('GA4_LK_SERVICE_ACCOUNT')
    if not raw:
        raise RuntimeError('missing_google_service_account_secret')
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return json.loads(base64.b64decode(raw).decode())


def google_access_token(sa: dict[str, Any]) -> str:
    now = int(time.time())
    claim = {'iss': sa['client_email'], 'scope': CONTENT_SCOPE, 'aud': sa.get('token_uri') or 'https://oauth2.googleapis.com/token', 'iat': now, 'exp': now + 3600}
    header = {'alg': 'RS256', 'typ': 'JWT'}
    signing_input = b64url(json.dumps(header, separators=(',', ':')).encode()) + '.' + b64url(json.dumps(claim, separators=(',', ':')).encode())
    with tempfile.NamedTemporaryFile('w', delete=False) as key_file:
        key_file.write(sa['private_key'])
        key_path = key_file.name
    try:
        sig = subprocess.run(['openssl', 'dgst', '-sha256', '-sign', key_path], input=signing_input.encode(), capture_output=True, check=True).stdout
    finally:
        pathlib.Path(key_path).unlink(missing_ok=True)
    body = urllib.parse.urlencode({'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer', 'assertion': signing_input + '.' + b64url(sig)}).encode()
    req = urllib.request.Request(sa.get('token_uri') or 'https://oauth2.googleapis.com/token', data=body, method='POST')
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())['access_token']


def get_json(url: str, token: str) -> dict[str, Any]:
    req = urllib.request.Request(url)
    req.add_header('Authorization', 'Bearer ' + token)
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode())


def list_all(endpoint: str, merchant_id: str, token: str, max_pages: int = 500) -> list[dict[str, Any]]:
    rows = []
    page_token = None
    pages = 0
    while pages < max_pages:
        qs = {'maxResults': '250'}
        if page_token:
            qs['pageToken'] = page_token
        url = f'https://shoppingcontent.googleapis.com/content/v2.1/{merchant_id}/{endpoint}?' + urllib.parse.urlencode(qs)
        data = get_json(url, token)
        batch = data.get('resources') or []
        rows.extend(batch)
        pages += 1
        page_token = data.get('nextPageToken')
        if not page_token or not batch:
            break
    return rows


def parse_product_id(pid: str) -> dict[str, str]:
    parts = (pid or '').split(':', 3)
    if len(parts) == 4:
        return {'channel': parts[0], 'content_language': parts[1], 'target_country': parts[2], 'offer_id': parts[3]}
    return {'channel': '', 'content_language': '', 'target_country': '', 'offer_id': pid or ''}


def local_counts() -> dict[str, Any]:
    out = {'db_present': LOCAL_DB.exists()}
    if not LOCAL_DB.exists():
        return out
    con = sqlite3.connect(str(LOCAL_DB))
    cur = con.cursor()
    out['shopify_products_total_local'] = cur.execute('select count(*) from lk_products').fetchone()[0]
    out['shopify_products_active_local'] = cur.execute("select count(*) from lk_products where lower(coalesce(status,''))='active'").fetchone()[0]
    out['shopify_variants_total_local'] = cur.execute('select count(*) from lk_product_variants').fetchone()[0]
    out['shopify_variants_with_sku_local'] = cur.execute("select count(*) from lk_product_variants where coalesce(sku,'')<>''").fetchone()[0]
    out['shopify_distinct_skus_local'] = cur.execute("select count(distinct sku) from lk_product_variants where coalesce(sku,'')<>''").fetchone()[0]
    con.close()
    return out


def summarize(rows: list[dict[str, Any]], id_key: str) -> dict[str, Any]:
    parsed = []
    for r in rows:
        pid = r.get(id_key) or r.get('productId') or r.get('id') or ''
        meta = parse_product_id(pid)
        parsed.append((r, pid, meta))
    offer_counts = Counter(m['offer_id'] for _, _, m in parsed)
    key_counts = Counter((m['channel'], m['content_language'], m['target_country']) for _, _, m in parsed)
    duplicate_offer_ids = {k: v for k, v in offer_counts.items() if k and v > 1}
    samples = []
    for offer_id, count in sorted(duplicate_offer_ids.items(), key=lambda x: (-x[1], x[0]))[:25]:
        ids = [pid for _, pid, m in parsed if m['offer_id'] == offer_id][:8]
        titles = [r.get('title') for r, _, m in parsed if m['offer_id'] == offer_id and r.get('title')]
        samples.append({'offer_id': offer_id, 'count': count, 'product_ids_sample': ids, 'titles_sample': titles[:3]})
    return {
        'total_rows': len(rows),
        'unique_product_ids': len(set(pid for _, pid, _ in parsed)),
        'unique_offer_ids': len(offer_counts),
        'duplicate_offer_id_count': len(duplicate_offer_ids),
        'duplicate_offer_id_rows': sum(duplicate_offer_ids.values()),
        'dimension_counts': [{'channel': k[0], 'content_language': k[1], 'target_country': k[2], 'count': v} for k, v in key_counts.most_common(20)],
        'duplicate_samples': samples,
    }


def main() -> None:
    secrets = load_doppler()
    merchant_id = secrets.get('MERCHANT_CENTER_ID_LK')
    if not merchant_id:
        raise RuntimeError('missing_merchant_center_id')
    token = google_access_token(parse_service_account(secrets))
    statuses = list_all('productstatuses', merchant_id, token)
    products = list_all('products', merchant_id, token)
    status_summary = summarize(statuses, 'productId')
    product_summary = summarize(products, 'id')

    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'LK GMC catalog duplication audit read-only',
        'status': 'gmc_catalog_duplication_audit_ready_readonly',
        'source_labels': ['fact_merchant_center', 'fact_shopify_local_snapshot'],
        'merchant_center': {
            'productstatuses': status_summary,
            'products': product_summary,
        },
        'local_shopify_snapshot': local_counts(),
        'interpretation': {
            'is_25_6k_plausible_as_unique_lk_catalog': False,
            'reason': 'Merchant Center product count is materially higher than local Shopify product and variant counts. Product IDs are counted at offer/item level and can include historical/stale/feed-duplicated entries; duplicates must be cleaned only after feed/source audit.',
            'safe_next_step': 'List data sources/feeds and isolate source(s) creating duplicate/stale offers before deleting/excluding anything.',
        },
        'not_performed': [
            'merchant_product_delete', 'feed_delete_or_exclusion', 'shopify_write', 'database_write', 'campaign_or_external_send', 'checkout_or_theme_change'
        ],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    lines = [
        '# LK GMC Catalog Duplication Audit, 2026-05-12', '',
        f"Status: `{payload['status']}`", '',
        '## Resumo executivo',
        f"- Merchant productstatuses: {status_summary['total_rows']}",
        f"- Merchant products: {product_summary['total_rows']}",
        f"- Merchant unique offer IDs: {product_summary['unique_offer_ids']}",
        f"- Shopify local products total/active: {payload['local_shopify_snapshot'].get('shopify_products_total_local')} / {payload['local_shopify_snapshot'].get('shopify_products_active_local')}",
        f"- Shopify local variants total: {payload['local_shopify_snapshot'].get('shopify_variants_total_local')}",
        f"- Shopify local variants with SKU / distinct SKUs: {payload['local_shopify_snapshot'].get('shopify_variants_with_sku_local')} / {payload['local_shopify_snapshot'].get('shopify_distinct_skus_local')}",
        '',
        '## Veredito',
        '- Os 25,6 mil itens do Merchant não parecem representar o catálogo real único da LK.',
        '- A contagem do Merchant é por item/oferta e pode incluir variantes, histórico/stale items, fontes duplicadas ou combinações por país/idioma/canal.',
        '- Antes de excluir qualquer coisa, é necessário mapear fontes/feeds e provar qual origem está inflando a base.',
        '',
        '## Dimensões Merchant products',
    ]
    for d in product_summary['dimension_counts'][:10]:
        lines.append(f"- {d['channel']}:{d['content_language']}:{d['target_country']}: {d['count']}")
    lines.extend(['', '## Exemplos de offer_id duplicado'])
    for s in product_summary['duplicate_samples'][:10]:
        lines.append(f"- {s['offer_id']}: {s['count']} ids; amostra={s['product_ids_sample']}")
    lines.extend(['', '## Não executado'])
    for n in payload['not_performed']:
        lines.append(f'- {n}')
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(OUT_MD.read_text(encoding='utf-8'), encoding='utf-8')
    print(json.dumps({
        'status': payload['status'],
        'productstatuses_total': status_summary['total_rows'],
        'products_total': product_summary['total_rows'],
        'unique_offer_ids': product_summary['unique_offer_ids'],
        'local_variants': payload['local_shopify_snapshot'].get('shopify_variants_total_local'),
        'duplicate_offer_id_count': product_summary['duplicate_offer_id_count'],
    }, ensure_ascii=False))


if __name__ == '__main__':
    main()
