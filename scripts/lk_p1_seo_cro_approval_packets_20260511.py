#!/usr/bin/env python3
"""LK P1 SEO/CRO approval packets, read-only.

Turns the low-conversion priority router into approval-ready packets for the top
P1 pages. It reads public HTML only, combines GA4/GSC/Merchant facts already
materialized, and drafts exact title/meta plus above-the-fold CRO previews.
No Shopify, theme, Merchant, GSC, content, campaign, or customer-facing writes.
"""
from __future__ import annotations

import html
import json
import pathlib
import re
import urllib.error
import urllib.request
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'reports/lk-pdp-low-conversion-priority-router-2026-05-11.json'
OUT_JSON = ROOT / 'reports/lk-p1-seo-cro-approval-packets-2026-05-11.json'
OUT_MD = ROOT / 'reports/lk-p1-seo-cro-approval-packets-2026-05-11.md'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/p1-seo-cro-approval-packets-2026-05-11.md'
TOP_N = 8

UA = 'Hermes-LK-SEO-CRO-ReadOnly/1.0'


def clean_text(s: str | None) -> str | None:
    if s is None:
        return None
    s = html.unescape(re.sub(r'\s+', ' ', s)).strip()
    return s or None


def fetch_public_html(url: str) -> str:
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': 'text/html'})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            raw = r.read(1_500_000)
            return raw.decode(r.headers.get_content_charset() or 'utf-8', errors='replace')
    except urllib.error.HTTPError as e:
        return f'<!-- fetch_error HTTP {e.code} -->'
    except Exception as e:
        return f'<!-- fetch_error {type(e).__name__} -->'


def extract_html_facts(raw: str) -> dict[str, Any]:
    title = None
    m = re.search(r'<title[^>]*>(.*?)</title>', raw, re.I | re.S)
    if m:
        title = clean_text(re.sub(r'<[^>]+>', ' ', m.group(1)))
    meta = None
    m = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\'][^>]*>', raw, re.I | re.S)
    if not m:
        m = re.search(r'<meta[^>]+content=["\'](.*?)["\'][^>]+name=["\']description["\'][^>]*>', raw, re.I | re.S)
    if m:
        meta = clean_text(m.group(1))
    h1 = None
    m = re.search(r'<h1[^>]*>(.*?)</h1>', raw, re.I | re.S)
    if m:
        h1 = clean_text(re.sub(r'<[^>]+>', ' ', m.group(1)))
    return {
        'current_title': title,
        'current_title_len': len(title or ''),
        'current_meta': meta,
        'current_meta_len': len(meta or ''),
        'current_h1': h1,
        'current_h1_len': len(h1 or ''),
        'fetch_ok': 'fetch_error' not in raw[:100],
    }


def label_from_url(url: str, page_type: str, gsc: dict[str, Any] | None) -> str:
    if gsc and gsc.get('queries'):
        q = gsc['queries'][0].get('query')
        if q:
            return q.title().replace('Nb ', 'NB ').replace('Mqueen', 'McQueen')
    slug = url.rstrip('/').split('/')[-1].replace('-', ' ')
    for bad in ['tenis ', 'tênis ']:
        slug = slug.replace(bad, '')
    return slug.title().replace('X ', 'x ').replace('Lk', 'LK').replace('Mqueen', 'McQueen')


def title_for(item: dict[str, Any], label: str) -> str:
    page_type = item['page_type']
    if page_type == 'collection':
        base = f'{label} Originais | LK Sneakers'
    else:
        base = f'{label} Original | LK Sneakers'
    if len(base) <= 58:
        return base
    base = f'{label} | LK Sneakers'
    if len(base) <= 58:
        return base
    return base[:55].rstrip() + '...'


def meta_for(item: dict[str, Any], label: str) -> str:
    page_type = item['page_type']
    if page_type == 'collection':
        meta = f'Confira {label} originais na curadoria LK Sneakers, com seleção premium, loja física em São Paulo, autenticidade garantida e até 10x sem juros.'
    else:
        meta = f'{label} original na curadoria LK Sneakers, com autenticidade garantida, seleção premium, loja física em São Paulo e até 10x sem juros.'
    if len(meta) <= 155:
        return meta
    return meta[:152].rstrip(' ,.;') + '...'


def cro_preview(item: dict[str, Any], label: str) -> list[str]:
    page_type = item['page_type']
    if page_type == 'collection':
        return [
            f'Reforçar no topo da collection que a seleção {label} é original e curada pela LK.',
            'Adicionar bloco curto de confiança: autenticidade, atendimento humano, loja física e parcelamento.',
            'Priorizar cards disponíveis/mais fortes acima da dobra e reduzir distrações antes da grade.',
        ]
    return [
        f'Reforçar acima da dobra que o produto {label} é original e passa por curadoria LK.',
        'Evidenciar prova de confiança: autenticidade, loja física, atendimento e condições de pagamento.',
        'Checar se foto, tamanho disponível e CTA aparecem claramente sem rolagem excessiva.',
    ]


