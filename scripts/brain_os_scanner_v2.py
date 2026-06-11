#!/usr/bin/env python3
"""Brain OS scanner v2: local/read-only semantic classification.

Adds hub/receipt/backup/artifact classification while reusing PROJECT_DEFS from
scripts/brain_os_scanner.py.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

DEFAULT_ROOT = Path('/opt/data/hermes_bruno_ingest/hermes-brain')
TEXT_EXTS = {'.md', '.json', '.txt', '.yaml', '.yml', '.csv'}
EXCLUDE_PARTS = {'.git', '__pycache__'}
SCANNER_VERSION = 'brain-os-v2'
CLASSIFICATION_POLICY_VERSION = 'brain-os-artifact-classification-v1'
HUB_MANIFEST_SCHEMAS = {'brain-os-project-hub-v1', 'brain_os_project_manifest_v1'}
CANONICAL_HUB_RE = re.compile(r'(^|/)areas/[^/]+/(?:sub-areas/[^/]+/)?projetos/[^/]+/manifest\.json$')
MANIFEST_CLASSES = ('hub_manifest', 'receipt_manifest', 'backup_manifest', 'artifact_manifest', 'other')


def load_project_defs() -> list[dict]:
    p = Path(__file__).with_name('brain_os_scanner.py')
    spec = importlib.util.spec_from_file_location('brain_os_scanner_v1', p)
    if not spec or not spec.loader:
        raise RuntimeError(f'cannot load {p}')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return list(module.PROJECT_DEFS)


PROJECT_DEFS = load_project_defs()


def iter_files(root: Path) -> Iterable[Path]:
    for dp, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_PARTS]
        p = Path(dp)
        for name in files:
            f = p / name
            if f.suffix.lower() in TEXT_EXTS:
                yield f


def safe_read(path: Path, max_bytes: int = 200_000) -> str:
    try:
        return path.read_bytes()[:max_bytes].decode('utf-8', errors='ignore').lower()
    except Exception:
        return ''


def safe_json(path: Path, max_bytes: int = 200_000) -> Any | None:
    try:
        return json.loads(path.read_bytes()[:max_bytes].decode('utf-8', errors='ignore'))
    except Exception:
        return None


def classify_artifact(root: Path, path: Path) -> dict:
    try:
        rel = str(path.relative_to(root))
    except ValueError:
        rel = str(path)
    name_l = path.name.lower()
    stem_l = path.stem.lower()
    obj = safe_json(path) if path.suffix.lower() == '.json' else None

    if isinstance(obj, dict):
        schema = obj.get('schema')
        parent_rel = str(path.parent.relative_to(root)) if path.is_relative_to(root) else str(path.parent)
        if name_l == 'manifest.json' and schema in HUB_MANIFEST_SCHEMAS and CANONICAL_HUB_RE.search(rel) and obj.get('hub_path') == parent_rel:
            return {'artifact_type': 'hub_manifest', 'confidence': 'high', 'signals': ['canonical_manifest_path', f'schema:{schema}', 'hub_path_matches_parent']}
        if name_l == 'manifest.json' and ('by_category' in obj or 'items' in obj or 'canonical_folder' in obj):
            return {'artifact_type': 'artifact_manifest', 'confidence': 'high', 'signals': ['index_manifest_shape']}
        keys = {str(k).lower() for k in obj.keys()}
        if keys.intersection({'rollback', 'rollback_data', 'rollback_plan', 'backup', 'backup_path', 'restore_plan'}):
            return {'artifact_type': 'backup_manifest', 'confidence': 'high', 'signals': ['rollback_or_backup_keys']}
        if keys.intersection({'verification', 'verified_live', 'results', 'execution', 'executed_at', 'receipt', 'status'}):
            return {'artifact_type': 'receipt_manifest', 'confidence': 'medium', 'signals': ['execution_or_verification_keys']}

    local_hint = f'{name_l} {stem_l}'
    if re.search(r'(^|[-_. ])(backup|rollback|pre-write|prewrite|bak|snapshot)([-_. ]|$)', local_hint):
        return {'artifact_type': 'backup_manifest', 'confidence': 'medium', 'signals': ['backup_path_token']}
    if re.search(r'(^|[-_. ])(receipt|recibo|execution|executed|verification|verified|readback|audit|approval)([-_. ]|$)', local_hint):
        return {'artifact_type': 'receipt_manifest', 'confidence': 'medium', 'signals': ['receipt_path_token']}
    if name_l == 'manifest.json' or re.search(r'(^|[-_. ])(artifact|index|fixture|preview|report)([-_. ]|$)', local_hint):
        return {'artifact_type': 'artifact_manifest', 'confidence': 'medium', 'signals': ['artifact_path_token']}
    return {'artifact_type': 'other', 'confidence': 'low', 'signals': []}


def count_owner_files(root: Path, rel: str) -> int:
    p = root / rel
    if not p.exists():
        return 0
    return sum(1 for f in p.rglob('*') if f.is_file())


def existing_hub_dirs(root: Path, hubs: list[str]) -> list[str]:
    return [h for h in hubs if (root / h).exists()]


def live_hubs(root: Path, hubs: list[str]) -> list[str]:
    found = []
    for h in hubs:
        manifest = root / h / 'manifest.json'
        if manifest.exists() and classify_artifact(root, manifest)['artifact_type'] == 'hub_manifest':
            found.append(h)
    return found


def aggregate(items: Iterable[str]) -> dict:
    out = {k: 0 for k in MANIFEST_CLASSES}
    for item in items:
        out[item] = out.get(item, 0) + 1
    return {k: v for k, v in out.items() if v}


def scan(root: Path) -> dict:
    root = root.resolve()
    text_files = list(iter_files(root))
    rels = [str(p.relative_to(root)) for p in text_files]
    all_classes = []
    manifest_counts = {k: 0 for k in MANIFEST_CLASSES}
    for p in text_files:
        typ = classify_artifact(root, p)['artifact_type']
        all_classes.append(typ)
        if p.name.lower() == 'manifest.json':
            manifest_counts[typ] += 1

    candidates = []
    for spec in PROJECT_DEFS:
        term_hits = 0
        file_hits = []
        term_re = re.compile('|'.join(re.escape(t.lower()) for t in spec['terms']))
        for p, rel in zip(text_files, rels):
            rel_l = rel.lower()
            path_match = any(t.lower().replace(' ', '-') in rel_l or t.lower() in rel_l for t in spec['terms'])
            content_match = False
            if path_match:
                content_match = True
            elif len(file_hits) < 250:
                content_match = bool(term_re.search(safe_read(p, 60_000)))
            if path_match or content_match:
                file_hits.append(rel)
                term_hits += 1
        owner_files = count_owner_files(root, spec['owner_area'])
        hub_dirs = existing_hub_dirs(root, spec['suggested_hubs'])
        hubs = live_hubs(root, spec['suggested_hubs'])
        score = min(owner_files // 100, 40) + min(term_hits // 25, 30) + (15 if not hubs else 5) + (10 if spec['risk'] else 0) + (5 if spec['wave'] == 1 else 0)
        class_counts = {}
        samples = []
        for rel in file_hits:
            typ = classify_artifact(root, root / rel)['artifact_type']
            class_counts[typ] = class_counts.get(typ, 0) + 1
        for rel in file_hits[:30]:
            cls = classify_artifact(root, root / rel)
            samples.append({'path': rel, 'artifact_type': cls['artifact_type'], 'confidence': cls['confidence'], 'signals': cls['signals'][:5]})
        if not hubs and hub_dirs:
            recommendation = 'promote_or_replace_artifact_manifest_with_hub_manifest'
            maturity = 'hub_dir_without_live_manifest'
        elif not hubs:
            recommendation = 'canonical_hub_needed'
            maturity = 'canonical_hub_missing'
        else:
            recommendation = 'monitor_or_refine_existing_hub'
            maturity = 'live_hub_present'
        candidates.append({
            'id': spec['id'], 'title': spec['title'], 'owner_area': spec['owner_area'],
            'suggested_hubs': spec['suggested_hubs'], 'existing_hubs': hubs,
            'existing_hub_dirs': hub_dirs, 'live_hub_count': len(hubs),
            'non_live_hub_dirs': sorted(set(hub_dirs) - set(hubs)), 'maturity': maturity,
            'wave': spec['wave'], 'risk': spec['risk'], 'owner_file_count': owner_files,
            'term_hit_files': term_hits, 'artifact_class_counts': class_counts,
            'sample_artifacts': file_hits[:30], 'sample_artifact_classes': samples,
            'score': score, 'recommendation': recommendation,
        })
    candidates = sorted(candidates, key=lambda x: (x['wave'], -x['score']))
    with_hub = sum(1 for c in candidates if c['live_hub_count'])
    return {
        'generated_at': datetime.now(timezone.utc).isoformat(), 'root': str(root),
        'mode': 'read_only_scan', 'scanner_version': SCANNER_VERSION,
        'classification_policy_version': CLASSIFICATION_POLICY_VERSION,
        'total_text_files_scanned': len(text_files), 'artifact_class_counts': aggregate(all_classes),
        'manifest_class_counts': {k: v for k, v in manifest_counts.items() if v},
        'candidate_count': len(candidates), 'candidates_with_live_hub': with_hub,
        'candidates_without_live_hub': len(candidates) - with_hub,
        'live_hub_count_in_project_defs': sum(c['live_hub_count'] for c in candidates),
        'candidates': candidates,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default=str(DEFAULT_ROOT))
    ap.add_argument('--json', action='store_true')
    ap.add_argument('--output')
    args = ap.parse_args()
    result = scan(Path(args.root))
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text + '\n', encoding='utf-8')
    if args.json or not args.output:
        print(text)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
