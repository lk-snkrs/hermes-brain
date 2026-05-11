#!/usr/bin/env python3
"""LK OS creative visual approval gate, read-only.

Creates the final Phase 3 creative gate: image assets can only enter executive
preview/email after visual clarity checks and explicit human approval. This script
uses already-versioned creative asset metadata. It does not call Meta, download
assets, send email, create cron, or change campaigns.
"""
from __future__ import annotations

import json
import pathlib
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
ASSETS_JSON = ROOT / 'reports/lk-weekly-creative-assets-2026-05-09/creative-assets-output.json'
OUT_JSON = ROOT / 'reports/lk-os-creative-visual-approval-gate-2026-05-11.json'
OUT_MD = ROOT / 'reports/lk-os-creative-visual-approval-gate-2026-05-11.md'
BRAIN_DOC = ROOT / 'areas/lk/sub-areas/trafego-pago/rotinas/creative-visual-approval-gate-readonly-2026-05-11.md'

MIN_WIDTH = 600
MIN_HEIGHT = 600
MIN_BYTES = 50_000
MIN_STDEV = 20.0
MIN_MEAN_LUMA = 20.0
MAX_MEAN_LUMA = 235.0
BLOCKED_SOURCES = {'thumbnail_url'}


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def brl(v: float | int | None) -> str:
    if v is None:
        return 'n/d'
    return 'R$ ' + f'{float(v):,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


def visual_quality(asset: dict[str, Any]) -> tuple[str, list[str]]:
    reasons: list[str] = []
    if not asset or not asset.get('ok'):
        reasons.append('no_ok_chosen_asset')
        return 'blocked_no_asset', reasons
    q = asset.get('quality') or {}
    size = asset.get('size') or [0, 0]
    width, height = (size + [0, 0])[:2]
    if not q.get('decoded'):
        reasons.append('not_decoded')
    if width < MIN_WIDTH or height < MIN_HEIGHT:
        reasons.append(f'low_resolution_{width}x{height}')
    if (asset.get('bytes') or 0) < MIN_BYTES:
        reasons.append('low_file_size_bytes')
    if asset.get('source') in BLOCKED_SOURCES:
        reasons.append('thumbnail_source_only')
    if q.get('black_frame'):
        reasons.append('black_frame')
    if q.get('side_black_bars'):
        reasons.append('side_black_bars')
    mean = float(q.get('mean_luma') or 0)
    stdev = float(q.get('stdev_luma') or 0)
    if mean < MIN_MEAN_LUMA:
        reasons.append('too_dark')
    if mean > MAX_MEAN_LUMA:
        reasons.append('too_bright')
    if stdev < MIN_STDEV:
        reasons.append('low_visual_contrast')
    if reasons:
        return 'blocked_visual_quality', reasons
    return 'candidate_needs_human_approval', ['automated_quality_passed_but_human_approval_missing']


def rank_key(row: dict[str, Any]) -> tuple[float, float, float]:
    return (float(row.get('purchases') or 0), float(row.get('value') or 0), float(row.get('spend') or 0))