def packet_for(item: dict[str, Any], rank: int) -> dict[str, Any]:
    raw = fetch_public_html(item['url'])
    facts = extract_html_facts(raw)
    label = label_from_url(item['url'], item['page_type'], item.get('gsc_context'))
    proposed_title = title_for(item, label)
    proposed_meta = meta_for(item, label)
    gsc = item.get('gsc_context') or {}
    return {
        'rank': rank,
        'priority': item['priority'],
        'score': item['score'],
        'url': item['url'],
        'page_type': item['page_type'],
        'label': label,
        'source_facts': {
            'ga4_sessions': item['sessions'],
            'ga4_purchases': item['ecommerce_purchases'],
            'ga4_landing_purchase_rate_percent': item['landing_purchase_rate_percent'],
            'ga4_revenue': item['purchase_revenue'],
            'gsc_impressions': gsc.get('impressions'),
            'gsc_ctr_percent': gsc.get('ctr_percent'),
            'gsc_position': gsc.get('position'),
            'gsc_top_query': (gsc.get('queries') or [{}])[0].get('query') if gsc.get('queries') else None,
            'source_labels': item['source_labels'],
        },
        **facts,
        'proposed_title': proposed_title,
        'proposed_title_len': len(proposed_title),
        'proposed_meta': proposed_meta,
        'proposed_meta_len': len(proposed_meta),
        'visible_h1_proposed': None,
        'seo_field_scope': 'collection SEO title/meta' if item['page_type'] == 'collection' else 'PDP SEO title/meta',
        'cro_preview_scope': 'visible above-the-fold recommendation preview',
        'cro_preview_bullets': cro_preview(item, label),
        'risk_split': {
            'seo_fields_only': 'baixo, se aprovado e aplicado só em SEO title/meta de produto/collection',
            'visible_content': 'médio, exige preview separado antes de alterar H1, descrição, layout ou tema',
        },
        'approval_status': 'needs_approval',
        'write_allowed_now': False,
    }


def build_payload() -> dict[str, Any]:
    src = json.loads(SOURCE.read_text())
    p1 = [x for x in src['queue'] if x['priority'] == 'P1'][:TOP_N]
    packets = [packet_for(item, i + 1) for i, item in enumerate(p1)]
    return {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'LK P1 SEO/CRO approval packets from low-conversion router',
        'source': str(SOURCE.relative_to(ROOT)),
        'summary': {
            'packets': len(packets),
            'seo_field_previews': len(packets),
            'visible_cro_previews': len(packets),
            'writes_allowed_now': 0,
        },
        'packets': packets,
        'guardrails': [
            'This is preview only; no Shopify, theme, content, Merchant, feed, GSC, Indexing API, campaign or customer send writes.',
            'SEO title/meta preview is separated from visible H1/body/layout CRO recommendations.',
            'Homepage is not included in this packet set; homepage SEO needs separate plan/rollback if it appears later.',
            'Public HTML fetch is read-only and used only to capture current title/meta/H1.',
        ],
        'not_performed': [
            'shopify_write', 'seo_field_update', 'visible_h1_update', 'pdp_body_update', 'theme_write',
            'merchant_center_write', 'feed_update', 'gsc_admin_change', 'indexing_api_submit',
            'content_publish', 'campaign_or_customer_send', 'cron_creation'
        ],
    }


def md(payload: dict[str, Any]) -> str:
    lines = [
        '# LK P1 SEO/CRO Approval Packets, 2026-05-11', '',
        f"Generated at: `{payload['generated_at']}`", '',
        '## Veredito', '',
        'Transformei os P1 de baixa conversão em pacotes de aprovação: cada página tem dados GA4/GSC, title/meta atuais, proposta exata e recomendações CRO visíveis separadas de SEO fields. Nada foi aplicado.', '',
        '## Snapshot', '',
        f"- Pacotes: {payload['summary']['packets']}",
        f"- Previews SEO title/meta: {payload['summary']['seo_field_previews']}",
        f"- Previews CRO visíveis: {payload['summary']['visible_cro_previews']}",
        f"- Writes liberados agora: {payload['summary']['writes_allowed_now']}", '',
    ]
    for p in payload['packets']:
        f = p['source_facts']
        lines.extend([
            f"## {p['rank']}. {p['priority']} · {p['page_type']} · score {p['score']}", '',
            f"URL: {p['url']}", '',
            '### Dados', '',
            f"- GA4: {f['ga4_sessions']} sessões, {f['ga4_purchases']} compras, CVR landing {f['ga4_landing_purchase_rate_percent']}%, receita R$ {f['ga4_revenue']}",
            f"- GSC: {f['gsc_impressions']} impressões, CTR {f['gsc_ctr_percent']}%, posição {f['gsc_position']}",
            f"- Query destaque: `{f['gsc_top_query']}`", '',
            '### SEO fields, preview', '',
            f"- Title atual ({p['current_title_len']}): {p['current_title'] or '(não capturado)'}",
            f"- Title proposto ({p['proposed_title_len']}): {p['proposed_title']}",
            f"- Meta atual ({p['current_meta_len']}): {p['current_meta'] or '(não capturado)'}",
            f"- Meta proposta ({p['proposed_meta_len']}): {p['proposed_meta']}",
            f"- H1 atual ({p['current_h1_len']}): {p['current_h1'] or '(não capturado)'}",
            '- H1 proposto: sem alteração nesta etapa', '',
            '### CRO visível, preview separado', '',
        ])
        for b in p['cro_preview_bullets']:
            lines.append(f'- {b}')
        lines.extend(['', '### Aprovação', '', f"- Status: `{p['approval_status']}`", '- SEO fields e mudanças visíveis devem ser aprovados separadamente.', ''])
    lines.extend(['## Guardrails', ''])
    for g in payload['guardrails']:
        lines.append(f'- {g}')
    lines.extend(['', '## O que não foi feito', ''])
    for n in payload['not_performed']:
        lines.append(f'- {n}')
    return '\n'.join(lines) + '\n'


def main() -> None:
    payload = build_payload()
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    text = md(payload)
    OUT_MD.write_text(text, encoding='utf-8')
    BRAIN_DOC.write_text(text, encoding='utf-8')
    print(json.dumps({'ok': True, 'summary': payload['summary']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
