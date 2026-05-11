#!/usr/bin/env python3
"""LK OS approval and learning ledger, read-only.

Aggregates recent LK OS approval/decision artifacts into a single operational
ledger so Hermes can route future work without re-asking or forgetting Lucas's
decisions.
"""
from __future__ import annotations

import csv
import json
import pathlib
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT_JSON = ROOT / 'reports/lk-os-approval-learning-ledger-2026-05-11.json'
OUT_CSV = ROOT / 'reports/lk-os-approval-learning-ledger-2026-05-11.csv'
OUT_MD = ROOT / 'reports/lk-os-approval-learning-ledger-2026-05-11.md'
BRAIN_DOC = ROOT / 'areas/lk/rotinas/approval-learning-ledger-2026-05-11.md'


def load_json(rel: str) -> dict[str, Any]:
    p = ROOT / rel
    if not p.exists():
        return {}
    return json.loads(p.read_text())


def add(records: list[dict[str, Any]], **kw: Any) -> None:
    defaults = {
        'business': 'LK Sneakers',
        'source_type': '',
        'source_artifact': '',
        'decision_id': '',
        'item_label': '',
        'status': '',
        'risk': '',
        'allowed_next_action': '',
        'blocked_actions': [],
        'requires_future_approval': True,
        'external_or_visible_write_done': False,
        'learning': '',
        'owner': 'Hermes/Lucas',
    }
    defaults.update(kw)
    records.append(defaults)


def build() -> dict[str, Any]:
    records: list[dict[str, Any]] = []

    # Supplier quote decisions, still a live approval queue.
    quote = load_json('reports/lk-os-approval-decision-log-router-2026-05-04_2026-05-10.json')
    for row in quote.get('decision_log', []):
        add(
            records,
            source_type='supplier_quote_decision',
            source_artifact='reports/lk-os-approval-decision-log-router-2026-05-04_2026-05-10.json',
            decision_id=row.get('decision_id') or '',
            item_label=row.get('family') or row.get('item_label') or '',
            status=row.get('current_status') or 'needs_approval',
            risk='external_supplier_lookup_or_contact',
            allowed_next_action=row.get('if_approved_next_step') if row.get('current_status') == 'needs_approval' else 'resolve_data_gap_readonly_before_approval',
            blocked_actions=[row.get('blocked_action') or 'supplier_contact'] + row.get('separate_approval_required_after_quote', []),
            requires_future_approval=True,
            external_or_visible_write_done=False,
            learning='Cotação/sourcing só avança com decisão explícita; pesquisa externa é on-demand, não full-sync permanente.',
            owner=row.get('next_actor') or 'Lucas/Júlio',
        )

    # SEO fields: approved and executed.
    seo_exec = load_json('reports/lk-approved-p1-seo-fields-execution-2026-05-11.json')
    for row in seo_exec.get('records', []):
        add(
            records,
            source_type='shopify_seo_field_execution',
            source_artifact='reports/lk-approved-p1-seo-fields-execution-2026-05-11.json',
            decision_id=f"LK-SEO-EXEC-20260511-{int(row.get('rank', 0)):02d}",
            item_label=row.get('handle') or row.get('url') or '',
            status='executed_verified' if row.get('verified_live') else row.get('status', 'executed_not_verified'),
            risk='shopify_seo_field_write_low_visible_risk',
            allowed_next_action='monitor_gsc_ga4_impact_next_week',
            blocked_actions=['h1_update', 'body_update', 'theme_or_liquid_write', 'merchant_feed_write', 'campaign_send'],
            requires_future_approval=False,
            external_or_visible_write_done=False,
            learning='Lucas approval for SEO improvements covered only title/meta fields; execution must keep rollback and live verification.',
            owner='Hermes',
        )

    # Visible CRO: explicitly pending future.
    cro = load_json('reports/lk-visible-cro-pending-future-2026-05-11.json')
    for row in cro.get('items', []):
        add(
            records,
            source_type='visible_cro_pending_future',
            source_artifact='reports/lk-visible-cro-pending-future-2026-05-11.json',
            decision_id=f"LK-CRO-PENDING-20260511-{int(row.get('rank', 0)):02d}",
            item_label=row.get('label') or row.get('url') or '',
            status='pending_future',
            risk='visible_site_content_or_theme_change',
            allowed_next_action='prepare_fresh_preview_when_lucas_reopens_cro',
            blocked_actions=row.get('pending_scope', []) + ['content_publish', 'theme_or_liquid_write'],
            requires_future_approval=True,
            external_or_visible_write_done=False,
            learning='CRO visível deve ficar pendente para futuro; não confundir aprovação de SEO title/meta com aprovação de H1/body/layout.',
            owner='Lucas/Hermes',
        )

    status_counts: dict[str, int] = {}
    source_counts: dict[str, int] = {}
    for r in records:
        status_counts[r['status']] = status_counts.get(r['status'], 0) + 1
        source_counts[r['source_type']] = source_counts.get(r['source_type'], 0) + 1

    payload = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'LK OS approval manager and learning ledger',
        'mode': 'read_only_documentation_router',
        'summary': {
            'records': len(records),
            'status_counts': status_counts,
            'source_counts': source_counts,
            'executed_verified': status_counts.get('executed_verified', 0),
            'pending_future': status_counts.get('pending_future', 0),
            'needs_approval': status_counts.get('needs_approval', 0),
            'external_or_visible_writes_done': sum(1 for r in records if r['external_or_visible_write_done']),
            'writes_allowed_now': 0,
        },
        'records': records,
        'routing_rules': [
            'executed_verified: do not repeat execution; monitor impact and keep rollback artifact.',
            'pending_future: keep in backlog; future work requires fresh preview and approval.',
            'needs_approval: prepare decision packet; do not contact supplier/client or write external systems.',
            'needs_data: resolve data gap read-only before asking for approval.',
        ],
    }
    return payload


