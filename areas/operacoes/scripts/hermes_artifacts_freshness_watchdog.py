#!/usr/bin/env python3
"""Read-only freshness watchdog for Hermes v0.13 operational artifacts.

Silent contract for no_agent cron:
- exit 0 + empty stdout: OK, no Telegram noise;
- exit 0 + stdout: drift/anomaly alert;
- never prints secrets or PII.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sqlite3
from pathlib import Path
from zoneinfo import ZoneInfo

BASE = Path('/opt/data')
TZ = ZoneInfo('America/Sao_Paulo')
REPORT_DIR = BASE / 'lk_weekly_influencer_sales_reports'
KANBAN_DB = BASE / 'kanban' / 'boards' / 'lk-growth-ops' / 'kanban.db'
BRAIN = BASE / 'hermes_bruno_ingest' / 'hermes-brain'
REQUIRED_DOCS = [
    BRAIN / 'areas/operacoes/rotinas/hermes-v013-operacionalizacao.md',
    BRAIN / 'areas/operacoes/rotinas/hermes-v013-kanban-lk-growth-ops.md',
    BRAIN / 'areas/operacoes/rotinas/hermes-v013-watchdogs-no-agent.md',
    BRAIN / 'reports/hermes-release-catchup-2026-05-10/action-matrix.md',
]
REQUIRED_CRON_JOB_IDS = {'f5a23dd6a1bd', 'edd06fe19397'}
CRON_JOBS = BASE / 'cron' / 'jobs.json'


def iso_now() -> str:
    return dt.datetime.now(TZ).isoformat(timespec='seconds')


def latest_report_age_days() -> tuple[int | None, Path | None]:
    files = sorted(REPORT_DIR.glob('lk-weekly-influencer-sales-*.json'), key=lambda p: p.stat().st_mtime, reverse=True)
    if not files:
        return None, None
    latest = files[0]
    mtime = dt.datetime.fromtimestamp(latest.stat().st_mtime, TZ)
    age = dt.datetime.now(TZ) - mtime
    return int(age.total_seconds() // 86400), latest


def kanban_counts() -> dict[str, int] | None:
    if not KANBAN_DB.exists():
        return None
    conn = sqlite3.connect(str(KANBAN_DB))
    try:
        cols = {row[1] for row in conn.execute('pragma table_info(tasks)').fetchall()}
        if 'archived_at' in cols:
            query = 'select status, count(*) from tasks where archived_at is null group by status'
        else:
            query = 'select status, count(*) from tasks group by status'
        rows = conn.execute(query).fetchall()
    finally:
        conn.close()
    return {str(status): int(count) for status, count in rows}


def cron_job_ids() -> set[str]:
    if not CRON_JOBS.exists():
        return set()
    data = json.loads(CRON_JOBS.read_text(encoding='utf-8'))
    if isinstance(data, dict):
        jobs = data.get('jobs', [])
    elif isinstance(data, list):
        jobs = data
    else:
        jobs = []
    return {str(j.get('job_id') or j.get('id')) for j in jobs if isinstance(j, dict)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--verbose', action='store_true')
    ap.add_argument('--max-weekly-report-age-days', type=int, default=8)
    args = ap.parse_args()

    alerts: list[str] = []

    age, report = latest_report_age_days()
    if age is None:
        alerts.append(f'LK weekly influencer report ausente em {REPORT_DIR}')
    elif age > args.max_weekly_report_age_days:
        alerts.append(f'LK weekly influencer report stale: {report} tem {age} dias; limite={args.max_weekly_report_age_days}')

    counts = kanban_counts()
    if counts is None:
        alerts.append(f'Kanban board lk-growth-ops ausente: {KANBAN_DB}')
    elif sum(counts.values()) < 7:
        alerts.append(f'Kanban board lk-growth-ops com cards insuficientes: {counts}')

    missing_docs = [str(p) for p in REQUIRED_DOCS if not p.exists()]
    if missing_docs:
        alerts.append('Docs Hermes v0.13 ausentes: ' + ', '.join(missing_docs))

    missing_crons = sorted(REQUIRED_CRON_JOB_IDS - cron_job_ids())
    if missing_crons:
        alerts.append('Cron jobs esperados ausentes: ' + ', '.join(missing_crons))

    if alerts:
        print('⚠️ Hermes v0.13 artifact freshness watchdog')
        print(f'check_at: {iso_now()}')
        for item in alerts:
            print(f'- {item}')
        return 0

    if args.verbose:
        print(json.dumps({
            'ok': True,
            'check_at': iso_now(),
            'latest_weekly_report': str(report) if report else None,
            'latest_weekly_report_age_days': age,
            'kanban_counts': counts,
            'required_cron_jobs': sorted(REQUIRED_CRON_JOB_IDS),
        }, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
