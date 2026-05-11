#!/usr/bin/env python3
"""Send LK Phase 5 P1 WhatsApp concierge messages via Evolution API.

Default is dry-run. Use --execute only after explicit Lucas approval. Keeps PII in
private_exports and writes an anonymized Brain report.
"""
from __future__ import annotations

import argparse
import base64
import csv
import hashlib
import json
import pathlib
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/private_exports/lk_crm')
INPUT = PRIVATE_DIR / 'lk_phase5_p1_whatsapp_approved_manual_send_2026-05-11.csv'
AUDIT = PRIVATE_DIR / 'lk_phase5_p1_whatsapp_evolution_audit_2026-05-11.csv'
OUT_JSON = ROOT / 'reports/lk-phase5-p1-whatsapp-evolution-send-2026-05-11.json'
OUT_MD = ROOT / 'reports/lk-phase5-p1-whatsapp-evolution-send-2026-05-11.md'
DOPPLER_TOKEN_FILE = pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')


def safe_ref(value: str) -> str:
    return hashlib.sha256((value or '').encode()).hexdigest()[:12]


def normalize_phone(phone: str) -> str:
    digits = ''.join(ch for ch in (phone or '') if ch.isdigit())
    if not digits:
        return ''
    if digits.startswith('55'):
        return digits
    return '55' + digits


def load_secrets() -> dict[str, str]:
    token = DOPPLER_TOKEN_FILE.read_text().strip()
    req = urllib.request.Request('https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json')
    req.add_header('Authorization', 'Basic ' + base64.b64encode((token + ':').encode()).decode())
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def send_text(base_url: str, api_key: str, instance: str, number: str, text: str) -> tuple[int, str]:
    url = base_url.rstrip('/') + '/message/sendText/' + urllib.parse.quote(instance, safe='')
    body = json.dumps({'number': number, 'text': text}, ensure_ascii=False).encode()
    req = urllib.request.Request(url, data=body, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('apikey', api_key)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.status, r.read(500).decode('utf-8', 'replace')


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--execute', action='store_true', help='Actually send messages')
    ap.add_argument('--delay-seconds', type=float, default=8.0)
    args = ap.parse_args()

    rows = list(csv.DictReader(INPUT.open(newline='')))
    # De-dupe by normalized phone; keep first row/message per phone.
    deduped = []
    seen = set()
    for r in rows:
        number = normalize_phone(r.get('phone', ''))
        if not number or number in seen:
            continue
        seen.add(number)
        r['_normalized_phone'] = number
        deduped.append(r)

    status_rows = []
    sent = 0
    failed = 0
    mode = 'EXECUTE_SEND' if args.execute else 'DRY_RUN_NO_SEND'
    secrets_loaded = False
    base_url = api_key = instance = ''
    if args.execute:
        s = load_secrets()
        secrets_loaded = True
        base_url = (s.get('EVOLUTION_API_BASE_URL') or s.get('EVOLUTION_API_URL') or '').rstrip('/')
        api_key = s.get('EVOLUTION_API_KEY') or s.get('EVOLUTION_API_TOKEN') or ''
        instance = s.get('EVOLUTION_INSTANCE') or s.get('EVOLUTION_INSTANCE_NAME') or ''
        if not (base_url and api_key and instance):
            raise RuntimeError('Missing Evolution API configuration')

    for i, r in enumerate(deduped, start=1):
        number = r['_normalized_phone']
        message = r.get('message_approved_manual') or ''
        result = {
            'generated_at': datetime.now(timezone.utc).isoformat(),
            'mode': mode,
            'customer_ref': r.get('customer_ref', ''),
            'phone_hash': safe_ref(number),
            'segment': r.get('segment', ''),
            'recommended_product': r.get('recommended_product', ''),
            'message_chars': len(message),
            'send_status': 'not_sent_dry_run',
            'http_status': '',
            'error_type': '',
        }
        if args.execute:
            try:
                status, _body = send_text(base_url, api_key, instance, number, message)
                result['send_status'] = 'sent'
                result['http_status'] = str(status)
                sent += 1
            except urllib.error.HTTPError as e:
                result['send_status'] = 'failed'
                result['http_status'] = str(e.code)
                result['error_type'] = 'HTTPError'
                failed += 1
            except Exception as e:  # noqa: BLE001
                result['send_status'] = 'failed'
                result['error_type'] = type(e).__name__
                failed += 1
            if i < len(deduped):
                time.sleep(args.delay_seconds)
        status_rows.append(result)

    fieldnames = list(status_rows[0].keys()) if status_rows else ['generated_at','mode']
    with AUDIT.open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader(); w.writerows(status_rows)
    AUDIT.chmod(0o600)

    counts = {
        'input_rows': len(rows),
        'deduped_phone_recipients': len(deduped),
        'sent': sent,
        'failed': failed,
        'dry_run_not_sent': 0 if args.execute else len(deduped),
    }
    summary = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'mode': mode,
        'secrets_loaded': secrets_loaded,
        'counts': counts,
        'private_audit': str(AUDIT),
        'guardrails': [
            'Uses approved physical-store-only WhatsApp file',
            'Dedupes by normalized phone before sending',
            'No phone numbers, names, or message bodies in Brain report',
            'Does not touch Klaviyo/Shopify/Tiny/Supabase',
        ],
    }
    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')
    lines = [
        '# LK Phase 5 P1 — WhatsApp Evolution send log — 2026-05-11', '',
        '## Veredito', '',
        ('Mensagens enviadas via Evolution.' if args.execute else 'Dry-run concluído; nenhuma mensagem enviada.'), '',
        '## Modo', '', f'- {mode}', '', '## Contagens', '',
    ]
    for k, v in counts.items():
        lines.append(f'- {k}: {v}')
    lines += ['', '## Arquivo privado de auditoria', '', f'- `{AUDIT}`', '', '## Guardrails', '']
    for g in summary['guardrails']:
        lines.append(f'- {g}')
    OUT_MD.write_text('\n'.join(lines) + '\n')
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
