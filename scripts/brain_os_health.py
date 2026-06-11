#!/usr/bin/env python3
"""Brain OS health/audit: local-only maturity scoring for canonical hubs."""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

REQUIRED = ['README.md','CURRENT_STATE.md','DECISIONS_AND_GUARDRAILS.md','ARTIFACT_INDEX.md','TIMELINE.md','NEXT_STEPS.md','manifest.json']
ACCEPTED_SCHEMAS = {'brain-os-project-hub-v1','brain_os_project_manifest_v1'}
SECRET_PATTERNS = [
    re.compile(r'-----BEGIN [A-Z ]*PRIVATE KEY-----'),
    re.compile(r'AKIA[0-9A-Z]{16}'),
    re.compile(r'gh[pousr]_[A-Za-z0-9_]{20,}'),
    re.compile(r'\b\d{8,12}:[A-Za-z0-9_-]{30,}\b'),
    re.compile(r'(?i)Bearer\s+[A-Za-z0-9._-]{20,}'),
    re.compile(r'(?i)(api[_-]?key|secret|token|password|authorization)\s*[:=]\s*["\']?[^\s"\']{12,}'),
]
FONTE_TERMS = ('fonte viva','source of truth','fonte da verdade','tiny','shopify','gmc','meta','klaviyo','chatwoot','supabase','runtime')
APPROVAL_TERMS = ('aprovação','approval','write','external','externo','api','cron','docker','runtime','vps','shopify','tiny','gmc','meta','klaviyo','chatwoot','supabase')


def read(path: Path) -> str:
    try:
        return path.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        return ''


def parse_json(path: Path):
    try:
        return json.loads(read(path))
    except Exception:
        return None


def iso_age_days(value: str | None):
    if not value:
        return None
    m = re.search(r'\d{4}-\d{2}-\d{2}(?:T[0-9:.+-]+Z?)?', value)
    if not m:
        return None
    s = m.group(0).replace('Z', '+00:00')
    try:
        dt = datetime.fromisoformat(s) if 'T' in s else datetime.fromisoformat(s).replace(tzinfo=timezone.utc)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return max(0, (datetime.now(timezone.utc) - dt).days)
    except Exception:
        return None


def status(score: int) -> str:
    if score >= 90:
        return 'healthy'
    if score >= 75:
        return 'watch'
    if score >= 60:
        return 'needs_attention'
    return 'critical'


def secret_findings(text: str) -> int:
    return sum(1 for rx in SECRET_PATTERNS if rx.search(text or ''))


def hub_manifests(root: Path):
    return sorted(root.glob('areas/**/projetos/*/manifest.json'))


def audit_hub(root: Path, manifest_path: Path) -> dict:
    hub = manifest_path.parent
    rel = str(hub.relative_to(root))
    issues: list[str] = []
    actions: list[str] = []
    missing = [f for f in REQUIRED if not (hub / f).exists()]
    thin = [f for f in REQUIRED if (hub / f).exists() and f.endswith('.md') and len(read(hub / f).strip()) < 120]
    if missing:
        issues.append('missing_required_files:' + ','.join(missing))
        actions.append('restore required hub package files')
    for f in thin:
        issues.append(f'{f}_too_thin')

    obj = parse_json(manifest_path)
    schema = None
    if not isinstance(obj, dict):
        issues.append('manifest_json_invalid')
        obj = {}
    else:
        schema = obj.get('schema')
        if schema not in ACCEPTED_SCHEMAS:
            issues.append('manifest_schema_missing_or_unaccepted')
        if obj.get('hub_path') and obj.get('hub_path') != rel:
            issues.append('manifest_hub_path_mismatch')
        if obj.get('external_writes') not in (False, None):
            issues.append('external_writes_not_false')
        if obj.get('runtime_changes') is True:
            issues.append('runtime_changes_true')
        if not obj.get('source_of_truth') and 'source_of_truth' not in obj:
            issues.append('manifest_source_of_truth_empty')
        if len(obj.get('guardrails') or []) < 2 and 'guardrail_count' not in obj:
            issues.append('manifest_guardrails_thin')

    completeness = max(0, 100 - len(missing) * 18 - len(thin) * 5 - (0 if isinstance(obj, dict) else 40))
    age = iso_age_days(str(obj.get('updated_at') or obj.get('created_at') or ''))
    if age is None:
        age = iso_age_days(read(hub / 'CURRENT_STATE.md'))
    if age is None:
        freshness = 10
        issues.append('freshness_no_parseable_updated_at')
        actions.append('refresh CURRENT_STATE.md and manifest.updated_at from local evidence')
    elif age <= 14:
        freshness = 100
    elif age <= 30:
        freshness = 85
    elif age <= 60:
        freshness = 60
    elif age <= 90:
        freshness = 35
        issues.append(f'stale_updated_at_{age}d')
    else:
        freshness = 10
        issues.append(f'stale_updated_at_{age}d')

    next_txt = read(hub / 'NEXT_STEPS.md').lower()
    next_steps = 0
    if len(next_txt.strip()) >= 120:
        next_steps += 30
    if any(t in next_txt for t in ('local','documental','read-only','readonly')):
        next_steps += 25
    if any(t in next_txt for t in ('aprovação','approval','aprovar')):
        next_steps += 25
    if any(t in next_txt for t in APPROVAL_TERMS):
        next_steps += 20
    if next_steps < 70:
        issues.append('next_steps_not_decision_grade')
        actions.append('split NEXT_STEPS into local/documental vs approval-required actions')

    docs = '\n'.join(read(hub / f) for f in ['CURRENT_STATE.md','DECISIONS_AND_GUARDRAILS.md','NEXT_STEPS.md']).lower()
    fv = 0
    if obj.get('source_of_truth') or 'source_of_truth' in obj:
        fv += 20
    if obj.get('guardrails') or 'guardrail_count' in obj:
        fv += 20
    if any(t in docs for t in FONTE_TERMS):
        fv += 20
    if any(t in docs for t in APPROVAL_TERMS):
        fv += 20
    if obj.get('external_writes') is False or schema == 'brain-os-project-hub-v1':
        fv += 20
    if fv < 60:
        issues.append('fonte_viva_guardrails_weak')
        actions.append('strengthen source-of-truth/fonte viva and external-write guardrails')

    art = read(hub / 'ARTIFACT_INDEX.md')
    artifact = 0
    if len(art.strip()) >= 200:
        artifact += 20
    bullets = [ln.strip()[2:].strip() for ln in art.splitlines() if ln.strip().startswith('- ')]
    pathish = []
    for b in bullets:
        if '`' in b and len(b.split('`')) > 1:
            pathish.append(b.split('`')[1])
        elif b:
            pathish.append(b.split()[0])
    if len(pathish) >= 10:
        artifact += 25
    elif len(pathish) >= 5:
        artifact += 15
    if not any(p.startswith('/') for p in pathish):
        artifact += 20
    else:
        issues.append('artifact_index_absolute_paths')
    if any(t in art.lower() for t in ('receipt','report','runbook','prd','artifact','artefato','tipo')):
        artifact += 15
    if not secret_findings(art):
        artifact += 20
    else:
        issues.append('secret_like_pattern_detected_redacted')
    missing_samples = sum(1 for p in pathish[:20] if not p.startswith('/') and not (root / p).exists())
    if missing_samples:
        issues.append(f'artifact_index_missing_sample_paths_{missing_samples}')
    if artifact < 60:
        issues.append('artifact_index_quality_weak')
        actions.append('curate ARTIFACT_INDEX by artifact type and verify relative paths')

    score = round(completeness * .25 + freshness * .20 + next_steps * .20 + fv * .25 + artifact * .10)
    st = status(score)
    if st in ('critical','needs_attention') and not actions:
        actions.append('review hub quality and metadata')
    return {
        'hub_path': rel,
        'project_id': obj.get('project_id') or obj.get('id') or hub.name,
        'title': obj.get('title') or hub.name,
        'schema': schema,
        'score': score,
        'status': st,
        'component_scores': {'completeness': completeness, 'freshness': freshness, 'next_steps': next_steps, 'fonte_viva_guardrails': fv, 'artifact_index': artifact},
        'age_days': age,
        'issues': issues,
        'recommended_next_actions': sorted(set(actions))[:5],
    }


