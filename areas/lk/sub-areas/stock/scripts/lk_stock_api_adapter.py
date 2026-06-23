#!/usr/bin/env python3
"""Read-only Stock OS API adapter for internal LK stock lookup.

This module is intentionally small and dependency-free so Júlio's site can call a
stable HTTP/JSON contract without learning the Stock OS SQLite schema.
It reads the current Stock OS pointer and SQLite DB only; it never calls Tiny or
Shopify and never writes external systems.
"""
from __future__ import annotations

import argparse
import json
import os
import sqlite3
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, quote, urlparse

ROOT_MARKERS = ("AGENTS.md", "START-HERE.md", "MAPA.md")
DEFAULT_POINTER = Path("areas/lk/sub-areas/stock/data/lk_stock_os_current_pointer.json")
DEFAULT_LIMIT = 10
MAX_LIMIT = 50_000
READONLY_GUARDRAILS = {
    "tiny_write": 0,
    "shopify_write": 0,
    "writes_externos": 0,
    "public_availability_safe": 0,
    "availability_claim_allowed": 0,
}

BRAND_PATTERNS = (
    ("new-balance", ("new balance", " nb ")),
    ("on-running", ("on running", "on cloud", "cloudmonster", "cloudstratus", "cloudsolo")),
    ("onitsuka", ("onitsuka", "mexico 66", "otiger")),
    ("nike", ("nike", "air jordan", "jordan", "dunk", "air force", "air max", "cortez", "vomero")),
    ("adidas", ("adidas", "yeezy", "samba", "gazelle", "campus", "handball spezial")),
    ("asics", ("asics", "gel-kayano", "gel 1130", "gel-nimbus", "gel-lyte", "gt-2000")),
    ("salomon", ("salomon", "xt-6", "acs pro")),
    ("hoka", ("hoka", "clifton", "bondi", "mafate")),
    ("puma", ("puma", "speedcat", "palermo", "avanti")),
    ("autry", ("autry", "medalist")),
    ("vans", ("vans",)),
    ("converse", ("converse", "chuck taylor")),
    ("reebok", ("reebok",)),
    ("saucony", ("saucony",)),
    ("crocs", ("crocs",)),
    ("alo-yoga", ("alo yoga",)),
    ("saint-studio", ("saint studio",)),
)


def infer_brand(title: str | None) -> str:
    haystack = f" {str(title or '').lower()} "
    for brand, needles in BRAND_PATTERNS:
        if any(needle in haystack for needle in needles):
            return brand
    return "outros"


def find_brain_root(start: Path | None = None) -> Path:
    cur = (start or Path(__file__).parent).resolve()
    for candidate in (cur, *cur.parents):
        if all((candidate / marker).exists() for marker in ROOT_MARKERS):
            return candidate
    return Path.cwd().resolve()


def resolve_path(root: Path, value: str | Path) -> Path:
    path = Path(value)
    if not path.is_absolute():
        return root / path
    if path.exists():
        return path
    parts = path.parts
    if "hermes-brain" in parts:
        rel = Path(*parts[parts.index("hermes-brain") + 1 :])
        rebased = root / rel
        if rebased.exists():
            return rebased
    return path


def load_pointer(pointer_path: str | Path | None = None, root: Path | None = None) -> dict[str, Any]:
    brain_root = root or find_brain_root()
    raw_path = Path(pointer_path) if pointer_path else DEFAULT_POINTER
    path = raw_path if raw_path.is_absolute() else brain_root / raw_path
    pointer = json.loads(path.read_text(encoding="utf-8"))
    pointer["_pointer_path"] = str(path)
    return pointer


def current_db_path(pointer: dict[str, Any], root: Path | None = None) -> Path:
    brain_root = root or find_brain_root()
    try:
        value = pointer["artifacts"]["sqlite_db"]
    except KeyError as exc:
        raise RuntimeError("Stock OS pointer missing artifacts.sqlite_db") from exc
    return resolve_path(brain_root, value)


def clamp_limit(limit: int | str | None) -> int:
    try:
        parsed = int(limit) if limit is not None else DEFAULT_LIMIT
    except (TypeError, ValueError):
        parsed = DEFAULT_LIMIT
    return max(1, min(MAX_LIMIT, parsed))


def row_value(row: sqlite3.Row, key: str, default: Any = None) -> Any:
    return row[key] if key in row.keys() else default


def table_exists(con: sqlite3.Connection, table: str) -> bool:
    return bool(con.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (table,)).fetchone())


