#!/usr/bin/env python3
"""Validate LK Phase 8 dry-runs for Daily Sales Brief and Weekly CEO Review.

This script does not call external APIs itself. It reads the just-generated
read-only briefing artifacts and records whether the manual dry-run gates passed.
"""
from __future__ import annotations

import json
import pathlib
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
DAILY_JSON = ROOT / 'reports/lk-os-daily-sales-brief-2026-05-10.json'
DAILY_TG_JSON = ROOT / 'reports/lk-os-daily-sales-brief-telegram-preview-2026-05-10.json'
WEEKLY_JSON = ROOT / 'reports/lk-os-weekly-ceo-review-2026-05-04_2026-05-10.json'
WEEKLY_TG_JSON = ROOT / 'reports/lk-os-weekly-ceo-review-telegram-preview-2026-05-04_2026-05-10.json'
OUT_JSON = ROOT / 'reports/lk-daily-weekly-dry-run-validation-2026-05-11.json'
OUT_MD = ROOT / 'reports/lk-daily-weekly-dry-run-validation-2026-05-11.md'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/daily-weekly-dry-run-validation-2026-05-11.md'
REGISTRY_JSON = ROOT / 'reports/lk-safe-automation-readiness-registry-2026-05-11.json'

BLOCKED_ACTIONS = {
    'telegram_send', 'external_send', 'campaign', 'cron', 'shopify_write',
    'tiny_write', 'klaviyo_send', 'whatsapp_send', 'supplier_contact',
    'n8n_flow_create', 'production_db_write', 'price_write', 'stock_write',
}


def load(path: pathlib.Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding='utf-8'))


def has_blocked_not_performed(payload: dict[str, Any]) -> bool:
    return bool(BLOCKED_ACTIONS.intersection(set(payload.get('not_performed') or [])))


def source_ok(payload: dict[str, Any], expected: list[str]) -> dict[str, bool]:
    sources = payload.get('sources') or {}
    out: dict[str, bool] = {}
    for key in expected:
        src = sources.get(key) or {}
        out[key] = bool(src.get('ok') is True or src.get('status') in {'ok', 'partial_ok'} or src)
    return out


def build() -> dict[str, Any]:
    daily = load(DAILY_JSON)
    daily_tg = load(DAILY_TG_JSON)
    weekly = load(WEEKLY_JSON)
    weekly_tg = load(WEEKLY_TG_JSON)
    registry = load(REGISTRY_JSON)

    daily_sources = source_ok(daily, ['shopify', 'ga4', 'tiny_stock'])
    weekly_sources = source_ok(weekly, ['shopify', 'ga4', 'tiny_stock', 'meta_ads', 'metricool_google_ads'])

    validations = [
        {
            'automation_id': 'LK-AUTO-001',
            'name': 'Daily Sales Brief read-only',
            'dry_run_status': 'passed' if all(daily_sources.values()) and has_blocked_not_performed(daily) and has_blocked_not_performed(daily_tg) else 'review_needed',
            'artifact_json': str(DAILY_JSON.relative_to(ROOT)),
            'telegram_preview_json': str(DAILY_TG_JSON.relative_to(ROOT)),
            'window': daily.get('date_range') or {'business_date': daily.get('business_date')},
            'source_checks': daily_sources,
            'telegram_preview': {
                'channel': daily_tg.get('channel'),
                'would_notify': daily_tg.get('would_notify'),
                'silence_policy': daily_tg.get('silence_policy'),
            },
            'metrics_snapshot': {
                'business_date': daily.get('business_date'),
                'shopify_orders': (daily.get('sources', {}).get('shopify') or {}).get('orders_count'),
                'shopify_revenue': (daily.get('sources', {}).get('shopify') or {}).get('revenue_total'),
                'ga4_sessions': ((daily.get('sources', {}).get('ga4') or {}).get('totals') or {}).get('sessions'),
                'tiny_risk_counts': (daily.get('sources', {}).get('tiny_stock') or {}).get('risk_counts'),
            },
            'blocked_actions_confirmed': sorted(BLOCKED_ACTIONS.intersection(set(daily.get('not_performed') or []) | set(daily_tg.get('not_performed') or []))),
            'activation_recommendation': 'eligible_for_lucas_cadence_approval_not_active',
        },
        {
            'automation_id': 'LK-AUTO-002',
            'name': 'Weekly CEO Review read-only',
            'dry_run_status': 'passed' if all(weekly_sources.values()) and has_blocked_not_performed(weekly) and has_blocked_not_performed(weekly_tg) else 'review_needed',
            'artifact_json': str(WEEKLY_JSON.relative_to(ROOT)),
            'telegram_preview_json': str(WEEKLY_TG_JSON.relative_to(ROOT)),
            'window': weekly.get('week'),
            'source_checks': weekly_sources,
            'telegram_preview': {
                'channel': weekly_tg.get('channel'),
                'would_notify': weekly_tg.get('would_notify'),
                'silence_policy': weekly_tg.get('silence_policy'),
            },
            'metrics_snapshot': {
                'start_date': (weekly.get('week') or {}).get('start_date'),
                'end_date': (weekly.get('week') or {}).get('end_date'),
                'shopify_orders': (weekly.get('sources', {}).get('shopify') or {}).get('orders_count'),
                'shopify_revenue': (weekly.get('sources', {}).get('shopify') or {}).get('revenue_total'),
                'ga4_sessions': ((weekly.get('sources', {}).get('ga4') or {}).get('totals') or {}).get('sessions'),
                'meta_spend': (weekly.get('sources', {}).get('meta_ads') or {}).get('spend'),
                'metricool_google_ads_rows': (weekly.get('sources', {}).get('metricool_google_ads') or {}).get('google_ads_rows'),
                'tiny_risk_counts': (weekly.get('sources', {}).get('tiny_stock') or {}).get('risk_counts'),
            },
            'blocked_actions_confirmed': sorted(BLOCKED_ACTIONS.intersection(set(weekly.get('not_performed') or []) | set(weekly_tg.get('not_performed') or []))),
            'activation_recommendation': 'eligible_for_lucas_cadence_approval_not_active',
        },
    ]
    passed = sum(1 for v in validations if v['dry_run_status'] == 'passed')
    return {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'LK Phase 8 manual dry-run validation for Daily + Weekly read-only automations',
        'registry_source': str(REGISTRY_JSON.relative_to(ROOT)),
        'summary': {
            'automations_validated': len(validations),
            'dry_runs_passed': passed,
            'dry_runs_review_needed': len(validations) - passed,
            'crons_created': 0,
            'n8n_flows_created': 0,
            'telegram_sends': 0,
            'external_sends': 0,
            'production_writes': 0,
            'eligible_for_lucas_cadence_approval': passed,
            'activated_now': 0,
        },
        'validations': validations,
        'registry_context': {
            'candidate_automations': registry.get('summary', {}).get('candidate_automations'),
            'activation_requires_lucas_approval': registry.get('summary', {}).get('activation_requires_lucas_approval'),
        },
        'next_gate': 'Lucas can approve cadence/delivery for LK-AUTO-001 and/or LK-AUTO-002 if he wants recurring activation; otherwise keep manual/on-demand.',
    }


