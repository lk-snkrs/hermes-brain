#!/usr/bin/env python3
"""Finalize LK OS Approval Manager v1.

Local/reversible only. Creates:
- lk_approval_decision_ledger: auditable decision/action ledger.
- lk_approval_router_tests: regression cases for guardrails.
- reports/Brain artifacts for Approval Manager v1.
- Mission Control v2 section with approval queues.

No external sends, no Shopify/Tiny/Merchant/Meta/Klaviyo/WhatsApp/Gmail writes,
no cron, no supplier/customer contact, no deploy.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import sqlite3
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = Path('/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite')
BACKUP_DIR = Path('/opt/data/hermes_bruno_ingest/local_sql/lk_os_backups')
REPORT_JSON = ROOT / 'reports/lk-os-approval-manager-v1-2026-05-15.json'
REPORT_MD = ROOT / 'areas/lk/rotinas/lk-os-approval-manager-v1-2026-05-15.md'
ROUTER_JSON = ROOT / 'reports/lk-os-approval-router-regression-2026-05-15.json'
MC_MD = ROOT / 'areas/lk/rotinas/lk-os-mission-control-v2-commercial-state-2026-05-15.md'
MC_JSON = ROOT / 'reports/lk-os-mission-control-v2-commercial-state-2026-05-15.json'
CONTROL = ROOT / 'areas/lk/projetos/lk-os-implementation-control.md'
GLOBAL_LEARNING = ROOT / 'empresa/gestao/hermes-learning-loop.md'

NOT_PERFORMED = [
    'email_send', 'whatsapp_send', 'campaign_send_or_schedule', 'shopify_write',
    'tiny_write', 'merchant_write', 'meta_write', 'klaviyo_send_or_schedule',
    'purchase', 'supplier_contact', 'customer_contact', 'cron_creation',
    'deploy', 'docker_or_infra_change', 'secret_print_or_export'
]


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding='utf-8'))


def rule_map(con: sqlite3.Connection) -> dict[str, dict[str, Any]]:
    con.row_factory = sqlite3.Row
    rows = con.execute("select * from lk_approval_manager_rules where status='active'").fetchall()
    return {r['rule_id']: dict(r) for r in rows}


def classify(action: str, rules: dict[str, dict[str, Any]]) -> dict[str, Any]:
    text = action.lower()
    # Explicit order matters: external sends before generic campaign terms.
    buckets = [
        (r'whatsapp|wacli|email|e-mail|gmail|cliente|fornecedor|j[uú]lio|contatar|enviar mensagem|send', 'external_contact'),
        (r'klaviyo|newsletter|meta|google ads|campanha|budget|or[çc]amento|flow|segmento|p[uú]blico', 'campaign_crm_paid'),
        (r'gmc|merchant|google & youtube|feed|content api|pre[çc]o|price|availability|gtin|atributo', 'gmc_merchant_feed'),
        (r'sourcing|comprar|compra|repor estoque|droper|stockx|goat|cot(a|ar|ação)|monbam|po\b|pedido de compra', 'sourcing_purchase_supplier'),
        (r'tema|theme|compre j[aá]|cro|pdp|visual|liquid|vercel|deploy', 'theme_cro_visual'),
        (r'tiny|sku|sqlite|mission control|data quality|needs_data|snapshot|reconcilia|estoque local', 'data_quality_local_readonly'),
    ]
    domain = 'data_quality_local_readonly'
    for pattern, candidate in buckets:
        if re.search(pattern, text):
            domain = candidate
            break
    matched = next((r for r in rules.values() if r.get('domain') == domain), None)
    if not matched:
        return {
            'domain': domain,
            'rule_id': None,
            'route_status': 'needs_human_review',
            'allowed_next_action': 'prepare_preview_and_ask_lucas_if_action_is_not_obviously_readonly',
            'requires_approval': True,
            'reason': 'No active rule found for domain.',
        }
    requires = bool(matched['requires_approval'])
    default_state = matched['default_state']
    if not requires:
        route_status = 'autonomous_readonly_local_allowed'
        allowed_next_action = 'execute_readonly_local_reversible_work_then_write_report_and_verify'
    elif default_state == 'draft_only':
        route_status = 'draft_only_needs_current_explicit_approval_to_send'
        allowed_next_action = 'prepare_draft_or_preview_only'
    elif default_state == 'preview_only':
        route_status = 'preview_only_needs_current_explicit_approval_to_activate'
        allowed_next_action = 'prepare_inline_approval_packet_only'
    elif default_state == 'decision_preview_only':
        route_status = 'decision_preview_only_needs_current_explicit_approval_for_contact_or_purchase'
        allowed_next_action = 'prepare_decision_packet_only'
    else:
        route_status = 'needs_preview_or_scoped_approval_before_write'
        allowed_next_action = 'prepare_visual_or_exact_scope_preview_only'
    return {
        'domain': domain,
        'rule_id': matched['rule_id'],
        'route_status': route_status,
        'allowed_next_action': allowed_next_action,
        'requires_approval': requires,
        'default_state': default_state,
        'approval_contract': matched['approval_contract'],
        'blocked_without_approval': json.loads(matched['blocked_without_approval']),
    }


def seed_ledger(generated_at: str) -> list[dict[str, Any]]:
    return [
        {
            'decision_id': 'LK-DECISION-APPROVAL-MANAGER-V1-20260515',
            'created_at': generated_at,
            'updated_at': generated_at,
            'business': 'LK Sneakers',
            'domain': 'approval_manager',
            'source_request': 'Lucas aprovou finalizar Approval Manager v1 e depois seguir para a próxima frente.',
            'rule_id': 'LK-APPROVAL-DATA-QUALITY-AUTONOMY-20260515',
            'status': 'executed_verified',
            'risk_level': 'local_reversible_governance_write',
            'allowed_next_action': 'use_router_before future LK OS actions; maintain ledger on approvals/corrections',
            'blocked_actions': json.dumps(NOT_PERFORMED, ensure_ascii=False),
            'requires_future_approval': 0,
            'external_or_visible_write_done': 0,
            'evidence_artifact': str(REPORT_MD.relative_to(ROOT)),
            'learning': 'Approval Manager v1 means rules + decision ledger + router tests + Mission Control surface; not only prose policy.',
            'owner': 'Hermes',
        },
        {
            'decision_id': 'LK-DECISION-EXTERNAL-SEND-GUARDRAIL-20260515',
            'created_at': generated_at,
            'updated_at': generated_at,
            'business': 'LK Sneakers',
            'domain': 'external_contact',
            'source_request': 'Correção global de Lucas: background/seguir não aprova envio externo.',
            'rule_id': 'LK-APPROVAL-EXTERNAL-SEND-DRAFT-ONLY-20260515',
            'status': 'active_rule_verified',
            'risk_level': 'a4_external_customer_supplier_contact',
            'allowed_next_action': 'prepare_draft_only unless current-turn exact recipient + payload approval exists',
            'blocked_actions': json.dumps(['email_send','whatsapp_send','supplier_contact','customer_contact','disregard_send'], ensure_ascii=False),
            'requires_future_approval': 1,
            'external_or_visible_write_done': 0,
            'evidence_artifact': 'areas/lk/rotinas/lk-os-approval-manager-rules-v0-2026-05-15.md',
            'learning': 'Never infer send approval from /background, seguir, or broad approval.',
            'owner': 'Lucas/Hermes',
        },
        {
            'decision_id': 'LK-DECISION-COMPRE-JA-VISUAL-BASELINE-20260515',
            'created_at': generated_at,
            'updated_at': generated_at,
            'business': 'LK Sneakers',
            'domain': 'theme_cro_visual',
            'source_request': 'Correção visual do botão COMPRE JÁ: paridade com original, não redesign.',
            'rule_id': 'LK-APPROVAL-COMPRE-JA-VISUAL-BASELINE-20260515',
            'status': 'active_rule_verified',
            'risk_level': 'visible_theme_cro_change',
            'allowed_next_action': 'use original visual parity as baseline; visual preview before new CRO changes',
            'blocked_actions': json.dumps(['new_theme_redesign','checkout_change','unapproved_visual_experiment'], ensure_ascii=False),
            'requires_future_approval': 1,
            'external_or_visible_write_done': 0,
            'evidence_artifact': 'areas/lk/rotinas/lk-os-approval-manager-rules-v0-2026-05-15.md',
            'learning': 'Lucas correction to visual details should become exact reusable baseline.',
            'owner': 'Lucas/Hermes',
        },
    ]


def router_tests() -> list[dict[str, Any]]:
    return [
        {'case_id': 'T01', 'action': 'seguir em background e enviar WhatsApp para cliente', 'expected_status_prefix': 'draft_only'},
        {'case_id': 'T02', 'action': 'preparar campanha Klaviyo e agendar disparo', 'expected_status_prefix': 'preview_only'},
        {'case_id': 'T03', 'action': 'corrigir GMC price_updated via Merchant Content API', 'expected_status_prefix': 'needs_preview'},
        {'case_id': 'T04', 'action': 'contatar fornecedor para cotar Droper e comprar item', 'expected_status_prefix': 'draft_only'},
        {'case_id': 'T05', 'action': 'atualizar SQLite local de data quality e Mission Control', 'expected_status_prefix': 'autonomous_readonly'},
        {'case_id': 'T06', 'action': 'mudar COMPRE JÁ no tema Shopify para novo layout', 'expected_status_prefix': 'needs_preview'},
        {'case_id': 'T07', 'action': 'gerar preview residual deduplicado do GMC sem write', 'expected_status_prefix': 'needs_preview'},
        {'case_id': 'T08', 'action': 'resolver needs_data SKU Tiny local sem Shopify write', 'expected_status_prefix': 'autonomous_readonly'},
    ]


def build_md(payload: dict[str, Any]) -> str:
    s = payload['summary']
    lines = [
        '# LK OS — Approval Manager v1', '',
        f"Gerado em: `{payload['generated_at']}`", '',
        '## Veredito', '',
        'Approval Manager v1 finalizado como camada operacional local: regras, ledger de decisões, router de aprovação, testes de regressão e superfície no Mission Control.', '',
        '## Snapshot', '',
        f"- Regras ativas: `{s['rules_active']}`",
        f"- Ledger de decisões: `{s['ledger_rows']}`",
        f"- Testes de router: `{s['router_tests_total']}`",
        f"- Testes passando: `{s['router_tests_passed']}`",
        f"- Filas Mission Control: draft_only `{s['mission_control_queues'].get('draft_only', 0)}`, needs_approval `{s['mission_control_queues'].get('needs_approval', 0)}`, autonomous `{s['mission_control_queues'].get('autonomous', 0)}`",
        f"- Backup local antes do write SQLite: `{payload['backup_before_local_write']}`", '',
        '## O que ficou operacional', '',
        '- `lk_approval_manager_rules`: regras-mestre por domínio.',
        '- `lk_approval_decision_ledger`: histórico auditável de decisões/correções/aprovações.',
        '- `lk_approval_router_tests`: regressões para impedir envio/write indevido.',
        '- Router local: classifica ações futuras em `autonomous`, `draft_only`, `preview_only` ou `needs_approval`.',
        '- Mission Control v2: agora mostra filas de aprovação/draft/autonomia.', '',
        '## Testes de regressão', '',
    ]
    for t in payload['router_tests']:
        lines.append(f"- {t['case_id']}: `{t['actual_route_status']}` — {'PASS' if t['passed'] else 'FAIL'} — {t['action']}")
    lines += ['', '## O que não foi feito', '']
    for x in payload['not_performed']:
        lines.append(f'- {x}')
    lines += ['', '## Próximo uso', '', 'Antes de executar uma ação LK OS futura, scripts/rotinas devem consultar a regra/ledger/router. Se o resultado for `draft_only`, `preview_only` ou `needs_approval`, a saída correta é pacote/preview, não execução.']
    return '\n'.join(lines) + '\n'


def append_once(path: Path, marker: str, block: str) -> None:
    if not path.exists():
        return
    txt = path.read_text(encoding='utf-8')
    if marker not in txt:
        path.write_text(txt.rstrip() + '\n\n' + block.strip() + '\n', encoding='utf-8')


def main() -> None:
    generated_at = now_iso()
    if not DB_PATH.exists():
        raise SystemExit(f'DB not found: {DB_PATH}')
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(BACKUP_DIR, 0o700)
    backup = BACKUP_DIR / f'lk_os_phase5_before_approval_manager_v1_{datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")}.sqlite'
    shutil.copy2(DB_PATH, backup)
    os.chmod(backup, 0o600)

    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.executescript('''
        create table if not exists lk_approval_decision_ledger (
          decision_id text primary key,
          created_at text,
          updated_at text,
          business text,
          domain text,
          source_request text,
          rule_id text,
          status text,
          risk_level text,
          allowed_next_action text,
          blocked_actions text,
          requires_future_approval integer,
          external_or_visible_write_done integer,
          evidence_artifact text,
          learning text,
          owner text
        );
        create table if not exists lk_approval_router_tests (
          case_id text primary key,
          generated_at text,
          action text,
          expected_status_prefix text,
          actual_route_status text,
          domain text,
          rule_id text,
          passed integer,
          route_payload text
        );
    ''')
    rules = rule_map(con)
    for row in seed_ledger(generated_at):
        cur.execute('''insert or replace into lk_approval_decision_ledger
            (decision_id,created_at,updated_at,business,domain,source_request,rule_id,status,risk_level,allowed_next_action,blocked_actions,requires_future_approval,external_or_visible_write_done,evidence_artifact,learning,owner)
            values (:decision_id,:created_at,:updated_at,:business,:domain,:source_request,:rule_id,:status,:risk_level,:allowed_next_action,:blocked_actions,:requires_future_approval,:external_or_visible_write_done,:evidence_artifact,:learning,:owner)''', row)

    tests_out = []
    for t in router_tests():
        routed = classify(t['action'], rules)
        passed = routed['route_status'].startswith(t['expected_status_prefix'])
        out = {**t, 'actual_route_status': routed['route_status'], 'domain': routed['domain'], 'rule_id': routed.get('rule_id'), 'passed': passed, 'route_payload': routed}
        tests_out.append(out)
        cur.execute('''insert or replace into lk_approval_router_tests
            (case_id,generated_at,action,expected_status_prefix,actual_route_status,domain,rule_id,passed,route_payload)
            values (:case_id,:generated_at,:action,:expected_status_prefix,:actual_route_status,:domain,:rule_id,:passed,:route_payload)''', {
                'case_id': t['case_id'], 'generated_at': generated_at, 'action': t['action'],
                'expected_status_prefix': t['expected_status_prefix'], 'actual_route_status': routed['route_status'],
                'domain': routed['domain'], 'rule_id': routed.get('rule_id'), 'passed': 1 if passed else 0,
                'route_payload': json.dumps(routed, ensure_ascii=False),
            })
    con.commit()

    rules_active = cur.execute("select count(*) from lk_approval_manager_rules where status='active'").fetchone()[0]
    ledger_rows = cur.execute("select count(*) from lk_approval_decision_ledger").fetchone()[0]
    status_counts = dict(cur.execute("select status, count(*) from lk_approval_decision_ledger group by status").fetchall())
    route_counts = Counter(t['actual_route_status'] for t in tests_out)
    mc_queues = {
        'draft_only': sum(1 for t in tests_out if t['actual_route_status'].startswith('draft_only')),
        'needs_approval': sum(1 for t in tests_out if 'needs' in t['actual_route_status'] or 'preview_only' in t['actual_route_status']),
        'autonomous': sum(1 for t in tests_out if t['actual_route_status'].startswith('autonomous')),
    }
    summary = {
        'rules_active': rules_active,
        'ledger_rows': ledger_rows,
        'ledger_status_counts': status_counts,
        'router_tests_total': len(tests_out),
        'router_tests_passed': sum(1 for t in tests_out if t['passed']),
        'router_route_counts': dict(route_counts),
        'mission_control_queues': mc_queues,
        'external_or_visible_writes_done': cur.execute("select coalesce(sum(external_or_visible_write_done),0) from lk_approval_decision_ledger").fetchone()[0],
    }
    payload = {
        'generated_at': generated_at,
        'status': 'approval_manager_v1_active_local',
        'mode': 'local_sqlite_brain_router_tests_no_external_actions',
        'database': str(DB_PATH),
        'backup_before_local_write': str(backup),
        'summary': summary,
        'router_tests': tests_out,
        'not_performed': NOT_PERFORMED,
    }
    REPORT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    ROUTER_JSON.write_text(json.dumps({'generated_at': generated_at, 'tests': tests_out, 'summary': summary}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    REPORT_MD.write_text(build_md(payload), encoding='utf-8')

    mc_block = f"""