def build_report(root: Path) -> dict:
    hubs = [audit_hub(root, p) for p in hub_manifests(root)]
    counts = Counter(h['status'] for h in hubs)
    issues = Counter(i for h in hubs for i in h['issues'])
    scores = [h['score'] for h in hubs] or [0]
    return {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'root': str(root.resolve()),
        'mode': 'read_only_local_health_audit',
        'auditor_version': 'brain-os-health-v1',
        'total_hubs': len(hubs),
        'status_counts': {k: counts.get(k, 0) for k in ['healthy','watch','needs_attention','critical']},
        'average_score': round(sum(scores) / len(scores), 1),
        'min_score': min(scores),
        'max_score': max(scores),
        'top_issues': dict(issues.most_common(15)),
        'lowest_scoring_hubs': sorted(hubs, key=lambda h: (h['score'], h['hub_path']))[:15],
        'hubs': sorted(hubs, key=lambda h: h['hub_path']),
    }


def render_md(report: dict) -> str:
    lines = ['# Brain OS Health Audit', '', f"- Generated at: `{report['generated_at']}`", f"- Root: `{report['root']}`", f"- Mode: `{report['mode']}`", f"- Hubs audited: `{report['total_hubs']}`", f"- Average score: `{report['average_score']}/100`", f"- Status counts: `{report['status_counts']}`", '', '## Lowest scoring hubs']
    for h in report['lowest_scoring_hubs'][:10]:
        issues = ', '.join(h['issues'][:3]) or 'no issues'
        lines.append(f"- `{h['hub_path']}` — {h['score']}/100 ({h['status']}); issues: {issues}")
    lines += ['', '## Top issues']
    for k, v in report['top_issues'].items():
        lines.append(f'- `{k}`: {v}')
    lines += ['', '## Guardrails', '- Local/read-only audit only.', '- No external APIs, runtime, Docker, VPS, cron, or secrets output.', '- Scores do not authorize external writes.']
    return '\n'.join(lines) + '\n'


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default='.')
    ap.add_argument('--json-output')
    ap.add_argument('--markdown-output')
    ap.add_argument('--stdout-json', action='store_true')
    ap.add_argument('--stdout-markdown', action='store_true')
    args = ap.parse_args()
    report = build_report(Path(args.root).resolve())
    if args.json_output:
        p = Path(args.json_output); p.parent.mkdir(parents=True, exist_ok=True); p.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    if args.markdown_output:
        p = Path(args.markdown_output); p.parent.mkdir(parents=True, exist_ok=True); p.write_text(render_md(report), encoding='utf-8')
    if args.stdout_json or not (args.json_output or args.markdown_output or args.stdout_markdown):
        print(json.dumps(report, ensure_ascii=False, indent=2))
    if args.stdout_markdown:
        print(render_md(report))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
