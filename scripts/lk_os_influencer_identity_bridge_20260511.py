#!/usr/bin/env python3
"""LK OS influencer identity bridge, read-only.

Builds an operational queue for Phase 3 Paid & Influencer Intelligence: handles,
coupons, ad naming patterns, Shopify bridge evidence and stock consequence. It
uses only versioned Brain reports and does not call Meta/Shopify/Tiny or create
campaign/coupon/send/write anything.
"""
from __future__ import annotations

import json
import pathlib
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
DICT_MD = ROOT / 'areas/lk/sub-areas/trafego-pago/contexto/campaign-attribution-dictionary-v0.2.md'
MATRIX_JSON = ROOT / 'reports/lk-influencer-sku-stock-matrix-readonly-2026-05-10.json'
META_JSON = ROOT / 'reports/lk-meta-campaign-title-roas-readonly-2026-05-10.json'
OUT_JSON = ROOT / 'reports/lk-os-influencer-identity-bridge-2026-05-11.json'
OUT_MD = ROOT / 'reports/lk-os-influencer-identity-bridge-2026-05-11.md'
BRAIN_DOC = ROOT / 'areas/lk/sub-areas/trafego-pago/rotinas/influencer-identity-bridge-readonly-2026-05-11.md'

INFLUENCERS = ['Silvia Heinz', 'Helena Lunardelli', 'Lala Noleto']
STATUS_BY_CONFIDENCE = {
    'high': 'validated_needs_official_handle_coupon_registry',
    'medium': 'mapped_needs_official_registry_and_ad_id_bridge',
    'low': 'investigation_required_before_operational_use',
}


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def brl(v: float | int | None) -> str:
    if v is None:
        return 'n/d'
    return 'R$ ' + f'{float(v):,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


def slug(name: str) -> str:
    return re.sub(r'[^a-z0-9]+', '_', name.lower()).strip('_')


def parse_dictionary_sections(text: str) -> dict[str, dict[str, Any]]:
    sections: dict[str, dict[str, Any]] = {}
    for name in INFLUENCERS:
        s = slug(name)
        m = re.search(rf'## {re.escape(s)}_v02\n(?P<body>.*?)(?=\n## |\Z)', text, re.S)
        body = m.group('body') if m else ''
        status = re.search(r'- status: `([^`]+)`', body)
        handle = re.search(r'- influencer_handle: (.+)', body)
        meta = re.search(r'- Meta platform signal: spend R\$ ([^;]+); compras Meta ([^;]+); valor Meta R\$ ([^;]+); ROAS plataforma ([^\n]+)', body)
        patterns = re.findall(r'- campaign: `([^`]+)` \| adset: `([^`]+)` \| ad: `([^`]+)`', body)
        sections[name] = {
            'dictionary_status_v02': status.group(1) if status else 'unknown',
            'influencer_handle_current': handle.group(1).strip() if handle else '[a confirmar]',
            'meta_platform_signal_text': meta.group(0).lstrip('- ') if meta else None,
            'known_ad_patterns': [
                {'campaign_name_pattern': c, 'adset_name_pattern': a, 'ad_name_pattern': ad}
                for c, a, ad in patterns
            ],
        }
    return sections


