#!/usr/bin/env python3
"""LK GMC post A/B/C monitor, read-only.

Checks exact IDs from the approved 2026-05-14 A/B/C package:
- 12 Shopify DRAFT/landing-page-404 Merchant IDs remain absent (products.get + productstatuses.get)
- 64 non-critical attr patched IDs have no target color/ageGroup/gender diagnostics
- full productstatuses baseline for next LK OS gates
No Merchant/Shopify/Tiny/Notion/feed/campaign writes.
"""
from __future__ import annotations

import csv, importlib.util, json, pathlib, time, urllib.error, urllib.parse, urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
AUDIT = ROOT/'scripts/lk_gmc_catalog_duplication_audit_20260512.py'
DELETE_VERIFY = ROOT/'reports/lk-gmc-2026-05-14-draft-404-merchant-delete-delayed-verify.json'
ATTR_RECHECK = ROOT/'reports/lk-approved-c-attrs-poststatus-recheck-2026-05-14.json'
RUN_STAMP = '2026-05-14-post-abc-monitor'
OUT_JSON = ROOT/f'reports/lk-gmc-{RUN_STAMP}.json'
OUT_MD = ROOT/f'reports/lk-gmc-{RUN_STAMP}.md'
OUT_CSV = ROOT/f'reports/lk-gmc-{RUN_STAMP}-issue-summary.csv'

TARGET_ATTRS = {'color', 'age group', 'gender', 'ageGroup'}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_audit():
    spec = importlib.util.spec_from_file_location('audit', AUDIT)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(mod)
    return mod


def request_json(url: str, token: str, attempts: int = 4) -> dict[str, Any] | None:
    last = ''
    for i in range(1, attempts + 1):
        req = urllib.request.Request(url)
        req.add_header('Authorization', 'Bearer ' + token)
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                raw = r.read().decode()
                return json.loads(raw) if raw else {}
        except urllib.error.HTTPError as e:
            raw = e.read().decode(errors='replace')
            if e.code == 404:
                return None
            last = f'http_{e.code}: {raw[:500]}'
            if e.code not in {429, 500, 502, 503, 504} or i == attempts:
                raise RuntimeError(last) from e
        except Exception as e:
            last = str(e)[:500]
            if i == attempts:
                raise RuntimeError(last) from e
        time.sleep(min(30, 2 ** i))
    raise RuntimeError(last or 'request_failed')


def product_url(mid: str, pid: str) -> str:
    return f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/products/' + urllib.parse.quote(pid, safe='')


def status_url(mid: str, pid: str) -> str:
    return f'https://shoppingcontent.googleapis.com/content/v2.1/{mid}/productstatuses/' + urllib.parse.quote(pid, safe='')


def issue_key(issue: dict[str, Any]) -> str:
    return str(issue.get('code') or issue.get('servability') or issue.get('attributeName') or 'unknown_issue')


def channel(pid: str) -> str:
    return (pid or '').split(':', 1)[0] if ':' in (pid or '') else 'unknown'


def load_ids() -> tuple[list[str], list[str]]:
    deleted = [r['product_id'] for r in json.loads(DELETE_VERIFY.read_text())['rows']]
    attrs = [r['product_id'] for r in json.loads(ATTR_RECHECK.read_text())['rows']]
    return sorted(set(deleted)), sorted(set(attrs))


def is_target_attr_issue(issue: dict[str, Any]) -> bool:
    text = ' '.join(str(issue.get(k) or '') for k in ['attributeName','code','detail','description']).lower()
    return any(a.lower() in text for a in TARGET_ATTRS)


def summarize_statuses(statuses: list[dict[str, Any]]) -> dict[str, Any]:
    issue_counts = Counter()
    issue_by_channel: dict[str, Counter] = defaultdict(Counter)
    dest_counts = Counter()
    rows_with_issues = 0
    samples = []
    for st in statuses:
        pid = st.get('productId') or ''
        ch = channel(pid)
        issues = st.get('itemLevelIssues') or []
        if issues:
            rows_with_issues += 1
        for issue in issues:
            key = issue_key(issue)
            issue_counts[key] += 1
            issue_by_channel[ch][key] += 1
            if len(samples) < 25:
                samples.append({
                    'product_id': pid,
                    'title': st.get('title'),
                    'channel': ch,
                    'issue_key': key,
                    'severity': issue.get('severity'),
                    'attributeName': issue.get('attributeName'),
                    'detail': str(issue.get('detail') or '')[:180],
                })
        for d in st.get('destinationStatuses') or []:
            dest = d.get('destination') or d.get('destinationName') or 'unknown_destination'
            stat = d.get('status') or 'unknown_status'
            dest_counts[f'{dest}:{stat}'] += 1
    return {
        'productstatuses_read': len(statuses),
        'rows_with_item_issues': rows_with_issues,
        'item_issue_instances': sum(issue_counts.values()),
        'item_issue_counts_top': [{'issue_key': k, 'count': v} for k,v in issue_counts.most_common(30)],
        'item_issue_counts_by_channel_top': {ch: [{'issue_key': k, 'count': v} for k,v in c.most_common(12)] for ch,c in issue_by_channel.items()},
        'destination_status_counts_top': [{'destination_status': k, 'count': v} for k,v in dest_counts.most_common(20)],
        'sample_issues': samples,
    }


