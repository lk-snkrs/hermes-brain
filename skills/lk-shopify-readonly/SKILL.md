---
name: lk-shopify-readonly
description: Use when Lucas asks for LK Sneakers Shopify data, order/customer/product/catalog checks, or safe read-only Shopify analysis. Enforces Doppler-only secrets, GET/query-only access, Tiny-vs-Shopify stock boundaries, and approval rules before any Shopify write or customer-facing action.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [lk-sneakers, shopify, ecommerce, read-only, doppler, lucas-cimino]
    related_skills: [doppler-secrets-operations, multiempresa-routing-lucas, lucas-chief-of-staff, lk-market-trends, lk-shopify-product-upload]
---

# LK Shopify Read-only

## Overview

Use this skill for LK Sneakers Shopify work that is safe, analytical, and read-only: checking orders, customers, products, variants, SKUs, tags, collections, source URLs, and CRM/sales signals.

This skill deliberately does **not** authorize Shopify writes. Any mutation, theme/app/admin change, customer communication, product/price/stock update, tag write, webhook change, campaign send, or destructive/admin action requires a plan, preview/rollback where applicable, and explicit Lucas approval.

## Source-of-truth rules for LK

- Shopify is the source for sales, customers, orders, product catalog/source context, tags, and part of CRM context.
- Tiny / `LK | CONTROLE ESTOQUE` is the stock truth.
- Shopify stock is not reliable enough to be treated as final stock truth.
- Availability must be variant/size-level when the user asks about produto/tamanho/SKU.
- `encomenda BR/US` status is human-curated in the Shopify order context; do not infer it blindly.
- External campaigns/messages use preview + Lucas approval before any Klaviyo, WhatsApp/Evolution, Shopify email/SMS, or customer-facing send.

## Secrets and environment

Secrets live in Doppler `lc-keys/prd`. Never print values.

Expected names:

- `SHOPIFY_STORE_URL`
- `SHOPIFY_ACCESS_TOKEN`

Known historical detail: older docs mention `SHOPIFY_ACCESS_TOKEN` as the correct token name, not `SHOPIFY_API_TOKEN`. If both exist, prefer `SHOPIFY_ACCESS_TOKEN` unless Lucas/Brain says otherwise.

Before live API work, check only existence, not values. Preferred helper if available:

```bash
/opt/data/hermes_bruno_ingest/hermes_doppler.sh exists SHOPIFY_STORE_URL SHOPIFY_ACCESS_TOKEN
```

If using Doppler directly, do not echo token values. Keep tokens in environment variables inside one shell/Python process.

## Safe read-only workflow

1. Route the task to LK, not Zipper or SPITI.
2. Identify the object and objective:
   - order(s), customer(s), product(s), variant/SKU, campaign/source, time window, collection, or tag.
3. Confirm that the requested action is read-only.
4. Confirm Doppler secret existence without printing values.
5. Use only Shopify Admin REST `GET` endpoints or Admin GraphQL `query` operations.
6. Start with a small limit/window and expand only if necessary.
7. Minimize PII in outputs. Prefer IDs, counts, SKU, status, dates, totals and aggregated patterns.
8. Cross-check with Tiny/Supabase/GA4/Meta/Klaviyo only when needed and label each source clearly.
9. Separate:
   - fact observed;
   - interpretation;
   - recommended action;
   - confidence/risk;
   - approval required.
10. If the user asks for an action that would write to Shopify or contact customers, stop at preview/plan and ask for explicit approval before executing.

## REST examples — read-only only

Use the correct shop host shape. If `SHOPIFY_STORE_URL` already includes `.myshopify.com`, do not append it again.

```bash
STORE="$(doppler secrets get SHOPIFY_STORE_URL -p lc-keys -c prd --plain)"
TOKEN="$(doppler secrets get SHOPIFY_ACCESS_TOKEN -p lc-keys -c prd --plain)"
curl -sS "https://${STORE}/admin/api/2024-01/orders.json?status=any&limit=5" \
  -H "X-Shopify-Access-Token: ${TOKEN}"
```

Product by SKU usually needs searching variants/products and then reading product details. Keep limits small first.

```bash
curl -sS "https://${STORE}/admin/api/2024-01/products.json?limit=5" \
  -H "X-Shopify-Access-Token: ${TOKEN}"
```

## GraphQL examples — query only

Allowed operation type: `query`.

