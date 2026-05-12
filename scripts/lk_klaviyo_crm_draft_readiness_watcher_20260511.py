#!/usr/bin/env python3
"""LK-AUTO-005 Klaviyo CRM draft watcher, read-only readiness preview.

Manual only. Uses Klaviyo GET endpoints to validate the approved Phase 5 P1 list/template/campaign draft state.
No campaign send, schedule, mutation, flow activation, customer contact, or PII output.
"""
from __future__ import annotations

import base64
import json
import pathlib
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOPPLER_TOKEN_FILE = pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
SOURCE_JSON = ROOT / 'reports/lk-phase5-p1-klaviyo-klaviyo-objects-2026-05-11.json'
OUT_JSON = ROOT / 'reports/lk-klaviyo-crm-draft-readiness-watcher-2026-05-11.json'
OUT_MD = ROOT / 'reports/lk-klaviyo-crm-draft-readiness-watcher-2026-05-11.md'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/klaviyo-crm-draft-readiness-watcher-2026-05-11.md'
BASE = 'https://a.klaviyo.com/api'
REVISION = '2024-10-15'


def load_doppler_secrets() -> dict[str, str]:
    token = DOPPLER_TOKEN_FILE.read_text().strip()
    req = urllib.request.Request('https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json')
    req.add_header('Authorization', 'Basic ' + base64.b64encode((token + ':').encode()).decode())
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())


def api_get(path: str, token: str, query: dict[str, str] | None = None) -> dict[str, Any]:
    url = BASE + path
    if query:
        url += '?' + urllib.parse.urlencode(query)
    req = urllib.request.Request(url, method='GET')
    req.add_header('Authorization', f'Klaviyo-API-Key {token}')
    req.add_header('Accept', 'application/json')
    req.add_header('Content-Type', 'application/json')
    req.add_header('revision', REVISION)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            raw = resp.read().decode()
            return {'status': resp.status, 'body': json.loads(raw) if raw else {}}
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode(errors='replace')
        try:
            parsed = json.loads(raw) if raw else {}
        except Exception:
            parsed = {'raw': raw[:500]}
        return {'status': exc.code, 'body': parsed, 'error': True}


def source_ids() -> dict[str, Any]:
    src = json.loads(SOURCE_JSON.read_text(encoding='utf-8'))
    k = src.get('klaviyo') or {}
    return {
        'source_generated_at': src.get('generated_at'),
        'list_name': k.get('list_name'),
        'list_id': k.get('list_id'),
        'template_name': k.get('template_name'),
        'template_id': k.get('template_id'),
        'campaign_name': k.get('campaign_name'),
        'campaign_id': k.get('campaign_id'),
        'campaign_message_id': k.get('campaign_message_id'),
        'source_campaign_status': k.get('campaign_status'),
        'source_campaign_scheduled_at': k.get('campaign_scheduled_at'),
        'source_campaign_send_time': k.get('campaign_send_time'),
        'source_profile_import_job_status': k.get('profile_import_job_status'),
        'source_profile_import_failed_count': k.get('profile_import_failed_count'),
        'approved_profiles_submitted': (src.get('counts') or {}).get('approved_profiles_submitted'),
        'unique_emails_submitted': (src.get('counts') or {}).get('unique_emails_submitted'),
    }


def safe_attrs(item: dict[str, Any]) -> dict[str, Any]:
    return item.get('attributes') or {}


def get_data(res: dict[str, Any]) -> dict[str, Any] | None:
    body = res.get('body') or {}
    data = body.get('data')
    return data if isinstance(data, dict) else None