def stock_freshness_summary(db_path: Path) -> dict[str, Any]:
    con = sqlite3.connect(f"file:{db_path}?mode=ro&immutable=1", uri=True)
    con.row_factory = sqlite3.Row
    try:
        observed = con.execute(
            """
            SELECT min(source_observed_at) AS source_observed_at_min,
                   max(source_observed_at) AS source_observed_at_max
              FROM current_local_stock
             WHERE source_observed_at LIKE '20__-__-__T%'
            """
        ).fetchone()
        freshness_rows = [
            dict(row)
            for row in con.execute(
                """
                SELECT coalesce(stock_freshness, 'unknown') AS freshness, count(*) AS count
                  FROM current_local_stock
                 GROUP BY coalesce(stock_freshness, 'unknown')
                 ORDER BY count DESC, freshness ASC
                 LIMIT 12
                """
            )
        ]
        latest_sync: dict[str, Any] = {}
        if table_exists(con, "tiny_full_sync_runs"):
            row = con.execute(
                """
                SELECT run_id, started_at, finished_at, rows_scanned, rows_updated, rows_failed, rows_skipped, status
                  FROM tiny_full_sync_runs
                 ORDER BY coalesce(finished_at, started_at, run_id) DESC
                 LIMIT 1
                """
            ).fetchone()
            latest_sync = dict(row) if row else {}
        return {
            "source_observed_at_min": observed["source_observed_at_min"] if observed else None,
            "source_observed_at_max": observed["source_observed_at_max"] if observed else None,
            "latest_sync_run_id": latest_sync.get("run_id"),
            "latest_sync_started_at": latest_sync.get("started_at"),
            "latest_sync_finished_at": latest_sync.get("finished_at"),
            "latest_sync_status": latest_sync.get("status"),
            "latest_sync_rows_scanned": latest_sync.get("rows_scanned"),
            "latest_sync_rows_updated": latest_sync.get("rows_updated"),
            "latest_sync_rows_failed": latest_sync.get("rows_failed"),
            "latest_sync_rows_skipped": latest_sync.get("rows_skipped"),
            "freshness_counts": freshness_rows,
        }
    finally:
        con.close()


def movement_summary(db_path: Path) -> dict[str, Any]:
    empty = {"changed": 0, "went_to_zero": 0, "back_in_stock": 0, "went_negative": 0, "biggest_drops": []}
    con = sqlite3.connect(f"file:{db_path}?mode=ro&immutable=1", uri=True)
    con.row_factory = sqlite3.Row
    try:
        if not table_exists(con, "tiny_full_sync_item_ledger"):
            return empty
        latest = con.execute("SELECT run_id FROM tiny_full_sync_item_ledger ORDER BY id DESC LIMIT 1").fetchone()
        if not latest:
            return empty
        run_id = latest["run_id"]
        counts = con.execute(
            """
            SELECT
              sum(CASE WHEN previous_quantity IS NOT NULL AND quantity IS NOT NULL AND quantity != previous_quantity THEN 1 ELSE 0 END) AS changed,
              sum(CASE WHEN previous_quantity > 0 AND quantity = 0 THEN 1 ELSE 0 END) AS went_to_zero,
              sum(CASE WHEN coalesce(previous_quantity, 0) <= 0 AND quantity > 0 THEN 1 ELSE 0 END) AS back_in_stock,
              sum(CASE WHEN quantity < 0 THEN 1 ELSE 0 END) AS went_negative
             FROM tiny_full_sync_item_ledger
             WHERE run_id = ?
            """,
            (run_id,),
        ).fetchone()
        drops = [
            dict(row)
            for row in con.execute(
                """
                SELECT sku, handle, quantity, previous_quantity, (quantity - previous_quantity) AS delta, observed_at
                  FROM tiny_full_sync_item_ledger
                 WHERE run_id = ? AND previous_quantity IS NOT NULL AND quantity IS NOT NULL AND quantity < previous_quantity
                 ORDER BY delta ASC, sku ASC
                 LIMIT 20
                """,
                (run_id,),
            )
        ]
        return {
            "run_id": run_id,
            "changed": int(counts["changed"] or 0),
            "went_to_zero": int(counts["went_to_zero"] or 0),
            "back_in_stock": int(counts["back_in_stock"] or 0),
            "went_negative": int(counts["went_negative"] or 0),
            "biggest_drops": drops,
        }
    finally:
        con.close()


