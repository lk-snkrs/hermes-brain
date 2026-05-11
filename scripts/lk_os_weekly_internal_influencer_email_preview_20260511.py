#!/usr/bin/env python3
"""LK OS weekly internal influencer email preview, read-only.

Creates a weekly internal email packet from versioned Phase 3 artifacts. This is
preview-only: no Gmail/Klaviyo/WhatsApp send, no cron, no campaign/coupon/write.
The copy intentionally avoids dashboard/tool jargon in the customer-facing body.
"""
from __future__ import annotations

import html
import json
import pathlib
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPLIT_JSON = ROOT / 'reports/lk-os-pareto-operational-split-2026-05-11.json'
IDENTITY_JSON = ROOT / 'reports/lk-os-influencer-identity-bridge-2026-05-11.json'
OUT_JSON = ROOT / 'reports/lk-os-weekly-internal-influencer-email-preview-2026-05-11.json'
OUT_MD = ROOT / 'reports/lk-os-weekly-internal-influencer-email-preview-2026-05-11.md'
OUT_HTML = ROOT / 'reports/lk-os-weekly-internal-influencer-email-preview-2026-05-11.html'
BRAIN_DOC = ROOT / 'areas/lk/sub-areas/trafego-pago/rotinas/weekly-internal-influencer-email-preview-2026-05-11.md'

BLOCKED_TERMS = [
    'DesignMD', 'dashboard', 'Cloudflare', 'plain text', 'MCP', 'tool call', 'script output'
]


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def brl(v: float | int | None) -> str:
    if v is None:
        return 'n/d'
    return 'R$ ' + f'{float(v):,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


def get_identity(name: str, identities: list[dict[str, Any]]) -> dict[str, Any] | None:
    aliases = {
        'Silvia': 'Silvia Heinz',
        'Helena': 'Helena Lunardelli',
    }
    target = aliases.get(name, name)
    for row in identities:
        if row.get('influencer_name') == target:
            return row
    return None


def short_products(identity: dict[str, Any] | None, limit: int = 4) -> list[str]:
    if not identity:
        return []
    out = []
    for row in identity.get('top_product_sku_size_examples_sanitized') or []:
        product = row.get('product') or 'Produto'
        sku = row.get('sku') or 'SKU n/d'
        size = row.get('size_or_variant') or 'tam. n/d'
        qty = row.get('qty') or 0
        revenue = brl(row.get('revenue_fact_shopify'))
        risk = row.get('stock_risk_fact_tiny_stock') or 'risco n/d'
        out.append(f'{product} | SKU {sku} | tam. {size} | {qty} un. | {revenue} | estoque: {risk}')
        if len(out) >= limit:
            break
    return out


