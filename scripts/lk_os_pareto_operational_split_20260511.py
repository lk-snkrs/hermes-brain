#!/usr/bin/env python3
"""LK OS Pareto-compatible vs Lucas-operational split, read-only.

Materializes Phase 3's channel/influencer reporting boundary using already
versioned Brain artifacts. It does not call Meta, Shopify, GA4, Metricool,
Klaviyo or Tiny and does not change campaigns, budgets, coupons or sends.
"""
from __future__ import annotations

import json
import pathlib
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
PARETO_JSON = ROOT / 'reports/lk-pareto-april-2026/pareto-compatible-script-output.json'
IDENTITY_JSON = ROOT / 'reports/lk-os-influencer-identity-bridge-2026-05-11.json'
OUT_JSON = ROOT / 'reports/lk-os-pareto-operational-split-2026-05-11.json'
OUT_MD = ROOT / 'reports/lk-os-pareto-operational-split-2026-05-11.md'
BRAIN_DOC = ROOT / 'areas/lk/sub-areas/trafego-pago/rotinas/pareto-operational-split-readonly-2026-05-11.md'


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def brl(v: float | int | None) -> str:
    if v is None:
        return 'n/d'
    return 'R$ ' + f'{float(v):,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


def as_money(v: Any) -> float:
    try:
        return round(float(v or 0), 2)
    except Exception:
        return 0.0