Blocked operation type: `mutation`.

```graphql
query OrdersPreview($first: Int!) {
  orders(first: $first, reverse: true) {
    nodes {
      id
      name
      createdAt
      displayFinancialStatus
      displayFulfillmentStatus
      totalPriceSet { shopMoney { amount currencyCode } }
      tags
    }
  }
}
```

## Approval boundaries

Free within scope:

- Read orders/customers/products/variants/tags/collections with minimal PII.
- Produce analysis, reports, QA, anomaly checks and previews.
- Create Hermes Brain documentation, templates, checklists, and read-only scripts.

Requires Lucas approval before execution:

- Any Shopify mutation: tags, notes, customer fields, products, variants, price, stock, fulfillment, cancellation, refunds, discounts, theme, apps, webhooks, metafields, admin settings.
- Any customer-facing or team-facing external send via Shopify/Klaviyo/Evolution/WhatsApp/email/SMS.
- Any bulk export with personal data.
- Any database write, campaign edit, product/price/stock purchase decision, or automation enabling.

Requires plan + rollback + explicit approval:

- Admin/destructive operations: theme, checkout, domains, billing, app permissions, webhook creation/deletion, access tokens, production integrations.
- LK theme/CRO modifications: Lucas requires every theme change to be prepared first on the `dev` branch/dev theme, with preview/screenshots for review, before any production publish or merge.

## Approved exception pattern — product/collection SEO fields

Use only when Lucas explicitly approves previewed LK SEO improvements for Shopify product/collection SEO fields. Approval of SEO title/meta does **not** approve visible CRO.

1. Limit scope to exact approved `seo.title` and `seo.description` values.
2. Products: query `productByHandle { id handle title seo { title description } }`, then mutate `productUpdate(input: { id, seo: { title, description } })`.
3. Collections: query `collectionByHandle { id handle title descriptionHtml seo { title description } }`, then mutate `collectionUpdate(input: { id, seo: { title, description } })`.
4. Verify each object live with the same query and compare target values exactly.
5. Save JSON/Markdown rollback audit with previous SEO title/meta for every object.
6. Do not touch H1, body, `descriptionHtml`, theme/Liquid, images, price, stock, SKU, Merchant, GSC, campaigns or sends unless separately previewed and approved.

Detailed session reference lives under `lk-seo-weekly-improvement/references/approved-p1-seo-fields-execution-20260511.md`.

## Approved exception pattern — narrow Shopify product tag correction

Use only when Lucas explicitly approves a narrow product-tag write/correction in chat (for example, correcting a mistaken broad SALE tag scope). This does **not** authorize price, stock, product-title, collection, campaign, customer, theme, app, or bulk-export changes.

1. If a related background task may be running, inspect/stop/reconcile before continuing; if no process is visible locally, reconcile live Shopify state directly.
2. Query products read-only first and filter locally with explicit predicates; Shopify product search is broad and may return false positives.
3. Save a JSON backup before writes with product IDs, titles, handles, statuses, tags, and timestamp.
4. Use only `tagsAdd`/`tagsRemove` for the exact approved tag(s) and exact approved target/non-target predicate.
5. Re-query and verify both positive and negative conditions: targets have the tag; non-targets do not.
6. Save a JSON report with counts, changed products, verification result, violations, and rollback data.

Session reference: `references/shopify-product-tag-correction-20260515.md` covers the Adidas Samba Jane `SALE` correction, Doppler API fallback when the CLI is unavailable, and the pitfall that `Sambae`/`Samba OG`/`Samba LT` are not `Samba Jane`.

## Approved exception pattern — narrow Shopify navigation/menu update

Use only when Lucas explicitly asks to add/rename/remove a specific LK menu/navigation link (for example, “adicione no menubar/menu a coleção X”), and treat his direct request as approval only for that exact menu/link scope.

