#!/usr/bin/env python3
"""LK CRM Phase 5 next decision router, read-only.

Consolidates the CRM/RFM/Recompra state after the P1 Klaviyo draft and prior
WhatsApp concierge execution into a safe decision router for Lucas. It does not
send, schedule, create lists/campaigns, call APIs, or expose PII.
"""
from __future__ import annotations

import json
import pathlib
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
APPROVAL_PACKET = ROOT / 'reports/lk-phase5-p1-final-approval-packet-2026-05-11.json'
KLAVIYO_OBJECTS = ROOT / 'reports/lk-phase5-p1-klaviyo-klaviyo-objects-2026-05-11.json'
WHATSAPP_AUDIT = ROOT / 'reports/lk-phase5-p1-whatsapp-evolution-send-2026-05-11.json'
OUT_JSON = ROOT / 'reports/lk-crm-phase5-next-decision-router-2026-05-11.json'
OUT_MD = ROOT / 'reports/lk-crm-phase5-next-decision-router-2026-05-11.md'
BRAIN_DOC = ROOT / 'areas/lk/sub-areas/crm/rotinas/phase5-next-decision-router-readonly-2026-05-11.md'


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_json(path: pathlib.Path) -> dict[str, Any]:
    if not path.exists():
        return {'_missing': True, '_path': str(path.relative_to(ROOT))}
    return json.loads(path.read_text(encoding='utf-8'))


def route_klaviyo_p1(klaviyo: dict[str, Any]) -> dict[str, Any]:
    k = klaviyo.get('klaviyo') or {}
    if klaviyo.get('_missing'):
        status = 'needs_data'
        blockers = ['klaviyo_objects_report_missing']
    else:
        blockers = []
        if k.get('campaign_status') != 'Draft':
            blockers.append('campaign_not_draft')
        if k.get('campaign_scheduled_at') is not None or k.get('campaign_send_time') is not None:
            blockers.append('campaign_has_schedule_or_send_time')
        if k.get('profile_import_failed_count') not in (0, None):
            blockers.append('profile_import_failures')
        blockers.append('ui_template_selection_unverified')
        blockers.append('lucas_final_send_approval_missing')
        status = 'needs_manual_ui_verification_before_send'
    return {
        'decision_id': 'crm_phase5_p1_klaviyo_draft',
        'title': 'P1 Klaviyo loja física, manter draft até revisão final',
        'current_status': status,
        'recommended_next_step': 'Confirmar no painel Klaviyo que o template aprovado está selecionado no campaign message; depois pedir aprovação explícita para enviar/agendar ou manter pausado.',
        'allowed_decision_values': ['keep_draft', 'verify_ui_only', 'approve_send_later_with_final_checklist', 'pause_or_archive'],
        'blocked_until': blockers,
        'objects_sanitized': {
            'list_id': k.get('list_id'),
            'template_id': k.get('template_id'),
            'campaign_id': k.get('campaign_id'),
            'campaign_message_id': k.get('campaign_message_id'),
            'campaign_status': k.get('campaign_status'),
            'scheduled_at': k.get('campaign_scheduled_at'),
            'send_time': k.get('campaign_send_time'),
            'profiles_submitted': (klaviyo.get('counts') or {}).get('approved_profiles_submitted'),
            'profile_import_failed_count': k.get('profile_import_failed_count'),
        },
        'execution_allowed_now': False,
        'source_labels': ['manual_approval', 'platform_signal'],
    }


def route_whatsapp_p1(whatsapp: dict[str, Any]) -> dict[str, Any]:
    counts = whatsapp.get('counts') or {}
    sent = counts.get('sent') or 0
    failed = counts.get('failed') or 0
    return {
        'decision_id': 'crm_phase5_p1_whatsapp_concierge_status',
        'title': 'P1 WhatsApp concierge, pós-execução e bloqueio de repetição',
        'current_status': 'executed_partial_prior_approval_context' if sent else 'no_send_recorded',
        'recommended_next_step': 'Não reenviar automaticamente. Usar auditoria privada para evitar duplicidade; se avançar, preparar somente follow-up preview com dedupe e validação de número.',
        'allowed_decision_values': ['hold_no_followup', 'prepare_followup_preview_only', 'prepare_failure_resolution_preview'],
        'public_counts': {
            'sent': sent,
            'failed': failed,
            'deduped_phone_recipients': counts.get('deduped_phone_recipients'),
        },
        'blocked_until': ['new_lucas_approval_for_any_followup', 'dedupe_against_private_audit', 'validate_failed_number_before_retry'],
        'execution_allowed_now': False,
        'source_labels': ['manual_approval'],
    }


def route_p2_candidates(packet: dict[str, Any]) -> dict[str, Any]:
    groups = packet.get('groups') or []
    p2_like = []
    held = []
    for group in groups:
        status = group.get('status')
        segment = group.get('segment')
        if status == 'HOLD':
            held.append(group)
        elif segment not in {'Champions/VIP', 'Novo alto potencial'}:
            p2_like.append(group)
    # The P1 packet mostly contains P1-ready groups; P2 requires a fresh queue, not reuse.
    return {
        'decision_id': 'crm_phase5_p2_or_reactivation_preview',
        'title': 'Preparar P2 ou reativação fria como preview, não campanha',
        'current_status': 'needs_preview_from_rfm_queue',
        'recommended_next_step': 'Gerar P2 read-only a partir do RFM/local SQL, com Tiny stock gate e copy preview. Não reutilizar automaticamente a fila P1.',
        'allowed_decision_values': ['prepare_p2_preview_only', 'prepare_reactivation_preview_only', 'defer_p2'],
        'p1_packet_context': {
            'ready_recipients_same_size_stock': (packet.get('totals') or {}).get('ready_recipients_same_size_stock'),
            'blocked_by_stock_or_mapping': (packet.get('totals') or {}).get('blocked_by_stock_or_mapping'),
            'ready_groups': (packet.get('totals') or {}).get('ready_groups'),
            'hold_groups': (packet.get('totals') or {}).get('hold_groups'),
            'held_groups_from_p1_packet': len(held),
        },
        'blocked_until': ['fresh_p2_segment_preview', 'tiny_stock_gate', 'lucas_approval_before_any_list_campaign_or_send'],
        'execution_allowed_now': False,
        'source_labels': ['fact_shopify', 'fact_tiny_stock', 'derived_reconciliation'],
    }


