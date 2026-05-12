#!/usr/bin/env python3
"""LK GMC Review mandatory read-only watchdog.

Repository copy of the cron script installed at `/opt/data/scripts/lk_gmc_review_watchdog.py`.
Runs the Merchant Center read-only router and prints a concise Telegram-ready report.
"""
from __future__ import annotations

import json
import pathlib
import subprocess
import sys
from datetime import datetime, timezone

ROOT = pathlib.Path('/opt/data/hermes_bruno_ingest/hermes-brain')
ROUTER = ROOT / 'scripts/lk_merchant_center_feed_readonly_router_20260511.py'
REPORT = ROOT / 'reports/lk-merchant-center-feed-readonly-router-2026-05-11.json'


def main() -> int:
    started = datetime.now(timezone.utc).isoformat()
    proc = subprocess.run([sys.executable, str(ROUTER)], cwd=str(ROOT), text=True, capture_output=True, timeout=300)
    if proc.returncode != 0:
        print('LK GMC Review, falha no watchdog')
        print(f'- Started UTC: {started}')
        print(f'- Return code: {proc.returncode}')
        if proc.stderr:
            print('- stderr:')
            print(proc.stderr[-1800:])
        if proc.stdout:
            print('- stdout:')
            print(proc.stdout[-1800:])
        return proc.returncode or 1

    data = json.loads(REPORT.read_text(encoding='utf-8'))
    s = data.get('summary') or {}
    issue_groups = data.get('issue_groups') or []
    top_codes = data.get('top_issue_codes') or []

    print('## LK GMC Review, read-only')
    print('')
    print(f'Gerado UTC: `{data.get("generated_at")}`')
    print('')
    print('**Veredito:** Merchant Center revisado em modo leitura. Nenhum write/feed update/Shopify/GSC/campanha executado.')
    print('')
    print('**Snapshot:**')
    print(f'- Produtos/status lidos: {s.get("product_statuses_read", 0)}')
    print(f'- Itens na fila P1/P2: {s.get("queue_items", 0)}')
    print(f'- P1: {s.get("p1_items", 0)}')
    print(f'- P2: {s.get("p2_items", 0)}')
    print(f'- Produtos com issue: {s.get("products_with_item_issues", 0)}')
    print(f'- Produtos com destino reprovado: {s.get("products_with_disapproved_destination", 0)}')
    print(f'- Cruzamentos com GSC: {s.get("products_crossing_gsc_priority", 0)}')
    print(f'- Writes liberados agora: {s.get("writes_allowed_now", 0)}')
    print('')
    print('**Top grupos:**')
    if issue_groups:
        for idx, group in enumerate(issue_groups[:5], 1):
            print(f'{idx}. {group.get("priority")} · {group.get("recommended_action")} · {group.get("count")} itens')
            print(f'   - Issues: {group.get("issue_codes")}')
            print(f'   - Destinos reprovados: {group.get("disapproved_destinations")}')
    else:
        print('- Nenhum grupo P1/P2 encontrado.')
    print('')
    print('**Top issue codes:**')
    if top_codes:
        for item in top_codes[:8]:
            print(f'- {item.get("issue")}: {item.get("count")}')
    else:
        print('- Nenhum issue code retornado.')
    print('')
    print('**Bloqueado sem aprovação:** Merchant/feed write, Shopify write, GSC admin/Indexing API, conteúdo público, campanhas/envios.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
