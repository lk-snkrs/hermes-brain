#!/usr/bin/env python3
"""Apply Lucas-approved second LK GMC required-attributes batch.

WRITE scope approved by Lucas via Telegram on 2026-05-12: "Corrigir e aprovar".
This script updates only the existing Gist-backed supplemental feed rows for the
72 preview rows marked `supplemental_feed_preview_preferred`, then updates the
Merchant datafeed fetch URL to the new revision-pinned raw URL and calls fetchNow.

Rollback: restore the saved backup CSV to the Gist and restore the saved datafeed
JSON if needed, then call datafeeds.fetchNow.
"""
from __future__ import annotations

import base64
import csv
import io
import json
import os
import pathlib
import subprocess
import tempfile
import time
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOPPLER_TOKEN_FILE = pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
PREVIEW_JSON = ROOT / 'reports/lk-gmc-required-attrs-preview-2026-05-12.json'
OUT_JSON = ROOT / 'reports/lk-gmc-required-attrs-apply-second-batch-2026-05-12.json'
OUT_MD = ROOT / 'reports/lk-gmc-required-attrs-apply-second-batch-2026-05-12.md'
BACKUP_CSV = ROOT / 'reports/lk-gmc-supplemental-feed-before-required-attrs-second-batch-2026-05-12.csv'
APPLIED_CSV = ROOT / 'reports/lk-gmc-supplemental-feed-after-required-attrs-second-batch-2026-05-12.csv'
DATAFEED_BACKUP_JSON = ROOT / 'reports/lk-gmc-datafeed-before-required-attrs-second-batch-2026-05-12.json'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/gmc-required-attrs-apply-second-batch-2026-05-12.md'
GIST_ID = '8eb7f7fb61a46fa8d5a4d64fa7f21b2f'
GIST_FILE = 'lk_sneakers_gmc_color_feed.csv'
DATAFEED_ID = '407508563'
CONTENT_SCOPE = 'https://www.googleapis.com/auth/content'
APPROVAL = 'Lucas explicitly approved via Telegram: "Corrigir e aprovar" on 2026-05-12 after the 72-row preview.'


def b64url(raw: bytes) -> str:
    return base64.urlsafe_b64encode(raw).rstrip(b'=').decode()


def request_json(url: str, method: str = 'GET', token: str | None = None, payload: Any | None = None, timeout: int = 120) -> dict[str, Any]:
    data = None if payload is None else json.dumps(payload, ensure_ascii=False).encode()
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header('Accept', 'application/json')
    if data is not None:
        req.add_header('Content-Type', 'application/json')
    if token:
        req.add_header('Authorization', 'Bearer ' + token)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        text = r.read().decode()
        return json.loads(text) if text else {}


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
    signing_input = b64url(json.dumps({'alg': 'RS256', 'typ': 'JWT'}, separators=(',', ':')).encode()) + '.' + b64url(json.dumps(claim, separators=(',', ':')).encode())
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


def parse_csv(text: str) -> tuple[list[str], list[dict[str, str]]]:
    reader = csv.DictReader(io.StringIO(text))
    return list(reader.fieldnames or []), [{k: (v or '') for k, v in row.items()} for row in reader]


def to_csv(fieldnames: list[str], rows: list[dict[str, str]]) -> str:
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=fieldnames, lineterminator='\n')
    writer.writeheader()
    for row in rows:
        writer.writerow({k: row.get(k, '') for k in fieldnames})
    return buf.getvalue()


def build_new_csv(current_text: str, preview: dict[str, Any]) -> tuple[str, dict[str, Any]]:
    fields, rows = parse_csv(current_text)
    for required in ['id', 'color', 'age_group', 'gender', 'size']:
        if required not in fields:
            fields.append(required)
    by_id = {r.get('id', ''): r for r in rows if r.get('id')}
    approved_rows = [r for r in preview.get('results', []) if r.get('recommended_surface') == 'supplemental_feed_preview_preferred']
    created = updated = unchanged = 0
    for r in approved_rows:
        offer_id = r['offer_id']
        sug = r.get('suggested_attributes') or {}
        row = by_id.get(offer_id)
        if row is None:
            row = {f: '' for f in fields}
            row['id'] = offer_id
            rows.append(row)
            by_id[offer_id] = row
            created += 1
        before = dict(row)
        row['age_group'] = sug.get('age_group') or row.get('age_group', '')
        row['gender'] = sug.get('gender') or row.get('gender', '')
        row['size'] = sug.get('size') or row.get('size', '')
        if before == row:
            unchanged += 1
        else:
            updated += 1
    return to_csv(fields, rows), {
        'existing_rows_before': len(rows) - created,
        'rows_after': len(rows),
        'approved_required_attr_rows': len(approved_rows),
        'rows_created': created,
        'rows_updated_or_completed': updated,
        'rows_already_matching': unchanged,
        'age_group_counts_applied': dict(Counter((r.get('suggested_attributes') or {}).get('age_group') for r in approved_rows)),
        'gender_counts_applied': dict(Counter((r.get('suggested_attributes') or {}).get('gender') for r in approved_rows)),
    }


