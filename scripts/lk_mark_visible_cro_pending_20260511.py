#!/usr/bin/env python3
"""Mark LK visible CRO recommendations as pending future.

Lucas explicitly said: "Deixe em pending o cro visível ok? Faremos no futuro".
This script records that decision in a dated Brain artifact without applying any
Shopify/theme/content writes.
"""
from __future__ import annotations

import json
import pathlib
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'reports/lk-p1-seo-cro-approval-packets-2026-05-11.json'
EXECUTION = ROOT / 'reports/lk-approved-p1-seo-fields-execution-2026-05-11.json'
OUT_JSON = ROOT / 'reports/lk-visible-cro-pending-future-2026-05-11.json'
OUT_MD = ROOT / 'reports/lk-visible-cro-pending-future-2026-05-11.md'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/visible-cro-pending-future-2026-05-11.md'


def main() -> None:
    packets = json.loads(SOURCE.read_text())['packets']
    execution = json.loads(EXECUTION.read_text())
    items = []
    for p in packets:
        items.append({
            'rank': p['rank'],
            'url': p['url'],
            'page_type': p['page_type'],
            'label': p['label'],
            'status': 'pending_future',
            'reason': 'Lucas decidiu deixar CRO visível para o futuro',
            'pending_scope': [
                'visible_h1_or_intro',
                'pdp_or_collection_body_copy',
                'above_the_fold_trust_block',
                'layout_or_theme_adjustment',
            ],
            'cro_preview_bullets': p.get('cro_preview_bullets', []),
            'write_allowed_now': False,
        })
    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'LK visible CRO pending future decision',
        'decision_text': 'Lucas: Deixe em pending o cro visível ok? Faremos no futuro',
        'seo_execution_source': 'reports/lk-approved-p1-seo-fields-execution-2026-05-11.json',
        'approval_packet_source': 'reports/lk-p1-seo-cro-approval-packets-2026-05-11.json',
        'summary': {
            'visible_cro_items_marked_pending_future': len(items),
            'seo_fields_already_executed_verified': execution['summary']['executed_verified'],
            'visible_changes_applied': 0,
            'writes_allowed_now': 0,
        },
        'items': items,
        'not_performed': [
            'visible_h1_update',
            'pdp_body_update',
            'collection_description_update',
            'layout_update',
            'theme_or_liquid_write',
            'image_update',
            'merchant_center_write',
            'feed_update',
            'gsc_admin_change',
            'indexing_api_submit',
            'content_publish',
            'campaign_or_customer_send',
            'cron_creation',
        ],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    lines = [
        '# LK Visible CRO Pending Future, 2026-05-11', '',
        f"Generated at: `{payload['generated_at']}`", '',
        '## Decisão', '',
        'Lucas decidiu deixar o CRO visível em `pending_future` para fazer no futuro. Os SEO fields já executados e verificados continuam documentados; nenhuma mudança visível foi aplicada.', '',
        '## Snapshot', '',
        f"- Itens CRO visível marcados como pending_future: {payload['summary']['visible_cro_items_marked_pending_future']}",
        f"- SEO fields já executados/verificados: {payload['summary']['seo_fields_already_executed_verified']}",
        f"- Mudanças visíveis aplicadas agora: {payload['summary']['visible_changes_applied']}",
        f"- Writes liberados agora: {payload['summary']['writes_allowed_now']}", '',
        '## Itens pendentes', '',
    ]
    for item in items:
        lines.extend([
            f"### {item['rank']}. {item['page_type']} · {item['label']}", '',
            f"- URL: {item['url']}",
            f"- Status: `{item['status']}`",
            '- Escopo pendente: H1/intro, body copy, bloco de confiança above-the-fold ou layout/tema, conforme preview futuro.',
            '- Write permitido agora: false', '',
        ])
    lines.extend(['## O que não foi feito', ''])
    for n in payload['not_performed']:
        lines.append(f'- {n}')
    text = '\n'.join(lines) + '\n'
    OUT_MD.write_text(text, encoding='utf-8')
    BRAIN_DOC.write_text(text, encoding='utf-8')
    print(json.dumps({'ok': True, 'summary': payload['summary']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