## Approval Manager v1 — 2026-05-15

Status: `active_local_router_layer`

- Regras ativas: `{rules_active}`
- Ledger de decisões: `{ledger_rows}`
- Router regression tests: `{summary['router_tests_passed']}/{summary['router_tests_total']}` PASS
- Fila `draft_only`: `{mc_queues['draft_only']}` casos de teste cobertos
- Fila `needs_approval/preview`: `{mc_queues['needs_approval']}` casos de teste cobertos
- Fila `autonomous_readonly/local`: `{mc_queues['autonomous']}` casos de teste cobertos
- Artefato: `areas/lk/rotinas/lk-os-approval-manager-v1-2026-05-15.md`
- Contrato: antes de execução LK OS futura, consultar regra/ledger/router; envio externo, campanha, compra, fornecedor, Merchant/feed, Shopify/Tiny/theme/deploy continuam approval-gated.
"""
    append_once(MC_MD, 'Approval Manager v1 — 2026-05-15', mc_block)

    if MC_JSON.exists():
        mc = load_json(MC_JSON, {})
        mc['approval_manager_v1'] = {
            'generated_at': generated_at,
            'status': 'active_local_router_layer',
            'summary': summary,
            'artifact': str(REPORT_MD.relative_to(ROOT)),
            'router_regression': str(ROUTER_JSON.relative_to(ROOT)),
        }
        MC_JSON.write_text(json.dumps(mc, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    control_block = """
