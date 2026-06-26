#!/usr/bin/env python3
"""LK GMC Phase 7 post-cleanup monitoring, read-only.

Reads Merchant products/productstatuses after approved cleanup packages and writes
sanitized operational reports. No Merchant/Shopify/Tiny/feed/DB/POS writes.
"""
from __future__ import annotations

import csv
import importlib.util
import json
import pathlib
from collections import Counter, defaultdict
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / 'scripts/lk_gmc_catalog_duplication_audit_20260512.py'
LOCAL_CD_EXEC_JSON = ROOT / 'reports/lk-gmc-2026-05-12-local-cd-63-old-lia-cleanup-execution.json'
PACKAGE_A_JSON = ROOT / 'reports/lk-gmc-2026-05-12-package-a-online-stale-triage.json'
PACKAGE_B_JSON = ROOT / 'reports/lk-gmc-2026-05-12-package-b-identifier-fix.json'
B3_ROLLBACK_JSON = ROOT / 'reports/lk-gmc-2026-05-12-package-b3-emergency-rollback-restore.json'
RUN_STAMP = '2026-05-12-phase7-post-cleanup-monitor'
OUT_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
OUT_CSV = ROOT / f'reports/lk-gmc-{RUN_STAMP}-issue-summary.csv'
OUT_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
BRAIN_DOC = ROOT / f'areas/lk/rotinas/gmc-{RUN_STAMP}.md'
CONTROL = ROOT / 'areas/lk/projetos/lk-os-implementation-control.md'
INDEX = ROOT / 'empresa/rotinas/_index.md'


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_json(path: pathlib.Path) -> dict[str, Any]:
    if not path.exists():
        return {'_missing': str(path)}
    return json.loads(path.read_text(encoding='utf-8'))