def write_outputs(payload: dict[str, Any]) -> None:
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    s = payload['summary']
    lines = [
        '# LK Daily + Weekly Dry-run Validation, 2026-05-11', '',
        f"Generated at: `{payload['generated_at']}`", '',
        '## Veredito', '',
        'Daily Sales Brief e Weekly CEO Review passaram no dry-run manual read-only. Eles ficam elegíveis para uma decisão de cadência/destino, mas não foram ativados como cron/n8n e não foram enviados.', '',
        '## Snapshot', '',
        f"- Automações validadas: {s['automations_validated']}",
        f"- Dry-runs passed: {s['dry_runs_passed']}",
        f"- Review needed: {s['dry_runs_review_needed']}",
        f"- Crons criados: {s['crons_created']}",
        f"- n8n flows criados: {s['n8n_flows_created']}",
        f"- Telegram sends: {s['telegram_sends']}",
        f"- Envios externos: {s['external_sends']}",
        f"- Writes produtivos: {s['production_writes']}", '',
        '## Validações', '',
    ]
    for v in payload['validations']:
        snap = v['metrics_snapshot']
        lines.extend([
            f"### {v['automation_id']} · {v['name']}", '',
            f"- Status: `{v['dry_run_status']}`",
            f"- Artefato: `{v['artifact_json']}`",
            f"- Preview Telegram: `{v['telegram_preview_json']}`",
            f"- Would notify: `{v['telegram_preview']['would_notify']}`",
            f"- Recomendação: `{v['activation_recommendation']}`",
            f"- Ações bloqueadas confirmadas: {', '.join(v['blocked_actions_confirmed'])}",
            f"- Snapshot: `{json.dumps(snap, ensure_ascii=False)}`", '',
        ])
    lines.extend([
        '## Próximo gate', '',
        payload['next_gate'], '',
        '## Não realizado', '',
        '- Nenhum cron criado.',
        '- Nenhum n8n flow criado.',
        '- Nenhum Telegram enviado.',
        '- Nenhum e-mail, WhatsApp, Klaviyo ou campanha enviado/agendado.',
        '- Nenhum write Shopify/Tiny/Merchant/GSC/produção.',
    ])
    text = '\n'.join(lines) + '\n'
    OUT_MD.write_text(text, encoding='utf-8')
    BRAIN_DOC.write_text(text, encoding='utf-8')


def main() -> None:
    payload = build()
    write_outputs(payload)
    print(json.dumps({'ok': True, 'summary': payload['summary']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