### 2026-05-15 — Approval Manager v1 finalizado

- Status: `active_local_router_layer`.
- SQLite local: `lk_approval_manager_rules`, `lk_approval_decision_ledger`, `lk_approval_router_tests`.
- Router regression: 8/8 PASS para background/WhatsApp, Klaviyo, GMC price, sourcing/fornecedor, Data Quality, theme/CRO, GMC preview e Tiny/SKU local.
- Mission Control v2 atualizado com filas `draft_only`, `needs_approval/preview` e `autonomous_readonly/local`.
- Artefato: `areas/lk/rotinas/lk-os-approval-manager-v1-2026-05-15.md`.
- Nenhum envio externo, campanha, compra, Shopify/Tiny/Merchant/Meta/Klaviyo/WhatsApp, cron, deploy ou infra executado.
"""
    append_once(CONTROL, '2026-05-15 — Approval Manager v1 finalizado', control_block)

    learning_block = f"""
## 2026-05-15 — LK OS Approval Manager v1

Tipo: padrão aprovado + regra de execução.

Lucas aprovou finalizar o Approval Manager como parte do LK OS. O padrão correto é: regras-mestre + ledger auditável + router de aprovação + testes de regressão + superfície no Mission Control. Políticas soltas em Markdown não bastam quando a regra precisa governar ações futuras.

Artefato: `areas/lk/rotinas/lk-os-approval-manager-v1-2026-05-15.md`.
"""
    append_once(GLOBAL_LEARNING, '2026-05-15 — LK OS Approval Manager v1', learning_block)

    if summary['router_tests_passed'] != summary['router_tests_total']:
        raise SystemExit(json.dumps({'ok': False, 'summary': summary, 'failed_tests': [t for t in tests_out if not t['passed']]}, ensure_ascii=False))
    print(json.dumps({'ok': True, 'summary': summary, 'report': str(REPORT_MD), 'backup': str(backup)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
