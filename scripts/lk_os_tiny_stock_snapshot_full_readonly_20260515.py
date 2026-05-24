#!/usr/bin/env python3
"""LK OS Tiny full stock snapshot, read-only.

Creates a resumable local SQLite snapshot of Tiny products/stock by SKU/size/deposit and
recalculates a derived LK commercial stock state for Shopify variants. No Tiny/Shopify writes.

Safe defaults:
- Full product list is pulled via produtos.pesquisa with empty search.
- Stock is checked via produto.obter.estoque for Tiny rows with codigo.
- API pacing is conservative and resumable by run_id.
- Outputs stay local/private for raw operational rows; public MD/JSON is aggregate only.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import pathlib
import re
import shutil
import sqlite3
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
DB = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite')
BACKUP_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_os_backups')
PRIVATE_DIR = pathlib.Path('/opt/data/hermes_bruno_ingest/local_sql/lk_tiny_stock_snapshots')
REPORT_JSON = ROOT / 'reports/lk-os-tiny-stock-snapshot-full-readonly-2026-05-15.json'
REPORT_MD = ROOT / 'areas/lk/rotinas/lk-os-tiny-stock-snapshot-full-readonly-2026-05-15.md'
DOPPLER_TOKEN_FILE = pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token')
OFFICIAL_DEPOSIT = 'LK | CONTROLE ESTOQUE'
DEFAULT_DELAY = 1.0
MIN_STOCK_DELAY = 1.0
MAX_RETRIES = 4


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def slug_ts() -> str:
    return datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')


def load_secrets() -> dict[str, str]:
    token = DOPPLER_TOKEN_FILE.read_text().strip()
    req = urllib.request.Request(
        'https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json'
    )
    req.add_header('Authorization', 'Basic ' + base64.b64encode((token + ':').encode()).decode())
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)


def tiny_call(token: str, method: str, params: dict[str, Any], delay: float) -> dict[str, Any]:
    if delay > 0:
        time.sleep(delay)
    last: dict[str, Any] | None = None
    for attempt in range(1, MAX_RETRIES + 1):
        started = time.perf_counter()
        data = urllib.parse.urlencode({**params, 'token': token, 'formato': 'json'}).encode()
        req = urllib.request.Request(f'https://api.tiny.com.br/api2/{method}.php', data=data, method='POST')
        try:
            with urllib.request.urlopen(req, timeout=90) as resp:
                body = json.load(resp)
            retorno = (body or {}).get('retorno') or {}
            latency = int((time.perf_counter() - started) * 1000)
            out = {
                'ok': True,
                'http_status': resp.status,
                'tiny_status': retorno.get('status'),
                'tiny_erros': retorno.get('erros'),
                'latency_ms': latency,
                'body': body,
            }
            # Tiny may return status=Erro inside HTTP 200 during throttles; retry those.
            if retorno.get('status') == 'OK':
                return out
            last = out
        except urllib.error.HTTPError as exc:
            raw = exc.read().decode(errors='replace')
            last = {'ok': False, 'http_status': exc.code, 'tiny_status': None, 'error': 'HTTPError', 'message': raw[:500]}
        except Exception as exc:  # noqa: BLE001
            last = {'ok': False, 'http_status': None, 'tiny_status': None, 'error': type(exc).__name__, 'message': str(exc)[:500]}
        time.sleep(min(12, 1.5 * attempt))
    return last or {'ok': False, 'error': 'unknown'}


def norm_sku(s: Any) -> str:
    return re.sub(r'[^a-z0-9]+', '', str(s or '').lower())


def parse_size_from_name(name: Any) -> str | None:
    text = str(name or '').strip()
    if ' - ' in text:
        tail = text.rsplit(' - ', 1)[-1].strip()
        return tail or None
    m = re.search(r'(?:^|\s)(\d{2}(?:[\.,]5)?|PP|P|M|G|GG|XG|XXG|XS|S|L|XL|XXL|Único|Unico)(?:\s|$)', text, re.I)
    if m:
        return m.group(1).replace(',', '.')
    return None


def ensure_dirs() -> None:
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE_DIR, 0o700)
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)


def backup_db() -> pathlib.Path:
    ensure_dirs()
    backup = BACKUP_DIR / f'lk_os_phase5_before_tiny_stock_snapshot_full_readonly_{slug_ts()}.sqlite'
    shutil.copy2(DB, backup)
    os.chmod(backup, 0o600)
    return backup


def connect() -> sqlite3.Connection:
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    return con


def init_schema(con: sqlite3.Connection) -> None:
    con.executescript(
        '''
        create table if not exists lk_tiny_stock_snapshot_runs (
          run_id text primary key,
          started_at text not null,
          finished_at text,
          status text not null,
          mode text not null,
          official_deposit text not null,
          total_pages integer,
          products_listed_count integer default 0,
          stock_checked_count integer default 0,
          stock_error_count integer default 0,
          notes text,
          source_labels text not null,
          not_performed text not null
        );
        create table if not exists lk_tiny_stock_products (
          run_id text not null,
          tiny_id text not null,
          codigo text,
          normalized_codigo text,
          nome text,
          parsed_size text,
          situacao text,
          preco real,
          pagina integer,
          listed_at text,
          raw_json text,
          primary key(run_id, tiny_id)
        );
        create index if not exists idx_lk_tiny_stock_products_run_codigo on lk_tiny_stock_products(run_id, normalized_codigo);
        create table if not exists lk_tiny_stock_deposits (
          run_id text not null,
          tiny_id text not null,
          codigo text,
          normalized_codigo text,
          nome text,
          parsed_size text,
          situacao text,
          saldo_total real,
          saldo_reservado real,
          saldo_disponivel_estimado real,
          deposito_nome text,
          deposito_saldo real,
          deposito_desconsiderar text,
          checked_at text,
          tiny_status text,
          http_status integer,
          latency_ms integer,
          error text,
          raw_deposit_json text,
          primary key(run_id, tiny_id, deposito_nome)
        );
        create index if not exists idx_lk_tiny_stock_deposits_run_codigo on lk_tiny_stock_deposits(run_id, normalized_codigo);
        create table if not exists lk_variant_commercial_state (
          variant_id text primary key,
          product_id text,
          source_variant_id text,
          product_title text,
          variant_title text,
          sku text,
          normalized_size text,
          current_price real,
          shopify_is_active integer,
          dq_status text,
          tiny_run_id text,
          tiny_match_count integer,
          tiny_official_available real,
          tiny_total_available real,
          tiny_status text,
          commercial_state text,
          blocker text,
          source_labels text,
          last_recalculated_at text
        );
        '''
    )
    con.commit()


def create_run(con: sqlite3.Connection, run_id: str, mode: str) -> None:
    con.execute(
        '''insert or ignore into lk_tiny_stock_snapshot_runs
           (run_id, started_at, status, mode, official_deposit, source_labels, not_performed)
           values (?, ?, ?, ?, ?, ?, ?)''',
        (
            run_id,
            now(),
            'running',
            mode,
            OFFICIAL_DEPOSIT,
            json.dumps(['fact_tiny_stock', 'derived_reconciliation'], ensure_ascii=False),
            json.dumps(['tiny_write', 'shopify_write', 'inventory_change', 'price_change', 'supplier_contact', 'purchase', 'campaign_or_external_send'], ensure_ascii=False),
        ),
    )
    con.commit()


def list_products(con: sqlite3.Connection, token: str, run_id: str, delay: float, max_pages: int | None) -> int:
    # Resume: skip pages already fully inserted if interrupted.
    first = tiny_call(token, 'produtos.pesquisa', {'pesquisa': '', 'pagina': 1}, delay)
    ret = ((first.get('body') or {}).get('retorno') or {}) if first.get('body') else {}
    if ret.get('status') != 'OK':
        raise RuntimeError(f'Tiny list page 1 failed: {first.get("error") or ret.get("erros") or first.get("message")}')
    total_pages = int(ret.get('numero_paginas') or 1)
    if max_pages:
        total_pages = min(total_pages, max_pages)
    con.execute('update lk_tiny_stock_snapshot_runs set total_pages=? where run_id=?', (total_pages, run_id))
    con.commit()

    def insert_page(page: int, retorno: dict[str, Any]) -> int:
        rows = retorno.get('produtos') or []
        n = 0
        for item in rows:
            p = (item or {}).get('produto') or {}
            tiny_id = str(p.get('id') or '').strip()
            if not tiny_id:
                continue
            codigo = str(p.get('codigo') or '').strip()
            nome = str(p.get('nome') or '').strip()
            con.execute(
                '''insert or replace into lk_tiny_stock_products
                   (run_id,tiny_id,codigo,normalized_codigo,nome,parsed_size,situacao,preco,pagina,listed_at,raw_json)
                   values (?,?,?,?,?,?,?,?,?,?,?)''',
                (run_id, tiny_id, codigo, norm_sku(codigo), nome, parse_size_from_name(nome), p.get('situacao'), safe_float(p.get('preco')), page, now(), json.dumps(p, ensure_ascii=False)),
            )
            n += 1
        return n

    listed = insert_page(1, ret)
    con.commit()
    for page in range(2, total_pages + 1):
        existing = con.execute('select count(*) c from lk_tiny_stock_products where run_id=? and pagina=?', (run_id, page)).fetchone()['c']
        if existing > 0:
            continue
        res = tiny_call(token, 'produtos.pesquisa', {'pesquisa': '', 'pagina': page}, delay)
        retorno = ((res.get('body') or {}).get('retorno') or {}) if res.get('body') else {}
        if retorno.get('status') != 'OK':
            con.execute('update lk_tiny_stock_snapshot_runs set stock_error_count=stock_error_count+1, notes=? where run_id=?', (f'list page {page} failed: {res.get("error") or retorno.get("erros") or res.get("message")}', run_id))
            con.commit()
            continue
        listed += insert_page(page, retorno)
        if page % 10 == 0:
            con.execute('update lk_tiny_stock_snapshot_runs set products_listed_count=(select count(*) from lk_tiny_stock_products where run_id=?) where run_id=?', (run_id, run_id))
            con.commit()
    con.execute('update lk_tiny_stock_snapshot_runs set products_listed_count=(select count(*) from lk_tiny_stock_products where run_id=?) where run_id=?', (run_id, run_id))
    con.commit()
    return listed


def safe_float(x: Any) -> float | None:
    if x is None or x == '':
        return None
    try:
        return float(str(x).replace(',', '.'))
    except Exception:
        return None


def stock_rows_to_check(con: sqlite3.Connection, run_id: str, limit: int | None) -> list[sqlite3.Row]:
    sql = '''
      select p.*
      from lk_tiny_stock_products p
      left join lk_tiny_stock_deposits d on d.run_id=p.run_id and d.tiny_id=p.tiny_id
      where p.run_id=? and coalesce(p.codigo,'')<>'' and d.tiny_id is null
      order by p.pagina, p.tiny_id
    '''
    if limit:
        sql += f' limit {int(limit)}'
    return con.execute(sql, (run_id,)).fetchall()


def check_stock(con: sqlite3.Connection, token: str, run_id: str, delay: float, limit: int | None) -> None:
    rows = stock_rows_to_check(con, run_id, limit)
    for idx, row in enumerate(rows, 1):
        res = tiny_call(token, 'produto.obter.estoque', {'id': row['tiny_id']}, delay)
        retorno = ((res.get('body') or {}).get('retorno') or {}) if res.get('body') else {}
        error_text = json.dumps(res.get('tiny_erros') or res.get('error') or res.get('message') or retorno.get('erros'), ensure_ascii=False)
        if retorno.get('status') != 'OK' and ('API Bloqueada' in error_text or 'Excedido o número de acessos' in error_text):
            con.execute(
                '''update lk_tiny_stock_snapshot_runs
                   set status='partial_api_rate_limited', notes=?,
                       stock_checked_count=(select count(distinct tiny_id) from lk_tiny_stock_deposits where run_id=?),
                       stock_error_count=(select count(distinct tiny_id) from lk_tiny_stock_deposits where run_id=? and error is not null)
                   where run_id=?''',
                ('Tiny rate limit/bloqueio detectado; execução pausada para não pressionar API. Use resume após cooldown com delay maior.', run_id, run_id, run_id),
            )
            con.commit()
            print(json.dumps({'run_id': run_id, 'paused': 'tiny_api_rate_limited', 'checked_this_process': idx-1}, ensure_ascii=False), flush=True)
            break
        p = retorno.get('produto') or {}
        deposits = p.get('depositos') or []
        saldo = safe_float(p.get('saldo'))
        reservado = safe_float(p.get('saldoReservado')) or 0.0
        disponivel = max((saldo or 0.0) - reservado, 0.0) if saldo is not None else None
        base = {
            'run_id': run_id,
            'tiny_id': str(p.get('id') or row['tiny_id']),
            'codigo': str(p.get('codigo') or row['codigo'] or '').strip(),
            'normalized_codigo': norm_sku(p.get('codigo') or row['codigo']),
            'nome': str(p.get('nome') or row['nome'] or '').strip(),
            'parsed_size': parse_size_from_name(p.get('nome') or row['nome']),
            'situacao': p.get('situacao') or row['situacao'],
            'saldo_total': saldo,
            'saldo_reservado': reservado,
            'saldo_disponivel_estimado': disponivel,
            'checked_at': now(),
            'tiny_status': retorno.get('status') or res.get('tiny_status'),
            'http_status': res.get('http_status'),
            'latency_ms': res.get('latency_ms'),
            'error': None if retorno.get('status') == 'OK' else json.dumps(res.get('tiny_erros') or res.get('error') or res.get('message'), ensure_ascii=False),
        }
        if deposits:
            for item in deposits:
                dep = (item or {}).get('deposito') or {}
                con.execute(
                    '''insert or replace into lk_tiny_stock_deposits
                       (run_id,tiny_id,codigo,normalized_codigo,nome,parsed_size,situacao,saldo_total,saldo_reservado,saldo_disponivel_estimado,deposito_nome,deposito_saldo,deposito_desconsiderar,checked_at,tiny_status,http_status,latency_ms,error,raw_deposit_json)
                       values (:run_id,:tiny_id,:codigo,:normalized_codigo,:nome,:parsed_size,:situacao,:saldo_total,:saldo_reservado,:saldo_disponivel_estimado,:deposito_nome,:deposito_saldo,:deposito_desconsiderar,:checked_at,:tiny_status,:http_status,:latency_ms,:error,:raw_deposit_json)''',
                    {**base, 'deposito_nome': dep.get('nome') or '__NO_DEPOSIT_NAME__', 'deposito_saldo': safe_float(dep.get('saldo')), 'deposito_desconsiderar': dep.get('desconsiderar'), 'raw_deposit_json': json.dumps(dep, ensure_ascii=False)},
                )
        else:
            con.execute(
                '''insert or replace into lk_tiny_stock_deposits
                   (run_id,tiny_id,codigo,normalized_codigo,nome,parsed_size,situacao,saldo_total,saldo_reservado,saldo_disponivel_estimado,deposito_nome,deposito_saldo,deposito_desconsiderar,checked_at,tiny_status,http_status,latency_ms,error,raw_deposit_json)
                   values (:run_id,:tiny_id,:codigo,:normalized_codigo,:nome,:parsed_size,:situacao,:saldo_total,:saldo_reservado,:saldo_disponivel_estimado,:deposito_nome,:deposito_saldo,:deposito_desconsiderar,:checked_at,:tiny_status,:http_status,:latency_ms,:error,:raw_deposit_json)''',
                {**base, 'deposito_nome': '__NO_DEPOSIT_RETURNED__', 'deposito_saldo': None, 'deposito_desconsiderar': None, 'raw_deposit_json': '{}'},
            )
        if idx % 25 == 0:
            con.execute('''update lk_tiny_stock_snapshot_runs set
                              stock_checked_count=(select count(distinct tiny_id) from lk_tiny_stock_deposits where run_id=?),
                              stock_error_count=(select count(distinct tiny_id) from lk_tiny_stock_deposits where run_id=? and error is not null)
                           where run_id=?''', (run_id, run_id, run_id))
            con.commit()
            print(json.dumps({'run_id': run_id, 'checked_this_process': idx, 'remaining_in_batch': len(rows)-idx}, ensure_ascii=False), flush=True)
    con.execute('''update lk_tiny_stock_snapshot_runs set
                      stock_checked_count=(select count(distinct tiny_id) from lk_tiny_stock_deposits where run_id=?),
                      stock_error_count=(select count(distinct tiny_id) from lk_tiny_stock_deposits where run_id=? and error is not null)
                   where run_id=?''', (run_id, run_id, run_id))
    con.commit()


def latest_run_with_stock(con: sqlite3.Connection, run_id: str | None = None) -> str | None:
    if run_id:
        return run_id
    row = con.execute("select run_id from lk_tiny_stock_snapshot_runs where stock_checked_count>0 order by started_at desc limit 1").fetchone()
    return row['run_id'] if row else None


def recalc_commercial_state(con: sqlite3.Connection, run_id: str) -> dict[str, Any]:
    con.execute('delete from lk_variant_commercial_state')
    # Aggregate Tiny official deposit by normalized codigo. Keep match count explicit; duplicate codes block exact stock confidence.
    con.execute(
        '''
        insert into lk_variant_commercial_state
        (variant_id,product_id,source_variant_id,product_title,variant_title,sku,normalized_size,current_price,shopify_is_active,dq_status,
         tiny_run_id,tiny_match_count,tiny_official_available,tiny_total_available,tiny_status,commercial_state,blocker,source_labels,last_recalculated_at)
        with tiny_agg as (
          select normalized_codigo,
                 count(distinct tiny_id) as match_count,
                 sum(case when deposito_nome=? then coalesce(deposito_saldo,0) else 0 end) as official_available,
                 max(coalesce(saldo_disponivel_estimado,0)) as total_available,
                 sum(case when tiny_status='OK' then 0 else 1 end) as error_rows
          from lk_tiny_stock_deposits
          where run_id=? and normalized_codigo<>''
          group by normalized_codigo
        )
        select
          v.variant_id, v.product_id, v.source_variant_id, v.product_title, v.title as variant_title, v.sku,
          q.normalized_size, v.price, v.is_active, q.dq_status,
          ? as tiny_run_id,
          coalesce(t.match_count,0) as tiny_match_count,
          t.official_available as tiny_official_available,
          t.total_available as tiny_total_available,
          case
            when coalesce(v.sku,'')='' then 'no_shopify_sku'
            when t.normalized_codigo is null then 'not_mapped_in_tiny_snapshot'
            when t.match_count>1 then 'ambiguous_duplicate_tiny_code'
            when coalesce(t.error_rows,0)>0 then 'tiny_stock_error'
            when coalesce(t.official_available,0)>0 then 'available_official_deposit'
            else 'zero_official_deposit'
          end as tiny_status,
          case
            when coalesce(v.sku,'')='' then 'blocked_missing_shopify_sku'
            when lower(coalesce(q.shopify_product_status,'')) in ('draft','archived') then 'monitor_non_active_shopify_product'
            when q.dq_status not in ('ready_basic_variant_layer','ready_for_stock_decision','needs_tiny_stock_truth') then 'blocked_data_quality'
            when t.normalized_codigo is null then 'blocked_tiny_not_mapped'
            when t.match_count>1 then 'blocked_tiny_duplicate_code'
            when coalesce(t.error_rows,0)>0 then 'blocked_tiny_read_error'
            when coalesce(t.official_available,0)>0 then 'ready_available_tiny'
            else 'ready_zero_stock_sourcing_candidate'
          end as commercial_state,
          case
            when coalesce(v.sku,'')='' then 'Shopify variant sem SKU'
            when lower(coalesce(q.shopify_product_status,'')) in ('draft','archived') then 'Shopify product não ativo (draft/archived)'
            when q.dq_status not in ('ready_basic_variant_layer','ready_for_stock_decision','needs_tiny_stock_truth') then q.blocking_reason
            when t.normalized_codigo is null then 'SKU não apareceu no snapshot Tiny completo'
            when t.match_count>1 then 'Código Tiny duplicado/ambíguo'
            when coalesce(t.error_rows,0)>0 then 'Erro de leitura Tiny para o SKU'
            else null
          end as blocker,
          json_array('fact_shopify','fact_tiny_stock','derived_reconciliation') as source_labels,
          ? as last_recalculated_at
        from lk_product_variants v
        left join lk_variant_quality_status q on q.variant_id=v.variant_id
        left join tiny_agg t on t.normalized_codigo=lower(replace(replace(replace(replace(replace(coalesce(v.sku,''),'-',''),' ',''),'.',''),'_',''),'/',''))
        ''',
        (OFFICIAL_DEPOSIT, run_id, run_id, now()),
    )
    con.commit()
    rows = con.execute('select commercial_state, count(*) c from lk_variant_commercial_state group by commercial_state order by c desc').fetchall()
    tiny = con.execute('select tiny_status, count(*) c from lk_variant_commercial_state group by tiny_status order by c desc').fetchall()
    return {
        'commercial_state_counts': {r['commercial_state']: r['c'] for r in rows},
        'tiny_status_counts': {r['tiny_status']: r['c'] for r in tiny},
    }


def summarize(con: sqlite3.Connection, run_id: str, backup: pathlib.Path | None, mode: str) -> dict[str, Any]:
    run = dict(con.execute('select * from lk_tiny_stock_snapshot_runs where run_id=?', (run_id,)).fetchone())
    counts = {
        'tiny_products_listed': con.execute('select count(*) c from lk_tiny_stock_products where run_id=?', (run_id,)).fetchone()['c'],
        'tiny_products_with_codigo': con.execute("select count(*) c from lk_tiny_stock_products where run_id=? and coalesce(codigo,'')<>'')", (run_id,)).fetchone()['c'] if False else None,
        'stock_products_checked': con.execute('select count(distinct tiny_id) c from lk_tiny_stock_deposits where run_id=?', (run_id,)).fetchone()['c'],
        'deposit_rows': con.execute('select count(*) c from lk_tiny_stock_deposits where run_id=?', (run_id,)).fetchone()['c'],
        'official_deposit_rows': con.execute('select count(*) c from lk_tiny_stock_deposits where run_id=? and deposito_nome=?', (run_id, OFFICIAL_DEPOSIT)).fetchone()['c'],
        'official_positive_rows': con.execute('select count(*) c from lk_tiny_stock_deposits where run_id=? and deposito_nome=? and coalesce(deposito_saldo,0)>0', (run_id, OFFICIAL_DEPOSIT)).fetchone()['c'],
    }
    counts['tiny_products_with_codigo'] = con.execute("select count(*) c from lk_tiny_stock_products where run_id=? and coalesce(codigo,'')<>''", (run_id,)).fetchone()['c']
    com = recalc_commercial_state(con, run_id)
    summary = {
        'generated_at': now(),
        'run_id': run_id,
        'mode': mode,
        'status': run.get('status'),
        'backup_before_local_write': str(backup) if backup else None,
        'database': str(DB),
        'raw_private_dir': str(PRIVATE_DIR),
        'reports': {'json': str(REPORT_JSON), 'md': str(REPORT_MD)},
        'source_labels': ['fact_tiny_stock', 'fact_shopify', 'derived_reconciliation'],
        'official_deposit': OFFICIAL_DEPOSIT,
        'counts': counts,
        **com,
        'not_performed': ['tiny_write', 'shopify_write', 'inventory_change', 'price_change', 'supplier_contact', 'purchase', 'campaign_or_external_send', 'cron_creation'],
        'limitations': [
            'Snapshot Tiny v2 via produtos.pesquisa + produto.obter.estoque; rows still running/partial if status is not completed.',
            'Tiny stock resume/full modes now enforce delay >= 1.0s; lower values are bumped automatically to reduce API pressure after rate limits.',
            'Tiny remains operational stock truth; Shopify inventory was not used as stock truth.',
            'GMC availability policy remains separate: do not turn Tiny zero into Merchant out-of-stock automatically.',
        ],
    }
    REPORT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')
    lines = [
        '# LK OS Tiny Stock Snapshot Full Read-only — 2026-05-15',
        '',
        f"Gerado em: `{summary['generated_at']}`",
        f"Run ID: `{run_id}`",
        f"Status: `{summary['status']}`",
        '',
        '## Veredito',
        '',
        '- Snapshot Tiny read-only criado/materializado localmente.' if summary['status'] == 'completed' else ('- Snapshot Tiny read-only iniciado/materializado parcialmente; execução pausada por rate limit/bloqueio Tiny para não pressionar a API.' if summary['status'] == 'partial_api_rate_limited' else '- Snapshot Tiny read-only iniciado/atualizado localmente; ainda pode estar parcial se a execução estiver rodando.'),
        '- A camada derivada `lk_variant_commercial_state` foi recalculada a partir de Shopify + Tiny local.',
        '- Nenhum write em Tiny, Shopify, Merchant, Notion, campanhas, estoque ou preço.',
        '',
        '## Contagens',
        '',
    ]
    for k, v in summary['counts'].items():
        lines.append(f'- {k}: `{v}`')
    lines += ['', '## Estado comercial derivado', '']
    for k, v in summary['commercial_state_counts'].items():
        lines.append(f'- {k}: `{v}`')
    lines += ['', '## Status Tiny por variant Shopify', '']
    for k, v in summary['tiny_status_counts'].items():
        lines.append(f'- {k}: `{v}`')
    lines += ['', '## Limites / guardrails', '']
    for item in summary['limitations']:
        lines.append(f'- {item}')
    lines += ['', '## O que não foi feito', '']
    for item in summary['not_performed']:
        lines.append(f'- {item}')
    REPORT_MD.write_text('\n'.join(lines) + '\n')
    return summary


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--run-id', default=None)
    ap.add_argument('--mode', choices=['full', 'resume', 'list-only', 'recalc-only'], default='full')
    ap.add_argument('--delay', type=float, default=DEFAULT_DELAY)
    ap.add_argument('--max-pages', type=int, default=None)
    ap.add_argument('--stock-limit', type=int, default=None)
    args = ap.parse_args()

    ensure_dirs()
    backup = None
    if args.mode != 'recalc-only':
        backup = backup_db()
    con = connect()
    init_schema(con)
    run_id = args.run_id or f'tiny_stock_{slug_ts()}'
    if args.mode != 'recalc-only':
        create_run(con, run_id, args.mode)
    else:
        existing = latest_run_with_stock(con, args.run_id)
        if not existing:
            raise SystemExit('No stock snapshot run found for recalc-only')
        run_id = existing

    if args.mode in {'full', 'resume'} and args.delay < MIN_STOCK_DELAY:
        print(json.dumps({'guardrail': 'delay_bumped_to_minimum', 'requested_delay': args.delay, 'effective_delay': MIN_STOCK_DELAY}, ensure_ascii=False), flush=True)
        args.delay = MIN_STOCK_DELAY

    if args.mode in {'full', 'resume', 'list-only'}:
        secrets = load_secrets()
        tiny_token = secrets.get('TINY_API_TOKEN') or ''
        if not tiny_token:
            raise SystemExit('Missing TINY_API_TOKEN')
        if args.mode in {'full', 'list-only'}:
            list_products(con, tiny_token, run_id, args.delay, args.max_pages)
        if args.mode in {'full', 'resume'}:
            check_stock(con, tiny_token, run_id, args.delay, args.stock_limit)
        remaining = con.execute('''select count(*) c from lk_tiny_stock_products p
                                   left join lk_tiny_stock_deposits d on d.run_id=p.run_id and d.tiny_id=p.tiny_id
                                   where p.run_id=? and coalesce(p.codigo,'')<>'' and d.tiny_id is null''', (run_id,)).fetchone()['c']
        current_status = con.execute('select status from lk_tiny_stock_snapshot_runs where run_id=?', (run_id,)).fetchone()['status']
        if current_status == 'partial_api_rate_limited':
            status = current_status
        else:
            status = 'completed' if remaining == 0 and args.mode != 'list-only' else ('listed_only' if args.mode == 'list-only' else 'partial_needs_resume')
        con.execute('''update lk_tiny_stock_snapshot_runs set status=?, finished_at=?, products_listed_count=(select count(*) from lk_tiny_stock_products where run_id=?), stock_checked_count=(select count(distinct tiny_id) from lk_tiny_stock_deposits where run_id=?), stock_error_count=(select count(distinct tiny_id) from lk_tiny_stock_deposits where run_id=? and error is not null) where run_id=?''', (status, now(), run_id, run_id, run_id, run_id))
        con.commit()

    summary = summarize(con, run_id, backup, args.mode)
    print(json.dumps({'run_id': run_id, 'status': summary['status'], 'counts': summary['counts'], 'commercial_state_counts': summary['commercial_state_counts']}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