def datafeed_payload_from_before(before: dict[str, Any], revision_raw_url: str) -> dict[str, Any]:
    payload = {k: v for k, v in before.items() if k not in {'kind', 'errors', 'warnings'}}
    payload.setdefault('fetchSchedule', {})['fetchUrl'] = revision_raw_url
    for target in payload.get('targets') or []:
        included = target.get('includedDestinations') or []
        target['excludedDestinations'] = [d for d in (target.get('excludedDestinations') or []) if d not in included and d != 'LocalSurfacesAcrossGoogle']
    return payload


def main() -> None:
    preview = json.loads(PREVIEW_JSON.read_text(encoding='utf-8'))
    approved_count = sum(1 for r in preview.get('results', []) if r.get('recommended_surface') == 'supplemental_feed_preview_preferred')
    if preview.get('status') != 'gmc_required_attrs_preview_ready_readonly' or approved_count != 72:
        raise RuntimeError(f'unexpected_preview_state approved_count={approved_count}')
    secrets = load_doppler()
    github_token = secrets.get('GITHUB_TOKEN') or secrets.get('GITHUB_LK_TOKEN') or secrets.get('GH_TOKEN') or secrets.get('GITHUB_SPITI_HUB_TOKEN')
    merchant_id = secrets.get('MERCHANT_CENTER_ID_LK')
    if not github_token or not merchant_id:
        raise RuntimeError('missing_required_token_or_merchant_id')
    google_token = google_access_token(parse_service_account(secrets))

    gist_before = request_json(f'https://api.github.com/gists/{GIST_ID}', token=github_token)
    before_file = (gist_before.get('files') or {}).get(GIST_FILE) or {}
    before_text = before_file.get('content') or urllib.request.urlopen(before_file['raw_url'], timeout=120).read().decode('utf-8-sig')
    BACKUP_CSV.write_text(before_text, encoding='utf-8')
    after_text, stats = build_new_csv(before_text, preview)
    APPLIED_CSV.write_text(after_text, encoding='utf-8')

    gist_after = request_json(f'https://api.github.com/gists/{GIST_ID}', method='PATCH', token=github_token, payload={'files': {GIST_FILE: {'content': after_text}}})
    gist_file_after = (gist_after.get('files') or {}).get(GIST_FILE) or {}
    revision_raw_url = gist_file_after.get('raw_url')
    gist_verified = (gist_file_after.get('content') or '') == after_text

    datafeed_url = f'https://shoppingcontent.googleapis.com/content/v2.1/{merchant_id}/datafeeds/{DATAFEED_ID}'
    datafeed_before = request_json(datafeed_url, token=google_token)
    DATAFEED_BACKUP_JSON.write_text(json.dumps(datafeed_before, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    datafeed_after_update = request_json(datafeed_url, method='PUT', token=google_token, payload=datafeed_payload_from_before(datafeed_before, revision_raw_url))
    fetch_response = request_json(datafeed_url + '/fetchNow', method='POST', token=google_token, payload={})
    datafeed_after = request_json(datafeed_url, token=google_token)

    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'LK GMC required attributes second batch apply via supplemental feed gist',
        'status': 'gmc_required_attrs_second_batch_applied_fetch_triggered' if gist_verified and (datafeed_after.get('fetchSchedule') or {}).get('fetchUrl') == revision_raw_url else 'gmc_required_attrs_second_batch_apply_needs_attention',
        'approval': APPROVAL,
        'summary': {
            **stats,
            'gist_patch_verified_by_api_content': gist_verified,
            'datafeed_fetch_url_updated_to_revision': (datafeed_after.get('fetchSchedule') or {}).get('fetchUrl') == revision_raw_url,
            'merchant_fetch_now_called': True,
            'merchant_fetch_now_response_keys': sorted(fetch_response.keys()),
            'production_writes': 2,
            'gist_feed_write': 1,
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
            'backup_csv': str(BACKUP_CSV.relative_to(ROOT)),
            'datafeed_backup_json': str(DATAFEED_BACKUP_JSON.relative_to(ROOT)),
            'instruction': 'PATCH the gist file back to backup_csv; optionally PUT datafeed_backup_json back to datafeeds/{id}; then POST fetchNow.',
        },
        'surface': {'gist_id': GIST_ID, 'gist_file': GIST_FILE, 'datafeed_id': DATAFEED_ID, 'datafeed_name': datafeed_after.get('name')},
        'not_performed': ['shopify_product_or_metafield_write', 'gsc_admin_or_indexing_submit', 'checkout_setting_change', 'theme_or_pdp_write', 'campaign_send_or_schedule', 'supplier_contact', 'purchase_or_po', 'external_marketplace_call', 'n8n_flow_creation'],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    lines = ['# LK GMC Required Attributes Apply, Second Batch, 2026-05-12', '', f"Status: `{payload['status']}`", '', '## Resumo']
    for k, v in payload['summary'].items():
        lines.append(f'- {k}: {v}')
    lines.extend(['', '## Rollback', f"- Backup CSV: `{payload['rollback']['backup_csv']}`", f"- Datafeed backup: `{payload['rollback']['datafeed_backup_json']}`", f"- Instrução: {payload['rollback']['instruction']}", '', '## Não executado'])
    for n in payload['not_performed']:
        lines.append(f'- {n}')
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(OUT_MD.read_text(encoding='utf-8'), encoding='utf-8')
    print(json.dumps({'status': payload['status'], 'summary': payload['summary']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