def row_to_result(row: sqlite3.Row) -> dict[str, Any]:
    local_safe = int(row["local_consult_safe"] or 0) == 1
    identity_safe = int(row["identity_resolved_safe"] or 0) == 1
    public_safe = int(row["public_availability_safe"] or 0)
    availability_allowed = int(row["availability_claim_allowed"] or 0)
    confirmed = local_safe and identity_safe
    # Internal stock control must still surface live Tiny quantities for locally
    # consultable rows even when Shopify identity is not fully resolved. Public
    # availability remains blocked by `status=nao_confirmado`,
    # public_availability_safe=0 and availability_claim_allowed=0.
    quantity = row["stock_quantity_max_observed"] if local_safe else None
    motivo = None if confirmed else "identity_not_resolved_for_public_availability" if local_safe else "local_consult_not_safe"
    title = row["title"]
    brand = infer_brand(title)
    scored_priority = row_value(row, "scored_action_priority")
    action_priority = scored_priority or "P3"
    scored_lane = row_value(row, "scored_action_lane")
    if scored_lane:
        action_lane = scored_lane
    elif not confirmed:
        action_lane = "RESOLVE_IDENTITY_BEFORE_STOCK_DECISION"
    else:
        action_lane = "NO_ACTION"
    previous_quantity = row_value(row, "previous_quantity")
    ledger_quantity = row_value(row, "ledger_quantity")
    stock_delta = None
    if previous_quantity is not None and ledger_quantity is not None:
        stock_delta = float(ledger_quantity or 0) - float(previous_quantity or 0)
    thumbnail_url = row_value(row, "thumbnail_url")
    if not thumbnail_url and row["handle"]:
        thumbnail_url = f"/api/product-thumbnail?handle={quote(str(row['handle']))}"
    return {
        "status": "confirmado" if confirmed else "nao_confirmado",
        "sku": row["sku"],
        "handle": row["handle"],
        "produto": title,
        "product_title": title,
        "title": title,
        "nome": title,
        "marca": brand,
        "brand": brand,
        "tamanho": row["size"],
        "tiny_codigo": row["tiny_codigo"],
        "tiny_id_candidates": row["tiny_id_candidates"],
        "quantity_lk_controle_estoque": quantity,
        "observed_stock_quantity": row["stock_quantity_max_observed"],
        "raw_stock_quantity_max_observed": row["stock_quantity_max_observed"],
        "stock_source": row["stock_source"],
        "stock_freshness": row["stock_freshness"],
        "source_observed_at": row["source_observed_at"],
        "canonical_status": row["canonical_status"],
        "priority": action_priority,
        "sanitation_priority": row["priority"],
        "action_priority": action_priority,
        "action_lane": action_lane,
        "operational_score": float(row_value(row, "operational_score", 0) or 0),
        "units_signal": float(row_value(row, "units_signal", 0) or 0),
        "revenue_signal": float(row_value(row, "revenue_signal", 0) or 0),
        "store_units_signal": float(row_value(row, "store_units_signal", 0) or 0),
        "demand_tier": row_value(row, "demand_tier"),
        "rupture_risk": row_value(row, "rupture_risk"),
        "signal_sources": row_value(row, "signal_sources"),
        "scored_in_stock_os": int(row_value(row, "scored_in_stock_os", 0) or 0),
        "previous_quantity": previous_quantity,
        "ledger_quantity": ledger_quantity,
        "ledger_observed_at": row_value(row, "ledger_observed_at"),
        "ledger_status": row_value(row, "ledger_status"),
        "stock_delta": stock_delta,
        "thumbnail_url": thumbnail_url or "",
        "image_url": thumbnail_url or "",
        "local_consult_safe": int(row["local_consult_safe"] or 0),
        "identity_resolved_safe": int(row["identity_resolved_safe"] or 0),
        "needs_live_tiny_confirmation": int(row["needs_live_tiny_confirmation"] or 0),
        "public_availability_safe": public_safe,
        "availability_claim_allowed": availability_allowed,
        "motivo": motivo,
        "data_quality_gap": row["data_quality_gap"],
        "action": None if confirmed else "reconfirmar via lk-stock/Tiny antes de afirmar disponibilidade",
    }


