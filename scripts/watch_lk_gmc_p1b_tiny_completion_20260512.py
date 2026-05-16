#!/usr/bin/env python3
"""Silent watchdog for LK GMC P1-B Tiny packet completion.

Prints nothing while the known process is still running. Once it finishes, emits
one Telegram-ready inline summary and writes a sentinel to avoid duplicate sends.
"""
from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path

ROOT = Path('/opt/data/hermes_bruno_ingest/hermes-brain')
REPORT = ROOT / 'reports/lk-gmc-2026-05-12-p1-availability-tiny-packet.json'
MD = ROOT / 'reports/lk-gmc-2026-05-12-p1-availability-tiny-packet.md'
SENTINEL = ROOT / 'reports/.lk-gmc-p1b-tiny-watchdog-notified-2026-05-12'
PID = '190'


def pid_alive(pid: str) -> bool:
    try:
        r = subprocess.run(['ps', '-p', pid, '-o', 'pid=,cmd='], text=True, capture_output=True, timeout=5)
        return r.returncode == 0 and 'lk_gmc_p1_availability_tiny_packet_20260512.py' in r.stdout
    except Exception:
        return False


def main() -> None:
    if SENTINEL.exists():
        return
    if pid_alive(PID):
        return
    if not REPORT.exists():
        print('LK GMC P1-B Tiny packet terminou, mas o JSON final ainda não foi encontrado. Verificar manualmente antes de qualquer write.')
        SENTINEL.write_text('missing_report\n', encoding='utf-8')
        return
    data = json.loads(REPORT.read_text(encoding='utf-8'))
    s = data.get('summary') or {}
    status = data.get('status') or 'unknown'
    decision_counts = s.get('decision_state_counts') or {}
    print('\n'.join([
        'LK GMC P1-B Tiny packet finalizado.',
        '',
        f'Status: `{status}`',
        '',
        'Resumo inline:',
        f"- Produtos online com `availability` ausente: {s.get('online_missing_availability_candidates', '—')}",
        f"- Ready para apply se Lucas aprovar: {s.get('ready_for_availability_apply_if_lucas_approves', '—')}",
        f"- Proposta `in stock`: {s.get('ready_in_stock', '—')}",
        f"- Proposta `out of stock`: {s.get('ready_out_of_stock', '—')}",
        f"- Bloqueados/revisão: {s.get('blocked_or_review', '—')}",
        f"- Estados: `{decision_counts}`",
        '',
        'Não executado: Merchant/Tiny/Shopify/feed/DB/POS/campanhas writes = 0.',
        '',
        'Próximo gate: eu só devo preparar/aplicar `availability` se houver itens ready e Lucas aprovar explicitamente. Se ready = 0, não há write para aprovar; vira revisão/higiene de dados.',
    ]))
    SENTINEL.write_text('notified\n', encoding='utf-8')


if __name__ == '__main__':
    main()
