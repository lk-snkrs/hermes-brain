#!/usr/bin/env python3
"""Generate LK Phase 5 P1 final channel lists from local SQL.

Creates:
- Private import/ops CSVs under /opt/data/hermes_bruno_ingest/private_exports/lk_crm/ (chmod 600)
- Public/anonymized Brain report under reports/ (no PII)

No external sends, no Klaviyo/WhatsApp writes, no Shopify/Tiny/Supabase writes.
"""
from __future__ import annotations

import csv
import json
import pathlib
import sqlite3
from collections import Counter, defaultdict
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
DB = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite')
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/private_exports/lk_crm')
P1_IDS = PRIVATE_DIR / 'lk_phase5_p1_recipient_ids_2026-05-11.json'
OUT_MD = ROOT / 'reports/lk-phase5-p1-final-channel-lists-preview-2026-05-11.md'
OUT_JSON = ROOT / 'reports/lk-phase5-p1-final-channel-lists-preview-2026-05-11.json'
PRIVATE_WA = PRIVATE_DIR / 'lk_phase5_p1_whatsapp_concierge_ready_2026-05-11.csv'
PRIVATE_KL = PRIVATE_DIR / 'lk_phase5_p1_klaviyo_ready_2026-05-11.csv'
PRIVATE_ALL = PRIVATE_DIR / 'lk_phase5_p1_all_ready_channel_queue_2026-05-11.csv'


def copy_for(segment: str, product: str, channel: str) -> tuple[str, str]:
    # Internal preview only. Final copy should be reviewed before any send.
    product_short = product.replace('Tênis ', '').strip()
    if segment == 'Champions/VIP' and channel == 'whatsapp_concierge':
        return (
            'VIP concierge / curadoria reservada',
            f'Oi {{first_name}}, tudo bem? Vi aqui que você já comprou peças bem especiais com a LK. Entrou disponibilidade em tamanho próximo ao seu perfil de {product_short}. Se fizer sentido, te mando as opções antes de abrir para a base.',
        )
    if segment == 'Champions/VIP':
        return (
            'VIP limitado / sem desconto',
            f'Uma curadoria reservada da LK para clientes recorrentes: {product_short} em tamanhos selecionados, com atendimento próximo e sem comunicação massiva.',
        )
    if segment == 'Novo alto potencial':
        return (
            'Segunda compra / best-seller real',
            f'Depois da sua primeira escolha na LK, separamos uma recomendação com base em um modelo que vem performando bem e com disponibilidade real no seu tamanho: {product_short}.',
        )
    return (
        'Recompra por afinidade',
        f'Seleção LK baseada no seu histórico de compra e em disponibilidade real: {product_short}.',
    )


