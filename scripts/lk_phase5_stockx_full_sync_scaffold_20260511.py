#!/usr/bin/env python3
"""Add StockX/KicksDev full-sync scaffold to LK local SQLite.

This is intentionally non-destructive and does not scrape StockX/GOAT.
It creates the local SQL tables required by the LK OS PRD so the operational
DB is ready for a compliant StockX/KicksDev full sync once connector endpoint
and rate limits are validated.

No external writes. No raw PII. No secret values printed or stored.
"""
from __future__ import annotations

import base64
import csv
import json
import pathlib
import re
import sqlite3
import urllib.request
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
LOCAL_DB = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite')
DOPPLER_TOKEN_FILE = pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
APPROVAL_REPORT = ROOT / 'reports/lk-phase5-p1-final-approval-packet-2026-05-11.json'
SOURCING_CSV = ROOT / 'reports/lk-growth-ops/lk_stock_sourcing_signals_2026-05-11.csv'
OUT_MD = ROOT / 'reports/lk-phase5-stockx-full-sync-local-sql-scaffold-2026-05-11.md'
OUT_JSON = ROOT / 'reports/lk-phase5-stockx-full-sync-local-sql-scaffold-2026-05-11.json'


def load_secret_names() -> list[str]:
    token = DOPPLER_TOKEN_FILE.read_text().strip()
    req = urllib.request.Request(
        'https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json'
    )
    req.add_header('Authorization', 'Basic ' + base64.b64encode((token + ':').encode()).decode())
    with urllib.request.urlopen(req, timeout=60) as resp:
        secrets = json.load(resp)
    return sorted(k for k in secrets if any(term in k.upper() for term in ['STOCKX', 'KICKS', 'GOAT', 'DROPER']))


def normalize_model_query(title: str) -> str:
    text = str(title or '')
    text = re.sub(r'^Tênis\s+', '', text, flags=re.I)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def infer_size_system(title: str, size: str) -> str:
    # Conservative: LK stores BR/EU-like sizes. StockX/GOAT usually require US Men/Women
    # conversion before comparison, so every row starts as conversion_required.
    if not size:
        return 'unknown'
    return 'lk_br_eu_observed__stockx_conversion_required'


def read_candidate_products() -> list[dict]:
    candidates: dict[tuple[str, str], dict] = {}
    if APPROVAL_REPORT.exists():
        approval = json.loads(APPROVAL_REPORT.read_text())
        for g in approval.get('groups', []):
            key = (g.get('anchor_product') or '', '')
            if key[0]:
                candidates[key] = {
                    'source': 'p1_final_approval_packet',
                    'product_title': key[0],
                    'sku': '',
                    'size': '',
                    'priority_hint': g.get('status'),
                    'demand_signal': g.get('ready_recipients') or 0,
                }
    if SOURCING_CSV.exists():
        with SOURCING_CSV.open(newline='') as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader):
                if i >= 80:  # enough for scaffold; not a full market sync yet
                    break
                title = row.get('Produto') or row.get('product_title') or row.get('product_name') or row.get('Produto ') or ''
                sku = row.get('SKU') or row.get('sku') or ''
                size = row.get('Tam.') or row.get('size') or row.get('Tamanho') or ''
                key = (title, sku)
                if title:
                    candidates[key] = {
                        'source': 'stock_sourcing_signals_2026_05_11',
                        'product_title': title,
                        'sku': sku,
                        'size': size,
                        'priority_hint': row.get('Sinal') or row.get('signal') or '',
                        'demand_signal': row.get('Vend. 30d') or row.get('sold_30d') or '',
                    }
    return list(candidates.values())


