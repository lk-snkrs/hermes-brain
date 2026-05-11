#!/usr/bin/env python3
"""Broad Tiny discovery for LK Phase 5 P1 held rows.

Purpose: rescue held P1 rows by searching Tiny directly for same-size available
curation candidates, beyond the first Shopify snapshot matrix.

Read-only. No PII. No external sends. No writes.
"""
from __future__ import annotations

import json
import pathlib
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))

from lk_phase5_p1_recipients_tiny_stock_20260511 import (  # noqa: E402
    load_secrets,
    norm_size,
    size_from_tiny_variant,
    stock_for_product_id,
    tiny_call,
)

GATE_JSON = ROOT / 'reports/lk-phase5-p1-post-tiny-action-gate-2026-05-11.json'
OUT_JSON = ROOT / 'reports/lk-phase5-p1-tiny-broad-curation-discovery-2026-05-11.json'
OUT_MD = ROOT / 'reports/lk-phase5-p1-tiny-broad-curation-discovery-2026-05-11.md'


def search_terms_for(product: str) -> list[str]:
    if 'New Balance 204L' in product:
        return ['New Balance 204L', 'Adidas Taekwondo', 'Alo Yoga ALO Runner']
    if 'Onitsuka Tiger Mexico 66' in product:
        return ['Onitsuka Tiger Mexico 66', 'Onitsuka Tiger Mexico', 'Adidas Taekwondo']
    if 'Jacquemus' in product or 'Moon Shoe' in product:
        return ['Nike Moon Shoe SP Jacquemus', 'Jacquemus', 'Nike x Jacquemus']
    if 'Samba' in product:
        return ['Adidas Samba', 'Adidas Taekwondo']
    return [product]


SEARCH_CACHE: dict[str, list[dict]] = {}
PRODUCT_CACHE: dict[str, dict] = {}
STOCK_CACHE: dict[str, dict] = {}


def tiny_product_candidates(tiny_token: str, query: str) -> list[dict]:
    if query in SEARCH_CACHE:
        return SEARCH_CACHE[query]
    ret = tiny_call(tiny_token, 'produtos.pesquisa', {'pesquisa': query}).get('retorno', {})
    out = []
    for wrap in ret.get('produtos') or []:
        p = wrap.get('produto') or {}
        if p.get('id'):
            out.append({k: p.get(k) for k in ['id', 'nome', 'codigo', 'situacao', 'preco']})
    SEARCH_CACHE[query] = out
    return out


def tiny_product_detail(tiny_token: str, product_id: str) -> dict:
    if product_id not in PRODUCT_CACHE:
        PRODUCT_CACHE[product_id] = tiny_call(tiny_token, 'produto.obter', {'id': product_id}).get('retorno', {}).get('produto') or {}
    return PRODUCT_CACHE[product_id]


def tiny_stock(tiny_token: str, product_id: str) -> dict:
    if product_id not in STOCK_CACHE:
        STOCK_CACHE[product_id] = stock_for_product_id(tiny_token, product_id)
    return STOCK_CACHE[product_id]


def discover_for_group(tiny_token: str, purchase_product: str, size: str) -> dict:
    target = norm_size(size)
    seen_products: set[str] = set()
    seen_variants: set[str] = set()
    available = []
    checked_products = 0
    checked_variants = 0
    query_counts = {}

    for term in search_terms_for(purchase_product):
        products = tiny_product_candidates(tiny_token, term)
        query_counts[term] = len(products)
        for p in products[:18]:
            pid = str(p.get('id') or '')
            if not pid or pid in seen_products:
                continue
            seen_products.add(pid)
            checked_products += 1
            prod = tiny_product_detail(tiny_token, pid)
            variants = prod.get('variacoes') or []
            if not variants:
                variants = [{'variacao': prod}]
            for wrap in variants:
                v = wrap.get('variacao') or {}
                vid = str(v.get('id') or pid)
                if not vid or vid in seen_variants:
                    continue
                checked_variants += 1
                vsize = size_from_tiny_variant(v)
                if norm_size(vsize) != target:
                    continue
                seen_variants.add(vid)
                st = tiny_stock(tiny_token, vid)
                qty = float(st.get('saldo_disponivel_estimado') or 0)
                if qty > 0:
                    available.append({
                        'tiny_id': st.get('tiny_id'),
                        'title': st.get('nome') or prod.get('nome') or p.get('nome'),
                        'size': vsize,
                        'sku': st.get('codigo') or v.get('codigo') or p.get('codigo'),
                        'available_estimated_total': qty,
                        'situacao': st.get('situacao'),
                        'match_source': f'tiny_broad_search:{term}',
                    })
    available.sort(key=lambda x: (-float(x.get('available_estimated_total') or 0), str(x.get('title') or '')))
    return {
        'purchase_product': purchase_product,
        'purchase_size': size,
        'search_terms': search_terms_for(purchase_product),
        'query_counts': query_counts,
        'checked_products': checked_products,
        'checked_variants': checked_variants,
        'available_candidate_count': len(available),
        'available_candidates': available[:12],
        'status': 'TINY_BROAD_CANDIDATES_FOUND' if available else 'NO_BROAD_TINY_CANDIDATE_FOUND',
    }