def main() -> None:
    now = datetime.now(timezone.utc).isoformat()
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    PRIVATE_DIR.chmod(0o700)

    id_data = json.loads(P1_IDS.read_text())
    id_by_ref = {r['customer_ref']: r for r in id_data['candidate_rows']}

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    p1 = [dict(r) for r in conn.execute('SELECT * FROM p1_candidate_recipients')]
    groups = {r['group_key']: dict(r) for r in conn.execute('SELECT * FROM final_approval_groups')}
    stock = {(r['anchor_product'], r['size'], r['sku']): dict(r) for r in conn.execute('SELECT * FROM tiny_anchor_stock')}
    customers = {str(r['customer_id']): dict(r) for r in conn.execute('SELECT customer_id,email,phone,first_name,last_name,full_name,accepts_marketing FROM lk_customers')}
    conn.close()

    ready_rows = []
    blocked_rows = []
    for r in p1:
        st = stock.get((r['anchor_product'], r['anchor_size'], r['anchor_sku']))
        private = id_by_ref.get(r['customer_ref'], {})
        customer_id = str(private.get('customer_id') or '')
        customer = customers.get(customer_id, {})
        base = {
            **r,
            'customer_id': customer_id,
            'source_customer_id': str(private.get('source_customer_id') or ''),
            'email': customer.get('email') or '',
            'phone': customer.get('phone') or '',
            'first_name': customer.get('first_name') or '',
            'full_name': customer.get('full_name') or '',
            'live_accepts_marketing': customer.get('accepts_marketing'),
            'stock_status': (st or {}).get('status') or 'unmapped',
            'available_estimated_total': (st or {}).get('available_estimated_total'),
        }
        if st and st.get('status') == 'available' and (st.get('available_estimated_total') or 0) > 0:
            ready_rows.append(base)
        else:
            blocked_rows.append(base)

    # Assign channels. No send/list creation; these are final preview/import files only.
    all_queue = []
    klaviyo = []
    whatsapp = []
    seen_kl = set()
    seen_wa = set()

    for r in ready_rows:
        group_key = f"{r['segment']} | {r['anchor_product']}"
        g = groups.get(group_key, {})
        # Channel policy: VIP w/phone => WhatsApp concierge first. Email fallback/limited allowed.
        if r['segment'] == 'Champions/VIP' and r.get('phone'):
            channel = 'whatsapp_concierge'
        elif r.get('email'):
            channel = 'klaviyo_preview'
        elif r.get('phone'):
            channel = 'whatsapp_concierge'
        else:
            channel = 'hold_no_contact'
        angle, preview = copy_for(r['segment'], r['anchor_product'], channel)
        enriched = {
            'channel': channel,
            'customer_id': r['customer_id'],
            'source_customer_id': r['source_customer_id'],
            'customer_ref': r['customer_ref'],
            'email': r.get('email') or '',
            'phone': r.get('phone') or '',
            'first_name': r.get('first_name') or '',
            'full_name': r.get('full_name') or '',
            'segment': r['segment'],
            'anchor_product': r['anchor_product'],
            'anchor_size': r['anchor_size'],
            'anchor_sku': r['anchor_sku'],
            'stock_status': r['stock_status'],
            'available_estimated_total': r['available_estimated_total'],
            'monetary_value': r['monetary_value'],
            'frequency_orders': r['frequency_orders'],
            'recency_days': r['recency_days'],
            'recommended_channel_action': g.get('recommended_channel_action') or '',
            'copy_angle': angle,
            'copy_preview_internal': preview,
            'approval_status': 'PREVIEW_ONLY_NOT_SENT',
        }
        all_queue.append(enriched)
        if channel == 'klaviyo_preview' and enriched['email'] and enriched['email'] not in seen_kl:
            klaviyo.append(enriched); seen_kl.add(enriched['email'])
        if channel == 'whatsapp_concierge' and enriched['phone'] and enriched['phone'] not in seen_wa:
            whatsapp.append(enriched); seen_wa.add(enriched['phone'])

    fieldnames = ['channel','customer_id','source_customer_id','customer_ref','email','phone','first_name','full_name','segment','anchor_product','anchor_size','anchor_sku','stock_status','available_estimated_total','monetary_value','frequency_orders','recency_days','recommended_channel_action','copy_angle','copy_preview_internal','approval_status']
    for path, rows in [(PRIVATE_ALL, all_queue), (PRIVATE_KL, klaviyo), (PRIVATE_WA, whatsapp)]:
        with path.open('w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader(); w.writerows(rows)
        path.chmod(0o600)

    # Anonymized metrics for Brain report.
    by_channel = Counter(r['channel'] for r in all_queue)
    by_segment = Counter(r['segment'] for r in all_queue)
    by_group = Counter(f"{r['segment']} | {r['anchor_product']}" for r in all_queue)
    by_product = Counter(r['anchor_product'] for r in all_queue)
    copy_groups = []
    for (segment, product, channel), rows in defaultdict(list).items():
        pass
    copy_preview_map = {}
    for r in all_queue:
        key = (r['segment'], r['anchor_product'], r['channel'])
        copy_preview_map.setdefault(key, {'segment': r['segment'], 'anchor_product': r['anchor_product'], 'channel': r['channel'], 'count': 0, 'copy_angle': r['copy_angle'], 'copy_preview_internal': r['copy_preview_internal']})
        copy_preview_map[key]['count'] += 1
    copy_previews = sorted(copy_preview_map.values(), key=lambda x: (-x['count'], x['segment'], x['anchor_product']))

    summary = {
        'generated_at': now,
        'scope': 'Preview-only final P1 channel queues. No send, no external list creation.',
        'private_exports': {
            'all_ready_channel_queue': str(PRIVATE_ALL),
            'klaviyo_ready': str(PRIVATE_KL),
            'whatsapp_concierge_ready': str(PRIVATE_WA),
        },
        'counts': {
            'p1_candidates_total': len(p1),
            'ready_same_size_stock': len(ready_rows),
            'blocked_stock_or_mapping': len(blocked_rows),
            'all_queue_rows': len(all_queue),
            'klaviyo_unique_emails': len(klaviyo),
            'whatsapp_unique_phones': len(whatsapp),
        },
        'by_channel': dict(by_channel),
        'by_segment': dict(by_segment),
        'top_groups': dict(by_group.most_common(20)),
        'top_products': dict(by_product.most_common(20)),
        'copy_previews': copy_previews,
        'guardrails': [
            'No Klaviyo list created',
            'No WhatsApp/Evolution send',
            'No customer-facing action',
            'Private files chmod 600 under private_exports only',
            'Brain report contains no raw emails/phones/names',
        ],
    }
    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')

    lines = [
        '# LK Phase 5 P1 — listas finais por canal (preview, sem envio) — 2026-05-11', '',
        '## Veredito', '',
        'Listas finais P1 foram geradas em arquivos privados para operação/preview. Nenhum envio, lista externa, tag, campanha ou automação foi executado.', '',
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
    lines += ['', '## Top grupos prontos', '']
    for k, v in by_group.most_common(10):
        lines.append(f'- {k}: {v}')
    lines += ['', '## Previews de copy por grupo/canal', '']
    for c in copy_previews[:12]:
        lines += [
            f"### {c['segment']} | {c['anchor_product']} | {c['channel']} ({c['count']})",
            f"- Ângulo: {c['copy_angle']}",
            f"- Preview interno: {c['copy_preview_internal']}",
            '',
        ]
    lines += [
        '## Arquivos privados gerados', '',
        f'- `{PRIVATE_ALL}`',
        f'- `{PRIVATE_KL}`',
        f'- `{PRIVATE_WA}`',
        '',
        '## Guardrails', '',
    ]
    for g in summary['guardrails']:
        lines.append(f'- {g}')
    OUT_MD.write_text('\n'.join(lines) + '\n')
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