def build_rows(ads: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows = []
    for ad in sorted(ads, key=rank_key, reverse=True):
        asset = ad.get('chosen_asset') or {}
        status, blockers = visual_quality(asset)
        q = asset.get('quality') or {}
        size = asset.get('size') or [None, None]
        rows.append({
            'ad_id': ad.get('ad_id'),
            'influencer': ad.get('influencer'),
            'ad_name': ad.get('ad_name'),
            'creative_id': ad.get('creative_id'),
            'platform_signal': {
                'spend': ad.get('spend'),
                'purchases': ad.get('purchases'),
                'value': ad.get('value'),
                'clicks': ad.get('clicks'),
                'impressions': ad.get('impressions'),
            },
            'chosen_asset_sanitized': {
                'source': asset.get('source'),
                'size': size,
                'bytes': asset.get('bytes'),
                'sha16': asset.get('sha16'),
                'path': asset.get('path'),
                'quality': {
                    'decoded': q.get('decoded'),
                    'mean_luma': q.get('mean_luma'),
                    'stdev_luma': q.get('stdev_luma'),
                    'black_frame': q.get('black_frame'),
                    'side_black_bars': q.get('side_black_bars'),
                },
            },
            'visual_gate_status': status,
            'blockers_or_requirements': blockers,
            'eligible_for_email_image_now': False,
            'human_approval_status': 'not_requested_not_granted',
            'safe_next_step': 'manual_visual_review_and_lucas_approval_before_any_email_or_campaign_use',
            'source_labels': ['platform_signal'],
        })
    return rows


def build_payload() -> dict[str, Any]:
    data = json.loads(ASSETS_JSON.read_text(encoding='utf-8'))
    rows = build_rows(data.get('ads') or [])
    counts: dict[str, int] = {}
    for row in rows:
        counts[row['visual_gate_status']] = counts.get(row['visual_gate_status'], 0) + 1
    return {
        'generated_at': now_utc(),
        'scope': 'LK OS Phase 3 creative visual approval gate, read-only',
        'read_only': True,
        'source': str(ASSETS_JSON.relative_to(ROOT)),
        'period': data.get('period'),
        'rules': {
            'email_images_default': 'blocked_until_visual_clear_and_human_approved',
            'minimum_resolution': [MIN_WIDTH, MIN_HEIGHT],
            'minimum_bytes': MIN_BYTES,
            'blocked_sources': sorted(BLOCKED_SOURCES),
            'automatic_checks_are_not_approval': True,
            'creative_to_product_attribution': 'requires exact Shopify ad_id bridge; text/coupon stays influencer-level',
        },
        'summary': {
            'ads_evaluated': len(rows),
            'status_counts': counts,
            'eligible_for_email_image_now': 0,
            'human_approved': 0,
        },
        'creative_gate': rows,
        'approval_required_for': [
            'include_image_in_email_or_executive_report',
            'send_email_with_inline_creatives',
            'campaign_budget_creative_or_utm_change',
            'shopify_or_tiny_write',
            'customer_send_or_supplier_action',
            'cron_creation',
        ],
        'not_performed': [
            'live_meta_call', 'asset_download', 'gmail_send', 'klaviyo_send', 'whatsapp_send',
            'cron_creation', 'campaign_change', 'budget_change', 'creative_change', 'utm_change',
            'coupon_change', 'shopify_write', 'tiny_write', 'production_db_write'
        ],
    }


def build_md(payload: dict[str, Any]) -> str:
    lines = [
        '# LK OS Creative Visual Approval Gate, read-only',
        '',
        f"Generated at: `{payload['generated_at']}`",
        '',
        '## Status',
        '',
        '- Imagens em e-mail/relatório executivo: bloqueadas por padrão.',
        '- Critério: imagem precisa passar qualidade automática e ainda receber aprovação humana explícita.',
        '- Nenhuma imagem foi promovida para envio ou campanha.',
        '',
        '## Resumo',
        '',
        f"- Criativos avaliados: {payload['summary']['ads_evaluated']}",
        f"- Elegíveis para e-mail agora: {payload['summary']['eligible_for_email_image_now']}",
        f"- Aprovados por humano: {payload['summary']['human_approved']}",
        '',
        'Status counts:',
    ]
    for k, v in sorted(payload['summary']['status_counts'].items()):
        lines.append(f'- {k}: {v}')
    lines.extend(['', '## Fila de revisão visual', ''])
    for i, row in enumerate(payload['creative_gate'], 1):
        sig = row['platform_signal']
        asset = row['chosen_asset_sanitized']
        size = asset.get('size') or ['n/d', 'n/d']
        lines.extend([
            f"### {i}. {row['influencer']} | ad_id `{row['ad_id']}`",
            '',
            f"- Status: `{row['visual_gate_status']}`",
            f"- Requisitos/bloqueios: {', '.join(row['blockers_or_requirements'])}",
            f"- Sinal Meta: {sig.get('purchases')} compras, {brl(sig.get('value'))} valor, {brl(sig.get('spend'))} spend.",
            f"- Asset: fonte `{asset.get('source')}`, tamanho {size[0]}×{size[1]}, sha16 `{asset.get('sha16')}`.",
            f"- Próximo passo seguro: {row['safe_next_step']}.",
            '',
        ])
    lines.extend([
        '## O que não foi feito',
        '',
    ])
    for item in payload['not_performed']:
        lines.append(f'- {item}')
    return '\n'.join(lines) + '\n'


def main() -> None:
    payload = build_payload()
    md = build_md(payload)
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    OUT_MD.write_text(md, encoding='utf-8')
    BRAIN_DOC.write_text(md.replace('# LK OS Creative Visual Approval Gate, read-only', '# LK OS, Creative Visual Approval Gate read-only, 2026-05-11'), encoding='utf-8')
    print(json.dumps({'ok': True, 'summary': payload['summary'], 'json': str(OUT_JSON)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
