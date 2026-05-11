#!/usr/bin/env python3
"""Prepare internal copy preview for LK Phase 5 P1 rows rescued by broad Tiny discovery.

No PII in Brain reports. Private operational CSV has customer_ref only, not raw name/email/phone.
No sends, no Klaviyo list, no external writes.
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
GATE = ROOT / 'reports/lk-phase5-p1-post-tiny-action-gate-2026-05-11.json'
DISCOVERY = ROOT / 'reports/lk-phase5-p1-tiny-broad-curation-discovery-2026-05-11.json'
PRIVATE_OUT = PRIVATE_DIR / 'lk_phase5_p1_broad_tiny_copy_preview_queue_2026-05-11.csv'
OUT_JSON = ROOT / 'reports/lk-phase5-p1-broad-tiny-copy-preview-2026-05-11.json'
OUT_MD = ROOT / 'reports/lk-phase5-p1-broad-tiny-copy-preview-2026-05-11.md'


def read_csv(path: pathlib.Path) -> list[dict]:
    with path.open(newline='') as f:
        return list(csv.DictReader(f))


def short_product(title: str) -> str:
    return (title or '').replace('Tênis ', '').replace('Tenis ', '').strip()


def copy_for(channel: str, purchase_product: str, candidate_title: str) -> tuple[str, str]:
    purchase = short_product(purchase_product)
    candidate = short_product(candidate_title)
    same = purchase == candidate or purchase in candidate
    if channel == 'whatsapp_concierge':
        if same:
            return (
                'loja física / continuidade do mesmo perfil / estoque Tiny validado',
                f'Oi {{first_name}}, tudo bem? Vi sua compra do {purchase} na LK Flagship. Temos uma unidade validada no Tiny em um caminho muito próximo dessa escolha. Se fizer sentido, separo para você ver com calma antes de abrir para lista maior.',
            )
        return (
            'loja física / curadoria por produto comprado / estoque Tiny validado',
            f'Oi {{first_name}}, tudo bem? A partir da sua compra do {purchase} na LK Flagship, separei o {candidate} no seu tamanho. Ele mantém a mesma leitura de estilo, mas muda o ponto de moda para não ficar repetitivo. Posso te mostrar?',
        )
    if same:
        return (
            'loja física / continuidade do mesmo perfil / e-mail preview',
            f'Depois da sua compra presencial do {purchase}, selecionamos uma opção validada no Tiny que mantém a mesma intenção de estilo e disponibilidade no seu tamanho.',
        )
    return (
        'loja física / recomendação por afinidade / e-mail preview',
        f'Com base na sua compra presencial do {purchase}, selecionamos {candidate}: uma continuidade de estilo com disponibilidade validada no Tiny para o seu tamanho.',
    )


def main() -> None:
    queue = read_csv(QUEUE)
    gate = json.loads(GATE.read_text())
    discovery = json.loads(DISCOVERY.read_text())

    held_refs = {r['customer_ref'] for r in gate['decisions'] if r['decision'] == 'HOLD_NO_TINY_VALIDATED_RECOMMENDATION'}
    best_candidate = {}
    for d in discovery['discoveries']:
        candidates = d.get('available_candidates') or []
        if candidates:
            key = (d['purchase_product'], str(d['purchase_size']))
            best_candidate[key] = candidates[0]

    rows = []
    allocated_by_sku = Counter()
    hold_over_capacity = []
    for r in queue:
        if r['customer_ref'] not in held_refs:
            continue
        key = (r.get('store_purchase_product') or r.get('anchor_product') or '', str(r.get('store_purchase_size') or r.get('anchor_size') or ''))
        candidate = best_candidate.get(key)
        if not candidate:
            continue
        sku = str(candidate['sku'])
        capacity = int(float(candidate.get('available_estimated_total') or 0))
        if allocated_by_sku[sku] >= capacity:
            hold_over_capacity.append({
                'customer_ref': r['customer_ref'],
                'channel': r['channel'],
                'segment': r['segment'],
                'purchase_product': key[0],
                'purchase_size': key[1],
                'recommended_product': candidate['title'],
                'recommended_size': candidate['size'],
                'recommended_sku': sku,
                'tiny_available_estimated_total': candidate['available_estimated_total'],
                'hold_reason': 'TINY_CAPACITY_ALREADY_ALLOCATED_IN_PREVIEW',
            })
            continue
        allocated_by_sku[sku] += 1
        angle, preview = copy_for(r['channel'], key[0], candidate['title'])
        rows.append({
            'customer_ref': r['customer_ref'],
            'channel': r['channel'],
            'segment': r['segment'],
            'purchase_product': key[0],
            'purchase_size': key[1],
            'recommended_product': candidate['title'],
            'recommended_size': candidate['size'],
            'recommended_sku': sku,
            'tiny_available_estimated_total': candidate['available_estimated_total'],
            'copy_angle': angle,
            'copy_preview_internal': preview,
            'approval_status': 'INTERNAL_PREVIEW_ONLY_NOT_SENT_CAPACITY_RESERVED_IN_PREVIEW',
        })

    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    PRIVATE_DIR.chmod(0o700)
    fieldnames = ['customer_ref', 'channel', 'segment', 'purchase_product', 'purchase_size', 'recommended_product', 'recommended_size', 'recommended_sku', 'tiny_available_estimated_total', 'copy_angle', 'copy_preview_internal', 'approval_status']
    with PRIVATE_OUT.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    PRIVATE_OUT.chmod(0o600)

    by_channel = Counter(r['channel'] for r in rows)
    by_segment = Counter(r['segment'] for r in rows)
    by_pair = Counter(f"{r['purchase_product']} | {r['purchase_size']} -> {r['recommended_product']} | {r['recommended_size']}" for r in rows)
    summary = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'Internal copy preview queue from broad Tiny discovery. No sends, no external writes, no PII in Brain report.',
        'private_preview_queue': str(PRIVATE_OUT),
        'counts': {
            'internal_preview_rows': len(rows),
            'held_over_capacity': len(hold_over_capacity),
            'channels': dict(by_channel),
            'segments': dict(by_segment),
        },
        'inventory_allocation_by_sku': dict(allocated_by_sku),
        'held_over_capacity': hold_over_capacity,
        'recommendation_pairs': dict(by_pair),
        'copy_previews': [
            {
                'channel': r['channel'],
                'segment': r['segment'],
                'purchase_product': r['purchase_product'],
                'purchase_size': r['purchase_size'],
                'recommended_product': r['recommended_product'],
                'recommended_size': r['recommended_size'],
                'recommended_sku': r['recommended_sku'],
                'tiny_available_estimated_total': r['tiny_available_estimated_total'],
                'copy_angle': r['copy_angle'],
                'copy_preview_internal': r['copy_preview_internal'],
            }
            for r in rows
        ],
        'guardrails': [
            'Preview interno apenas',
            'Nenhum envio WhatsApp, Klaviyo ou e-mail',
            'Nenhuma lista externa criada',
            'Nenhum write em Shopify, Tiny ou Supabase',
            'Relatório Brain sem PII',
        ],
    }
    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')

    lines = [
        '# LK Phase 5 P1, copy preview pós-descoberta Tiny ampla, 2026-05-11',
        '',
        '## Veredito',
        '',
        'Foram resgatadas poucas linhas com estoque Tiny real. Mantive tudo como preview interno, sem envio. O resultado já é mais seguro que usar snapshot Shopify sozinho, mas ainda pede revisão humana de curadoria antes de qualquer ação externa.',
        '',
        '## Contagens',
        '',
        f'- internal_preview_rows: {len(rows)}',
        f'- held_over_capacity: {len(hold_over_capacity)}',
    ]
    for channel, count in by_channel.items():
        lines.append(f'- canal {channel}: {count}')
    for segment, count in by_segment.items():
        lines.append(f'- segmento {segment}: {count}')
    lines += ['', '## Pares de recomendação', '']
    for pair, count in by_pair.items():
        lines.append(f'- {pair}: {count}')
    lines += ['', '## Previews internos de copy', '']
    for r in rows:
        lines += [
            f"### {r['channel']} | {r['segment']} | {r['purchase_product']} tamanho {r['purchase_size']}",
            f"- Recomendação: {r['recommended_product']} | tamanho {r['recommended_size']} | SKU {r['recommended_sku']} | Tiny disp. {r['tiny_available_estimated_total']}",
            f"- Ângulo: {r['copy_angle']}",
            f"- Preview interno: {r['copy_preview_internal']}",
            '',
        ]
    if hold_over_capacity:
        lines += ['## Linhas seguradas por capacidade Tiny', '']
        for h in hold_over_capacity:
            lines.append(f"- {h['purchase_product']} tamanho {h['purchase_size']} -> {h['recommended_product']} SKU {h['recommended_sku']}: segurado porque a capacidade Tiny já foi reservada neste preview")
        lines.append('')
    lines += ['## Guardrails', '']
    for g in summary['guardrails']:
        lines.append(f'- {g}')
    OUT_MD.write_text('\n'.join(lines) + '\n')

    print(json.dumps(summary['counts'], ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
