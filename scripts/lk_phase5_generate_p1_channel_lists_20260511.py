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


def _short_product(product: str) -> str:
    return (product or '').replace('Tênis ', '').strip()


def copy_for(segment: str, recommended_product: str, channel: str, purchase_product: str) -> tuple[str, str]:
    # Internal preview only. Final copy should be reviewed before any send.
    product_short = _short_product(recommended_product)
    purchase_short = _short_product(purchase_product)
    same_product = purchase_short and purchase_short == product_short
    if channel == 'whatsapp_concierge':
        if same_product:
            return (
                'Loja física / concierge direto / mesmo perfil',
                f'Oi {{first_name}}, tudo bem? Vi que você comprou na LK Flagship o {purchase_short}. Separei uma curadoria pequena no mesmo caminho, peças que conversam com esse estilo, mais pela leitura de moda do que por “mais um sneaker”. Posso te mandar 2 ou 3 opções bem pontuais?',
            )
        return (
            'Loja física / concierge direto / curadoria por compra',
            f'Oi {{first_name}}, tudo bem? Vi que você comprou na LK Flagship o {purchase_short}. Pela leitura da sua escolha, separei {product_short} como uma opção que conversa com esse estilo sem ficar óbvia. Posso te mandar essa e mais algumas alternativas no mesmo clima?',
        )
    if same_product:
        return (
            'Loja física / recompra por perfil / sem massificar',
            f'Você comprou na LK Flagship o {purchase_short}. Fizemos uma leitura de estilo a partir dessa escolha e separamos uma curadoria curta, com peças que mantêm a mesma intenção de moda e disponibilidade real no seu tamanho.',
        )
    if segment == 'Champions/VIP':
        return (
            'Loja física / VIP limitado / sem desconto',
            f'Você comprou na LK Flagship o {purchase_short}. Pela mesma leitura de estilo, separamos {product_short} em tamanho compatível, uma indicação mais consultiva, pensada para continuar o guarda-roupa e não só repetir categoria.',
        )
    if segment == 'Novo alto potencial':
        return (
            'Loja física / segunda compra / curadoria direta',
            f'Depois da sua escolha na LK Flagship, {purchase_short}, separamos {product_short} como continuidade natural desse estilo: uma recomendação de moda, com estoque real no seu tamanho, sem cara de disparo genérico.',
        )
    return (
        'Loja física / recompra por afinidade',
        f'Seleção LK baseada na sua compra presencial de {purchase_short}: {product_short}, com curadoria de moda e disponibilidade real no seu tamanho.',
    )


def is_physical_store_order(order: dict) -> bool:
    tags = order.get('tags') or ''
    return order.get('source_name') == 'pos' or 'Point of Sale' in tags or 'LKFLAGSHIP' in tags


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

    store_context_by_key = {}
    for r in p1:
        private = id_by_ref.get(r['customer_ref'], {})
        customer_id = str(private.get('customer_id') or '')
        if not customer_id:
            continue
        matches = [dict(x) for x in conn.execute(
            """
            SELECT o.order_number,o.order_created_at,o.source_name,o.tags,oi.title,oi.variant_title,oi.sku
            FROM lk_orders o
            JOIN lk_order_items oi ON oi.order_id=o.order_id
            WHERE o.customer_id=?
              AND oi.title=?
              AND COALESCE(oi.variant_title,'')=COALESCE(?,'')
              AND COALESCE(oi.sku,'')=COALESCE(?,'')
            ORDER BY o.order_created_at DESC
            """,
            (customer_id, r['anchor_product'], str(r.get('anchor_size') or ''), r.get('anchor_sku') or ''),
        )]
        store_matches = [m for m in matches if is_physical_store_order(m)]
        if store_matches:
            key = (r['customer_ref'], r['segment'], r['anchor_product'])
            store_context_by_key[key] = store_matches[0]
    conn.close()

    ready_rows = []
    blocked_rows = []
    store_excluded_rows = []
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
            store_context = store_context_by_key.get((r['customer_ref'], r['segment'], r['anchor_product']))
            if store_context:
                base.update({
                    'store_purchase_order_number': store_context.get('order_number') or '',
                    'store_purchase_at': store_context.get('order_created_at') or '',
                    'store_purchase_product': store_context.get('title') or r['anchor_product'],
                    'store_purchase_size': store_context.get('variant_title') or r['anchor_size'],
                    'store_purchase_sku': store_context.get('sku') or r['anchor_sku'],
                    'store_purchase_source_name': store_context.get('source_name') or '',
                })
                ready_rows.append(base)
            else:
                base['stock_status'] = 'available_but_not_physical_store_anchor_purchase'
                store_excluded_rows.append(base)
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
        angle, preview = copy_for(r['segment'], r['anchor_product'], channel, r.get('store_purchase_product') or r['anchor_product'])
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
            'store_purchase_product': r.get('store_purchase_product') or '',
            'store_purchase_size': r.get('store_purchase_size') or '',
            'store_purchase_sku': r.get('store_purchase_sku') or '',
            'store_purchase_at': r.get('store_purchase_at') or '',
            'store_purchase_source_name': r.get('store_purchase_source_name') or '',
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

    fieldnames = ['channel','customer_id','source_customer_id','customer_ref','email','phone','first_name','full_name','segment','store_purchase_product','store_purchase_size','store_purchase_sku','store_purchase_at','store_purchase_source_name','anchor_product','anchor_size','anchor_sku','stock_status','available_estimated_total','monetary_value','frequency_orders','recency_days','recommended_channel_action','copy_angle','copy_preview_internal','approval_status']
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
        'scope': 'Preview-only final P1 channel queues. Physical-store anchor purchases only. No send, no external list creation.',
        'private_exports': {
            'all_ready_channel_queue': str(PRIVATE_ALL),
            'klaviyo_ready': str(PRIVATE_KL),
            'whatsapp_concierge_ready': str(PRIVATE_WA),
        },
        'counts': {
            'p1_candidates_total': len(p1),
            'ready_same_size_stock_before_store_filter': len(ready_rows) + len(store_excluded_rows),
            'ready_physical_store_anchor_purchase': len(ready_rows),
            'excluded_online_or_non_store_anchor_purchase': len(store_excluded_rows),
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
            'No online/web anchor purchases included in this physical-store action',
            'No Klaviyo list created',
            'No WhatsApp/Evolution send',
            'No customer-facing action',
            'Private files chmod 600 under private_exports only',
            'Brain report contains no raw emails/phones/names',
        ],
    }
    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')

    lines = [
        '# LK Phase 5 P1, listas finais por canal (preview, sem envio), 2026-05-11', '',
        '## Veredito', '',
        'Listas P1 revisadas para a regra aprovada por Lucas: somente clientes cuja compra-âncora foi na loja física/LK Flagship. Nenhum envio, lista externa, tag, campanha ou automação foi executado.', '',
        '## Regra comercial aplicada', '',
        '- Entram: compras-âncora com `source_name=pos`, tag `Point of Sale` ou `LKFLAGSHIP`.',
        '- Saem: compras online/web/draft mesmo quando havia estoque no tamanho.',
        '- Copy revisada: mais direta, citando a compra presencial e oferecendo curadoria/opções relacionadas.', '',
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