def summarize_matrix(matrix: dict[str, Any]) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    results = matrix.get('results') or {}
    matched_orders = matrix.get('matched_orders') or {}
    for name in INFLUENCERS:
        rows = results.get(name) or []
        risk_counts: Counter[str] = Counter()
        evidence_counts: Counter[str] = Counter()
        total_qty = 0
        total_revenue = 0.0
        sku_rows = 0
        top_rows = []
        for r in rows:
            risk_counts[str(r.get('risk') or 'unknown')] += 1
            for k, v in (r.get('evidence') or {}).items():
                evidence_counts[k] += int(v or 0)
            total_qty += int(r.get('qty') or 0)
            total_revenue += float(r.get('revenue') or 0)
            if r.get('sku') and r.get('sku') != '[sem SKU no Shopify]':
                sku_rows += 1
            top_rows.append({
                'product': r.get('name'),
                'sku': r.get('sku'),
                'size_or_variant': r.get('variant'),
                'qty': r.get('qty'),
                'revenue_fact_shopify': r.get('revenue'),
                'stock_risk_fact_tiny_stock': r.get('risk'),
                'evidence_types': sorted((r.get('evidence') or {}).keys()),
            })
        top_rows.sort(key=lambda x: float(x.get('revenue_fact_shopify') or 0), reverse=True)
        out[name] = {
            'matched_orders_fact_shopify': int(matched_orders.get(name) or 0),
            'line_rows': len(rows),
            'rows_with_sku': sku_rows,
            'qty_fact_shopify': total_qty,
            'revenue_fact_shopify': round(total_revenue, 2),
            'risk_counts': dict(risk_counts),
            'evidence_counts': dict(evidence_counts),
            'top_rows': top_rows[:8],
        }
    return out


def campaign_summary(meta: dict[str, Any]) -> dict[str, Any]:
    campaigns = meta.get('campaigns') or []
    return {
        'period': meta.get('period'),
        'meta_campaign_count': meta.get('meta_campaign_count'),
        'meta_spend_total_campaigns_platform_signal': meta.get('meta_spend_total_campaigns'),
        'meta_value_total_campaigns_platform_signal': meta.get('meta_value_total_campaigns'),
        'shopify_web_orders_fact_shopify': meta.get('shopify_web_orders'),
        'shopify_web_revenue_fact_shopify': meta.get('shopify_web_revenue'),
        'campaigns_with_shopify_utm_orders': sum(1 for c in campaigns if (c.get('shopify_utm_orders') or 0) > 0),
        'campaigns': [
            {
                'campaign_id': c.get('campaign_id'),
                'campaign_name': c.get('campaign_name'),
                'family': c.get('family'),
                'spend_platform_signal': c.get('spend'),
                'value_meta_platform_signal': c.get('value_meta'),
                'roas_meta_attributed_platform_signal': c.get('roas_meta_attributed'),
                'shopify_utm_orders_fact_shopify': c.get('shopify_utm_orders'),
                'shopify_utm_revenue_fact_shopify': c.get('shopify_utm_revenue'),
            }
            for c in campaigns
        ],
    }


def confidence_for(name: str, mat: dict[str, Any], dictionary_status: str) -> str:
    if mat['matched_orders_fact_shopify'] >= 20 and mat['revenue_fact_shopify'] > 100000:
        return 'high'
    if mat['matched_orders_fact_shopify'] > 0 or dictionary_status.startswith('validated'):
        return 'medium'
    return 'low'