1. Query all Shopify menus first; do not assume `main-menu` is the live header menu.
2. For the current LK storefront, update both `mega-menu-c-pia-1` (`Mega Menu (PC)`) and `mega-menu-mobile` (`Mega Menu (MOBILE)`) when Lucas says “menubar/menu” generically.
3. Save a full JSON backup of every targeted menu before `menuUpdate`; rollback is re-applying the backed-up full `items` tree.
4. Preserve the existing nested menu tree and make only the requested link/label change. Prefer collection resource links (`type: COLLECTION`, `resourceId`) when the collection exists; avoid external-looking full HTTP links for internal collections.
5. If a menu already has a broader/incorrect label pointing to the same collection (e.g. `On Running` → `/collections/loewe-x-on-running`), normalize it instead of adding a duplicate.
6. Verify by re-querying Admin menus and checking the item under the intended parent (usually `Sneakers`) in both PC and mobile menus. Live homepage HTML may show only footer links or cached/header-loaded content, so Admin readback is primary verification.
7. Do not edit theme/Liquid, products, prices, stock, collections themselves, footer, campaigns, or apps unless separately requested/approved.

Detailed session reference: `references/shopify-navigation-menu-update-20260515.md`.

## Approved exception pattern — SKU-only Shopify normalization

Use only when Lucas explicitly approves a Shopify SKU write, e.g. “pode alterar”, after a preview/backup exists.

1. Limit scope to variant-level SKU fields; do not change price, inventory, titles, handles, products, images, collections, campaigns, customers, or Tiny.
2. Build a backup plan per variant with: product title, handle, Shopify variant ID, size/variant title, old Shopify SKU, target Tiny `codigo`, Tiny product ID/name, and rollback SKU.
3. Only write variants where:
   - Tiny `codigo` is non-empty;
   - Shopify variant is found with high confidence by product + size and/or old SKU;
   - target is truly different from the current Shopify SKU.
4. Prefer Shopify REST for this narrow mutation: `PUT /admin/api/2024-01/variants/{numeric_variant_id}.json` with body `{ "variant": { "id": <id>, "sku": "<Tiny codigo>" } }`.
5. Verify each write immediately with `GET /admin/api/2024-01/variants/{id}.json` and compare live `sku` exactly to the Tiny `codigo`, including spaces/punctuation.
6. Write an audit report with success/failure counts, skipped reasons, and rollback data before telling Lucas it is complete.

Pitfall: GraphQL `productVariantUpdate` may return no useful `productVariant.sku` in this environment even when no `userErrors` are present; for SKU-only updates, REST `PUT /variants/{id}.json` gave verifiable `200` responses and exact live SKU verification.

Detailed session reference: `references/shopify-sku-normalization-to-tiny-20260511.md`.

## Output format for Lucas

Use Portuguese. Be direct.

Recommended format:

- Veredito curto.
- Fonte(s) consultada(s).
- O que encontrei.
- Risco/incerteza.
- Ação recomendada.
- O que não fiz: writes, envios, campanha, estoque/preço/tema/admin.
- Aprovação necessária, if any. If asking Lucas to approve anything from Telegram, paste the actual preview text, fields/options, and exact approval wording inline; local Brain/JSON/CSV/MD paths are audit references only and cannot be the approval surface.

## Operationalization reference

For the stricter standard Lucas expects before calling this skill “100% installed/operational”, load `references/shopify-skill-operationalization-20260511.md`. In short: verify the runtime skill, Hermes Brain copy, Brain indexes/MAPAs, health check, secret scan, PR merge/sync, and any relevant watchdog cron state before giving a final verdict.

For LK theme/CRO preview work on Shopify dev themes, load `references/shopify-theme-dev-cro-preview-20260515.md`. It captures the safe repo→PR→dev/unpublished theme workflow: base from `origin/dev`, scope Liquid by collection/product handles, snapshot remote assets before upload, verify target theme `lk-new-theme/dev` is `unpublished`, upload only changed assets, validate preview URLs/screenshots, and never publish/merge/alter product-price-stock-campaign without separate approval. It also records Lucas's mobile-first visual loop: change dev theme, open preview, inspect/screenshot on mobile, self-correct ugly/broken layouts, then report only the validated version. For PDP mobile decision-area refinements, also load `references/pdp-mobile-decision-area-cro-20260515.md`: selected-size badge, clearer unavailable sizes, hide mobile `COMPRE JÁ` when competing with `ADICIONAR AO CARRINHO`, offset floating WhatsApp above sticky ATC, and keep `Sujeito a encomenda` acima de `Detalhes do produto`. If Lucas later explicitly approves production promotion, the same reference defines the narrow production path: verify `lk-new-theme/production` role `main`, backup under `backups/theme-production/`, upload only approved asset(s), validate the live URL without `preview_theme_id`, and avoid merging unrelated CRO branch diffs wholesale.