def main() -> None:
    gate = json.loads(GATE_JSON.read_text())
    hold_rows = [r for r in gate['decisions'] if r['decision'] == 'HOLD_NO_TINY_VALIDATED_RECOMMENDATION']
    groups: dict[tuple[str, str], int] = defaultdict(int)
    for r in hold_rows:
        groups[(r['purchase_product'], r['purchase_size'])] += 1

    secrets = load_secrets()
    tiny_token = secrets['TINY_API_TOKEN']
    discoveries = []
    for (product, size), count in sorted(groups.items(), key=lambda x: (-x[1], x[0][0], x[0][1])):
        d = discover_for_group(tiny_token, product, size)
        d['held_row_count'] = count
        discoveries.append(d)

    status_counts = Counter(d['status'] for d in discoveries)
    total_available = sum(d['available_candidate_count'] for d in discoveries)
    summary = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'Read-only broad Tiny discovery for P1 held rows. No PII, no sends, no writes.',
        'counts': {
            'held_rows_considered': len(hold_rows),
            'unique_product_size_groups_considered': len(discoveries),
            'groups_with_broad_tiny_candidates': status_counts['TINY_BROAD_CANDIDATES_FOUND'],
            'groups_without_broad_tiny_candidates': status_counts['NO_BROAD_TINY_CANDIDATE_FOUND'],
            'available_candidate_rows_found': total_available,
        },
        'discoveries': discoveries,
        'recommendation': 'Usar estes achados só como nova camada de curadoria interna. Antes de qualquer campanha, revisar manualmente se o produto conversa com a compra original e gerar copy final sem envio automático.',
        'guardrails': [
            'Busca e checagem de estoque Tiny apenas read-only',
            'Nenhum envio WhatsApp, Klaviyo ou e-mail',
            'Nenhum write em Shopify, Tiny ou Supabase',
            'Nenhum PII nos outputs',
        ],
    }
    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')

    lines = [
        '# LK Phase 5 P1, descoberta ampla Tiny para curadoria, 2026-05-11',
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
    lines += ['', '## Achados por produto comprado e tamanho', '']
    for d in discoveries:
        lines += [
            f"### {d['purchase_product']} | tamanho {d['purchase_size']} | {d['held_row_count']} linha(s) em hold",
            f"- Status: {d['status']}",
            f"- Termos buscados: {', '.join(d['search_terms'])}",
            f"- Produtos Tiny checados: {d['checked_products']}",
            f"- Variações Tiny checadas: {d['checked_variants']}",
            f"- Candidatos disponíveis: {d['available_candidate_count']}",
        ]
        if d['available_candidates']:
            for idx, c in enumerate(d['available_candidates'][:8], 1):
                lines.append(
                    f"  {idx}. {c['title']} | tamanho {c['size']} | SKU {c['sku']} | disp. estimada {c['available_estimated_total']} | {c['match_source']}"
                )
        else:
            lines.append('- Sem candidato disponível no Tiny por busca ampla. Próximo caminho: sourcing sob demanda ou revisão de família de estilo.')
        lines.append('')
    lines += ['## Guardrails', '']
    for g in summary['guardrails']:
        lines.append(f'- {g}')
    OUT_MD.write_text('\n'.join(lines) + '\n')

    print(json.dumps(summary['counts'], ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
