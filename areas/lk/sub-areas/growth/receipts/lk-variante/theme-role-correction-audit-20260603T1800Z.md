# LK Variante — Theme Role Correction Audit

Timestamp: 2026-06-03T18:00Z
Scope: read-only Shopify Admin audit after Lucas reported that `lk-new-theme/dev` must never be the live theme and that `lk-new-theme/production` is the correct live theme.

## Read-only action performed

Queried Shopify Admin REST `themes.json` and relevant assets for:

- `155065417950` — `lk-new-theme/production`
- `155065450718` — `lk-new-theme/dev`

No Shopify writes were performed.

## Current theme roles observed

- `155065417950` — name `lk-new-theme/production` — role `main` — updated `2026-06-03T14:41:29-03:00`
- `155065450718` — name `lk-new-theme/dev` — role `unpublished` — updated `2026-06-03T14:54:17-03:00`

The previously used preview theme `156623372510` no longer appeared in the theme list, consistent with Lucas saying it was deleted.

## Relevant asset inspection

### Production/main: `155065417950`

- `sections/lk-pdp.liquid` renders `lk-variante-top30-visited-v2`
- `snippets/lk-variante-top30-visited-v2.liquid` SHA12: `eda8d824a952`
- `snippets/lk-variante-top30-visited.liquid` SHA12: `089cc730d730`
- Batch 19 sample handles inspected were absent from the main active snippet/source:
  - `nike-sb-dunk-low-prm-paisley-brown`: absent
  - `tenis-new-balance-530-white-chrome-blue-branco`: absent
  - `tenis-onitsuka-tiger-mexico-66-sd-exposed-foam-peacoat-azul`: absent
  - removed handle `nike-sb-dunk-low-club-58-gulf`: absent

### Dev/unpublished: `155065450718`

- `sections/lk-pdp.liquid` renders `lk-variante-top30-visited`
- `snippets/lk-variante-top30-visited.liquid` SHA12: `0485d33c024e`
- Batch 19 sample handles are present in dev/unpublished:
  - `nike-sb-dunk-low-prm-paisley-brown`: present
  - `tenis-new-balance-530-white-chrome-blue-branco`: present
  - `tenis-onitsuka-tiger-mexico-66-sd-exposed-foam-peacoat-azul`: present
  - removed handle `nike-sb-dunk-low-club-58-gulf`: absent

## Conclusion

Current live storefront source of truth is `lk-new-theme/production` / theme ID `155065417950`, not theme ID `155065450718`.

The prior Batch 19 source SHA `0485d33c024e` is currently on `lk-new-theme/dev` (`unpublished`), not on the currently live production theme.

Do not continue with writes. Prepare a correction packet only: compare the intended approved Curadoria groups from the dev/source receipt against the current production active snippet `lk-variante-top30-visited-v2`, produce a scoped promotion/merge plan, backup path, static QA plan, live QA plan, and request explicit Lucas approval before any production write.

## Guardrail update

Future LK theme work must verify immediately before every write:

- target theme name must be `lk-new-theme/production` for production writes;
- target theme role must be `main` for production writes;
- theme ID must be the currently observed ID at that moment, not hardcoded from a previous receipt;
- dev/preview writes require a current existing theme with role `unpublished`; if the previous preview theme was deleted, choose a fresh unpublished target only after Lucas approval.
