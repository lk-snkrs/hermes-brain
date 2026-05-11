#!/usr/bin/env python3
"""Create approved LK Phase 5 P1 Klaviyo list + reusable email template, no send.

External writes performed only after Lucas approval:
- Creates/reuses a Klaviyo list for the approved P1 physical-store queue.
- Imports/upserts approved profiles into that list with LK custom properties.
- Creates/reuses an email template containing the approved customer-facing HTML.

Guardrails:
- Does not create or schedule a campaign send.
- Does not send any email/SMS.
- Does not print secrets or raw PII.
"""
from __future__ import annotations

import base64
import csv
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PRIVATE_IMPORT = Path('/opt/data/hermes_bruno_ingest/private_exports/lk_crm/lk_phase5_p1_klaviyo_approved_import_2026-05-11.csv')
EMAIL_HTML = ROOT / 'reports/lk-phase5-p1-klaviyo-approved-email-2026-05-11.html'
OUT_JSON = ROOT / 'reports/lk-phase5-p1-klaviyo-klaviyo-objects-2026-05-11.json'
OUT_MD = ROOT / 'reports/lk-phase5-p1-klaviyo-klaviyo-objects-2026-05-11.md'
DOPPLER_TOKEN_FILE = Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
REVISION = '2025-10-15'
BASE = 'https://a.klaviyo.com/api'
LIST_NAME = 'LK Phase 5 P1 Loja Física Recompra 2026-05-11'
TEMPLATE_NAME = 'LK Phase 5 P1 Curadoria Loja Física 2026-05-11'


def load_doppler_secrets() -> dict[str, str]:
    token = DOPPLER_TOKEN_FILE.read_text().strip()
    req = urllib.request.Request('https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json')
    req.add_header('Authorization', 'Basic ' + base64.b64encode((token + ':').encode()).decode())
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())


def api_request(method: str, path: str, token: str, body: dict[str, Any] | None = None, query: dict[str, str] | None = None) -> dict[str, Any]:
    url = BASE + path
    if query:
        url += '?' + urllib.parse.urlencode(query)
    data = None if body is None else json.dumps(body, ensure_ascii=False).encode()
    req = urllib.request.Request(url, data=data, method=method)
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


def read_private_rows() -> list[dict[str, str]]:
    with PRIVATE_IMPORT.open(newline='') as f:
        rows = list(csv.DictReader(f))
    missing = [idx for idx, row in enumerate(rows, 1) if not row.get('email')]
    if missing:
        raise RuntimeError(f'approved import has rows without email: {missing}')
    return rows


def list_all(token: str, path: str) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    cursor: str | None = None
    for _ in range(10):
        query = {'page[size]': '10'}
        if cursor:
            query['page[cursor]'] = cursor
        res = api_request('GET', path, token, query=query)
        if res.get('status', 0) >= 400:
            raise RuntimeError(f'GET {path} failed status={res.get("status")} body={json.dumps(res.get("body"), ensure_ascii=False)[:500]}')
        body = res.get('body') or {}
        out.extend(body.get('data') or [])
        next_url = ((body.get('links') or {}).get('next'))
        if not next_url:
            break
        parsed = urllib.parse.urlparse(next_url)
        qs = urllib.parse.parse_qs(parsed.query)
        cursor_vals = qs.get('page[cursor]')
        if not cursor_vals:
            break
        cursor = cursor_vals[0]
    return out


def find_by_name(token: str, path: str, name: str) -> dict[str, Any] | None:
    for item in list_all(token, path):
        if ((item.get('attributes') or {}).get('name') or '').strip() == name:
            return item
    return None


def create_or_get_list(token: str) -> tuple[str, bool]:
    existing = find_by_name(token, '/lists/', LIST_NAME)
    if existing:
        return existing['id'], False
    body = {'data': {'type': 'list', 'attributes': {'name': LIST_NAME}}}
    res = api_request('POST', '/lists/', token, body=body)
    if res.get('status') not in (200, 201, 202):
        raise RuntimeError(f'Create list failed status={res.get("status")} body={json.dumps(res.get("body"), ensure_ascii=False)[:700]}')
    return res['body']['data']['id'], True


