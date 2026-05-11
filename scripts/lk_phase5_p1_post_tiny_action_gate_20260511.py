#!/usr/bin/env python3
"""Create LK Phase 5 post-Tiny-validation action gate.

Combines:
- P1 private queue;
- Evolution audit;
- Tiny validation for recommendation candidates.

Outputs anonymized Brain report and JSON. No PII, no external action.
"""
from __future__ import annotations

import csv
import json
import pathlib
from collections import Counter
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/private_exports/lk_crm')
QUEUE = PRIVATE_DIR / 'lk_phase5_p1_all_ready_channel_queue_2026-05-11.csv'
AUDIT = PRIVATE_DIR / 'lk_phase5_p1_whatsapp_evolution_audit_2026-05-11.csv'
VALIDATION = ROOT / 'reports/lk-phase5-recommendation-matrix-tiny-validation-2026-05-11.json'
OUT_JSON = ROOT / 'reports/lk-phase5-p1-post-tiny-action-gate-2026-05-11.json'
OUT_MD = ROOT / 'reports/lk-phase5-p1-post-tiny-action-gate-2026-05-11.md'


def read_csv(path: pathlib.Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline='') as f:
        return list(csv.DictReader(f))


def main() -> None:
    queue = read_csv(QUEUE)
    audit = read_csv(AUDIT)
    validation = json.loads(VALIDATION.read_text())

    sent_refs = {r['customer_ref'] for r in audit if r.get('send_status') == 'sent'}
    failed_refs = {r['customer_ref'] for r in audit if r.get('send_status') == 'failed'}

    ready_product_size = set()
    ready_by_group = {}
    for g in validation['groups']:
        ready = [c for c in g['candidates'] if c.get('tiny_status') == 'available' and float(c.get('tiny_available_estimated_total') or 0) > 0]
        if ready:
            key = (g['purchase_product'], str(g['purchase_size']))
            ready_product_size.add(key)
            ready_by_group[' | '.join(key)] = {
                'recipient_count': g['recipient_count'],
                'ready_candidates': ready,
            }

    rows = []
    for r in queue:
        key = (r.get('store_purchase_product') or r.get('anchor_product') or '', str(r.get('store_purchase_size') or r.get('anchor_size') or ''))
        if r['customer_ref'] in sent_refs:
            decision = 'HOLD_ALREADY_SENT_WHATSAPP'
        elif r['customer_ref'] in failed_refs:
            decision = 'HOLD_WHATSAPP_FAILED_NUMBER_REVIEW'
        elif key in ready_product_size:
            decision = 'READY_FOR_INTERNAL_COPY_PREVIEW_ONLY'
        else:
            decision = 'HOLD_NO_TINY_VALIDATED_RECOMMENDATION'
        rows.append({
            'customer_ref': r['customer_ref'],
            'channel': r['channel'],
            'segment': r['segment'],
            'purchase_product': key[0],
            'purchase_size': key[1],
            'decision': decision,
        })

    decision_counts = Counter(r['decision'] for r in rows)
    by_channel = Counter(r['channel'] for r in rows)
    by_segment = Counter(r['segment'] for r in rows)

    summary = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'Internal gate after Tiny validation and Evolution audit. No PII, no sends, no writes.',
        'counts': {
            'p1_ready_queue_rows': len(queue),
            'already_sent_whatsapp': decision_counts['HOLD_ALREADY_SENT_WHATSAPP'],
            'failed_whatsapp_number_review': decision_counts['HOLD_WHATSAPP_FAILED_NUMBER_REVIEW'],
            'ready_for_internal_copy_preview_only': decision_counts['READY_FOR_INTERNAL_COPY_PREVIEW_ONLY'],
            'hold_no_tiny_validated_recommendation': decision_counts['HOLD_NO_TINY_VALIDATED_RECOMMENDATION'],
        },
        'by_channel': dict(by_channel),
        'by_segment': dict(by_segment),
        'ready_product_size_groups': ready_by_group,
        'decisions': rows,
        'recommendation': 'Não retomar envios. O único grupo produto+tamanho validado no Tiny pertence a cliente que já recebeu WhatsApp no primeiro lote. As linhas restantes precisam de curadoria manual, remapeamento Tiny ou sourcing sob demanda antes de qualquer nova mensagem ou preview de campanha.',
        'guardrails': [
            'Nenhum envio externo executado',
            'Nenhuma lista ou campanha Klaviyo criada',
            'Nenhum write em Shopify, Tiny ou Supabase',
            'Nenhum PII no relatório Brain',
        ],
    }
    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')

    lines = [
        '# LK Phase 5 P1, gate pós-validação Tiny, 2026-05-11',
        '',
        '## Veredito',
        '',
        summary['recommendation'],
        '',
        '## Contagens',
        '',
    ]
    for k, v in summary['counts'].items():
        lines.append(f'- {k}: {v}')
    lines += ['', '## Leitura operacional', '']
    lines += [
        '- O snapshot local do Shopify sugeria disponibilidade para vários candidatos, mas a validação read-only no Tiny derrubou quase todos por zero estoque ou falta de mapeamento.',
        '- O único grupo com candidato realmente disponível no Tiny já pertence a cliente que recebeu WhatsApp no primeiro lote.',
        '- Portanto, não há nova linha segura para retomar disparo agora.',
        '- Próximo trabalho seguro: curadoria manual dos 12 pendentes, remap de SKU/Tiny para itens not_mapped, ou sourcing sob demanda para Jacquemus/Onitsuka antes de qualquer copy final.',
    ]
    lines += ['', '## Grupos com Tiny validado', '']
    if ready_by_group:
        for group_key, payload in ready_by_group.items():
            lines.append(f'- {group_key}: {len(payload["ready_candidates"])} candidato(s) com Tiny disponível')
    else:
        lines.append('- Nenhum grupo validado.')
    lines += ['', '## Guardrails', '']
    for guardrail in summary['guardrails']:
        lines.append(f'- {guardrail}')
    OUT_MD.write_text('\n'.join(lines) + '\n')

    print(json.dumps(summary['counts'], ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
