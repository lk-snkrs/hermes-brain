#!/usr/bin/env python3
"""Build LK Phase 5 local SQLite operational cache.

Safe local DB convention:
- outside git repo under /opt/data/hermes_bruno_ingest/local_sql/
- no raw email/name/phone/address
- stores hashed customer refs, queue readiness, Tiny stock checks, and report metadata
- source for campaign planning/approval, not source of truth
"""
from __future__ import annotations

import json
import pathlib
import sqlite3
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
LOCAL_DB = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite')
PRIVATE_IDS = pathlib.Path('/opt/data/hermes_bruno_ingest/private_exports/lk_crm/lk_phase5_p1_recipient_ids_2026-05-11.json')
STOCK_REPORT = ROOT / 'reports/lk-phase5-p1-recipients-stock-guard-2026-05-11.json'
APPROVAL_REPORT = ROOT / 'reports/lk-phase5-p1-final-approval-packet-2026-05-11.json'


def main() -> None:
    LOCAL_DB.parent.mkdir(parents=True, exist_ok=True)
    stock = json.loads(STOCK_REPORT.read_text())
    approval = json.loads(APPROVAL_REPORT.read_text())
    private = json.loads(PRIVATE_IDS.read_text()) if PRIVATE_IDS.exists() else {"candidate_rows": []}

    conn = sqlite3.connect(LOCAL_DB)
    cur = conn.cursor()
    cur.executescript(
        """
        PRAGMA journal_mode=WAL;
        CREATE TABLE IF NOT EXISTS metadata (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS p1_candidate_recipients (
            customer_ref TEXT NOT NULL,
            segment TEXT NOT NULL,
            anchor_product TEXT NOT NULL,
            anchor_size TEXT,
            anchor_sku TEXT,
            last_anchor_order_at TEXT,
            r_score INTEGER,
            f_score INTEGER,
            m_score INTEGER,
            frequency_orders INTEGER,
            monetary_value REAL,
            recency_days INTEGER,
            has_email INTEGER,
            has_phone INTEGER,
            accepts_marketing TEXT,
            PRIMARY KEY (customer_ref, segment, anchor_product)
        );
        CREATE TABLE IF NOT EXISTS p1_group_readiness (
            group_key TEXT PRIMARY KEY,
            live_candidate_count INTEGER NOT NULL,
            ready_with_same_size_stock INTEGER NOT NULL,
            blocked_by_stock_or_mapping INTEGER NOT NULL,
            campaign_gate TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS tiny_anchor_stock (
            anchor_product TEXT NOT NULL,
            size TEXT NOT NULL,
            sku TEXT,
            status TEXT NOT NULL,
            available_estimated_total REAL NOT NULL,
            match_count INTEGER NOT NULL,
            PRIMARY KEY (anchor_product, size, sku)
        );
        CREATE TABLE IF NOT EXISTS final_approval_groups (
            group_key TEXT PRIMARY KEY,
            segment TEXT NOT NULL,
            anchor_product TEXT NOT NULL,
            ready_recipients INTEGER NOT NULL,
            blocked_recipients INTEGER NOT NULL,
            status TEXT NOT NULL,
            recommended_channel_action TEXT NOT NULL,
            copy_angle TEXT NOT NULL
        );
        """
    )
    cur.execute('DELETE FROM p1_candidate_recipients')
    cur.execute('DELETE FROM p1_group_readiness')
    cur.execute('DELETE FROM tiny_anchor_stock')
    cur.execute('DELETE FROM final_approval_groups')

    for row in private.get('candidate_rows', []):
        rfm = row.get('rfm') or {}
        flags = row.get('contact_flags') or {}
        cur.execute(
            """
            INSERT OR REPLACE INTO p1_candidate_recipients VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                row.get('customer_ref'), row.get('segment'), row.get('anchor_product'), row.get('anchor_size'), row.get('anchor_sku'), row.get('last_anchor_order_at'),
                rfm.get('r_score'), rfm.get('f_score'), rfm.get('m_score'), rfm.get('frequency_orders'), rfm.get('monetary_value'), rfm.get('recency_days'),
                int(bool(flags.get('has_email'))), int(bool(flags.get('has_phone'))), str(flags.get('accepts_marketing')),
            ),
        )

    for group_key, row in stock.get('readiness_by_group', {}).items():
        cur.execute(
            'INSERT OR REPLACE INTO p1_group_readiness VALUES (?,?,?,?,?)',
            (group_key, row.get('live_candidate_count') or 0, row.get('ready_with_same_size_stock') or 0, row.get('blocked_by_stock_or_mapping') or 0, row.get('campaign_gate') or ''),
        )

    for anchor, block in stock.get('tiny_stock_by_anchor', {}).items():
        for v in block.get('variant_checks', []):
            cur.execute(
                'INSERT OR REPLACE INTO tiny_anchor_stock VALUES (?,?,?,?,?,?)',
                (anchor, str(v.get('size') or ''), v.get('sku') or '', v.get('status') or '', float(v.get('available_estimated_total') or 0), int(v.get('match_count') or 0)),
            )

    for row in approval.get('groups', []):
        cur.execute(
            'INSERT OR REPLACE INTO final_approval_groups VALUES (?,?,?,?,?,?,?,?)',
            (row.get('group'), row.get('segment'), row.get('anchor_product'), row.get('ready_recipients') or 0, row.get('blocked_recipients') or 0, row.get('status') or '', row.get('recommended_channel_action') or '', row.get('copy_angle') or ''),
        )

    now = datetime.now(timezone.utc).isoformat()
    metadata = {
        'scope': 'LK Phase 5 local SQLite operational cache; no raw PII; source of truth remains Shopify/Supabase/Tiny.',
        'generated_at': now,
        'stock_report': str(STOCK_REPORT),
        'approval_report': str(APPROVAL_REPORT),
        'private_ids_source': str(PRIVATE_IDS),
    }
    for k, v in metadata.items():
        cur.execute('INSERT OR REPLACE INTO metadata VALUES (?,?,?)', (k, v, now))

    conn.commit()
    counts = {}
    for table in ['p1_candidate_recipients', 'p1_group_readiness', 'tiny_anchor_stock', 'final_approval_groups']:
        counts[table] = cur.execute(f'SELECT COUNT(*) FROM {table}').fetchone()[0]
    conn.close()
    LOCAL_DB.chmod(0o600)
    print(json.dumps({'db': str(LOCAL_DB), 'mode': oct(LOCAL_DB.stat().st_mode & 0o777), 'counts': counts}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
