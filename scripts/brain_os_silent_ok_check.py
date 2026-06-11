#!/usr/bin/env python3
"""Brain OS silent-OK local check. Prints only on failure unless --verbose.

This is a local script only; it does not install or schedule any cron job.
"""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default='.')
    ap.add_argument('--verbose', action='store_true')
    args = ap.parse_args()
    root = Path(args.root).resolve()
    problems = []
    cmds = [
        ['python3','scripts/brain_os_scanner_v2.py','--root',str(root),'--output','reports/governance/brain-os/brain-os-candidates-latest.json'],
        ['python3','scripts/brain_os_health.py','--root',str(root),'--json-output','reports/governance/brain-os/brain-os-health-latest.json','--markdown-output','reports/governance/brain-os/brain-os-health-latest.md'],
        ['python3','scripts/brain_os_docs_runtime_guard.py','--root',str(root),'--json-output','reports/governance/brain-os/brain-os-docs-runtime-guard-latest.json','--markdown-output','reports/governance/brain-os/brain-os-docs-runtime-guard-latest.md'],
    ]
    for cmd in cmds:
        r = subprocess.run(cmd, cwd=root, text=True, capture_output=True)
        if r.returncode:
            problems.append({'cmd': ' '.join(cmd[:2]), 'exit': r.returncode, 'stderr': r.stderr[-500:]})
    h = json.loads((root / 'reports/governance/brain-os/brain-os-health-latest.json').read_text())
    if h.get('status_counts', {}).get('critical', 0) > 0:
        problems.append({'health_critical': h['status_counts']['critical']})
    if problems or args.verbose:
        print(json.dumps({'ok': not problems, 'problems': problems}, ensure_ascii=False, indent=2))
    return 1 if problems else 0

if __name__ == '__main__':
    raise SystemExit(main())
