# Receipt — Timberwolf SEO stale public HTML recheck — 2026-06-16

## Context

After Option C PDP SEO apply, Admin readback showed 13/13 products correct. Public HTML for `tenis-new-balance-204l-timberwolf-bege` intermittently served old title/meta.

## Actions

1. Rechecked public HTML with cache-busted URLs.
2. Re-saved the approved SEO payload for the single product.
3. Verified Shopify Admin `seo` field and legacy global SEO metafields.
4. Ran 12 public HTML probes.

## Evidence

Product:

- `tenis-new-balance-204l-timberwolf-bege`

Admin product SEO:

- title: `Tênis New Balance 204L Timberwolf | LK Sneakers`
- description: `New Balance 204L Timberwolf Bege original. Silhueta retrô premium, curadoria LK, atendimento humano e compra segura em até 10x.`

Legacy global metafields:

- `global.title_tag`: matches target
- `global.description_tag`: matches target

Public probes:

- 12/12 HTTP 200
- 0 Liquid errors
- 4/12 served new target title
- 8/12 served older title: `Tênis New Balance 204L Arid Timberwolf Bege | LK Sneakers`

## Interpretation

The Shopify source of truth is corrected. The remaining discrepancy is intermittent public storefront cache/edge propagation, not a wrong Shopify SEO field.

A theme-level hard override could force the title on this handle, but that would be a production theme change for one already-correct product SEO field and is not recommended unless the stale state persists after a reasonable propagation window.

## Recommendation

Monitor again later. If stale public HTML persists, prepare a scoped theme-level override approval packet or open Shopify support/cache escalation; do not keep rewriting identical product SEO fields.

## Rollback

No additional lasting change beyond the already-approved Option C SEO update. Rollback remains the Option C `prewrite-snapshot.json`.
