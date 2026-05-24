#!/usr/bin/env python3
"""Verify approved-only LK GMC required-attributes second batch.

Reads only preview rows marked `supplemental_feed_preview_preferred` and checks
Content API product resources for ageGroup, gender and size. Read-only.
"""
from __future__ import annotations

import base64
import json
import pathlib
import subprocess
import tempfile
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOPPLER_TOKEN_FILE = pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
PREVIEW_JSON = ROOT / 'reports/lk-gmc-required-attrs-preview-2026-05-12.json'
OUT_JSON = ROOT / 'reports/lk-gmc-required-attrs-verify-second-batch-2026-05-12.json'
OUT_MD = ROOT / 'reports/lk-gmc-required-attrs-verify-second-batch-2026-05-12.md'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/gmc-required-attrs-verify-second-batch-2026-05-12.md'
CONTENT_SCOPE = 'https://www.googleapis.com/auth/content'


def b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b'=').decode()


def load_doppler() -> dict[str, str]:
    token = DOPPLER_TOKEN_FILE.read_text().strip()
    req = urllib.request.Request('https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json')
    req.add_header('Authorization', 'Basic ' + base64.b64encode((token + ':').encode()).decode())
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())


def google_token(secrets: dict[str, str]) -> str:
    raw = secrets.get('GOOGLE_SERVICE_ACCOUNT_JSON') or secrets.get('GA4_LK_N8N_ZIPPER_SERVICE_ACCOUNT') or secrets.get('GA4_LK_SERVICE_ACCOUNT')
    sa = json.loads(raw) if raw and raw.strip().startswith('{') else json.loads(base64.b64decode(raw or '').decode())
    now = int(time.time())
    claim = {'iss': sa['client_email'], 'scope': CONTENT_SCOPE, 'aud': sa.get('token_uri') or 'https://oauth2.googleapis.com/token', 'iat': now, 'exp': now + 3600}
    signing_input = b64url(json.dumps({'alg': 'RS256', 'typ': 'JWT'}, separators=(',', ':')).encode()) + '.' + b64url(json.dumps(claim, separators=(',', ':')).encode())
    with tempfile.NamedTemporaryFile('w', delete=False) as f:
        f.write(sa['private_key'])
        key_path = f.name
    try:
        sig = subprocess.run(['openssl', 'dgst', '-sha256', '-sign', key_path], input=signing_input.encode(), capture_output=True, check=True).stdout
    finally:
        pathlib.Path(key_path).unlink(missing_ok=True)
    req = urllib.request.Request(sa.get('token_uri') or 'https://oauth2.googleapis.com/token', data=urllib.parse.urlencode({'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer', 'assertion': signing_input + '.' + b64url(sig)}).encode(), method='POST')
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())['access_token']


def get_product(mid: str, token: str, offer_id: str) -> dict[str, Any]:
    pid = 'online:pt:BR:' + offer_id
    url = f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/products/{urllib.parse.quote(pid, safe="")}'
    req = urllib.request.Request(url)
    req.add_header('Authorization', 'Bearer ' + token)
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.loads(r.read().decode())


def main() -> None:
    preview = json.loads(PREVIEW_JSON.read_text(encoding='utf-8'))
    rows_to_verify = [r for r in preview['results'] if r.get('recommended_surface') == 'supplemental_feed_preview_preferred']
    secrets = load_doppler()
    token = google_token(secrets)
    mid = secrets['MERCHANT_CENTER_ID_LK']
    rows = []
    for r in rows_to_verify:
        sug = r.get('suggested_attributes') or {}
        offer = r['offer_id']
        try:
            p = get_product(mid, token, offer)
            got_sizes = p.get('sizes') or []
            ok = p.get('ageGroup') == sug.get('age_group') and p.get('gender') == sug.get('gender') and (sug.get('size') in got_sizes)
            rows.append({'offer_id': offer, 'ok': ok, 'expected': {'ageGroup': sug.get('age_group'), 'gender': sug.get('gender'), 'size': sug.get('size')}, 'actual': {'ageGroup': p.get('ageGroup'), 'gender': p.get('gender'), 'sizes': got_sizes}, 'error': None})
        except Exception as e:
            rows.append({'offer_id': offer, 'ok': False, 'expected': sug, 'actual': {}, 'error': str(e)[:300]})
    summary = {
        'rows_verified': len(rows),
        'rows_matching_applied_attrs': sum(1 for r in rows if r['ok']),
        'rows_not_matching': sum(1 for r in rows if not r['ok']),
        'content_api_product_writes': 0,
        'merchant_status_recheck_note': 'Product resources may lag after datafeed.fetchNow; diagnostics lag even more.',
    }
    payload = {'generated_at': datetime.now(timezone.utc).isoformat(), 'scope': 'LK GMC required attrs second batch approved-only verification', 'status': 'gmc_required_attrs_second_batch_product_attrs_verified' if summary['rows_not_matching'] == 0 else 'gmc_required_attrs_second_batch_product_attrs_partial', 'summary': summary, 'results': rows, 'not_performed': ['merchant_write', 'shopify_write', 'gsc_write', 'campaign_send', 'supplier_contact', 'purchase_or_po', 'marketplace_call', 'n8n_flow_creation']}
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    lines = ['# LK GMC Required Attributes Verify, Second Batch, 2026-05-12', '', f"Status: `{payload['status']}`", '', '## Resumo']
    for k, v in summary.items():
        lines.append(f'- {k}: {v}')
    lines.extend(['', '## Amostras'])
    for r in rows[:20]:
        lines.append(f"- {r['offer_id']}: ok={r['ok']} expected={r['expected']} actual={r['actual']} error={r['error']}")
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(OUT_MD.read_text(encoding='utf-8'), encoding='utf-8')
    print(json.dumps({'status': payload['status'], 'summary': summary}, ensure_ascii=False))
    if summary['rows_not_matching']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