def row_index(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {str(r.get('label')): r for r in rows}


def compact_row(row: dict[str, Any] | None) -> dict[str, Any] | None:
    if not row:
        return None
    return {
        'label': row.get('label'),
        'ads': row.get('ads'),
        'spend_platform_signal': as_money(row.get('spend')),
        'purchases_platform_signal': row.get('purchases'),
        'value_platform_signal': as_money(row.get('value')),
        'roas_platform_signal': row.get('roas'),
        'cpa_platform_signal': row.get('cpa'),
        'match_basis': 'Meta ad_name primary, adset/campaign fallback only if ad_name absent',
        'example_ad_ids_count': len(row.get('examples') or []),
    }


def identity_index(identity: dict[str, Any]) -> dict[str, dict[str, Any]]:
    idx = {}
    for row in identity.get('identity_bridge') or []:
        key = str(row.get('influencer_name') or '')
        idx[key] = row
        if key == 'Silvia Heinz':
            idx['Silvia'] = row
        if key == 'Helena Lunardelli':
            idx['Helena'] = row
    return idx


def classify_pair(label: str, pareto: dict[str, Any] | None, operational: dict[str, Any] | None, identity: dict[str, Any] | None) -> dict[str, Any]:
    pareto_c = compact_row(pareto)
    operational_c = compact_row(operational)
    if label in ('Maria', 'Maria Fernanda', 'Mariah'):
        grouping_rule = 'pareto_compatible_keep_separate_marias'
        lucas_rule = 'also_keep_separate_unless_lucas_explicitly_requests_family_rollup'
    elif identity:
        grouping_rule = 'pareto_compatible_name_as_reported'
        lucas_rule = 'lucas_operational_requires_shopify_tiny_bridge_before_stock_or_campaign_decision'
    else:
        grouping_rule = 'pareto_compatible_platform_row'
        lucas_rule = 'lucas_operational_platform_signal_only_until_bridge_exists'
    bridge_strength = None
    if identity:
        bridge_strength = identity.get('shopify_bridge_strength')
    elif label in ('Maria', 'Maria Fernanda', 'Mariah'):
        bridge_strength = 'not_evaluated_in_current_identity_bridge_keep_separate'
    else:
        bridge_strength = 'unknown_or_platform_signal_only'
    operational_allowed = bool(identity and identity.get('confidence') in ('high', 'medium'))
    if label == 'Lala Noleto':
        operational_allowed = False
    return {
        'label': label,
        'pareto_compatible': pareto_c,
        'lucas_operational': operational_c,
        'bridge_strength': bridge_strength,
        'identity_status': identity.get('current_status') if identity else 'not_in_identity_bridge',
        'source_labels': ['platform_signal'] + (['fact_shopify', 'fact_tiny_stock', 'derived_reconciliation'] if identity else []),
        'grouping_rule_pareto_compatible': grouping_rule,
        'grouping_rule_lucas_operational': lucas_rule,
        'operational_decision_allowed_now': operational_allowed,
        'operational_decision_limit': (
            'may_prepare internal product/stock analysis only, still no campaign/coupon/send/write without approval'
            if operational_allowed else
            'do not use for stock/campaign/budget decision until Shopify/Tiny bridge or official registry is confirmed'
        ),
    }


def build_payload() -> dict[str, Any]:
    pareto = json.loads(PARETO_JSON.read_text(encoding='utf-8'))
    identity = json.loads(IDENTITY_JSON.read_text(encoding='utf-8'))
    pidx = row_index(pareto.get('pareto_rows') or [])
    oidx = row_index(pareto.get('operational_rows') or [])
    iidx = identity_index(identity)
    # Use report-facing labels from Pareto/Lucas rows. Identity aliases enrich
    # short labels like `Silvia`/`Helena`, but should not create duplicate rows.
    labels = sorted(set(pidx) | set(oidx))
    # Avoid duplicate short/full names when both exist in historical outputs.
    if 'Silvia' in labels and 'Silvia Heinz' in labels:
        labels.remove('Silvia Heinz')
    if 'Helena' in labels and 'Helena Lunardelli' in labels:
        labels.remove('Helena Lunardelli')
    # Keep human-priority labels first.
    priority = ['Silvia', 'Helena', 'Lala Noleto', 'Maria', 'Maria Fernanda', 'Mariah']
    labels = [l for l in priority if l in labels] + [l for l in labels if l not in priority]
    rows = [classify_pair(label, pidx.get(label), oidx.get(label), iidx.get(label)) for label in labels]
    decision_counts = {
        'operational_decision_allowed_now': sum(1 for r in rows if r['operational_decision_allowed_now']),
        'platform_signal_or_investigation_only': sum(1 for r in rows if not r['operational_decision_allowed_now']),
        'pareto_rows': len(pidx),
        'lucas_operational_rows': len(oidx),
    }
    return {
        'generated_at': now_utc(),
        'scope': 'LK OS Phase 3 Pareto-compatible vs Lucas-operational split, read-only',
        'read_only': True,
        'sources': {
            'pareto_monthly_reconciliation': str(PARETO_JSON.relative_to(ROOT)),
            'identity_bridge': str(IDENTITY_JSON.relative_to(ROOT)),
        },
        'periods': {
            'pareto_month': pareto.get('month'),
            'pareto_period': pareto.get('period'),
            'identity_bridge_generated_at': identity.get('generated_at'),
        },
        'rules': {
            'pareto_compatible': [
                'Match influencer primarily by Meta ad_name using Maicon rule.',
                'Sum all ad_id rows under the same normalized influencer.',
                'Keep Maria, Maria Fernanda and Mariah separated.',
                'Numbers remain platform_signal and are compatible with Pareto/Meta dashboard language.',
            ],
            'lucas_operational': [
                'Do not decide product, stock, budget, coupon or creative from campaign/adset generic names.',
                'Require Shopify/Tiny bridge for product/SKU/size consequences.',
                'Silvia/Helena have usable bridge for internal analysis; Lala remains investigation in this recorte.',
                'Even when usable, execution still requires explicit approval for campaign/coupon/send/write.',
            ],
        },
        'summary': decision_counts,
        'global_platform_signal': compact_row(pareto.get('global')),
        'match_source_counts': pareto.get('meta_influencer_match_source_counts'),
        'split_rows': rows,
        'not_performed': [
            'live_meta_call', 'live_shopify_call', 'live_ga4_call', 'live_metricool_call', 'live_klaviyo_call',
            'campaign_change', 'budget_change', 'creative_change', 'coupon_create_or_update', 'utm_change',
            'shopify_write', 'tiny_write', 'customer_send', 'production_db_write', 'cron_creation'
        ],
    }


def build_md(payload: dict[str, Any]) -> str:
    s = payload['summary']
    lines = [
        '# LK OS Pareto-compatible vs Lucas-operational Split, read-only',
        '',
        f"Generated at: `{payload['generated_at']}`",
        '',
        '## Veredito operacional',
        '',
        'A Fase 3 agora tem a fronteira formal entre o que é compatível com Pareto/Meta e o que pode orientar decisão operacional de Lucas. Pareto-compatible mantém a linguagem de plataforma; Lucas-operational só avança quando há ponte Shopify/Tiny ou identidade confirmada.',
        '',
        '## Resumo',
        '',
        f"- Linhas Pareto-compatible: {s['pareto_rows']}",
        f"- Linhas Lucas-operational: {s['lucas_operational_rows']}",
        f"- Linhas que podem virar análise operacional interna agora: {s['operational_decision_allowed_now']}",
        f"- Linhas que seguem platform_signal/investigação: {s['platform_signal_or_investigation_only']}",
        '',
        '## Regras fixadas',
        '',
        '### Pareto-compatible',
        '',
    ]
    for rule in payload['rules']['pareto_compatible']:
        lines.append(f'- {rule}')
    lines.extend(['', '### Lucas-operational', ''])
    for rule in payload['rules']['lucas_operational']:
        lines.append(f'- {rule}')
    lines.extend(['', '## Linhas principais', ''])
    priority = {'Silvia', 'Helena', 'Lala Noleto', 'Maria', 'Maria Fernanda', 'Mariah'}
    for row in [r for r in payload['split_rows'] if r['label'] in priority]:
        p = row.get('pareto_compatible') or {}
        o = row.get('lucas_operational') or {}
        lines.extend([
            f"### {row['label']}",
            f"- Status identidade: `{row['identity_status']}`",
            f"- Bridge: `{row['bridge_strength']}`",
            f"- Pareto-compatible spend: {brl(p.get('spend_platform_signal')) if p else 'n/d'}; compras: {p.get('purchases_platform_signal', 'n/d') if p else 'n/d'}; valor: {brl(p.get('value_platform_signal')) if p else 'n/d'}",
            f"- Lucas-operational spend: {brl(o.get('spend_platform_signal')) if o else 'n/d'}; compras: {o.get('purchases_platform_signal', 'n/d') if o else 'n/d'}; valor: {brl(o.get('value_platform_signal')) if o else 'n/d'}",
            f"- Decisão operacional permitida agora: `{row['operational_decision_allowed_now']}`",
            f"- Limite: {row['operational_decision_limit']}",
            '',
        ])
    lines.extend([
        '## O que não foi feito',
        '',
        '- Nenhuma chamada live a Meta, Shopify, GA4, Metricool, Klaviyo ou Tiny.',
        '- Nenhuma campanha, orçamento, criativo, cupom, UTM, Shopify/Tiny, cliente, estoque, preço, banco de produção ou cron foi alterado.',
        '- Nenhum envio externo foi feito.',
        '',
        '## Próximo passo seguro',
        '',
        'Usar esta fronteira no e-mail semanal interno: uma seção Pareto-compatible para conferência de mídia e uma seção Lucas-operational para decisões que exigem ponte Shopify/Tiny. O e-mail deve ser preview-only até aprovação e sem jargão de dashboard.',
    ])
    return '\n'.join(lines) + '\n'


def main() -> None:
    payload = build_payload()
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    md = build_md(payload)
    OUT_MD.write_text(md, encoding='utf-8')
    BRAIN_DOC.write_text(md.replace('# LK OS Pareto-compatible vs Lucas-operational Split, read-only', '# LK OS, Pareto-compatible vs Lucas-operational Split read-only, 2026-05-11'), encoding='utf-8')
    print(json.dumps({'ok': True, 'rows': len(payload['split_rows']), 'json': str(OUT_JSON), 'md': str(OUT_MD), 'brain_doc': str(BRAIN_DOC)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
