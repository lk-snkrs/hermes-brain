# Catalog-wide Shopify SKU normalization to Tiny — 2026-05-11

## When to use

Use this reference when Lucas asks to make Shopify variant SKUs match Tiny `codigo` across more than a small manual queue. This remains a narrow approved exception to the default read-only Shopify posture.

## Proven catalog-wide workflow

1. Read full Shopify catalog via REST pagination:
   - `GET /admin/api/2024-01/products.json?limit=250&fields=id,title,handle,status,variants`
   - preserve product title, handle, variant ID, variant title/options, current SKU.
2. Read Tiny product catalog from `produtos.pesquisa.php` page-by-page.
   - Keep only rows with non-empty `codigo` as write targets.
   - Tiny is the target for SKU identity and stock truth; do not change Tiny in this flow.
3. Build indexes:
   - exact Tiny `codigo`;
   - normalized SKU: remove non-alphanumeric and uppercase;
   - normalized product name including title + size.
4. Plan only high-confidence Shopify variant updates:
   - current Shopify SKU already equals Tiny `codigo` → mark `already_exact`, no write;
   - current SKU normalized matches exactly one Tiny `codigo` → safe punctuation/spacing update;
   - normalized SKU has multiple Tiny candidates → require product title + size disambiguation;
   - blank/no Shopify SKU → allow only if product + size has one unique Tiny row with non-empty `codigo`;
   - ambiguous/no match/Tiny code blank → skip, do not guess.
5. Write a plan file before or during execution with per-variant rollback:
   - Shopify product ID/title/handle;
   - numeric variant ID;
   - variant title/options/size;
   - old Shopify SKU;
   - target Tiny `codigo`;
   - Tiny product ID/name/situation;
   - match reason;
   - rollback SKU.
6. Execute SKU-only writes via REST `PUT /variants/{id}.json` and verify each row with `GET /variants/{id}.json`.
7. Make the execution idempotent/resumable:
   - before each write, GET the current live SKU;
   - if it already equals target, count as `resumed_already_applied`/verified, not failure;
   - this protects against command timeouts after partial completion.
8. Record final counts: catalog size, Tiny rows, planned, verified, failed, already exact, skipped by safety reason, and match-reason distribution.

## Session result to remember

Catalog-wide run on 2026-05-11:

- Shopify read: 2,271 products / 15,041 variants.
- Tiny read: 18,001 products / 15,746 with non-empty `codigo`.
- Already exact before writes: 13,254 variants.
- Planned/verified updates: 505 variants.
- Failed: 0.
- Skipped safely: 1,282 variants.
- Match reasons: 238 normalized SKU unique, 11 normalized SKU + title/size, 256 title/size unique.
- A first long run timed out after applying some rows; the resumable executor detected 272 rows already at target and finished cleanly.

## Important pitfalls

- A large report can trigger the Brain secret scanner with false positives from innocent text/handles. In the observed run, a product handle containing `dusk-shower` matched an OpenAI secret heuristic (`sk-...` substring). Sanitize non-essential handle text in audit JSON if it causes a false positive, then rerun `brain_health_check.py` and a changed-file secret scan.
- Do not call this “all products fixed” without the skipped count. Say: all safe/high-confidence divergences were fixed; ambiguous/blank-code/no-match rows were skipped.
- Do not use Shopify stock as truth during this process; SKU identity is being aligned, stock remains Tiny.

## Reporting language for Lucas

Use a concise status:

- “Fiz para o catálogo completo nos casos seguros.”
- Give counts: read, already identical, updated/verified, failed, skipped.
- Explicitly state only variant SKU changed; no price/stock/title/handle/images/campaigns/Tiny/DB/VPS/secrets.
- Point to audit files and rollback data.