def import_audit():
    spec = importlib.util.spec_from_file_location('audit', AUDIT_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def channel(pid: str) -> str:
    return (pid or '').split(':', 1)[0] if ':' in (pid or '') else 'unknown'


def dimension(pid: str) -> str:
    parts = (pid or '').split(':', 3)
    if len(parts) == 4:
        return ':'.join(parts[:3])
    return 'unknown'


def issue_key(issue: dict[str, Any]) -> str:
    return str(issue.get('code') or issue.get('servability') or issue.get('attributeName') or 'unknown_issue')


def summarize_statuses(statuses: list[dict[str, Any]]) -> dict[str, Any]:
    by_channel = Counter()
    by_dimension = Counter()
    issue_counts = Counter()
    issue_by_channel: dict[str, Counter] = defaultdict(Counter)
    destination_counts = Counter()
    destination_by_channel: dict[str, Counter] = defaultdict(Counter)
    issue_rows = 0
    destination_problem_rows = 0
    sample_issues = []
    for st in statuses:
        pid = st.get('productId') or ''
        ch = channel(pid)
        dim = dimension(pid)
        by_channel[ch] += 1
        by_dimension[dim] += 1
        issues = st.get('itemLevelIssues') or []
        if issues:
            issue_rows += 1
        for issue in issues:
            key = issue_key(issue)
            issue_counts[key] += 1
            issue_by_channel[ch][key] += 1
            if len(sample_issues) < 30:
                sample_issues.append({
                    'product_id': pid,
                    'channel': ch,
                    'title': st.get('title'),
                    'issue_key': key,
                    'severity': issue.get('severity'),
                    'resolution': issue.get('resolution'),
                    'destination': issue.get('destination'),
                    'detail': str(issue.get('detail') or '')[:180],
                })
        dests = st.get('destinationStatuses') or []
        bad_dest = False
        for d in dests:
            dest_name = d.get('destination') or d.get('destinationName') or 'unknown_destination'
            status = d.get('status') or 'unknown_status'
            k = f'{dest_name}:{status}'
            destination_counts[k] += 1
            destination_by_channel[ch][k] += 1
            if status not in {'approved', 'pending'}:
                bad_dest = True
        if bad_dest:
            destination_problem_rows += 1
    return {
        'total_statuses': len(statuses),
        'by_channel': dict(by_channel),
        'by_dimension_top': [{'dimension': k, 'count': v} for k, v in by_dimension.most_common(20)],
        'rows_with_item_issues': issue_rows,
        'item_issue_instances': sum(issue_counts.values()),
        'item_issue_counts_top': [{'issue_key': k, 'count': v} for k, v in issue_counts.most_common(30)],
        'item_issue_counts_by_channel_top': {ch: [{'issue_key': k, 'count': v} for k, v in cnt.most_common(15)] for ch, cnt in issue_by_channel.items()},
        'destination_status_counts_top': [{'destination_status': k, 'count': v} for k, v in destination_counts.most_common(30)],
        'destination_status_counts_by_channel_top': {ch: [{'destination_status': k, 'count': v} for k, v in cnt.most_common(15)] for ch, cnt in destination_by_channel.items()},
        'rows_with_destination_problem': destination_problem_rows,
        'sample_issues': sample_issues,
    }


def write_outputs(payload: dict[str, Any]) -> None:
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    fields = ['scope', 'bucket', 'key', 'count']
    rows = []
    for row in payload['current_merchant_statuses']['item_issue_counts_top']:
        rows.append({'scope': 'merchant_current', 'bucket': 'item_issue', 'key': row['issue_key'], 'count': row['count']})
    for row in payload['current_merchant_statuses']['destination_status_counts_top']:
        rows.append({'scope': 'merchant_current', 'bucket': 'destination_status', 'key': row['destination_status'], 'count': row['count']})
    with OUT_CSV.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(rows)
    s = payload['summary']
    lines = [
        '# LK GMC Phase 7 Post-cleanup Monitor, 2026-05-12', '',
        f"Status: `{payload['status']}`", '',
        '## Resumo executivo',
        f"- Merchant products atuais: {s['merchant_products_current']}",
        f"- Merchant productstatuses atuais: {s['merchant_productstatuses_current']}",
        f"- Online/local atuais: {s['products_by_channel'].get('online',0)} / {s['products_by_channel'].get('local',0)}",
        f"- Local C/D cleanup: old IDs ausentes {s['local_cd_old_absent']}/{s['local_cd_old_total']}; replacement IDs presentes {s['local_cd_replacements_present']}/{s['local_cd_replacements_total']}",
        f"- Linhas com item issues: {s['rows_with_item_issues']}",
        f"- Instâncias de item issues: {s['item_issue_instances']}",
        f"- Linhas com destination problem: {s['rows_with_destination_problem']}", '',
        '## Top item issues atuais',
    ]
    for r in payload['current_merchant_statuses']['item_issue_counts_top'][:12]:
        lines.append(f"- {r['issue_key']}: {r['count']}")
    lines.extend(['', '## Top destination statuses atuais'])
    for r in payload['current_merchant_statuses']['destination_status_counts_top'][:12]:
        lines.append(f"- {r['destination_status']}: {r['count']}")
    lines.extend(['', '## Veredito', payload['interpretation']['verdict'], '', '## Próximo bloco seguro'])
    for n in payload['interpretation']['next_safe_blocks']:
        lines.append(f'- {n}')
    lines.extend(['', '## Não executado'])
    for n in payload['not_performed']:
        lines.append(f'- {n}')
    lines.extend(['', '## Arquivos', f'- JSON: `{OUT_JSON}`', f'- CSV issues: `{OUT_CSV}`'])
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    BRAIN_DOC.write_text(OUT_MD.read_text(encoding='utf-8'), encoding='utf-8')
    if CONTROL.exists():
        marker = '### 2026-05-12 — GMC Phase 7 post-cleanup monitor'
        text = CONTROL.read_text(encoding='utf-8')
        block = (
            f"\n{marker}\n\n"
            f"- Status: {payload['status']}.\n"
            f"- Merchant products/statuses atuais: {s['merchant_products_current']} / {s['merchant_productstatuses_current']}.\n"
            f"- Local C/D verificado: old_absent={s['local_cd_old_absent']}/{s['local_cd_old_total']}; replacements_present={s['local_cd_replacements_present']}/{s['local_cd_replacements_total']}.\n"
            f"- Item issues atuais: rows={s['rows_with_item_issues']}; instances={s['item_issue_instances']}; destination_problem_rows={s['rows_with_destination_problem']}.\n"
            f"- Nenhum write executado; próximo bloco recomendado: diagnostics delta/read-only e novo pacote apenas se houver candidato exato.\n\n"
        )
        if marker not in text:
            CONTROL.write_text(text.rstrip() + block, encoding='utf-8')
    if INDEX.exists():
        line = f'| LK GMC Phase 7 Post-cleanup Monitor 2026-05-12 | `areas/lk/rotinas/gmc-{RUN_STAMP}.md` | Recheck read-only pós-limpeza: valida ausência dos 63 old LIA, preservação dos 14 replacements e resumo atual de item/destination issues |'
        text = INDEX.read_text(encoding='utf-8')
        if line not in text:
            INDEX.write_text(text.rstrip() + '\n' + line + '\n', encoding='utf-8')


def main() -> None:
    audit = import_audit()
    secrets = audit.load_doppler()
    merchant_id = secrets.get('MERCHANT_CENTER_ID_LK')
    if not merchant_id:
        raise RuntimeError('missing_merchant_center_id')
    token = audit.google_access_token(audit.parse_service_account(secrets))
    products = audit.list_all('products', merchant_id, token)
    statuses = audit.list_all('productstatuses', merchant_id, token)
    current_product_ids = {p.get('id') for p in products}
    products_by_channel = Counter(channel(p.get('id') or '') for p in products)
    statuses_summary = summarize_statuses(statuses)

    local_cd = load_json(LOCAL_CD_EXEC_JSON)
    public_rows = local_cd.get('public_rows') or []
    old_ids = {r.get('old_product_id_deleted') for r in public_rows if r.get('old_product_id_deleted')}
    replacement_ids = {x for r in public_rows for x in str(r.get('replacement_local_product_ids_kept') or '').split(';') if x}
    old_absent = sum(1 for x in old_ids if x not in current_product_ids)
    repl_present = sum(1 for x in replacement_ids if x in current_product_ids)

    summary = {
        'merchant_products_current': len(products),
        'merchant_productstatuses_current': len(statuses),
        'products_by_channel': dict(products_by_channel),
        'local_cd_old_total': len(old_ids),
        'local_cd_old_absent': old_absent,
        'local_cd_replacements_total': len(replacement_ids),
        'local_cd_replacements_present': repl_present,
        'rows_with_item_issues': statuses_summary['rows_with_item_issues'],
        'item_issue_instances': statuses_summary['item_issue_instances'],
        'rows_with_destination_problem': statuses_summary['rows_with_destination_problem'],
    }
    status = 'gmc_phase7_post_cleanup_monitor_readonly_ready'
    if old_absent == len(old_ids) and repl_present == len(replacement_ids):
        verdict = '- Pós-limpeza local C/D segue saudável: 63 old IDs continuam ausentes e 14 replacement rows continuam presentes. A limpeza está encerrada operacionalmente; o próximo ganho deve vir de diagnostics/delta, não de repetir deletes locais.'
    else:
        status = 'gmc_phase7_post_cleanup_monitor_readonly_needs_review'
        verdict = '- Pós-limpeza requer revisão: algum old ID reapareceu ou replacement row está ausente. Não executar novos writes até diagnosticar a fonte.'
    payload = {
        'generated_at': utc_now(),
        'status': status,
        'scope': 'LK GMC Phase 7 post-cleanup read-only monitoring after approved A/B/local C-D work',
        'source_labels': ['fact_merchant_center', 'derived_reconciliation', 'manual_approval_lucas_2026_05_12'],
        'summary': summary,
        'current_merchant_statuses': statuses_summary,
        'executed_package_refs': {
            'local_cd_cleanup': str(LOCAL_CD_EXEC_JSON),
            'package_a': str(PACKAGE_A_JSON),
            'package_b': str(PACKAGE_B_JSON),
            'b3_rollback': str(B3_ROLLBACK_JSON),
        },
        'interpretation': {
            'verdict': verdict,
            'next_safe_blocks': [
                'Read-only diagnostics delta after Merchant reprocessing window: compare issue codes/counts against this Phase 7 baseline.',
                'If issues remain material, build a new approval packet only from exact current product IDs with rollback snapshot; no broad deletes.',
                'Refresh Mission Control with this baseline once diagnostics stabilizes.',
            ],
        },
        'not_performed': ['merchant_product_delete','merchant_product_insert','merchant_product_update','content_api_custombatch','datafeed_fetchNow','feed_update','shopify_write','tiny_write','database_write','pos_or_local_inventory_setting_change','campaign_or_external_send'],
    }
    write_outputs(payload)
    print(json.dumps({'status': status, 'summary': summary, 'public_report': str(OUT_MD)}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