def build_rows(sections: dict[str, Any], matrix_summary: dict[str, Any]) -> list[dict[str, Any]]:
    rows = []
    for name in INFLUENCERS:
        sec = sections.get(name) or {}
        mat = matrix_summary.get(name) or {}
        conf = confidence_for(name, mat, sec.get('dictionary_status_v02', 'unknown'))
        evidence_counts = mat.get('evidence_counts') or {}
        missing = []
        if (sec.get('influencer_handle_current') or '').strip() == '[a confirmar]':
            missing.append('official_influencer_handle')
        missing.append('official_coupon_codes_or_confirmed_no_coupon')
        missing.append('ad_id_or_utm_content_per_creative')
        if conf == 'low':
            missing.append('shopify_bridge_evidence')
        rows.append({
            'identity_bridge_id': f'LK-INFLUENCER-{slug(name).upper()}-20260511',
            'influencer_name': name,
            'current_status': STATUS_BY_CONFIDENCE[conf],
            'confidence': conf,
            'dictionary_status_v02': sec.get('dictionary_status_v02', 'unknown'),
            'official_handle_status': 'missing_pending_lucas_or_agency_confirmation',
            'official_coupon_status': 'missing_pending_lucas_or_agency_confirmation',
            'current_handle_value': sec.get('influencer_handle_current', '[a confirmar]'),
            'shopify_bridge_strength': 'strong' if conf == 'high' else ('partial' if conf == 'medium' else 'none_found_in_recorte'),
            'matched_orders_fact_shopify': mat.get('matched_orders_fact_shopify', 0),
            'revenue_fact_shopify': mat.get('revenue_fact_shopify', 0.0),
            'qty_fact_shopify': mat.get('qty_fact_shopify', 0),
            'risk_counts_fact_tiny_stock': mat.get('risk_counts', {}),
            'evidence_counts_fact_shopify': evidence_counts,
            'known_ad_patterns_platform_signal': sec.get('known_ad_patterns', []),
            'missing_fields_to_operationalize': missing,
            'safe_next_step': 'collect_official_handle_coupon_ad_id_registry_preview_only' if conf != 'low' else 'investigate_real_bridge_before_stock_campaign_decision',
            'blocked_until_confirmed': [
                'coupon_creation_or_edit',
                'campaign_naming_change',
                'budget_or_creative_change',
                'customer_send',
                'stock_or_purchase_action',
            ],
            'source_labels': ['fact_shopify', 'fact_tiny_stock', 'platform_signal', 'derived_reconciliation'],
            'top_product_sku_size_examples_sanitized': mat.get('top_rows', []),
        })
    return rows


def build_registry_template(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            'influencer_name': r['influencer_name'],
            'official_handle': None,
            'official_coupon_codes': [],
            'official_utm_content_patterns': [],
            'official_ad_ids': [],
            'approved_product_themes': [],
            'commercial_window_start': None,
            'commercial_window_end': None,
            'owner_to_confirm': 'Lucas/Pareto/LK',
            'status': 'pending_confirmation',
            'notes': 'Do not create coupons/campaigns from this template; fill only after human confirmation.',
        }
        for r in rows
    ]


def build_md(payload: dict[str, Any]) -> str:
    s = payload['summary']
    lines = [
        '# LK OS Influencer Identity Bridge, read-only',
        '',
        f"Generated at: `{payload['generated_at']}`",
        '',
        '## Veredito operacional',
        '',
        'O próximo bloco seguro da Fase 3 foi separar identidade oficial de influencer, cupom, handle, ad_id e UTM da evidência de plataforma. O relatório não cria cupom, não mexe em campanha e não transforma ROAS de Meta em venda operacional.',
        '',
        '## Resumo',
        '',
        f"- Influencers roteados: {s['influencer_rows']}",
        f"- Alta confiança Shopify/Tiny: {s['confidence_counts'].get('high', 0)}",
        f"- Média confiança: {s['confidence_counts'].get('medium', 0)}",
        f"- Baixa confiança/investigação: {s['confidence_counts'].get('low', 0)}",
        f"- Receita Shopify com ponte direta nas matrizes: {brl(s['revenue_fact_shopify_total'])}",
        f"- Pedidos Shopify casados: {s['matched_orders_fact_shopify_total']}",
        '',
        '## Fila de identidade e ponte',
        '',
    ]
    for row in payload['identity_bridge']:
        risks = ', '.join(f'{k}: {v}' for k, v in (row['risk_counts_fact_tiny_stock'] or {}).items()) or 'n/d'
        evidence = ', '.join(f'{k}: {v}' for k, v in (row['evidence_counts_fact_shopify'] or {}).items()) or 'n/d'
        missing = ', '.join(row['missing_fields_to_operationalize'])
        lines.extend([
            f"### {row['influencer_name']}",
            f"- Status: `{row['current_status']}`",
            f"- Confiança: `{row['confidence']}`",
            f"- Handle oficial: `{row['official_handle_status']}`",
            f"- Cupons oficiais: `{row['official_coupon_status']}`",
            f"- Pedidos Shopify casados: {row['matched_orders_fact_shopify']}",
            f"- Receita Shopify: {brl(row['revenue_fact_shopify'])}",
            f"- Evidência Shopify: {evidence}",
            f"- Consequência estoque/Tiny: {risks}",
            f"- Falta para operacionalizar: {missing}",
            f"- Próximo passo seguro: `{row['safe_next_step']}`",
            '',
        ])
    lines.extend([
        '## Template de cadastro oficial, preview-only',
        '',
        'Preencher depois com Lucas/Pareto/LK, sem criar cupom nem alterar campanha automaticamente:',
        '',
    ])
    for r in payload['official_registry_template_preview']:
        lines.extend([
            f"- {r['influencer_name']}: handle oficial, cupons oficiais, utm_content, ad_ids, temas de produto, janela comercial, owner e status.",
        ])
    lines.extend([
        '',
        '## O que não foi feito',
        '',
        '- Nenhuma chamada live a Meta, Shopify, Tiny, GA4, Metricool ou Klaviyo.',
        '- Nenhum cupom foi criado ou alterado.',
        '- Nenhuma campanha, anúncio, budget, UTM, criativo, tag, Shopify/Tiny, cliente, estoque, preço, banco de produção ou cron foi alterado.',
        '- Nenhum envio externo foi feito.',
        '',
        '## Próximo passo seguro',
        '',
        'Usar esta fila para Lucas/Pareto/LK preencher handles/cupons/ad_ids oficiais. Depois, gerar a ponte `ad_id/utm_content/cupom/landing/referrer/note/tag` com status validated/mapped/ambiguous/investigation, ainda sem mexer em mídia ou criar cupom.',
    ])
    return '\n'.join(lines) + '\n'


