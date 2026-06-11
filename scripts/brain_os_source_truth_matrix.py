#!/usr/bin/env python3
"""Generate local Brain OS source-of-truth matrix from hub manifests/docs."""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

DOMAINS = ['Tiny','Shopify','GMC','Meta','Klaviyo','Chatwoot','Supabase','WhatsApp','Doppler','GitHub','VPS','Docker','Cron','SPITI','Zipper','LK']


def read(p: Path) -> str:
    try:
        return p.read_text(errors='ignore')
    except Exception:
        return ''


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default='.')
    ap.add_argument('--json-output')
    ap.add_argument('--markdown-output')
    args = ap.parse_args()
    root = Path(args.root).resolve()
    rows = []
    for mf in sorted(root.glob('areas/**/projetos/*/manifest.json')):
        hub = mf.parent
        rel = str(hub.relative_to(root))
        txt = '\n'.join(read(hub / f) for f in ['manifest.json','CURRENT_STATE.md','DECISIONS_AND_GUARDRAILS.md','NEXT_STEPS.md']).lower()
        domains = [d for d in DOMAINS if d.lower() in txt]
        live_required = any(t.lower() in txt for t in ['fonte viva','source of truth','runtime','live','atual','current'])
        approval_required = any(t in txt for t in ['aprovação','approval','write','external','externo','publish','delete','update'])
        rows.append({'hub_path': rel, 'domains': domains, 'live_source_required': live_required, 'approval_required_for_writes': approval_required})
    by_domain = defaultdict(list)
    for r in rows:
        for d in r['domains']:
            by_domain[d].append(r['hub_path'])
    report = {'generated_at': datetime.now(timezone.utc).isoformat(), 'root': str(root), 'mode': 'local_source_truth_matrix', 'matrix_version': 'brain-os-source-truth-matrix-v1', 'hub_count': len(rows), 'domain_counts': {k: len(v) for k, v in sorted(by_domain.items())}, 'hubs': rows}
    if args.json_output:
        p = Path(args.json_output); p.parent.mkdir(parents=True, exist_ok=True); p.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    if args.markdown_output:
        p = Path(args.markdown_output); p.parent.mkdir(parents=True, exist_ok=True)
        lines = ['# Brain OS Source-of-Truth Matrix', '', f"- Generated at: `{report['generated_at']}`", f"- Hubs: `{len(rows)}`", '', '## Domain counts']
        for k, v in report['domain_counts'].items():
            lines.append(f'- `{k}`: {v}')
        lines += ['', '## Hubs requiring live source / approval guard']
        for r in rows:
            if r['live_source_required'] or r['approval_required_for_writes']:
                lines.append(f"- `{r['hub_path']}` — domains={r['domains']}; live_source_required={r['live_source_required']}; approval_required_for_writes={r['approval_required_for_writes']}")
        p.write_text('\n'.join(lines) + '\n')
    if not (args.json_output or args.markdown_output):
        print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
