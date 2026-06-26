# LK Tiny Local Stock DB Phase A Implementation Plan

> **For Hermes:** Use Superpowers + TDD. Execute task-by-task with local-only changes. No Shopify/Tiny writes, no webhook creation, no cron, no external messages.

**Goal:** Implement Phase A local from the PRD: a Tiny-derived local stock DB by SKU/tamanho, wired into the LK responder and the Shopify→Tiny dry-run processor.

**Architecture:** Add a small SQLite module as the single interface for local Tiny stock snapshots. The responder uses local DB records before broad Tiny search; when live Tiny reads happen, they update the DB. The dry-run processor updates the same DB whenever it reads Tiny for an event.

**Tech Stack:** Python stdlib, SQLite, existing LK scripts/tests.

---

## Task 1: Add RED tests for local Tiny stock DB

**Objective:** Prove the DB module contract before implementation.

**Files:**
- Create: `/opt/data/tests/test_lk_tiny_stock_local_db.py`
- Future Create: `/opt/data/scripts/lk_tiny_stock_local_db.py`

**Steps:**
1. Write tests for schema creation, upsert, fresh lookup, stale lookup, event ledger idempotency, and queue insert.
2. Run: `python3 -m unittest /opt/data/tests/test_lk_tiny_stock_local_db.py -v`
3. Expected RED: import/module failure or missing functions.

## Task 2: Implement local DB module

**Objective:** Make Task 1 pass with minimal local-only SQLite code.

**Files:**
- Create: `/opt/data/scripts/lk_tiny_stock_local_db.py`

**Steps:**
1. Implement `init_db`, `upsert_stock`, `lookup_skus`, `record_stock_event`, `enqueue_refresh`, `mark_stale`.
2. Run Task 1 tests; expected GREEN.

## Task 3: Add RED integration tests for responder fast path

**Objective:** Ensure the responder reads fresh local Tiny DB before falling back to old cache/live Tiny.

**Files:**
- Modify: `/opt/data/tests/test_lk_whatsapp_assisted_sale.py`
- Modify: `/opt/data/scripts/lk_hermes_whatsapp_responder.py`

**Steps:**
1. Add a test that patches local DB lookup to return `U9060BLK` fresh and asserts the answer uses `Tiny local snapshot` without calling live Tiny or broad Tiny.
2. Run targeted test; expected RED.

## Task 4: Integrate responder with local DB

**Objective:** Use local DB snapshots before old TTL cache/live Tiny, and upsert local DB after live Tiny results.

**Files:**
- Modify: `/opt/data/scripts/lk_hermes_whatsapp_responder.py`

**Steps:**
1. Import/load local DB module safely.
2. Add `local_stock_db_instock_variants_for_candidates`.
3. Call it before old cache path.
4. Upsert local DB after exact live Tiny and resolver reads.
5. Run responder tests; expected GREEN.

## Task 5: Add RED dry-run processor integration test

**Objective:** Ensure Shopify event dry-run updates local DB when Tiny read succeeds.

**Files:**
- Modify: `/opt/data/scripts/tests/test_lk_shopify_tiny_stock_sync_dryrun.py`
- Modify: `/opt/data/scripts/lk_shopify_tiny_stock_sync_dryrun.py`

**Steps:**
1. Add a test patching DB path/temp module behavior and fake Tiny read success.
2. Assert local DB contains the SKU after processing.
3. Run targeted test; expected RED.

## Task 6: Integrate dry-run processor with local DB

**Objective:** Update local DB and stock event ledger from dry-run event processing, with no external writes.

**Files:**
- Modify: `/opt/data/scripts/lk_shopify_tiny_stock_sync_dryrun.py`

**Steps:**
1. Import local DB module.
2. On `tiny.status == ok`, upsert stock with event metadata and record event.
3. Keep existing dry-run ledger and `write_executed=False` unchanged.
4. Run dry-run tests; expected GREEN.

## Task 7: Full verification + Brain receipt

**Objective:** Prove Phase A local is implemented and documented.

**Commands:**
- `python3 -m py_compile /opt/data/scripts/lk_tiny_stock_local_db.py /opt/data/scripts/lk_hermes_whatsapp_responder.py /opt/data/scripts/lk_shopify_tiny_stock_sync_dryrun.py`
- `python3 -m unittest /opt/data/tests/test_lk_tiny_stock_local_db.py /opt/data/tests/test_lk_whatsapp_assisted_sale.py /opt/data/scripts/tests/test_lk_shopify_tiny_stock_sync_dryrun.py -v`
- CLI smoke: `python3 /opt/data/scripts/lk_hermes_whatsapp_responder.py --ask '@Hermes cliente quer New Balance 9060 38, o que temos?' --stock-only --json-output`

**Receipt:**
- Write Brain receipt under `areas/lk/sub-areas/atendimento/receipts/` with files changed, verification, guardrails, rollback.

## Safety checklist

- No Shopify write.
- No Tiny write.
- No webhook creation.
- No cron creation.
- No WhatsApp/manual external send.
- Local SQLite only.
