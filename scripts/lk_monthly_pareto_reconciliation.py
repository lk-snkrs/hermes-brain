#!/usr/bin/env python3
"""LK monthly Pareto-compatible reconciliation.

Read-only workflow:
- Pulls Meta Ads insights at ad level for a closed month.
- Uses one canonical purchase/value key per ad.
- Produces a Pareto-compatible influencer grouping plus a Lucas-operational grouping.
- Keeps Maria, Maria Fernanda and Mariah separated in Pareto-compatible mode.

No campaign, Shopify, database or production writes.
"""
from __future__ import annotations

import argparse
import calendar
import datetime as dt
import html
import importlib.util
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

import requests

BASE = Path('/opt/data')
OUT_DIR = BASE / 'lk_monthly_pareto_reconciliation_reports'
WEEKLY_SCRIPT = BASE / 'hermes_bruno_ingest' / 'scripts' / 'lk_weekly_influencer_sales_report.py'
META_ACCOUNT_FALLBACK = 'act_1242062509867163'
CANONICAL_ACTIONS = ['offsite_conversion.fb_pixel_purchase', 'omni_purchase', 'purchase']

APRIL_2026_PARETO = {
    # Important: Pareto/PDF calls this Meta field "Receita", but it is the
    # Ads Manager conversion value / attributed value, not LK real net sales.
    'global': {'spend': 38954.76, 'purchases': 229.0, 'value': 797654.65, 'roas': 20.48, 'cpa': 170.11},
    'ecommerce': {'orders': 233, 'revenue': 722636.36, 'investment': 65436.52, 'roas': 11.04},
    # Pareto page 7 platform dashboards. These are NOT deduped channel sales.
    'platform_dashboards': {
        'meta_ads_manager': {'spend': 38954.76, 'purchases': 229.0, 'attributed_value': 797654.65, 'roas': 20.48, 'cpa': 170.11},
        'google_ads': {'spend': 26481.76, 'purchases': 795.58, 'attributed_value': 207240.45, 'roas': 7.83, 'cpa': 33.29},
    },
    # Pareto pages 12–13: use these for realistic traffic/channel revenue shares.
    'ga4_channels': {
        'Paid Social': {'revenue': 211329.00, 'conversion_rate': 0.07},
        'Organic Social': {'revenue': 157968.00, 'conversion_rate': 0.38},
        'Direct': {'revenue': 100760.00, 'conversion_rate': 0.27},
        'Cross-network': {'revenue': 58924.00, 'conversion_rate': 0.16},
        'Paid Search': {'revenue': 51137.00, 'conversion_rate': 0.46},
    },
    'ga4_source_medium': {
        'facebook / paid': {'sessions': 43799, 'revenue': 181859.02, 'conversion_rate': 0.11},
        'l.instagram.com / referral': {'sessions': 6198, 'revenue': 141618.15, 'conversion_rate': 0.63},
        'google / cpc': {'sessions': 26002, 'revenue': 130069.50, 'conversion_rate': 0.19},
        'direct / none': {'sessions': 12801, 'revenue': 100759.70, 'conversion_rate': 0.27},
        'google / organic': {'sessions': 17090, 'revenue': 33442.81, 'conversion_rate': 0.10},
    },
    'influencers': {
        'Ju Mesquita': {'ads': 9, 'spend': 2663.19, 'purchases': 20.0, 'value': 58595.44},
        'Arlindo': {'ads': 3, 'spend': 2071.87, 'purchases': 16.0, 'value': 75312.65},
        'Fiorela': {'ads': 9, 'spend': 1833.69, 'purchases': 12.0, 'value': 42691.50},
        'Maria': {'ads': 2, 'spend': 907.85, 'purchases': 2.0, 'value': 741.54},
    },
}

PARETO_PATTERNS: list[tuple[str, list[str]]] = [
    ('Maria Fernanda', [r'\bmaria\s+fernanda\b']),
    ('Mariah', [r'\bmariah\b']),
    ('Maria', [r'\bmaria\b']),
    ('Ju Mesquita', [r'\bju\s*mesquita\b', r'\bjuliana\s*mesquita\b']),
    ('Arlindo', [r'\barlindo\b']),
    ('Fiorela', [r'\bfiorela\b', r'\bfiorella\b']),
    ('Lala Noleto', [r'\blala\b', r'\bnoleto\b', r'\bnolleto\b']),
    ('Helena', [r'\bhelena\b']),
    ('Silvia', [r'\bsilvia\b']),
    ('Malu Borges', [r'\bmalu\s+borges\b']),
    ('Gio Pagano', [r'\bgio\s+pagano\b', r'\bgiovanna\s+pagano\b']),
    ('Ma Zanetti', [r'\bma\s+zanetti\b', r'\bma\s+zanetti\b']),
]


