#!/usr/bin/env python3
"""Prepare LK Phase 5 P1 approved action files from physical-store-only queue.

Creates private PII-bearing files under private_exports (chmod 600) and a no-PII Brain
report. Does not send WhatsApp, create Klaviyo lists, or write to any external system.
"""
from __future__ import annotations

import csv
import json
import pathlib
from collections import Counter
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/private_exports/lk_crm')
SOURCE_ALL = PRIVATE_DIR / 'lk_phase5_p1_all_ready_channel_queue_2026-05-11.csv'
SOURCE_KL = PRIVATE_DIR / 'lk_phase5_p1_klaviyo_ready_2026-05-11.csv'
SOURCE_WA = PRIVATE_DIR / 'lk_phase5_p1_whatsapp_concierge_ready_2026-05-11.csv'
APPROVED_ALL = PRIVATE_DIR / 'lk_phase5_p1_all_approved_not_sent_2026-05-11.csv'
APPROVED_KL = PRIVATE_DIR / 'lk_phase5_p1_klaviyo_approved_import_2026-05-11.csv'
APPROVED_WA = PRIVATE_DIR / 'lk_phase5_p1_whatsapp_approved_manual_send_2026-05-11.csv'
OUT_JSON = ROOT / 'reports/lk-phase5-p1-approved-action-files-2026-05-11.json'
OUT_MD = ROOT / 'reports/lk-phase5-p1-approved-action-files-2026-05-11.md'


def read_csv(path: pathlib.Path) -> list[dict[str, str]]:
    with path.open(newline='') as f:
        return list(csv.DictReader(f))


def write_csv(path: pathlib.Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    with path.open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        w.writeheader()
        w.writerows(rows)
    path.chmod(0o600)


def build_whatsapp_message(row: dict[str, str]) -> str:
    first = (row.get('first_name') or '').strip() or '{first_name}'
    preview = (row.get('copy_preview_internal') or '').strip()
    return preview.replace('{first_name}', first)


def main() -> None:
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    PRIVATE_DIR.chmod(0o700)

    all_rows = read_csv(SOURCE_ALL)
    kl_rows = read_csv(SOURCE_KL)
    wa_rows = read_csv(SOURCE_WA)

    for r in all_rows:
        r['approval_status'] = 'APPROVED_BY_LUCAS_READY_NOT_SENT'
        r['approval_note'] = 'Lucas approved continuing after physical-store-only filter and direct copy correction.'

    kl_import = []
    for r in kl_rows:
        kl_import.append({
            'email': r.get('email', ''),
            'first_name': r.get('first_name', ''),
            'customer_ref': r.get('customer_ref', ''),
            'lk_segment': r.get('segment', ''),
            'lk_campaign': 'LK_PHASE5_P1_LOJA_FISICA_RECOMPRA_20260511',
            'lk_purchase_product': r.get('store_purchase_product', ''),
            'lk_purchase_size': r.get('store_purchase_size', ''),
            'lk_recommended_product': r.get('anchor_product', ''),
            'lk_recommended_size': r.get('anchor_size', ''),
            'lk_recommended_sku': r.get('anchor_sku', ''),
            'lk_copy_angle': r.get('copy_angle', ''),
            'lk_copy_preview_internal': r.get('copy_preview_internal', ''),
            'approval_status': 'APPROVED_BY_LUCAS_READY_NOT_SENT',
        })

    wa_manual = []
    for r in wa_rows:
        wa_manual.append({
            'phone': r.get('phone', ''),
            'first_name': r.get('first_name', ''),
            'customer_ref': r.get('customer_ref', ''),
            'segment': r.get('segment', ''),
            'purchase_product': r.get('store_purchase_product', ''),
            'purchase_size': r.get('store_purchase_size', ''),
            'recommended_product': r.get('anchor_product', ''),
            'recommended_size': r.get('anchor_size', ''),
            'recommended_sku': r.get('anchor_sku', ''),
            'message_approved_manual': build_whatsapp_message(r),
            'approval_status': 'APPROVED_BY_LUCAS_READY_NOT_SENT',
        })

    write_csv(APPROVED_ALL, all_rows, list(all_rows[0].keys()) if all_rows else [])
    write_csv(APPROVED_KL, kl_import, list(kl_import[0].keys()) if kl_import else [])
    write_csv(APPROVED_WA, wa_manual, list(wa_manual[0].keys()) if wa_manual else [])

    by_channel = Counter(r.get('channel', '') for r in all_rows)
    by_segment = Counter(r.get('segment', '') for r in all_rows)
    by_product = Counter(r.get('anchor_product', '') for r in all_rows)
    by_wa_product = Counter(r.get('recommended_product', '') for r in wa_manual)
    by_kl_product = Counter(r.get('lk_recommended_product', '') for r in kl_import)

    summary = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'Approved action files only; no external send/list/write executed.',
        'approval_basis': 'Lucas said “Seguir aprovado” after physical-store-only correction and copy refinement.',
        'private_exports': {
            'all_approved_not_sent': str(APPROVED_ALL),
            'klaviyo_approved_import': str(APPROVED_KL),
            'whatsapp_approved_manual_send': str(APPROVED_WA),
        },
        'counts': {
            'all_approved_rows': len(all_rows),
            'klaviyo_import_rows': len(kl_import),
            'whatsapp_manual_rows': len(wa_manual),
            'klaviyo_unique_emails': len({r.get('email') for r in kl_import if r.get('email')}),
            'whatsapp_unique_phones': len({r.get('phone') for r in wa_manual if r.get('phone')}),
        },
        'by_channel': dict(by_channel),
        'by_segment': dict(by_segment),
        'top_products_all': dict(by_product.most_common(10)),
        'top_products_whatsapp': dict(by_wa_product.most_common(10)),
        'top_products_klaviyo': dict(by_kl_product.most_common(10)),
        'guardrails': [
            'No WhatsApp/Evolution send executed',
            'No Klaviyo list or campaign created',
            'No Shopify/Tiny/Supabase write',
            'PII kept only in private_exports with chmod 600',
            'Brain report contains counts/products only, no raw email/phone/name',
        ],
    }
    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')

    lines = [
        '# LK Phase 5 P1, arquivos aprovados para ação (sem envio), 2026-05-11', '',
        '## Veredito', '',
        'Arquivos finais foram preparados com status aprovado, mantendo a regra de loja física/POS e copy direta por produto comprado. Nenhum envio externo foi executado.', '',
        '## Base de aprovação', '',
        '- Aprovação recebida: “Seguir aprovado”.',
        '- Escopo aplicado: clientes com compra-âncora na LK Flagship/loja física.',
        '- Canais preparados: WhatsApp concierge manual e Klaviyo import.', '',
        '## Contagens', '',
    ]
    for k, v in summary['counts'].items():
        lines.append(f'- {k}: {v}')
    lines += ['', '## Distribuição por canal', '']
    for k, v in by_channel.items():
        lines.append(f'- {k}: {v}')
    lines += ['', '## Distribuição por segmento', '']
    for k, v in by_segment.items():
        lines.append(f'- {k}: {v}')
    lines += ['', '## Top produtos, todos', '']
    for k, v in by_product.most_common(10):
        lines.append(f'- {k}: {v}')
    lines += ['', '## Arquivos privados gerados', '']
    for path in summary['private_exports'].values():
        lines.append(f'- `{path}`')
    lines += ['', '## Guardrails', '']
    for g in summary['guardrails']:
        lines.append(f'- {g}')
    OUT_MD.write_text('\n'.join(lines) + '\n')
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