For small production collection-page visual hotfixes like adding icons to the benefits/trust strip, use `references/collection-trust-strip-icons-production-hotfix-20260515.md`. It captures the production-safe pattern: verify theme name/role, fetch+backup the live asset, patch only the trust-strip CSS/HTML in the live string, read back by hash/substrings, retry Asset API if a 200 response reads back stale, and validate the storefront visually.

For tiny production trustbar behavior/link hotfixes on collection/PDP (e.g. making `Loja Física / Jardins, SP` link to `/pages/loja-fisica`), use `references/theme-trustbar-link-production-hotfix-20260515.md`. It captures the safe live-asset patch pattern when the local repo has unrelated diffs: fetch live assets, backup, patch temporary live strings only, upload exact section assets, read back by substring counts, and validate with cachebusted storefront URLs.

For LK OS Stock Intelligence work where Lucas asks to resolve SKU/mapping before sourcing, load `references/lk-stock-sku-saneamento-20260511.md`. It captures the B→A workflow: resolve `sem SKU no Shopify` / `mapear SKU no Tiny` first, use Shopify GraphQL query + Tiny read-only fallback searches, then prepare Fila A preview without writes or supplier contact.

For the approved SKU-only exception where Lucas explicitly authorizes Shopify SKU writes to match Tiny, load `references/shopify-sku-normalization-to-tiny-20260511.md`. It captures the plan/backup, REST update, exact live verification, skipped-row logic, and rollback shape.

For catalog-wide SKU normalization, load `references/catalog-wide-shopify-sku-normalization-20260511.md`. It captures full Shopify/Tiny catalog comparison, high-confidence match rules, idempotent timeout resume, large-audit secret-scan false positives, and how to report “safe divergences fixed” without implying ambiguous rows were changed.

For the post-normalization residual queue, load `references/residual-fila-b-prioritization-20260511.md`. It captures how to classify skipped variants into residual buckets, prioritize P0/P1/P2/P3 manual review, and avoid jumping to sourcing before ambiguous/no-match SKU rows are resolved.

For the P0 follow-up after live Shopify/Tiny lookup, load `references/p0-residual-correction-queue-20260511.md`. It captures the rule that Tiny size/color matches without populated `codigo` are still not safe for automatic SKU-only writes; convert the findings into a human correction queue (MD/JSON/CSV) before any Fila A/sourcing.

For the P0 Tiny code correction preview, load `references/p0-tiny-code-correction-preview-20260511.md`. It captures how to separate candidate Tiny `codigo` writes with target codes from rows that still need Lucas/Júlio to define the canonical code.

For live P0 residual follow-up, load `references/lk-p0-residual-live-lookup-20260511.md`. It captures the Shopify GET + Tiny search/detail workflow, the requirement for a unique Tiny candidate with populated canonical `codigo`, and the rule that Tiny matches without code or ambiguous size/color matches cannot move to automatic SKU-only write or sourcing.

For Shopify image enrichment in CRM/Klaviyo visual previews, load `references/shopify-image-enrichment-for-previews-20260511.md`. It captures the SKU-exact-first then product/handle fallback pattern when a queue carries a base SKU that does not exactly match Shopify variant SKUs, while keeping the operation read-only and not treating images as stock proof.

For LK sale-tag/product collection work, load `references/shopify-sale-tag-custom-collection-20260515.md`. It captures the rule that `/collections/sale` may be a manual/custom collection (`LK Sale`), so adding tag `SALE` alone may not make products appear; resolve collection type first, use GraphQL `title:*term*` candidate search with local filtering, add `collect` records for active/published products when needed, and verify collection membership via GraphQL `collectionByHandle.products` full pagination.

For LK GMC title optimization that touches Merchant ProductInput titles but must not alter visible Shopify titles, load `references/gmc-productinput-title-optimization-20260513.md`. It captures the P2B critical-title pattern (`39`/`M/m`/`Natural` as broken GMC titles), the safe shoes-with-size pilot workflow, Merchant API v1 `productAttributes.title` patch shape for dataSource `10636492695`, rollback/verification rules, and the `Item uploaded through multiple feeds` pitfall.

For the post-write blocked P0 residual decision queue, load `references/p0-blocked-residual-decision-queue-20260511.md`. It captures how to handle the final rows where Shopify SKU is blank and Tiny `codigo` is blank, or Shopify SKU exists but Tiny duplicate matches remain: produce a Lucas/Júlio decision queue, not an automatic write preview.

