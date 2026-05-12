#!/usr/bin/env python3
"""Refresh LK GMC supplemental datafeed fetch URL to the just-updated Gist revision.

Why: GitHub's revisionless gist raw URL can be CDN-cached. The Gist API returns a
revision-pinned raw_url immediately. Updating Merchant's datafeed fetch URL to
that raw_url and triggering fetchNow makes the approved supplemental feed change
fetchable now, while preserving rollback artifacts.
"""
from __future__ import annotations

import base64
import json
import pathlib
import subprocess
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOPPLER_TOKEN_FILE = pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
GIST_ID = '8eb7f7fb61a46fa8d5a4d64fa7f21b2f'
GIST_FILE = 'lk_sneakers_gmc_color_feed.csv'
DATAFEED_ID = '407508563'
CONTENT_SCOPE = 'https://www.googleapis.com/auth/content'
OUT_JSON = ROOT / 'reports/lk-gmc-required-attrs-datafeed-refresh-2026-05-12.json'
OUT_MD = ROOT / 'reports/lk-gmc-required-attrs-datafeed-refresh-2026-05-12.md'
DATAFEED_BACKUP_JSON = ROOT / 'reports/lk-gmc-datafeed-before-required-attrs-refresh-2026-05-12.json'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/gmc-required-attrs-datafeed-refresh-2026-05-12.md'


def b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b'=').decode()


def http_json(url: str, method: str = 'GET', token: str | None = None, payload: Any | None = None) -> dict[str, Any]:
    data = None if payload is None else json.dumps(payload, ensure_ascii=False).encode()
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header('Accept', 'application/json')
    if data is not None:
        req.add_header('Content-Type', 'application/json')
    if token:
        req.add_header('Authorization', 'Bearer ' + token)
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            text = r.read().decode()
            return json.loads(text) if text else {}
    except urllib.error.HTTPError as e:
        text = e.read().decode(errors='replace')
        try:
            body = json.loads(text)
        except Exception:
            body = {'raw': text[:1000]}
        raise RuntimeError(f'http_{e.code}_{method}_{url}: {json.dumps(body, ensure_ascii=False)[:1200]}') from e


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
    header = {'alg': 'RS256', 'typ': 'JWT'}
    signing_input = b64url(json.dumps(header, separators=(',', ':')).encode()) + '.' + b64url(json.dumps(claim, separators=(',', ':')).encode())
    with tempfile.NamedTemporaryFile('w', delete=False) as f:
        f.write(sa['private_key']); key_path = f.name
    try:
        sig = subprocess.run(['openssl', 'dgst', '-sha256', '-sign', key_path], input=signing_input.encode(), capture_output=True, check=True).stdout
    finally:
        pathlib.Path(key_path).unlink(missing_ok=True)
    body = urllib.parse.urlencode({'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer', 'assertion': signing_input + '.' + b64url(sig)}).encode()
    req = urllib.request.Request(sa.get('token_uri') or 'https://oauth2.googleapis.com/token', data=body, method='POST')
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())['access_token']


