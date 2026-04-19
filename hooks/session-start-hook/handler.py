"""
Handler for session:start event.
Runs the Session Start Protocol — brain check, pending, crons, decisions, lessons.
Injects a briefing into the conversation context.
"""

import os
import json
from pathlib import Path
from datetime import datetime

HERMES_HOME = os.path.expanduser("~/.hermes")
BRAIN_DIR = os.path.join(HERMES_HOME, "hermes-brain")
MEMORIES_DIR = os.path.join(HERMES_HOME, "memories")

def _read(path):
    try:
        with open(path) as f:
            return f.read()
    except:
        return None

def handle(event_type: str, context: dict) -> dict:
    """
    Returns a dict with session start protocol data.
    The gateway will inject this into the system prompt or conversation context.
    """
    result = {
        "event": event_type,
        "timestamp": datetime.now().isoformat(),
        "current_work": None,
        "pending_summary": None,
        "high_priority": [],
        "cron_status": None,
        "decisions_note": None,
        "lessons_note": None,
    }

    # 1. CURRENT_WORK.md
    cw = _read(os.path.join(HERMES_HOME, "CURRENT_WORK.md"))
    if cw:
        result["current_work"] = cw.strip()
        result["current_work_exists"] = True
    else:
        result["current_work"] = None
        result["current_work_exists"] = False

    # 2. pending.md
    pending = _read(os.path.join(MEMORIES_DIR, "pending.md"))
    if pending:
        result["pending_summary"] = pending.strip()
        # Extract high priority items
        lines = pending.split("\n")
        for line in lines:
            if "[alta]" in line.lower() or "[urgente]" in line.lower() or "URGENTE" in line:
                result["high_priority"].append(line.strip())

    # 3. decisions.md (just note if updated recently)
    decisions = _read(os.path.join(MEMORIES_DIR, "decisions.md"))
    if decisions:
        result["decisions_note"] = f"decisions.md existe ({len(decisions)} chars)"

    # 4. lessons.md (just note if exists)
    lessons = _read(os.path.join(MEMORIES_DIR, "lessons.md"))
    if lessons:
        result["lessons_note"] = f"lessons.md existe ({len(lessons)} chars)"

    # 5. Check for brain sync status
    brain_sync_file = os.path.join(HERMES_HOME, "memories", "last_sync.txt")
    last_sync = _read(brain_sync_file)
    if last_sync:
        result["last_brain_sync"] = last_sync.strip()

    return result