For the transition from SKU saneamento to commercial sourcing, load `references/lk-fila-a-sourcing-preview-20260511.md`. It captures the rule that Lucas may intentionally mark low-sales ambiguous residuals as `pending_low_sales_manual_fix_later`; exclude those rows from Fila A and produce only a read-only sourcing/reposição preview until supplier contact or purchase is explicitly approved. Correction learned 2026-05-12: do not treat broad Fila A/P1 opportunity as permission to create supplier quote messages. Commercial replenishment sourcing should start only from a sold/requested SKU/size with stockout confirmed; check Droper first, compare StockX vs GOAT only if Droper lacks it, then prepare a Noxon/Júlio task with the cheapest viable source. Hermes never buys or contacts the compras group autonomously.

For the deeper future external-price workflow, load `references/lk-external-price-intelligence-pending-20260511.md`, but apply the LK OS boundary from `lk-market-trends/references/on-demand-sourcing-sql-boundary-20260511.md`: Droper/StockX/GOAT/KicksDev are on-demand sourcing/upload references, not permanent external price full-sync tables in LK local SQL. It defines the pending/later status, comparison shape, US Men/Women size-normalization requirement, LK import-cost formula, and “cheapest viable” output definition.

For the next Fila A step after Lucas approves “validar fornecedor/lead time/margem” and “montar fila de cotação”, load `references/lk-fila-a-validation-quote-preview-20260511.md`. It captures how to compute cost ceilings for margin targets, apply lead-time gates, group supplier quote briefs by model/family, and keep quote quantity distinct from purchase approval.

For broader LK OS Data Spine work, source snapshots, freshness reports, cross-source labels (`fact_shopify`, `fact_tiny_stock`, `fact_ga4`, `platform_signal`), or Daily/Weekly CEO Briefing inputs, load `lk-data-spine-readonly` instead of treating it as a Shopify-only task. Shopify read-only remains one source inside the Data Spine; Tiny freshness and platform reconciliation belong to that broader skill.

For LK `needs_data` or SKU/data blocker cleanup, use `lk-data-spine-readonly` plus `references/needs-data-autofix-readonly-20260512.md`. Shopify read-only lookup is allowed autonomously for reconciliation, but it does not authorize Shopify/Tiny writes, sourcing, supplier contact, purchases, or external marketplace calls.

## Verification checklist

Before saying “100%” or “funciona”:

- [ ] I verified the relevant file/API/source, not only memory.
- [ ] If the claim is that the skill is installed/operational, I verified both the local skill path and any Hermes Brain copy/index entries that should exist.
- [ ] If the claim is about a merged Brain change, I verified health check, secret scan, PR/merge state and local sync to `origin/main`.
- [ ] Secrets were not printed, stored, or committed.
- [ ] Only GET/query operations were used.
- [ ] No customer-facing send was made.
- [ ] No Shopify write/admin/destructive action was made, **unless** Lucas explicitly approved a narrow SKU-only write and I created backup/rollback + live verification.
- [ ] If stock was involved, I did not treat Shopify stock as final truth.
- [ ] If reporting product availability, I used variant/size-level language.
- [ ] If data is live/business-critical, I stated source and timestamp.
- [ ] If I wrote code/docs, I ran syntax/health/secret checks appropriate to the change.

## Common pitfalls

0. **Product upload has its own skill.** If Lucas asks to `subir produto`, cadastrar produto, use GOAT photos/order, create product SKUs, or draft Shopify product descriptions, load `lk-shopify-product-upload`. Keep this read-only skill focused on catalog/sales/order validation unless a separately approved narrow write flow applies.

0. **Market Trends/WhatsApp intake belongs elsewhere.** If Lucas mentions LC WhatsApp `!subir`, hype, drops, sourcing trends, or “market trends”, load/use `lk-market-trends`; keep this Shopify skill focused on catalog/sales/order validation. Shopify can be a read-only validation source for Market Trends, but `!subir` is intake, not Shopify-write approval.