def load_weekly_module():
    spec = importlib.util.spec_from_file_location('lk_weekly', WEEKLY_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f'Cannot import weekly script at {WEEKLY_SCRIPT}')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def parse_month(month: str) -> tuple[str, str]:
    y, m = [int(x) for x in month.split('-', 1)]
    last = calendar.monthrange(y, m)[1]
    return f'{y:04d}-{m:02d}-01', f'{y:04d}-{m:02d}-{last:02d}'


def parse_num(v: Any) -> float:
    try:
        return float(v or 0)
    except Exception:
        return 0.0


def money(v: float) -> str:
    return ('R$ {:,.2f}'.format(float(v or 0))).replace(',', 'X').replace('.', ',').replace('X', '.')


def pct(v: float) -> str:
    return f'{v:.2f}%'.replace('.', ',')


def canonical_metric(items: Iterable[Dict[str, Any]]) -> Tuple[float, str | None]:
    vals = {a.get('action_type'): parse_num(a.get('value')) for a in (items or [])}
    for key in CANONICAL_ACTIONS:
        if key in vals:
            return vals[key], key
    return 0.0, None


def normalize_text(s: Any) -> str:
    s = str(s or '').lower()
    table = str.maketrans('áàãâäéèêëíìîïóòõôöúùûüçñ', 'aaaaaeeeeiiiiooooouuuucn')
    s = s.translate(table)
    return re.sub(r'\s+', ' ', s)


def row_text(row: Dict[str, Any]) -> str:
    return normalize_text(' | '.join(str(row.get(k) or '') for k in ['campaign_name', 'adset_name', 'ad_name']))


def fetch_meta(secrets: Dict[str, str], start: str, end: str) -> list[dict[str, Any]]:
    token = secrets.get('META_ACCESS_TOKEN') or secrets.get('FACEBOOK_ACCESS_TOKEN')
    account = secrets.get('META_ADS_ACCOUNT_ID') or META_ACCOUNT_FALLBACK
    if not token:
        raise RuntimeError('META access token missing')
    if not str(account).startswith('act_'):
        account = f'act_{account}'
    fields = ','.join(['campaign_id','adset_id','ad_id','campaign_name','adset_name','ad_name','spend','clicks','impressions','actions','action_values'])
    url = f'https://graph.facebook.com/v19.0/{account}/insights'
    params = {
        'access_token': token,
        'level': 'ad',
        'time_range': json.dumps({'since': start, 'until': end}),
        'fields': fields,
        'limit': 5000,
        'action_attribution_windows': json.dumps(['7d_click','1d_view']),
    }
    rows: list[dict[str, Any]] = []
    while url:
        r = requests.get(url, params=params, timeout=90)
        r.raise_for_status()
        data = r.json()
        rows.extend(data.get('data') or [])
        url = (data.get('paging') or {}).get('next')
        params = None
    return rows


def add_row(bucket: Dict[str, Any], row: Dict[str, Any]) -> None:
    purchases, purchase_key = canonical_metric(row.get('actions') or [])
    value, value_key = canonical_metric(row.get('action_values') or [])
    spend = parse_num(row.get('spend'))
    bucket['ad_ids'].add(row.get('ad_id'))
    bucket['spend'] += spend
    bucket['purchases'] += purchases
    bucket['value'] += value
    bucket['clicks'] += parse_num(row.get('clicks'))
    bucket['impressions'] += parse_num(row.get('impressions'))
    if purchases or len(bucket['examples']) < 3:
        bucket['examples'].append({
            'campaign_name': row.get('campaign_name'),
            'adset_name': row.get('adset_name'),
            'ad_name': row.get('ad_name'),
            'ad_id': row.get('ad_id'),
            'spend': spend,
            'purchases': purchases,
            'value': value,
            'purchase_key': purchase_key,
            'value_key': value_key,
        })


def empty_bucket() -> Dict[str, Any]:
    return {'ad_ids': set(), 'spend': 0.0, 'purchases': 0.0, 'value': 0.0, 'clicks': 0.0, 'impressions': 0.0, 'examples': []}


def finalize_bucket(label: str, b: Dict[str, Any]) -> Dict[str, Any]:
    spend, purchases, value = b['spend'], b['purchases'], b['value']
    return {
        'label': label,
        'ads': len([x for x in b['ad_ids'] if x]),
        'spend': round(spend, 2),
        'purchases': round(purchases, 2),
        'value': round(value, 2),
        'roas': round(value / spend, 2) if spend else 0.0,
        'cpa': round(spend / purchases, 2) if purchases else 0.0,
        'clicks': int(b['clicks']),
        'impressions': int(b['impressions']),
        'examples': b['examples'][:5],
    }


