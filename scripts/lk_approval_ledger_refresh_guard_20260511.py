#!/usr/bin/env python3
"""LK-AUTO-004 Approval Learning Ledger refresh guard.

Manual/post-action only. This script runs the ledger generator, validates routing
invariants, and writes a readiness report. It does not create crons, approvals,
external sends, or production writes.
"""
from __future__ import annotations

import json
import pathlib
import subprocess
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
LEDGER_SCRIPT = ROOT / 'scripts/lk_os_approval_learning_ledger_20260511.py'
LEDGER_JSON = ROOT / 'reports/lk-os-approval-learning-ledger-2026-05-11.json'
OUT_JSON = ROOT / 'reports/lk-approval-ledger-refresh-guard-2026-05-11.json'
OUT_MD = ROOT / 'reports/lk-approval-ledger-refresh-guard-2026-05-11.md'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/approval-ledger-refresh-guard-2026-05-11.md'


def run_ledger() -> dict[str, Any]:
    before = json.loads(LEDGER_JSON.read_text(encoding='utf-8')) if LEDGER_JSON.exists() else None
    result = subprocess.run(
        ['python3', str(LEDGER_SCRIPT)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        timeout=120,
        check=False,
    )
    if result.returncode != 0:
        return {
            'ok': False,
            'stage': 'ledger_generation',
            'returncode': result.returncode,
            'stdout_tail': result.stdout[-2000:],
            'stderr_tail': result.stderr[-2000:],
            'before_summary': before.get('summary') if before else None,
        }
    after = json.loads(LEDGER_JSON.read_text(encoding='utf-8'))
    return {
        'ok': True,
        'stage': 'ledger_generation',
        'returncode': result.returncode,
        'stdout_tail': result.stdout[-2000:],
        'stderr_tail': result.stderr[-2000:],
        'before_summary': before.get('summary') if before else None,
        'after': after,
    }


def validate(payload: dict[str, Any]) -> list[dict[str, str]]:
    issues: list[dict[str, str]] = []
    records = payload.get('records', [])
    ids = [r.get('decision_id') or r.get('item_label') for r in records]
    duplicates = sorted({x for x in ids if x and ids.count(x) > 1})
    for item in duplicates:
        issues.append({'severity': 'fail', 'code': 'duplicate_decision_id', 'detail': str(item)})

    for r in records:
        status = r.get('status')
        did = r.get('decision_id') or r.get('item_label') or 'unknown'
        if status == 'executed_verified' and r.get('requires_future_approval'):
            issues.append({'severity': 'fail', 'code': 'executed_still_requires_approval', 'detail': did})
        if status in ('needs_approval', 'pending_future', 'needs_data') and not r.get('requires_future_approval'):
            issues.append({'severity': 'fail', 'code': 'pending_without_future_approval', 'detail': did})
        if status == 'executed_verified' and any(x in (r.get('allowed_next_action') or '') for x in ['write', 'update', 'execute']):
            issues.append({'severity': 'warn', 'code': 'executed_action_wording_may_invite_write', 'detail': did})
        blocked = ' '.join(r.get('blocked_actions') or [])
        if status in ('needs_approval', 'needs_data') and not blocked:
            issues.append({'severity': 'warn', 'code': 'missing_blocked_actions', 'detail': did})

    summary = payload.get('summary', {})
    if summary.get('writes_allowed_now') != 0:
        issues.append({'severity': 'fail', 'code': 'writes_allowed_now_not_zero', 'detail': str(summary.get('writes_allowed_now'))})
    if summary.get('external_or_visible_writes_done') != 0:
        issues.append({'severity': 'fail', 'code': 'ledger_claims_external_visible_write', 'detail': str(summary.get('external_or_visible_writes_done'))})
    if not records:
        issues.append({'severity': 'fail', 'code': 'empty_ledger', 'detail': 'no records'})
    return issues


def build_report() -> dict[str, Any]:
    generated = run_ledger()
    if not generated['ok']:
        return {
            'generated_at': datetime.now(timezone.utc).isoformat(),
            'automation_id': 'LK-AUTO-004',
            'mode': 'manual_post_action_only',
            'status': 'failed',
            'crons_created': 0,
            'n8n_flows_created': 0,
            'external_sends': 0,
            'production_writes': 0,
            'generation': generated,
            'issues': [{'severity': 'fail', 'code': 'ledger_generation_failed', 'detail': 'see generation stderr'}],
        }
    ledger = generated['after']
    issues = validate(ledger)
    fail_count = sum(1 for i in issues if i['severity'] == 'fail')
    warn_count = sum(1 for i in issues if i['severity'] == 'warn')
    return {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'automation_id': 'LK-AUTO-004',
        'name': 'Approval Learning Ledger refresh guard',
        'mode': 'manual_post_action_only',
        'status': 'passed' if fail_count == 0 else 'failed',
        'summary': {
            'ledger_records': ledger.get('summary', {}).get('records', 0),
            'executed_verified': ledger.get('summary', {}).get('executed_verified', 0),
            'pending_future': ledger.get('summary', {}).get('pending_future', 0),
            'needs_approval': ledger.get('summary', {}).get('needs_approval', 0),
            'needs_data': ledger.get('summary', {}).get('status_counts', {}).get('needs_data', 0),
            'fail_count': fail_count,
            'warn_count': warn_count,
            'crons_created': 0,
            'n8n_flows_created': 0,
            'external_sends': 0,
            'production_writes': 0,
        },
        'generation': {
            'returncode': generated['returncode'],
            'before_summary': generated['before_summary'],
            'after_summary': ledger.get('summary'),
        },
        'issues': issues,
        'routing_contract': [
            'Run manually after approval, correction, execution, or a new source artifact changes.',
            'If status passed and report changed, commit through PR with health check and secret scan.',
            'Do not create a cron yet; this is a guard/protocol, not an external automation.',
            'Do not auto-approve or auto-execute any item from the ledger.',
        ],
    }


def write_outputs(report: dict[str, Any]) -> None:
    OUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    s = report.get('summary', {})
    lines = [
        '# LK Approval Ledger Refresh Guard, 2026-05-11', '',
        f"Generated at: `{report['generated_at']}`", '',
        '## Veredito', '',
        f"Status: `{report['status']}`", '',
        'LK-AUTO-004 avançou para um guard manual pós-ação: ele regenera o ledger, valida contradições e escreve um relatório de readiness, sem cron, sem n8n, sem aprovação automática e sem execução externa.', '',
        '## Snapshot', '',
        f"- Ledger records: {s.get('ledger_records')}",
        f"- Executed verified: {s.get('executed_verified')}",
        f"- Pending future: {s.get('pending_future')}",
        f"- Needs approval: {s.get('needs_approval')}",
        f"- Needs data: {s.get('needs_data')}",
        f"- Fails: {s.get('fail_count')}",
        f"- Warnings: {s.get('warn_count')}",
        f"- Crons created: {s.get('crons_created')}",
        f"- n8n flows created: {s.get('n8n_flows_created')}",
        f"- External sends: {s.get('external_sends')}",
        f"- Production writes: {s.get('production_writes')}", '',
        '## Contrato', '',
    ]
    for rule in report.get('routing_contract', []):
        lines.append(f'- {rule}')
    lines.extend(['', '## Issues', ''])
    if report.get('issues'):
        for issue in report['issues']:
            lines.append(f"- `{issue['severity']}` · `{issue['code']}`: {issue['detail']}")
    else:
        lines.append('- Nenhuma contradição encontrada.')
    lines.extend(['', '## Uso operacional', '', 'Rodar este guard depois de qualquer aprovação/correção/execução relevante no LK OS antes de abrir PR final. Se falhar, corrigir a fonte ou o ledger antes de avançar.'])
    text = '\n'.join(lines) + '\n'
    OUT_MD.write_text(text, encoding='utf-8')
    BRAIN_DOC.write_text(text, encoding='utf-8')


def main() -> None:
    report = build_report()
    write_outputs(report)
    print(json.dumps({'ok': report['status'] == 'passed', 'summary': report.get('summary', {}), 'issues': report.get('issues', [])}, ensure_ascii=False))
    if report['status'] != 'passed':
        raise SystemExit(1)


if __name__ == '__main__':
    main()
