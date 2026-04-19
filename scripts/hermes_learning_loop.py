#!/usr/bin/env python3
"""
Hermes Learning Loop — Weekly Consolidation
Analyzes recent sessions for patterns, corrections, errors.
"""
import os, sqlite3
from datetime import datetime, timedelta
from pathlib import Path

HERMES_HOME = os.path.expanduser("~/.hermes")
SESSION_DB = os.path.join(HERMES_HOME, "state.db")
LESSONS_FILE = os.path.join(HERMES_HOME, "memories/lessons.md")

def get_sessions(days=7):
    """Get recent sessions with latest user message as preview."""
    if not os.path.exists(SESSION_DB):
        return []
    conn = sqlite3.connect(SESSION_DB)
    c = conn.cursor()
    cutoff_ts = (datetime.now() - timedelta(days=days)).timestamp()
    c.execute("""
        SELECT s.title, SUBSTR(m.content, 1, 200) as preview, s.started_at
        FROM sessions s
        LEFT JOIN messages m ON m.session_id = s.id AND m.role = 'user'
        WHERE s.started_at > ?
        ORDER BY s.started_at DESC LIMIT 100
    """, (cutoff_ts,))
    rows = c.fetchall()
    conn.close()
    return rows

def detect_corrections(sessions):
    corrections = []
    for title, preview, _ in sessions:
        combined = f"{(title or '')} {(preview or '')}"
        if any(w in combined.lower() for w in ["você esqueceu", "não faça isso", "corrigir", "não é assim", "pq perguntou", "esqueceu", "você errou"]):
            corrections.append((title, preview))
    return corrections

def detect_error_recoveries(sessions):
    errors = []
    for title, preview, _ in sessions:
        combined = f"{(title or '')} {(preview or '')}"
        if any(w in combined.lower() for w in ["erro", "falhou", "failed", "error", "não funciona"]):
            errors.append((title, preview))
    return errors

def detect_misfires(sessions):
    misfires = []
    for title, preview, _ in sessions:
        combined = f"{(title or '')} {(preview or '')}"
        if any(w in combined.lower() for w in ["corrigi", "já corrigi", "na verdade", "aplicar tudo"]):
            misfires.append((title, preview))
    return misfires

def generate_report():
    sessions = get_sessions(7)
    corrections = detect_corrections(sessions)
    errors = detect_error_recoveries(sessions)
    misfires = detect_misfires(sessions)

    report = []
    report.append("# Hermes Learning Loop — Weekly Report")
    report.append(f"Gerado em: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    report.append(f"Sessões analisadas: {len(sessions)}")
    report.append("")

    if corrections:
        report.append(f"## Correções do Lucas ({len(corrections)})")
        for title, preview in corrections[:5]:
            report.append(f"- *{(title or 'Sem título')[:80]}*")
            if preview:
                report.append(f"  → {preview[:120]}")
        report.append("")

    if errors:
        report.append(f"## Erros Identificados ({len(errors)})")
        for title, preview in errors[:5]:
            report.append(f"- *{(title or 'Sem título')[:80]}*")
        report.append("")

    if misfires:
        report.append(f"## Auto-correções ({len(misfires)})")
        for title, _ in misfires[:5]:
            report.append(f"- *{(title or 'Sem título')[:80]}*")
        report.append("")

    if not any([corrections, errors, misfires]):
        report.append("Nenhuma anomalia esta semana. Sistema estável.")

    return "\n".join(report)

if __name__ == "__main__":
    report = generate_report()
    print(report)