1. **Wrong token name.** Use `SHOPIFY_ACCESS_TOKEN`, not the historical mistaken `SHOPIFY_API_TOKEN` unless confirmed.
2. **Double `.myshopify.com`.** Some scripts expect `lk-sneakerss`; others expect `lk-sneakerss.myshopify.com`. Inspect the URL composition before calling.
3. **Skill ≠ automation.** Creating this skill does not create a cron or live sync. It only makes the safe procedure reusable.
3.1. **Runtime skill can drift from the Brain copy.** Before telling Lucas the Shopify skill is “100%”, compare `/opt/data/skills/productivity/lk-shopify-readonly/SKILL.md` against the Brain copy `skills/lk-shopify-readonly/SKILL.md` and verify the `references/` directories, not just index links. If they differ, sync the Brain copy/references from the runtime skill, create an audit report, run Brain health + diff check + changed-file secret scan, then PR/merge/sync before giving the final verdict.
4. **Shopify stock confusion.** Shopify stock is not LK stock truth; Tiny is.
5. **Platform attribution confusion.** Meta/Klaviyo platform signal is not the same as Shopify-confirmed revenue. Label ambiguity.
6. **PII over-sharing.** Do not put unnecessary customer personal data in Telegram, Brain, commits or reports.
7. **Silent success.** A script can return OK while inserting zero rows. Verify data freshness/counts when the task is about sync health.
7.1. **Local Data Spine can be stale for Shopify variant IDs.** In GMC/identifier reconciliation, if local `lk_product_variants` cannot resolve a Merchant product `link` variant ID, do not immediately call the row permanently ambiguous. A read-only Shopify Admin GraphQL `nodes(ids: [gid://shopify/ProductVariant/<legacy_id>])` probe can confirm whether the variant is live, ACTIVE and has SKU. This is evidence only; any Merchant delete/update still needs its own preview, rollback and approval.
8. **Jumping to Fila A before B.** For LK Stock Intelligence, Lucas wants B first: resolve `sem SKU no Shopify` and `mapear SKU no Tiny` before commercial sourcing/reposition previews.
9. **Tiny search false negatives.** Tiny SKU lookup may miss variants because Tiny stores spaces/punctuation differently (e.g. Shopify `1183C102751-3` vs Tiny `1183C102 751-3`) or variants have blank `codigo`. Retry with normalized/spaced SKU and product-title+size searches before declaring “not in Tiny”.
10. **Treating Tiny match as enough.** A Tiny size/color match with blank `codigo` or duplicate candidate IDs is not a safe write target. Produce a correction queue and require human/Tiny `codigo` confirmation before Shopify SKU-only preview or sourcing.
10. **Tiny candidate without `codigo` is not actionable.** In residual/P0 cleanup, a Tiny search or detail match that returns the right product/size but no canonical `codigo` still blocks automatic Shopify SKU writes and sourcing. Require a unique candidate with populated Tiny `codigo`, otherwise route to manual/Tiny canonical-code resolution first.
11. **P0 residual ≠ Fila A.** Even when a residual row overlaps sales/rupture, do a live read-only Shopify + Tiny detail lookup before commercial recommendations; no sourcing/reposition until SKU truth is confirmed.
12. **Homepage SEO is not a product/collection write.** In LK Shopify, approved product/collection SEO title/meta changes can be done via Admin GraphQL with backup + live verification, but homepage Online Store SEO title/meta is not exposed as a safe product/collection mutation. Do not edit theme/Liquid/admin settings to force homepage SEO without a separate plan + rollback.
12.1. **GMC title issue is not automatically a Shopify title issue.** For LK, duplicated or short titles across variants usually do not mean the visible Shopify product titles are wrong. Separate Shopify visible titles/SEO fields from GMC ProductInput titles. Critical GMC title fixes and shoes-with-size pilots should target Merchant API `productAttributes.title` only, with rollback/verification, and explicitly say `não alterar Shopify`. If Merchant API returns `Item uploaded through multiple feeds`, mark that item for feed/data-source triage instead of retrying blindly or changing Shopify.
13. **Collection GraphQL schema quirk.** `Collection.onlineStoreUrl` was unavailable in the Admin API version used during LK SEO execution and caused a GraphQL undefined-field error. For collection read/write verification, query `id`, `handle`, `title`, `descriptionHtml`, and `seo` unless the schema is rechecked.
14. **Tiny child variation writes have hidden payload traps.** For approved Tiny `codigo` corrections on child variations, the root wrapper must include `sequencia` inside each `produto` record; `produto.obter` may not return it, so use `sequencia: "1"` for single-record writes. Throttle writes conservatively to avoid Tiny API blocks. For apparel where the Tiny name displays `S-P`/`L-G` but grade stores `S/P`/`L/G`, including `grade` in the payload can normalize the name and violate “codigo only”; omit `grade` and preserve scalar fields, then verify no non-code changes.
15. **Pending residuals should not poison Fila A.** If Lucas says low-sales ambiguous residuals can wait, mark them explicitly (e.g. `pending_low_sales_manual_fix_later`), document the decision, and exclude them from sourcing/reposição previews. Do not keep looping on them or mix them into supplier/purchase recommendations.
16. **CRM/recompra priorities must be anchored in actual best-sellers.** When Lucas asks for CRM/RFM/recompra prioritization, do not start from generic families like Onitsuka/New Balance/Dunk unless they are derived from live order data. Rank by real `order_items` units/revenue first, then segment customers around the best-selling product they actually bought. If you use families/cohorts, label them as secondary interpretation, not the priority list.
17. **Exact SKU lookup may miss preview images.** CRM/Klaviyo visual previews often contain base SKUs while Shopify image/media belongs to variant SKUs or product records with suffixes. Try exact SKU first, then read-only product/handle/title fallback before declaring the image missing. This enriches preview visuals only; it is not stock validation and does not authorize any Shopify/Klaviyo write. See `references/shopify-image-enrichment-for-previews-20260511.md`.
18. **GMC title fixes are not automatically Shopify title fixes.** If a Merchant/GMC title appears as only a size/color/variant value (e.g. `39`, `M/m`, `Natural`), first use Shopify read-only evidence (Admin query when needed, public product `.js`, Data Spine, or handle fallback labeled low/medium confidence) to reconstruct a GMC/ProductInput preview. Do not say the visible Shopify title is wrong, and do not mutate Shopify product titles/SEO fields unless Lucas separately approves Shopify scope with before/after preview and rollback.
18.1. **SALE tag may not equal SALE collection membership.** In LK, `/collections/sale` has resolved as a custom/manual collection (`LK Sale`) in at least one session. If Lucas asks to tag products for SALE “para aparecer na coleção”, first resolve whether `sale` is smart or custom. For a custom collection, adding tag `SALE` alone is not enough; add `collect` records for active/published products and verify via GraphQL `collectionByHandle.products`, not only REST `collects` pagination. Product discovery should use Admin GraphQL search such as `title:*samba*` plus local filtering; broad REST scans/searches can miss candidates or include irrelevant matches.
19. **Theme dev preview is still a write.** Uploading Liquid/CSS/JS to `lk-new-theme/dev` is safer than production but still requires Lucas approval, a remote asset backup, exact theme name/role verification (`unpublished`), scoped route guards, PR to `dev`, and screenshot/preview validation. Never treat approval for a preview pack as approval to publish, merge, change products/prices/stock, or configure external popup/campaign tools.
20. **Do not report LK mobile theme changes before visual self-correction.** Lucas expects mobile-first validation for current LK CRO/theme iterations: alter dev, open preview, take/inspect a mobile view or user screenshot, fix visible issues (cropped CTA/text, horizontal overflow, ugly/cramped trust bars) before asking him to review. If a mobile trust bar is requested “sem scroll”, prefer either a compact 4-column single-row grid or a 2×2 grid depending on Lucas's latest preference; hide extra cards after the first four rather than allowing cut-off cards.
21. **Production theme hotfixes must preserve remote-only layout/app code.** When promoting or patching production theme assets, do not upload local `layout/theme.liquid` or other broad local assets wholesale unless you have proven the local file matches live. Fetch the live asset, backup it, patch only the target block, upload the patched live string, then read back and verify. If the local repo has uncommitted diffs or a branch that differs from production, generate patched live strings in `/tmp` from the fetched assets and upload those, not the working-tree files. Storefront HTML may remain cached per handle/route after Asset API success; verify representative live URLs actually contain the new guard/snippet before declaring the change global, using cachebuster query params when needed. Full-page screenshots can also make hidden filter drawers look open; check viewport + DOM state before reporting a blocker.
22. **Do not remove PDP trustbar to solve visual awkwardness.** For LK PDP mobile, trustbar is conversion-critical. When it looks wrong, preserve it and fix layout instead: place it after `Provador Virtual` and before `Sujeito a encomenda`, match the visual rhythm/height to the Provador card (≈52px, off-white, 1px light border), and tighten spacing consistently.