def main() -> None:
    dictionary_text = DICT_MD.read_text(encoding='utf-8')
    matrix = json.loads(MATRIX_JSON.read_text(encoding='utf-8'))
    meta = json.loads(META_JSON.read_text(encoding='utf-8'))
    sections = parse_dictionary_sections(dictionary_text)
    matrix_summary = summarize_matrix(matrix)
    rows = build_rows(sections, matrix_summary)
    confidence_counts = Counter(r['confidence'] for r in rows)
    payload = {
        'generated_at': now_utc(),
        'scope': 'LK OS Phase 3 influencer identity bridge, read-only',
        'read_only': True,
        'sources': {
            'dictionary_v02': str(DICT_MD.relative_to(ROOT)),
            'influencer_sku_stock_matrix': str(MATRIX_JSON.relative_to(ROOT)),
            'meta_campaign_title_roas': str(META_JSON.relative_to(ROOT)),
        },
        'summary': {
            'influencer_rows': len(rows),
            'confidence_counts': dict(confidence_counts),
            'matched_orders_fact_shopify_total': sum(int(r['matched_orders_fact_shopify'] or 0) for r in rows),
            'revenue_fact_shopify_total': round(sum(float(r['revenue_fact_shopify'] or 0) for r in rows), 2),
            'source_labels': ['fact_shopify', 'fact_tiny_stock', 'platform_signal', 'derived_reconciliation'],
        },
        'platform_campaign_context': campaign_summary(meta),
        'identity_bridge': rows,
        'official_registry_template_preview': build_registry_template(rows),
        'not_performed': [
            'live_meta_call', 'live_shopify_call', 'live_tiny_call', 'coupon_create_or_update',
            'campaign_or_budget_or_creative_change', 'utm_change', 'shopify_write', 'tiny_write',
            'klaviyo_or_whatsapp_or_email_send', 'stock_or_price_change', 'production_db_write', 'cron_creation'
        ],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    md = build_md(payload)
    OUT_MD.write_text(md, encoding='utf-8')
    BRAIN_DOC.write_text(md.replace('# LK OS Influencer Identity Bridge, read-only', '# LK OS, Influencer Identity Bridge read-only, 2026-05-11'), encoding='utf-8')
    print(json.dumps({'ok': True, 'rows': len(rows), 'json': str(OUT_JSON), 'md': str(OUT_MD), 'brain_doc': str(BRAIN_DOC)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
