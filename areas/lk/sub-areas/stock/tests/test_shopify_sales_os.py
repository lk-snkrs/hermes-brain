#!/usr/bin/env python3
from __future__ import annotations

import json
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "shopify_sales_os.py"
FIXTURE = ROOT / "fixtures" / "webhook_shopify_order_paid.json"


def run_cmd(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(SCRIPT), *args], cwd=ROOT, text=True, capture_output=True, check=False)


class ShopifySalesOsTest(unittest.TestCase):
    def test_ingests_order_fixture_idempotently(self) -> None:
        with tempfile.TemporaryDirectory(prefix="shopify-sales-os-") as tmp:
            db = Path(tmp) / "shopify_sales_os.db"
            first = run_cmd("ingest-file", "--db", str(db), "--payload", str(FIXTURE), "--topic", "orders/paid")
            self.assertEqual(first.returncode, 0, first.stderr)
            first_json = json.loads(first.stdout)
            self.assertEqual(first_json["status"], "processed")
            self.assertEqual(first_json["guardrails"]["shopify_write"], 0)
            self.assertEqual(first_json["guardrails"]["external_write"], 0)

            second = run_cmd("ingest-file", "--db", str(db), "--payload", str(FIXTURE), "--topic", "orders/paid")
            self.assertEqual(second.returncode, 0, second.stderr)
            second_json = json.loads(second.stdout)
            self.assertEqual(second_json["status"], "ignored")
            self.assertEqual(second_json["reason"], "duplicate_event")

            con = sqlite3.connect(db)
            con.row_factory = sqlite3.Row
            self.assertEqual(con.execute("select count(*) c from shopify_orders").fetchone()["c"], 1)
            self.assertEqual(con.execute("select count(*) c from shopify_order_line_items").fetchone()["c"], 1)
            self.assertEqual(con.execute("select count(*) c from shopify_sales_event_ledger").fetchone()["c"], 1)

    def test_exports_dashboard_summary(self) -> None:
        with tempfile.TemporaryDirectory(prefix="shopify-sales-os-") as tmp:
            db = Path(tmp) / "shopify_sales_os.db"
            out = Path(tmp) / "shopify_sales_summary.json"
            ingest = run_cmd("ingest-file", "--db", str(db), "--payload", str(FIXTURE), "--topic", "orders/paid")
            self.assertEqual(ingest.returncode, 0, ingest.stderr)

            export = run_cmd("export-summary", "--db", str(db), "--output", str(out))
            self.assertEqual(export.returncode, 0, export.stderr)
            payload = json.loads(out.read_text())
            self.assertEqual(payload["status"], "ok")
            self.assertEqual(payload["source"], "shopify_sales_os_db")
            self.assertEqual(payload["totals"]["orders"], 1)
            self.assertEqual(payload["totals"]["units"], 6)
            self.assertEqual(payload["top_products"][0]["sku"], "NK-AMP-BLK-40")
            self.assertEqual(payload["guardrails"], {
                "shopify_write": 0,
                "tiny_write": 0,
                "external_write": 0,
                "public_availability_promise": 0,
                "auto_purchase": 0,
            })


if __name__ == "__main__":
    unittest.main()
