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
import base64
import calendar
import datetime as dt
import importlib.util
import json
import re
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, Tuple

import requests
from google.auth.transport.requests import Request as GoogleAuthRequest
from google.oauth2 import service_account

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


def ga4_credentials(secrets: Dict[str, str]):
    sa_raw = secrets.get('GA4_LK_SERVICE_ACCOUNT') or secrets.get('GOOGLE_SERVICE_ACCOUNT_JSON')
    prop = secrets.get('GOOGLE_ANALYTICS_PROPERTY_ID') or secrets.get('GA4_LK_PROPERTY_ID') or secrets.get('GA4_PROPERTY_ID')
    if not sa_raw or not prop:
        raise RuntimeError('GA4 service account or property id missing')
    creds = service_account.Credentials.from_service_account_info(
        json.loads(sa_raw), scopes=['https://www.googleapis.com/auth/analytics.readonly']
    )
    creds.refresh(GoogleAuthRequest())
    return str(prop), creds.token


def ga4_report(secrets: Dict[str, str], start: str, end: str, dimensions: list[str], metrics: list[str], limit: int = 100) -> dict[str, Any]:
    prop, token = ga4_credentials(secrets)
    url = f'https://analyticsdata.googleapis.com/v1beta/properties/{prop}:runReport'
    body = {
        'dateRanges': [{'startDate': start, 'endDate': end}],
        'metrics': [{'name': m} for m in metrics],
        'limit': limit,
    }
    if dimensions:
        body['dimensions'] = [{'name': d} for d in dimensions]
        body['orderBys'] = [{'metric': {'metricName': metrics[0]}, 'desc': True}]
    else:
        body['metricAggregations'] = ['TOTAL']
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode(),
        headers={'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'},
        method='POST',
    )
    return json.loads(urllib.request.urlopen(req, timeout=90).read().decode())


def metric_values(row: dict[str, Any], metric_names: list[str]) -> dict[str, float]:
    return {name: parse_num(v.get('value')) for name, v in zip(metric_names, row.get('metricValues') or [])}


def fetch_ga4_pareto_metrics(secrets: Dict[str, str], start: str, end: str) -> dict[str, Any]:
    # This reproduces the Pareto ecommerce/channel pages from GA4 directly:
    # - totalRevenue / transactions / sessions for executive summary
    # - sessionDefaultChannelGroup for "Canais que mais contribuíram para receita"
    # - sessionSourceMedium for "Principais origens de tráfego e receita"
    summary_metrics = ['totalRevenue', 'transactions', 'sessions', 'averagePurchaseRevenue']
    summary_data = ga4_report(secrets, start, end, [], summary_metrics)
    summary = metric_values((summary_data.get('rows') or [{}])[0], summary_metrics)
    channel_metrics = ['totalRevenue', 'sessions', 'transactions', 'sessionConversionRate']
    ch_data = ga4_report(secrets, start, end, ['sessionDefaultChannelGroup'], channel_metrics, limit=25)
    sm_data = ga4_report(secrets, start, end, ['sessionSourceMedium'], channel_metrics, limit=25)
    def rows(data):
        out = []
        for row in data.get('rows') or []:
            label = row['dimensionValues'][0]['value']
            vals = metric_values(row, channel_metrics)
            out.append({
                'label': label,
                'revenue': round(vals['totalRevenue'], 2),
                'sessions': int(vals['sessions']),
                'transactions': int(round(vals['transactions'])),
                'conversion_rate_pct': round(vals['sessionConversionRate'] * 100, 4),
            })
        return out
    return {
        'summary': {
            'revenue': round(summary['totalRevenue'], 2),
            'orders': int(round(summary['transactions'])),
            'sessions': int(round(summary['sessions'])),
            'average_order_value': round(summary['averagePurchaseRevenue'], 2),
        },
        'channels': rows(ch_data),
        'source_medium': rows(sm_data),
        'property_id_used': secrets.get('GOOGLE_ANALYTICS_PROPERTY_ID'),
    }