def query_rows(db_path: Path, query: str, limit: int) -> list[sqlite3.Row]:
    term = query.strip()
    like = f"%{term}%"
    select_columns = """
        SELECT c.sku, c.handle, c.title, c.size, c.tiny_codigo, c.tiny_id_candidates, c.priority,
               c.canonical_status, c.stock_quantity_sum_observed, c.stock_quantity_max_observed, c.stock_source,
               c.stock_freshness, c.source_observed_at, c.local_consult_safe,
               c.identity_resolved_safe, c.public_availability_safe,
               c.availability_claim_allowed, c.needs_live_tiny_confirmation,
               c.data_quality_gap,
               s.action_priority AS scored_action_priority,
               s.action_lane AS scored_action_lane,
               s.operational_score,
               s.units_signal,
               s.revenue_signal,
               s.store_units_signal,
               s.demand_tier,
               s.rupture_risk,
               s.signal_sources,
               CASE WHEN s.sku IS NULL THEN 0 ELSE 1 END AS scored_in_stock_os,
               l.previous_quantity,
               l.quantity AS ledger_quantity,
               l.observed_at AS ledger_observed_at,
               l.status AS ledger_status
        FROM current_local_stock c
        LEFT JOIN current_stock_scored s
          ON s.sku = c.sku AND coalesce(s.handle, '') = coalesce(c.handle, '')
        LEFT JOIN (
          SELECT item.*
            FROM tiny_full_sync_item_ledger item
            JOIN (
              SELECT sku, coalesce(handle, '') AS handle_key, max(id) AS max_id
                FROM tiny_full_sync_item_ledger
               GROUP BY sku, coalesce(handle, '')
            ) latest
              ON latest.max_id = item.id
        ) l
          ON l.sku = c.sku AND coalesce(l.handle, '') = coalesce(c.handle, '')
    """
    order_by = """
        ORDER BY
          CASE coalesce(s.action_priority, 'P3')
            WHEN 'P0' THEN 0
            WHEN 'P1' THEN 1
            WHEN 'P2' THEN 2
            ELSE 3
          END,
          CASE
            WHEN c.local_consult_safe = 1 AND c.identity_resolved_safe = 1 THEN 0
            ELSE 1
          END,
          c.sku ASC,
          c.size ASC
        LIMIT ?
    """
    con = sqlite3.connect(f"file:{db_path}?mode=ro&immutable=1", uri=True)
    con.row_factory = sqlite3.Row
    try:
        if term.lower() == "all":
            return list(con.execute(f"{select_columns} {order_by}", (limit,)))
        return list(
            con.execute(
                f"""
                {select_columns}
                WHERE c.sku = ?
                   OR c.tiny_codigo = ?
                   OR c.handle = ?
                   OR c.sku LIKE ?
                   OR c.tiny_codigo LIKE ?
                   OR c.handle LIKE ?
                   OR c.title LIKE ?
                ORDER BY
                  CASE
                    WHEN c.sku = ? THEN 0
                    WHEN c.tiny_codigo = ? THEN 1
                    WHEN c.handle = ? THEN 2
                    WHEN c.local_consult_safe = 1 AND c.identity_resolved_safe = 1 THEN 3
                    ELSE 4
                  END,
                  CASE coalesce(s.action_priority, 'P3')
                    WHEN 'P0' THEN 0
                    WHEN 'P1' THEN 1
                    WHEN 'P2' THEN 2
                    ELSE 3
                  END,
                  c.sku ASC,
                  c.size ASC
                LIMIT ?
                """,
                (term, term, term, like, like, like, like, term, term, term, limit),
            )
        )
    finally:
        con.close()


def count_matching_rows(db_path: Path, query: str) -> int:
    term = query.strip()
    like = f"%{term}%"
    con = sqlite3.connect(f"file:{db_path}?mode=ro&immutable=1", uri=True)
    try:
        if term.lower() == "all":
            return int(con.execute("SELECT count(*) FROM current_local_stock").fetchone()[0])
        return int(
            con.execute(
                """
                SELECT count(*)
                  FROM current_local_stock
                 WHERE sku = ?
                    OR tiny_codigo = ?
                    OR handle = ?
                    OR sku LIKE ?
                    OR tiny_codigo LIKE ?
                    OR handle LIKE ?
                    OR title LIKE ?
                """,
                (term, term, term, like, like, like, like),
            ).fetchone()[0]
        )
    finally:
        con.close()


def lookup_stock(
    query: str,
    *,
    pointer_path: str | Path | None = None,
    limit: int | str | None = DEFAULT_LIMIT,
) -> dict[str, Any]:
    q = (query or "").strip()
    pointer = load_pointer(pointer_path)
    db_path = current_db_path(pointer)
    safe_limit = clamp_limit(limit)
    base = {
        "query": q,
        "source": "Stock OS DB",
        "pointer_path": pointer.get("_pointer_path"),
        "db_path": str(db_path),
        "current_stage": pointer.get("current_stage"),
        "pointer_updated_at_utc": pointer.get("updated_at_utc"),
        "guardrails": READONLY_GUARDRAILS.copy(),
        "results": [],
    }
    if not q:
        return {**base, "status": "nao_confirmado", "motivo": "empty_query"}
    if not db_path.exists():
        return {**base, "status": "nao_confirmado", "motivo": "stock_os_db_missing"}

    total_count = count_matching_rows(db_path, q)
    rows = query_rows(db_path, q, safe_limit)
    results = [row_to_result(row) for row in rows]
    if not results:
        return {
            **base,
            "status": "nao_confirmado",
            "motivo": "no_local_match",
            "total_count": total_count,
            "result_count": 0,
            "truncated": False,
        }

    confirmed_any = any(item["status"] == "confirmado" for item in results)
    first = results[0]
    freshness = stock_freshness_summary(db_path)
    movements = movement_summary(db_path)
    return {
        **base,
        "status": "confirmado" if confirmed_any else "nao_confirmado",
        "freshness": first.get("stock_freshness"),
        "source_observed_at": freshness.get("source_observed_at_max") or first.get("source_observed_at"),
        "freshness_summary": freshness,
        "movement_summary": movements,
        "result_count": len(results),
        "total_count": total_count,
        "truncated": total_count > len(results),
        "results": results,
    }


