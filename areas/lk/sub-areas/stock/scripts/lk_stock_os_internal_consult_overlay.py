#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import shutil
import sqlite3
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

BASE = Path('areas/lk/sub-areas/stock')
SCRIPTS = BASE / 'scripts'
sys.path.insert(0, str(SCRIPTS.resolve()))

from lk_stock_tiny_shopify_crosswalk import OFFICIAL_DEPOSIT, tiny_stock  # noqa: E402

POINTER = BASE / 'data/lk_stock_os_current_pointer.json'
DATA = BASE / 'data'
REPORTS = BASE / 'reports'
REFERENCES = BASE / 'references'


def iso_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')


def utc_run_id() -> str:
    return datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')


def connect(path: Path) -> sqlite3.Connection:
    con = sqlite3.connect(path)
    con.row_factory = sqlite3.Row
    return con


def read_pointer() -> dict[str, Any]:
    return json.loads(POINTER.read_text(encoding='utf-8'))


def resolve_db(ptr: dict[str, Any], input_db: str | None = None) -> Path:
    raw = input_db or (ptr.get('artifacts') or {}).get('sqlite_db')
    if not raw:
        raise SystemExit('pointer has no artifacts.sqlite_db')
    path = Path(raw)
    if not path.exists():
        raise SystemExit(f'input db not found: {path}')
    return path


def table_exists(con: sqlite3.Connection, name: str) -> bool:
    return bool(con.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (name,)).fetchone())


def create_tables(con: sqlite3.Connection) -> None:
    con.execute('''CREATE TABLE IF NOT EXISTS internal_consult_overlay_decisions (
      run_id TEXT, observed_at_utc TEXT, sku TEXT, handle TEXT, title TEXT, size TEXT,
      previous_status TEXT, new_status TEXT, decision TEXT, reason TEXT,
      tiny_id TEXT, tiny_codigo TEXT, quantity REAL, quantity_source TEXT,
      local_consult_safe INTEGER, identity_resolved_safe INTEGER,
      public_availability_safe INTEGER, availability_claim_allowed INTEGER,
      tiny_write INTEGER, shopify_write INTEGER, writes_externos INTEGER,
      payload_json TEXT,
      PRIMARY KEY (run_id, sku, handle)
    )''')


def latest_full_live_rows(con: sqlite3.Connection) -> dict[tuple[str, str], sqlite3.Row]:
    if not table_exists(con, 'full_live_match_decisions'):
        return {}
    rows: dict[tuple[str, str], sqlite3.Row] = {}
    for r in con.execute('''
        SELECT * FROM full_live_match_decisions
        ORDER BY sku, handle, observed_at_utc
    '''):
        rows[(r['sku'], r['handle'])] = r
    return rows


def update_scored_if_present(con: sqlite3.Connection, sku: str, handle: str, status: str, quantity: float | None, local_consult_safe: int, identity_resolved_safe: int) -> None:
    if not table_exists(con, 'current_stock_scored'):
        return
    cols = {r['name'] for r in con.execute('PRAGMA table_info(current_stock_scored)')}
    assignments = ['canonical_status=?', 'local_consult_safe=?', 'identity_resolved_safe=?', 'public_availability_safe=0', 'availability_claim_allowed=0']
    values: list[Any] = [status, local_consult_safe, identity_resolved_safe]
    if 'stock_quantity_max_observed' in cols:
        assignments.append('stock_quantity_max_observed=?')
        values.append(quantity)
    values.extend([sku, handle])
    con.execute(f"UPDATE current_stock_scored SET {', '.join(assignments)} WHERE sku=? AND handle=?", values)