def main() -> None:
    secrets = load_doppler()
    gh = secrets.get('GITHUB_TOKEN') or secrets.get('GITHUB_LK_TOKEN') or secrets.get('GH_TOKEN') or secrets.get('GITHUB_SPITI_HUB_TOKEN')
    gt = google_token(secrets)
    merchant_id = secrets['MERCHANT_CENTER_ID_LK']

    gist = http_json(f'https://api.github.com/gists/{GIST_ID}', token=gh)
    file_info = gist['files'][GIST_FILE]
    revision_raw_url = file_info['raw_url']
    content_prefix = (file_info.get('content') or '')[:200]
    content_has_required_headers = content_prefix.startswith('id,color,age_group,gender,size')

    datafeed_url = f'https://shoppingcontent.googleapis.com/content/v2.1/{merchant_id}/datafeeds/{DATAFEED_ID}'
    before = http_json(datafeed_url, token=gt)
    DATAFEED_BACKUP_JSON.write_text(json.dumps(before, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    # Content API v2.1 has no PATCH for datafeeds. Full PUT is required.
    # Google returns this historical target with Shopping in both included and
    # excluded destinations; resubmitting verbatim is rejected. Since this
    # supplemental correction is intended to fix Shopping/Display/Surfaces item
    # issues, sanitize only the impossible duplicate by removing destinations
    # from excluded when they are also included. The full pre-write config is
    # saved in DATAFEED_BACKUP_JSON for rollback.
    after_payload = json.loads(json.dumps(before))
    after_payload.setdefault('fetchSchedule', {})['fetchUrl'] = revision_raw_url
    for target in after_payload.get('targets') or []:
        included = set(target.get('includedDestinations') or [])
        # API also rejects legacy LocalSurfacesAcrossGoogle in excludedDestinations.
        # Keep only valid non-duplicated exclusions; for this feed that becomes empty.
        excluded = [d for d in (target.get('excludedDestinations') or []) if d not in included and d != 'LocalSurfacesAcrossGoogle']
        target['excludedDestinations'] = excluded
    updated = http_json(datafeed_url, method='PUT', token=gt, payload=after_payload)
    fetch = http_json(datafeed_url + '/fetchNow', method='POST', token=gt, payload={})
    verified = http_json(datafeed_url, token=gt)

    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'LK GMC required attrs datafeed fetch URL refresh',
        'status': 'gmc_required_attrs_revision_fetch_triggered' if verified.get('fetchSchedule', {}).get('fetchUrl') == revision_raw_url and content_has_required_headers else 'gmc_required_attrs_revision_fetch_needs_attention',
        'summary': {
            'gist_revision_raw_url_detected': True,
            'gist_content_has_required_headers': content_has_required_headers,
            'previous_fetch_url': before.get('fetchSchedule', {}).get('fetchUrl'),
            'new_fetch_url': verified.get('fetchSchedule', {}).get('fetchUrl'),
            'datafeed_fetch_url_updated': verified.get('fetchSchedule', {}).get('fetchUrl') == revision_raw_url,
            'merchant_fetch_now_called': True,
            'merchant_fetch_now_response_keys': sorted(fetch.keys()),
            'production_writes': 1,
            'merchant_datafeed_config_write': 1,
            'shopify_writes': 0,
            'gsc_writes': 0,
            'campaign_sends': 0,
            'external_contacts': 0,
            'purchases_or_pos': 0,
            'marketplace_calls': 0,
            'n8n_flows_created': 0,
        },
        'rollback': {
            'datafeed_backup_json': str(DATAFEED_BACKUP_JSON.relative_to(ROOT)),
            'rollback_instruction': 'PUT the saved datafeed JSON back to Content API datafeeds/{id}, then trigger fetchNow.',
        },
        'datafeed_after': {k: verified.get(k) for k in ['id','name','fileName','fetchSchedule','targets','format']},
        'fetch_now_response': fetch,
        'not_performed': ['shopify_write','gsc_write','checkout_or_theme_write','campaign_send','supplier_or_customer_contact','purchase_or_po','external_marketplace_call','n8n_flow_creation'],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    lines = ['# LK GMC Required Attributes Datafeed Refresh, 2026-05-12', '', f"Status: `{payload['status']}`", '', '## Resumo', '']
    for k, v in payload['summary'].items():
        display = v if 'url' not in k else str(v).split('/raw/')[0] + '/raw/[revision]/' + GIST_FILE if v else v
        lines.append(f'- {k}: {display}')
    lines.extend(['', '## Rollback', f"- Backup: `{payload['rollback']['datafeed_backup_json']}`", f"- Instrução: {payload['rollback']['rollback_instruction']}", '', '## Não executado'])
    for n in payload['not_performed']:
        lines.append(f'- {n}')
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(OUT_MD.read_text(encoding='utf-8'), encoding='utf-8')
    print(json.dumps({'status': payload['status'], 'summary': payload['summary']}, ensure_ascii=False))
    if not payload['status'].endswith('triggered'):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
