#!/usr/bin/env python3
"""Finalize remaining LK GMC P2A online categorization/product_type candidates.

Scope: Merchant API v1 ProductInputs PATCH only for dataSource 10636492695.
Fields: productAttributes.googleProductCategory and productAttributes.productTypes only.
No Shopify/Tiny/price/availability/title/image/link/local inventory/feed/campaign changes.

This executor is intentionally resumable and private-progress-first because it may touch
many products. It does a fresh Merchant read of every deterministic online candidate,
skips already-compliant rows, creates private rollback shards, patches in bounded batches,
then verifies exact Merchant readback.
"""
from __future__ import annotations

import argparse, importlib.util, json, os, pathlib, re, sys, time
from collections import Counter
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
P2_PATH = ROOT / 'scripts/lk_gmc_p2_category_product_type_executor_20260513.py'
RUN_STAMP = '2026-05-13-p2a-finalize-remaining-online'
PUBLIC_JSON = ROOT / f'reports/lk-gmc-{RUN_STAMP}.json'
PUBLIC_MD = ROOT / f'reports/lk-gmc-{RUN_STAMP}.md'
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots')
DATA_SOURCE_ID = '10636492695'
APPROVAL_TEXT_REQUIRED = 'eu autorizo finalizar todos os produtos que faltam ok? seguir'

