#!/usr/bin/env python3
"""Validate LK Phase 5 recommendation-matrix candidates against Tiny stock.

Read-only. Uses Doppler in-process for Tiny token and never prints secrets.
Inputs:
- reports/lk-phase5-purchase-to-recommendation-matrix-2026-05-11.json
Outputs:
- reports/lk-phase5-recommendation-matrix-tiny-validation-2026-05-11.json
- reports/lk-phase5-recommendation-matrix-tiny-validation-2026-05-11.md

No customer PII, no external sends, no writes to Tiny/Shopify/Supabase/Klaviyo/WhatsApp.
"""
from __future__ import annotations

import json
import pathlib
import sys
from collections import Counter
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))

from lk_phase5_p1_recipients_tiny_stock_20260511 import find_tiny_variant_stock, load_secrets  # noqa: E402

IN_JSON = ROOT / 'reports/lk-phase5-purchase-to-recommendation-matrix-2026-05-11.json'
OUT_JSON = ROOT / 'reports/lk-phase5-recommendation-matrix-tiny-validation-2026-05-11.json'
OUT_MD = ROOT / 'reports/lk-phase5-recommendation-matrix-tiny-validation-2026-05-11.md'


def validate() -> dict:
    matrix = json.loads(IN_JSON.read_text())
    secrets = load_secrets()
    tiny_token = secrets['TINY_API_TOKEN']

    validation_cache: dict[tuple[str, str, str], dict] = {}
    groups = []
    for group in matrix['groups']:
        candidates = []
        for c in group.get('candidates') or []:
            sku = str(c.get('sku') or '')
            title = str(c.get('title') or '')
            size = str(c.get('variant_title') or group.get('purchase_size') or '')
            key = (sku, title, size)
            if key not in validation_cache:
                validation_cache[key] = find_tiny_variant_stock(tiny_token, sku, title, size)
            tiny = validation_cache[key]
            candidate = {
                'title': title,
                'size': size,
                'sku': sku,
                'shopify_snapshot_inventory': c.get('inventory_quantity'),
                'shopify_snapshot_price': c.get('price'),
                'tiny_status': tiny.get('status'),
                'tiny_match_count': tiny.get('match_count'),
                'tiny_available_estimated_total': tiny.get('available_estimated_total'),
            }
            candidates.append(candidate)
        ready_candidates = [c for c in candidates if c.get('tiny_status') == 'available' and float(c.get('tiny_available_estimated_total') or 0) > 0]
        groups.append({
            'purchase_product': group['purchase_product'],
            'purchase_size': group['purchase_size'],
            'recipient_count': group['recipient_count'],
            'style_family': group['style_family'],
            'recommendation_basis': group['recommendation_basis'],
            'ready_candidate_count': len(ready_candidates),
            'candidate_count': len(candidates),
            'status': 'TINY_VALIDATED_READY_FOR_COPY_PREVIEW' if ready_candidates else 'NO_TINY_READY_CANDIDATE_REQUIRES_MANUAL_REVIEW',
            'candidates': candidates,
        })

    status_counter = Counter(g['status'] for g in groups)
    candidate_status_counter = Counter(c['tiny_status'] for g in groups for c in g['candidates'])
    return {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'Read-only Tiny validation for LK Phase 5 P1 recommendation matrix. No PII, no sends, no writes.',
        'input_matrix': str(IN_JSON),
        'counts': {
            'groups_total': len(groups),
            'groups_tiny_validated_ready': status_counter['TINY_VALIDATED_READY_FOR_COPY_PREVIEW'],
            'groups_requiring_manual_review': status_counter['NO_TINY_READY_CANDIDATE_REQUIRES_MANUAL_REVIEW'],
            'candidate_rows_checked': sum(len(g['candidates']) for g in groups),
        },
        'candidate_tiny_status': dict(candidate_status_counter),
        'groups': groups,
        'guardrails': [
            'Read-only Tiny API calls only',
            'No customer-facing message generated or sent',
            'No Klaviyo list or campaign created',
            'No Shopify, Supabase or Tiny writes',
            'No PII in Brain outputs',
        ],
    }


def write_markdown(summary: dict) -> None:
    lines = [
        '# LK Phase 5, validação Tiny da matriz de recomendações, 2026-05-11',
        '',
        '## Veredito',
        '',
        'Validação read-only feita no Tiny para os candidatos da matriz Produto Comprado para Sugestão de Moda. O próximo passo continua sendo preview interno de copy, não envio.',
        '',
        '## Contagens',
        '',
    ]
    for k, v in summary['counts'].items():
        lines.append(f'- {k}: {v}')
    lines += ['', '## Status dos candidatos no Tiny', '']
    for k, v in summary['candidate_tiny_status'].items():
        lines.append(f'- {k}: {v}')
    lines += ['', '## Grupos validados', '']
    for group in summary['groups']:
        lines += [
            f"### {group['purchase_product']} | tamanho {group['purchase_size']} | {group['recipient_count']} linha(s)",
            f"- Status: {group['status']}",
            f"- Candidatos prontos no Tiny: {group['ready_candidate_count']} de {group['candidate_count']}",
        ]
        if group['candidates']:
            for idx, c in enumerate(group['candidates'], 1):
                price = c.get('shopify_snapshot_price')
                price_txt = f"R$ {price:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.') if isinstance(price, (int, float)) else ''
                lines.append(
                    f"  {idx}. {c['title']} | tamanho {c['size']} | SKU {c['sku']} | Tiny {c['tiny_status']} | disp. estimada {c['tiny_available_estimated_total']} | snapshot Shopify {c['shopify_snapshot_inventory']} | {price_txt}"
                )
        else:
            lines.append('- Sem candidatos da matriz para validar no Tiny.')
        lines.append('')
    lines += ['## Guardrails', '']
    for guardrail in summary['guardrails']:
        lines.append(f'- {guardrail}')
    OUT_MD.write_text('\n'.join(lines) + '\n')


def main() -> None:
    summary = validate()
    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')
    write_markdown(summary)
    print(json.dumps(summary['counts'], ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
