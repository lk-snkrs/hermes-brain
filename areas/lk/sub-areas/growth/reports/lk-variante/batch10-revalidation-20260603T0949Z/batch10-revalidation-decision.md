# Curadoria LK — Batch 10 revalidation / Production decision

Timestamp UTC: 2026-06-03T10:29:08Z

## Request

Lucas asked to continue implementation and selected: revalidate Batch 10 in Dev and prepare Production approval.

## Evidence collected

### Asset API readback

- Dev theme `155065450718` snippet SHA12: `3ddbc92afb29`
- Production theme `155065417950` snippet SHA12: `6e36b5761ff3`
- Dev and Production are **not equal**.

### Batch 10 group status

- `top30-air-jordan-1-low-regular`
  - Dev marker count: 1
  - Production marker count: 1
  - 10 handles / labels / images in both.
- `top30-air-jordan-1-low-og-regular`
  - Dev marker count: 0
  - Production marker count: 0
  - Interpretation: group remains disabled/removed after semantic hotfix; should not be promoted as Batch 10.
- `top30-adidas-sambae-regular`
  - Dev marker count: 1
  - Production marker count: 1
  - 10 handles / labels / images in both.

### Live public QA samples

- AJ1 Low regular: 1 Curadoria block, short labels, no Liquid error.
- AJ1 Low OG Mocha control: 0 Curadoria block, no stale wrong OG block, no Liquid error.
- Adidas Sambae: 1 Curadoria block, short labels, no Liquid error.
- NB 530 canonical: 1 Curadoria block, `top30-nb-530`, 5 short labels, no Liquid error.

## Decision

Do **not** promote the old Batch 10 Dev asset to Production.

Reason: Production has newer anti-stale/final source than Dev (`6e36b5761ff3` vs `3ddbc92afb29`) and the surviving Batch 10 groups are already present and passing live QA in Production. Promoting the old Dev asset would risk reverting post-hotfix Production work.

## Recommended next step

Start a fresh Batch 11 from current Production source/readback, not from the stale Batch 10 Dev source.

Batch 11 workflow:

1. Parse current Production coverage.
2. Build new read-only candidate groups from live catalog/orders.
3. Prepare exact group list and Dev patch from current Production source.
4. Ask Lucas approval for Dev upload only.
5. After Dev QA, ask separate Production approval.

## Non-actions

- No Shopify write in this revalidation turn.
- No Production promotion.
- No product/price/stock/app/checkout changes.

## Rollback

No rollback needed for this turn because no write was executed.