def create_profile_import_job(token: str, list_id: str, rows: list[dict[str, str]]) -> tuple[str | None, int, dict[str, Any]]:
    profiles = []
    for row in rows:
        profiles.append({
            'type': 'profile',
            'attributes': {
                'email': row.get('email', '').strip(),
                'first_name': row.get('first_name', '').strip(),
                'properties': {
                    'customer_ref': row.get('customer_ref', ''),
                    'lk_segment': row.get('lk_segment', ''),
                    'lk_campaign': row.get('lk_campaign', ''),
                    'lk_purchase_product': row.get('lk_purchase_product', ''),
                    'lk_purchase_size': row.get('lk_purchase_size', ''),
                    'lk_recommended_product': row.get('lk_recommended_product', ''),
                    'lk_recommended_size': row.get('lk_recommended_size', ''),
                    'lk_recommended_sku': row.get('lk_recommended_sku', ''),
                    'lk_copy_angle': row.get('lk_copy_angle', ''),
                    'lk_approval_status': row.get('approval_status', ''),
                },
            },
        })
    body = {
        'data': {
            'type': 'profile-bulk-import-job',
            'attributes': {'profiles': {'data': profiles}},
            'relationships': {'lists': {'data': [{'type': 'list', 'id': list_id}]}},
        }
    }
    res = api_request('POST', '/profile-bulk-import-jobs/', token, body=body)
    if res.get('status') not in (200, 201, 202):
        raise RuntimeError(f'Profile import failed status={res.get("status")} body={json.dumps(res.get("body"), ensure_ascii=False)[:1000]}')
    data = res.get('body', {}).get('data') or {}
    return data.get('id'), res.get('status'), res.get('body') or {}


def create_or_get_template(token: str, html: str) -> tuple[str, bool]:
    existing = find_by_name(token, '/templates/', TEMPLATE_NAME)
    if existing:
        return existing['id'], False
    body = {'data': {'type': 'template', 'attributes': {'name': TEMPLATE_NAME, 'editor_type': 'CODE', 'html': html}}}
    res = api_request('POST', '/templates/', token, body=body)
    if res.get('status') not in (200, 201, 202):
        raise RuntimeError(f'Create template failed status={res.get("status")} body={json.dumps(res.get("body"), ensure_ascii=False)[:1000]}')
    return res['body']['data']['id'], True


def create_or_get_campaign_draft(token: str, list_id: str) -> tuple[str, str | None, bool, dict[str, Any]]:
    name = 'LK Phase 5 P1 Curadoria Loja Física 2026-05-11, DRAFT'
    res = api_request('GET', '/campaigns/', token, query={'filter': "equals(messages.channel,'email')", 'page[size]': '10'})
    if res.get('status') == 200:
        for item in res.get('body', {}).get('data') or []:
            if (item.get('attributes') or {}).get('name') == name:
                messages = ((item.get('relationships') or {}).get('campaign-messages') or {}).get('data') or []
                return item['id'], (messages[0].get('id') if messages else None), False, item
    body = {
        'data': {
            'type': 'campaign',
            'attributes': {
                'name': name,
                'audiences': {'included': [list_id], 'excluded': []},
                'send_options': {'use_smart_sending': False, 'ignore_unsubscribes': False},
                'tracking_options': {'is_tracking_clicks': True, 'is_tracking_opens': True, 'add_tracking_params': False},
                'campaign-messages': {'data': [{
                    'type': 'campaign-message',
                    'attributes': {'definition': {'channel': 'email', 'label': name, 'content': {
                        'subject': 'Uma curadoria LK pensada para você',
                        'preview_text': 'Selecionamos algumas opções com o olhar da LK Flagship para o seu próximo sneaker.',
                        'from_email': 'contato@lksneakers.com.br',
                        'from_label': 'LK Sneakers',
                    }}},
                }]},
            },
        }
    }
    res = api_request('POST', '/campaigns/', token, body=body)
    if res.get('status') not in (200, 201, 202):
        raise RuntimeError(f'Create campaign draft failed status={res.get("status")} body={json.dumps(res.get("body"), ensure_ascii=False)[:1000]}')
    item = res['body']['data']
    messages = ((item.get('relationships') or {}).get('campaign-messages') or {}).get('data') or []
    return item['id'], (messages[0].get('id') if messages else None), True, item


