from __future__ import annotations

import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from lk_stock_api_adapter import current_db_path, lookup_stock, make_json_response


class StockApiAdapterTest(unittest.TestCase):
    def _make_db(self, path: Path) -> None:
        con = sqlite3.connect(path)
        con.execute(
            """
            CREATE TABLE current_local_stock (
              sku TEXT,
              handle TEXT,
              title TEXT,
              size TEXT,
              tiny_codigo TEXT,
              tiny_id_candidates TEXT,
              priority TEXT,
              canonical_status TEXT,
              issue_type TEXT,
              decision_lane TEXT,
              local_action TEXT,
              packet_md TEXT,
              stock_observation_count INTEGER,
              stock_quantity_observed_values TEXT,
              stock_quantity_sum_observed REAL,
              stock_quantity_max_observed REAL,
              stock_positive_observed INTEGER,
              stock_zero_observed INTEGER,
              stock_source TEXT,
              stock_freshness TEXT,
              source_observed_at TEXT,
              local_consult_safe INTEGER,
              identity_resolved_safe INTEGER,
              public_availability_safe INTEGER,
              availability_claim_allowed INTEGER,
              needs_live_tiny_confirmation INTEGER,
              data_quality_gap TEXT
            )
            """
        )
        con.execute(
            """
            CREATE TABLE current_stock_scored (
              sku TEXT,
              handle TEXT,
              title TEXT,
              size TEXT,
              canonical_status TEXT,
              identity_resolved_safe INTEGER,
              local_consult_safe INTEGER,
              stock_quantity_max_observed REAL,
              units_signal REAL,
              revenue_signal REAL,
              store_units_signal REAL,
              demand_tier TEXT,
              rupture_risk TEXT,
              action_priority TEXT,
              action_lane TEXT,
              operational_score REAL,
              signal_sources TEXT,
              availability_claim_allowed INTEGER,
              public_availability_safe INTEGER
            )
            """
        )
        con.execute(
            """
            CREATE TABLE tiny_full_sync_runs (
              run_id TEXT,
              started_at TEXT,
              finished_at TEXT,
              input_db TEXT,
              output_db TEXT,
              rows_scanned INTEGER,
              rows_updated INTEGER,
              rows_failed INTEGER,
              rows_skipped INTEGER,
              status TEXT,
              tiny_write INTEGER,
              shopify_write INTEGER,
              writes_externos INTEGER,
              public_availability_safe INTEGER,
              availability_claim_allowed INTEGER,
              summary_json TEXT
            )
            """
        )
        con.execute(
            """
            CREATE TABLE tiny_full_sync_item_ledger (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              run_id TEXT NOT NULL,
              sku TEXT NOT NULL,
              handle TEXT,
              tiny_product_id TEXT NOT NULL,
              status TEXT NOT NULL,
              quantity REAL,
              previous_quantity REAL,
              observed_at TEXT NOT NULL,
              deposit TEXT NOT NULL,
              error TEXT,
              tiny_write INTEGER NOT NULL DEFAULT 0,
              shopify_write INTEGER NOT NULL DEFAULT 0,
              writes_externos INTEGER NOT NULL DEFAULT 0,
              public_availability_safe INTEGER NOT NULL DEFAULT 0,
              availability_claim_allowed INTEGER NOT NULL DEFAULT 0
            )
            """
        )
        rows = [
            ("ABC-40", "tenis-abc", "Tênis Nike ABC", "40", "ABC-40", "123", "P0", "CONSULTABLE_LOCAL_RESOLVED_BY_FULL_LIVE_MATCH", "", "", "", "", 1, "2.0", 2.0, 2.0, 1, 0, "tiny_full_sync", "tiny_full_sync_nightly", "2026-06-12T06:20:21Z", 1, 1, 0, 0, 1, "RECONFIRM_BEFORE_PUBLIC"),
            ("DUP-40", "tenis-dup", "Tênis DUP", "40", "DUP-40", "123,456", "P1", "BLOCKED_TINY_DUPLICATE_LIVE_FULL", "tiny_duplicate_exact_code_blocked", "TINY_DUPLICATE_PACKET", "Resolver duplicidade Tiny", "packet.md", 0, "", None, None, 0, 0, "gate_b2", "stale", "2026-06-12T10:29:59Z", 0, 0, 0, 0, 1, "BLOCKED_TINY_DUPLICATE"),
        ]
        con.executemany(
            """
            INSERT INTO current_local_stock VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            rows,
        )
        con.execute(
            """
            INSERT INTO current_stock_scored VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                "ABC-40",
                "tenis-abc",
                "Tênis Nike ABC",
                "40",
                "CONSULTABLE_LOCAL_RESOLVED_BY_FULL_LIVE_MATCH",
                1,
                1,
                2.0,
                7.0,
                1999.90,
                3.0,
                "HIGH",
                "ZERO_STOCK_DEMAND",
                "P0",
                "REPLENISHMENT_DECISION_PACKET_CANDIDATE",
                88.5,
                "sales_d30,stock_os",
                0,
                0,
            ),
        )
        con.execute(
            "INSERT INTO tiny_full_sync_runs VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            ("run-1", "2026-06-12T10:00:00Z", "2026-06-12T10:31:00Z", "in.db", "out.db", 2, 2, 0, 0, "ok", 0, 0, 0, 0, 0, "{}"),
        )
        con.executemany(
            """
            INSERT INTO tiny_full_sync_item_ledger
            (run_id, sku, handle, tiny_product_id, status, quantity, previous_quantity, observed_at, deposit)
            VALUES (?,?,?,?,?,?,?,?,?)
            """,
            [
                ("run-1", "ABC-40", "tenis-abc", "123", "updated", 2.0, 5.0, "2026-06-12T10:30:00Z", "LK | CONTROLE ESTOQUE"),
                ("run-1", "DUP-40", "tenis-dup", "456", "updated", 0.0, 1.0, "2026-06-12T10:30:00Z", "LK | CONTROLE ESTOQUE"),
            ],
        )
        con.commit()
        con.close()

    def _make_pointer(self, path: Path, db: Path) -> None:
        path.write_text(
            json.dumps(
                {
                    "pointer_name": "lk_stock_os_current_pointer",
                    "current_stage": "test_stage",
                    "updated_at_utc": "2026-06-12T07:00:00Z",
                    "artifacts": {"sqlite_db": str(db)},
                    "guardrails": {
                        "tiny_write": 0,
                        "shopify_write": 0,
                        "writes_externos": 0,
                        "public_availability_safe": 0,
                        "availability_claim_allowed": 0,
                    },
                },
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

    def test_lookup_confirmed_row_returns_stock_os_contract_and_public_guards(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            db = tmp_path / "stock.db"
            pointer = tmp_path / "pointer.json"
            self._make_db(db)
            self._make_pointer(pointer, db)

            result = lookup_stock("ABC-40", pointer_path=pointer)

            self.assertEqual(result["status"], "confirmado")
            self.assertEqual(result["query"], "ABC-40")
            self.assertEqual(result["source"], "Stock OS DB")
            self.assertEqual(result["freshness"], "tiny_full_sync_nightly")
            self.assertEqual(result["source_observed_at"], "2026-06-12T10:29:59Z")
            self.assertEqual(result["guardrails"]["tiny_write"], 0)
            self.assertEqual(result["guardrails"]["shopify_write"], 0)
            self.assertEqual(result["guardrails"]["public_availability_safe"], 0)
            self.assertEqual(result["guardrails"]["availability_claim_allowed"], 0)
            self.assertEqual(result["results"][0]["sku"], "ABC-40")
            self.assertEqual(result["results"][0]["produto"], "Tênis Nike ABC")
            self.assertEqual(result["results"][0]["title"], "Tênis Nike ABC")
            self.assertEqual(result["results"][0]["product_title"], "Tênis Nike ABC")
            self.assertEqual(result["results"][0]["marca"], "nike")
            self.assertEqual(result["results"][0]["quantity_lk_controle_estoque"], 2.0)
            self.assertEqual(result["results"][0]["status"], "confirmado")

    def test_lookup_merges_operational_score_without_confusing_sanitation_priority(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            db = tmp_path / "stock.db"
            pointer = tmp_path / "pointer.json"
            self._make_db(db)
            self._make_pointer(pointer, db)

            result = lookup_stock("ABC-40", pointer_path=pointer)
            row = result["results"][0]

            self.assertEqual(row["sanitation_priority"], "P0")
            self.assertEqual(row["action_priority"], "P0")
            self.assertEqual(row["action_lane"], "REPLENISHMENT_DECISION_PACKET_CANDIDATE")
            self.assertEqual(row["operational_score"], 88.5)
            self.assertEqual(row["units_signal"], 7.0)
            self.assertEqual(row["revenue_signal"], 1999.90)
            self.assertEqual(row["store_units_signal"], 3.0)
            self.assertEqual(row["demand_tier"], "HIGH")
            self.assertEqual(row["rupture_risk"], "ZERO_STOCK_DEMAND")

    def test_lookup_exposes_global_freshness_movement_and_thumbnail_contract(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            db = tmp_path / "stock.db"
            pointer = tmp_path / "pointer.json"
            self._make_db(db)
            self._make_pointer(pointer, db)

            result = lookup_stock("all", pointer_path=pointer, limit=1000)
            row = next(item for item in result["results"] if item["sku"] == "ABC-40")

            self.assertEqual(result["freshness_summary"]["source_observed_at_min"], "2026-06-12T06:20:21Z")
            self.assertEqual(result["freshness_summary"]["source_observed_at_max"], "2026-06-12T10:29:59Z")
            self.assertEqual(result["freshness_summary"]["latest_sync_finished_at"], "2026-06-12T10:31:00Z")
            self.assertEqual(result["source_observed_at"], "2026-06-12T10:29:59Z")
            self.assertEqual(result["movement_summary"]["went_to_zero"], 1)
            self.assertEqual(result["movement_summary"]["changed"], 2)
            self.assertEqual(row["previous_quantity"], 5.0)
            self.assertEqual(row["stock_delta"], -3.0)
            self.assertEqual(row["thumbnail_url"], "/api/product-thumbnail?handle=tenis-abc")

    def test_lookup_unscored_sanitation_row_defaults_to_p3_not_sanitation_p_lane(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            db = tmp_path / "stock.db"
            pointer = tmp_path / "pointer.json"
            self._make_db(db)
            self._make_pointer(pointer, db)

            result = lookup_stock("DUP-40", pointer_path=pointer)
            row = result["results"][0]

            self.assertEqual(row["sanitation_priority"], "P1")
            self.assertEqual(row["action_priority"], "P3")
            self.assertEqual(row["action_lane"], "RESOLVE_IDENTITY_BEFORE_STOCK_DECISION")
            self.assertEqual(row["operational_score"], 0)

    def test_lookup_blocked_row_is_not_confirmed_not_zero_stock(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            db = tmp_path / "stock.db"
            pointer = tmp_path / "pointer.json"
            self._make_db(db)
            self._make_pointer(pointer, db)

            result = lookup_stock("DUP-40", pointer_path=pointer)

            self.assertEqual(result["status"], "nao_confirmado")
            self.assertEqual(result["results"][0]["status"], "nao_confirmado")
            self.assertIsNone(result["results"][0]["quantity_lk_controle_estoque"])
            self.assertEqual(result["results"][0]["motivo"], "local_consult_not_safe")
            self.assertEqual(result["results"][0]["action"], "reconfirmar via lk-stock/Tiny antes de afirmar disponibilidade")

    def test_lookup_missing_query_is_not_confirmed(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            db = tmp_path / "stock.db"
            pointer = tmp_path / "pointer.json"
            self._make_db(db)
            self._make_pointer(pointer, db)

            result = lookup_stock("inexistente", pointer_path=pointer)

            self.assertEqual(result["status"], "nao_confirmado")
            self.assertEqual(result["results"], [])
            self.assertEqual(result["motivo"], "no_local_match")

    def test_lookup_all_returns_dashboard_feed_without_public_availability(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            db = tmp_path / "stock.db"
            pointer = tmp_path / "pointer.json"
            self._make_db(db)
            self._make_pointer(pointer, db)

            result = lookup_stock("all", pointer_path=pointer, limit=1000)

            self.assertEqual(result["status"], "confirmado")
            self.assertEqual(result["query"], "all")
            self.assertEqual(result["result_count"], 2)
            self.assertEqual([item["sku"] for item in result["results"]], ["ABC-40", "DUP-40"])
            self.assertEqual(result["guardrails"]["public_availability_safe"], 0)
            self.assertEqual(result["guardrails"]["availability_claim_allowed"], 0)

    def test_lookup_all_honors_dashboard_large_limit_without_silent_50_row_clamp(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            db = tmp_path / "stock.db"
            pointer = tmp_path / "pointer.json"
            self._make_db(db)
            con = sqlite3.connect(db)
            extra_rows = []
            for i in range(60):
                extra_rows.append(
                    (
                        f"BULK-{i:03d}",
                        "bulk-handle",
                        "Produto Bulk",
                        str(i),
                        f"BULK-{i:03d}",
                        str(1000 + i),
                        "",
                        "CONSULTABLE_LOCAL_RESOLVED_BY_OBSERVED_EXACT_VARIANT_PROMOTION",
                        "",
                        "",
                        "",
                        "",
                        1,
                        "0.0",
                        0.0,
                        0.0,
                        0,
                        1,
                        "tiny_full_sync",
                        "tiny_full_sync_nightly",
                        "2026-06-12T10:29:59Z",
                        1,
                        1,
                        0,
                        0,
                        1,
                        "",
                    )
                )
            con.executemany("INSERT INTO current_local_stock VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", extra_rows)
            con.commit()
            con.close()
            self._make_pointer(pointer, db)

            result = lookup_stock("all", pointer_path=pointer, limit=1000)

            self.assertEqual(result["result_count"], 62)
            self.assertEqual(len(result["results"]), 62)
            self.assertEqual(result["total_count"], 62)
            self.assertFalse(result["truncated"])

    def test_lookup_all_honors_limit_above_ten_thousand_for_full_dashboard_feed(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            db = tmp_path / "stock.db"
            pointer = tmp_path / "pointer.json"
            self._make_db(db)
            con = sqlite3.connect(db)
            extra_rows = []
            for i in range(10020):
                extra_rows.append(
                    (
                        f"FULL-{i:05d}",
                        f"full-handle-{i}",
                        "Produto Full",
                        str(i),
                        f"FULL-{i:05d}",
                        str(2000 + i),
                        "PENDING_CATALOG_BACKFILL",
                        "CONSULTABLE_LOCAL_RESOLVED_BY_FULL_LIVE_MATCH",
                        "",
                        "ACTIVE_SHOPIFY_SKELETON_BACKFILL",
                        "",
                        "",
                        1,
                        "0.0",
                        0.0,
                        0.0,
                        0,
                        1,
                        "tiny_full_sync",
                        "tiny_full_sync_nightly",
                        "2026-06-12T10:29:59Z",
                        1,
                        1,
                        0,
                        0,
                        1,
                        "",
                    )
                )
            con.executemany("INSERT INTO current_local_stock VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", extra_rows)
            con.commit()
            con.close()
            self._make_pointer(pointer, db)

            result = lookup_stock("all", pointer_path=pointer, limit=11000)

            self.assertEqual(result["total_count"], 10022)
            self.assertEqual(result["result_count"], 10022)
            self.assertEqual(len(result["results"]), 10022)
            self.assertFalse(result["truncated"])

    def test_current_db_path_rebases_absolute_pointer_path_under_current_brain_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            db = root / "areas/lk/sub-areas/stock/data/stock.db"
            db.parent.mkdir(parents=True)
            db.write_text("placeholder", encoding="utf-8")
            pointer = {"artifacts": {"sqlite_db": "/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/data/stock.db"}}

            result = current_db_path(pointer, root=root)

            self.assertEqual(result, db)

    def test_make_json_response_is_utf8_json(self):
        payload = make_json_response({"produto": "Tênis ABC"})
        self.assertIn('"produto": "Tênis ABC"', payload)


if __name__ == "__main__":
    unittest.main()
