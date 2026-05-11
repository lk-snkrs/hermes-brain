#!/usr/bin/env python3
"""Build LK Phase 5 product-purchase to product-recommendation matrix.

Read-only, local-only.
Inputs:
- Local SQLite LK OS cache.
- Private P1 channel queue created previously.

Outputs:
- An anonymized Brain Markdown report.
- An anonymized JSON report.

No PII is written to Brain reports. No external sends or writes.
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
PRIVATE_QUEUE = pathlib.Path('/opt/data/hermes_bruno_ingest/private_exports/lk_crm/lk_phase5_p1_all_ready_channel_queue_2026-05-11.csv')
OUT_MD = ROOT / 'reports/lk-phase5-purchase-to-recommendation-matrix-2026-05-11.md'
OUT_JSON = ROOT / 'reports/lk-phase5-purchase-to-recommendation-matrix-2026-05-11.json'

RULES = [
    {
        'match_any': ['New Balance 204L Arid Timberwolf', 'New Balance 204L Mushroom Arid Stone'],
        'style_family': 'low-profile neutro, suede e tons terrosos',
        'search_terms': ['New Balance 204L Silver Metallic Flat Taupe', 'New Balance 204L Silver Metallic Sage Green', 'New Balance 204L Black Timberwolf', 'Adidas Taekwondo Cloud White', 'Adidas Taekwondo Core Black', 'Alo Yoga ALO Runner Espresso'],
        'basis': 'mantém a leitura minimalista e premium, mas muda textura ou acabamento para não parecer repetição literal',
    },
    {
        'match_any': ['Onitsuka Tiger Mexico 66 Kill Bill', 'Onitsuka Tiger Mexico 66 White Black'],
        'style_family': 'retro slim com presença gráfica',
        'search_terms': ['Onitsuka Tiger Mexico 66 Glitter Pack Black', 'Onitsuka Tiger Mexico 66 Glitter Pack Pure Silver', 'Onitsuka Tiger Mexico 66 Black/Dragon Fruit', 'Onitsuka Tiger Mexico 66 Sabot Cream Mustard', 'Adidas Taekwondo Caroline Hu x CLOT'],
        'basis': 'continua a silhueta baixa e fashion, com opção de brilho, contraste ou variação sabot',
    },
    {
        'match_any': ['Adidas Samba OG Crochet Pack'],
        'style_family': 'Samba artesanal, textura e verão urbano',
        'search_terms': ['Adidas Samba OG Off White Earth Strata', 'Adidas Samba LT Cream White Black Gum', 'Adidas Taekwondo Mei Ballet Branco', 'Adidas Taekwondo Mei Ballet Black Gum', 'Slyce Racquet Club Off White'],
        'basis': 'preserva a linguagem baixa e casual, abrindo caminho para Taekwondo ou apparel leve em tons claros',
    },
    {
        'match_any': ['Nike Moon Shoe SP Jacquemus'],
        'style_family': 'designer sneaker, Jacquemus e Nike com leitura de moda',
        'search_terms': ['Nike Moon Shoe SP Jacquemus Pale Pink', 'Nike Moon Shoe SP Jacquemus University Red', 'Nike Moon Shoe SP Jacquemus Off Noir', 'Nike Moon Shoe SP Jacquemus Off White', 'Bolsa Jacquemus Le Bambino', 'Bolsa Nike x Jacquemus Small Swoosh'],
        'basis': 'mantém o território Jacquemus e transforma a próxima abordagem em curadoria de styling, não só outro tênis',
    },
]


def load_queue() -> list[dict]:
    if not PRIVATE_QUEUE.exists():
        raise FileNotFoundError(f'Missing private queue: {PRIVATE_QUEUE}')
    with PRIVATE_QUEUE.open(newline='') as f:
        return list(csv.DictReader(f))


def matching_rule(product: str) -> dict:
    for rule in RULES:
        if any(token in product for token in rule['match_any']):
            return rule
    return {
        'match_any': [],
        'style_family': 'afinidade de marca, cor e silhueta',
        'search_terms': [],
        'basis': 'sem regra específica ainda, manter em revisão manual antes de qualquer ação',
    }


def candidate_products(conn: sqlite3.Connection, anchor_product: str, size: str, rule: dict) -> list[dict]:
    candidates: list[dict] = []
    seen = set()
    terms = rule.get('search_terms') or []
    for term in terms:
        for row in conn.execute(
            """
            SELECT
              p.title,
              p.vendor,
              p.product_type,
              p.handle,
              v.title AS variant_title,
              v.sku,
              v.price,
              v.inventory_quantity
            FROM lk_products p
            JOIN lk_product_variants v ON v.product_id = p.product_id
            WHERE p.status = 'active'
              AND p.title LIKE ?
              AND COALESCE(v.inventory_quantity, 0) > 0
              AND COALESCE(v.option1, v.title, '') = ?
              AND p.title <> ?
            ORDER BY v.inventory_quantity DESC, v.price ASC
            LIMIT 3
            """,
            (f'%{term}%', size, anchor_product),
        ):
            key = (row['title'], row['variant_title'], row['sku'])
            if key in seen:
                continue
            seen.add(key)
            candidates.append(dict(row))
    return candidates[:5]


def summarize() -> dict:
    rows = load_queue()
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    grouped: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for row in rows:
        product = row.get('store_purchase_product') or row.get('anchor_product') or ''
        size = row.get('store_purchase_size') or row.get('anchor_size') or ''
        grouped[(product, size)].append(row)

    groups = []
    no_candidate = []
    total_recipients = 0
    candidate_counter = Counter()
    for (purchase_product, size), recs in sorted(grouped.items(), key=lambda x: (-len(x[1]), x[0][0], x[0][1])):
        total_recipients += len(recs)
        rule = matching_rule(purchase_product)
        candidates = candidate_products(conn, purchase_product, size, rule)
        for c in candidates:
            candidate_counter[c['title']] += len(recs)
        item = {
            'purchase_product': purchase_product,
            'purchase_size': size,
            'recipient_count': len(recs),
            'style_family': rule['style_family'],
            'recommendation_basis': rule['basis'],
            'candidate_count': len(candidates),
            'candidates': candidates,
            'validation_status': 'SHOPIFY_SNAPSHOT_ONLY_REQUIRES_TINY_BEFORE_SEND' if candidates else 'NO_SIZE_MATCH_REQUIRES_MANUAL_CURATOR',
        }
        groups.append(item)
        if not candidates:
            no_candidate.append(item)

    conn.close()
    return {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'Internal product-purchase to product-recommendation matrix for LK Phase 5 P1. No PII, no send, no external write.',
        'input_queue': str(PRIVATE_QUEUE),
        'counts': {
            'ready_queue_rows_without_pii': len(rows),
            'unique_purchase_product_size_groups': len(groups),
            'groups_with_candidates': sum(1 for g in groups if g['candidate_count'] > 0),
            'groups_without_candidates': len(no_candidate),
            'recipient_rows_covered': total_recipients,
        },
        'top_candidate_products_by_covered_recipients': dict(candidate_counter.most_common(20)),
        'groups': groups,
        'guardrails': [
            'No Klaviyo list created',
            'No WhatsApp or Evolution send',
            'No Shopify, Tiny or Supabase write',
            'Candidate stock is from local Shopify snapshot only',
            'Tiny stock validation remains mandatory before any customer-facing action',
            'Brain outputs contain no names, emails or phones',
        ],
    }


def write_markdown(summary: dict) -> None:
    lines = [
        '# LK Phase 5, matriz Produto Comprado para Sugestão de Moda, 2026-05-11',
        '',
        '## Veredito',
        '',
        'Matriz interna criada para tirar a Fase 5 do genérico. A recomendação agora parte do produto comprado na loja física e busca opções por tamanho no snapshot local do Shopify. Ainda não é lista de envio, porque Tiny precisa validar estoque final antes de qualquer ação com cliente.',
        '',
        '## Contagens',
        '',
    ]
    for key, value in summary['counts'].items():
        lines.append(f'- {key}: {value}')
    lines += ['', '## Top candidatos por cobertura de clientes', '']
    for title, count in summary['top_candidate_products_by_covered_recipients'].items():
        lines.append(f'- {title}: cobre {count} linha(s) da fila por tamanho')
    lines += ['', '## Matriz por produto comprado e tamanho', '']
    for group in summary['groups']:
        lines += [
            f"### {group['purchase_product']} | tamanho {group['purchase_size']} | {group['recipient_count']} linha(s)",
            f"- Família de estilo: {group['style_family']}",
            f"- Base da recomendação: {group['recommendation_basis']}",
            f"- Status: {group['validation_status']}",
        ]
        if group['candidates']:
            lines.append('- Candidatos:')
            for idx, c in enumerate(group['candidates'], 1):
                price = c.get('price')
                price_txt = f"R$ {price:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.') if isinstance(price, (int, float)) else ''
                lines.append(
                    f"  {idx}. {c['title']} | tamanho {c['variant_title']} | SKU {c['sku']} | inv. snapshot {c['inventory_quantity']} | {price_txt}"
                )
        else:
            lines.append('- Candidatos: nenhum match em tamanho no snapshot local. Revisar manualmente ou buscar sourcing sob demanda.')
        lines.append('')
    lines += ['## Guardrails', '']
    for guardrail in summary['guardrails']:
        lines.append(f'- {guardrail}')
    OUT_MD.write_text('\n'.join(lines) + '\n')


def main() -> None:
    summary = summarize()
    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')
    write_markdown(summary)
    print(json.dumps(summary['counts'], ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