def main() -> None:
    rows = read_private_rows()
    html = EMAIL_HTML.read_text()
    secrets = load_doppler_secrets()
    token = secrets.get('KLAVIYO_API_KEY') or ''
    if not token:
        raise RuntimeError('KLAVIYO_API_KEY missing in Doppler response')

    list_id, list_created = create_or_get_list(token)
    job_id, import_status, _ = create_profile_import_job(token, list_id, rows)
    template_id, template_created = create_or_get_template(token, html)
    campaign_id, campaign_message_id, campaign_created, campaign = create_or_get_campaign_draft(token, list_id)
    campaign_attrs = campaign.get('attributes') or {}

    summary = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'Klaviyo list + template + campaign draft created/reused after Lucas approval. No campaign send, no schedule, no flow activation.',
        'klaviyo': {
            'list_name': LIST_NAME,
            'list_id': list_id,
            'list_created': list_created,
            'profile_import_job_id': job_id,
            'profile_import_http_status': import_status,
            'template_name': TEMPLATE_NAME,
            'template_id': template_id,
            'template_created': template_created,
            'campaign_name': 'LK Phase 5 P1 Curadoria Loja Física 2026-05-11, DRAFT',
            'campaign_id': campaign_id,
            'campaign_message_id': campaign_message_id,
            'campaign_created': campaign_created,
            'campaign_status': campaign_attrs.get('status'),
            'campaign_scheduled_at': campaign_attrs.get('scheduled_at'),
            'campaign_send_time': campaign_attrs.get('send_time'),
            'campaign_template_note': 'Template HTML was created in Klaviyo. API draft campaign was created with audience/subject/from fields; template HTML may need to be selected in Klaviyo UI before final send approval.',
        },
        'counts': {
            'approved_profiles_submitted': len(rows),
            'unique_emails_submitted': len({r.get('email') for r in rows if r.get('email')}),
        },
        'source_files': {
            'approved_private_import': str(PRIVATE_IMPORT),
            'approved_html': str(EMAIL_HTML.relative_to(ROOT)),
        },
        'guardrails': [
            'No campaign send executed',
            'No campaign schedule executed',
            'No flow activation executed',
            'No SMS/WhatsApp action executed',
            'No raw PII in Brain report',
        ],
    }
    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')
    lines = [
        '# LK Phase 5 P1, Klaviyo objects, 2026-05-11', '',
        '## Veredito', '',
        'Criei/reusei os objetos aprovados no Klaviyo para deixar a ação pronta como rascunho operacional. Nenhum envio, agendamento ou flow foi ativado.', '',
        '## Klaviyo', '',
        f'- Lista: `{LIST_NAME}`',
        f'- List ID: `{list_id}`',
        f'- Lista criada agora: {list_created}',
        f'- Profile import job ID: `{job_id}`',
        f'- Template: `{TEMPLATE_NAME}`',
        f'- Template ID: `{template_id}`',
        f'- Template criado agora: {template_created}',
        f'- Campaign draft: `LK Phase 5 P1 Curadoria Loja Física 2026-05-11, DRAFT`',
        f'- Campaign ID: `{campaign_id}`',
        f'- Campaign message ID: `{campaign_message_id}`',
        f'- Campaign criada agora: {campaign_created}',
        f'- Campaign status: `{campaign_attrs.get("status")}`',
        f'- Campaign scheduled_at: `{campaign_attrs.get("scheduled_at")}`',
        f'- Campaign send_time: `{campaign_attrs.get("send_time")}`',
        '- Observação: o template HTML aprovado foi criado no Klaviyo; o rascunho da campanha está com público/assunto/remetente, e o HTML pode precisar ser selecionado no editor antes da aprovação final de envio.', '',
        '## Contagens', '',
        f'- Perfis aprovados submetidos: {len(rows)}',
        f'- E-mails únicos submetidos: {len({r.get("email") for r in rows if r.get("email")})}', '',
        '## Guardrails', '',
    ]
    for item in summary['guardrails']:
        lines.append(f'- {item}')
    OUT_MD.write_text('\n'.join(lines) + '\n')
    print(json.dumps({
        'list_id': list_id,
        'list_created': list_created,
        'profile_import_job_id': job_id,
        'template_id': template_id,
        'template_created': template_created,
        'campaign_id': campaign_id,
        'campaign_message_id': campaign_message_id,
        'campaign_created': campaign_created,
        'campaign_status': campaign_attrs.get('status'),
        'campaign_scheduled_at': campaign_attrs.get('scheduled_at'),
        'campaign_send_time': campaign_attrs.get('send_time'),
        'profiles_submitted': len(rows),
        'outputs': {'json': str(OUT_JSON), 'md': str(OUT_MD)},
    }, ensure_ascii=False))


if __name__ == '__main__':
    main()