def write_outputs(payload: dict[str, Any]) -> None:
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
    with OUT_CSV.open('w', newline='', encoding='utf-8') as f:
        fields = ['issue_key','count']
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader()
        for row in payload['full_status_baseline']['item_issue_counts_top']:
            w.writerow(row)
    s = payload['summary']
    lines = [
        '# LK GMC — Monitor read-only pós A/B/C, 2026-05-14', '',
        f"Gerado em: `{payload['generated_at']}`", '',
        '## Resultado',
        f"- Status: `{payload['status']}`",
        f"- 12 IDs DRAFT/404 removidos: {s['deleted_absent_both_count']}/12 seguem ausentes por `products.get` e `productstatuses.get`.",
        f"- 64 atributos C: {s['attr_ids_without_target_issue_count']}/64 sem diagnóstico alvo de `color/ageGroup/gender`.",
        f"- Productstatuses lidos: {payload['full_status_baseline']['productstatuses_read']}",
        f"- Linhas com issues no catálogo geral: {payload['full_status_baseline']['rows_with_item_issues']}",
        '', '## Top diagnósticos gerais atuais'
    ]
    for row in payload['full_status_baseline']['item_issue_counts_top'][:12]:
        lines.append(f"- `{row['issue_key']}`: {row['count']}")
    lines += ['', '## Não executado']
    for item in payload['not_performed']:
        lines.append(f'- {item}')
    lines += ['', '## Próximo gate seguro', payload['next_safe_gate']]
    OUT_MD.write_text('\n'.join(lines) + '\n')


def main() -> None:
    audit = load_audit()
    secrets = audit.load_doppler()
    mid = secrets['MERCHANT_CENTER_ID_LK']
    token = audit.google_access_token(audit.parse_service_account(secrets))
    deleted_ids, attr_ids = load_ids()

    deleted_rows = []
    for pid in deleted_ids:
        prod = request_json(product_url(mid, pid), token)
        st = request_json(status_url(mid, pid), token)
        deleted_rows.append({'product_id': pid, 'present_product_get': prod is not None, 'present_status_get': st is not None})

    attr_rows = []
    target_issue_counts = Counter()
    for pid in attr_ids:
        st = request_json(status_url(mid, pid), token)
        issues = (st or {}).get('itemLevelIssues') or []
        target = [i for i in issues if is_target_attr_issue(i)]
        for i in target:
            target_issue_counts[issue_key(i)] += 1
        attr_rows.append({'product_id': pid, 'status_present': st is not None, 'target_attr_issue_count': len(target), 'target_attr_issues': [{'issue_key': issue_key(i), 'attributeName': i.get('attributeName'), 'detail': str(i.get('detail') or '')[:180]} for i in target]})

    statuses = audit.list_all('productstatuses', mid, token)
    full = summarize_statuses(statuses)
    summary = {
        'deleted_targets': len(deleted_ids),
        'deleted_absent_both_count': sum(1 for r in deleted_rows if not r['present_product_get'] and not r['present_status_get']),
        'attr_targets': len(attr_ids),
        'attr_ids_without_target_issue_count': sum(1 for r in attr_rows if r['target_attr_issue_count'] == 0),
        'target_attr_issue_counts': dict(target_issue_counts),
    }
    status = 'post_abc_clean_for_target_scope' if summary['deleted_absent_both_count'] == len(deleted_ids) and summary['attr_ids_without_target_issue_count'] == len(attr_ids) else 'post_abc_needs_review'
    payload = {
        'generated_at': utc_now(),
        'scope': 'read-only monitor after approved 2026-05-14 LK A/B/C execution',
        'status': status,
        'source_labels': ['fact_merchant_center','manual_approval_lucas_abc','fact_shopify_readonly_prior_draft_diagnosis'],
        'summary': summary,
        'deleted_exact_id_check': deleted_rows,
        'attr_exact_id_check': attr_rows,
        'full_status_baseline': full,
        'next_safe_gate': 'Build next residual preview only after reviewing current full diagnostics; no second Merchant/Shopify/Notion write without explicit inline approval.',
        'not_performed': ['Merchant write/delete/patch', 'Shopify publish/redirect/write', 'Tiny write', 'Notion write', 'feed fetch/upload', 'campaign/message/customer/supplier contact'],
    }
    write_outputs(payload)
    print(json.dumps({'status': status, 'summary': summary, 'out_json': str(OUT_JSON), 'out_md': str(OUT_MD)}, ensure_ascii=False))

if __name__ == '__main__':
    main()