def classify_for_email(split_rows: list[dict[str, Any]], identities: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    actionable = []
    investigate = []
    watch = []
    for row in split_rows:
        label = row['label']
        identity = get_identity(label, identities)
        pareto = row.get('pareto_compatible') or {}
        if row.get('operational_decision_allowed_now') and identity:
            actionable.append({
                'name': label,
                'status': 'pronto para análise interna, sem execução automática',
                'why': 'há ponte com Shopify e consequência de estoque para priorizar leitura de produto',
                'shopify_orders': identity.get('matched_orders_fact_shopify'),
                'shopify_revenue': identity.get('revenue_fact_shopify'),
                'platform_spend': pareto.get('spend_platform_signal'),
                'platform_purchases': pareto.get('purchases_platform_signal'),
                'products': short_products(identity),
                'next_step': 'validar handle/cupom/ad_id oficiais e só depois transformar em ação de mídia/estoque com aprovação',
            })
        elif label == 'Lala Noleto':
            investigate.append({
                'name': label,
                'status': 'investigação',
                'why': 'há sinal de mídia, mas não há ponte direta Shopify no recorte',
                'platform_spend': pareto.get('spend_platform_signal'),
                'platform_purchases': pareto.get('purchases_platform_signal'),
                'shopify_orders': 0,
                'shopify_revenue': 0,
                'next_step': 'confirmar cupom, UTM, landing ou ad_id antes de qualquer leitura de produto, verba ou estoque',
            })
        elif label in ('Maria', 'Maria Fernanda', 'Mariah'):
            watch.append({
                'name': label,
                'status': 'manter separado na leitura Pareto-compatible',
                'why': 'nomes parecidos não devem ser consolidados automaticamente',
                'platform_spend': pareto.get('spend_platform_signal'),
                'platform_purchases': pareto.get('purchases_platform_signal'),
                'next_step': 'seguir separado até existir ponte operacional própria',
            })
    return {'actionable': actionable, 'investigate': investigate, 'watch': watch}


def build_email_text(groups: dict[str, list[dict[str, Any]]], split: dict[str, Any]) -> dict[str, str]:
    period = split.get('periods', {}).get('pareto_period') or {}
    subject = 'LK, leitura semanal de influencers, mídia e estoque, preview interno'
    preview = 'Silvia e Helena podem virar análise interna; Lala segue investigação; Marias continuam separadas.'
    lines = [
        'Oi, time.',
        '',
        f'Fechei uma leitura interna do período {period.get("start", "n/d")} a {period.get("end", "n/d")} para separar o que é sinal de mídia do que já pode orientar decisão operacional.',
        '',
        'Resumo rápido:',
        '- Silvia e Helena têm ponte suficiente para análise interna de produto e estoque, mas não autorizam campanha, cupom, compra ou envio.',
        '- Lala tem sinal de mídia, mas ainda precisa de confirmação de cupom, UTM, landing ou ad_id antes de qualquer decisão.',
        '- Maria, Maria Fernanda e Mariah continuam separadas para evitar leitura misturada.',
        '',
        'Prioridades da semana:',
    ]
    for item in groups['actionable']:
        lines.extend([
            f'- {item["name"]}: {item["shopify_orders"]} pedidos com ponte Shopify, {brl(item["shopify_revenue"])} em receita com evidência, próximo passo: {item["next_step"]}.',
        ])
    for item in groups['investigate']:
        lines.append(f'- {item["name"]}: {item["why"]}; próximo passo: {item["next_step"]}.')
    lines.extend(['', 'Produtos que merecem atenção interna:'])
    for item in groups['actionable']:
        lines.append(f'- {item["name"]}:')
        for product in item['products']:
            lines.append(f'  - {product}')
    lines.extend([
        '',
        'Decisões bloqueadas até aprovação:',
        '- criar ou alterar cupom;',
        '- mudar campanha, verba, criativo ou UTM;',
        '- alterar Shopify, Tiny, preço ou estoque;',
        '- enviar e-mail, WhatsApp ou qualquer comunicação externa;',
        '- comprar, reservar produto ou acionar fornecedor.',
        '',
        'Próximo passo sugerido: preencher a lista oficial de handle, cupom, UTM e ad_id por influencer. Com isso, a próxima leitura semanal deixa de misturar sinal de mídia com decisão de estoque.',
    ])
    return {'subject': subject, 'preview': preview, 'body_markdown': '\n'.join(lines)}


def build_html(email: dict[str, str]) -> str:
    body_lines = email['body_markdown'].split('\n')
    parts = []
    for line in body_lines:
        if not line:
            parts.append('<div style="height:12px"></div>')
        elif line.startswith('- '):
            parts.append(f'<li style="margin:6px 0;color:#3f3a34;line-height:1.5">{html.escape(line[2:])}</li>')
        elif line.startswith('  - '):
            parts.append(f'<li style="margin:4px 0 4px 18px;color:#5b544b;line-height:1.45">{html.escape(line[4:])}</li>')
        elif line.endswith(':'):
            parts.append(f'<h3 style="font-family:Georgia,serif;font-size:18px;margin:18px 0 8px;color:#151515">{html.escape(line)}</h3>')
        else:
            parts.append(f'<p style="margin:0;color:#3f3a34;line-height:1.55">{html.escape(line)}</p>')
    return f'''<!doctype html>
<html><head><meta charset="utf-8"><title>{html.escape(email['subject'])}</title></head>
<body style="margin:0;background:#f7f3ed;font-family:Arial,Helvetica,sans-serif;color:#151515">
  <div style="max-width:720px;margin:0 auto;background:#fffaf2;padding:0 0 32px">
    <div style="background:#111;padding:22px 28px;color:#fff">
      <div style="font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:#d8c2a2">LK Sneakers</div>
      <h1 style="font-family:Georgia,serif;font-weight:400;font-size:28px;margin:8px 0 0">Leitura semanal de influencers</h1>
    </div>
    <div style="padding:28px">
      <p style="margin:0 0 18px;color:#8a6b45;font-size:14px">Preview interno, não enviado automaticamente.</p>
      {''.join(parts)}
    </div>
  </div>
</body></html>
'''


def validate_no_jargon(texts: list[str]) -> list[str]:
    findings = []
    for term in BLOCKED_TERMS:
        for txt in texts:
            if term.lower() in txt.lower():
                findings.append(term)
                break
    return sorted(set(findings))


def build_payload() -> dict[str, Any]:
    split = json.loads(SPLIT_JSON.read_text(encoding='utf-8'))
    identity = json.loads(IDENTITY_JSON.read_text(encoding='utf-8'))
    identities = identity.get('identity_bridge') or []
    groups = classify_for_email(split.get('split_rows') or [], identities)
    email = build_email_text(groups, split)
    html_text = build_html(email)
    jargon = validate_no_jargon([email['subject'], email['preview'], email['body_markdown']])
    return {
        'generated_at': now_utc(),
        'scope': 'LK OS Phase 3 weekly internal influencer email preview, read-only',
        'channel': 'email_preview_only',
        'would_send': False,
        'read_only': True,
        'sources': {
            'pareto_operational_split': str(SPLIT_JSON.relative_to(ROOT)),
            'identity_bridge': str(IDENTITY_JSON.relative_to(ROOT)),
        },
        'summary': {
            'actionable_internal_analysis': len(groups['actionable']),
            'investigation': len(groups['investigate']),
            'watch_separate_names': len(groups['watch']),
            'blocked_jargon_findings': jargon,
        },
        'email_preview': email,
        'html_preview_path': str(OUT_HTML.relative_to(ROOT)),
        'routing': groups,
        'approval_required_for': [
            'real_email_send', 'klaviyo_or_whatsapp_send', 'coupon_create_or_update',
            'campaign_budget_creative_or_utm_change', 'shopify_or_tiny_write',
            'stock_price_purchase_supplier_action', 'cron_creation'
        ],
        'not_performed': [
            'gmail_send', 'klaviyo_send', 'whatsapp_send', 'cron_creation', 'live_meta_call',
            'live_shopify_call', 'live_tiny_call', 'campaign_change', 'coupon_change',
            'shopify_write', 'tiny_write', 'production_db_write'
        ],
    }, html_text


def build_md(payload: dict[str, Any]) -> str:
    e = payload['email_preview']
    lines = [
        '# LK OS Weekly Internal Influencer Email Preview, read-only',
        '',
        f"Generated at: `{payload['generated_at']}`",
        '',
        '## Status',
        '',
        '- Canal: preview interno de e-mail.',
        '- Envio: não enviado.',
        '- Cron: não criado.',
        f"- Jargão bloqueado encontrado no corpo do e-mail: {', '.join(payload['summary']['blocked_jargon_findings']) if payload['summary']['blocked_jargon_findings'] else '0'}",
        '',
        '## Assunto',
        '',
        e['subject'],
        '',
        '## Preview',
        '',
        e['preview'],
        '',
        '## Corpo do e-mail',
        '',
        e['body_markdown'],
        '',
        '## Artefatos',
        '',
        f"- HTML preview: `{payload['html_preview_path']}`",
        '',
        '## O que não foi feito',
        '',
    ]
    for item in payload['not_performed']:
        lines.append(f'- {item}')
    return '\n'.join(lines) + '\n'


def main() -> None:
    payload, html_text = build_payload()
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    OUT_HTML.write_text(html_text, encoding='utf-8')
    md = build_md(payload)
    OUT_MD.write_text(md, encoding='utf-8')
    BRAIN_DOC.write_text(md.replace('# LK OS Weekly Internal Influencer Email Preview, read-only', '# LK OS, Weekly Internal Influencer Email Preview read-only, 2026-05-11'), encoding='utf-8')
    print(json.dumps({'ok': True, 'json': str(OUT_JSON), 'md': str(OUT_MD), 'html': str(OUT_HTML), 'jargon_findings': payload['summary']['blocked_jargon_findings']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