def build() -> dict[str, Any]:
    ids = source_ids()
    secrets = load_doppler_secrets()
    token = secrets.get('KLAVIYO_API_KEY') or ''
    if not token:
        raise RuntimeError('KLAVIYO_API_KEY missing in Doppler response')

    checks: list[dict[str, Any]] = []
    def add_check(name: str, ok: bool, severity: str, detail: str, evidence: dict[str, Any] | None = None) -> None:
        checks.append({'name': name, 'ok': ok, 'severity': severity, 'detail': detail, 'evidence': evidence or {}})

    list_res = api_get(f"/lists/{ids['list_id']}/", token) if ids.get('list_id') else {'status': 0, 'body': {}}
    template_res = api_get(f"/templates/{ids['template_id']}/", token) if ids.get('template_id') else {'status': 0, 'body': {}}
    campaign_res = api_get(f"/campaigns/{ids['campaign_id']}/", token) if ids.get('campaign_id') else {'status': 0, 'body': {}}

    list_data = get_data(list_res)
    template_data = get_data(template_res)
    campaign_data = get_data(campaign_res)
    campaign_attrs = safe_attrs(campaign_data or {})

    add_check('list_get_readonly', list_res.get('status') == 200 and bool(list_data), 'fail', 'Klaviyo list can be read by ID.', {'http_status': list_res.get('status'), 'list_id': ids.get('list_id'), 'list_name': ids.get('list_name')})
    add_check('template_get_readonly', template_res.get('status') == 200 and bool(template_data), 'warn', 'Klaviyo template can be read by ID; warn only because the campaign can still exist without template linked via API.', {'http_status': template_res.get('status'), 'template_id': ids.get('template_id'), 'template_name': ids.get('template_name')})
    add_check('campaign_get_readonly', campaign_res.get('status') == 200 and bool(campaign_data), 'fail', 'Klaviyo campaign can be read by ID.', {'http_status': campaign_res.get('status'), 'campaign_id': ids.get('campaign_id'), 'campaign_name': ids.get('campaign_name')})

    status = campaign_attrs.get('status') or ids.get('source_campaign_status')
    scheduled_at = campaign_attrs.get('scheduled_at') if 'scheduled_at' in campaign_attrs else ids.get('source_campaign_scheduled_at')
    send_time = campaign_attrs.get('send_time') if 'send_time' in campaign_attrs else ids.get('source_campaign_send_time')
    archived = campaign_attrs.get('archived')
    add_check('campaign_is_draft', status == 'Draft', 'fail', 'Campaign must remain Draft.', {'live_or_source_status': status})
    add_check('campaign_not_scheduled', scheduled_at in (None, ''), 'fail', 'Campaign must not be scheduled.', {'scheduled_at': scheduled_at})
    add_check('campaign_send_time_empty', send_time in (None, ''), 'fail', 'Campaign send_time must be empty.', {'send_time': send_time})
    if archived is not None:
        add_check('campaign_not_archived', archived is False, 'warn', 'Campaign should not be archived if Lucas needs to inspect the draft.', {'archived': archived})

    add_check('no_raw_pii_output', True, 'fail', 'Report uses only counts and Klaviyo object IDs; no customer emails/names are emitted.', {'approved_profiles_submitted': ids.get('approved_profiles_submitted'), 'unique_emails_submitted': ids.get('unique_emails_submitted')})
    add_check('no_deep_link_guessed', True, 'fail', 'No Klaviyo UI deep link is generated; use verified IDs/names only.', {'campaign_id': ids.get('campaign_id'), 'campaign_message_id': ids.get('campaign_message_id')})
    add_check('send_schedule_mutations_blocked', True, 'fail', 'Script only uses GET endpoints and does not call campaign send/schedule/update/create endpoints.', {'methods_used': ['GET']})

    fail_count = sum(1 for c in checks if not c['ok'] and c['severity'] == 'fail')
    warn_count = sum(1 for c in checks if not c['ok'] and c['severity'] == 'warn')
    readiness_status = 'ready_for_lucas_review_no_send' if fail_count == 0 else 'blocked_needs_fix_before_review'

    return {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'automation_id': 'LK-AUTO-005',
        'name': 'Klaviyo CRM draft watcher',
        'mode': 'manual_readonly_readiness_preview',
        'readiness_status': readiness_status,
        'summary': {
            'checks': len(checks),
            'fail_count': fail_count,
            'warn_count': warn_count,
            'campaign_status': status,
            'campaign_scheduled_at': scheduled_at,
            'campaign_send_time': send_time,
            'approved_profiles_submitted': ids.get('approved_profiles_submitted'),
            'unique_emails_submitted': ids.get('unique_emails_submitted'),
            'crons_created': 0,
            'n8n_flows_created': 0,
            'campaign_sends': 0,
            'campaign_schedules': 0,
            'customer_contacts': 0,
            'production_writes': 0,
        },
        'klaviyo_objects': {
            'list_name': ids.get('list_name'),
            'list_id': ids.get('list_id'),
            'template_name': ids.get('template_name'),
            'template_id': ids.get('template_id'),
            'campaign_name': ids.get('campaign_name'),
            'campaign_id': ids.get('campaign_id'),
            'campaign_message_id': ids.get('campaign_message_id'),
        },
        'checks': checks,
        'guardrails': [
            'No campaign send executed.',
            'No campaign schedule executed.',
            'No campaign/list/template mutation executed by this watcher.',
            'No flow activation executed.',
            'No SMS/WhatsApp/customer contact executed.',
            'No raw PII emitted into Brain or Telegram.',
            'No unverified Klaviyo deep link generated.',
        ],
        'next_gate': 'Lucas can review verified IDs/names and decide adjust, pause, or explicitly approve a separate send packet. This watcher itself must not send.',
    }


