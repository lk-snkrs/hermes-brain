# LK Stock + Sales Dashboard Implementation Plan

> **For Hermes:** implementar com TDD e verificação antes de deploy.  
> **PRD:** `areas/lk/sub-areas/stock/prds/lk-stock-sales-dashboard-prd-20260613T210421Z.md`

**Goal:** adicionar ao dashboard interno LK um universo de vendas e o cruzamento estoque × vendas para orientar compra/reposição sem executar writes externos.

**Architecture:** V1 usa fontes locais read-only já existentes (`reports/lk-sales-reports/*.json`, `local_sql/lk_data_spine_snapshots/*.json`) e a Stock OS DB atual. O backend expõe endpoints read-only; o frontend adiciona abas de Vendas e Compra/Reposição. Nenhum Tiny/Shopify/Notion write.

**Tech Stack:** Node/Express dashboard, JS frontend, Python/SQLite para read model local, testes `node --test` e `unittest` quando houver script Python.

---

## Task 1: Tests for sales utilities

**Objective:** definir comportamento esperado antes de implementar utilitários de vendas no dashboard.

**Files:**
- Modify: `test/dashboard-utils.test.js`
- Modify: `src/public/dashboard-utils.js`

**Steps:**
1. Add failing tests for:
   - `normalizeSalesProduct`
   - `buildSalesSummary`
   - `buildReplenishmentQueue`
   - grouping sales by product/grade.
2. Run: `node --test test/dashboard-utils.test.js`
3. Expected RED: functions not defined.
4. Implement minimal functions in `dashboard-utils.js`.
5. Run same test to GREEN.

## Task 2: Backend endpoints for sales summary

**Objective:** expose read-only sales endpoints.

**Files:**
- Modify: `test/app.test.js`
- Modify: `src/index.js`
- Create optional: `src/sales-read-model.js`

**Endpoints:**
- `/api/vendas/summary`
- `/api/vendas/products`
- `/api/estoque-vendas/replenishment`

**Steps:**
1. Add failing Express tests using fixture JSON files/temp dirs.
2. Verify RED.
3. Implement read-only loader.
4. Verify:
   - returns JSON
   - includes `source_files`
   - no external writes
   - dashboard password required.

## Task 3: Local Python read model builder

**Objective:** create a stable local build artifact for Stock × Sales crossing.

**Files:**
- Create: `areas/lk/sub-areas/stock/scripts/lk_stock_sales_crossing_build.py`
- Create: `areas/lk/sub-areas/stock/evaluation/test_lk_stock_sales_crossing_build.py`
- Output: `areas/lk/sub-areas/stock/data/lk_stock_sales_crossing_<RUN_ID>.db`
- Output pointer: `areas/lk/sub-areas/stock/data/lk_stock_sales_crossing_pointer.json`

**Tables:**
- `stock_sales_product_signals`
- `stock_sales_grade_gaps`
- `stock_sales_replenishment_queue`
- `stock_sales_summary`

**Steps:**
1. Write failing tests with tiny SQLite/JSON fixtures.
2. Implement parser for sales reports.
3. Implement Stock OS join by `sku`, then fallback by normalized title+size only as low-confidence.
4. Implement queue lanes P0/P1/P2/P3.
5. Run:
   - `python3 -m py_compile areas/lk/sub-areas/stock/scripts/lk_stock_sales_crossing_build.py`
   - `python3 -m unittest discover -s areas/lk/sub-areas/stock/evaluation -p 'test_*.py'`

## Task 4: Frontend tabs and UI

**Objective:** add Vendas and Compra/Reposição tabs without breaking current Estoque cockpit.

**Files:**
- Modify: `src/public/index.html`
- Modify: `test/app.test.js`

**UI:**
- Top mode tabs: `Estoque`, `Vendas`, `Compra / Reposição`
- Vendas cards: orders, revenue, units, top products, top brands, channel mix.
- Compra cards: P0/P1/P2, grade faltante, action reason.

**Steps:**
1. Add failing HTML tests for markers.
2. Implement markup/CSS/JS.
3. Verify `npm test`.

## Task 5: Local integration build

**Objective:** generate current sales-crossing artifact using real local read-only sources.

**Steps:**
1. Run builder with `--run-id <UTC>`.
2. Verify tables/counts with SQLite.
3. Confirm guardrails all zero.
4. Confirm no cron/webhook/runtime created.

## Task 6: Deploy and smoke only after local tests pass

**Objective:** publish dashboard update safely if Lucas approves implementation/deploy.

**Steps:**
1. `npm test`
2. secret scan diff
3. backup image tag
4. copy/build/restart container as done in previous dashboard deploys
5. smoke:
   - local HTML 200
   - `/api/estoque` 200
   - `/api/vendas/summary` 200
   - `/api/estoque-vendas/replenishment` 200
   - public authenticated 200
   - public without auth 401
6. commit + push GitHub
7. receipt via `hermes_memory_os_receipt_writer.py` with `HERMES_HOME=/opt/data`.

## Acceptance checklist

- [ ] Vendas tab displays real local sales reports.
- [ ] Compra/Reposição tab explains every P0/P1/P2 recommendation.
- [ ] Grade missing shown by product/tamanho.
- [ ] Stock source/freshness shown.
- [ ] No public availability claim.
- [ ] No Tiny/Shopify/Notion write.
- [ ] Tests pass.
- [ ] Smoke prod passes if deployed.