def pareto_label(text: str) -> str | None:
    # Ordered on purpose: Maria Fernanda and Mariah must beat broad Maria.
    for label, pats in PARETO_PATTERNS:
        if any(re.search(p, text) for p in pats):
            return label
    return None


def group_pareto(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    buckets: dict[str, Dict[str, Any]] = defaultdict(empty_bucket)
    for row in rows:
        label = pareto_label(row_text(row))
        if label:
            add_row(buckets[label], row)
    return sorted([finalize_bucket(k, v) for k, v in buckets.items()], key=lambda x: (x['purchases'], x['value']), reverse=True)


def group_operational(rows: list[dict[str, Any]], weekly_mod) -> list[dict[str, Any]]:
    aliases = weekly_mod.load_aliases()
    buckets: dict[str, Dict[str, Any]] = defaultdict(empty_bucket)
    for row in rows:
        label = weekly_mod.match_influencer(row_text(row), aliases)
        if label:
            add_row(buckets[label], row)
    return sorted([finalize_bucket(k, v) for k, v in buckets.items()], key=lambda x: (x['purchases'], x['value']), reverse=True)


def global_totals(rows: list[dict[str, Any]]) -> Dict[str, Any]:
    b = empty_bucket()
    for row in rows:
        add_row(b, row)
    out = finalize_bucket('Meta global', b)
    out['rows'] = len(rows)
    return out


def compare(expected: Dict[str, float], actual: Dict[str, Any]) -> Dict[str, Any]:
    out = {}
    for k in ['spend', 'purchases', 'value', 'roas', 'cpa']:
        if k not in expected:
            continue
        e, a = float(expected[k]), float(actual.get(k) or 0)
        delta = a - e
        denom = abs(e) or 1.0
        out[k] = {'expected': e, 'actual': round(a, 2), 'delta': round(delta, 2), 'match_pct': round(max(0.0, 100.0 - abs(delta) / denom * 100.0), 4)}
    return out


def render_md(rep: Dict[str, Any]) -> str:
    lines = []
    lines.append(f"# LK — Pareto-compatible monthly reconciliation — {rep['month']}")
    lines.append('')
    lines.append('## Resumo')
    g = rep['global']
    lines.append(f"- Meta global: {money(g['spend'])} spend, {g['purchases']:.0f} compras atribuídas no gerenciador, {money(g['value'])} **valor atribuído Meta no gerenciador** (não venda/receita real LK), ROAS Meta {g['roas']:.2f}, CPA Meta {money(g['cpa'])}.")
    ecommerce = rep.get('pareto_ecommerce') or {}
    if ecommerce:
        diff = g['value'] - ecommerce.get('revenue', 0)
        lines.append(f"- Venda real e-commerce Pareto: {ecommerce.get('orders', 0):.0f} pedidos, {money(ecommerce.get('revenue', 0))} receita total, {money(ecommerce.get('investment', 0))} investimento total, ROAS geral {ecommerce.get('roas', 0):.2f}.")
        lines.append(f"- Correção de senso crítico: o Meta Ads Manager atribuiu {money(g['value'])}, {money(diff)} acima da receita total da LK; logo esse número **não é venda da Meta** nem pode entrar na divisão Meta vs Google de vendas reais.")
    ga4_channels = rep.get('pareto_ga4_channels') or {}
    if ga4_channels:
        lines.append('- Receita real por canal deve usar Pareto/GA4/canais, não dashboards isolados de plataforma:')
        for channel, data in ga4_channels.items():
            lines.append(f"  - {channel}: {money(data['revenue'])}; conversão {data['conversion_rate']:.2f}%.")
    ga4_sm = rep.get('pareto_ga4_source_medium') or {}
    if ga4_sm:
        lines.append('- Principais origens/mídias Pareto/GA4:')
        for source, data in ga4_sm.items():
            lines.append(f"  - {source}: {data['sessions']:,} sessões; {money(data['revenue'])}; conversão {data['conversion_rate']:.2f}%.")
    if rep.get('expected_global'):
        lines.append('- Comparação Pareto global — campo Meta/Ads Manager:')
        for key, c in rep['expected_global'].items():
            label = 'attributed_value' if key == 'value' else key
            lines.append(f"  - {label}: esperado `{c['expected']}`, atual `{c['actual']}`, delta `{c['delta']}`, match `{c['match_pct']}%`.")
    lines.append('- Regra Lucas: 99%+ é operacionalmente correto; diferenças pequenas de poucos reais não bloqueiam se a metodologia está alinhada.')
    lines.append('- Marias separadas no modo Pareto-compatible: Maria, Maria Fernanda e Mariah.')
    lines.append('')
    lines.append('## Influencers — Pareto-compatible')
    for r in rep['pareto_rows']:
        lines.append(f"- {r['label']}: {r['ads']} anúncios; spend {money(r['spend'])}; compras atribuídas {r['purchases']:.0f}; valor atribuído Meta {money(r['value'])}; ROAS Meta {r['roas']:.2f}; CPA Meta {money(r['cpa'])}.")
    lines.append('')
    lines.append('## Influencers — Lucas-operacional')
    for r in rep['operational_rows'][:30]:
        lines.append(f"- {r['label']}: {r['ads']} anúncios; spend {money(r['spend'])}; compras atribuídas {r['purchases']:.0f}; valor atribuído Meta {money(r['value'])}; ROAS Meta {r['roas']:.2f}.")
    lines.append('')
    lines.append('## Correção conceitual')
    lines.append('- Correto: LK vendeu no mês o valor de e-commerce/Shopify/Pareto, e essa receita deve ser distribuída por canais usando GA4/Pareto channel grouping/source-medium.')
    lines.append('- Correto: Meta Ads e Google Ads reportam valores atribuídos em dashboards próprios; esses valores servem para diagnóstico da plataforma, não para dizer quanto cada canal vendeu de verdade.')
    lines.append('- Errado: dividir venda real entre Meta e Google usando `Receita` dos gerenciadores, porque os dashboards podem se sobrepor e a soma pode ultrapassar a venda total da LK.')
    lines.append('- Errado: dizer que “a Meta vendeu” mais que a LK vendeu no mês.')
    lines.append('')
    lines.append('## Guardrails')
    lines.append('- Meta é atribuição de plataforma, não receita operacional final.')
    lines.append('- Shopify/Pareto e-commerce é a referência de venda real mensal do negócio.')
    lines.append('- Shopify/produto/SKU/tamanho exigem ponte segura em outro relatório operacional.')
    lines.append('- Não usar thumbnail 64×64 como criativo visual em e-mails LK.')
    return '\n'.join(lines) + '\n'


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--month', default='2026-04', help='YYYY-MM')
    ap.add_argument('--out-dir', default=str(OUT_DIR))
    args = ap.parse_args()

    start, end = parse_month(args.month)
    weekly = load_weekly_module()
    secrets = weekly.load_secrets()
    rows = fetch_meta(secrets, start, end)
    g = global_totals(rows)
    pareto_rows = group_pareto(rows)
    operational_rows = group_operational(rows, weekly)
    rep = {
        'month': args.month,
        'period': {'start': start, 'end': end},
        'generated_at': dt.datetime.now(dt.timezone.utc).isoformat(),
        'global': g,
        'pareto_rows': pareto_rows,
        'operational_rows': operational_rows,
        'pareto_ecommerce': {},
        'pareto_platform_dashboards': {},
        'pareto_ga4_channels': {},
        'pareto_ga4_source_medium': {},
        'expected_global': {},
        'expected_influencers': {},
    }
    if args.month == '2026-04':
        rep['pareto_ecommerce'] = APRIL_2026_PARETO['ecommerce']
        rep['pareto_platform_dashboards'] = APRIL_2026_PARETO['platform_dashboards']
        rep['pareto_ga4_channels'] = APRIL_2026_PARETO['ga4_channels']
        rep['pareto_ga4_source_medium'] = APRIL_2026_PARETO['ga4_source_medium']
        rep['expected_global'] = compare(APRIL_2026_PARETO['global'], g)
        by_label = {r['label']: r for r in pareto_rows}
        rep['expected_influencers'] = {k: compare(v, by_label.get(k, {})) for k, v in APRIL_2026_PARETO['influencers'].items()}

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    base = out_dir / f'lk-pareto-compatible-reconciliation-{args.month}'
    json_path = base.with_suffix('.json')
    md_path = base.with_suffix('.md')
    json_path.write_text(json.dumps(rep, ensure_ascii=False, indent=2), encoding='utf-8')
    md_path.write_text(render_md(rep), encoding='utf-8')
    print(json.dumps({'month': args.month, 'rows': len(rows), 'json': str(json_path), 'md': str(md_path), 'global': g}, ensure_ascii=False))


if __name__ == '__main__':
    main()
