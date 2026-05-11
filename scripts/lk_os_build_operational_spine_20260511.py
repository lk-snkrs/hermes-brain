#!/usr/bin/env python3
"""Build LK OS local operational SQLite spine from read-only Supabase data.

Scope: people/customers, orders, order_items, products, variants, RFM and sync metadata.
No external writes. Secrets are fetched in-process from Doppler and never printed.
The SQLite DB is private (chmod 600) and may contain LK operational PII.
"""
from __future__ import annotations

import base64
import hashlib
import json
import pathlib
import sqlite3
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
DB = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite')
DOPPLER_TOKEN_FILE = pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
OUT_MD = ROOT / 'reports/lk-os-local-sql-operational-spine-2026-05-11.md'
OUT_JSON = ROOT / 'reports/lk-os-local-sql-operational-spine-2026-05-11.json'
PAGE = 1000


def doppler_secrets() -> dict[str, str]:
    token = DOPPLER_TOKEN_FILE.read_text().strip()
    req = urllib.request.Request(
        'https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json'
    )
    req.add_header('Authorization', 'Basic ' + base64.b64encode((token + ':').encode()).decode())
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)


def fetch_all(base_url: str, key: str, table: str, columns: list[str], order_col: str = 'id') -> list[dict[str, Any]]:
    headers = {
        'apikey': key,
        'Authorization': 'Bearer ' + key,
        'Accept': 'application/json',
        'Prefer': 'count=exact',
    }
    rows: list[dict[str, Any]] = []
    offset = 0
    select = ','.join(columns)
    while True:
        qs = urllib.parse.urlencode({'select': select, 'order': f'{order_col}.asc', 'limit': PAGE, 'offset': offset})
        req = urllib.request.Request(f'{base_url}/rest/v1/{table}?{qs}', headers=headers)
        with urllib.request.urlopen(req, timeout=120) as resp:
            batch = json.load(resp)
        if not batch:
            break
        rows.extend(batch)
        if len(batch) < PAGE:
            break
        offset += PAGE
    return rows


def jdump(v: Any) -> str | None:
    if v is None:
        return None
    if isinstance(v, str):
        return v
    return json.dumps(v, ensure_ascii=False, separators=(',', ':'))


def parse_raw(v: Any) -> Any:
    if v is None:
        return None
    if isinstance(v, (dict, list)):
        return v
    if isinstance(v, str):
        try:
            return json.loads(v)
        except Exception:
            return None
    return None


def norm_email(email: str | None) -> str:
    return (email or '').strip().lower()


def customer_ref(email: str | None, phone: str | None, cid: Any) -> str:
    basis = norm_email(email) or str(phone or '').strip() or str(cid or '')
    return hashlib.sha256(('lk|' + basis).encode()).hexdigest()[:16]