def main() -> None:
    LOCAL_DB.parent.mkdir(parents=True, exist_ok=True)
    secret_names = load_secret_names()
    candidates = read_candidate_products()
    now = datetime.now(timezone.utc).isoformat()

    conn = sqlite3.connect(LOCAL_DB)
    cur = conn.cursor()
    cur.executescript(
        """
        PRAGMA journal_mode=WAL;
        CREATE TABLE IF NOT EXISTS external_market_sources (
            source_name TEXT PRIMARY KEY,
            source_type TEXT NOT NULL,
            credential_secret_name TEXT,
            access_status TEXT NOT NULL,
            sync_policy TEXT NOT NULL,
            notes TEXT,
            updated_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS market_product_identity (
            identity_id INTEGER PRIMARY KEY AUTOINCREMENT,
            lk_product_title TEXT NOT NULL,
            lk_sku TEXT,
            lk_size TEXT,
            normalized_query TEXT NOT NULL,
            stockx_product_id TEXT,
            stockx_slug TEXT,
            goat_product_id TEXT,
            kicksdev_product_id TEXT,
            identity_status TEXT NOT NULL,
            mapping_confidence TEXT NOT NULL,
            size_system_status TEXT NOT NULL,
            source_from TEXT NOT NULL,
            priority_hint TEXT,
            demand_signal TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            UNIQUE(lk_product_title, lk_sku, lk_size)
        );
        CREATE TABLE IF NOT EXISTS market_full_sync_runs (
            run_id TEXT PRIMARY KEY,
            source_name TEXT NOT NULL,
            run_type TEXT NOT NULL,
            status TEXT NOT NULL,
            started_at TEXT NOT NULL,
            finished_at TEXT,
            products_requested INTEGER DEFAULT 0,
            products_matched INTEGER DEFAULT 0,
            size_offers_upserted INTEGER DEFAULT 0,
            error_summary TEXT,
            notes TEXT
        );
        CREATE TABLE IF NOT EXISTS stockx_product_snapshots (
            snapshot_id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_id TEXT,
            identity_id INTEGER,
            stockx_product_id TEXT,
            stockx_slug TEXT,
            title TEXT,
            brand TEXT,
            colorway TEXT,
            retail_price_usd REAL,
            lowest_ask_usd REAL,
            highest_bid_usd REAL,
            last_sale_usd REAL,
            sales_last_72h INTEGER,
            sales_last_30d INTEGER,
            captured_at TEXT NOT NULL,
            raw_json_path TEXT
        );
        CREATE TABLE IF NOT EXISTS stockx_size_offers (
            offer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_id TEXT,
            identity_id INTEGER,
            stockx_product_id TEXT,
            stockx_size TEXT,
            stockx_size_system TEXT,
            lk_size_normalized TEXT,
            lowest_ask_usd REAL,
            highest_bid_usd REAL,
            last_sale_usd REAL,
            estimated_lk_landed_brl REAL,
            conversion_status TEXT NOT NULL,
            offer_status TEXT NOT NULL,
            captured_at TEXT NOT NULL,
            UNIQUE(run_id, identity_id, stockx_size, stockx_size_system)
        );
        CREATE TABLE IF NOT EXISTS sourcing_price_comparisons (
            comparison_id INTEGER PRIMARY KEY AUTOINCREMENT,
            identity_id INTEGER,
            lk_product_title TEXT NOT NULL,
            lk_sku TEXT,
            lk_size TEXT,
            droper_best_brl REAL,
            stockx_estimated_landed_brl REAL,
            goat_estimated_landed_brl REAL,
            cheapest_source TEXT,
            cheapest_price_brl REAL,
            comparison_status TEXT NOT NULL,
            reason TEXT,
            captured_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS size_conversion_rules (
            rule_id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand TEXT,
            category TEXT,
            source_size_system TEXT NOT NULL,
            source_size TEXT NOT NULL,
            lk_size TEXT NOT NULL,
            confidence TEXT NOT NULL,
            notes TEXT,
            UNIQUE(brand, category, source_size_system, source_size, lk_size)
        );
        CREATE TABLE IF NOT EXISTS market_sync_gaps (
            gap_id INTEGER PRIMARY KEY AUTOINCREMENT,
            gap_type TEXT NOT NULL,
            severity TEXT NOT NULL,
            affected_table TEXT,
            description TEXT NOT NULL,
            required_action TEXT NOT NULL,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL
        );
        """
    )

    sources = [
        ('StockX', 'market_price_inventory', 'KICKSDB_API_KEY', 'connector_scaffolded_not_full_synced', 'signal_triggered_full_sync_candidate', 'Use KicksDev/API-compatible source; direct forbidden scraping is blocked.'),
        ('GOAT', 'market_price_inventory', 'KICKSDB_API_KEY', 'connector_scaffolded_not_full_synced', 'signal_triggered_full_sync_candidate', 'Use KicksDev/API-compatible source where available; normalize US Men/Women before LK comparison.'),
        ('Droper', 'br_local_marketplace', None, 'connector_scaffolded_not_full_synced', 'signal_triggered_full_sync_candidate', 'Brazil local price comparison required before sourcing approval.'),
    ]
    for row in sources:
        cur.execute(
            'INSERT OR REPLACE INTO external_market_sources VALUES (?,?,?,?,?,?,?)',
            (*row, now),
        )

    inserted = 0
    for c in candidates:
        title = c.get('product_title') or ''
        sku = c.get('sku') or ''
        size = c.get('size') or ''
        cur.execute(
            """
            INSERT OR IGNORE INTO market_product_identity
            (lk_product_title, lk_sku, lk_size, normalized_query, stockx_product_id, stockx_slug, goat_product_id, kicksdev_product_id,
             identity_status, mapping_confidence, size_system_status, source_from, priority_hint, demand_signal, created_at, updated_at)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (title, sku, size, normalize_model_query(title), None, None, None, None,
             'needs_external_market_mapping', 'unmapped', infer_size_system(title, size), c.get('source') or '', str(c.get('priority_hint') or ''), str(c.get('demand_signal') or ''), now, now),
        )
        inserted += cur.rowcount

    run_id = 'stockx_full_sync_scaffold_2026_05_11'
    cur.execute(
        'INSERT OR REPLACE INTO market_full_sync_runs VALUES (?,?,?,?,?,?,?,?,?,?,?)',
        (run_id, 'StockX', 'schema_scaffold_and_candidate_queue', 'blocked_before_live_full_sync', now, now, len(candidates), 0, 0,
         'No live StockX/KicksDev product endpoint was validated in this run; API credential names exist but full sync not executed.',
         'This creates the local SQL contract required before running any compliant full sync.'),
    )

    gaps = [
        ('connector_endpoint', 'high', 'external_market_sources', 'KicksDev/StockX endpoint contract not validated in code yet.', 'Validate official endpoint/docs or existing connector; do not scrape forbidden StockX pages.', 'open'),
        ('size_conversion', 'high', 'size_conversion_rules', 'US Men vs US Women conversion must be explicit before comparing StockX/GOAT with LK/BR/EU sizes.', 'Create and verify brand/category size conversion matrix.', 'open'),
        ('pricing_inputs', 'medium', 'stockx_size_offers', 'Dollar/custo_trazer_usd should be configurable for estimated LK landed cost.', 'Move import formula inputs into local SQL config before live recommendations.', 'open'),
        ('source_comparison', 'medium', 'sourcing_price_comparisons', 'Droper/GOAT comparison tables exist but no live connectors have populated them.', 'Populate only after signal-triggered compliant search and approval boundaries.', 'open'),
    ]
    cur.executemany('DELETE FROM market_sync_gaps WHERE gap_type=? AND description=?', [(g[0], g[3]) for g in gaps])
    for gap in gaps:
        cur.execute('INSERT INTO market_sync_gaps (gap_type,severity,affected_table,description,required_action,status,created_at) VALUES (?,?,?,?,?,?,?)', (*gap, now))

    # Seed a few conservative conversion placeholders, intentionally not enough for decisions.
    for sys_name in ['US Men', 'US Women']:
        cur.execute(
            """
            DELETE FROM size_conversion_rules
            WHERE brand IS NULL AND category='sneakers' AND source_size_system=? AND source_size='TBD' AND lk_size='TBD'
            """,
            (sys_name,),
        )
        cur.execute(
            """
            INSERT INTO size_conversion_rules
            (brand, category, source_size_system, source_size, lk_size, confidence, notes)
            VALUES (?,?,?,?,?,?,?)
            """,
            (None, 'sneakers', sys_name, 'TBD', 'TBD', 'placeholder', 'Required before comparing StockX/GOAT sizes; do not use placeholder for pricing decisions.'),
        )

    conn.commit()
    counts = {}
    for table in ['external_market_sources', 'market_product_identity', 'market_full_sync_runs', 'stockx_product_snapshots', 'stockx_size_offers', 'sourcing_price_comparisons', 'size_conversion_rules', 'market_sync_gaps']:
        counts[table] = cur.execute(f'SELECT COUNT(*) FROM {table}').fetchone()[0]
    conn.close()
    LOCAL_DB.chmod(0o600)

    report = {
        'generated_at': now,
        'verdict': 'Local SQL was not complete for LK OS StockX full sync; scaffold has now been added, but live full sync is not executed yet.',
        'local_db': str(LOCAL_DB),
        'db_mode': oct(LOCAL_DB.stat().st_mode & 0o777),
        'secret_names_found': secret_names,
        'counts': counts,
        'guardrails': [
            'No StockX/GOAT scraping',
            'No external writes',
            'No secret values stored or printed',
            'No sourcing/contact/purchase',
            'Tables are schema/candidate scaffold until connector is validated',
        ],
        'next_steps': [
            'Validate official KicksDev/StockX connector endpoint and rate limits.',
            'Build explicit US Men/US Women → LK/BR/EU size conversion matrix.',
            'Populate stockx_product_snapshots and stockx_size_offers for signal-triggered candidate products.',
            'Compare Droper/StockX/GOAT landed cost before any sourcing recommendation.',
        ],
    }
    OUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    lines = [
        '# LK OS — StockX full sync scaffold no SQL local — 2026-05-11',
        '',
        '## Veredito',
        '',
        'O SQL local **não estava perfeito** para o PRD LK OS porque ainda não tinha as tabelas de full sync StockX/KicksDev/GOAT/Droper. Corrigi a estrutura local, mas **não executei full sync externo vivo** porque o conector/endpoints oficiais ainda precisam ser validados e scraping direto de StockX/GOAT é bloqueado pelo PRD.',
        '',
        '## Banco local',
        '',
        f'- SQLite: `{LOCAL_DB}`',
        f'- Permissão: `{oct(LOCAL_DB.stat().st_mode & 0o777)}`',
        '- Sem PII e sem secrets.',
        '',
        '## Tabelas adicionadas',
        '',
    ]
    for table, count in counts.items():
        lines.append(f'- `{table}`: {count}')
    lines += [
        '',
        '## Status das credenciais',
        '',
        f'- Secret names encontrados no Doppler: {", ".join(secret_names) if secret_names else "nenhum"}',
        '- Valores não foram impressos nem salvos.',
        '',
        '## Lacunas abertas antes do FULL SYNC real',
        '',
        '- Validar contrato oficial do endpoint KicksDev/StockX e limites de rate limit.',
        '- Criar matriz explícita US Men / US Women → LK/BR/EU por marca/categoria.',
        '- Popular snapshots por produto/tamanho somente via fonte permitida, sem scraping proibido.',
        '- Comparar Droper, StockX e GOAT com custo final LK antes de qualquer sourcing.',
        '',
        '## Guardrails',
        '',
        '- Nenhuma compra, contato, campanha, PO, Notion ou WhatsApp executado.',
        '- Nenhum write em Shopify/Tiny/Supabase.',
        '- Nenhum scraping direto de StockX/GOAT.',
    ]
    OUT_MD.write_text('\n'.join(lines) + '\n')
    print(json.dumps({'db': str(LOCAL_DB), 'mode': oct(LOCAL_DB.stat().st_mode & 0o777), 'counts': counts, 'report': str(OUT_MD)}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