def make_json_response(payload: dict[str, Any]) -> str:
    return json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)


class StockApiHandler(BaseHTTPRequestHandler):
    server_version = "LKStockOSAdapter/0.1"

    def _send_json(self, status_code: int, payload: dict[str, Any]) -> None:
        body = make_json_response(payload).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _authorized(self) -> bool:
        token = os.environ.get("LK_STOCK_API_TOKEN", "").strip()
        if not token:
            return True
        expected = f"Bearer {token}"
        return self.headers.get("Authorization") == expected

    def do_GET(self) -> None:  # noqa: N802 - BaseHTTPRequestHandler API
        if not self._authorized():
            self._send_json(401, {"status": "unauthorized"})
            return
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)
        if parsed.path == "/health":
            try:
                pointer = load_pointer(os.environ.get("LK_STOCK_API_POINTER") or None)
                db = current_db_path(pointer)
                self._send_json(
                    200,
                    {
                        "status": "ok" if db.exists() else "degraded",
                        "source": "Stock OS DB",
                        "db_exists": db.exists(),
                        "pointer_path": pointer.get("_pointer_path"),
                        "current_stage": pointer.get("current_stage"),
                        "guardrails": READONLY_GUARDRAILS.copy(),
                    },
                )
            except Exception as exc:  # pragma: no cover - defensive HTTP boundary
                self._send_json(500, {"status": "error", "error": str(exc)})
            return
        if parsed.path in {"/lookup", "/api/lk-stock/lookup"}:
            query = (params.get("q") or params.get("query") or [""])[0]
            limit = (params.get("limit") or [DEFAULT_LIMIT])[0]
            try:
                payload = lookup_stock(query, pointer_path=os.environ.get("LK_STOCK_API_POINTER") or None, limit=limit)
            except Exception as exc:  # pragma: no cover - defensive HTTP boundary
                self._send_json(500, {"status": "nao_confirmado", "motivo": "adapter_error", "error": str(exc)})
                return
            self._send_json(200, payload)
            return
        self._send_json(404, {"status": "not_found", "available_paths": ["/health", "/lookup?q=SKU", "/api/lk-stock/lookup?q=SKU"]})

    def log_message(self, format: str, *args: Any) -> None:  # noqa: A002 - inherited name
        if os.environ.get("LK_STOCK_API_ACCESS_LOG") == "1":
            super().log_message(format, *args)


def serve(host: str, port: int) -> None:
    server = ThreadingHTTPServer((host, port), StockApiHandler)
    print(f"LK Stock OS read-only adapter listening on http://{host}:{port}", flush=True)
    server.serve_forever()


def main() -> int:
    parser = argparse.ArgumentParser(description="LK Stock OS read-only API adapter")
    parser.add_argument("query", nargs="?", help="SKU, Tiny code, handle or title term to lookup")
    parser.add_argument("--pointer", help="Override Stock OS pointer path")
    parser.add_argument("--limit", default=DEFAULT_LIMIT)
    parser.add_argument("--json", action="store_true", dest="json_output", default=True)
    parser.add_argument("--serve", action="store_true", help="Run HTTP server")
    parser.add_argument("--host", default=os.environ.get("LK_STOCK_API_HOST", "127.0.0.1"))
    parser.add_argument("--port", type=int, default=int(os.environ.get("LK_STOCK_API_PORT", "8765")))
    args = parser.parse_args()
    if args.serve:
        if args.pointer:
            os.environ["LK_STOCK_API_POINTER"] = args.pointer
        serve(args.host, args.port)
        return 0
    if not args.query:
        parser.error("query is required unless --serve is used")
    print(make_json_response(lookup_stock(args.query, pointer_path=args.pointer, limit=args.limit)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