def init_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        PRAGMA journal_mode=WAL;
        CREATE TABLE IF NOT EXISTS lk_os_sync_runs (
            run_id TEXT PRIMARY KEY,
            source TEXT NOT NULL,
            status TEXT NOT NULL,
            started_at TEXT NOT NULL,
            finished_at TEXT,
            rows_customers INTEGER DEFAULT 0,
            rows_orders INTEGER DEFAULT 0,
            rows_order_items INTEGER DEFAULT 0,
            rows_products INTEGER DEFAULT 0,
            rows_variants INTEGER DEFAULT 0,
            rows_rfm INTEGER DEFAULT 0,
            notes TEXT
        );
        CREATE TABLE IF NOT EXISTS lk_customers (
            customer_id TEXT PRIMARY KEY,
            source TEXT,
            source_customer_id TEXT,
            customer_ref TEXT NOT NULL,
            email TEXT,
            phone TEXT,
            first_name TEXT,
            last_name TEXT,
            full_name TEXT,
            accepts_marketing INTEGER,
            tags TEXT,
            notes TEXT,
            tamanho_principal TEXT,
            orders_count INTEGER,
            total_spent REAL,
            first_order_at TEXT,
            last_order_at TEXT,
            customer_created_at TEXT,
            customer_updated_at TEXT,
            updated_at TEXT,
            raw_json TEXT
        );
        CREATE INDEX IF NOT EXISTS idx_lk_customers_ref ON lk_customers(customer_ref);
        CREATE INDEX IF NOT EXISTS idx_lk_customers_email ON lk_customers(email);

        CREATE TABLE IF NOT EXISTS lk_orders (
            order_id TEXT PRIMARY KEY,
            source TEXT,
            source_order_id TEXT,
            source_customer_id TEXT,
            customer_id TEXT,
            customer_ref TEXT,
            order_number TEXT,
            order_created_at TEXT,
            processed_at TEXT,
            financial_status TEXT,
            fulfillment_status TEXT,
            cancelled_at TEXT,
            currency TEXT,
            subtotal_price REAL,
            total_discount REAL,
            total_shipping REAL,
            total_tax REAL,
            total_price REAL,
            source_name TEXT,
            tags TEXT,
            note TEXT,
            updated_at TEXT
        );
        CREATE INDEX IF NOT EXISTS idx_lk_orders_customer_ref ON lk_orders(customer_ref);
        CREATE INDEX IF NOT EXISTS idx_lk_orders_created ON lk_orders(order_created_at);

        CREATE TABLE IF NOT EXISTS lk_order_items (
            item_id TEXT PRIMARY KEY,
            order_id TEXT,
            source_order_id TEXT,
            source_line_item_id TEXT,
            product_id TEXT,
            variant_id TEXT,
            source_product_id TEXT,
            source_variant_id TEXT,
            title TEXT,
            variant_title TEXT,
            sku TEXT,
            vendor TEXT,
            product_type TEXT,
            quantity INTEGER,
            unit_price REAL,
            compare_at_price REAL,
            total_discount REAL,
            line_subtotal REAL,
            line_total REAL,
            item_created_at TEXT,
            updated_at TEXT
        );
        CREATE INDEX IF NOT EXISTS idx_lk_order_items_sku ON lk_order_items(sku);
        CREATE INDEX IF NOT EXISTS idx_lk_order_items_product ON lk_order_items(product_id, variant_id);

        CREATE TABLE IF NOT EXISTS lk_products (
            product_id TEXT PRIMARY KEY,
            source TEXT,
            source_product_id TEXT,
            title TEXT,
            handle TEXT,
            vendor TEXT,
            product_type TEXT,
            status TEXT,
            tags TEXT,
            featured_image_url TEXT,
            editorial_email TEXT,
            body_html TEXT,
            product_created_at TEXT,
            product_updated_at TEXT,
            updated_at TEXT,
            raw_json TEXT
        );
        CREATE INDEX IF NOT EXISTS idx_lk_products_title ON lk_products(title);
        CREATE INDEX IF NOT EXISTS idx_lk_products_handle ON lk_products(handle);

        CREATE TABLE IF NOT EXISTS lk_product_variants (
            variant_id TEXT PRIMARY KEY,
            product_id TEXT,
            source_variant_id TEXT,
            source_product_id TEXT,
            title TEXT,
            sku TEXT,
            option1 TEXT,
            option2 TEXT,
            option3 TEXT,
            price REAL,
            compare_at_price REAL,
            inventory_quantity INTEGER,
            inventory_policy TEXT,
            barcode TEXT,
            position INTEGER,
            taxable INTEGER,
            requires_shipping INTEGER,
            grams REAL,
            weight REAL,
            weight_unit TEXT,
            is_active INTEGER,
            cost_price REAL,
            inventory_item_id TEXT,
            product_title TEXT,
            created_at TEXT,
            updated_at TEXT,
            raw_json TEXT
        );
        CREATE INDEX IF NOT EXISTS idx_lk_product_variants_sku ON lk_product_variants(sku);
        CREATE INDEX IF NOT EXISTS idx_lk_product_variants_product ON lk_product_variants(product_id);

        CREATE TABLE IF NOT EXISTS lk_customer_rfm (
            customer_id TEXT PRIMARY KEY,
            customer_ref TEXT,
            rfm_segment TEXT,
            r_score INTEGER,
            f_score INTEGER,
            m_score INTEGER,
            frequency_orders INTEGER,
            monetary_value REAL,
            recency_days INTEGER,
            last_order_at TEXT,
            updated_at TEXT
        );
        CREATE INDEX IF NOT EXISTS idx_lk_customer_rfm_segment ON lk_customer_rfm(rfm_segment);

        CREATE TABLE IF NOT EXISTS lk_os_entity_dictionary (
            entity_name TEXT PRIMARY KEY,
            source_of_truth TEXT NOT NULL,
            local_table TEXT NOT NULL,
            pii_level TEXT NOT NULL,
            notes TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );
        """
    )


def fnum(v: Any) -> float | None:
    if v in (None, ''):
        return None
    try:
        return float(v)
    except Exception:
        return None


def fint(v: Any) -> int | None:
    if v in (None, ''):
        return None
    try:
        return int(float(v))
    except Exception:
        return None


def main() -> None:
    started = datetime.now(timezone.utc).isoformat()
    run_id = 'lk_os_operational_spine_2026_05_11'
    sec = doppler_secrets()
    base_url = (sec['SUPABASE_LK_URL']).rstrip('/')
    key = sec['SUPABASE_LK_SERVICE_KEY']

    customers = fetch_all(base_url, key, 'customers', [
        'id','source','source_customer_id','email','phone','first_name','last_name','full_name','accepts_marketing','tags','notes','tamanho_principal','orders_count','total_spent','first_order_at','last_order_at','customer_created_at','customer_updated_at','updated_at','raw'
    ])
    orders = fetch_all(base_url, key, 'orders', [
        'id','source','source_order_id','source_customer_id','customer_id','email','phone','order_number','order_created_at','processed_at','financial_status','fulfillment_status','cancelled_at','currency','subtotal_price','total_discount','total_shipping','total_tax','total_price','source_name','tags','note','updated_at'
    ])
    items = fetch_all(base_url, key, 'order_items', [
        'id','order_id','source_order_id','source_line_item_id','product_id','variant_id','source_product_id','source_variant_id','title','variant_title','sku','vendor','product_type','quantity','unit_price','compare_at_price','total_discount','line_subtotal','line_total','item_created_at','updated_at'
    ])
    products = fetch_all(base_url, key, 'products', [
        'id','source','source_product_id','title','handle','vendor','product_type','status','tags','featured_image_url','editorial_email','body_html','product_created_at','product_updated_at','updated_at','raw'
    ])
    variants_source = fetch_all(base_url, key, 'product_variants', [
        'id','product_id','shopify_product_id','shopify_variant_id','source_variant_id','inventory_item_id','product_title','title','sku','vendor','option1','option2','option3','price','compare_at_price','cost_price','inventory_quantity','barcode','requires_shipping','taxable','weight','weight_unit','is_active','created_at','updated_at'
    ])
    rfm = fetch_all(base_url, key, 'customer_rfm', [
        'customer_id','rfm_segment','r_score','f_score','m_score','frequency_orders','monetary_value','recency_days','last_order_at','updated_at'
    ], order_col='customer_id')

    # Customer lookup for refs on orders/RFM.
    by_id = {str(c.get('id')): c for c in customers}
    by_source_customer_id = {str(c.get('source_customer_id')): c for c in customers if c.get('source_customer_id') is not None}

    DB.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB)
    init_schema(conn)
    for col, ddl in [
        ('is_active', 'ALTER TABLE lk_product_variants ADD COLUMN is_active INTEGER'),
        ('cost_price', 'ALTER TABLE lk_product_variants ADD COLUMN cost_price REAL'),
        ('inventory_item_id', 'ALTER TABLE lk_product_variants ADD COLUMN inventory_item_id TEXT'),
        ('product_title', 'ALTER TABLE lk_product_variants ADD COLUMN product_title TEXT'),
    ]:
        existing_cols = [r[1] for r in conn.execute('PRAGMA table_info(lk_product_variants)').fetchall()]
        if col not in existing_cols:
            conn.execute(ddl)
    cur = conn.cursor()

    for table in ['lk_customers','lk_orders','lk_order_items','lk_products','lk_product_variants','lk_customer_rfm']:
        cur.execute(f'DELETE FROM {table}')

    for c in customers:
        cref = customer_ref(c.get('email'), c.get('phone'), c.get('id'))
        cur.execute(
            """INSERT OR REPLACE INTO lk_customers VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (str(c.get('id')), c.get('source'), str(c.get('source_customer_id') or ''), cref, norm_email(c.get('email')) or None, c.get('phone'), c.get('first_name'), c.get('last_name'), c.get('full_name'), 1 if c.get('accepts_marketing') else 0, jdump(c.get('tags')), c.get('notes'), c.get('tamanho_principal'), fint(c.get('orders_count')), fnum(c.get('total_spent')), c.get('first_order_at'), c.get('last_order_at'), c.get('customer_created_at'), c.get('customer_updated_at'), c.get('updated_at'), jdump(c.get('raw'))),
        )

    for o in orders:
        c = by_id.get(str(o.get('customer_id'))) or by_source_customer_id.get(str(o.get('source_customer_id')))
        cref = customer_ref((c or {}).get('email') or o.get('email'), (c or {}).get('phone') or o.get('phone'), o.get('customer_id') or o.get('source_customer_id'))
        cur.execute(
            """INSERT OR REPLACE INTO lk_orders VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (str(o.get('id')), o.get('source'), str(o.get('source_order_id') or ''), str(o.get('source_customer_id') or ''), str(o.get('customer_id') or ''), cref, str(o.get('order_number') or ''), o.get('order_created_at'), o.get('processed_at'), o.get('financial_status'), o.get('fulfillment_status'), o.get('cancelled_at'), o.get('currency'), fnum(o.get('subtotal_price')), fnum(o.get('total_discount')), fnum(o.get('total_shipping')), fnum(o.get('total_tax')), fnum(o.get('total_price')), o.get('source_name'), jdump(o.get('tags')), o.get('note'), o.get('updated_at')),
        )

    for it in items:
        cur.execute(
            """INSERT OR REPLACE INTO lk_order_items VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (str(it.get('id')), str(it.get('order_id') or ''), str(it.get('source_order_id') or ''), str(it.get('source_line_item_id') or ''), str(it.get('product_id') or ''), str(it.get('variant_id') or ''), str(it.get('source_product_id') or ''), str(it.get('source_variant_id') or ''), it.get('title'), it.get('variant_title'), it.get('sku'), it.get('vendor'), it.get('product_type'), fint(it.get('quantity')), fnum(it.get('unit_price')), fnum(it.get('compare_at_price')), fnum(it.get('total_discount')), fnum(it.get('line_subtotal')), fnum(it.get('line_total')), it.get('item_created_at'), it.get('updated_at')),
        )

    variant_count = 0
    for p in products:
        cur.execute(
            """INSERT OR REPLACE INTO lk_products VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (str(p.get('id')), p.get('source'), str(p.get('source_product_id') or ''), p.get('title'), p.get('handle'), p.get('vendor'), p.get('product_type'), p.get('status'), jdump(p.get('tags')), p.get('featured_image_url'), p.get('editorial_email'), p.get('body_html'), p.get('product_created_at'), p.get('product_updated_at'), p.get('updated_at'), jdump(p.get('raw'))),
        )

    for v in variants_source:
        vid = v.get('id') or v.get('shopify_variant_id') or v.get('source_variant_id')
        if not vid:
            continue
        cur.execute(
            """INSERT OR REPLACE INTO lk_product_variants VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (str(vid), str(v.get('product_id') or ''), str(v.get('source_variant_id') or v.get('shopify_variant_id') or vid), str(v.get('shopify_product_id') or ''), v.get('title'), v.get('sku'), v.get('option1'), v.get('option2'), v.get('option3'), fnum(v.get('price')), fnum(v.get('compare_at_price')), fint(v.get('inventory_quantity')), None, v.get('barcode'), None, 1 if v.get('taxable') else 0, 1 if v.get('requires_shipping') else 0, None, fnum(v.get('weight')), v.get('weight_unit'), 1 if v.get('is_active') else 0, fnum(v.get('cost_price')), str(v.get('inventory_item_id') or ''), v.get('product_title'), v.get('created_at'), v.get('updated_at'), jdump(v)),
        )
        variant_count += 1

    for r in rfm:
        c = by_id.get(str(r.get('customer_id')))
        cref = customer_ref((c or {}).get('email'), (c or {}).get('phone'), r.get('customer_id'))
        cur.execute(
            """INSERT OR REPLACE INTO lk_customer_rfm VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
            (str(r.get('customer_id')), cref, r.get('rfm_segment'), fint(r.get('r_score')), fint(r.get('f_score')), fint(r.get('m_score')), fint(r.get('frequency_orders')), fnum(r.get('monetary_value')), fint(r.get('recency_days')), r.get('last_order_at'), r.get('updated_at')),
        )

    dictionary = [
        ('customer', 'Supabase customers / Shopify customer source', 'lk_customers', 'PII_PRIVATE_LOCAL', 'Clientes/pessoas da LK; permitido apenas no SQLite chmod 600, não em relatórios públicos.'),
        ('order', 'Supabase orders / Shopify order source', 'lk_orders', 'PII_MINIMIZED_PRIVATE_LOCAL', 'Pedidos com customer_ref; endereços não materializados nesta versão.'),
        ('order_item', 'Supabase order_items', 'lk_order_items', 'NO_DIRECT_PII', 'Itens vendidos por produto/SKU/tamanho quando disponível.'),
        ('product', 'Supabase products / Shopify catalog source', 'lk_products', 'NO_DIRECT_PII', 'Catálogo de produtos LK.'),
        ('variant', 'Shopify product raw variants via Supabase products', 'lk_product_variants', 'NO_DIRECT_PII', 'Variantes/tamanho/SKU; estoque Shopify apenas sinal fraco, Tiny é verdade.'),
        ('rfm', 'Supabase customer_rfm', 'lk_customer_rfm', 'PII_LINKED_PRIVATE_LOCAL', 'Scores e segmento CRM para operação interna.'),
        ('stock', 'Tiny LK | CONTROLE ESTOQUE snapshots', 'tiny_anchor_stock', 'NO_DIRECT_PII', 'Verdade de disponibilidade vem do Tiny, não Shopify.'),
        ('sourcing_quote', 'GOAT/Droper/StockX/KicksDev on-demand', 'future_on_demand_quote_log', 'NO_DIRECT_PII', 'Não fazer full sync permanente de preço externo; registrar só evidência por decisão.'),
    ]
    now = datetime.now(timezone.utc).isoformat()
    for row in dictionary:
        cur.execute('INSERT OR REPLACE INTO lk_os_entity_dictionary VALUES (?,?,?,?,?,?)', (*row, now))

    cur.execute('INSERT OR REPLACE INTO lk_os_sync_runs VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', (
        run_id, 'Supabase LK REST read-only', 'completed', started, now, len(customers), len(orders), len(items), len(products), variant_count, len(rfm), 'Operational spine: people/customers + products + orders/RFM; no external writes.'
    ))
    conn.commit()

    counts = {}
    for t in ['lk_customers','lk_orders','lk_order_items','lk_products','lk_product_variants','lk_customer_rfm','lk_os_entity_dictionary']:
        counts[t] = cur.execute(f'SELECT COUNT(*) FROM {t}').fetchone()[0]
    # Useful QA without exposing PII.
    qa = {
        'customers_with_email': cur.execute('SELECT COUNT(*) FROM lk_customers WHERE email IS NOT NULL AND email != ""').fetchone()[0],
        'customers_with_phone': cur.execute('SELECT COUNT(*) FROM lk_customers WHERE phone IS NOT NULL AND phone != ""').fetchone()[0],
        'variants_with_sku': cur.execute('SELECT COUNT(*) FROM lk_product_variants WHERE sku IS NOT NULL AND sku != ""').fetchone()[0],
        'orders_paid_like': cur.execute("SELECT COUNT(*) FROM lk_orders WHERE financial_status IN ('paid','partially_paid','authorized') AND cancelled_at IS NULL").fetchone()[0],
    }
    conn.close()
    DB.chmod(0o600)

    report = {
        'generated_at': now,
        'db': str(DB),
        'mode': oct(DB.stat().st_mode & 0o777),
        'source': 'Supabase LK REST read-only',
        'counts': counts,
        'qa': qa,
        'guardrails': ['No external writes', 'No customer send', 'No secrets printed', 'PII only in private chmod 600 SQLite, not in report'],
    }
    OUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    lines = [
        '# LK OS — SQL local operational spine — 2026-05-11', '',
        '## Veredito', '',
        'O SQL local agora foi ampliado para o coração operacional correto: pessoas/clientes + pedidos + itens + produtos + variantes + RFM. GOAT/Droper/StockX continuam como consulta on-demand, não como full sync permanente de preço externo.', '',
        '## Banco', '', f'- SQLite: `{DB}`', f'- Permissão: `{oct(DB.stat().st_mode & 0o777)}`', '- Fonte: Supabase LK REST em modo read-only.', '',
        '## Contagens materializadas', '',
    ]
    for k, v in counts.items():
        lines.append(f'- `{k}`: {v}')
    lines += ['', '## QA sem PII', '']
    for k, v in qa.items():
        lines.append(f'- `{k}`: {v}')
    lines += ['', '## Guardrails', '', '- Nenhum write externo.', '- Nenhum envio/campanha.', '- Nenhum segredo impresso.', '- PII fica apenas no SQLite privado chmod 600; relatórios do Brain usam contagens/agregados.']
    OUT_MD.write_text('\n'.join(lines) + '\n')
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