def write_outputs(payload: dict[str, Any]) -> None:
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    fields = ['decision_id','source_type','item_label','status','risk','allowed_next_action','requires_future_approval','external_or_visible_write_done','source_artifact']
    with OUT_CSV.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in payload['records']:
            w.writerow({k: r.get(k) for k in fields})

    s = payload['summary']
    lines = [
        '# LK OS Approval Learning Ledger, 2026-05-11', '',
        f"Generated at: `{payload['generated_at']}`", '',
        '## Veredito', '',
        'Fase 7 ganhou um ledger operacional: decisões aprovadas, executadas, pendentes e bloqueadas ficam roteáveis em um único artefato, sem novos writes externos.', '',
        '## Snapshot', '',
        f"- Registros: {s['records']}",
        f"- Executed verified: {s['executed_verified']}",
        f"- Pending future: {s['pending_future']}",
        f"- Needs approval: {s['needs_approval']}",
        f"- Writes externos/visíveis feitos por este ledger: {s['external_or_visible_writes_done']}",
        f"- Writes liberados agora: {s['writes_allowed_now']}", '',
        '## Contagem por fonte', '',
    ]
    for k, v in sorted(s['source_counts'].items()):
        lines.append(f'- {k}: {v}')
    lines.extend(['', '## Regras de roteamento', ''])
    for rule in payload['routing_rules']:
        lines.append(f'- {rule}')
    lines.extend(['', '## Registros prioritários', ''])
    for r in payload['records']:
        lines.extend([
            f"### {r['decision_id'] or r['item_label']}", '',
            f"- Fonte: `{r['source_type']}`",
            f"- Item: {r['item_label']}",
            f"- Status: `{r['status']}`",
            f"- Próxima ação permitida: {r['allowed_next_action']}",
            f"- Exige aprovação futura: {r['requires_future_approval']}",
            f"- Aprendizado: {r['learning']}", '',
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