def insert_decision(con: sqlite3.Connection, run_id: str, decision: dict[str, Any]) -> None:
    con.execute('''INSERT OR REPLACE INTO internal_consult_overlay_decisions VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (
        run_id,
        decision['observed_at_utc'],
        decision['sku'],
        decision['handle'],
        decision.get('title') or '',
        decision.get('size') or '',
        decision.get('previous_status') or '',
        decision.get('new_status') or '',
        decision.get('decision') or '',
        decision.get('reason') or '',
        decision.get('tiny_id') or '',
        decision.get('tiny_codigo') or '',
        decision.get('quantity'),
        decision.get('quantity_source') or '',
        int(decision.get('local_consult_safe') or 0),
        int(decision.get('identity_resolved_safe') or 0),
        0,
        0,
        0,
        0,
        0,
        json.dumps(decision, ensure_ascii=False, sort_keys=True),
    ))


def apply_parent_non_variant(con: sqlite3.Connection, row: sqlite3.Row, run_id: str, observed_at: str) -> dict[str, Any]:
    status = 'CONSULTABLE_LOCAL_PARENT_BASE_NO_STOCK_VARIANT'
    reason = 'parent/base line is not a sellable size variant; keep searchable internally without stock promise'
    con.execute('''UPDATE current_local_stock SET
        canonical_status=?, local_consult_safe=1, identity_resolved_safe=0,
        public_availability_safe=0, availability_claim_allowed=0,
        needs_live_tiny_confirmation=1,
        stock_source=?, stock_freshness=?, source_observed_at=?,
        data_quality_gap=?
      WHERE sku=? AND handle=?''', (
        status,
        'Stock OS local classification (parent/base non-stock-variant)',
        'classified_parent_base_non_stock_variant',
        observed_at,
        reason,
        row['sku'], row['handle'],
    ))
    update_scored_if_present(con, row['sku'], row['handle'], status, None, 1, 0)
    return {
        'observed_at_utc': observed_at,
        'sku': row['sku'], 'handle': row['handle'], 'title': row['title'], 'size': row['size'],
        'previous_status': row['canonical_status'], 'new_status': status,
        'decision': 'CLASSIFIED_PARENT_BASE_NON_STOCK_VARIANT', 'reason': reason,
        'quantity': None, 'quantity_source': 'none_not_stock_variant',
        'local_consult_safe': 1, 'identity_resolved_safe': 0,
        'public_availability_safe': 0, 'availability_claim_allowed': 0,
        'tiny_write': 0, 'shopify_write': 0, 'writes_externos': 0,
    }


def apply_tiny_internal_consult(con: sqlite3.Connection, row: sqlite3.Row, live: sqlite3.Row, run_id: str, observed_at: str, sleep_seconds: float) -> dict[str, Any]:
    tiny_id = str(live['tiny_ids'] or '').strip()
    tiny_codigo = str(live['tiny_codigos'] or row['tiny_codigo'] or '').strip()
    time.sleep(sleep_seconds)
    stock = tiny_stock(tiny_id)
    if not stock or stock.get('deposito') != OFFICIAL_DEPOSIT or stock.get('saldo') is None:
        return {
            'observed_at_utc': observed_at,
            'sku': row['sku'], 'handle': row['handle'], 'title': row['title'], 'size': row['size'],
            'previous_status': row['canonical_status'], 'new_status': row['canonical_status'],
            'decision': 'SKIPPED_TINY_READBACK_FAILED',
            'reason': f'Tiny readback did not return {OFFICIAL_DEPOSIT}',
            'tiny_id': tiny_id, 'tiny_codigo': tiny_codigo,
            'quantity': None, 'quantity_source': 'tiny_readback_failed',
            'local_consult_safe': 0, 'identity_resolved_safe': 0,
            'public_availability_safe': 0, 'availability_claim_allowed': 0,
            'tiny_write': 0, 'shopify_write': 0, 'writes_externos': 0,
            'stock_readback': stock,
        }
    quantity = float(stock['saldo'])
    status = 'CONSULTABLE_LOCAL_TINY_STOCK_IDENTITY_BLOCKED'
    reason = f'Tiny exact unique readback succeeded, but Shopify/Tiny identity remains blocked by previous status {row["canonical_status"]}'
    stock_positive = 1 if quantity > 0 else 0
    stock_zero = 1 if quantity == 0 else 0
    con.execute('''UPDATE current_local_stock SET
        canonical_status=?, tiny_codigo=?, tiny_id_candidates=?,
        stock_observation_count=1,
        stock_quantity_observed_values=?, stock_quantity_sum_observed=?, stock_quantity_max_observed=?,
        stock_positive_observed=?, stock_zero_observed=?,
        stock_source=?, stock_freshness=?, source_observed_at=?,
        local_consult_safe=1, identity_resolved_safe=0,
        public_availability_safe=0, availability_claim_allowed=0,
        needs_live_tiny_confirmation=1,
        data_quality_gap=?
      WHERE sku=? AND handle=?''', (
        status, tiny_codigo, tiny_id,
        str(quantity), quantity, quantity,
        stock_positive, stock_zero,
        f'Tiny produto.obter.estoque / {OFFICIAL_DEPOSIT} (internal consult overlay; identity blocked)',
        'live_tiny_readback_internal_consult_overlay', observed_at,
        reason,
        row['sku'], row['handle'],
    ))
    update_scored_if_present(con, row['sku'], row['handle'], status, quantity, 1, 0)
    return {
        'observed_at_utc': observed_at,
        'sku': row['sku'], 'handle': row['handle'], 'title': row['title'], 'size': row['size'],
        'previous_status': row['canonical_status'], 'new_status': status,
        'decision': 'PROMOTED_TINY_UNIQUE_INTERNAL_CONSULT_IDENTITY_BLOCKED',
        'reason': reason,
        'tiny_id': tiny_id, 'tiny_codigo': tiny_codigo,
        'quantity': quantity,
        'quantity_source': f'Tiny produto.obter.estoque / {OFFICIAL_DEPOSIT}',
        'local_consult_safe': 1, 'identity_resolved_safe': 0,
        'public_availability_safe': 0, 'availability_claim_allowed': 0,
        'tiny_write': 0, 'shopify_write': 0, 'writes_externos': 0,
        'stock_readback': stock,
    }


def recompute_totals(con: sqlite3.Connection) -> dict[str, Any]:
    row = con.execute('''SELECT
        count(*) AS current_local_stock_rows,
        sum(CASE WHEN coalesce(local_consult_safe,0)=1 THEN 1 ELSE 0 END) AS local_consult_safe_rows,
        sum(CASE WHEN coalesce(local_consult_safe,0)=0 THEN 1 ELSE 0 END) AS non_consultable_blocked_rows,
        sum(CASE WHEN coalesce(identity_resolved_safe,0)=1 THEN 1 ELSE 0 END) AS identity_resolved_safe_rows,
        sum(CASE WHEN coalesce(identity_resolved_safe,0)=0 THEN 1 ELSE 0 END) AS identity_unresolved_rows,
        sum(CASE WHEN coalesce(public_availability_safe,0)=1 THEN 1 ELSE 0 END) AS public_availability_safe_rows,
        sum(CASE WHEN coalesce(availability_claim_allowed,0)=1 THEN 1 ELSE 0 END) AS availability_claim_allowed_rows,
        sum(CASE WHEN coalesce(stock_quantity_max_observed,0)>0 THEN 1 ELSE 0 END) AS stock_positive_current_rows,
        sum(CASE WHEN stock_quantity_max_observed=0 THEN 1 ELSE 0 END) AS stock_zero_current_rows
      FROM current_local_stock''').fetchone()
    status_counts = {r['canonical_status']: r['c'] for r in con.execute('SELECT canonical_status, count(*) c FROM current_local_stock GROUP BY canonical_status ORDER BY c DESC')}
    blocked_counts = {r['canonical_status']: r['c'] for r in con.execute('SELECT canonical_status, count(*) c FROM current_local_stock WHERE coalesce(local_consult_safe,0)=0 GROUP BY canonical_status ORDER BY c DESC')}
    totals = dict(row)
    totals['status_counts'] = status_counts
    totals['non_consultable_blocked_status_counts'] = blocked_counts
    return totals


def write_reports(run_id: str, summary: dict[str, Any], decisions: list[dict[str, Any]]) -> dict[str, str]:
    REPORTS.mkdir(parents=True, exist_ok=True)
    REFERENCES.mkdir(parents=True, exist_ok=True)
    json_path = REPORTS / f'lk-stock-os-internal-consult-overlay-{run_id}.json'
    csv_path = REPORTS / f'lk-stock-os-internal-consult-overlay-{run_id}.csv'
    md_path = REPORTS / f'lk-stock-os-internal-consult-overlay-{run_id}.md'
    guide_path = REFERENCES / 'lk-stock-os-internal-consult-overlay-guide-20260616.md'
    json_path.write_text(json.dumps({'summary': summary, 'decisions': decisions}, ensure_ascii=False, indent=2, sort_keys=True), encoding='utf-8')
    fields = ['decision','sku','handle','title','size','previous_status','new_status','tiny_id','tiny_codigo','quantity','quantity_source','reason','local_consult_safe','identity_resolved_safe','observed_at_utc']
    with csv_path.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        w.writeheader(); w.writerows(decisions)
    lines = [
        '# Report — LK Stock OS internal consult overlay', '',
        f'- Run ID: `{run_id}`',
        f'- Input DB: `{summary["input_db"]}`',
        f'- Output DB: `{summary["output_db"]}`',
        f'- Decisions total: `{summary["decisions_total"]}`',
        f'- Tiny unique rows promoted to internal consult: `{summary["decision_counts"].get("PROMOTED_TINY_UNIQUE_INTERNAL_CONSULT_IDENTITY_BLOCKED", 0)}`',
        f'- Parent/base rows classified as non-stock variants: `{summary["decision_counts"].get("CLASSIFIED_PARENT_BASE_NON_STOCK_VARIANT", 0)}`',
        f'- Tiny readback failures/skips: `{summary["decision_counts"].get("SKIPPED_TINY_READBACK_FAILED", 0)}`',
        f'- Non-consultable blocked rows after: `{summary["totals_after"].get("non_consultable_blocked_rows")}`',
        f'- Identity unresolved rows after: `{summary["totals_after"].get("identity_unresolved_rows")}`',
        '', '## Guardrails', '',
        '- Tiny write: 0', '- Shopify write: 0', '- Writes externos: 0', '- Public availability/pronta entrega pública: 0',
        '', '## Nota', '',
        'Este overlay melhora consulta interna e leitura de quantidade quando há readback Tiny único. Ele não corrige cadastro externo nem libera promessa pública.',
    ]
    md_path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    guide_path.write_text('# Guia — Internal consult overlay Stock OS\n\nUse quando linhas bloqueadas têm Tiny exato único ou quando linhas `parent/base` estavam poluindo contagem de bloqueio de variantes. Guardrails: Tiny/Shopify/public write 0; identidade bloqueada continua `identity_resolved_safe=0`.\n', encoding='utf-8')
    return {'json': str(json_path), 'csv': str(csv_path), 'md': str(md_path), 'guide': str(guide_path)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--run-id', default=utc_run_id())
    ap.add_argument('--input-db')
    ap.add_argument('--sleep-seconds', type=float, default=1.2)
    ap.add_argument('--limit', type=int, default=0)
    args = ap.parse_args()

    ptr = read_pointer()
    input_db = resolve_db(ptr, args.input_db)
    output_db = (DATA / f'lk_stock_os_current_internal_consult_overlay_{args.run_id}.db').resolve()
    shutil.copy2(input_db, output_db)

    con = connect(output_db)
    create_tables(con)
    live_map = latest_full_live_rows(con)
    observed_at = iso_now()
    rows = [dict(r) for r in con.execute('SELECT * FROM current_local_stock WHERE coalesce(local_consult_safe,0)=0 ORDER BY handle, sku')]
    if args.limit:
        rows = rows[:args.limit]

    decisions: list[dict[str, Any]] = []
    for idx, row_dict in enumerate(rows, start=1):
        # Re-fetch as sqlite Row for consistent access after prior updates.
        row = con.execute('SELECT * FROM current_local_stock WHERE sku=? AND handle=?', (row_dict['sku'], row_dict['handle'])).fetchone()
        live = live_map.get((row['sku'], row['handle']))
        decision: dict[str, Any] | None = None
        if (row['size'] or '') == 'parent/base':
            decision = apply_parent_non_variant(con, row, args.run_id, observed_at)
        elif live and int(live['tiny_exact_count'] or 0) == 1 and live['tiny_saldo_lk_controle_estoque'] is not None and ';' not in str(live['tiny_ids'] or ''):
            decision = apply_tiny_internal_consult(con, row, live, args.run_id, observed_at, args.sleep_seconds)
        if decision:
            decisions.append(decision)
            insert_decision(con, args.run_id, decision)
        if idx % 25 == 0:
            con.commit()
            print(json.dumps({'progress': idx, 'total': len(rows), 'decisions': len(decisions), 'run_id': args.run_id}, ensure_ascii=False), flush=True)
    con.commit()
    totals_after = recompute_totals(con)
    decision_counts = dict(Counter(d['decision'] for d in decisions))
    summary = {
        'run_id': args.run_id,
        'created_at_utc': observed_at,
        'finished_at_utc': iso_now(),
        'input_db': str(input_db),
        'output_db': str(output_db),
        'decisions_total': len(decisions),
        'decision_counts': decision_counts,
        'totals_after': totals_after,
        'guardrails': {'tiny_write': 0, 'shopify_write': 0, 'writes_externos': 0, 'public_availability_safe': 0, 'availability_claim_allowed': 0},
    }
    artifacts = write_reports(args.run_id, summary, decisions)
    con.commit(); con.close()

    ptr.setdefault('artifacts', {})['sqlite_db'] = str(output_db)
    ptr['artifacts']['internal_consult_overlay_db'] = str(output_db)
    ptr['artifacts']['internal_consult_overlay_json'] = artifacts['json']
    ptr['artifacts']['internal_consult_overlay_csv'] = artifacts['csv']
    ptr['artifacts']['internal_consult_overlay_md'] = artifacts['md']
    ptr['artifacts']['internal_consult_overlay_guide'] = artifacts['guide']
    ptr['current_stage'] = 'internal_consult_overlay_completed'
    ptr['updated_at_utc'] = summary['finished_at_utc']
    ptr['guardrails'] = summary['guardrails']
    ptr['internal_consult_overlay'] = {
        'run_id': args.run_id,
        'decision_counts': decision_counts,
        'output_db': str(output_db),
        'guardrails': summary['guardrails'],
        'non_consultable_blocked_rows_after': totals_after['non_consultable_blocked_rows'],
        'identity_unresolved_rows_after': totals_after['identity_unresolved_rows'],
    }
    old_totals = ptr.get('totals') or {}
    ptr['totals'] = {**old_totals, **{k: v for k, v in totals_after.items() if k != 'status_counts'}}
    ptr['totals']['status_counts_current'] = totals_after['status_counts']
    POINTER.write_text(json.dumps(ptr, ensure_ascii=False, indent=2, sort_keys=True), encoding='utf-8')

    print(json.dumps({'summary': summary, 'artifacts': {'db': str(output_db), **artifacts, 'pointer': str(POINTER)}}, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
