#!/usr/bin/env python3
"""Apply Lucas-approved LK GMC required attributes via the existing supplemental feed.

This is a WRITE script. It is only safe to run after explicit Lucas approval.
It updates the existing GitHub Gist-backed Merchant Center supplemental feed
(`LK Sneakers - Color Supplemental Feed`) by preserving all existing rows and
adding age_group/gender/size for the approved 80 offer IDs.

Rollback: the script writes a dated backup of the previous CSV and records exact
API responses. Revert by PATCHing the gist file back to the backup CSV and
triggering datafeeds.fetchNow again.
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
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOPPLER_TOKEN_FILE = pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
PREVIEW_JSON = ROOT / 'reports/lk-gmc-required-attrs-preview-2026-05-12.json'
OUT_JSON = ROOT / 'reports/lk-gmc-required-attrs-apply-2026-05-12.json'
OUT_MD = ROOT / 'reports/lk-gmc-required-attrs-apply-2026-05-12.md'
BACKUP_CSV = ROOT / 'reports/lk-gmc-supplemental-feed-before-required-attrs-2026-05-12.csv'
APPLIED_CSV = ROOT / 'reports/lk-gmc-supplemental-feed-after-required-attrs-2026-05-12.csv'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/gmc-required-attrs-apply-2026-05-12.md'

GIST_ID = '8eb7f7fb61a46fa8d5a4d64fa7f21b2f'
GIST_FILE = 'lk_sneakers_gmc_color_feed.csv'
RAW_URL = f'https://gist.githubusercontent.com/lk-snkrs/{GIST_ID}/raw/{GIST_FILE}'
DATAFEED_ID = '407508563'
CONTENT_SCOPE = 'https://www.googleapis.com/auth/content'

APPROVAL = 'Lucas explicitly approved via Telegram: "Corrigir e aplicar e seguir" on 2026-05-12.'


def b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b'=').decode()


def request_json(url: str, method: str = 'GET', token: str | None = None, payload: Any | None = None, timeout: int = 90) -> dict[str, Any]:
    data = None if payload is None else json.dumps(payload, ensure_ascii=False).encode()
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header('Accept', 'application/json')
    if data is not None:
        req.add_header('Content-Type', 'application/json')
    if token:
        req.add_header('Authorization', 'Bearer ' + token)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            text = r.read().decode()
            return json.loads(text) if text else {}
    except urllib.error.HTTPError as e:
        text = e.read().decode(errors='replace')
        try:
            body = json.loads(text)
        except Exception:
            body = {'raw': text[:1000]}
        raise RuntimeError(f'http_{e.code}_{method}_{url}: {json.dumps(body, ensure_ascii=False)[:1200]}') from e


def request_text(url: str, timeout: int = 90) -> str:
    with urllib.request.urlopen(url, timeout=timeout) as r:
        return r.read().decode('utf-8-sig')


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
        sa = json.loads(raw)
    except json.JSONDecodeError:
        sa = json.loads(base64.b64decode(raw).decode())
    return sa


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


def parse_csv(text: str) -> tuple[list[str], list[dict[str, str]]]:
    reader = csv.DictReader(io.StringIO(text))
    rows = [{k: (v or '') for k, v in row.items()} for row in reader]
    return list(reader.fieldnames or []), rows


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
    by_id: dict[str, dict[str, str]] = {r.get('id', ''): r for r in rows if r.get('id')}
    created = 0
    updated = 0
    unchanged = 0
    approved_rows = [r for r in preview.get('results', []) if r.get('recommended_surface') == 'supplemental_feed_preview_preferred']
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
        # Preserve existing color values; this approved run targets required attributes.
        row['age_group'] = sug.get('age_group') or row.get('age_group', '')
        row['gender'] = sug.get('gender') or row.get('gender', '')
        row['size'] = sug.get('size') or row.get('size', '')
        if before == row:
            unchanged += 1
        else:
            updated += 1
    new_text = to_csv(fields, rows)
    stats = {
        'existing_rows_before': len(by_id) if created == 0 else len(by_id) - created,
        'rows_after': len(rows),
        'approved_required_attr_rows': len(approved_rows),
        'rows_created': created,
        'rows_updated_or_completed': updated,
        'rows_already_matching': unchanged,
        'columns_after': fields,
        'age_group_counts_applied': dict(Counter((r.get('suggested_attributes') or {}).get('age_group') for r in approved_rows)),
        'gender_counts_applied': dict(Counter((r.get('suggested_attributes') or {}).get('gender') for r in approved_rows)),
    }
    return new_text, stats


def patch_gist(github_token: str, content: str) -> dict[str, Any]:
    payload = {'files': {GIST_FILE: {'content': content}}}
    return request_json(f'https://api.github.com/gists/{GIST_ID}', method='PATCH', token=github_token, payload=payload)


def trigger_fetch_now(merchant_id: str, google_token: str) -> dict[str, Any]:
    # Content API method is datafeeds.fetchnow at /fetchNow.
    url = f'https://shoppingcontent.googleapis.com/content/v2.1/{merchant_id}/datafeeds/{DATAFEED_ID}/fetchNow'
    return request_json(url, method='POST', token=google_token, payload={})


def get_datafeed(merchant_id: str, google_token: str) -> dict[str, Any]:
    url = f'https://shoppingcontent.googleapis.com/content/v2.1/{merchant_id}/datafeeds/{DATAFEED_ID}'
    return request_json(url, token=google_token)


def main() -> None:
    preview = json.loads(PREVIEW_JSON.read_text(encoding='utf-8'))
    if preview.get('status') != 'gmc_required_attrs_preview_ready_readonly':
        raise RuntimeError('preview_not_ready')
    if (preview.get('summary') or {}).get('supplemental_feed_preview_rows') != 80:
        raise RuntimeError('unexpected_preview_row_count')

    secrets = load_doppler()
    github_token = secrets.get('GITHUB_TOKEN') or secrets.get('GITHUB_LK_TOKEN') or secrets.get('GH_TOKEN') or secrets.get('GITHUB_SPITI_HUB_TOKEN')
    if not github_token:
        raise RuntimeError('missing_github_token_for_gist_update')
    merchant_id = secrets.get('MERCHANT_CENTER_ID_LK')
    if not merchant_id:
        raise RuntimeError('missing_merchant_center_id')
    google_token = google_access_token(parse_service_account(secrets))

    before_text = request_text(RAW_URL)
    BACKUP_CSV.write_text(before_text, encoding='utf-8')
    after_text, stats = build_new_csv(before_text, preview)
    APPLIED_CSV.write_text(after_text, encoding='utf-8')

    gist_response = patch_gist(github_token, after_text)
    gist_file = (gist_response.get('files') or {}).get(GIST_FILE) or {}
    verified_content = gist_file.get('content') or ''
    gist_verified = verified_content == after_text

    fetch_response = trigger_fetch_now(merchant_id, google_token)
    datafeed_after = get_datafeed(merchant_id, google_token)

    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'LK GMC required attributes apply via supplemental feed gist',
        'status': 'gmc_required_attrs_applied_fetch_triggered' if gist_verified else 'gmc_required_attrs_apply_needs_verification',
        'approval': APPROVAL,
        'surface': {
            'type': 'merchant_center_supplemental_feed_csv_gist',
            'gist_id': GIST_ID,
            'gist_file': GIST_FILE,
            'datafeed_id': DATAFEED_ID,
            'datafeed_name': datafeed_after.get('name'),
            'fetch_url': ((datafeed_after.get('fetchSchedule') or {}).get('fetchUrl')),
        },
        'summary': {
            **stats,
            'gist_patch_verified_by_api_content': gist_verified,
            'merchant_fetch_now_called': True,
            'merchant_fetch_now_response_keys': sorted(fetch_response.keys()),
            'production_writes': 1,
            'merchant_feed_write': 1,
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
            'rollback_instruction': 'PATCH the gist file back to the backup CSV content, then POST datafeeds/{datafeed_id}/fetchNow again.',
        },
        'fetch_now_response': fetch_response,
        'datafeed_after': {k: datafeed_after.get(k) for k in ['id', 'name', 'fileName', 'fetchSchedule', 'targets', 'format']},
        'not_performed': [
            'shopify_product_or_metafield_write', 'gsc_admin_or_indexing_submit', 'checkout_setting_change',
            'theme_or_pdp_write', 'campaign_send_or_schedule', 'supplier_contact', 'purchase_or_po',
            'external_marketplace_call', 'n8n_flow_creation',
        ],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    lines = [
        '# LK GMC Required Attributes Apply, 2026-05-12', '',
        f"Generated at: `{payload['generated_at']}`", '',
        '## Veredito', '',
        f"Status: `{payload['status']}`", '',
        'Lucas aprovou a aplicação. O supplemental feed existente do Merchant foi atualizado no Gist e o fetchNow do datafeed foi acionado.', '',
        '## Resumo', '',
    ]
    for k, v in payload['summary'].items():
        lines.append(f'- {k}: {v}')
    lines.extend(['', '## Superfície aplicada', ''])
    for k, v in payload['surface'].items():
        lines.append(f'- {k}: {v}')
    lines.extend(['', '## Rollback', '', f"- Backup: `{payload['rollback']['backup_csv']}`", f"- Instrução: {payload['rollback']['rollback_instruction']}", '', '## Não executado', ''])
    for n in payload['not_performed']:
        lines.append(f'- {n}')
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(OUT_MD.read_text(encoding='utf-8'), encoding='utf-8')
    print(json.dumps({'status': payload['status'], 'summary': payload['summary']}, ensure_ascii=False))
    if not gist_verified:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