def fetch_metricool_google_ads(secrets: Dict[str, str], start: str, end: str) -> dict[str, Any]:
    user_id, blog_id, token = secrets.get('METRICOOL_USER_ID'), secrets.get('METRICOOL_BLOG_ID'), secrets.get('METRICOOL_API_TOKEN')
    if not (user_id and blog_id and token):
        raise RuntimeError('Metricool credentials missing')
    params = {
        'userId': user_id,
        'blogId': blog_id,
        'userToken': token,
        'from': f'{start}T00:00:00',
        'to': f'{end}T23:59:59',
        'timezone': 'America/Sao_Paulo',
    }
    url = 'https://app.metricool.com/api/v2/analytics/campaigns/googleads?' + urllib.parse.urlencode(params)
    data = json.loads(urllib.request.urlopen(url, timeout=90).read().decode())
    campaigns = data.get('data') or []
    spend = sum(parse_num(c.get('spent')) for c in campaigns)
    conversions = sum(parse_num(c.get('conversions')) for c in campaigns)
    value = sum(parse_num(c.get('allConversionsValue')) for c in campaigns)
    clicks = sum(parse_num(c.get('clicks')) for c in campaigns)
    impressions = sum(parse_num(c.get('impressions')) for c in campaigns)
    return {
        'source': 'Metricool Google Ads API',
        'campaigns': len(campaigns),
        'spend': round(spend, 2),
        'conversions': round(conversions, 2),
        'attributed_value': round(value, 2),
        'roas': round(value / spend, 2) if spend else 0,
        'cpa': round(spend / conversions, 2) if conversions else 0,
        'clicks': int(clicks),
        'impressions': int(impressions),
        'top_campaigns': sorted([
            {
                'name': c.get('name'),
                'spend': round(parse_num(c.get('spent')), 2),
                'conversions': round(parse_num(c.get('conversions')), 2),
                'attributed_value': round(parse_num(c.get('allConversionsValue')), 2),
                'roas': round(parse_num(c.get('purchaseROAS')), 2),
            } for c in campaigns
        ], key=lambda x: x['attributed_value'], reverse=True)[:10],
    }


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
    ga4 = rep.get('ga4_calculated') or {}
    ecommerce = ga4.get('summary') or {}
    if ecommerce:
        diff = g['value'] - ecommerce.get('revenue', 0)
        total_spend = g['spend'] + (rep.get('google_ads_platform') or {}).get('spend', 0)
        overall_roas = ecommerce.get('revenue', 0) / total_spend if total_spend else 0
        lines.append(f"- Venda real e-commerce calculada via GA4: {ecommerce.get('orders', 0):.0f} pedidos, {money(ecommerce.get('revenue', 0))} receita total, {ecommerce.get('sessions', 0):,} sessões, ticket médio {money(ecommerce.get('average_order_value', 0))}.")
        lines.append(f"- Investimento pago calculado: Meta {money(g['spend'])} + Google/Metricool {money((rep.get('google_ads_platform') or {}).get('spend', 0))} = {money(total_spend)}; ROAS geral calculado {overall_roas:.2f}.")
        lines.append(f"- Correção de senso crítico: o Meta Ads Manager atribuiu {money(g['value'])}, {money(diff)} acima da receita total da LK; logo esse número **não é venda da Meta** nem pode entrar na divisão Meta vs Google de vendas reais.")
    channels = ga4.get('channels') or []
    if channels:
        lines.append('- Receita real por canal calculada via GA4 `sessionDefaultChannelGroup`:')
        for row in channels[:10]:
            lines.append(f"  - {row['label']}: {money(row['revenue'])}; {row['sessions']:,} sessões; {row['transactions']} pedidos; conversão {row['conversion_rate_pct']:.2f}%.")
    source_medium = ga4.get('source_medium') or []
    if source_medium:
        lines.append('- Principais origens/mídias calculadas via GA4 `sessionSourceMedium`:')
        for row in source_medium[:10]:
            lines.append(f"  - {row['label']}: {row['sessions']:,} sessões; {money(row['revenue'])}; {row['transactions']} pedidos; conversão {row['conversion_rate_pct']:.2f}%.")
    google = rep.get('google_ads_platform') or {}
    if google:
        lines.append(f"- Google Ads calculado via Metricool: spend {money(google['spend'])}; conversões atribuídas {google['conversions']:.2f}; valor atribuído {money(google['attributed_value'])}; ROAS plataforma {google['roas']:.2f}.")
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
    ga4 = fetch_ga4_pareto_metrics(secrets, start, end)
    google_ads = fetch_metricool_google_ads(secrets, start, end)
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
        'google_ads_platform': google_ads,
        'ga4_calculated': ga4,
        'expected_global': {},
        'expected_influencers': {},
    }
    if args.month == '2026-04':
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