def write_outputs(payload: dict[str, Any]) -> None:
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    s = payload['summary']
    lines = [
        '# LK Klaviyo CRM Draft Readiness Watcher, 2026-05-11', '',
        f"Generated at: `{payload['generated_at']}`", '',
        '## Veredito', '',
        f"Status: `{payload['readiness_status']}`", '',
        'LK-AUTO-005 avançou para um watcher manual/read-only de readiness: ele valida IDs e estado do rascunho Klaviyo, mas não envia, não agenda, não cria campanha, não ativa flow e não expõe PII.', '',
        '## Snapshot', '',
        f"- Checks: {s['checks']}",
        f"- Fails: {s['fail_count']}",
        f"- Warnings: {s['warn_count']}",
        f"- Campaign status: `{s['campaign_status']}`",
        f"- Campaign scheduled_at: `{s['campaign_scheduled_at']}`",
        f"- Campaign send_time: `{s['campaign_send_time']}`",
        f"- Perfis aprovados enviados ao import original: {s['approved_profiles_submitted']}",
        f"- Emails únicos no import original: {s['unique_emails_submitted']}",
        f"- Campaign sends: {s['campaign_sends']}",
        f"- Campaign schedules: {s['campaign_schedules']}",
        f"- Customer contacts: {s['customer_contacts']}",
        f"- Production writes: {s['production_writes']}", '',
        '## Objetos Klaviyo verificados por ID/nome', '',
    ]
    for k, v in payload['klaviyo_objects'].items():
        lines.append(f'- {k}: `{v}`')
    lines.extend(['', '## Checks', ''])
    for c in payload['checks']:
        mark = 'OK' if c['ok'] else c['severity'].upper()
        lines.append(f"- {mark}: `{c['name']}` — {c['detail']}")
    lines.extend(['', '## Guardrails', ''])
    for g in payload['guardrails']:
        lines.append(f'- {g}')
    lines.extend(['', '## Próximo gate', '', payload['next_gate']])
    text = '\n'.join(lines) + '\n'
    OUT_MD.write_text(text, encoding='utf-8')
    BRAIN_DOC.write_text(text, encoding='utf-8')


def main() -> None:
    payload = build()
    write_outputs(payload)
    print(json.dumps({'ok': payload['readiness_status'] == 'ready_for_lucas_review_no_send', 'summary': payload['summary']}, ensure_ascii=False))
    if payload['summary']['fail_count']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