NOT_PERFORMED = [
    'title_update', 'price_update', 'availability_update', 'image_or_link_update',
    'merchant_delete', 'local_inventory_write', 'shopify_write', 'tiny_write',
    'database_write', 'feed_fetch_or_upload', 'campaign_or_message_send'
]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_mod(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(mod)
    return mod


def attrs(p: dict[str, Any]) -> dict[str, Any]:
    return p.get('productAttributes') or p.get('attributes') or {}


def pid(p: dict[str, Any]) -> str:
    return p.get('id') or p.get('productId') or p.get('name', '').split('/')[-1]


def offer(product_id: str) -> str:
    return product_id.split(':')[-1]


def guess_category(title: str) -> tuple[str | None, str | None, str | None]:
    s = (title or '').lower()
    if any(x in s for x in ['camiseta', 't-shirt', 'tee shirt', 'short sleeve', 'long sleeve']):
        return ('Apparel & Accessories > Clothing > Shirts & Tops', 'Camiseta', 'shirt_token_high_confidence')
    if any(x in s for x in ['moletom', 'hoodie', 'jaqueta', 'jacket', 'sweatshirt']):
        return ('Apparel & Accessories > Clothing > Outerwear', 'Moletom/Jaqueta', 'outerwear_token_high_confidence')
    if any(x in s for x in ['shorts', 'bermuda']):
        return ('Apparel & Accessories > Clothing > Shorts', 'Shorts', 'shorts_token_high_confidence')
    if any(x in s for x in ['calça', 'pants', 'sweatpants']):
        return ('Apparel & Accessories > Clothing > Pants', 'Calça', 'pants_token_high_confidence')
    if any(x in s for x in ['boné', 'bone ', 'cap ']):
        return ('Apparel & Accessories > Clothing Accessories > Hats', 'Boné', 'hat_token_high_confidence')
    if any(x in s for x in ['bolsa', 'bag', 'shoulder bag', 'tote', 'wallet', 'carteira']):
        return ('Luggage & Bags > Handbags, Wallets & Cases', 'Bolsa/Carteira', 'bag_token_high_confidence')
    if any(x in s for x in ['tênis ', 'tenis ', 'sneaker', 'handball spezial', 'samba og', 'gazelle', 'air jordan', 'air force', 'sb dunk', 'yeezy', 'new balance', 'asics gel', 'onitsuka', 'slide', 'mule']):
        return ('Apparel & Accessories > Shoes', 'Tênis', 'shoe_token_high_confidence')
    return (None, None, None)


PRIORITY = {
    'Apparel & Accessories > Clothing > Shirts & Tops': 0,
    'Apparel & Accessories > Clothing > Outerwear': 1,
    'Apparel & Accessories > Clothing > Shorts': 2,
    'Apparel & Accessories > Clothing > Pants': 3,
    'Apparel & Accessories > Clothing Accessories > Hats': 4,
    'Luggage & Bags > Handbags, Wallets & Cases': 5,
    'Apparel & Accessories > Shoes': 6,
}


def refresh_token(w, audit, secrets):
    return audit.google_access_token(audit.parse_service_account(secrets))


def merchant_attrs(p2, mid: str, token: str, product_id: str) -> dict[str, Any]:
    _name, encoded, *_ = p2.product_input_name(mid, product_id)
    return (p2.merchant_product_get(mid, encoded, token).get('productAttributes') or {})


def snapshot(batch_no: int, records: list[dict[str, Any]], approval_text: str) -> pathlib.Path:
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE_DIR, 0o700)
    path = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-batch{batch_no:04d}-rollback-{datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")}.json'
    payload = {
        'generated_at': utc_now(),
        'scope': 'Finalize remaining deterministic online P2A category/productTypes only',
        'data_source': f'accounts/*/dataSources/{DATA_SOURCE_ID}',
        'approval_text_received': approval_text,
        'rollback_instruction': 'Patch productAttributes.googleProductCategory/productTypes back to previous values for exact product IDs if rollback is needed.',
        'records': records,
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    os.chmod(path, 0o600)
    return path


def write_public(status: str, summary: dict[str, Any], manifest_path: pathlib.Path | None, progress_path: pathlib.Path | None, rollback_paths: list[str], verify_sample: list[dict[str, Any]] | None = None):
    payload = {
        'generated_at': utc_now(),
        'status': status,
        'api': 'Merchant API v1 ProductInputs PATCH',
        'data_source': f'accounts/*/dataSources/{DATA_SOURCE_ID}',
        'summary': summary,
        'private_manifest_path': str(manifest_path) if manifest_path else None,
        'private_progress_path': str(progress_path) if progress_path else None,
        'private_rollback_snapshot_paths_count': len(rollback_paths),
        'private_rollback_snapshot_paths': rollback_paths[-5:],
        'verify_sample': verify_sample or [],
        'not_performed': NOT_PERFORMED,
    }
    PUBLIC_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    lines = [
        '# LK GMC P2A Finalize Remaining Online — 2026-05-13', '',
        f'Status: `{status}`', '',
        '## Escopo',
        '- Merchant API v1 ProductInputs PATCH.',
        '- Somente `productAttributes.googleProductCategory` + `productAttributes.productTypes`.',
        f'- DataSource: `{DATA_SOURCE_ID}`.',
        '- Exclui local inventory/LIA e candidatos ambíguos.', '',
        '## Resumo',
    ]
    for k, v in summary.items():
        lines.append(f'- {k}: {v}')
    lines += ['', '## Rollback privado', f'- Shards criados: {len(rollback_paths)}', '', '## Não executado']
    lines += [f'- {x}' for x in NOT_PERFORMED]
    PUBLIC_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--approval-text', default='')
    ap.add_argument('--batch-size', type=int, default=250)
    ap.add_argument('--patch-sleep', type=float, default=0.20)
    ap.add_argument('--read-sleep', type=float, default=0.03)
    ap.add_argument('--verify-delay', type=int, default=180)
    ap.add_argument('--max-apply', type=int, default=0, help='0 means all selected')
    ap.add_argument('--resume-manifest', default='')
    args = ap.parse_args()

    mode = 'apply' if args.apply else 'dry-run'
    if args.apply and args.approval_text.strip().lower() != APPROVAL_TEXT_REQUIRED:
        raise RuntimeError('apply_blocked_missing_exact_approval_text: ' + APPROVAL_TEXT_REQUIRED)

    p2 = load_mod(P2_PATH, 'p2finalize')
    w = p2.import_w4()
    audit = w.import_audit()
    secrets = audit.load_doppler()
    mid = secrets.get('MERCHANT_CENTER_ID_LK')
    token = refresh_token(w, audit, secrets)

    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE_DIR, 0o700)
    run_ts = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    manifest_path = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-manifest-{run_ts}.json'
    progress_path = PRIVATE_DIR / f'lk-gmc-{RUN_STAMP}-progress-{run_ts}.jsonl'

    selected: list[dict[str, Any]]
    base_count = 0
    skipped_compliant = 0
    skipped_errors: list[dict[str, Any]] = []

    if args.resume_manifest:
        manifest = json.loads(pathlib.Path(args.resume_manifest).read_text(encoding='utf-8'))
        selected = manifest['selected_rows']
        base_count = manifest.get('base_candidates', 0)
        skipped_compliant = manifest.get('skipped_already_compliant', 0)
    else:
        products = w.list_all('products', mid, token)
        base = []
        for p in products:
            product_id = pid(p)
            if not product_id.startswith('online:pt:BR:'):
                continue
            at = attrs(p)
            title = at.get('title') or p.get('title') or ''
            sgpc, spt, evidence = guess_category(title)
            if not sgpc:
                continue
            base.append({
                'product_id': product_id,
                'offer_id': offer(product_id),
                'title': title,
                'suggested_googleProductCategory': sgpc,
                'suggested_productTypes': [spt],
                'evidence': evidence,
            })
        base.sort(key=lambda r: (PRIORITY.get(r['suggested_googleProductCategory'], 9), r['suggested_productTypes'][0], r['title'], r['product_id']))
        base_count = len(base)
        selected = []
        for idx, r in enumerate(base, 1):
            if idx % 500 == 0:
                print(json.dumps({'phase': 'fresh_scan', 'checked': idx, 'selected': len(selected), 'skipped_compliant': skipped_compliant}, ensure_ascii=False), flush=True)
                token = refresh_token(w, audit, secrets)
            try:
                fresh = merchant_attrs(p2, mid, token, r['product_id'])
                cur_gpc = fresh.get('googleProductCategory')
                cur_pts = fresh.get('productTypes') or []
                eligible = cur_gpc != r['suggested_googleProductCategory'] or cur_pts != r['suggested_productTypes']
                if not eligible:
                    skipped_compliant += 1
                else:
                    selected.append({
                        **r,
                        'fresh_current_googleProductCategory': cur_gpc,
                        'fresh_current_productTypes': cur_pts,
                        'fresh_title': fresh.get('title') or r['title'],
                    })
            except Exception as e:
                skipped_errors.append({'product_id': r['product_id'], 'error': str(e)[:1200]})
            time.sleep(args.read_sleep)
        if args.max_apply:
            selected = selected[:args.max_apply]
        manifest_payload = {
            'generated_at': utc_now(),
            'mode': mode,
            'base_candidates': base_count,
            'skipped_already_compliant': skipped_compliant,
            'selected_count': len(selected),
            'selected_bucket_counts': {f'{k[0]} / {k[1]}': v for k, v in Counter((r['suggested_googleProductCategory'], (r['suggested_productTypes'] or [''])[0]) for r in selected).most_common()},
            'skipped_error_count': len(skipped_errors),
            'skipped_error_sample': skipped_errors[:50],
            'selected_rows': selected,
        }
        manifest_path.write_text(json.dumps(manifest_payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        os.chmod(manifest_path, 0o600)

    summary = {
        'mode': mode,
        'base_candidates': base_count,
        'selected_to_patch': len(selected),
        'skipped_already_compliant': skipped_compliant,
        'selected_bucket_counts': {f'{k[0]} / {k[1]}': v for k, v in Counter((r['suggested_googleProductCategory'], (r['suggested_productTypes'] or [''])[0]) for r in selected).most_common()},
    }

    if not args.apply:
        write_public('dry_run_ready', summary, manifest_path, None, [])
        print(json.dumps({'status': 'dry_run_ready', 'summary': summary, 'manifest': str(manifest_path), 'report': str(PUBLIC_MD)}, ensure_ascii=False, indent=2), flush=True)
        return

    rollback_paths: list[str] = []
    exec_results: list[dict[str, Any]] = []
    with progress_path.open('w', encoding='utf-8') as progress:
        os.chmod(progress_path, 0o600)
        for batch_no, start in enumerate(range(0, len(selected), args.batch_size), 1):
            batch = selected[start:start + args.batch_size]
            token = refresh_token(w, audit, secrets)
            rollback_records = []
            # Fresh pre-patch read for rollback/current state and idempotent skip.
            for r in batch:
                try:
                    fresh = merchant_attrs(p2, mid, token, r['product_id'])
                    cur_gpc = fresh.get('googleProductCategory')
                    cur_pts = fresh.get('productTypes') or []
                    if cur_gpc == r['suggested_googleProductCategory'] and cur_pts == r['suggested_productTypes']:
                        item = {'product_id': r['product_id'], 'execution_status': 'skipped_already_compliant_prepatch'}
                        exec_results.append(item); progress.write(json.dumps(item, ensure_ascii=False) + '\n'); progress.flush()
                        continue
                    rollback_records.append({**r, 'rollback_googleProductCategory': cur_gpc, 'rollback_productTypes': cur_pts})
                except Exception as e:
                    item = {'product_id': r['product_id'], 'execution_status': 'failed_prepatch_read', 'error': str(e)[:1200]}
                    exec_results.append(item); progress.write(json.dumps(item, ensure_ascii=False) + '\n'); progress.flush()
            if not rollback_records:
                continue
            rollback = snapshot(batch_no, rollback_records, args.approval_text)
            rollback_paths.append(str(rollback))
            print(json.dumps({'phase': 'patch_batch_start', 'batch_no': batch_no, 'records': len(rollback_records), 'patched_so_far': sum(1 for x in exec_results if x.get('execution_status') == 'patched_p2a_finalize_v1')}, ensure_ascii=False), flush=True)
            for r in rollback_records:
                try:
                    resp = p2.patch_category_product_types(mid, token, r['product_id'], r['suggested_googleProductCategory'], r['suggested_productTypes'])
                    item = {
                        'product_id': r['product_id'],
                        'execution_status': 'patched_p2a_finalize_v1',
                        'product_input': resp.get('name'),
                        'expected_googleProductCategory': r['suggested_googleProductCategory'],
                        'expected_productTypes': r['suggested_productTypes'],
                    }
                except Exception as e:
                    item = {'product_id': r['product_id'], 'execution_status': 'failed_patch_p2a_finalize_v1', 'error': str(e)[:1500]}
                exec_results.append(item)
                progress.write(json.dumps(item, ensure_ascii=False) + '\n')
                progress.flush()
                if item['execution_status'].startswith('failed_patch'):
                    write_public('apply_stopped_on_patch_failure', {**summary, 'execution_results_summary': dict(Counter(x.get('execution_status') for x in exec_results))}, manifest_path, progress_path, rollback_paths)
                    print(json.dumps({'status': 'apply_stopped_on_patch_failure', 'failed': item, 'progress': str(progress_path)}, ensure_ascii=False, indent=2), flush=True)
                    return
                time.sleep(args.patch_sleep)
            write_public('apply_in_progress', {**summary, 'execution_results_summary': dict(Counter(x.get('execution_status') for x in exec_results)), 'patched_so_far': sum(1 for x in exec_results if x.get('execution_status') == 'patched_p2a_finalize_v1')}, manifest_path, progress_path, rollback_paths)

    if args.verify_delay:
        print(json.dumps({'phase': 'verify_delay', 'seconds': args.verify_delay}, ensure_ascii=False), flush=True)
        time.sleep(args.verify_delay)

    verify_results: list[dict[str, Any]] = []
    token = refresh_token(w, audit, secrets)
    expected_by_pid = {r['product_id']: r for r in selected}
    patched = [x for x in exec_results if x.get('execution_status') == 'patched_p2a_finalize_v1']
    for idx, item in enumerate(patched, 1):
        if idx % 500 == 0:
            print(json.dumps({'phase': 'verify', 'checked': idx, 'total': len(patched)}, ensure_ascii=False), flush=True)
            token = refresh_token(w, audit, secrets)
        r = expected_by_pid.get(item['product_id'])
        try:
            fresh = merchant_attrs(p2, mid, token, item['product_id'])
            actual_gpc = fresh.get('googleProductCategory')
            actual_pts = fresh.get('productTypes') or []
            match = bool(r and actual_gpc == r['suggested_googleProductCategory'] and actual_pts == r['suggested_productTypes'])
            verify_results.append({**item, 'verify_status': 'verified_merchant_product_get', 'actual_googleProductCategory': actual_gpc, 'actual_productTypes': actual_pts, 'match_expected': match})
        except Exception as e:
            verify_results.append({**item, 'verify_status': 'verify_failed', 'verify_error': str(e)[:1200]})
        time.sleep(args.read_sleep)

    final_summary = {
        **summary,
        'execution_results_summary': dict(Counter(x.get('execution_status') for x in exec_results)),
        'verify_results_summary': dict(Counter(x.get('verify_status') for x in verify_results)),
        'patched_count': len(patched),
        'verified_match_expected': sum(1 for x in verify_results if x.get('match_expected')),
        'verify_mismatch_count': sum(1 for x in verify_results if x.get('verify_status') == 'verified_merchant_product_get' and not x.get('match_expected')),
        'verify_failed_count': sum(1 for x in verify_results if x.get('verify_status') == 'verify_failed'),
    }
    status = 'apply_verified' if final_summary['verified_match_expected'] == len(patched) and final_summary['verify_failed_count'] == 0 and final_summary['verify_mismatch_count'] == 0 else 'apply_completed_needs_review'
    write_public(status, final_summary, manifest_path, progress_path, rollback_paths, verify_results[:100])
    print(json.dumps({'status': status, 'summary': final_summary, 'report': str(PUBLIC_MD), 'manifest': str(manifest_path), 'progress': str(progress_path)}, ensure_ascii=False, indent=2), flush=True)


if __name__ == '__main__':
    main()
