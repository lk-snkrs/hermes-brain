#!/usr/bin/env python3
"""Brain OS strict docs/runtime guard: local scan for risky stale instructions."""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

RISK = [
    ('runtime_write', re.compile(r'(?i)\b(docker compose up|docker compose down|systemctl|supervisorctl|s6-|restart gateway|kill -9|ssh\s|scp\s)\b')),
    ('external_write', re.compile(r'(?i)\b(shopify.*(write|update|publish|delete)|tiny.*(write|update|delete)|gh pr merge|git push|send(ed)? whatsapp|email send)\b')),
    ('secret_literal', re.compile(r'(?i)(api[_-]?key|token|secret|password)\s*[:=]\s*[^\s`"\']{12,}')),
]
EXCLUDE = {'.git','__pycache__'}
DOC_EXT = {'.md','.py','.yaml','.yml','.json','.txt'}


def iter_files(root: Path):
    for p in root.rglob('*'):
        if any(part in EXCLUDE for part in p.parts):
            continue
        if p.is_file() and p.suffix.lower() in DOC_EXT:
            yield p


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default='.')
    ap.add_argument('--json-output')
    ap.add_argument('--markdown-output')
    ap.add_argument('--fail-on-findings', action='store_true')
    args = ap.parse_args()
    root = Path(args.root).resolve()
    findings = []
    for f in iter_files(root):
        rel = str(f.relative_to(root))
        if rel.startswith('reports/governance/brain-os/brain-os-docs-runtime-guard'):
            continue
        txt = f.read_text(errors='ignore')[:300000]
        for kind, rx in RISK:
            m = rx.search(txt)
            if m:
                line = txt.count('\n', 0, m.start()) + 1
                findings.append({'kind': kind, 'path': rel, 'line': line})
    report = {'generated_at': datetime.now(timezone.utc).isoformat(), 'root': str(root), 'mode': 'local_readonly_docs_runtime_guard', 'guard_version': 'brain-os-docs-runtime-guard-v1', 'finding_count': len(findings), 'findings': findings[:200], 'truncated': len(findings) > 200}
    if args.json_output:
        p = Path(args.json_output); p.parent.mkdir(parents=True, exist_ok=True); p.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    if args.markdown_output:
        p = Path(args.markdown_output); p.parent.mkdir(parents=True, exist_ok=True)
        lines = ['# Brain OS Docs/Runtime Guard', '', f"- Generated at: `{report['generated_at']}`", f"- Findings: `{len(findings)}`", '', '## Findings']
        if findings:
            for x in findings[:50]:
                lines.append(f"- `{x['kind']}` at `{x['path']}:{x['line']}`")
        else:
            lines.append('- Nenhum achado.')
        lines += ['', '## Guardrail', '- This report is local/read-only and never prints matched secret values.']
        p.write_text('\n'.join(lines) + '\n')
    if not (args.json_output or args.markdown_output):
        print(json.dumps(report, ensure_ascii=False, indent=2))
    if args.fail_on_findings and findings:
        return 2
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