def route_phase1_data_spine() -> dict[str, Any]:
    return {
        'decision_id': 'crm_phase5_return_to_data_spine_option',
        'title': 'Voltar para Fase 1 Data Spine, auditoria de base antes de CRM P2',
        'current_status': 'safe_readonly_option',
        'recommended_next_step': 'Se Lucas preferir reduzir risco antes de P2, atualizar snapshot read-only de Data Spine/RFM e freshness sem campanha ou envio.',
        'allowed_decision_values': ['refresh_data_spine_readonly', 'defer_data_spine'],
        'blocked_until': [],
        'execution_allowed_now': True,
        'source_labels': ['fact_shopify', 'fact_tiny_stock', 'fact_ga4', 'platform_signal'],
    }


def build_payload() -> dict[str, Any]:
    packet = load_json(APPROVAL_PACKET)
    klaviyo = load_json(KLAVIYO_OBJECTS)
    whatsapp = load_json(WHATSAPP_AUDIT)
    decisions = [
        route_klaviyo_p1(klaviyo),
        route_whatsapp_p1(whatsapp),
        route_p2_candidates(packet),
        route_phase1_data_spine(),
    ]
    return {
        'generated_at': now_utc(),
        'scope': 'LK CRM Phase 5 next decision router, read-only',
        'read_only': True,
        'sources': {
            'p1_approval_packet': str(APPROVAL_PACKET.relative_to(ROOT)),
            'klaviyo_objects': str(KLAVIYO_OBJECTS.relative_to(ROOT)),
            'whatsapp_audit_public': str(WHATSAPP_AUDIT.relative_to(ROOT)),
        },
        'summary': {
            'decision_options': len(decisions),
            'execution_allowed_now': sum(1 for d in decisions if d['execution_allowed_now']),
            'external_actions_allowed_now': 0,
            'recommended_safe_default': 'keep_p1_klaviyo_draft_and_prepare_p2_preview_only_or_refresh_data_spine_readonly',
        },
        'decision_router': decisions,
        'global_blockers': [
            'No Klaviyo send/schedule without final Lucas approval and UI template verification.',
            'No WhatsApp follow-up without fresh approval, dedupe and number validation.',
            'No P2 campaign/list creation before read-only preview and Tiny stock gate.',
            'No deep Klaviyo UI link unless verified in logged-in panel.',
        ],
        'not_performed': [
            'klaviyo_send', 'klaviyo_schedule', 'klaviyo_list_or_campaign_create', 'whatsapp_send',
            'email_send', 'sms_send', 'customer_tag_or_note', 'shopify_write', 'tiny_write',
            'supabase_write', 'production_db_write', 'cron_creation', 'live_api_call'
        ],
    }


def md(payload: dict[str, Any]) -> str:
    lines = [
        '# LK CRM Phase 5 Next Decision Router, read-only',
        '',
        f"Generated at: `{payload['generated_at']}`",
        '',
        '## Veredito',
        '',
        'Fase 5 está consolidada como pendente seguro: P1 Klaviyo fica em Draft, WhatsApp P1 não deve ser repetido automaticamente, e o próximo avanço seguro é P2 preview ou refresh read-only de Data Spine/RFM.',
        '',
        '## Resumo',
        '',
        f"- Opções de decisão: {payload['summary']['decision_options']}",
        f"- Execuções externas liberadas agora: {payload['summary']['external_actions_allowed_now']}",
        f"- Opções read-only liberadas agora: {payload['summary']['execution_allowed_now']}",
        '',
        '## Decision router',
        '',
    ]
    for d in payload['decision_router']:
        lines.extend([
            f"### {d['decision_id']}",
            '',
            f"- Título: {d['title']}",
            f"- Status: `{d['current_status']}`",
            f"- Próximo passo seguro: {d['recommended_next_step']}",
            f"- Execução liberada agora: `{d['execution_allowed_now']}`",
            f"- Decisões aceitas: {', '.join(d['allowed_decision_values'])}",
            f"- Bloqueios: {', '.join(d['blocked_until']) if d['blocked_until'] else 'nenhum para análise read-only'}",
            f"- Source labels: {', '.join(d['source_labels'])}",
            '',
        ])
    lines.extend(['## Bloqueios globais', ''])
    for b in payload['global_blockers']:
        lines.append(f'- {b}')
    lines.extend(['', '## O que não foi feito', ''])
    for n in payload['not_performed']:
        lines.append(f'- {n}')
    return '\n'.join(lines) + '\n'


def main() -> None:
    payload = build_payload()
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    text = md(payload)
    OUT_MD.write_text(text, encoding='utf-8')
    BRAIN_DOC.write_text(text.replace('# LK CRM Phase 5 Next Decision Router, read-only', '# LK CRM, Phase 5 Next Decision Router read-only, 2026-05-11'), encoding='utf-8')
    print(json.dumps({'ok': True, 'summary': payload['summary'], 'json': str(OUT_JSON)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
